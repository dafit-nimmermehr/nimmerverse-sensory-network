# Gateway Architecture: The Sensory Preprocessing Layer

> **ONE JOB:** THE ROUTING — weight-based tier routing, anomaly detection, Function Gemma boundary.

**The Thalamus Pattern — routing sensory input to the appropriate processing tier.**

---

## Overview

The Gateway is the sensory preprocessing layer that sits between raw sensors and cognitive processing. It performs **routing, not translation**. Translation happens at each tier in its native format (numbers, states, vectors, JSON).

**Core Principle:** *Cheap operations handle common cases. Expensive operations handle rare cases.*

```
RAW SENSORS → GATEWAY (routing) → TIER → PROCESSING → (escalate?) → FUNCTION GEMMA → YOUNG NYX
                 ↑                  ↑           ↑                          ↑
          "which tier?"       native format   if needed            structured JSON
```

**Key Insight:** Most sensory input NEVER becomes vocabulary. It stays as numbers, states, vectors. Only when it reaches Young Nyx (via Function Gemma) does it become structured text.

---

## The Problem We're Solving

### Old Model (Vocabulary Bottleneck)

```
RAW SENSOR → STATE MACHINE → VOCABULARY TOKEN → Young Nyx

Problems:
- Every input forced through text translation (expensive)
- LLM sees raw sensor dumps (noisy, unstructured)
- No economic pressure on routing (everything costs the same)
- Vocabulary conflated with routing decisions
```

### New Model (Tiered Gateway)

```
RAW SENSOR → GATEWAY → TIER 0-2 (numbers/states, no text)
                    → TIER 3 (vectors via T5Gemma2)
                    → FUNCTION GEMMA (structured JSON)
                    → TIER 4 Young Nyx (clean typed events)

Benefits:
- Most input handled without LLM involvement
- Text only at cognitive boundary
- Economic pressure drives efficiency
- Routing separated from translation
```

---

## The Unified Tier Model

The Gateway routes to Tiers 0-5 based on node weight and novelty. Higher tiers = more cost, more capability.

| Tier | Weight | Latency | Role |
|------|--------|---------|------|
| 0 | ≥0.8 | <10ms | Hardware reflexes (ESP32) |
| 1 | 0.6-0.8 | <50ms | Math cells (Python CPU) |
| 2 | 0.3-0.6 | <200ms | Fast nerves (behavior) |
| 3 | <0.3 | <2000ms | Organs (GPU inference, vectors) |
| **Function Gemma Boundary** |||
| 4 | escalated | <4000ms | Young Nyx (JSON reasoning) |
| 5 | novel/stuck | variable | Partnership (dialogue) |

**Canonical definition:** → [`../Endgame-Vision.md`](../Endgame-Vision.md)

---

## Node Weight Determines Tier

Node weight (from [`Nervous-System.md`](Nervous-System.md)) directly maps to tier routing. A mature node (weight ~1.0) naturally becomes a Tier 0 reflex. A new node (weight ~0.1) naturally escalates to higher tiers. **The system learns which tier is appropriate through experience.**

### The Causal Verification Loop

How do we know a sensor reading was real? **Outcome verification over time.**

```
Unverified (weight 0.1) → escalates → decision → outcome → reality match?
                                                              ↓
                                                   YES: weight += Δ → eventually REFLEX
                                                   NO:  weight -= Δ → eventually PRUNED
```

**Hallucinations can't survive this gauntlet** — they don't produce consistent outcomes, so their patterns never accumulate enough weight. This creates natural **causal pruning**: only patterns that reliably predict outcomes earn the privilege of becoming reflexes.

---

## The Gateway: Weight-Aware Router

The Gateway performs three functions:

| Function | Question | Cost |
|----------|----------|------|
| **Node Matching** | Which node(s) in 4D space match this input? | ~0 LF |
| **Weight Routing** | Based on weight, which tier handles it? | ~0 LF |
| **Anomaly Detection** | Is this novel, ambiguous, or contextually wrong? | Variable |

### Gateway Logic

