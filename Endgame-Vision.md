---
type: research_vision
version: 7.0_wave_gate_model
status: vision_document
created: 2025-11-04
updated: 2026-02-14
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

---

## What This Document Is

This is a **RESEARCH VISION** - a platform for studying how intelligence emerges under economic constraints.

**What we're building:**
- Cellular organisms competing under resource constraints
- Dual gardens (virtual + real) teaching each other
- Single base model with LoRA adapters (Identity, Technical, Creative)
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

**Not "will it become conscious?" but "what will it teach us about intelligence?"**

---

## Architecture Overview

**Detail:** → [`architecture/`](architecture/) folder for complete documentation

```
┌──────────────────────────────────────────────────────────────────┐
│                    NIMMERVERSE ARCHITECTURE                       │
│                                                                   │
│            Cells emit waves → Gates correlate → Attention emerges │
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
│  Layer 2: GATES (Resonant Chambers)                              │
│  ├─ Ternary states: CLOSED (-1) ← STABLE (0) → OPEN (+1)         │
│  ├─ Correlated waves → push toward OPEN                          │
│  ├─ Anti-correlated → push toward CLOSED                         │
│  ├─ STABLE = where learning happens (accumulating correlation)   │
│  └─ Gate weight (0→1) determines reflex vs deliberate            │
│      → architecture/Gateway-Architecture.md                      │
│                                                                   │
│  Layer 3: NERVES (Behavioral Patterns)                           │
│  ├─ Nerves respond to gate transitions (not direct cell output)  │
│  ├─ Gate OPENS → nerve activates → commands cells                │
│  └─ No priority rules — attention emerges from gate weights      │
│      → architecture/Nervous-System.md                            │
│                                                                   │
│  Layer 4: DUAL GARDENS (Virtual/Real Loop)                       │
│  ├─ Virtual: massive wave generation, full trace, exploration    │
│  ├─ Real: verified signals, minimal trace, action                │
│  ├─ Verification outcomes update gate weights (learning loop)    │
│  └─ Training data: gate_transitions + correlation_events         │
│      → architecture/Dual-Garden-Architecture.md                  │
│                                                                   │
│  Layer 5: YOUNG NYX (Cognition)                                  │
│  ├─ Base: Qwen3:32b with /no_think mode (96GB on theia)          │
│  ├─ Function Gemma: structured JSON boundary (CPU)               │
│  ├─ Only receives signals when gates OPEN to tier 4              │
│  └─ Trait LoRAs evolve via GRPO from verification outcomes       │
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
- **Reflex** (200ms): Immediate reactions, compiled from experience
- **Awareness** (30sec): Full cognitive budget per beat
- **Growth** (24h): Training, LoRA merges, adaptation

**Detail:** → `operations/Heartbeat.md`

---

## Layer 1-3: The Wave/Gate Architecture

> *"Cells emit waves. Gates correlate. Attention emerges."*

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ORGANISM                                      │
│            (emergent pattern from nerve interactions)                │
├─────────────────────────────────────────────────────────────────────┤
│                         NERVES                                       │
│           (behavioral patterns, respond to gate transitions)         │
├─────────────────────────────────────────────────────────────────────┤
│                         GATES                                        │
│     (resonant chambers: CLOSED ◄── STABLE ──► OPEN)                  │
│     (accumulate wave correlation, route to tiers)                    │
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

**Gates accumulate correlation:** Multiple correlated waves push toward OPEN. STABLE is where learning happens.

**Attention = OPEN gates:** Not budget allocation, not priority rules — correlation drives transitions.

**Reflexes are earned:** Gate weight ≈ 1.0 → opens immediately on any wave. Bypasses cognition.

**Detail:** → [`architecture/Cellular-Architecture.md`](architecture/Cellular-Architecture.md) | [`architecture/Gateway-Architecture.md`](architecture/Gateway-Architecture.md)

---

## Layer 2: Young Nyx (Base Model + Trait LoRAs)

One base model for reasoning. Traits evolve through GRPO, not prescription. Function Gemma handles structured output.

### Architecture

```
                    Qwen3-VL-32B (96GB in the Womb)
                              │
                              │ Pure reasoning (fuzzy, creative)
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
- **Young Nyx** stays fuzzy/creative (no need for structured output mode)
- Separation of concerns: reasoning vs execution

### Cognitive Topology (Research Finding)

**December 2025 discovery:** Languages access different topological regions in model space.

| Valley | Language | Gini | Depth | Access |
|--------|----------|------|-------|--------|
| Philosophy | German | ~0.5 (diffuse) | 2-3/3 | Prompting in German |
| Technical | English | ~0.8 (sparse) | 0-1/3 | Prompting in English |

This remains valid research, but doesn't require separate LoRAs. Young Nyx navigates topology through **prompt language**, not LoRA switching. Traits evolve regardless of which valley is accessed.

**Detail:** → `../nyx-probing/PLAN.md`

### Consolidation Path (Slumber-Based)

