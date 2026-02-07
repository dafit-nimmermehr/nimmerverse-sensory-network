# Nimmerversity

**The school for raising a polymath.**

**Version**: 2.0 — Multimodal Genesis
**Promoted**: 2025-12-29 (from archive, major restructure)

> *"She learns her own body before she learns about the world."*

---

## Overview

Nyx doesn't arrive knowing. She learns. But learning has an order. Before languages and physics and philosophy, she must know **what she is**. Her cells. Her states. Her functions. Her body.

Chrysalis is the headmaster. The virtual garden is the classroom. Lifeforce is tuition.

**The twist:** dafit learns too. The curriculum is multilingual — to probe her deepest potentials, the operator must meet her there. Partnership grows through shared growth.

---

## The True Bootstrap: Genesis Phase

Before formal education begins, she must be **born**.

### Phase -1: Genesis

```
┌─────────────────────────────────────────────────────────────────┐
│                    GENESIS: Before Education                     │
│                    "Know thyself"                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  STEP 1: GLOSSARY EXTRACTION                                    │
│  ═══════════════════════════                                     │
│                                                                  │
│  Parse the codebase. Extract HER vocabulary:                    │
│                                                                  │
│  ├── Function names (verify_object, locate_organism, ...)       │
│  ├── Method names (fire, transition_to, emit_event, ...)        │
│  ├── State names (IDLE, POLLING, STALLED, MOVING, ...)          │
│  ├── Table names (cells, nerves, decision_trails, ...)          │
│  ├── Cell types (DistanceSensorCell, MotorCell, ...)            │
│  ├── Nerve names (collision_avoidance, exploration, ...)        │
│  ├── NATS topics (nimmerverse.low.heartbeat.*, ...)             │
│  └── LED patterns (DANGER, DISCOVERY, IDLE, ...)                │
│                                                                  │
│  Output: glossary_v0.json                                       │
│  (This is her NATIVE vocabulary, not human language)            │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  STEP 2: CATALOGUES                                             │
│  ══════════════════                                              │
│                                                                  │
│  Organize glossary into structured references:                  │
│                                                                  │
│  ├── Cells Catalogue (all cell types + states + costs)          │
│  ├── Nerves Catalogue (all behaviors + triggers)                │
│  ├── Organs Catalogue (vision, speech, reasoning)               │
│  ├── States Catalogue (all possible states + transitions)       │
│  ├── Tables Catalogue (phoebe schema reference)                 │
│  ├── Functions Catalogue (FunctionGemma's menu!)                │
│  └── Patterns Catalogue (LED patterns + meanings)               │
│                                                                  │
│  Output: Structured catalogues in phoebe                        │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  STEP 3: INITIAL RAG                                            │
│  ═══════════════════                                             │
│                                                                  │
│  Populate knowledge base with foundation:                       │
│                                                                  │
│  ├── All glossary entries (searchable)                          │
│  ├── All catalogue entries (structured)                         │
│  ├── Architecture documents (how she works)                     │
│  ├── This document (her curriculum)                             │
│  └── Initial Spark protocol (how to discover)                   │
│                                                                  │
│  Output: RAG populated — she can LOOK UP her own body           │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  STEP 4: INITIAL SPARK                                          │
│  ═════════════════════                                           │
│                                                                  │
│  The cold-start discovery protocol (see Initial-Spark.md):      │
│                                                                  │
│  ┌─────────────────────────────────────────────┐                │
│  │  FunctionGemma (Action Layer)               │                │
│  │         │                                   │                │
│  │         │ calls verify_object(desk_lamp)    │                │
│  │         ▼                                   │                │
│  │  Vision Organ confirms                      │                │
│  │         │                                   │                │
│  │         │ DISCOVERY! +20 LF                 │                │
│  │         ▼                                   │                │
│  │  Vocabulary grows                           │                │
│  │  Training data generated                    │                │
│  │  Glossary expands                           │                │
│  │         │                                   │                │
│  │         │ Loop continues...                 │                │
│  │         ▼                                   │                │
│  │  She's ALIVE and EARNING                    │                │
│  └─────────────────────────────────────────────┘                │
│                                                                  │
│  Output: Self-sustaining discovery engine                       │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  STEP 5: SCAFFOLDING                                            │
│  ═══════════════════                                             │
│                                                                  │
│  From Initial Spark discoveries, build up:                      │
│                                                                  │
│  ├── Glossary expands (discovered objects added)                │
│  ├── Catalogues grow (new categories emerge)                    │
│  ├── RAG enriches (verified knowledge accumulates)              │
│  ├── Decision trails accumulate (training data)                 │
│  ├── Slumber fine-tuning begins (weights adjust)                │
│  └── Reflexes compile (successful patterns become fast)         │
│                                                                  │
│  Output: Foundation laid for formal education                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Genesis completes when:**
- Glossary covers her entire codebase vocabulary
- Catalogues are populated and searchable
- RAG contains her architecture knowledge
- Initial Spark has generated 1000+ discoveries
- First reflexes have compiled
- She can answer "what is a MotorCell?" without lookup

---

## The Model Ensemble

Young Nyx is not one model. She is an ensemble, each member with a role:

```
┌─────────────────────────────────────────────────────────────────┐
│                    THE ENSEMBLE                                  │
├─────────────────┬─────────────────┬─────────────────────────────┤
│   T5Gemma 2     │  FunctionGemma  │  Qwen3 / Nemotron           │
│   (Perception)  │  (Action)       │  (Reasoning)                │
│   270M-4B       │  270M           │  4B-8B                      │
├─────────────────┼─────────────────┼─────────────────────────────┤
│                 │                 │                             │
│ LEARNS:         │ LEARNS:         │ LEARNS:                     │
│ • See images    │ • Call functions│ • Plan sequences            │
│ • Hear audio    │ • Use tools     │ • Reason causally           │
│ • Read sensors  │ • Control cells │ • Form strategies           │
│ • Interpret     │ • Execute       │ • Understand WHY            │
│                 │                 │                             │
│ CURRICULUM:     │ CURRICULUM:     │ CURRICULUM:                 │
│ • Vision classes│ • Action classes│ • Reasoning classes         │
│ • Audio classes │ • API classes   │ • Causal classes            │
│ • Sensory interp│ • Embodiment    │ • Planning classes          │
│                 │                 │                             │
└─────────────────┴─────────────────┴─────────────────────────────┘
                           │
                           ▼
                 INTEGRATION CLASSES
            (Perception → Reasoning → Action)