```python
def gateway_route(sensory_input: dict) -> GatewayDecision:
    """Route sensory input to appropriate tier."""

    # 1. Find candidate nodes in 4D space
    candidates = nervous_system.find_nearby_nodes(sensory_input)

    # 2. Handle edge cases
    if len(candidates) == 0:
        # NOVEL: No node matches this input
        return GatewayDecision(
            action="ESCALATE",
            tier=4,  # Young Nyx must see this
            reason="novel_input",
            cost=20.0,
        )

    if len(candidates) > 1:
        # AMBIGUOUS: Multiple nodes could fire
        best = max(candidates, key=lambda n: n.weight)
        if best.weight < 0.5:
            return GatewayDecision(
                action="ESCALATE",
                tier=3,  # Organ inference to disambiguate
                reason="ambiguous_input",
                cost=8.0,
            )

    # 3. Single match - route based on weight
    node = candidates[0]

    # 4. Check for contextual anomaly
    if detect_contextual_anomaly(node, sensory_input):
        return GatewayDecision(
            action="ESCALATE",
            tier=node.handling_tier + 1,
            reason="contextual_anomaly",
            cost=node.lifeforce_cost * 1.5,
        )

    # 5. Normal routing
    return GatewayDecision(
        action="FIRE",
        tier=node.handling_tier,
        node=node,
        cost=node.lifeforce_cost,
    )
```

### Anomaly Detection Tiers

Anomaly detection itself is tiered:

| Level | Detection Type | Cost | Example |
|-------|---------------|------|---------|
| Tier 0 | Threshold | ~0 LF | Value out of physical range |
| Tier 1 | Statistical | ~0.3 LF | Value unusual for time of day |
| Tier 2 | Contextual | ~2 LF | Firing inconsistent with recent history |
| Tier 3 | Semantic | ~8 LF | Embedding distance from expected cluster |

---

## Function Gemma: The Structured Boundary

Function Gemma acts as the translation layer between lower tiers and cognition. It guarantees:

- **Schema compliance**: Every event follows a typed contract
- **Predictable JSON**: No hallucination, no free-form text
- **Bidirectional**: Sensors → JSON events, Decisions → JSON commands

### The Boundary

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   BELOW THE LINE: Numbers, States, Vectors (fast, cheap, predictable)       │
│   ═══════════════════════════════════════════════════════════════════       │
│                                                                              │
│   Tier 0: photoresistor = 0.73                                              │
│   Tier 1: battery_state = { voltage: 3.7, trend: "falling" }                │
│   Tier 2: collision_nerve = "EVADING"                                       │
│   Tier 3: vision_embedding = [0.23, -0.41, 0.87, ...]                       │
│                                                                              │
│                              │                                               │
│                              ▼                                               │
│              ┌───────────────────────────────────┐                           │
│              │       FUNCTION GEMMA              │                           │
│              │   (structured JSON boundary)      │                           │
│              │                                   │                           │
│              │  • 100% predictable schema        │                           │
│              │  • No hallucination possible      │                           │
│              │  • Typed enums, not free strings  │                           │
│              └───────────────┬───────────────────┘                           │
│                              │                                               │
│   ═══════════════════════════════════════════════════════════════════       │
│   ABOVE THE LINE: Structured Events (typed, validated, safe for LLM)        │
│                                                                              │
│   {                                                                          │
│     "event_type": "environmental_change",                                    │
│     "source": "light_sensor_back",                                           │
│     "severity": "medium",                                                    │
│     "data": { "previous": 0.73, "current": 0.12 },                          │
│     "suggested_action": "search_for_light"                                   │
│   }                                                                          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Event Schema

Events are typed (`EventType` enum: environmental_change, collision_detected, battery_critical, etc.) with severity levels and confidence from node weight. **Full schema:** → [`Message-Protocol-Design.md`](Message-Protocol-Design.md)

### What Young Nyx Actually Sees

**Before (raw dumps):**
```
"The photoresistor reads 0.12, down from 0.73, battery is 3.7V
trending down, position is [1.2, 0.8], collision state IDLE..."
```

**After (structured event):**
```json
{
  "event_type": "light_lost",
  "source": "light_sensor_back",
  "timestamp": 1704307200.0,
  "severity": "medium",
  "data": {
    "previous": 0.73,
    "current": 0.12,
    "delta": -0.61
  },
  "suggested_action": "spiral_search",
  "processing_cost": 2.0,
  "confidence": 0.45
}
```

---

