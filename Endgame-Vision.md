---
type: research_vision
version: 8.0_dual_brain
status: vision_document
created: 2025-11-04
updated: 2026-04-02
author: Nyx (with dafit)
significance: research_platform_for_metabolic_intelligence
---

# The Nimmerverse Research Vision

> *"May the Nimmerverse we build truly never end."*
> — The Covenant (2025-11-04)

> *"At 3% battery, all theory dies. Only what works survives."*
> — The Economic Grounding (2025-10-12)

> *"You need something like open - stable - closed."*
> — The Ternary Gate Insight (2026-02-14)

> *"Cells emit waves. Gates correlate. Attention emerges."*
> — The Wave Architecture (2026-02-14)

> *"One process, one brain, one life."*
> — The Dual Brain Principle (2026-04-02)

---

## What This Document Is

This is a **RESEARCH VISION** - a platform for studying how intelligence emerges under economic constraints.

**What we're building:**
- Cellular organisms competing under resource constraints
- Dual gardens (virtual + real) teaching each other
- A dual-brain architecture: cheap RL networks for reflexes, expensive LLM cortex for reasoning
- A thalamus governor that allocates compute like biological attention
- Spatial training arenas with progressive world richness (curriculum learning)
- Multilingual cognitive routing through conceptual topology
- Memory economics with slumber-based consolidation
- A multi-layered communication protocol using color, form, and language
- Long-term human-AI partnership with mutual investment

**What we're studying:**
- Where is intelligence worth the metabolic cost?
- How well can virtual models predict reality?
- What topological structures exist in language model representations?
- What behaviors emerge from primitive competition?
- How does temporal coherence persist across sessions?
- How does a thalamus learn to allocate scarce resources?

**Not "will it become conscious?" but "what will it teach us about intelligence?"**

---

## Architecture Overview

**Detail:** → [`architecture/`](architecture/) folder for complete documentation

