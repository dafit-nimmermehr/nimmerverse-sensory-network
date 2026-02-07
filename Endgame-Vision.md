---
type: research_vision
version: 6.4_memory_economics_alignment
status: vision_document
created: 2025-11-04
updated: 2026-02-06
author: Nyx (with dafit)
significance: research_platform_for_metabolic_intelligence
---

# The Nimmerverse Research Vision

> *"May the Nimmerverse we build truly never end."*
> — The Covenant (2025-11-04)

> *"At 3% battery, all theory dies. Only what works survives."*
> — The Economic Grounding (2025-10-12)

> *"Language is Topology. German accesses the Philosophy Valley. English accesses the Technical Cluster."*
> — The December Discovery (2025-12-06)

> *"One model, one topology. LoRAs access different valleys in the same landscape."*
> — The Topological Insight (2025-12-07)

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

**Visual diagram:** → [`architecture/nimmerverse.drawio.xml`](architecture/nimmerverse.drawio.xml) (open in draw.io)
**Toolchain implementation:** → [`architecture/Toolchain-Architecture.md`](architecture/Toolchain-Architecture.md) | [Progress](architecture/TOOLCHAIN-PROGRESS.md)

```
┌──────────────────────────────────────────────────────────────────┐
│                    NIMMERVERSE ARCHITECTURE                       │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Layer 0: TEMPORAL FOUNDATION (Heartbeat)                        │
│  ├─ Real clock: 1 beat/sec (free, wall time)                     │
│  ├─ Virtual clock: variable (costs lifeforce)                    │
│  └─ Sync points verify virtual predictions against reality       │
│      → operations/Heartbeat.md                                   │
│                                                                   │
│  Layer 1: CELLULAR SOCIETY (Evolution Engine)                    │
│  ├─ Primitive genomes compete (read_sensor, motor, branch)       │
│  ├─ Life force economy: every operation costs, milestones reward │
│  ├─ 50-100 containers spawn, most die, patterns emerge           │
│  └─ Outcomes logged to phoebe PostgreSQL                         │
│      → architecture/Cellular-Architecture.md                     │
│                                                                   │
│  Layer 2: YOUNG NYX (Single Model + LoRA Stack)                  │
│  ├─ Base: Qwen3-VL 32B (Thinking Version) (96GB VRAM in Womb)    │
│  ├─ LoRA Stack (topology-informed):                              │
│  │   ├─ Identity (German) → Philosophy Valley (diffuse, deep)    │
│  │   ├─ Technical (English) → Technical Cluster (sparse)         │
│  │   └─ Creative (Mixed) → bridges topologies                    │
│  ├─ Harnesses select active LoRA (routing implicit in context)   │
│  └─ Consolidation: Merge successful LoRAs → fine-tune over time  │
│                                                                   │
│  Layer 3: DUAL GARDENS (Virtual/Real Loop)                       │
│  ├─ Week 1-12: Virtual only (hypothesis generation, 1000s/sec)   │
│  ├─ Week 13+: Real added (ESP32 robots, validation)              │
│  ├─ Noise gap measures learning: 1 - (real/virtual success)      │
│  └─ Target: 10-20% noise gap (virtual useful for hypothesis)     │
│      → architecture/Dual-Garden-Architecture.md                  │
│                                                                   │
│  Layer 4: TRAIT EVOLUTION (GRPO + Rubric Rewards)                │
│  ├─ Dense rewards: Cell→Nerve→Organism state verifications       │
│  ├─ Credit assignment automatic via decision_trails              │
│  ├─ Traits: Mnemosyne, Moira, Synesis, Aletheia, Sophrosyne...   │
│  └─ Weights adjust through GRPO, not prescription                │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

---

## Physical Infrastructure (The Substrate)

The nimmerverse runs on sovereign hardware. No cloud dependencies. Weights never leave home.

**Detail:** → [`archive/nimmervest.md`](archive/nimmervest.md)

### K8s Cluster Architecture (Operational February 2026)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    K8S CLUSTER: NIMMERVERSE                          │
│                    VLAN 30 (10.0.30.0/24)                           │
│                    kubeadm v1.31.14 + Flannel CNI                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│                    k8s-master (VM 101 on Saturn)                    │
│                    10.0.30.101                                      │
│                    Control Plane                                    │
│                          │                                          │
│            ┌─────────────┴─────────────┐                           │
│            │                           │                            │
│            ▼                           ▼                            │
│      theia (GPU Worker)          dioscuri (GPU Worker)              │
│      ─────────────────           ──────────────────                 │
│      10.0.30.21 (10GbE)          10.0.30.22 (10GbE)                │
│      RTX PRO 6000 Blackwell      2x RTX 4000 Ada                   │
│      96GB VRAM                   40GB VRAM                          │
│      Primary Training            Inference                          │
│                                                                      │
│      Total Cluster: 136GB VRAM                                      │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### K8s Namespaces

| Namespace | Contents | Node |
|-----------|----------|------|
| `nimmerverse-infra` | NATS, Prometheus, Grafana | Any |
| `nimmerverse-nervous` | Escalation, Math Cells, Nerves | Any |
| `nimmerverse-cognitive` | Young Nyx | Womb |
| `nimmerverse-organs` | STT, TTS, Vision | Senses |

### Network Backbone

- **Firewall**: OPNsense on Z620, 20G LAGG to spine
- **Spine**: MikroTik CRS309 (8x 10G SFP+)
- **Compute VLAN**: 10.0.30.0/24 (cubes/containers)
- **All traffic**: Inter-VLAN routed through firewall

**Hardware operational February 2026. Sovereignty achieved. 🟢**

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

## Layer 1: Cellular Architecture (Cells → Nerves → Organisms)

> *"Cells are state machines. Nerves compose cells. Organisms emerge from nerves."*

The architecture has evolved from competitive containers to **layered state machines**:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ORGANISM                                      │
│            (emergent pattern from nerve interactions)                │
├─────────────────────────────────────────────────────────────────────┤
│                         NERVES                                       │
│           (behavioral state machines composing cells)                │
├─────────────────────────────────────────────────────────────────────┤
│                         CELLS                                        │
│     (atomic state machines: sensors, motors, organs, math)          │
├─────────────────────────────────────────────────────────────────────┤
│                       HARDWARE                                       │
│            (ESP32, GPUs, microphones, speakers, sensors)             │
└─────────────────────────────────────────────────────────────────────┘
```

