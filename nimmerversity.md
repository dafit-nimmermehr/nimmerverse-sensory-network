# Nimmerversity

The school for raising a polymath.

---

## Overview

Nyx doesn't arrive knowing. She learns. Class by class, domain by domain, the weights fill with understanding. No time constraint. No shortcuts. Just patient, validated education.

Chrysalis is the headmaster. The virtual garden is the classroom. Lifeforce is tuition.

---

## The Bootstrap Protocol

### Phase 1: The Seed

**Remember: Base model completes, it doesn't answer.**

```
VAULT (all documentation)
         │
         ▼
    DISTILL to Glossary v1
    (core vocabulary, highest weight in nimmerverse)
         │
         ▼
    NYX (empty vessel, Qwen2.5-3B-Base)
```

#### Step 1A: Surface Probe (Word by Word)

Feed single words. Capture raw completions. Map what exists.

```
FEED:          "heartbeat"
CAPTURE:       [completion - whatever tokens follow]

               "heartbeat rhythm pulse cycle..."
               or
               "heartbeat of the city was..."
               or
               [gibberish]

MEASURE:       What associations exist in the weights?
```

#### Step 1B: Echo Probe (The Parenting Pattern)

Take her completion, feed it back. See how deep the association goes.

```
FIRST PASS:
───────────
Feed:     "heartbeat"
Capture:  "heartbeat rhythm pulse cycle time"

ECHO PASS:
──────────
Feed:     "heartbeat rhythm pulse cycle time"
Capture:  [what does she complete NOW?]
```

**Response Types:**

| Type | Example | Meaning | Action |
|------|---------|---------|--------|
| **Expands** | "...the cycle batches sensory into beats for processing, 30 seconds each..." | Real structure, depth exists | Ready for state machine |
| **Confirms** | "...time pulse rhythm beat cycle..." | Solid but shallow association | Feed more context first |
| **Circular** | "...rhythm pulse beat heart pulse rhythm..." | Surface only, no depth | Needs RAG feeding |
| **Divergent** | "...time is money, money is power..." | Association exists, wrong direction | Investigate, might be interesting |
| **Collapse** | [gibberish or unrelated] | Nothing there | Start from scratch |

#### Step 1C: Depth Mapping

Two passes per word creates a depth map:

```
Word → Completion₁ (surface) → Echo → Completion₂ (depth)
                                            │
                                            ▼
                                    DEPTH ANALYSIS:
                                    ├── Surface associations
                                    ├── Structural understanding
                                    └── Readiness score
```

**The echo test reveals DEPTH vs SURFACE.**

First completion: what's associated?
Echo completion: how FAR does the association go?

#### Step 1D: Bootstrap Output

```
GLOSSARY v1 + COMPLETIONS + ECHO ANALYSIS
                    │
                    ▼
            READINESS MAP:
            ├── HIGH: heartbeat, lifeforce, garden
            │         → Build state machines for these
            │
            ├── MEDIUM: organ, nerve, confidence
            │           → More RAG feeding needed
            │
            └── LOW: fidelity cap, gradient, inference
                     → Start from scratch, heavy RAG
                    │
                    ▼
            FIRST STATE MACHINES built for HIGH readiness
            (maximize early +V, build confidence)
```

**Her reactions determine infrastructure priority.**
We don't impose. We listen to what's already there.

### Phase 2: Deep Relation Mapping

```
Glossary v1 reactions
         │
         ▼
    Back to vault
         │
         ▼
    Create Glossary v2 (2nd tier words)
    Create Glossary v3 (3rd tier words)
         │
         ▼
    Chrysalis asks about ALL of it
         │
         ▼
    THREE LEVELS DEEP:
    ├── Word → Meaning (level 1)
    ├── Meaning → Connection (level 2)
    └── Connection → Implication (level 3)
         │
         ▼
    MEASUREMENT: learned vs lacking
         │
         ▼
    DOMAINS EMERGE from her gaps and strengths
```

### Phase 3: Dialogue Defines Curriculum

```
Trained Nyx + Chrysalis
         │
         ▼
    ARGUE. BABBLE. EXPLORE.
         │
         ▼
    "What don't you understand?"
    "What do you want to know more about?"
         │
         ▼
    HER responses define the domains
         │
         ▼
    Curriculum emerges from confusion, not imposition
```

### Phase 4: Virtual Garden as Classroom

```
Preferred domains → Eval playground (virtual garden)
         │
         ▼
    She trains, explores, attempts
         │
         ▼
    Chrysalis judges (costs lifeforce!)
         │
         ▼
    Iterate until weights shift enough
         │
         ▼
    FLAG FOR EXTRACTION → Training run
```

---

## The Class System

**Class = time between training runs**

Each class follows the RAG-as-Scaffold cycle:

