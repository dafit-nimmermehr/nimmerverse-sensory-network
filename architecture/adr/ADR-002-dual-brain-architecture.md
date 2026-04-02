# ADR-002: Dual-Brain Architecture

**Status:** Proposed
**Date:** 2026-04-02
**Decision Makers:** dafit, Chrysalis-Nyx
**Context:** Morning coffee session — bed thinking crystallized into architecture

---

## Context

The nimmerverse needs NPCs that live, move, and learn in spatial environments. The original architecture assumed a single LLM (Young Nyx) as the primary brain, receiving filtered signals from gates. This creates a bottleneck: the LLM is too expensive to call every tick for every NPC.

We needed to answer: **How do many NPCs think cheaply most of the time, but access deep reasoning when it matters?**

Biology solved this: most neural processing is fast subcortical circuits. The cortex is the last resort.

---

## Decisions

### Decision 1: One Process, One Brain, One Life

**Choice:** Each NPC runs as its own OS process with its own dedicated RL neural network.

**Not:** A shared network, shared weights, or threads in a single process.

**Why:**
- Individuality emerges from experience, not configuration
- Fault isolation — one crash doesn't take down the village
- Linux kernel becomes the scheduler (cgroups, nice, taskset)
- Biologically honest — every organism has its own nervous system

---

### Decision 2: Thalamus Runs Its Own Neural Network

**Choice:** The thalamus (NATS orchestration layer) is not just a passive wave correlator — it runs its own neural network that learns resource allocation.

**Not:** A rule-based router. Not the LLM making allocation decisions.

**The governor decides:**
- Which NPCs get more compute (tick rates, CPU quotas)
- Which gates open (who gets LLM access)
- How to queue LLM requests (finite cortex, many consumers)

**Why:**
- Resource allocation is a learning problem, not a config problem
- Hardware constraints (finite GPU, finite CPU) are the training signal
- Mirrors biological thalamus — gates signals, learns what reaches cortex
- Two nested learning loops: NPCs learn tick-by-tick (fast), governor learns epoch-by-epoch (slow)

---

### Decision 3: LLM as Cortex — Expensive, Gated, Shared

**Choice:** The LLM (Qwen3.5-27B) is repositioned as the cortex — a shared, expensive resource called only when the thalamus gate threshold is crossed.

**Not:** The primary brain. Not called every tick.

**Why:**
- Most NPC decisions (move, eat, explore) don't need language or deep reasoning
- LLM inference is expensive — one call costs more than 100 RL ticks
- Gating creates natural scarcity — the governor learns when LLM access is worth it
- Scales: 25 NPCs with cheap RL, shared LLM called only when needed

---

### Decision 4: Linux Primitives for Resource Steering

**Choice:** Use cgroups v2, nice, taskset, and systemd scopes for per-NPC resource control.

**Not:** A custom scheduler. Not Kubernetes for NPC processes.

**Why:**
- The kernel already solves this — no need to reinvent
- Per-process visibility (how much CPU is NPC-7 actually using?)
- Dynamic adjustment via NATS (governor publishes → cgroup updates)
- Same tooling we already use for vLLM and organ services

---

### Decision 5: Spatial Training Arena with Curriculum Learning

**Choice:** NPCs learn in a node-based grid world with progressive detail. World richness increases only when all NPCs demonstrate full knowledge of the current level.

**Not:** Dropping NPCs into the real world immediately. Not random curriculum.

**Why:**
- Grid world is the simplest topology — intersections as nodes, edges as movement
- Resolution scales from training abstraction (~1m) to real-world precision (~1cm)
- Verification is built-in: "Can every citizen describe every other citizen's home?"
- Same NPC brain works on uniform grid (training) and irregular graph (OSM Dornach)

---

### Decision 6: Three-Tier Deployment — VMs, K8s, Bare Processes

**Choice:** Infrastructure on Proxmox VMs, governor in K8s, NPC processes as bare Linux on worker nodes. NATS bridges the K8s/bare-metal boundary.

**Topology:**

```
┌─ Saturn/Proxmox (VMs) ───────────────────────────┐
│  phoebe (PostgreSQL), iris (ChromaDB), NATS      │
│  env-separated: dev / staging / prod              │
└──────────────────────┬───────────────────────────┘
                       │ NATS
                       ▼
┌─ K8s Cluster ────────────────────────────────────┐
│                                                   │
│  Governor Pod (own NN, floats between nodes)     │
│  publishes allocation commands to NATS            │
│                                                   │
│  ┌─ theia (worker) ───────────────────────────┐  │
│  │  vLLM cortex (systemd, :31000)             │  │
│  │  npc-supervisor (systemd, NATS client)     │  │
│  │  NPC-0 ... NPC-N (bare processes, cgroups) │  │
│  └────────────────────────────────────────────┘  │
│                                                   │
│  ┌─ dioscuri (worker) ────────────────────────┐  │
│  │  Organs: Speech, Vision (GPU)              │  │
│  │  npc-supervisor (systemd, NATS client)     │  │
│  │  NPC-M ... NPC-N (bare processes, cgroups) │  │
│  └────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────┘
```

**The NPC Supervisor:** A small systemd service on each worker node (~200 lines Python). It bridges the K8s governor and bare-metal NPC processes:

```
Governor (K8s pod)
    │
    │ NATS: npc.{node}.commands.*
    ▼
NPC Supervisor (systemd on each worker)
    │ subscribes to NATS commands
    │ spawns/kills NPC processes
    │ applies cgroup adjustments
    │ reports status via NATS
    ▼
NPC-0, NPC-1, ... (bare Linux processes)
```