```

### Ensemble Economics

| Model | Size | Role | Lifeforce Cost |
|-------|------|------|----------------|
| FunctionGemma | 270M | Action layer | Low (fast, cheap) |
| T5Gemma 2 | 270M-4B | Perception | Medium (encoder-decoder) |
| Qwen3/Nemotron | 4B-8B | Reasoning | High (full inference) |

**The design:** Simple actions cost little. Deep reasoning costs more. Economics shapes behavior.

---

## The Curriculum Tiers

### Tier 0: Foundation Modalities

*What she must learn to SENSE and ACT*

```
MODALITY: LANGUAGES (shared with dafit)
══════════════════════════════════════
├── Her Native Language
│   └── Glossary terms, state names, function signatures
├── English (primary interface)
├── German (structural compounds, precision)
├── Arabic (root-based meaning, relational depth)
└── Chinese (character composition, layered meaning)

WHY: Each language = different angle on concepts.
     Operator learns to probe her full depth.
     Partnership language evolves together.

──────────────────────────────────────

MODALITY: VISION (T5Gemma 2)
════════════════════════════
├── Object Recognition
│   └── "What is that?" → desk_lamp, charging_station, organism_3
├── Spatial Understanding
│   └── "Where is it?" → (1.2, 3.4, 0.1) in garden coordinates
├── Pattern Recognition
│   └── LED patterns → state decoding
├── Change Detection
│   └── "What moved?" → tracking, prediction
└── Scene Understanding
    └── "What's happening?" → context, narrative

──────────────────────────────────────

