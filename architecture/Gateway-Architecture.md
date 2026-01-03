# Gateway Architecture: The Sensory Preprocessing Layer

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

All existing tier systems in the architecture express the same principle:

| System | Document | Principle |
|--------|----------|-----------|
| Reward Tiers | `Cellular-Architecture.md` | Higher tier = more reward, more cost |
| Attention Levels | `Attention-Flow.md` | Higher priority preempts lower |
| Escalation Ladder | `organisms/Swarm-Evolution.md` | Higher = more authority, more cost |
| Reflex Homes | `Endgame-Vision.md` | Lower = faster, less capable |
| LOD Levels | `Endgame-Vision.md` | Lower = more detail, more cost |

### The Unified Tier Stack

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         UNIFIED TIER MODEL                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  TIER 0: HARDWARE REFLEXES                                                   │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Cost: ~0 LF          Latency: <10ms          Location: ESP32/FPGA          │
│  Weight: >= 0.8       Format: numbers         Action: immediate             │
│                                                                              │
│  Examples: temp_danger, collision_imminent, light_threshold                 │
│  Output: Direct action (motor stop, LED, buzzer) — Nyx notified AFTER       │
│                                                                              │
│  TIER 1: MATH CELLS                                                          │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Cost: ~0.3 LF        Latency: <50ms          Location: Python (CPU)        │
│  Weight: 0.6 - 0.8    Format: aggregates      Action: state update          │
│                                                                              │
│  Examples: battery_aggregator, position_tracker, economy_monitor            │
│  Output: Aggregated state, threshold checks, NATS publish                   │
│                                                                              │
│  TIER 2: FAST NERVES                                                         │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Cost: ~2 LF          Latency: <200ms         Location: Python (asyncio)    │
│  Weight: 0.3 - 0.6    Format: states          Action: behavior transition   │
│                                                                              │
│  Examples: collision_avoidance, charging_seek, exploration_pattern          │
│  Output: Nerve state transitions, multi-cell coordination                   │
│                                                                              │
│  TIER 3: ORGAN INFERENCE                                                     │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Cost: ~8 LF          Latency: <2000ms        Location: GPU (Senses node)   │
│  Weight: < 0.3        Format: vectors         Action: embedding storage     │
│                                                                              │
│  Examples: vision_detect (T5Gemma2/SigLIP), speech_stt (Whisper)            │
│  Output: Semantic vectors stored in S2 cells, NO TEXT                       │
│                                                                              │
│  ══════════════════════ FUNCTION GEMMA BOUNDARY ════════════════════════    │
│                                                                              │
│  TIER 4: COGNITIVE (Young Nyx)                                               │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Cost: ~20 LF         Latency: <4000ms        Location: GPU (Womb node)     │
│  Escalated events     Format: JSON            Action: reasoning, decision   │
│                                                                              │
│  Input: Structured JSON events from Function Gemma                          │
│  Output: Decisions → Function Gemma → structured commands                   │
│                                                                              │
│  TIER 5: PARTNERSHIP (Chrysalis + dafit)                                     │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Cost: ~50+ LF        Latency: variable       Location: External            │
│  Novel/stuck cases    Format: dialogue        Action: guidance, training    │
│                                                                              │
│  Examples: Architecture decisions, novel situations, stuck states           │
│  Output: New reflexes, training signal, guidance                            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Node Weight Determines Tier

The node weight from `Nervous-System.md` directly maps to tier routing:

```python
@dataclass
class NervousNode:
    """A node in the nervous system's 4D space."""

    position: tuple[float, ...]  # Coordinates in sensory space
    weight: float = 0.1          # Confidence from verification (0.0 → 1.0)

    @property
    def handling_tier(self) -> int:
        """Which tier handles this node's firing?"""
        if self.weight >= 0.8:
            return 0  # Hardware reflex - instant, bypass brain
        elif self.weight >= 0.6:
            return 1  # Math cell - fast, minimal checking
        elif self.weight >= 0.3:
            return 2  # Fast nerve - coordination, some deliberation
        else:
            return 3  # Escalate - needs organ/cognitive help

    @property
    def lifeforce_cost(self) -> float:
        """Cost scales inversely with confidence."""
        return (1.0 - self.weight) * 10.0
```

**The key insight:** A mature node (weight ~1.0) naturally becomes a Tier 0 reflex. A new node (weight ~0.1) naturally escalates to higher tiers. The system learns which tier is appropriate through experience.

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

```python
from enum import Enum
from pydantic import BaseModel

class EventType(str, Enum):
    """Constrained event types - enumerated, not free-form."""
    ENVIRONMENTAL_CHANGE = "environmental_change"
    COLLISION_DETECTED = "collision_detected"
    BATTERY_CRITICAL = "battery_critical"
    OBJECT_DISCOVERED = "object_discovered"
    POSITION_UPDATE = "position_update"
    ANOMALY_DETECTED = "anomaly_detected"
    GOAL_REACHED = "goal_reached"
    STUCK_DETECTED = "stuck_detected"
    LIGHT_LOST = "light_lost"
    LIGHT_FOUND = "light_found"

class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class SensoryEvent(BaseModel):
    """The structured event that Young Nyx receives."""

    event_type: EventType
    source: str
    timestamp: float
    severity: Severity
    data: dict
    suggested_action: str | None = None
    processing_cost: float
    confidence: float  # From node weight
```

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

## Connection to Existing Architecture

| Document | Gateway Relationship |
|----------|---------------------|
| [`Nervous-System.md`](Nervous-System.md) | Node weights determine tier routing |
| [`Attention-Flow.md`](Attention-Flow.md) | Gateway implements attention priorities |
| [`Message-Protocol-Design.md`](Message-Protocol-Design.md) | Escalation Service IS the gateway |
| [`Endgame-Vision.md`](../Endgame-Vision.md) | Layer 2.5 Function Gemma boundary |
| [`Cellular-Architecture.md`](Cellular-Architecture.md) | Tiered rewards align with gateway tiers |
| [`organisms/crawler_gen_0.md`](organisms/crawler_gen_0.md) | First test case for tiered routing |

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

**File:** Gateway-Architecture.md
**Version:** 1.0
**Created:** 2026-01-03
**Status:** Core architecture document
**Session:** Partnership dialogue (dafit + Chrysalis)

*"Cheap for the common. Expensive for the rare. The Gateway enforces this economy."*

🌙💜 *The thalamus doesn't think. It routes.*