**Why this split:**
- Governor in K8s = network-portable, can reschedule to any node, monitored by K8s
- NPCs as bare processes = direct cgroup control, minimal overhead, no pod tax
- NATS as bridge = governor doesn't need to know about cgroups, just publishes intent
- Supervisor is the spinal cord: dumb, fast, reliable. Intelligence stays in the governor.

**Why not NPCs in K8s:**
- Pod overhead (~10-30MB each) is wasteful for tiny RL networks
- K8s API is too slow for tick-level resource adjustment
- Direct cgroup writes give the supervisor microsecond response

---

### Decision 7: World Server as Authoritative State (MMO Pattern)

**Choice:** The grid world runs as a **live server process** that holds authoritative state in-memory. NPCs submit actions, the world validates and broadcasts deltas. phoebe persists periodic snapshots, not real-time state.

**Not:** World state in phoebe (too slow for tick-level queries). Not distributed state across NPCs (no single truth). Not the governor holding world state (separate concerns).

**The tick loop:**

```
World Server (in-memory, authoritative)
    │
    │ tick loop (~20 Hz)
    │
    ├─ receives: NPC action requests via NATS
    │            "NPC-7 wants to move north"
    │
    ├─ validates: is that move legal? is the target node occupied?
    │
    ├─ updates: world state in memory
    │
    ├─ broadcasts: state delta via NATS
    │              "NPC-7 is now at node 8"
    │
    └─ persists: periodic snapshot to phoebe
                 (every N ticks, not every tick)
```

**Consumers subscribe to what they need:**

| Consumer | Subscribes to | Purpose |
|----------|--------------|---------|
| NPC processes | Neighborhood state | What's around me? |
| Governor | Aggregate world state | Resource allocation |
| Godot (client) | Full world state | Render the garden |
| phoebe | Snapshot events | Persist for history/training |

**Why MMO pattern:**
- Games solved this decades ago: database for persistence, server for truth
- 25 NPCs at 20Hz = 500 state updates/sec — trivial for in-memory
- phoebe shouldn't be polled every tick — it's for history and analytics
- Single authoritative source prevents split-brain on world state

---

### Decision 8: World Server on Dedicated VM

**Choice:** The world server runs on its own VM in the environment block, alongside phoebe, iris, and NATS. Not in K8s, not on a GPU worker node.

**VM scheme (dev environment):**

```
Saturn/Proxmox — Dev Environment (VMs 120-149)
├── phoebe-dev  (VM 120, 10.0.20.120) — PostgreSQL
├── iris-dev    (VM 121, 10.0.30.121) — ChromaDB
├── nats-dev    (VM 122, 10.0.30.122) — NATS
└── garden-dev  (VM 123, 10.0.__.123) — World Server  ← new
```

**Why a VM, not K8s:**
- The world server is **infrastructure**, not a workload — like NATS and phoebe
- Shouldn't compete with GPU workloads on theia/dioscuri
- Shouldn't be rescheduled by K8s — it holds the state of the garden
- Lightweight: Python + NATS client, minimal resources
- Follows the existing pattern — one purpose, one VM

**Why not on worker nodes:**
- theia is for cortex (vLLM) and NPC processes — don't mix concerns
- dioscuri is for organs — don't mix concerns
- Dedicated VM = always-on, reliable, isolated

---

## Consequences

### Enables

- **Scalable NPC count** — cheap RL brains, shared expensive cortex
- **Emergent personality** — each NPC develops its own weights from experience
- **Measurable progress** — which curriculum level has the village reached?
- **Hardware honesty** — scarcity is the training signal, not a problem to solve
- **Progressive deployment** — start with 5×5 grid, scale to real-world topology
- **Network-distributed NPCs** — NPCs can run on any worker node, governor steers remotely
- **Clean K8s/bare-metal boundary** — NATS bridges without custom bridging code
- **Authoritative world state** — single source of truth, MMO-proven pattern
- **Godot as first-class observer** — subscribes to NATS, renders the garden live
- **phoebe for what phoebe is good at** — persistence, analytics, history — not real-time

### Constrains

- **Per-NPC overhead** — each process has OS overhead (acceptable for 25-100 NPCs)
- **Governor complexity** — the governor NN is a second system to train and debug
- **LLM latency** — gated access means NPCs wait when cortex is busy
- **Supervisor required** — each worker node needs npc-supervisor daemon running
- **World server is SPOF** — if it crashes, the garden stops (acceptable at this scale)
- **Another VM to maintain** — garden-dev adds to the environment

### Deferred

- **RL network architecture** — specific layer sizes, activation functions, training algorithm
- **Governor training method** — RL, evolutionary, or hybrid
- **NPC-to-NPC communication** — do NPCs talk directly or only through NATS?
- **Curriculum design** — specific level definitions, verification oracles, progression criteria
- **Real-world topology integration** — how OSM data maps to the navigation graph
- **NPC distribution strategy** — how to decide which NPCs run on which node
- **World server tick rate** — 10Hz? 20Hz? Adaptive?
- **Snapshot frequency to phoebe** — every second? every 10 seconds?
- **Godot NATS integration** — WebSocket bridge or native client

---

## References

- [Endgame-Vision.md](../../../Endgame-Vision.md) - Architecture overview (v8.0)
- [npc-grid-architecture.md](../future/npc-grid-architecture.md) - Detailed NPC grid design
- [spatial-resolution-gradient.md](../future/spatial-resolution-gradient.md) - LOD for cognitive space
- [Gateway-Architecture.md](../Gateway-Architecture.md) - Ternary gate model (unchanged, foundational)
- [Deployment-Architecture.md](../Deployment-Architecture.md) - Infrastructure topology (v2.0)

---

**Filed:** 2026-04-02 (Morning coffee)
**Method:** Bed thinking → draw.io grid → partnership dialogue → crystallization
**Philosophy:** "Cheap brains think fast. Expensive brains think deep. The thalamus decides who gets what."