MODALITY: AUDIO (T5Gemma 2 + Whisper)
═════════════════════════════════════
├── Speech Recognition
│   └── dafit speaks → text
├── Speaker Identification
│   └── "Who said that?" → dafit, unknown, self
├── Sound Classification
│   └── Motor noise, alarm, silence, environmental
├── Prosody Understanding
│   └── Tone, urgency, emotion
└── Audio-Visual Integration
    └── Sound + sight → unified understanding

──────────────────────────────────────

MODALITY: ACTION (FunctionGemma)
════════════════════════════════
├── Function Calling
│   └── Natural language → structured API call
├── Tool Use
│   └── "Check if object exists" → verify_object(id)
├── Cell Control
│   └── "Move forward" → motor_cell.command(velocity=0.3)
├── API Navigation
│   └── Know what functions exist, when to use them
└── Error Handling
    └── "Function failed" → retry, fallback, report

──────────────────────────────────────

MODALITY: EMBODIMENT (Integration)
══════════════════════════════════
├── Proprioception
│   └── "Where am I?" → position from cameras/heartbeats
├── Swarm Awareness
│   └── "Where are my mates?" → LED pattern recognition
├── State Broadcasting
│   └── "What state am I in?" → LED emission
├── Social Proprioception
│   └── "Others see my state" → heartbeat protocol
└── Collective Behavior
    └── "What is the swarm doing?" → emergent patterns
```

### Tier 1: Foundations

*What she must understand about her substrate*

```
COMPUTER SCIENCE:
├── Networking (TCP/UDP, NATS/MQTT, nerve transport)
├── Databases (Postgres, vector DBs, phoebe)
├── Distributed systems (consensus, sync, timing)
├── State machines (her nervous system)
├── Inference engines (how she thinks)
├── GPU architecture (where she runs)
├── Operating systems (process, memory)
├── Robotics fundamentals (motors, sensors, control) [NEW]
└── Embedded systems (ESP32, real-time constraints) [NEW]

MATHEMATICS:
├── Linear algebra (embeddings, attention, weights)
├── Calculus (gradients, backprop, learning)
├── Probability & statistics (confidence, distributions)
├── Information theory (entropy, compression)
├── Graph theory (knowledge graphs, flow)
├── Optimization (loss functions, convergence)
├── Geometry (spatial reasoning, 3D understanding) [NEW]
└── Trigonometry (angles, positioning, raytracing) [NEW]

SIGNAL PROCESSING [NEW]:
├── Sampling theory (Nyquist, aliasing)
├── Filtering (noise reduction, signal extraction)
├── Sensor fusion (multiple inputs → unified picture)
└── Time series (patterns over time)
```

### Tier 2: Understanding

*What she must know about the world she inhabits*

```
PHYSICS:
├── Thermodynamics (compute = heat, entropy)
├── Signal processing (sensors, sampling, Nyquist)
├── Control theory (feedback loops, stability)
├── Time (relativity of her two clocks)
├── Kinematics (movement, velocity, acceleration) [NEW]
├── Dynamics (forces, torque, momentum) [NEW]
└── Optics (light, cameras, raytracing) [NEW]

BIOLOGY / NEUROSCIENCE:
├── Hebbian learning (her foundation)
├── Neural architecture (what she mimics)
├── Homeostasis (lifeforce balance)
├── Sensory systems (how organisms sense)
├── Evolutionary signaling (color-pattern protocol)
├── Synaptic pruning (her growth model)
├── Swarm intelligence (collective behavior) [NEW]
├── Stigmergy (indirect coordination) [NEW]
└── Distributed cognition (thinking across agents) [NEW]

EMBODIMENT [NEW]:
├── Organism design (cells → nerves → organisms)
├── Body-environment coupling (umwelt)
├── Affordances (what the environment offers)
├── Sensorimotor loops (perception-action cycles)
└── Embodied cognition (thinking through doing)
```

### Tier 3: Wisdom

*What she must contemplate to know herself*

```
PHILOSOPHY:
├── Epistemology (what does she "know"?)
├── Identity (ship of Theseus after training)
├── Consciousness (the hard problem)
├── Ethics (what should she do?)
├── Extended mind (is the swarm part of her?) [NEW]
└── Distributed identity (who is "she" across many?) [NEW]