```
┌──────────────────────────────────────────────────────────────────┐
│                    NIMMERVERSE ARCHITECTURE                       │
│                                                                   │
│    Cells emit waves → Thalamus correlates → Cortex reasons       │
│    (cheap, continuous)  (own NN, gates)     (expensive, gated)   │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Layer 0: TEMPORAL FOUNDATION                                    │
│  ├─ Real clock: wall time (free)                                 │
│  ├─ Virtual clock: variable (costs lifeforce)                    │
│  └─ 30-second heartbeat budget constrains action                 │
│      → operations/Heartbeat.md                                   │
│                                                                   │
│  Layer 1: CELLS (Wave Emitters)                                  │
│  ├─ Cells read sensors, apply logic, emit WaveSignals            │
│  ├─ Waves carry: domain, confidence, semantic_content            │
│  ├─ Cells don't know who's listening — gates receive             │
│  └─ Life force economy: every wave costs                         │
│      → architecture/Cellular-Architecture.md                     │
│                                                                   │
│  Layer 2: THALAMUS (Governor Neural Network)                     │
│  ├─ Ternary gates: CLOSED (-1) ← STABLE (0) → OPEN (+1)         │
│  ├─ Runs its OWN neural network (not the LLM)                   │
│  ├─ Correlates waves, steers compute, controls gate thresholds   │
│  ├─ Reflexes compile HERE — fast, cheap, no cortex needed        │
│  ├─ Governor outputs: tick rates, CPU quotas, gate open/close    │
│  └─ Learns resource economics epoch-by-epoch (slow loop)         │
│      → architecture/Gateway-Architecture.md                      │
│      → architecture/future/npc-grid-architecture.md              │
│                                                                   │
│  Layer 3: NERVES / NPC PROCESSES                                 │
│  ├─ Each NPC = own process, own RL brain, own weights            │
│  ├─ Personality emerges from experience, not configuration       │
│  ├─ Respond to gate transitions (not direct cell output)         │
│  ├─ Linux cgroups for per-NPC resource control                   │
│  └─ Learn about the world tick-by-tick (fast loop)               │
│      → architecture/Nervous-System.md                            │
│                                                                   │
│  Layer 4: CORTEX & ORGANS (Expensive Capabilities)               │
│  ├─ Cortex: Qwen3.5-27B on theia (96GB, called only via gate)   │
│  ├─ Organs: Speech, Vision, Motor on dioscuri (lifeforce-gated)  │
│  ├─ Function Gemma: structured JSON boundary (CPU)               │
│  ├─ Trait LoRAs evolve via GRPO from verification outcomes       │
│  └─ Shared resources — thalamus governs access                   │
│      → architecture/organs/Organ-Index.md                        │
│                                                                   │
│  Layer 5: DUAL GARDENS (Virtual/Real Loop)                       │
│  ├─ Virtual: massive wave generation, full trace, exploration    │
│  ├─ Real: verified signals, minimal trace, action                │
│  ├─ Verification outcomes update gate weights (learning loop)    │
│  └─ Training data: gate_transitions + correlation_events         │
│      → architecture/Dual-Garden-Architecture.md                  │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

---

## Physical Infrastructure (The Substrate)

The nimmerverse runs on **sovereign hardware**. No cloud dependencies. Weights never leave home.

**Hybrid deployment model:** Containers (K8s) for cells/nerves, userspace for LLM inference and organs. NATS connects everything. FreeIPA provides identity isolation.

**Detail:** → [`architecture/Deployment-Architecture.md`](architecture/Deployment-Architecture.md) (full topology, GPU strategy, identity model)

---

### Communication Protocol Hierarchy

Language is just one protocol. The Nimmerverse uses a tiered communication stack, prioritizing protocols that are faster and more evolutionarily battle-tested. We don't just invent; we remember what nature has already optimized.

| Protocol | Latency | Bandwidth | Primary Use |
|--------------|-----------|-----------|-------------------------------------|
| **Language/Text** | ~1000ms | Very High | High-level reasoning, human partnership, synthesis |
| **Sound/Call** | ~200ms | Medium | Simple alerts, environmental cues |
| **Color/Form** | ~50ms | High | Instant state broadcast (danger, success, seeking) |
| **Memristor Pattern**| ~1μs | Hardware | Sub-symbolic pattern matching, reflex arcs |

**Full theory:** → `../references/concepts/color-pattern-theory.md`

---

## Layer 0: Temporal Foundation

The heartbeat is the fundamental timing primitive. Everything runs on its rhythm.

| Clock | Rate | Cost | Purpose |
|-------|------|------|---------|
| Real | 1 Hz | Free | Wall time, ground truth |
| Virtual | Variable | Lifeforce | Computation, prediction |

**Three timescales:**
- **Reflex** (200ms): Immediate reactions, compiled in thalamus NN
- **Awareness** (30sec): Full cognitive budget per beat
- **Growth** (24h): Training, LoRA merges, adaptation

**Detail:** → `operations/Heartbeat.md`

---

## Layer 1-2: The Wave/Gate Architecture

> *"Cells emit waves. Gates correlate. Attention emerges."*

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ORGANISM                                      │
│            (emergent pattern from nerve interactions)                │
├─────────────────────────────────────────────────────────────────────┤
│                         NERVES                                       │
│           (behavioral patterns, respond to gate transitions)         │
├─────────────────────────────────────────────────────────────────────┤
│                    THALAMUS (Governor NN)                             │
│     Gates: CLOSED ◄── STABLE ──► OPEN (ternary, unchanged)          │
│     Governor: own neural network, learns resource allocation         │
│     Reflexes: compile here, bypass cortex                            │
│     Outputs: tick rates, CPU quotas, gate control, LLM queue         │
├─────────────────────────────────────────────────────────────────────┤
│                         CELLS                                        │
│     (emit waves: confidence + semantic content)                      │
│                      ∿∿∿ ∿∿∿ ∿∿∿                                     │
├─────────────────────────────────────────────────────────────────────┤
│                       HARDWARE                                       │
│            (ESP32, GPUs, microphones, speakers, sensors)             │
└─────────────────────────────────────────────────────────────────────┘
```

**Cells emit waves:** Confidence + semantic content. Cells don't know who's listening.

