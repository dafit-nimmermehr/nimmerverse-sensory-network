# Nimmerverse Sensory Network

Architecture documentation for a biomimetic AI nervous system and research platform.

> *"Cells emit waves. Gates correlate. Attention emerges."*

## What This Is

This repository contains the design philosophy and architectural patterns for the **Nimmerverse Research Platform** — a wave/gate architecture for studying how intelligence emerges under economic constraints.

**Start here:** → [Endgame-Vision.md](Endgame-Vision.md) (the executive map)

---

## Repository Structure

```
nimmerverse-sensory-network/
├── Endgame-Vision.md              # Executive map (start here!) v7.1
├── ROADMAP.md                     # Implementation phases + phoebe task queries
│
├── architecture/                  # Core system designs
│   ├── Temporal-Ternary-Gradient.md    # Ternary gates, why STABLE matters
│   ├── Gateway-Architecture.md         # Resonant gates, tier routing
│   ├── Cellular-Architecture.md        # Cells emit waves, nerves respond
│   ├── Dual-Garden-Architecture.md     # Virtual/Real learning loop
│   ├── Message-Protocol-Design.md      # NATS wire protocol, WaveSignal
│   ├── Nervous-System.md               # Wave → Gate → Node flow
│   ├── Attention-Flow.md               # Attention = OPEN gates
│   ├── Data-Architecture.md            # Phoebe schema (waves, gates, verification)
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

### The Wave/Gate Architecture

| Layer | Name | Purpose |
|-------|------|---------|
| 0 | Temporal | 30-second heartbeat, lifeforce budget |
| 1 | Cells | Emit waves with confidence + semantic content |
| 2 | Gates | Ternary resonant chambers (OPEN/STABLE/CLOSED) |
| 3 | Nerves | Behavioral patterns, respond to gate transitions |
| 4 | Gardens | Virtual (explore) + Real (verify) learning loop |
| 5 | Cognition | Young Nyx (qwen3:32b) via Function Gemma |

**Key Insight:** Attention is not allocated — it emerges from which gates are OPEN based on wave correlation.

**Physical Infrastructure:**
| Host | Role | GPU |
|------|------|-----|
| theia | Young Nyx (cognitive) | RTX PRO 6000 Blackwell 96GB |
| dioscuri | Senses (organs) | 2× RTX 4000 Ada 40GB |

Total: 136GB VRAM on K8s cluster with 10GbE jumbo frame interconnect.

### Message Protocol (NATS)

**Dumb router, smart edges.** Waves flow through NATS to gates.

```
{environment}.{garden}.{layer}.{domain}.{signal_type}

Examples:
dev.virtual.cells.distance.wave        # Cell emits wave
dev.virtual.gates.collision.transition # Gate state changes
dev.real.outcomes.feedback             # Verification outcome
prod.cognitive.nyx.request             # To Young Nyx
```

See [Message-Protocol-Design.md](architecture/Message-Protocol-Design.md) for full schema.

### Key Discoveries

**Ternary Gate Model (February 2026):** Binary logic doesn't model brains. You need OPEN - STABLE - CLOSED.
- **STABLE** is where learning happens (correlation accumulates)
- **Correlated waves** push gates toward OPEN
- **Reflexes** are earned (gate weight → 1.0)

**Wave Correlation (February 2026):** Attention isn't allocated — it emerges from which gates OPEN based on wave correlation.

**Sovereign Infrastructure (February 2026):** K8s cluster operational. 136GB GPU VRAM on 10GbE backbone.

### Philosophy

- **Cells emit, gates correlate** — Attention emerges, not allocated
- **STABLE is learning** — The resting state where patterns emerge
- **Constraints create intelligence** — Economic pressure forces optimization
- **Virtual explores, Real verifies** — The learning loop closes
- **Partnership over instruction** — Mutual growth, not commands

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

**Version:** 7.0 | **Created:** 2025-10-01 | **Updated:** 2026-02-14

*"Cells emit waves. Gates correlate. May the Nimmerverse truly never end."*

🌙💜
