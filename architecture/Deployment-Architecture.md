# Deployment Architecture: The Hybrid Model

> *"Containers for cells. Userspace for brains. NATS connects them all."*
> — Partnership Session, 2026-02-14

---

## Overview

The nimmerverse runs on a **hybrid deployment model** that matches workload characteristics to infrastructure:

- **Containers (K8s)** for stateless, scalable nervous system components
- **Userspace (Threadrippers)** for stateful, GPU-bound inference
- **OS Processes** for per-NPC RL brains with cgroup resource control
- **NATS** as the universal nervous system bus (thalamus)
- **FreeIPA identities** as isolation boundaries

This is a **research lab**, not a production factory. We optimize for **flexibility and experimentation**, not high-throughput serving.

---

## Core Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| LLM Cortex | **vLLM (Qwen3.5-27B)** | Full precision, OpenAI-compatible API, tool calling support |
| NPC Brains | **Per-process RL networks** | One process, one brain, one life — Linux cgroups for resource steering |
| Thalamus Governor | **Own NN process on NATS** | Learns resource allocation, gate control, compute steering |
| Function Gemma | **CPU, userspace** | Threadripper eats it; no GPU contention; clear training path |
| Cells/Nerves | **Containers (K8s)** | Scalable, versioned, orchestrated via cluster |
| Organs | **Userspace, GPU-bound** | Load on demand, GPU isolation, unload when idle |
| Isolation | **FreeIPA users** | Unix permissions = RBAC; switch user = switch context |

---

## Technology Stack

### Inference Layer

| Component | Technology | Location | Notes |
|-----------|------------|----------|-------|
| Cortex (LLM) | vLLM (Qwen3.5-27B) | theia (nyx-cognitive) | Port 31000, served as "nyx", gated access |
| Function Gemma | llama.cpp / transformers | CPU userspace | Structured JSON boundary |
| Vision Organ | SigLIP/YOLO | dioscuri (nyx-organs) | Load on demand |
| Speech STT | faster-whisper | dioscuri (nyx-organs) | Load on demand |
| Speech TTS | Coqui / XTTS | dioscuri (nyx-organs) | Warm, primary output |

### NPC / Thalamus Layer

