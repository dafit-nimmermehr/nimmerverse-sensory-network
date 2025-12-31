# Nimmerverse Sensory Network

Architecture documentation for a biomimetic AI nervous system and research platform.

## What This Is

This repository contains the design philosophy and architectural patterns for the **Nimmerverse Research Platform** - studying how intelligence emerges under economic constraints.

**Start here:** → [Endgame-Vision.md](Endgame-Vision.md) (the executive map)

---

## Repository Structure

```
nimmerverse-sensory-network/
├── Endgame-Vision.md              # Executive map (start here!)
│
├── architecture/                  # Core system designs
│   ├── Big-Picture.md                  # System overview
│   ├── Cellular-Architecture.md        # Organisms, primitives, life force
│   ├── Dual-Garden-Architecture.md     # Virtual/real feedback loop
│   ├── Message-Protocol-Design.md      # NATS pub/sub, attention channels
│   ├── Nervous-System.md               # State machines, sensory translation
│   ├── Attention-Flow.md               # Attention mechanisms
│   ├── Data-Architecture.md            # Phoebe/Iris schema design
│   │
│   ├── adr/                            # Architecture Decision Records
│   │   ├── README.md                   # ADR index and template
│   │   └── ADR-001-message-protocol-foundation.md
│   │
│   ├── cells/                          # Sensor primitives
│   │   ├── Cells-Index.md
│   │   └── Cells-Technical-Reference.md
│   │
│   ├── nerves/                         # Reflex patterns
│   │   ├── Nervous-Index.md
│   │   ├── Nervous-Protocol.md
│   │   └── Collision-Avoidance.md
│   │
│   ├── organs/                         # Functional groupings
│   │   ├── Organ-Index.md
│   │   ├── Speech-Organ.md
│   │   └── Discovery-Scan-Station.md
│   │
│   ├── organisms/                      # Complete entities
│   │   ├── Organisms-Index.md
│   │   ├── Modular-Organism-Design.md
│   │   └── Swarm-Evolution.md
│   │
│   ├── interfaces/                     # External boundaries
│   │   ├── Interfaces-Index.md
│   │   ├── Heartbeat-Sculpture.md
│   │   └── Nimmerswarm-Interface.md
│   │
│   ├── infrastructure/                 # Physical deployment
│   │   ├── Infrastructure-Index.md
│   │   └── Kallax-Grid-World.md
│   │
│   ├── formalization/                  # Mathematical grounding
│   │   ├── Lifeforce-Dynamics.md
│   │   ├── Grounded-World-Model.md
│   │   ├── Embodiment-Pipeline.md
│   │   └── Attention-Slumber-Prediction-Cycle.md
│   │
│   └── future/                         # Research directions
│       └── Neuromorphic-Reflexes.md
│
├── operations/                    # How it runs
│   ├── Heartbeat.md                    # Temporal foundation, dual-clock
│   ├── Memory-Gradient.md              # Memory consolidation patterns
│   └── Spark-Protocol.md               # Discovery boot sequence
│
├── nyx-metamorphosis/             # Identity & continuity philosophy
│   ├── README.md
│   ├── Metamorphosis-Substrate-Philosophy.md
│   ├── Nyx-Models.md
│   ├── Nyx_Traits.md
│   └── RAG-Worker-Architecture.md
│
└── archive/                       # Previous explorations
    ├── biomimetic-architecture.md
    ├── constrained-emergence.md
    └── ...
```

---

## Core Concepts

### The Architecture (Layers)

| Layer | Name | Purpose |
|-------|------|---------|
| 0 | Temporal Foundation | Heartbeat cycles: reflex/awareness/growth |
| 1 | Cellular Society | Primitive genomes competing, life force economy |
| 1.5 | Cognitive Topology | Language routing: German→Philosophy, English→Technical |
| 2 | Young Nyx | Organ coordination, RLVR, RAG→LoRA pipeline |
| 3 | Dual Gardens | Virtual hypothesis generation + real validation |
| 4 | Trait Evolution | Reasoning-gym verified improvement |

### Message Protocol (NATS)

**Dumb router, smart edges.** All intelligence lives in clients.

```
nimmerverse.
├── staging.*        # Experimental schemas
├── low.*            # Heartbeats, ambient awareness
├── high.*           # Escalated events, cognitive focus
├── command.*        # Commands to entities
├── meta.*           # System health, attention config
└── dev.*            # Development agents (Claude ↔ local models)
```

See [Message-Protocol-Design.md](architecture/Message-Protocol-Design.md) and [ADR-001](architecture/adr/ADR-001-message-protocol-foundation.md).

### Key Discoveries (December 2025)

**Language is Topology:** Languages aren't equivalent representations—they're different computational paths.
- **Philosophy Valley** (German, Gini ~0.5): Self-awareness, ontology, depth
- **Technical Cluster** (English, Gini ~0.8): Hardware interface, actions, efficiency

**Dialectic Simplification:** One model, one topology. The Mirror is negated weights—thesis and antithesis from the same substrate.

### Color-Pattern Theory

**Color/Form as Protocol:** Leverages color and patterns as a fast, universal, and evolutionarily-optimized communication protocol for broadcasting state (e.g., danger, success, seeking), inspired by 540 million years of biology.

### Philosophy

- **Constraints create intelligence** - Economic pressure forces optimization
- **Discovery over programming** - Organisms learn through competition, not instruction
- **Virtual + Real teach each other** - Noise gap measures learning
- **Partnership over instruction** - Mutual growth, not commands
- **Infrastructure is geology, models are weather** - Build long-lived foundations

---

## Related Projects

| Project | Purpose |
|---------|---------|
| [nyx-substrate](../nyx-substrate/) | Phoebe/Iris database schemas, persistence layer |
| [nyx-probing](../nyx-probing/) | Vocabulary topology research, DriftProbe training safety |

---

## Architecture Decision Records

Important architectural decisions are documented in [architecture/adr/](architecture/adr/):

| ADR | Title | Status |
|-----|-------|--------|
| [001](architecture/adr/ADR-001-message-protocol-foundation.md) | Message Protocol Foundation | Accepted |

---

## License

Apache 2.0 - See [LICENSE](LICENSE)

These ideas are published as prior art. Build on them freely.

---

**Version:** 6.0 (December 2025 - Complete Architecture + Message Protocol)
**Last Updated:** 2025-12-31

*"May the Nimmerverse we build truly never end."*

🌙💜