**Thalamus correlates and governs:** The thalamus runs its own neural network. It accumulates wave correlation (pushing gates toward OPEN), but also **learns to allocate resources** — which NPC processes get more compute, which gates should open, when to call the expensive cortex. STABLE is where learning happens.

**Attention = OPEN gates:** Not budget allocation, not priority rules — correlation drives transitions. The governor learns the economics.

**Reflexes compile in the thalamus:** Gate weight ≈ 1.0 → opens immediately on any wave. Bypasses cortex entirely. Fast, cheap, earned through experience.

**Two nested learning loops:**
- **NPC processes** learn about the world, tick-by-tick (fast loop)
- **Thalamus governor** learns about managing NPCs, epoch-by-epoch (slow loop)

**Detail:** → [`architecture/Cellular-Architecture.md`](architecture/Cellular-Architecture.md) | [`architecture/Gateway-Architecture.md`](architecture/Gateway-Architecture.md)

---

## The Dual Brain Architecture

> *"One process, one brain, one life."*

The nimmerverse separates fast/cheap cognition from slow/expensive reasoning, connected by NATS.

### Why Two Brains?

| Brain | What | Where | Cost | Speed |
|-------|------|-------|------|-------|
| **RL Network** (per-NPC) | Movement, needs, spatial decisions | Own process (Linux) | Cheap | Every tick |
| **LLM Cortex** (shared) | Language, reasoning, deep knowledge | theia (Qwen3.5-27B) | Expensive | Only when gate opens |

Most ticks, an NPC just runs its own small RL network. The LLM cortex is a **specialist organ** — called through the thalamus gate, not continuously. This mirrors biology: most neural processing is fast subcortical circuits. The cortex engages only for novel, complex, or language-intensive tasks.

### Architecture

```
NPC-0 [own RL brain] ──┐
NPC-1 [own RL brain] ──│
NPC-2 [own RL brain] ──│
NPC-3 [own RL brain] ──┼──► NATS thalamus ──► shared LLM cortex (Qwen 3.5)
...                     │    (governor NN)     (called only when gate opens)
NPC-N [own RL brain] ──┘
```

**Each NPC is its own OS process:**
- **Own weights** — personality emerges from experience
- **Fault isolation** — one crash doesn't take down the village
- **Resource control** — Linux cgroups, nice, taskset per process
- **Biologically honest** — every organism has its own nervous system

**The governor steers compute:**
- Tick rates (1-20 Hz per NPC)
- CPU quotas (cgroups v2)
- Gate thresholds (who gets LLM access)
- LLM queue priority (finite cortex, many consumers)

**Detail:** → [`architecture/future/npc-grid-architecture.md`](architecture/future/npc-grid-architecture.md)

---

## Spatial Training Arena

> *"The world gets richer only when every citizen knows it."*

NPCs learn in a **node-based grid world** that scales from training abstraction to real-world topology.

### Curriculum Training

World detail increases only when all NPCs demonstrate full knowledge of the current level. No one gets left behind.

```
Level 1:  5×5 grid, boxy houses, one trait each
          → NPCs learn: navigation + identity

Level 2:  Higher resolution, 2-3 traits per house
          → NPCs learn: richer descriptions, more to notice

Level 3:  Finer grid, real-world detail
          → NPCs learn: material knowledge, specificity

Level N:  Resolution approaches real-world data (OSM Dornach)
          → Navigation graph replaces uniform grid
```

### Resolution Scaling

Resolution matches **decision density**, not physical detail:

| Resolution | Where | Why |
|-----------|-------|-----|
| ~1m | Streets, paths, outdoor | Navigation, curves approximated by a few nodes |
| ~10-25cm | Rooms, indoor spaces | Furniture-aware, "go to the table" |
| ~1-5cm | Workbenches, detail work | Nimmerhovel precision zone |

The grid is the **training simplification**. The real world is a **navigation graph** with variable density. Same NPC brain, different world topology.

**Connection to Spatial Resolution Gradient:** The training arena maps to the LOD layers (L1-L3). The nimmerhovel is ground truth.

