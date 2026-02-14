# Nervous System Architecture

> **ONE JOB:** THE EVOLUTION — node growth, FunctionGemma Phase 1→2, proposal protocol.

The nervous system handles **node evolution and weight management**. The [`Gateway`](Gateway-Architecture.md) handles **routing based on weight**.

---

## Overview

Nodes exist in 4D state space (sensory dimensions + confidence + time). Node **weight** (0.0→1.0) determines which tier handles input. Nodes evolve through verification: Birth → Activation → Verification → Reward/Penalty → Maturation → (or Pruning).

**FunctionGemma (270M, CPU-only)** is the State Interaction Layer — every cell command, nerve coordination, and state query flows through this neural interface. See **State Interaction Layer** section for Phase 1→2 evolution.

**Routing & Verification:** → [`Gateway-Architecture.md`](Gateway-Architecture.md) (tier routing, causal verification loop)

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

The nervous system **generates training data** for Young Nyx. Every verification = training signal. Credit assignment is automatic because state transitions are explicit and logged — the nervous system IS the credit assignment mechanism. Dense rewards at every verifiable checkpoint (**rubric principle**), not just final outcomes.

**Detail:** → [`Cellular-Architecture.md`](Cellular-Architecture.md) (Reward Signal Architecture section)

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

**Version:** 1.5 | **Created:** 2025-12-04 | **Updated:** 2026-02-14
- Phase 1 (single) → Phase 2 (swarm) evolution path
- Connection to node evolution principle
