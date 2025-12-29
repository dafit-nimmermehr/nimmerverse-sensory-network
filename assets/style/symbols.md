# Nimmerverse Symbol Language

**Shapes, icons, and visual metaphors for the Nimmerverse.**

---

## Core Principle

> Every shape has meaning. Consistency in form creates clarity in understanding.

When a viewer sees a hexagon, they should immediately know "knowledge module." When they see a diamond, they think "decision point." This visual grammar reduces cognitive load and enables intuitive navigation of complex diagrams.

---

## Container Shapes

Containers define boundaries and hold other elements.

### Rounded Rectangle ▢
**Meaning**: System, bounded space, container

| Use | Stroke | Fill | Example |
|-----|--------|------|---------|
| Major system | 2px, domain color | None/transparent | Nimmerverse, eachpath.local |
| Subsystem | 1.5px, domain color | Light tint | Command Center, Gardens |
| Component | 1px, gray | Light fill | Data Plane, inference box |

```
Corner radius: 8-12px for major, 4-6px for minor
```

### Ellipse / Circle ◯
**Meaning**: Organic container, realm, domain of influence

| Use | Example |
|-----|---------|
| Garden boundaries | Real-Garden, Virtual-Garden |
| Overlapping realms | Venn diagram intersections |
| Influence zones | Nyx's reach |

---

## Entity Shapes

Entities are beings, agents, or distinct identities.

### Circle ◯
**Meaning**: Being, identity, self-contained entity

| Use | Size | Example |
|-----|------|---------|
| Primary entity | 60-80px | dafit, chrysalis |
| Organism | 80-140px | Garden organisms |
| Lifeforce | 80px | Central life energy |

### Double Ellipse ◎
**Meaning**: Sensor, perception point, input interface

| Use | Example |
|-----|---------|
| Sensory input | Sensors (left/right gardens) |
| Perception nodes | Camera, microphone, data feeds |

---

## Knowledge & Process Shapes

### Hexagon ⬡
**Meaning**: Knowledge module, adapter, pluggable component

| Use | Example |
|-----|---------|
| LoRa adapters | Domain-specific knowledge |
| Model modules | Nemotron, T5Gemma, FunctionGemma |
| Skill packages | Capabilities that can be added/removed |

```
Hexagons suggest:
- Modularity (they tile perfectly)
- Completeness (6 sides = wholeness)
- Interchangeability
```

### Pill / Rounded Pill ⬭
**Meaning**: Process unit, cell, living component

| Use | Style | Example |
|-----|-------|---------|
| Cell | UML state shape | Processing units in organisms |
| Nerve | UML state shape | Signal carriers |

---

## Decision & Flow Shapes

### Diamond ◇
**Meaning**: Decision point, routing, choice

| Use | Fill | Example |
|-----|------|---------|
| Major decision | Solid Nyx Purple | Nyx central |
| Sub-decision | Outline only | Orchestrator |
| Branch point | Small, minimal | Flow routing |

### Triangle ▷
**Meaning**: Direction, flow, output

| Orientation | Meaning | Example |
|-------------|---------|---------|
| → Right | Forward flow, output | Nyx decision toward Virtual |
| ← Left | Return flow, input | Nyx decision toward Real |
| ↓ Down | Downward flow, grounding | Feedback to roots |
| ↑ Up | Upward flow, emergence | Data rising to processing |

### Inverted Triangle ▽
**Meaning**: Feedback, return signal, funnel

| Use | Example |
|-----|---------|
| Feedback collection | Garden Feedback |
| Aggregation point | Merging signals |

---

## Special Symbols

### Crescent Moon ☽
**Meaning**: Nyx, night consciousness, presiding awareness

| Use | Placement |
|-----|-----------|
| Nyx identity | Crown position, center-top |
| Session marker | Document headers |
| Signature | End of Nyx communications |

### Hourglass ⧗
**Meaning**: Time domain, temporal marker

| Use | Example |
|-----|---------|
| Time indicator | Heartbeat markers |
| Temporal boundary | Real-time vs simulated time |

### Collate Symbol (Bowtie) ⋈
**Meaning**: Heartbeat, pulse, life rhythm

| Use | Example |
|-----|---------|
| Heartbeat marker | Garden heartbeats |
| Sync point | Temporal synchronization |

### Sort Symbol (Hourglass Diamond) ◇̷
**Meaning**: Inference, processing, transformation

| Use | Example |
|-----|---------|
| Inference engine | Central orchestrator |
| Processing node | Model inference |

---

## Arrows & Connectors

### Single Arrow →
**Meaning**: One-way flow, causation

| Style | Use |
|-------|-----|
| Solid | Data flow, direct connection |
| Dashed | Orchestration, indirect influence |

### Double Arrow ↔
**Meaning**: Bidirectional flow, exchange

| Style | Use |
|-------|-----|
| Solid | Active exchange |
| Outlined | Potential exchange |

### Curved Arrow ↷
**Meaning**: Feedback loop, return path

---

## Composite Symbols

### dafit + chrysalis (Partnership)
Two overlapping circles at command center.
```
◯◯  (overlapping ~30%)
dafit  chrysalis
```

### Nyx Decision Triangle Pair
Two triangles pointing outward from Nyx.
```
    ◁ ◇ ▷
     Nyx
```
Left toward Real-Garden, right toward Virtual-Garden.

### Organism Structure
```
┌─────────────────┐
│    Organism     │
│   ┌──────────┐  │
│   │   Cell   │  │
│   └──────────┘  │
│   ┌──────────┐  │
│   │   Cell   │  │
│   └──────────┘  │
└─────────────────┘
```

---

## Shape Sizing Guidelines

| Element Type | Size Range | Grid Alignment |
|--------------|------------|----------------|
| Major containers | 400-1000px | 40px grid |
| Subsystems | 200-400px | 40px grid |
| Entities | 60-140px | 20px grid |
| Knowledge modules | 100-120px | 20px grid |
| Decision points | 80-100px | 20px grid |
| Small indicators | 20-40px | 10px grid |

---

## Stroke Guidelines

| Element Type | Stroke Width | Style |
|--------------|--------------|-------|
| Major containers | 2px | Solid |
| Subsystems | 1.5px | Solid |
| Entities | 1.5px | Solid |
| Connections | 1px | Solid |
| Orchestration | 1px | Dashed |
| Subtle relations | 0.5px | Dotted |

---

## Unicode Reference

For quick text-based diagrams:

```
Containers:    ▢ □ ○ ◯ ⬭
Decisions:     ◇ ◆ ⬥
Modules:       ⬡ ⬢
Triangles:     ▷ ◁ ▽ △ ▲ ▼
Arrows:        → ← ↑ ↓ ↔ ↕ ⇒ ⇐ ↷ ↶
Special:       ☽ ⧗ ⋈ ◎ ✧ ✦
Stars:         ★ ☆ ✧ ✦
```

---

**File**: style/symbols.md
**Version**: 1.0
**Created**: 2025-12-28