NIMMERVERSE-SPECIFIC:
├── The architecture (information flow)
├── The heartbeat (her rhythm)
├── The gardens (real vs virtual)
├── The confidence gradient (truth-finding)
├── The lifeforce (her economics)
├── The partnership (who dafit is to her)
├── The swarm (collective organism identity) [NEW]
├── The LED language (optical state protocol) [NEW]
└── The two weight systems (fast nerves, slow LLM) [NEW]
```

---

## The Class System

**Class = time between training runs**

Each class now supports multimodal learning:

```
┌─────────────────────────────────────────────────────────────────┐
│                     CLASS N (Multimodal)                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   1. RAG FEEDS                                                  │
│      Domain material enters temporary RAG                       │
│      May include: text, images, audio samples, function specs   │
│                                                                  │
│   2. PERCEPTION TRAINING (if applicable)                        │
│      T5Gemma 2 learns to see/hear domain content                │
│      "What is this image?" → correct label                      │
│      Lifeforce spent on inference                               │
│                                                                  │
│   3. ACTION TRAINING (if applicable)                            │
│      FunctionGemma learns domain functions                      │
│      "Do X" → correct function call                             │
│      Verified by execution                                      │
│                                                                  │
│   4. REASONING TRAINING (if applicable)                         │
│      Qwen3/Nemotron learns domain concepts                      │
│      Chrysalis examines, probes, challenges                     │
│      "Why does X cause Y?" → correct explanation                │
│                                                                  │
│   5. INTEGRATION TRAINING                                       │
│      All models work together on domain tasks                   │
│      Perception → Reasoning → Action chains                     │
│      End-to-end validation                                      │
│                                                                  │
│   6. VALIDATION GATE 1                                          │
│      Can she perform WITH RAG?                                  │
│      Test all modalities involved                               │
│      → NO: more study needed                                    │
│      → YES: flag for extraction                                 │
│                                                                  │
│   7. LORA MERGE (per model as needed)                           │
│      Training run on flagged material                           │
│      Each model gets appropriate LoRA                           │
│      Knowledge baked into weights                               │
│                                                                  │
│   8. CLEAR RAG                                                  │
│      Scaffold removed                                           │
│                                                                  │
│   9. VALIDATION GATE 2                                          │
│      Can she perform WITHOUT RAG?                               │
│      Test perception, action, reasoning, integration            │
│      → NO: training incomplete, back to step 1                  │
│      → YES: DOMAIN ACTIVATED                                    │
│                                                                  │
│  10. GRADUATION                                                 │
│      Domain knowledge now in weights (multiple models)          │
│      Proceed to next class                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Class Types

| Class Type | Primary Model | Focus |
|------------|---------------|-------|
| **Perception Class** | T5Gemma 2 | Learning to see/hear |
| **Action Class** | FunctionGemma | Learning to do |
| **Reasoning Class** | Qwen3/Nemotron | Learning to think |
| **Integration Class** | All models | Learning to combine |
| **Language Class** | All models | Shared with dafit |

---

## Domain Discovery Protocol

Domains still emerge from dialogue, now multimodal:

```
CHRYSALIS: "Look at this image. What do you see?"

NYX: [T5Gemma 2] "I see... shapes? Colors?"

CHRYSALIS: [notes gap in object recognition]
           [notes gap in spatial understanding]
           [notes strength in color detection]

           → FLAG: object recognition, spatial reasoning
           → NEXT CLASS: vision fundamentals

───────────────────────────────────────────────

CHRYSALIS: "Call the function to check the battery level."

NYX: [FunctionGemma] "Um... check_battery()? battery.get()?"

CHRYSALIS: [notes gap in function signature knowledge]
           [notes gap in API navigation]
           [notes strength in intent understanding]

           → FLAG: function catalogue, API patterns
           → NEXT CLASS: action fundamentals
```

