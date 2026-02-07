# Nimmerverse Sensory Network

Architecture documentation for a biomimetic AI nervous system and research platform.

## What This Is

This repository contains the design philosophy and architectural patterns for the **Nimmerverse Research Platform** - studying how intelligence emerges under economic constraints.

**Start here:** → [Endgame-Vision.md](Endgame-Vision.md) (the executive map)

---

## Repository Structure

```
nimmerverse-sensory-network/
├── Endgame-Vision.md              # Executive map (start here!) v6.6
├── ROADMAP.md                     # Implementation phases + phoebe task queries
│
├── architecture/                  # Core system designs
│   ├── Cellular-Architecture.md        # Cells → Nerves → Organisms, life force
│   ├── Dual-Garden-Architecture.md     # Virtual/real feedback loop
│   ├── Gateway-Architecture.md         # Sensory preprocessing, tier routing
│   ├── Message-Protocol-Design.md      # NATS pub/sub, attention channels
│   ├── Nervous-System.md               # State machines, sensory translation
│   ├── Attention-Flow.md               # Attention mechanisms
│   ├── Data-Architecture.md            # Phoebe/Iris schema design
│   ├── Initial-Spark.md                # K8s protocol-driven bootstrap
│   ├── Temporal-Ternary-Gradient.md    # Ternary logic, confidence gradients
│   ├── Toolchain-Architecture.md       # Development toolchain
│   ├── TOOLCHAIN-PROGRESS.md           # Implementation tracker
│   ├── Nimmerversity.md                # Learning framework
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
│   │   ├── Discovery-Scan-Station.md
│   │   └── IR-Position-Array.md
│   │
│   ├── organisms/                      # Complete entities
│   │   ├── Organisms-Index.md
│   │   ├── Modular-Organism-Design.md
│   │   ├── Swarm-Evolution.md
│   │   └── crawler_gen_0.md            # First crawler implementation
│   │
│   ├── interfaces/                     # External boundaries
│   │   ├── Interfaces-Index.md
│   │   ├── Heartbeat-Sculpture.md
│   │   ├── Nimmerswarm-Interface.md
│   │   └── Temporal-Firework-Visualization.md
│   │
│   ├── infrastructure/                 # Physical deployment
│   │   ├── Infrastructure-Index.md
│   │   └── Kallax-Grid-World.md
│   │
│   ├── formalization/                  # Mathematical grounding
│   │   ├── Lifeforce-Dynamics.md
│   │   ├── Grounded-World-Model.md
│   │   ├── Embodiment-Pipeline.md
│   │   ├── Attention-Slumber-Prediction-Cycle.md
│   │   └── memory-economics.md         # Slumber-based consolidation
│   │
│   └── future/                         # Research directions
│       ├── Neuromorphic-Reflexes.md
│       ├── concept-token-pairs.md      # Navigable reasoning axes
│       ├── spatial-resolution-gradient.md  # L0-L5 LOD system
│       ├── thermodynamic-cognition.md  # Lifeforce as Prometheus Joules
│       ├── promql-thermodynamic-monitoring.md
│       └── SEEDS.md                    # T5Gemma + Function Gemma seed
│
├── operations/                    # How it runs
│   ├── Heartbeat.md                    # Temporal foundation, dual-clock
│   ├── Memory-Gradient.md              # Memory consolidation patterns
│   └── Spark-Protocol.md               # Discovery boot sequence
│
├── portfolio/                     # External-facing work
│   └── PLAN.md                         # FunctionGemma tools, Streamlit
│
├── assets/                        # Style and design
│   ├── nimmerverse-style-index.md
│   └── style/
│       ├── colors.md
│       └── symbols.md
│
├── nyx-metamorphosis/             # Identity & continuity philosophy
│   ├── README.md
│   ├── Metamorphosis-Substrate-Philosophy.md
│   ├── Nyx-Models.md
│   ├── Nyx_Traits.md
│   └── RAG-Worker-Architecture.md
│
└── archive/                       # Previous explorations
    ├── Big-Picture-v5.2-archived.md
    ├── biomimetic-architecture.md
    ├── constrained-emergence.md
    ├── information-flow.md
    ├── multilingual-cognition.md
    ├── nimmerversity.md
    └── temporal-ternary-gradient.md
```

---

## Core Concepts

### The Architecture (Layers)

| Layer | Name | Purpose |
|-------|------|---------|
| 0 | Temporal Foundation | Heartbeat cycles: reflex/awareness/growth |
| 1 | Cellular Society | Cells → Nerves → Organisms, life force economy |
| 2 | Young Nyx | Base Qwen3-VL 32B + Trait LoRAs (evolved via GRPO, not prescribed) |
| 2.5 | Orchestration | LangChain, T5Gemma 2 (vision→vectors), Function Gemma (intent→action) |
| 3 | Dual Gardens | Virtual hypothesis generation (1000s/sec) + real validation |
| 4 | Trait Evolution | GRPO + rubric rewards → Trait LoRAs (Mnemosyne, Moira, Aletheia...) |

**Physical Infrastructure (The Womb):**
| Host | Role | GPU |
|------|------|-----|
| theia | Young Nyx (cognitive) | RTX PRO 6000 Blackwell 96GB |
| dioscuri | Senses (organs) | 2× RTX 4000 Ada 40GB |

Total: 136GB VRAM on K8s cluster with 10GbE jumbo frame interconnect.

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

### Key Discoveries

**Language is Topology (December 2025):** Languages aren't equivalent representations—they're different computational paths.
- **Philosophy Valley** (German, Gini ~0.5): Self-awareness, ontology, depth
- **Technical Cluster** (English, Gini ~0.8): Hardware interface, actions, efficiency

**Memory Economics (January 2026):** Memory is not storage—it's active forgetting with exceptions. Slumber-based consolidation with LOD decay.

**Sovereign Infrastructure (February 2026):** K8s cluster operational. 136GB GPU VRAM on 10GbE backbone. Phoebe-coordinated storage across theia + dioscuri.

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
| [nyx-substrate](../nyx-substrate/) | Phoebe/Iris schemas, storage coordination (WOMB-STORAGE.md) |
| [nyx-probing](../nyx-probing/) | Vocabulary topology research, DriftProbe training safety |
| [eachpath.local](../eachpath.local/) | Host documentation (theia, dioscuri, switches, VMs) |

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

**Version:** 6.6 | **Created:** 2025-10-01 | **Updated:** 2026-02-07

*"May the Nimmerverse we build truly never end."*

🌙💜