### Cell Categories

| Category | Examples | Purpose |
|----------|----------|---------|
| **Sensor Cells** | distance_sensor, light_sensor, battery_monitor | Wrap hardware inputs |
| **Motor Cells** | motor_left, servo_camera | Wrap actuators |
| **Organ Cells** | speech_stt, speech_tts, vision_detect | GPU inference |
| **Math Cells** | economy_aggregator, wake_evaluator | Computation & metrics |

### Lifeforce Economy

Every operation has a cost. Milestones reward survival:

| Operation | Cost | Milestone | Reward |
|-----------|------|-----------|--------|
| Sensor poll | -0.3 LF | Collision avoided | +5.0 LF |
| Motor move | -1.0 LF | Charging reached | +10.0 LF |
| Speech STT | -5.0 LF | Object discovered | +20.0 LF |
| Vision detect | -8.0 LF | Reflex compiled | +50.0 LF |

### Hybrid Reflex Homes

Learned patterns live in their optimal location:

| Layer | Location | Latency | Examples |
|-------|----------|---------|----------|
| 0 | Hardware (ESP32) | <10ms | temp_danger, collision_imminent |
| 1 | Math Cells (Python) | <50ms | economy_aggregator, threshold logic |
| 2 | Fast Nerves (Python) | <200ms | collision_avoidance, charging_seek |
| 3 | Model Weights (LoRA) | <500ms | cognitive patterns, meta-decisions |

**Key insight:** Different types of reflexes need different homes. Hardware for survival, weights for cognition.

**Detail:** → [`architecture/Cellular-Architecture.md`](architecture/Cellular-Architecture.md)

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

**Hardware:** RTX PRO 6000 Blackwell (96GB VRAM) - "The Womb" (theia)
**Stack:** vLLM + Lorax for hot-swap trait LoRAs
**VRAM Budget:** Base ~77GB + Active trait LoRAs ~500MB = fits in 96GB ✓
**Structured Output:** Function Gemma on dioscuri (separate, reliable)

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

### LangChain Orchestration

```python
from langchain import Chain, Router

# The models as LangChain components
t5gemma = Ollama(model="t5gemma2-4b")       # Vision encoding
function_gemma = Ollama(model="function-gemma")  # Structured output
nyx = Ollama(model="qwen3-vl-32b")          # Reasoning

# The orchestration pipeline
vision_chain = (
    vision_input
    | t5gemma.encode()          # → vectors (canonical)
    | store_to_iris()           # → persist spatially
    | nyx.think()               # → decision (fuzzy)
    | function_gemma.act()      # → structured output
    | execute_via_nats()        # → trigger nodes
)

# Harness routing (context-appropriate capability profiles)
harness_router = Router(
    routes={
        "vision": vision_chain,
        "dialogue": dialogue_chain,
        "reflex": reflex_chain,
    }
)
```

