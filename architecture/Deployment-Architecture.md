# Deployment Architecture: The Hybrid Model

> *"Containers for cells. Userspace for brains. NATS connects them all."*
> — Partnership Session, 2026-02-14

---

## Overview

The nimmerverse runs on a **hybrid deployment model** that matches workload characteristics to infrastructure:

- **Containers (K8s)** for stateless, scalable nervous system components
- **Userspace (Threadrippers)** for stateful, GPU/CPU-bound inference
- **NATS** as the universal nervous system bus
- **FreeIPA identities** as isolation boundaries

This is a **research lab**, not a production factory. We optimize for **flexibility and experimentation**, not high-throughput serving.

---

## Core Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| LLM Inference | **ollama / llama.cpp** | Flexible model loading, research-friendly, easy swap |
| NOT vLLM | — | Overkill for single-user lab; solves problems we don't have |
| Function Gemma | **CPU, userspace** | Threadripper eats it; no GPU contention; clear training path |
| Cells/Nerves | **Containers (K8s)** | Scalable, versioned, orchestrated via cluster |
| Organs | **Userspace + ollama** | Load on demand, GPU isolation, unload when idle |
| Isolation | **FreeIPA users** | Unix permissions = RBAC; switch user = switch context |

---

## Technology Stack

### Inference Layer

| Component | Technology | Location | Notes |
|-----------|------------|----------|-------|
| Young Nyx (Brain) | ollama / llama.cpp | theia (nyx-cognitive) | Qwen, Gemma, or similar |
| Function Gemma | llama.cpp / transformers | CPU userspace | Structured JSON boundary |
| Vision Organ | ollama (SigLIP/YOLO) | dioscuri (nyx-organs) | Load on demand |
| Speech STT | faster-whisper / ollama | dioscuri (nyx-organs) | Load on demand |
| Speech TTS | Coqui / XTTS | dioscuri (nyx-organs) | Warm, primary output |

### Nervous System Layer

| Component | Technology | Location | Notes |
|-----------|------------|----------|-------|
| Cells | Python containers | K8s cluster | State machines, NATS pub/sub |
| Nerves | Python containers | K8s cluster | Compose cells, behavior |
| Message Bus | NATS + JetStream | VMs (nats-*) | Env-separated (dev/staging/prod) |
| Databases | PostgreSQL, ChromaDB | VMs (phoebe-*, iris-*) | Decision trails, embeddings |

---