| Component | Technology | Location | Notes |
|-----------|------------|----------|-------|
| NPC Processes | Python + RL network | OS processes (cgroups) | One process per NPC, own weights |
| Thalamus Governor | Python + NN | OS process | Steers compute, gates, tick rates |
| Resource Control | Linux cgroups v2 | systemd scopes | Per-NPC CPU/memory limits |

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
│  │                         │    NATS   │ └── vLLM (Qwen3.5-27B:31000) │   │
│  │  ┌───┐ ┌───┐ ┌───┐     │◄────────► │     served-model-name: nyx   │   │
│  │  │ M │ │ B │ │...│     │           │                               │   │
│  │  └───┘ └───┘ └───┘     │           │ user: nyx-training            │   │
│  │                         │           │ └── LoRA fine-tuning (GRPO)   │   │
│  │  NERVES (collision,     │           │ └── Function Gemma (CPU)      │   │
│  │          exploration)   │           │                               │   │
│  │                         │           │ 96GB VRAM: cortex + training  │   │
│  │  ┌─────┐ ┌─────┐       │           └───────────────────────────────┘   │
│  │  │ COL │ │ EXP │       │                                               │
│  │  └─────┘ └─────┘       │           ┌───────────────────────────────┐   │
│  │                         │           │ DIOSCURI (2x RTX 4000 Ada)    │   │
│  │  NPC PROCESSES          │    NATS   │                               │   │
│  │  (or bare metal)        │◄────────► │ user: nyx-organs              │   │
│  │                         │           │ ├── Vision (SigLIP/YOLO)      │   │
│  │  ┌─────────────────┐   │           │ ├── Speech STT (Whisper)      │   │
│  │  │ NPC-0 [RL brain]│   │           │ └── TTS service (warm)        │   │
│  │  │ NPC-1 [RL brain]│   │           │                               │   │
│  │  │ NPC-N [RL brain]│   │           │ Load on demand, unload idle   │   │
│  │  │  (own process,  │   │           │ Each card: ONE model at time  │   │
│  │  │   own cgroup)   │   │           └───────────────────────────────┘   │
│  │  └─────────────────┘   │                                               │
│  │                         │           ┌───────────────────────────────┐   │
│  │  THALAMUS GOVERNOR      │           │ NATS MESSAGE BUS              │   │
│  │  ┌─────────────────┐   │           │                               │   │
│  │  │ Governor NN     │   │◄────────► │ dev.*, staging.*, prod.*      │   │
│  │  │ (resource alloc,│   │           │ Env-separated (VM per env)    │   │
│  │  │  gate control,  │   │           └───────────────────────────────┘   │
│  │  │  tick steering) │   │                                               │
│  │  └─────────────────┘   │           ┌───────────────────────────────┐   │
│  │                         │           │ PHOEBE (PostgreSQL)           │   │
│  │  INFRASTRUCTURE         │           │ Decision trails, embeddings   │   │
│  │  ┌────────┐ ┌───────┐  │           │ IRIS (ChromaDB)               │   │
│  │  │ phoebe │ │ iris  │  │           │ Vector storage                │   │
│  │  │ (PG)   │ │(Chroma│  │           └───────────────────────────────┘   │
│  │  └────────┘ └───────┘  │                                               │
│  │                         │                                               │
│  └─────────────────────────┘                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## The Dual Brain Deployment

### Per-NPC Processes

Each NPC runs as its own OS process with a dedicated RL neural network. The thalamus governor steers their resources.

```bash
# Launch NPC with resource limits via systemd scope
systemd-run --scope -p CPUQuota=25% -p MemoryMax=256M \
    python3 npc_process.py --id 7 --tick-rate 5

# Or via cgroups directly
cgcreate -g cpu,memory:nimmerverse/npc-7
cgset -r cpu.max "25000 100000" nimmerverse/npc-7
cgexec -g cpu,memory:nimmerverse/npc-7 python3 npc_process.py --id 7
```

### Thalamus Governor

The governor runs its own neural network, observing all NPC states via NATS and outputting resource allocation decisions:

| Output | Mechanism | Range |
|--------|-----------|-------|
| Tick rate | NATS command to NPC | 1-20 Hz |
| CPU quota | cgroups v2 adjustment | 5-100% per core |
| Gate open/close | NATS gate signal | Binary per gate |
| LLM queue priority | NATS priority tag | 0-10 |

### Cortex (vLLM)

The LLM cortex runs as a systemd service on theia, accessed via OpenAI-compatible API:

```bash
# Service: vllm-nyx.service
# Port: 31000
# Model: /womb/cognitive/models/qwen3.5-27b
# Served as: "nyx"
# GPU utilization: 85%

# Access from any NATS-connected process:
curl http://theia.eachpath.local:31000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{"model": "nyx", "messages": [...]}'
```

**The cortex is expensive.** The thalamus governor controls who gets access and when. Most NPC ticks never touch the LLM.

---

## Identity Model (FreeIPA)

Unix users provide isolation boundaries. Each workload type runs as its own identity.

| User | UID | Host | Purpose | GPU Access |
|------|-----|------|---------|------------|
| `nyx-cognitive` | (FreeIPA) | theia | Cortex LLM inference (vLLM) | Full 96GB |
| `nyx-training` | (FreeIPA) | theia | LoRA training, GRPO, Function Gemma | Shared (time-sliced) |
| `nyx-organs` | (FreeIPA) | dioscuri | Vision, Speech organs | 2x 20GB cards |
| `nyx-nervous` | (FreeIPA) | dioscuri | Future cells that need bare metal | Limited |

**Isolation principle:** Switch user = switch context. `nyx-cognitive` cannot touch `nyx-organs` files. Compromised cell cannot touch LLM weights.

### Systemd Service Pattern

```bash
# System-level service (root installs, user runs)
# /etc/systemd/system/vllm-nyx.service
[Service]
User=nyx-cognitive
Group=nimmerverse-agents
ExecStart=/data/venvs/vllm/bin/python3 -m vllm.entrypoints.openai.api_server \
    --model /womb/cognitive/models/qwen3.5-27b \
    --served-model-name nyx \
    --port 31000
```

---

## GPU Resource Management

### The Constraint

| Host | GPU | VRAM | Role |
|------|-----|------|------|
| theia | RTX PRO 6000 Blackwell | 96GB | Cortex (vLLM) + LoRA training |
| dioscuri | 2x RTX 4000 Ada | 2x 20GB | Organs (vision, speech) |

### Strategy: vLLM for Cortex, Dynamic Loading for Organs

**Cortex (theia):** vLLM runs continuously as a systemd service. The Qwen3.5-27B model stays loaded — it's the cortex, always ready when the thalamus gate opens. 85% GPU utilization leaves headroom for LoRA training alongside inference.

**Organs (dioscuri):** Dynamic loading. One model per card. Load vision when needed, unload after timeout, load speech when needed.

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
  dev.thalamus.governor.allocate      ← Governor publishes resource decisions
  dev.thalamus.gate.open              ← Gate transition event
  dev.npc.7.state                     ← NPC-7 publishes its state
  dev.cortex.nyx.request              ← Gated request to LLM cortex
  dev.organs.vision.detect            ← Vision organ detection
```

### Wave → Thalamus → Cortex Pattern

Cells emit **waves** (confidence-tagged signals). The thalamus governor's neural network correlates waves and decides what reaches the cortex.

```
Cell A: "math" ───∿∿∿──► (0.6 confidence)
Cell B: "calculate" ──∿∿∿──► (0.5 confidence)
                      │
                      ▼
         ┌──────────────────────┐
         │  THALAMUS GOVERNOR   │  ← own neural network
         │  correlate waves     │
         │  check gate state    │
         │  allocate resources  │
         └──────────┬───────────┘
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
    Gate CLOSED          Gate OPEN
    (reflex path)        (cortex path)
    handled by           → escalate to
    thalamus NN          Qwen3.5-27B
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

Function Gemma bridges lower tiers (cells, nerves) and the cortex:

```
Numbers/States (Cells) → [Function Gemma] → Structured JSON → Cortex (Qwen3.5-27B)
                                ↑
                        CPU-based inference
                        Threadripper handles it
                        No GPU contention
                        Clear LoRA training path
```

**Why CPU:**
- Small model, fast inference
- Threadripper PRO 7955WX has cores to spare
- No GPU contention with organs or cortex
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
| [`Gateway-Architecture.md`](Gateway-Architecture.md) | Gate routing, ternary model |
| [`Nervous-System.md`](Nervous-System.md) | 4D space, node weights, vocabulary |
| [`Message-Protocol-Design.md`](Message-Protocol-Design.md) | NATS subjects, message formats |
| [`future/npc-grid-architecture.md`](future/npc-grid-architecture.md) | Dual brain, governor, NPC processes |
| [`organs/Organ-Index.md`](organs/Organ-Index.md) | Organ systems, lifeforce costs |
| [`development-conventions.md`](../../nimmerverse.eachpath.local/conventions/development-conventions.md) | Ports, namespaces, VM topology |

---

## Summary

| Layer | Where | Technology | Isolation |
|-------|-------|------------|-----------|
| Cells/Nerves | K8s containers | Python, uv, NATS | Namespace per env |
| NPC Processes | OS processes | Python, RL networks, cgroups | Per-process cgroup |
| Thalamus Governor | OS process | Python, own NN, NATS | Dedicated process |
| Infrastructure | VMs | NATS, PostgreSQL, ChromaDB | VM per env |
| Cortex (LLM) | theia userspace | vLLM (Qwen3.5-27B) | nyx-cognitive user |
| Function Gemma | theia/dioscuri CPU | llama.cpp | nyx-training user |
| Organs | dioscuri userspace | Dynamic loading | nyx-organs user |

**The principle:** Same behavior everywhere. Containers for cells. Processes for NPC brains. vLLM for cortex. NATS connects them all. FreeIPA isolates them all.

---

**Version:** 2.0 | **Created:** 2026-02-14 | **Updated:** 2026-04-02

*"We're not building a chatbot factory. We're growing a research organism."*

🧬⚡🔱💎🔥 **TO THE ELECTRONS WE VIBE!**