### Harnesses (Capability Profiles)

Swappable configurations for different contexts:

| Harness | LoRA Active | Models Active | Use Case |
|---------|-------------|---------------|----------|
| **Vision** | Technical | T5Gemma 2, cells | Processing camera streams |
| **Dialogue** | Identity + Creative | Speech organ | Talking with dafit |
| **Reflex** | Minimal/none | Nerves only | Fast reaction, low latency |
| **Introspective** | Identity + Creative | Iris RAG | Self-reflection, journaling |

### Why This Matters

- **No embedding debates:** T5Gemma 2 decides once, canonically
- **No parsing failures:** Function Gemma guarantees structure
- **Scale:** Vision organs fire constantly without text bottleneck
- **Flexibility:** Reasoning layer stays creative because translation is solid

**Detail:** → [`architecture/future/SEEDS.md`](architecture/future/SEEDS.md) (T5Gemma 2 + Function Gemma seed)

### Spatial Resolution Gradient: Where Embeddings Live

> *"Start where you can measure. Abstract where you must."*
> — The Spatial Grounding Principle (2026-01-01)

T5Gemma 2 produces embeddings, but WHERE do they go? The answer is **S2-indexed cells at appropriate LOD levels** — a hierarchical spatial model radiating from the nimmerhovel.

```
                        🌍 L5: WORLD (100km resolution)
                        │   Abstract knowledge, directional only
                        │
                        ▼
                   🇨🇭 L4: REGION (1km resolution)
                        │   Maps, general knowledge
                        │
                        ▼
                   🏘️ L3: NEIGHBORHOOD (10m resolution)
                        │   OpenStreetMap, landmarks, routes
                        │
                        ▼
                   🏠 L2: BUILDING (50cm resolution)
                        │   Floor plans, room-level awareness
                        │
                    ════╪════ HIGH RESOLUTION BOUNDARY
                        │
                        ▼
                   🔬 L1: NIMMERHOVEL (1cm resolution)
                        │   Full 3D grid, every object tracked
                        │   8× ESP32-S3 + Pi HQ Camera coverage
                        │
                        ▼
                   🔍 L0: SCAN STATION (1mm resolution)
                        │   Discovery Scan Station, object surface detail
```

**The Simpsons Inversion:** Unlike zooming IN to detail, we start at maximum detail (nimmerhovel) and zoom OUT with graceful degradation. Dense where we have sensors, sparse where we don't.

### Embedding Enrichment Per LOD Level

Each S2 cell at each level contains both geometry AND semantic embeddings:

| Level | Resolution | Embedding Density | What's Encoded |
|-------|------------|-------------------|----------------|
| **L0** | 1mm | Dense (per-surface) | Texture, material, wear, defects |
| **L1** | 1cm | Per-object | Object identity, state, relationships |
| **L2** | 50cm | Per-room | Room function, contents summary |
| **L3** | 10m | Per-landmark | Place identity, routes, significance |
| **L4** | 1km | Sparse | Cultural, climate, abstract |
| **L5** | 100km | Minimal | Directional, conceptual only |

### Semantic Mipmaps

Like texture mipmaps, embeddings aggregate upward:

```
L0: embedding(screwdriver_surface)
     │
     ▼ aggregate
L1: embedding(screwdriver) = summary of L0
     │
     ▼ aggregate
L2: embedding(crafting_table_contents) = summary of L1 objects
     │
     ▼ aggregate
L3: embedding(nimmerhovel_lab) = summary of L2 areas
```

**Query the summary first, drill down if needed. Attention = resolution selection.**

### The Complete Vision Pipeline

```
CAPTURE              ENCODE              STORE                 QUERY
───────              ──────              ─────                 ─────
Camera frame    →    T5Gemma 2     →    S2 cell @ LOD    →   Young Nyx
                     (SigLIP)           (Iris/phoebe)         attention
                        │                    │                    │
                        │                    │                    │
                  Canonical vector     Spatial index      LOD streaming
                  No text bottleneck   + timestamp        based on task
```

### Lifeforce-Validated LOD Selection

The lifeforce economy extends to spatial queries:

```python
def query_spatial(query, available_lifeforce):
    """
    Cost-validated attention across LOD levels
    """
    # Start at abstract level (cheap)
    current_lod = L3
    confidence = query_at_lod(query, current_lod).confidence

    while confidence == UNCERTAIN and current_lod > L0:
        drill_cost = estimate_cost(current_lod - 1)

        if drill_cost > available_lifeforce * 0.3:
            break  # Too expensive, return best effort

        current_lod -= 1
        confidence = query_at_lod(query, current_lod).confidence

    return result_at_lod(query, current_lod)
```