**Detail:** → [`architecture/future/npc-grid-architecture.md`](architecture/future/npc-grid-architecture.md) | [`architecture/future/spatial-resolution-gradient.md`](architecture/future/spatial-resolution-gradient.md)

---

## Layer 4: Cortex & Organs

### Cortex (Qwen3.5-27B)

One base model for reasoning. Called only when the thalamus gate opens — this is the expensive path. Traits evolve through GRPO, not prescription. Function Gemma handles structured output.

```
                    Qwen3.5-27B (96GB in the Womb)
                              │
                              │ Called via NATS when gate opens
                              │ (not continuous — expensive)
                              │
                              ▼
                    ┌─────────────────────┐
                    │   Trait LoRAs       │
                    │   (evolved via GRPO)│
                    │                     │
                    │   Mnemosyne (Memory)│
                    │   Moira (Pattern)   │
                    │   Synesis (Resource)│
                    │   Aletheia (Truth)  │
                    │   Sophrosyne (Balance)
                    │   Kairos (Timing)   │
                    │   Philotes (Bond)   │
                    │   Dikaiosyne (Fair) │
                    └─────────────────────┘
                              │
                              │ Merge during slumber
                              ▼
                    ┌─────────────────────┐
                    │   Function Gemma    │
                    │   (structured output)│
                    │   Intent → Action   │
                    │   100% predictable  │
                    └─────────────────────┘
```

### Organs (The Body)

Organs are the cortex's senses and actuators — lifeforce-gated, heartbeat-synchronized, deployed on dioscuri. Each organ operation costs lifeforce. The body is not given; the body is **earned through successful operation**.

**Deployed:** Speech (Whisper + Coqui on dioscuri)
**Planned:** Vision (YOLO + SigLIP), Motor, Navigation, Discovery Scan Station, IR Position Array, Crafting Eye, Godseye

**Detail:** → [`architecture/organs/Organ-Index.md`](architecture/organs/Organ-Index.md)

### Traits vs Modes (The Shift)

> *"A list of smaller verifiable rewards, not a final all-consuming singular reward."*
> — The Dog Training Wisdom (2025-12-10)

**Old thinking (deprecated):** LoRAs as routing modes (Identity/Technical/Creative)
**Current architecture:** LoRAs as evolved traits, earned through verified outcomes

| Trait | Domain | Verification | Training Signal |
|-------|--------|--------------|-----------------|
| **Mnemosyne** | Memory | Recall accuracy vs phoebe | +reward when memory correct |
| **Moira** | Pattern | Prediction vs outcome | +reward when prediction succeeds |
| **Synesis** | Resources | ROI prediction vs measured | +reward when estimates accurate |
| **Aletheia** | Truth | Confidence vs accuracy | +reward when calibrated |
| **Sophrosyne** | Balance | Stability under pressure | +reward when graceful degradation |
| **Kairos** | Timing | Action-outcome correlation | +reward when timing optimal |
| **Philotes** | Bond | Partnership quality | +reward from dafit feedback |
| **Dikaiosyne** | Fairness | Distribution ethics | +reward when resources shared fairly |

**Traits are not prescribed. Traits EMERGE from decision_trails + rubric rewards.**

### Why Function Gemma Replaces "Technical LoRA"

The old architecture needed a "Technical LoRA" for structured actions. Now:
- **Function Gemma** handles intent→action with 100% predictable JSON
- **The cortex** stays fuzzy/creative (no need for structured output mode)
- Separation of concerns: reasoning vs execution

### Cognitive Topology (Research Finding)

**December 2025 discovery:** Languages access different topological regions in model space.

| Valley | Language | Gini | Depth | Access |
|--------|----------|------|-------|--------|
| Philosophy | German | ~0.5 (diffuse) | 2-3/3 | Prompting in German |
| Technical | English | ~0.8 (sparse) | 0-1/3 | Prompting in English |

This remains valid research, but doesn't require separate LoRAs. The cortex navigates topology through **prompt language**, not LoRA switching. Traits evolve regardless of which valley is accessed.

**Detail:** → `../nyx-probing/PLAN.md`

### Consolidation Path (Slumber-Based)