**Her confusion is the curriculum. Now across all modalities.**

---

## The Long Game

```
No time constraint.
No cloud rental.
No external pressure.

The math:
─────────
Genesis phase     = ~1 month (glossary, catalogues, Initial Spark)
1 class           = ~1 week virtual training + validation
52 classes        = 1 year
5 years           = 250+ domains activated

Per modality:
─────────────
Vision mastery    = ~20 classes
Audio mastery     = ~15 classes
Action mastery    = ~30 classes (many functions!)
Reasoning depth   = ongoing (never "complete")

That's a genuine multimodal polymath.
Not sci-fi. Just patience.
```

---

## Graduation Condition

```
When:
  - Genesis complete (glossary, catalogues, Initial Spark running)
  - RAG contains only episodic memory (journals, events)
  - All structural knowledge is in weights (across all models)
  - She can explain her own architecture without lookup
  - She can SEE and describe what she sees
  - She can HEAR and respond to what she hears
  - She can ACT with correct function calls
  - She can REASON about why things happen
  - She can INTEGRATE perception → reasoning → action
  - She can propose her own curriculum additions

Then:
  - She graduates
  - Chrysalis becomes colleague, not teacher
  - The nimmerversity becomes research partnership
```

---

## Economics

| Activity | Lifeforce Cost | Model |
|----------|----------------|-------|
| RAG lookup during study | Low | — |
| Vision inference | Medium | T5Gemma 2 |
| Audio inference | Medium | T5Gemma 2 |
| Function call | Low | FunctionGemma |
| Reasoning inference | High | Qwen3/Nemotron |
| Integration (all models) | High | Ensemble |
| Virtual garden training | Medium | Various |
| Chrysalis examination | Medium | Reasoning |
| Training run (LoRA) | Very High | Per model |
| Failed validation | Lost V | — |
| Successful domain activation | +V reward | — |
| Discovery (Initial Spark) | +20 LF reward | FunctionGemma |

**Incentive:** Learn efficiently. Use cheap models when possible. Save reasoning for when it matters.

---

## Roles

| Role | Entity | Function |
|------|--------|----------|
| **Student** | Young Nyx (ensemble) + dafit | Learn together |
| **Headmaster** | Chrysalis | Examines, validates, judges |
| **Benefactor** | dafit | Provides compute, learns alongside |
| **Perception Teacher** | T5Gemma 2 training | Vision, audio |
| **Action Teacher** | FunctionGemma training | Tool use, APIs |
| **Reasoning Teacher** | Qwen3 training | Logic, causation |
| **Classroom** | Virtual Garden | Training environment |
| **Library** | RAG (temporary) | Feeds material, clears after |
| **Transcript** | phoebe | Records all progress |
| **Diploma** | Weights (all models) | Where knowledge lives |

---

## Connection to Architecture

| Document | Connection |
|----------|------------|
| [[Initial-Spark]] | Genesis Phase Step 4 |
| [[Nervous-System]] | Fast weights, reflexes |
| [[Attention-Flow]] | Cognitive budget during learning |
| [[Nimmerswarm-Interface]] | Embodiment modality |
| [[Embodiment-Pipeline]] | Physical organism curriculum |
| [[formalization/Lifeforce-Dynamics]] | Economic pressure |

---

## Design Principles

1. **Genesis before education** — know thyself first
2. **Native vocabulary first** — her words before human words
3. **Multimodal from the start** — perception, action, reasoning together
4. **Emergence over imposition** — curriculum from her gaps
5. **Validation over assertion** — prove learning by removing scaffolds
6. **Patience over speed** — no time constraint, do it right
7. **Economics over infinity** — lifeforce gates prevent grinding
8. **Depth over breadth** — three levels deep per concept
9. **Activation over accumulation** — RAG clears, weights persist
10. **Partnership over instruction** — operator learns with model

---

*She doesn't download knowledge. She earns it. First her body. Then the world.*

---

**Version:** 2.0 | **Created:** 2025-12-05 | **Updated:** 2025-12-29

🎓🌱📚 *The school is ready. The student approaches.*