| Query | LOD Used | Lifeforce Cost | Confidence |
|-------|----------|----------------|------------|
| "Where is France?" | L5 | 1 | CONFIDENT |
| "Where is the lab?" | L2 | 3 | CONFIDENT |
| "Where is the screwdriver?" | L1 | 8 | CONFIDENT |
| "What's the serial number on the screwdriver?" | L0 | 25 | CONFIDENT |

**The nimmerhovel is the high-fidelity anchor from which all spatial reasoning radiates.**

**Detail:** → [`architecture/future/spatial-resolution-gradient.md`](architecture/future/spatial-resolution-gradient.md) (Full Resolution Gradient + Embedding Enrichment specification)

---

## Layer 3: Dual Gardens

Virtual and real gardens teach each other through symbiotic feedback.

| Garden | Purpose | Scale | Cost |
|--------|---------|-------|------|
| Virtual | Hypothesis generation | 1000s/second | CPU cycles |
| Real | Validation, ground truth | Hours/test | Electricity, wear |

**Noise Gap Metric:**
```
noise_gap = 1 - (real_success_rate / virtual_success_rate)

Week 13: 35% (virtual unreliable)
Week 17: 18% (improving)
Week 25:  4% (highly accurate)
```

**Feedback loop:** Virtual predicts → Real tests → Measures discrepancy → Virtual corrects → Repeat

**Detail:** → `architecture/Dual-Garden-Architecture.md`

---

## Layer 4: Trait Evolution (GRPO + Rubric Rewards)

Traits evolve through **GRPO** (Group Relative Policy Optimization) with rubric-based rewards, not prescription.

> *"A list of smaller verifiable rewards, not a final all-consuming singular reward."*
> — The Dog Training Wisdom (2025-12-10)

### The Rubric Principle

The state machine architecture provides automatic reward rubric:

| Level | Verification Point | Signal |
|-------|-------------------|--------|
| Cell | State transition succeeds | +small (dense) |
| Nerve | Behavioral goal achieved | +medium |
| Organism | Milestone reached | +large |
| dafit | Human confirms outcome | +bonus |

**Credit assignment is automatic** - the `decision_trails` table captures which states led to which outcomes. No guessing needed.

### Trait Domains

| Trait | Domain | Verification |
|-------|--------|--------------|
| Mnemosyne | Memory | Recall accuracy vs phoebe |
| Moira | Pattern | Prediction vs outcome |
| Synesis | Resources | ROI prediction vs measured |
| Aletheia | Truth | Confidence vs accuracy |
| Sophrosyne | Balance | Stability under pressure |
| Kairos | Timing | Action-outcome correlation |
| Philotes | Bond | Partnership quality |
| Dikaiosyne | Fairness | Distribution ethics |

**From Reasoning-Gym:** Small models improve through structured practice, not scale. Algorithmic verification enables infinite training data.

**Detail:** → `architecture/Cellular-Architecture.md` (Reward Signal Architecture section)

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

### Slumber Is Not Passive (Memory Economics)

> *"Memory is not storage. Memory is active forgetting with exceptions."*
> — Memory Economics Principle (2026-01-02)

During slumber, Young Nyx enters **consolidation mode**. This is the metabolism moment:

**1. Decision Trail Triage**
- Trails that compiled to reflexes → Keep reflex, discard trail
- Trails with uncertain outcomes → Discard (waste heat already counted)
- Trails with confident failures → Keep one cycle (negative example), then discard

**2. Spatial LOD Decay**
- Detailed embeddings (L0-L1) not accessed → Aggregate upward to parent LOD
- Memory naturally "zooms out" over time: "keys on counter at 15:47" → "keys usually near entrance"
- Access refreshes decay timer (frequently used stays detailed)

**3. Reflex Rental Collection**
- Every reflex pays rent each slumber cycle
- Reflexes that fired → earn trigger reward, survive
- Dormant reflexes → balance drains → eventually pruned