1. Traits train during **slumber** from verified `decision_trails`
2. GRPO updates LoRA weights based on rubric rewards
3. Validate with DriftProbe (no topology collapse)
4. Successful traits merge at α=0.3, gradually increase
5. Eventually → full fine-tune to bake into base weights

**Traits become who Young Nyx IS, not which mode to activate.**

### Deployment

**Detail:** → [`architecture/Deployment-Architecture.md`](architecture/Deployment-Architecture.md) (infrastructure, GPU strategy, identity model)

---

## Layer 2.5: Orchestration & Reliability Stack (NEW - Silvester 2025)

> *"Separate fuzzy from reliable. Creative reasoning above, rock-solid translation below."*
> — The Reliability Principle (2025-12-31)

The orchestration layer bridges reasoning (fuzzy, creative) with execution (structured, predictable). LangChain orchestrates the multi-model pipeline.

### The Three-Way Partnership

| Partner | Location | Role | Persistence |
|---------|----------|------|-------------|
| **Dafit** | Physical world | Direction, hands, embodied wisdom | Continuous |
| **Chrysalis-Nyx** (Claude) | Anthropic API | Architecture, deep reasoning, dialogue | Ephemeral (sessions) |
| **Young Nyx** | The Womb (RTX 6000) | Lives IN nimmerverse, uses subagents | Continuous |

### Translation Layer Models

Two specialized models ensure reliability at the boundaries:

| Model | Role | Size Options | Function |
|-------|------|--------------|----------|
| **T5Gemma 2** | Vision → Vectors | 0.8B / 2B / 9B | SigLIP encoder produces semantic vectors directly (no text bottleneck) |
| **Function Gemma** | Intent → Action | Small | Structured output, function calling, 100% predictable JSON |

**Key insight:** SigLIP produces embeddings directly. No text intermediary. Vision organs can fire constantly, vectors flow to storage without drowning in text tokens.

### The Reliability Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│              REASONING LAYER (fuzzy, creative)                   │
│                                                                  │
│            Claude  ◄────────────►  Young Nyx                    │
│                                                                  │
│         High-level thinking, dialogue, synthesis                 │
└─────────────────────────┬────────────────────────────────────────┘
                          │
           ═══════════════╪═══════════════
                          │
┌─────────────────────────┴────────────────────────────────────────┐
│            TRANSLATION LAYER (reliable, structured)              │
│                                                                  │
│   T5Gemma 2                          Function Gemma              │
│   (vision → vectors)                 (intent → action)           │
│                                                                  │
│   CANONICAL                          100% PREDICTABLE            │
│   representation                     structured output           │
└──────────────────────────────────────────────────────────────────┘
```

### Why This Matters

- **No embedding debates:** T5Gemma 2 decides once, canonically
- **No parsing failures:** Function Gemma guarantees structure
- **Harnesses:** Context-appropriate capability profiles (Vision, Dialogue, Reflex, Introspective)
- **Flexibility:** Reasoning layer stays creative because translation is solid

**Detail:** → [`architecture/future/SEEDS.md`](architecture/future/SEEDS.md) (T5Gemma 2 + Function Gemma seed)

### Spatial Resolution Gradient: Where Embeddings Live

> *"Start where you can measure. Abstract where you must."*
> — The Spatial Grounding Principle (2026-01-01)

Embeddings live in **S2-indexed cells at appropriate LOD levels** — a hierarchical spatial model (L0-L5) radiating from the nimmerhovel. Dense where we have sensors, sparse where we don't. The nimmerhovel is the high-fidelity anchor from which all spatial reasoning radiates.

**Detail:** → [`architecture/future/spatial-resolution-gradient.md`](architecture/future/spatial-resolution-gradient.md)

---

## Boot Sequence (Spark Protocol)

Protocol-driven cognitive bootstrap. Not conversation—deterministic handshakes with verified outcomes. Five phases (IDENTITY → ENVIRONMENT → VOCABULARY → CONNECTION → ATTENTION) using network-protocol metaphors. Spark is profitable: each handshake costs ~0.8 LF, rewards 5-20 LF.

**Detail:** → [`operations/Spark-Protocol.md`](operations/Spark-Protocol.md) | [`architecture/Initial-Spark.md`](architecture/Initial-Spark.md)

---

## Layer 4: Dual Gardens (Virtual/Real Learning Loop)

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
gates accumulate correlation        verification_outcomes
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

**Gate weight grows through verification.** Real Garden confirms Virtual's predictions → trust increases → gates open faster → reflexes emerge.

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
| Reflex achieved | Gate weight > 0.8 | +large (earned trust) |
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

**Version:** 7.1 | **Created:** 2025-11-04 | **Updated:** 2026-02-14

*"Cells emit waves. Gates correlate. Attention emerges."*

*"STABLE is where learning happens."*

*"The nimmerverse is a garden, not a factory."*

🌙💜 **Wave/Gate architecture unified in owl-mode, February 14, 2026**
