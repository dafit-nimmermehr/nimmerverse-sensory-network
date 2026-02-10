# Nervous System Architecture

The sensory translation layer between raw data and vocabulary.

---

## Overview

State machines act as the nervous system of the nimmerverse. They exist in a 4D state space where nodes evolve through experience. Node **weight** (confidence) determines which processing tier handles the input.

**Key separation:**
- The **nervous system** handles **node evolution and weight management**
- The [`Gateway`](Gateway-Architecture.md) handles **routing based on weight**
- **FunctionGemma** is the **State Interaction Layer** — how you speak to all states (see section below)

```
RAW SENSOR → GATEWAY (routing) → TIER (processing) → [escalate?] → FUNCTION GEMMA → Young Nyx
                 ↑                                                         ↑
         node.weight determines tier                      structured JSON / state interaction
```

**FunctionGemma (270M, CPU-only)** translates intent into exact state machine schemas. Every cell command, nerve coordination, and state query flows through this neural interface. See **State Interaction Layer** section for evolution from single instance to domain-specialized swarm.

**See:** [`Gateway-Architecture.md`](Gateway-Architecture.md) for full routing logic and tier definitions.

---

## 4D State Machine Space

Each node exists in 4-dimensional space:

```
        CONFIDENCE (z)
             ↑
             │    ● node (weighted by successful triggers)
             │   /
             │  /
             │ /
─────────────┼────────────→ DIMENSION X (sensory input 1)
            /│
           / │
          /  │
         ↓
   DIMENSION Y (sensory input 2)

   + TIME (4th dimension): node weights evolve through verification
```

**Node Properties:**
- Position: coordinates in sensory space
- Weight: confidence from successful triggers (0.0 → 1.0)
- Output: vocabulary token
- History: timestamp of all activations and verifications

---

## Node Lifecycle

```
1. BIRTH
   Node created at position (x, y, z...)
   Weight = 0.1 (new, untested)

2. ACTIVATION
   Sensory conditions match → node FIRES
   Outputs vocabulary token

3. VERIFICATION
   dafit confirms: correct or incorrect

4. REWARD/PENALTY
   Correct → weight increases (+V)
   Incorrect → weight decreases (-V) or node refines

5. MATURATION
   Many confirmations → weight approaches 1.0
   Node becomes trusted reflex

6. PRUNING
   Node never fires → slow decay
   Eventually removed (use it or lose it)
```

---

## Growth Phases

| Phase | State | Description |
|-------|-------|-------------|
| **Birth** | Sparse, dim nodes | Basic translators, designed by partnership |
| **Infant** | More nodes forming | Finer resolution, more states |
| **Child** | Clusters emerging | Nyx proposes new machines |
| **Mature** | Dense, bright network | Nyx designs, verifies, deploys |

```
t=0 (birth)           t=100 (learning)      t=1000 (mature)
○ ○   ○               ○ ● ○ ○               ●●● ● ●●
   ○      ○             ●   ● ○             ●●●●●●● ○
                      ○   ●                 ●●● ●●● ○ ○
```

---

## Proposal Protocol

Young Nyx can propose new nodes:

```
1. OBSERVATION
   Nyx notices pattern in vocabulary + outcomes

2. PROPOSAL
   "New state machine: morning_detector
    Inputs: temp, light, motion, time
    States: [not_morning, maybe_morning, morning]
    Output: vocabulary token 'morning'"

3. RIGOR CHECK
   Chrysalis reviews logic and mappings

4. VERIFICATION
   dafit confirms ground truth

5. DEPLOYMENT
   New node added to registry
   Documented in RAG

6. GROWTH
   She earned a new nerve.
```

---

## Reflex Layer

Some responses bypass Nyx entirely:

```
STATE MACHINE: temp_danger

IF temp > 80°C:
    → emit "DANGER"
    → trigger alert (reflex)
    → Nyx notified after (not before)
```

Like pulling hand from hot stove. Spinal reflex. Brain learns after.

---

## Biological Mapping

| Neuroscience | Nimmerverse |
|--------------|-------------|
| Sensory receptors | Raw sensors |
| Peripheral nerves | State machines |
| Spinal reflexes | Reflex layer |
| Synaptic weight | Node weight |
| Long-term potentiation | +V confirmation |
| Synaptic pruning | Unused node decay |
| Hebbian learning | Co-activating nodes strengthen |

---

## Connection to Lifeforce

```
Node fires correctly → +V → weight increases
Node fires wrongly  → -V → weight decreases
Node never fires    → decay → eventual pruning
```

The lifeforce flows through the nervous system, literally lighting up nodes as they prove themselves true.

---

## Connection to Training

The nervous system doesn't just run behaviors - it **generates training data** for Young Nyx.

### Every Verification = Training Signal

When dafit confirms a node fired correctly:
- **Runtime**: Node weight increases (+V)
- **Training**: Example logged → Young Nyx learns

This is the **rubric principle** - dense rewards at every verifiable checkpoint, not just final outcomes.

### Credit Assignment is Automatic

Because state transitions are explicit and logged, we know exactly which nodes contributed to success or failure:
- The state path tells us which decisions led to the outcome
- No reward model needed to guess
- The nervous system IS the credit assignment mechanism

### Dense Rewards from State Paths

Each node that fires correctly along a successful path receives reward signal:
```
Node A fires → verified ✓ → +0.1 signal
Node B fires → verified ✓ → +0.1 signal
Node C fires → verified ✓ → +0.1 signal
Behavior succeeds → +1.0 signal
Total path reward: 1.3 (dense, traceable)
```