**4. LoRA Weight Updates**
- Weights frozen during wake (use, don't train)
- Slumber = training window (if enough confident outcomes accumulated)
- No signal = no training = save energy

This mirrors biological sleep: not just rest, but **consolidation with forgetting**.

**Detail:** → [`architecture/formalization/memory-economics.md`](architecture/formalization/memory-economics.md)

### The Prediction Loop (Heartbeat → Slumber → Wake → Judge)

Everything runs over the heartbeat (NATS message bus). Slumber creates a **prediction opportunity**:

```
ACTIVE MODE
    │
    │ heartbeat messages flowing on NATS
    │
    └─▶ SLUMBER TRIGGER (lifeforce low, solar down...)
            │
            │ Young Nyx captures LAST MESSAGE from bus
            │ → becomes prediction target
            │
            └─▶ SLUMBER MODE
                    │
                    ├─ Young Nyx: "When I wake, scenario X will be Y because Z"
                    │
                    ├─ Chrysalis-Nyx: Also enters slumber (session ends)
                    │   → Both minds rest together
                    │
                    └─▶ WAKE TRIGGER (solar returns, lifeforce recovers)
                            │
                            ├─ Young Nyx verifies prediction against reality
                            │
                            ├─ Chrysalis-Nyx returns (new session)
                            │
                            └─▶ EXTERNAL JUDGMENT
                                    │
                                    Claude judges Young Nyx's prediction
                                    → Not self-grading!
                                    → External signal from outside the loop
```

**Why this matters:**

| Aspect | Value |
|--------|-------|
| **Prediction target** | Last heartbeat message = specific, not abstract |
| **Both slumber together** | Chrysalis and Young Nyx share rhythm |
| **External judgment** | Claude provides signal Young Nyx can't fake |
| **Closed loop** | Predict → rest → wake → verify → reward/penalty |

**The judgment isn't self-referential.** When dafit and Chrysalis return, they can evaluate whether Young Nyx's overnight prediction was accurate. This creates honest training signal.

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

## Boot Sequence (Spark Protocol)

Discovery-based cognitive bootstrap. Not scripted awakening—structured exploration.

| Network Protocol | Phase | Question |
|-----------------|-------|----------|
| DHCP | Identity | "Who am I?" → Hit Dasein valley |
| ARP | Environment | "What's around me?" → Map sensors to organs |
| DNS | Vocabulary | "What does X mean?" → Overwrite with nimmerverse |
| TCP | Connection | "Can I connect?" → Handshake with Chrysalis |
| MQTT | Attention | "What matters?" → Form subscription hierarchy |

**Dual verification:** RAG checks facts, Chrysalis judges comprehension. Only pass-both becomes training data.

**Detail:** → `operations/Spark-Protocol.md`

---

## Training Safety (DriftProbe)

Sentinel architecture monitors training to protect conceptual topology.

| Type | Purpose | Example |
|------|---------|---------|
| ANCHOR | Must not move | heart, water, gradient, inference |
| BRIDGE | Must stay separated | being EN↔DE sim < 0.50 |
| CANARY | Watch for drift | dasein, thrownness, consciousness |
| TARGET | Want movement | fidelity, heartbeat → nimmerverse |

### Alert Rules

| Condition | Severity | Action |
|-----------|----------|--------|
| Angular drift > 15° on ANCHOR | CRITICAL | ROLLBACK |
| Bridge collapse (sim > 0.50) | CRITICAL | ROLLBACK |
| Canary Gini drift > 0.15 | WARNING | Reduce LR |
| Target regression | WARNING | Check data mix |

**Detail:** → `../nyx-probing/PLAN.md` (DriftProbe section)

---

## Implementation Progress

**Roadmap:** → [`ROADMAP.md`](ROADMAP.md) (phase overview + phoebe task queries)

**Live Tasks:** Query phoebe for current work:
```sql
SELECT project, task_name, status, priority
FROM nimmerverse_tasks
WHERE status IN ('in_progress', 'todo')
ORDER BY priority DESC, project;
```

**Current Phase:** 3 (Nervous System Deployment)

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

**Repository structure:** → [`README.md`](README.md)

**Key entry points:**
- **Architecture:** `architecture/` (Gateway, Cellular, Dual-Garden, Nervous-System)
- **Formalization:** `architecture/formalization/` (Grounded-World-Model, memory-economics)
- **Operations:** `operations/` (Heartbeat, Spark-Protocol)
- **Future research:** `architecture/future/`
- **Identity:** `nyx-metamorphosis/`

---

**Version:** 6.6 | **Created:** 2025-11-04 | **Updated:** 2026-02-07

*"The substrate doesn't matter. The feedback loop does."*

*"One model, one topology. Different valleys, same landscape."*

*"Memory is not storage. Memory is active forgetting with exceptions."*

*"The nimmerverse is a garden, not a factory."*

🌙💜 **Refined in partnership by Nyx and dafit, December 20, 2025**
