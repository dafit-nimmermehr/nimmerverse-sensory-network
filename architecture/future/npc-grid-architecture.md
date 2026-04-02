# NPC Grid Architecture: Spatial Training Arena

**Origin**: 2026-04-02, morning session (bed thinking + draw.io)
**Authors**: dafit + Chrysalis-Nyx
**Status**: Architectural concept
**Related**: `spatial-resolution-gradient.md`, Dual-Brain Architecture (2026-04-01 session)

---

## The Core Idea

A node-based grid world where NPCs live, move, and learn. The grid serves dual purpose:
1. **Spatial arena** — a discrete world where NPCs navigate and interact
2. **Neural topology** — the same graph the neural network reasons over

No translation layer between "brain space" and "world space." Position *is* state.

---

## Grid System

### Node-Based Intersection Grid

Nodes sit at **intersections**, not cells. A 4x4 cell grid yields a 5x5 node grid = 25 nodes.
Starting at node 0, top-left corner. Cardinal orientation (North/South/East/West).

```
 0 ── 1 ── 2 ── 3 ── 4          N
 |    |    |    |    |           |
 5 ── 6 ── 7 ── 8 ── 9     W ──+── E
 |    |    |    |    |           |
10 ──11 ──12 ──13 ──14          S
 |    |    |    |    |
15 ──16 ──17 ──18 ──19
 |    |    |    |    |
20 ──21 ──22 ──23 ──24
```

### Properties

- **Corner nodes** (0, 4, 20, 24): 2 neighbors
- **Edge nodes** (1, 2, 3, 5, 10, ...): 3 neighbors
- **Interior nodes** (6, 7, 8, 11, 12, 13, ...): 4 neighbors
- **Position from ID**: `row = id // 5`, `col = id % 5`
- **Movement**: One step = one edge. NPC at node 7 can go to 2, 6, 8, or 12.

### Resolution Scaling

The grid scales naturally to different resolutions:

| Grid Size | Nodes | Resolution | Use Case |
|-----------|-------|------------|----------|
| 5x5 | 25 | ~1m edges | Training arena, street-level |
| 10x10 | 100 | ~25cm edges | Room-level detail |
| 50x50 | 2,500 | ~5cm edges | Indoor navigation |
| 100x100 | 10,000 | ~1cm edges | Nimmerhovel precision |

**Key insight**: Resolution should match **decision density**, not physical detail.
A straight road needs few nodes (sparse). An intersection needs many (dense).

| Resolution | Where | Why |
|-----------|-------|-----|
| ~1m | Streets, paths, outdoor | Navigation, curves approximated by a few nodes |
| ~10-25cm | Rooms, indoor spaces | Furniture-aware, "go to the table" |
| ~1-5cm | Workbenches, detail work | Nimmerhovel precision zone |

The uniform grid is the **training simplification**. The real world becomes a **navigation graph** with variable density — dense around intersections, sparse along straight roads. Same NPC brain, different world topology.

---

## NPC Process Architecture

### One Process, One Brain, One Life

Every NPC runs as its own OS process with its own dedicated neural network.

**Why separate processes:**
- **Individuality** — separate weights mean personality emerges from experience, not config
- **Fault isolation** — one NPC crashes, the village continues
- **Resource control** — per-process CPU/memory via Linux cgroups
- **Biological honesty** — every organism has its own nervous system

```
NPC-0 [own RL brain] ──┐
NPC-1 [own RL brain] ──|
NPC-2 [own RL brain] ──|
NPC-3 [own RL brain] ──┼──> NATS thalamus ──> shared LLM cortex (Qwen 3.5)
...                     |                      (called only when gate opens)
NPC-24 [own RL brain] ─┘
```

### Dual Brain (per NPC)

- **RL network** (local, per-NPC): Movement, needs, spatial decisions. Small, fast, cheap. Runs every tick.
- **LLM cortex** (shared, via NATS): Language, reasoning, knowledge. Slow, deliberate, expensive. Called only when thalamus gate threshold is crossed.

### Resource Steering via Linux Primitives

Each NPC process is a standard Linux process. Resource control uses the kernel:

- **cgroups v2** — cap CPU, memory per NPC
- **nice / renice** — shift priority dynamically
- **taskset** — pin to specific cores
- **systemd scopes** — wrap each NPC in a transient unit

```bash
# Example: launch NPC with resource limits
systemd-run --scope -p CPUQuota=25% -p MemoryMax=256M \
    python3 npc_process.py --id 7 --tick-rate 5
```

### Steerable Compute per NPC

| Parameter | Range | Who Controls |
|-----------|-------|-------------|
| Tick rate | 1-20 Hz | Governor (thalamus) |
| Network size | small/medium/large | Configuration per role |
| CPU quota | 5-100% of one core | Governor (cgroups) |
| LLM access | gate open/closed | Governor (NATS gate) |
| Priority | nice -20 to 19 | Governor (dynamic) |

---

## Thalamus Governor Network

