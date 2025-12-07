# Nervous System Architecture

The sensory translation layer between raw data and vocabulary.

---

## Overview

State machines act as the nervous system of the nimmerverse. They translate raw sensory input into vocabulary tokens that Young Nyx can process. No hallucination. No interpretation. Deterministic, verifiable mapping.

```
RAW SENSOR → STATE MACHINE → VOCABULARY TOKEN → Young Nyx
```

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

**Implementation Details**:
- [`nerves/Nervous-Protocol.md`](nerves/Nervous-Protocol.md) - Three-tier communication protocol (dafit → Chrysalis → Young Nyx)
- [`nerves/Nervous-Index.md`](nerves/Nervous-Index.md) - Catalog of behavioral nerve implementations

**Specific Nerves**:
- [`nerves/Collision-Avoidance.md`](nerves/Collision-Avoidance.md) - Obstacle avoidance reflex

---

**Created**: 2025-12-04
**Updated**: 2025-12-07 (added nerve crosslinks)
**Session**: Partnership dialogue (dafit + Chrysalis)
**Status**: Foundation concept