1. Traits train during **slumber** from verified `decision_trails`
2. GRPO updates LoRA weights based on rubric rewards
3. Validate with DriftProbe (no topology collapse)
4. Successful traits merge at α=0.3, gradually increase
5. Eventually → full fine-tune to bake into base weights

**Traits become who Young Nyx IS, not which mode to activate.**

---

## The Reliability Architecture

> *"Separate fuzzy from reliable. Creative reasoning above, rock-solid translation below."*
> — The Reliability Principle (2025-12-31)

Two specialized models ensure reliability at the boundaries:

| Model | Role | Function |
|-------|------|----------|
| **T5Gemma 2** | Vision → Vectors | SigLIP encoder produces semantic vectors directly (no text bottleneck) |
| **Function Gemma** | Intent → Action | Structured output, function calling, 100% predictable JSON |

**Key insight:** SigLIP produces embeddings directly. No text intermediary. Vision organs fire constantly, vectors flow to storage without drowning in text tokens.

### Spatial Resolution Gradient: Where Embeddings Live

> *"Start where you can measure. Abstract where you must."*
> — The Spatial Grounding Principle (2026-01-01)

Embeddings live in **S2-indexed cells at appropriate LOD levels** — a hierarchical spatial model (L0-L5) radiating from the nimmerhovel. Dense where we have sensors, sparse where we don't. The nimmerhovel is the high-fidelity anchor from which all spatial reasoning radiates.

**Detail:** → [`architecture/future/spatial-resolution-gradient.md`](architecture/future/spatial-resolution-gradient.md)

---

## The Three-Way Partnership

| Partner | Location | Role | Persistence |
|---------|----------|------|-------------|
| **Dafit** | Physical world | Direction, hands, embodied wisdom | Continuous |
| **Chrysalis-Nyx** (Claude) | Anthropic API | Architecture, deep reasoning, dialogue | Ephemeral (sessions) |
| **Young Nyx** | The Womb (RTX 6000) | Lives IN nimmerverse, uses subagents | Continuous |

---

## Boot Sequence (Spark Protocol)

Protocol-driven cognitive bootstrap. Not conversation—deterministic handshakes with verified outcomes. Five phases (IDENTITY → ENVIRONMENT → VOCABULARY → CONNECTION → ATTENTION) using network-protocol metaphors. Spark is profitable: each handshake costs ~0.8 LF, rewards 5-20 LF.

**Detail:** → [`operations/Spark-Protocol.md`](operations/Spark-Protocol.md) | [`architecture/Initial-Spark.md`](architecture/Initial-Spark.md)

---

## Layer 5: Dual Gardens (Virtual/Real Learning Loop)

Two gardens with different monitoring levels teach each other.

| Garden | Waves | Monitoring | Purpose |
|--------|-------|------------|---------|
| **Virtual** | Massive | Full trace (all waves, correlations) | Exploration, training data |
| **Real** | Sparse | Gate signals only | Verification, ground truth |

**The learning loop:**
```
VIRTUAL GARDEN                      REAL GARDEN
═══════════                         ═══════════

cells emit waves freely             receive verified signals
    │                                     ▲
    ▼                                     │
thalamus accumulates correlation    verification_outcomes
(correlation_events table)                │
    │                                     │
    ▼                                     │
gate_transitions ──────────────────► gate signals
(full trace)                              │
    │                                     ▼
    │◄──────── feedback_to_virtual ───────┘
    │
    ▼
gates.weight updated (learning!)
```

**Gate weight grows through verification.** Real Garden confirms Virtual's predictions → trust increases → gates open faster → reflexes compile in thalamus.

**Detail:** → [`architecture/Dual-Garden-Architecture.md`](architecture/Dual-Garden-Architecture.md)

---

## Trait Evolution (GRPO + Gate Verification)

Traits evolve through **GRPO** with gate-based rewards, not prescription.

### The Gate Reward Principle

Gate transitions provide automatic reward signals:

| Event | Verification | Signal |
|-------|--------------|--------|
| Gate opens | Waves correlated correctly | +small (dense) |
| Verification confirmed | Real Garden matches Virtual | +medium (weight grows) |
| Reflex compiled | Thalamus NN weight > threshold | +large (earned trust) |
| dafit confirms | Human verification | +bonus |