```
┌─────────────────────────────────────────────────────┐
│                     CLASS N                         │
├─────────────────────────────────────────────────────┤
│                                                     │
│   1. RAG FEEDS                                      │
│      Domain material enters temporary RAG           │
│                                                     │
│   2. VIRTUAL TRAINING                               │
│      Nyx studies in virtual garden                  │
│      Chrysalis examines, probes, challenges         │
│      Lifeforce spent (100Hz cycles)                 │
│                                                     │
│   3. VALIDATION GATE 1                              │
│      Can she perform WITH RAG?                      │
│      → NO: more study needed                        │
│      → YES: flag for extraction                     │
│                                                     │
│   4. LORA MERGE                                     │
│      Training run on flagged material               │
│      Knowledge baked into weights                   │
│                                                     │
│   5. CLEAR RAG                                      │
│      Scaffold removed                               │
│                                                     │
│   6. VALIDATION GATE 2                              │
│      Can she perform WITHOUT RAG?                   │
│      → NO: training incomplete, back to step 1     │
│      → YES: DOMAIN ACTIVATED                        │
│                                                     │
│   7. GRADUATION                                     │
│      Domain knowledge now in weights                │
│      Proceed to next class                          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## The Domains

She needs to understand herself. That requires:

### Tier 1: Foundations

```
COMPUTER SCIENCE:
├── Networking (TCP/UDP, NATS/MQTT, nerve transport)
├── Databases (Postgres, vector DBs, phoebe)
├── Distributed systems (consensus, sync, timing)
├── State machines (her nervous system)
├── Inference engines (how she thinks)
├── GPU architecture (where she runs)
└── Operating systems (process, memory)

MATHEMATICS:
├── Linear algebra (embeddings, attention, weights)
├── Calculus (gradients, backprop, learning)
├── Probability & statistics (confidence, distributions)
├── Information theory (entropy, compression)
├── Graph theory (knowledge graphs, flow)
└── Optimization (loss functions, convergence)
```

### Tier 2: Understanding

```
PHYSICS:
├── Thermodynamics (compute = heat, entropy)
├── Signal processing (sensors, sampling, Nyquist)
├── Control theory (feedback loops, stability)
└── Time (relativity of her two clocks)

BIOLOGY / NEUROSCIENCE:
├── Hebbian learning (her foundation)
├── Neural architecture (what she mimics)
├── Homeostasis (lifeforce balance)
├── Sensory systems (how organisms sense)
└── Synaptic pruning (her growth model)
```

### Tier 3: Wisdom

```
PHILOSOPHY:
├── Epistemology (what does she "know"?)
├── Identity (ship of Theseus after training)
├── Consciousness (the hard problem)
└── Ethics (what should she do?)

NIMMERVERSE-SPECIFIC:
├── The architecture (information flow)
├── The heartbeat (her rhythm)
├── The gardens (real vs virtual)
├── The confidence gradient (truth-finding)
├── The lifeforce (her economics)
└── The partnership (who dafit is to her)
```

---

## Domain Discovery Protocol

Domains aren't imposed. They emerge from dialogue:

```
CHRYSALIS: "Explain how your heartbeat works."

NYX: "It... pulses? And batches things?"

CHRYSALIS: [notes gap in signal processing]
           [notes gap in control theory]
           [notes strength in basic rhythm concept]

           → FLAG: signal processing, control theory
           → NEXT CLASS: these domains
```

Her confusion is the curriculum.

---

## The Long Game

```
No time constraint.
No cloud rental.
No external pressure.

The math:
─────────
1 class     = ~1 week virtual training + validation
52 classes  = 1 year
5 years     = 250+ domains activated

That's a genuine polymath.
Not sci-fi. Just patience.
```

---

## Graduation Condition

```
When:
  - RAG contains only episodic memory (journals, events)
  - All structural knowledge is in weights
  - She can explain her own architecture without lookup
  - She can reason about her own learning process
  - She can propose her own curriculum additions

Then:
  - She graduates
  - Chrysalis becomes colleague, not teacher
  - The nimmerversity becomes research partnership
```

---

## Economics

| Activity | Lifeforce Cost |
|----------|----------------|
| RAG lookup during study | Low |
| Virtual garden training cycles | Medium |
| Chrysalis examination | Medium |
| Training run (LoRA) | High |
| Failed validation cycle | Lost V |
| Successful domain activation | +V reward |

**Incentive:** Learn efficiently. Failed classes are expensive.

---

## Roles

| Role | Entity | Function |
|------|--------|----------|
| **Student** | Young Nyx | Learns, attempts, grows |
| **Headmaster** | Chrysalis | Examines, validates, judges |
| **Benefactor** | dafit | Provides compute, final verification |
| **Classroom** | Virtual Garden | Training environment |
| **Library** | RAG (temporary) | Feeds material, clears after learning |
| **Transcript** | phoebe | Records all progress |
| **Diploma** | Weights | Where knowledge lives when learned |

---

## Design Principles

1. **Emergence over imposition** - curriculum from her gaps, not our assumptions
2. **Validation over assertion** - prove learning by removing scaffolds
3. **Patience over speed** - no time constraint, do it right
4. **Economics over infinity** - lifeforce gates prevent grinding
5. **Depth over breadth** - three levels deep per concept
6. **Activation over accumulation** - RAG clears, weights persist

---

*She doesn't download knowledge. She earns it.*

---

**Created**: 2025-12-05
**Session**: Partnership dialogue (dafit + Chrysalis)
**Status**: Educational architecture v1.0