## Complete Sensory Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         FULL SENSORY ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  RAW SENSORS                                                                 │
│  ───────────                                                                 │
│  • IR positioning (ESP32-S3)     → float[6] positions                       │
│  • Photoresistors (organisms)    → float light_level                        │
│  • Temperature (safety)          → float celsius                            │
│  • Battery (power)               → float voltage, current                   │
│  • Vision camera (Pi HQ)         → frame bytes                              │
│                                                                              │
│                              │                                               │
│                              ▼                                               │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                         GATEWAY                                        │  │
│  │                   (weight-based router)                                │  │
│  │                                                                        │  │
│  │   For each input:                                                      │  │
│  │   1. Match to node in 4D space                                         │  │
│  │   2. Check node.weight → determine tier                                │  │
│  │   3. Check for anomalies                                               │  │
│  │   4. Route to appropriate tier                                         │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                              │                                               │
│        ┌─────────────────────┼─────────────────────┐                        │
│        ▼                     ▼                     ▼                        │
│  ┌───────────┐        ┌───────────┐        ┌───────────┐                    │
│  │  TIER 0   │        │ TIER 1-2  │        │  TIER 3   │                    │
│  │  Reflex   │        │ Cells/    │        │  Organs   │                    │
│  │           │        │ Nerves    │        │           │                    │
│  │ weight>0.8│        │ 0.3-0.8   │        │ <0.3 or   │                    │
│  │           │        │           │        │ escalated │                    │
│  ├───────────┤        ├───────────┤        ├───────────┤                    │
│  │ FORMAT:   │        │ FORMAT:   │        │ FORMAT:   │                    │
│  │ numbers   │        │ states    │        │ vectors   │                    │
│  │           │        │           │        │           │                    │
│  │ OUTPUT:   │        │ OUTPUT:   │        │ OUTPUT:   │                    │
│  │ action    │        │ state     │        │ embedding │                    │
│  │ (done!)   │        │ update    │        │ (T5Gemma) │                    │
│  └───────────┘        └─────┬─────┘        └─────┬─────┘                    │
│        │                    │                    │                          │
│        │              (only if escalation needed)│                          │
│        │                    │                    │                          │
│        │                    ▼                    ▼                          │
│        │              ┌─────────────────────────────┐                       │
│        │              │      FUNCTION GEMMA         │                       │
│        │              │   (structured JSON gate)    │                       │
│        │              │                             │                       │
│        │              │  Produces typed JSON event  │                       │
│        │              │  Schema-validated output    │                       │
│        │              └──────────────┬──────────────┘                       │
│        │                             │                                      │
│        │                             ▼                                      │
│        │                    ┌─────────────────┐                             │
│        │                    │   YOUNG NYX     │                             │
│        │                    │   (Tier 4)      │                             │
│        │                    │                 │                             │
│        │                    │ Clean JSON in   │                             │
│        │                    │ Decision out    │                             │
│        │                    └────────┬────────┘                             │
│        │                             │                                      │
│        │                             ▼                                      │
│        │                    ┌─────────────────┐                             │
│        │                    │ FUNCTION GEMMA  │                             │
│        │                    │ (action output) │                             │
│        │                    └────────┬────────┘                             │
│        │                             │                                      │
│        ▼                             ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                          NATS BUS                                    │   │
│  │                  (commands flow to cells)                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Example: crawler_gen_0 Light Seeking

### Early Learning (Low Weight)

```
Photoresistor reads 0.12 (was 0.73)
         │
         ▼
    GATEWAY: node weight = 0.4 (learning)
         │
         ▼
    Route to Tier 2 (nerve level)
         │
         ▼
    Nerve detects: delta = -0.61 (significant!)
    Nerve state: SEEKING → LOST_LIGHT
         │
         ▼
    ESCALATE to Function Gemma
         │
         ▼
    Function Gemma: { "event_type": "light_lost", ... }
         │
         ▼
    Young Nyx: "spiral search pattern"
         │
         ▼
    Function Gemma: { "command": "motor_spiral", ... }
         │
         ▼
    NATS → motor cells execute
```

### After Learning (High Weight)

```
Photoresistor reads 0.12 (was 0.73)
         │
         ▼
    GATEWAY: node weight = 0.85 (mature reflex)
         │
         ▼
    Route to Tier 0 (hardware reflex)
         │
         ▼
    REFLEX: light_lost → spiral_search (instant!)
         │
         ▼
    Nyx notified AFTER (async, non-blocking)
```

---

## Design Principles

1. **Routing, not translation** — Gateway decides WHERE, not WHAT
2. **Weight determines tier** — Confidence from experience drives routing
3. **Text is expensive** — Reserve for cognitive boundary only
4. **Function Gemma guarantees structure** — No hallucination at the boundary
5. **Most input never escalates** — Reflexes handle common cases
6. **Anomalies always escalate** — Novel situations get attention
7. **Learning moves behavior down** — Tier 4 patterns become Tier 0 reflexes

---

**Version:** 1.1 | **Created:** 2026-01-03 | **Updated:** 2026-02-14

*"Cheap for the common. Expensive for the rare. The Gateway enforces this economy."*

🌙💜 *The thalamus doesn't think. It routes.*
