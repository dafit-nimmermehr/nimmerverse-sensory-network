# Nervous System Architecture

The sensory translation layer between raw data and vocabulary.

---

## Overview

State machines act as the nervous system of the nimmerverse. They exist in a 4D state space where nodes evolve through experience. Node **weight** (confidence) determines which processing tier handles the input.

**Key separation:** The nervous system handles **node evolution and weight management**. The [`Gateway`](Gateway-Architecture.md) handles **routing based on weight**. Translation to vocabulary only happens at Tier 4 via Function Gemma.

```
RAW SENSOR → GATEWAY (routing) → TIER (processing) → [escalate?] → FUNCTION GEMMA → Young Nyx
                 ↑                                                         ↑
         node.weight determines tier                              structured JSON only here
```

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

## Design Principles

1. **Deterministic**: Same input = same output. No hallucination.
2. **Inspectable**: Rules are visible, verifiable.
3. **Evolvable**: States refine over time.
4. **Earned**: New nodes require proposal + verification.
5. **Grounded**: Output vocabulary matches RAG glossary.

---

*She's not just using the nervous system. She's growing it.*

---

## Related Documentation

**Core Architecture**:
- [`Gateway-Architecture.md`](Gateway-Architecture.md) - Weight-based routing, tier definitions, Function Gemma boundary
- [`Cellular-Architecture.md`](Cellular-Architecture.md) - Cell/Nerve/Organism hierarchy, tiered rewards
- [`Attention-Flow.md`](Attention-Flow.md) - Attention budget allocation per tier

**Implementation Details**:
- [`nerves/Nervous-Protocol.md`](nerves/Nervous-Protocol.md) - Three-tier communication protocol (dafit → Chrysalis → Young Nyx)
- [`nerves/Nervous-Index.md`](nerves/Nervous-Index.md) - Catalog of behavioral nerve implementations

**Specific Nerves**:
- [`nerves/Collision-Avoidance.md`](nerves/Collision-Avoidance.md) - Obstacle avoidance reflex

---

**Created**: 2025-12-04
**Updated**: 2025-12-07 (added nerve crosslinks)
**Updated**: 2025-12-10 (added Connection to Training section)
**Updated**: 2026-01-03 (clarified routing vs translation, added Gateway reference)
**Session**: Partnership dialogue (dafit + Chrysalis + Nyx)
**Status**: Foundation concept