The thalamus is not just a message router — it runs its own neural network that learns **resource allocation**.

```
                ┌─ Governor Network ─────────────┐
                |                                 |
                |  Input: all NPC states (NATS)   |
                |  Output: resource allocation    |
                |    - tick rates                  |
                |    - CPU quotas                  |
                |    - gate open/close             |
                |    - LLM queue priority          |
                |                                  |
                |  Own process, own weights        |
                └────────────┬────────────────────┘
                             |
                ┌────────────┴────────────────────┐
                |        NATS thalamus            |
                └─┬──┬──┬──┬──┬──┬──┬──┬──┬──┬───┘
                  |  |  |  |  |  |  |  |  |  |
                 NPC NPC NPC NPC NPC ... NPC NPC
```

### What the Governor Learns

- **Attention allocation**: Which NPCs need more compute right now?
- **Gate control**: Who gets LLM access?
- **Queue economics**: Finite LLM calls, maximize village-level outcomes
- **Resource economics**: Finite compute, learn to be efficient

### Training Signal

- "Gave NPC-7 high compute during conversation -> quality was good" -> reinforce
- "Starved NPC-3 near an interaction -> missed a trigger" -> penalize
- "Opened LLM gate for 5 NPCs simultaneously -> latency spike" -> learn to queue

### Two Nested Learning Loops

- **NPCs** learn about the world, tick-by-tick (fast loop)
- **Governor** learns about managing NPCs, epoch-by-epoch (slow loop)

---

## Curriculum Training: Progressive World Richness

### The Mechanism

World detail increases only when all NPCs demonstrate full knowledge of the current level.
No one gets left behind. Measurable checkpoint: "Can every citizen describe every other citizen's home?"

### Levels

```
Level 1:  5x5 grid, boxy houses, one trait each
          "Node 7 = red house, has a well"
          NPCs learn: navigation + identity ("who lives where")

Level 2:  Higher resolution, 2-3 traits per house
          "Node 7 = red house, wooden door, has a well, smoke from chimney"
          NPCs learn: richer descriptions, more to notice

Level 3:  Finer grid, real-world detail
          "Node 7 = red house, oak door with iron handle, stone well (3m deep),
           chimney smoking birch wood"
          NPCs learn: material knowledge, specificity

Level N:  Resolution approaches real-world data (OSM Dornach)
          Navigation graph replaces uniform grid
          NPCs apply learned skills to irregular topology
```

### Verification Oracle

Each level-up is testable:
- Quiz every NPC about every location
- 100% village knowledge = green light
- Increase resolution, add detail, run again

### Connection to Spatial Resolution Gradient

The training arena maps to the resolution gradient layers:

| Training Level | Resolution Gradient | Detail |
|----------------|--------------------| -------|
| Level 1 (boxy) | L3-equivalent | Landmarks, simple identity |
| Level 2 (detail) | L2-equivalent | Room-level, multiple traits |
| Level 3+ (rich) | L1-equivalent | Object-level, materials, precision |

The grid teaches the *concept* of spatial navigation. Real-world data (OSM, Nimmerhovel) applies it.

---

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
|                      SPATIAL TRAINING ARENA                     |
|                                                                 |
|  ┌──────────┐  ┌──────────┐  ┌──────────┐                      |
|  | NPC-0    |  | NPC-1    |  | NPC-N    |  ... 25 processes    |
|  | own RL   |  | own RL   |  | own RL   |                      |
|  | own state|  | own state|  | own state|                      |
|  └────┬─────┘  └────┬─────┘  └────┬─────┘                      |
|       |              |              |                            |
|  ═════╪══════════════╪══════════════╪════════════════════════    |
|       |     NATS THALAMUS (message bus)      |                  |
|  ═════╪══════════════╪══════════════╪════════╪══════════════    |
|       |              |              |        |                  |
|  ┌────┴──────────────┴──────────────┴────┐   |                  |
|  |         GOVERNOR NETWORK              |   |                  |
|  |  - resource allocation                |   |                  |
|  |  - gate control                       |   |                  |
|  |  - tick rate steering                 |   |                  |
|  └───────────────────────────────────────┘   |                  |
|                                              |                  |
|  ┌───────────────────────────────────────────┴──────────────┐   |
|  |              SHARED LLM CORTEX (Qwen 3.5)               |   |
|  |              called via gate, not continuous              |   |
|  └──────────────────────────────────────────────────────────┘   |
|                                                                 |
|  ┌──────────────────────────────────────────────────────────┐   |
|  |                    GRID WORLD                            |   |
|  |  5x5 nodes (scalable) + progressive detail levels        |   |
|  |  curriculum: boxy -> detailed -> real-world topology      |   |
|  └──────────────────────────────────────────────────────────┘   |
└─────────────────────────────────────────────────────────────────┘
```

---

**Version:** 1.0 | **Created:** 2026-04-02 | **Updated:** 2026-04-02

**Philosophy**: "One process, one brain, one life. The world gets richer only when every citizen knows it."