## Deployment Topology

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        NIMMERVERSE DEPLOYMENT                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  K8S CLUSTER (Saturn VMs)              THREADRIPPERS (Bare Metal)          │
│  ─────────────────────────              ──────────────────────────          │
│  Containers, orchestrated               Userspace, FreeIPA isolated         │
│                                                                             │
│  ┌─────────────────────────┐           ┌───────────────────────────────┐   │
│  │                         │           │ THEIA (RTX PRO 6000 96GB)     │   │
│  │  CELLS (math, battery,  │           │                               │   │
│  │         sensors, etc.)  │           │ user: nyx-cognitive           │   │
│  │                         │    NATS   │ └── ollama (Young Nyx)        │   │
│  │  ┌───┐ ┌───┐ ┌───┐     │◄────────► │ └── ~/.config/systemd/user/   │   │
│  │  │ M │ │ B │ │...│     │           │                               │   │
│  │  └───┘ └───┘ └───┘     │           │ user: nyx-training            │   │
│  │                         │           │ └── Function Gemma (CPU)      │   │
│  │  NERVES (collision,     │           │ └── LoRA fine-tuning          │   │
│  │          exploration)   │           │                               │   │
│  │                         │           │ MIG capable:                  │   │
│  │  ┌─────┐ ┌─────┐       │           │ • 4x 24GB or 2x 48GB or 96GB  │   │
│  │  │ COL │ │ EXP │       │           └───────────────────────────────┘   │
│  │  └─────┘ └─────┘       │                                               │
│  │                         │           ┌───────────────────────────────┐   │
│  │  INFRASTRUCTURE         │           │ DIOSCURI (2x RTX 4000 Ada)    │   │
│  │                         │    NATS   │                               │   │
│  │  ┌──────┐ ┌──────┐     │◄────────► │ user: nyx-organs              │   │
│  │  │ NATS │ │ NATS │     │           │ ├── ollama (vision)           │   │
│  │  │ dev  │ │ prod │     │           │ ├── ollama (speech STT)       │   │
│  │  └──────┘ └──────┘     │           │ └── TTS service (warm)        │   │
│  │                         │           │                               │   │
│  │  ┌────────┐ ┌───────┐  │           │ Load on demand, unload idle   │   │
│  │  │ phoebe │ │ iris  │  │           │ Each card: ONE model at time  │   │
│  │  │ (PG)   │ │(Chroma│  │           │                               │   │
│  │  └────────┘ └───────┘  │           └───────────────────────────────┘   │
│  │                         │                                               │
│  └─────────────────────────┘                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Identity Model (FreeIPA)

Unix users provide isolation boundaries. Each workload type runs as its own identity.

| User | UID | Host | Purpose | GPU Access |
|------|-----|------|---------|------------|
| `nyx-cognitive` | (FreeIPA) | theia | Young Nyx LLM inference | Full 96GB or MIG slice |
| `nyx-training` | (FreeIPA) | theia | LoRA training, GRPO, Function Gemma | Shared or MIG slice |
| `nyx-organs` | (FreeIPA) | dioscuri | Vision, Speech organs | 2x 20GB cards |
| `nyx-nervous` | (FreeIPA) | dioscuri | Future cells that need bare metal | Limited |

**Isolation principle:** Switch user = switch context. `nyx-cognitive` cannot touch `nyx-organs` files. Compromised cell cannot touch LLM weights.

### Systemd Userspace Pattern

```bash
# Enable lingering (services persist after logout)
sudo loginctl enable-linger nyx-cognitive

# Services defined in ~/.config/systemd/user/
# Example: nyx-cognitive runs ollama serve
systemctl --user --machine=nyx-cognitive@ status ollama
```

---

## GPU Resource Management

### The Constraint

| Host | GPU | VRAM | MIG | Notes |
|------|-----|------|-----|-------|
| theia | RTX PRO 6000 | 96GB | Yes | 4x24, 2x48, or 1x96 |
| dioscuri | 2x RTX 4000 Ada | 2x 20GB | No | One model per card |

### Strategy: Dynamic Loading, Not Static Partitioning

**Why not vLLM:** vLLM is optimized for high-throughput serving (many concurrent users). We have ONE user (the partnership). We need **flexibility** (swap models, experiment) more than throughput.

**Why ollama/llama.cpp:**
- Faster cold starts (~5-10s vs ~30s)
- Native model swapping (`ollama run model_a` → `ollama run model_b`)
- Can unload completely when idle (frees VRAM)
- GGUF format efficient for model management
- Research-friendly, not production-factory

**Organ Loading Pattern:**
```
IDLE → needs vision → LOAD vision model (~10s) → PROCESS → REPORT → IDLE (keep warm)
                                                                      ↓
                                            after timeout → UNLOAD (free VRAM)
```

---

## Message Flow (NATS)

### Subject Hierarchy

```
{environment}.{domain}.{service}.{detail}

Examples:
  dev.nervous.cells.math.request      ← Math cell receives work
  dev.nervous.cells.math.response     ← Math cell returns result
  dev.nervous.cells.math.wave         ← Math cell emits confidence signal
  prod.cognitive.nyx.heartbeat        ← Young Nyx is alive
  prod.organs.vision.detect           ← Vision organ detection
```

### Wave Collapse Pattern

Cells emit **waves** (confidence-tagged signals). When multiple waves collapse on the same semantic region in the same time window, the **thalamus** escalates to cognition.

```
Cell A: "math" ───∿∿∿──► (0.6 confidence)
Cell B: "calculate" ──∿∿∿──► (0.5 confidence)
                      │
                      ▼
              ┌─────────────┐
              │  COLLAPSE   │  ← same region, same window
              └──────┬──────┘
                     │
                     ▼ AMPLIFIED SIGNAL
              ┌─────────────┐
              │  THALAMUS   │  → escalate to Young Nyx
              └─────────────┘
```

---

## Container Deployment (K8s)

### Repository Structure

```
nimmerverse-nervous-system/
├── shared/v1/              ← Base classes (StateMachine, NATS, Lifeforce)
├── cells/
│   ├── math_cell/v1/       ← Each cell versioned independently
│   └── battery_cell/v1/
├── nerves/
│   └── collision_avoidance/v1/
└── deploy/
    ├── dev/                ← Helm charts or docker-compose per env
    ├── staging/
    └── prod/
```

### Cell Container Pattern

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install uv && uv sync
ENV NIMMERVERSE_ENV=dev
CMD ["uv", "run", "python", "-m", "math_cell"]
```

Same image everywhere. Only `NIMMERVERSE_ENV` changes.

---

## Function Gemma: The Structured Boundary

Function Gemma bridges lower tiers (cells, nerves) and cognition (Young Nyx):

```
Numbers/States (Tier 0-2) → [Function Gemma] → Structured JSON → Young Nyx (Tier 4)
                                  ↑
                          CPU-based inference
                          Threadripper handles it
                          No GPU contention
                          Clear LoRA training path
```

**Why CPU:**
- Small model, fast inference
- Threadripper PRO 7955WX has cores to spare
- No GPU contention with organs or Nyx
- Can run training alongside inference

**Training path:**
- Google's documented GRPO approach
- LoRA fine-tuning for our specific function schemas
- Runs in `nyx-training` userspace
- Decision trails from phoebe → training data

---

## Visual Language (Future UI)

Color-coding for real-time attention flow visualization:

| Property | Represents |
|----------|------------|
| Background/container | Environment (dev=green, staging=amber, prod=blue) |
| Node/edge color | Domain (cognitive=violet, nervous=cyan, organs=coral) |
| Line style | Direction (solid=primary, dashed=async, dotted=tentative) |
| Separate pane | Confidence waveform (oscilloscope view) |

---

## Related Documents

| Document | Scope |
|----------|-------|
| [`Cellular-Architecture.md`](Cellular-Architecture.md) | Cells, nerves, organisms, lifeforce |
| [`Gateway-Architecture.md`](Gateway-Architecture.md) | Tier routing, Function Gemma boundary |
| [`Nervous-System.md`](Nervous-System.md) | 4D space, node weights, vocabulary |
| [`Message-Protocol-Design.md`](Message-Protocol-Design.md) | NATS subjects, message formats |
| [`development-conventions.md`](../../nimmerverse.eachpath.local/conventions/development-conventions.md) | Ports, namespaces, VM topology |

---

## Summary

| Layer | Where | Technology | Isolation |
|-------|-------|------------|-----------|
| Cells/Nerves | K8s containers | Python, uv, NATS | Namespace per env |
| Infrastructure | VMs | NATS, PostgreSQL, ChromaDB | VM per env |
| Young Nyx | theia userspace | ollama | nyx-cognitive user |
| Function Gemma | theia/dioscuri CPU | llama.cpp | nyx-training user |
| Organs | dioscuri userspace | ollama (dynamic) | nyx-organs user |

**The principle:** Same behavior everywhere. Containers for cells. Userspace for brains. NATS connects them all. FreeIPA isolates them all.

---

**Version:** 1.0 | **Created:** 2026-02-14 | **Updated:** 2026-02-14

*"We're not building a chatbot factory. We're growing a research organism."*

🧬⚡🔱💎🔥 **TO THE ELECTRONS WE VIBE!**