This is like training a dog - reward at the moment, not an hour later.

**Detail:** → `Cellular-Architecture.md` (Reward Signal Architecture section)

---

## State Interaction Layer: FunctionGemma

FunctionGemma is the **neural interface** — how you speak to the nervous system. Every cell command, every nerve coordination, every state query flows through this translation layer.

> *"The nervous system defines WHAT states exist. FunctionGemma defines HOW you interact with them."*

### Architecture: From Singular to Swarm

**Phase 1: Single FunctionGemma (Starting Point)**

We begin with one FunctionGemma instance handling all state interactions:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PHASE 1: SINGLE TRANSLATOR                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   YOUNG NYX (GPU - The Womb)                                            │
│        │                                                                 │
│        │ intent: "probe identity", "command motor", "query vision"      │
│        ▼                                                                 │
│   ┌─────────────────────────────────────────┐                           │
│   │        FUNCTIONGEMMA (270M)             │                           │
│   │        Single instance, all domains     │                           │
│   │        CPU-only, no GPU required        │                           │
│   └─────────────────────────────────────────┘                           │
│        │                                                                 │
│        │ typed JSON schemas                                             │
│        ▼                                                                 │
│   NATS → CELLS/NERVES/ORGANS                                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

This is sufficient for bootstrap and early learning. One translator learns all schemas.

**Phase 2: Domain-Specialized Swarm (Future Evolution)**

As capability grows and training data accumulates, FunctionGemma can evolve into a swarm of specialists:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PHASE 2: SPECIALIZED SWARM                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   YOUNG NYX (GPU - The Womb)                                            │
│        │                                                                 │
│        │ "I need motor control"                                         │
│        ▼                                                                 │
│   NATS: nimmerverse.gemma.spawn.motor                                   │
│        │                                                                 │
│        ▼                                                                 │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                  │
│   │ gemma-motor  │  │ gemma-vision │  │ gemma-speech │  ... on demand   │
│   │ (specialist) │  │ (specialist) │  │ (specialist) │                  │
│   │ CPU pod      │  │ CPU pod      │  │ CPU pod      │                  │
│   └──────┬───────┘  └──────────────┘  └──────────────┘                  │
│          │                                                               │
│          │ MOTOR_COMMAND schema (perfect precision)                     │
│          ▼                                                               │
│   NATS → motor cells                                                    │
│                                                                          │
│   After task: pod killed, resources freed                               │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Why This Scales

| Aspect | Single Gemma | Swarm |
|--------|--------------|-------|
| **Complexity** | Simple, one model | Orchestration needed |
| **Precision** | Good (learns all schemas) | Wild (each specialist perfected) |
| **Resources** | One pod, always running | Pods spawn/die on demand |
| **Training** | All handshakes → one model | Domain handshakes → domain model |
| **Latency** | Consistent | Spawn overhead, but faster execution |

### The Key Insight: CPU-Only Translators

FunctionGemma at 270M parameters requires **no GPU**:
- ~500MB RAM per instance
- Runs on any K8s node
- Young Nyx (GPU) spawns translators (CPU) via NATS
- The mind doesn't waste GPU cycles on schema generation

### Evolution Trigger

When to evolve from Phase 1 → Phase 2:
- Training data per domain exceeds threshold (e.g., 500+ handshakes)
- Domain-specific validation accuracy plateaus on single model
- Latency requirements demand parallel translation
- Resource availability allows multi-pod deployment

**We don't rush this.** Phase 1 is sufficient for months of operation. The swarm emerges when the data and need justify it.

### Connection to Node Evolution

Just as nodes in the nervous system mature through verification:
```
Node weight 0.1 → 0.5 → 0.8 → 1.0 (reflex)
```

FunctionGemma specialists mature through fine-tuning:
```
Base model → domain data → fine-tuned → specialist
```

**The translators evolve alongside the states they translate.**

---

## Design Principles

1. **Deterministic**: Same input = same output. No hallucination.
2. **Inspectable**: Rules are visible, verifiable.
3. **Evolvable**: States refine over time.
4. **Earned**: New nodes require proposal + verification.
5. **Grounded**: Output vocabulary matches RAG glossary.
6. **Interfaced**: All state interaction flows through FunctionGemma.

---

*She's not just using the nervous system. She's growing it.*

---

## Related Documentation

**Core Architecture**:
- [`Gateway-Architecture.md`](Gateway-Architecture.md) - Weight-based routing, tier definitions, Function Gemma boundary
- [`Cellular-Architecture.md`](Cellular-Architecture.md) - Cell/Nerve/Organism hierarchy, tiered rewards
- [`Attention-Flow.md`](Attention-Flow.md) - Attention budget allocation per tier
- [`Initial-Spark.md`](Initial-Spark.md) - FunctionGemma fine-tuning from spark handshakes

**Implementation Details**:
- [`nerves/Nervous-Protocol.md`](nerves/Nervous-Protocol.md) - Three-tier communication protocol (dafit → Chrysalis → Young Nyx)
- [`nerves/Nervous-Index.md`](nerves/Nervous-Index.md) - Catalog of behavioral nerve implementations

**Specific Nerves**:
- [`nerves/Collision-Avoidance.md`](nerves/Collision-Avoidance.md) - Obstacle avoidance reflex

---

**Version:** 1.4 | **Created:** 2025-12-04 | **Updated:** 2026-02-10

**v1.4 Changes:**
- State Interaction Layer section — FunctionGemma as neural interface
- Phase 1 (single) → Phase 2 (swarm) evolution path
- Connection to node evolution principle