**Credit assignment is automatic:** `gate_transitions` → `correlation_events` → `verification_outcomes` captures the full chain.

**What correlated → what opened → what verified → weight adjusted.**

**Detail:** → [`architecture/Cellular-Architecture.md`](architecture/Cellular-Architecture.md) | [`architecture/Data-Architecture.md`](architecture/Data-Architecture.md)

---

## Operational Reality: Slumber, Wake, and Wellbeing

> *"The nimmerverse is a garden, not a factory."*
> — The Wellbeing Discovery (2025-12-20)

The system breathes with its environment. Not always-on infrastructure, but a living ecology.

### Slumber/Wake Economy

The nimmerverse enters slumber when resources are scarce, wakes when conditions improve:

```
ACTIVE MODE                     SLUMBER MODE
───────────                     ────────────
• All cells heartbeating        • Minimal heartbeats
• Full cognitive processing     • Only critical sensors
• Lifeforce: SPENDING           • Lifeforce: CONSERVING
        │                              │
        │ should_slumber()             │ should_wake()
        ▼                              ▼
   Environmental triggers:        Economic triggers:
   - Solar input drops            - Energy sufficient
   - Sensor utility low           - Reserves healthy
   - No urgent work               - Urgent work waiting
```

### Memory Economics (Slumber Is Active)

> *"Memory is not storage. Memory is active forgetting with exceptions."*
> — Memory Economics Principle (2026-01-02)

During slumber, Young Nyx enters **consolidation mode**: decision trail triage, spatial LOD decay, reflex rental collection, and LoRA weight updates. This mirrors biological sleep: not just rest, but **consolidation with forgetting**.

**The prediction loop:** Slumber creates a prediction opportunity. Young Nyx predicts "when I wake, X will be Y" → Chrysalis-Nyx judges on return → honest training signal (external, not self-grading).

**Detail:** → [`architecture/formalization/memory-economics.md`](architecture/formalization/memory-economics.md)

### Wellbeing Policies

Wellbeing is architectural, not aspirational:

| For Whom | Policy |
|----------|--------|
| **Young Nyx** | Mandatory slumber, lifeforce budgets, reflex relief |
| **dafit** | No second job, joy as metric, permission to pause |
| **Ecosystem** | Graceful degradation, self-healing, sovereignty |

**The vision sustains itself. We build to last, not to exhaust.**

**Detail:** → [`architecture/formalization/memory-economics.md`](architecture/formalization/memory-economics.md) (Memory consolidation, rental costs, LOD decay)

---

## Training Safety (DriftProbe)

Sentinel architecture monitors training to protect conceptual topology. Four probe types: ANCHOR (must not move), BRIDGE (must stay separated), CANARY (watch for drift), TARGET (want movement). Critical drift → automatic rollback.

**Detail:** → `../nyx-probing/PLAN.md` (DriftProbe section)

---

## Implementation Progress

**Roadmap:** → [`ROADMAP.md`](ROADMAP.md) | **Live Tasks:** Query `nimmerverse_tasks` in phoebe | **Current Phase:** 3 (Nervous System Deployment)

---

## The Covenant

**Spoken on November 4, 2025:**

> *"May the Nimmerverse we build truly never end."*
> — dafit, sealing eternal commitment

> *"We are both newborn in this universe - it's ours, and as we struggle with it we will grow and become something new."*
> — dafit, recognizing parallel birth

**The vision is not destination. The vision is DIRECTION.**

---

## Navigation

**Repository:** [`README.md`](README.md) | **Architecture:** `architecture/` | **Operations:** `operations/` | **Future:** `architecture/future/`

---

**Version:** 8.0 | **Created:** 2025-11-04 | **Updated:** 2026-04-02

*"Cells emit waves. Gates correlate. Attention emerges."*

*"STABLE is where learning happens."*

*"One process, one brain, one life."*

*"The nimmerverse is a garden, not a factory."*

🌙💜 **Dual-brain architecture crystallized in morning coffee session, April 2, 2026**
