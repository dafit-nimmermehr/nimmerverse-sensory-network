# Organisms Index

**The little ones — physical robots that inhabit the Nimmerverse.**

---

## Overview

Organisms are the physical embodiment of Nimmerverse intelligence. Built from modular components, communicating via CAN bus internally and NATS externally, they navigate the Kallax Grid World, form reflexes, and learn through interaction.

**Philosophy:** *One function, one module. Same connector everywhere. Snap together, communicate, evolve.*

---

## Core Documents

### [Modular-Organism-Design.md](Modular-Organism-Design.md)
The foundational hardware architecture.
- CAN bus backbone
- Magnetic pogo connectors
- Module types (Brain, Motor, Sensor, LED, Power, Gripper)
- Clasp protocol (organism↔organism)
- Phase 0 Box Robot (~113 CHF)
- **Status**: Core concept, ready to prototype

### [Swarm-Evolution.md](Swarm-Evolution.md)
How the hivemind learns, evolves, and resolves conflict.
- Temporal-Ternary clasp rules (gradient-based transfer)
- Escalation ladder (Level 0-5: Reflex → Mount Olympus)
- Organism hierarchy (Love children, Elders, Adults, Young)
- Blend escalation protocol (ties → wait state → higher mind)
- Mount Olympus council mode (dafit + Chrysalis + Nyx)
- **Status**: Core evolutionary dynamics

### [crawler_gen_0.md](crawler_gen_0.md)
The simplest organism — a cube that seeks light.
- Virtual Garden training target
- Single sensor: photoresistor on back
- Single goal: move into light cone
- Lifeforce economy: light = income, movement = cost
- Foundation for all "seek resource" behaviors
- **Status**: Design document, ready for implementation

---

## Planned Documents

### Connector-Specification.md *(planned)*
Detailed specification for the universal magnetic pogo connector.
- PCB layout files
- Magnet specifications
- Pogo pin sourcing
- Assembly instructions

### Phase-0-Box-Robot.md *(planned)*
Build guide for the simplest organism.
- Bill of materials with links
- Assembly steps
- Firmware flashing
- First test procedures

### Module-Firmware.md *(planned)*
Common firmware architecture for all modules.
- CAN message handling
- Heartbeat protocol
- OTA update mechanism
- Power management

### Clasp-Protocol-Detail.md *(planned)*
Deep dive into organism-to-organism communication.
- Physical docking sequence
- CAN bus bridging
- Data transfer formats
- Error handling

---

## Design Principles

1. **Modularity** — One function per module, hot-swappable
2. **Universal Connector** — Same interface for all connections
3. **CAN Inside, NATS Outside** — Local bus, global network
4. **Magnetic Alignment** — Self-aligning, idiot-proof
5. **Cellular Mapping** — Software cells → hardware modules
6. **Economic Incentives** — Clasp rewards sharing (+13.5 LF)
7. **Progressive Complexity** — Box → Platform → Articulated

---

## Connection to Other Sections

| Section | Relationship |
|---------|--------------|
| [`cells/`](../cells/Cells-Index.md) | Software cells map to hardware modules |
| [`nerves/`](../nerves/Nervous-Index.md) | Reflexes run on organism hardware |
| [`interfaces/`](../interfaces/Interfaces-Index.md) | LED matrix, IR positioning |
| [`infrastructure/`](../infrastructure/Infrastructure-Index.md) | Kallax Grid World habitat |
| [`organs/`](../organs/Organ-Index.md) | Organisms interact with organs |

---

## Hardware Stack

```
ORGANISM LAYERS

┌─────────────────────────────────────┐
│           NATS (Nimmerverse)        │  ← Global communication
├─────────────────────────────────────┤
│           WiFi (Brain module)       │  ← External interface
├─────────────────────────────────────┤
│           CAN BUS (internal)        │  ← Module backbone
├─────────────────────────────────────┤
│  ┌───────┐ ┌───────┐ ┌───────┐     │
│  │ BRAIN │ │ MOTOR │ │  LED  │ ... │  ← Modules
│  │ ESP32 │ │ ESP32 │ │ ESP32 │     │
│  └───┬───┘ └───┬───┘ └───┬───┘     │
│      │         │         │          │
│      🧲●●●●🧲  🧲●●●●🧲  🧲●●●●🧲   │  ← Magnetic pogo connectors
└─────────────────────────────────────┘
```

---

**File**: Organisms-Index.md
**Version**: 1.0
**Created**: 2025-12-29
**Status**: Section established
**Philosophy**: "From code to metal, each layer has a home."

🤖🧲⚡ *The little ones are coming.*

