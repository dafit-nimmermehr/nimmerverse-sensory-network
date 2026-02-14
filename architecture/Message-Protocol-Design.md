# Message Protocol Design: Router-Centric Architecture

> **ONE JOB:** THE WIRE — NATS topics, JSON schemas, bootstrap sequence.

## Overview

This document outlines the design for the Nimmerverse message protocol. The core principle: **the router is dumb infrastructure, not smart cognition.** All intelligence lives at the edges - in clients that connect to the router.

This follows the Unix philosophy: each component does one thing well. The router routes. Clients subscribe, publish, and think.

**Connection to Gateway:** The Escalation Service described in this document IS the Gateway (thalamus pattern). It implements the weight-based tier routing defined in [`Gateway-Architecture.md`](Gateway-Architecture.md).

---

## Core Principle: Dumb Core, Smart Edges

The router (NATS) is **dumb infrastructure** — it routes based on topic patterns and knows nothing about meaning. All intelligence lives at the edges: cells publish, the Escalation Service (Gateway) watches and routes, Nyx subscribes and thinks.

**Routing logic:** → [`Gateway-Architecture.md`](Gateway-Architecture.md) (tier routing, escalation patterns)

---

## Guiding Principles

1. **Dumb Core, Smart Edges**: The router has zero intelligence. All logic lives in clients.
2. **Clients are Equal**: Nyx is just another subscriber. So is the Command Center. So is the Escalation Service.
3. **Decoupling**: Publishers don't know who subscribes. Subscribers don't know who publishes.
4. **Hierarchy**: Topics follow a hierarchical structure for flexible pattern subscriptions.
5. **Lifeforce at the Edges**: The router doesn't track Lifeforce. Clients manage their own budgets.
6. **Fail Simple**: If the router dies, everything stops cleanly. No half-smart failures.

---

## Two Channels of Attention

Messages split into `nimmerverse.low.*` (background heartbeats) and `nimmerverse.high.*` (cognitive events). The Escalation Service promotes from low → high based on rules.

**Attention philosophy:** → [`Attention-Flow.md`](Attention-Flow.md) (budget allocation, preemption rules)

---

## Topic Hierarchy

```
nimmerverse.
├── low.                          # Low-attention channel
│   └── heartbeat.
│       └── <garden>.             # real | virtual
│           └── <entity_type>.    # cell | nerve | organ
│               └── <entity_id>   # e.g., distance_sensor_front
│
├── high.                         # High-attention channel
│   └── event.
│       └── <garden>.
│           └── <entity_type>.
│               └── <entity_id>
│
├── command.                      # Commands TO entities
│   └── <target>.
│       └── <command_type>
│
└── meta.                         # System-level messages
    ├── attention.focus           # Nyx's attention configuration
    ├── escalation.rules          # Escalation Service configuration
    └── health.                   # Client health/registration
```

---

## Message Schemas

### 1. `HeartbeatSignal` (Low-Attention)

Published by: Cells, Nerves, Organs
Subscribed by: Escalation Service, Command Center

**Topic:** `nimmerverse.low.heartbeat.<garden>.<entity_type>.<entity_id>`

```json
{
  "header": {
    "message_id": "uuid",
    "message_type": "HeartbeatSignal",
    "version": "1.0",
    "timestamp_real": "ISO8601",
    "timestamp_virtual": 123456
  },
  "body": {
    "entity_id": "distance_sensor_front",
    "status": "NOMINAL",
    "value": 25.5,
    "unit": "cm",
    "context": {
      "battery_pct": 85,
      "temperature_c": 22
    }
  }
}
```

**Status values:** `NOMINAL`, `WARNING`, `CRITICAL`, `OFFLINE`, `ERROR`

---

### 2. `StateChangeDetail` (High-Attention)

Published by: Cells/Nerves (when requested), Escalation Service (when escalating)
Subscribed by: Young Nyx, Command Center

**Topic:** `nimmerverse.high.event.<garden>.<entity_type>.<entity_id>`

```json
{
  "header": {
    "message_id": "uuid",
    "message_type": "StateChangeDetail",
    "version": "1.0",
    "timestamp_real": "ISO8601",
    "timestamp_virtual": 123456,
    "source_entity": {
      "id": "distance_sensor_front",
      "type": "cell",
      "layer": "1"
    },
    "correlation_id": "uuid",
    "escalated_by": "escalation_service"
  },
  "body": {
    "previous_state": "POLLING",
    "current_state": "REPORTING",
    "lifeforce_cost": 0.3,
    "outputs": {
      "distance_cm": 25.5,
      "confidence": 0.92,
      "raw_value": 456,
      "visual_state": [255, 0, 0, "Solid"]
    },
    "possible_actions": [
      {
        "action_id": "read_distance_history",
        "description": "Query historical distance data."
      },
      {
        "action_id": "trigger_nerve:collision_avoidance",
        "description": "Activate collision avoidance."
      }
    ],
    "trigger_reason": "distance < 30cm threshold"
  }
}
```

---

### 3. `AttentionFocus` (Nyx's Configuration)

Published by: Young Nyx
Subscribed by: Escalation Service

**This is how Nyx tells the Escalation Service what she cares about.** The router doesn't interpret this - it just delivers it to subscribers.

**Topic:** `nimmerverse.meta.attention.focus`

```json
{
  "header": {
    "message_id": "uuid",
    "message_type": "AttentionFocus",
    "version": "1.0",
    "timestamp_real": "ISO8601",
    "source_entity": {
      "id": "nyx_core",
      "type": "cognitive_core"
    }
  },
  "body": {
    "focus_mode": "EXPLORATION",
    "escalation_rules": [
      {
        "rule_id": "distance_alert_front",
        "source_pattern": "nimmerverse.low.heartbeat.real.cell.distance_sensor_*",
        "condition": "body.value < 30 AND body.status == 'NOMINAL'",
        "action": "escalate",
        "priority": 8
      },
      {
        "rule_id": "battery_critical",
        "source_pattern": "nimmerverse.low.heartbeat.real.cell.battery_*",
        "condition": "body.status == 'CRITICAL'",
        "action": "escalate_and_trigger",
        "trigger_nerve": "charging_seeking",
        "priority": 10
      }
    ],
    "direct_subscriptions": [
      "nimmerverse.high.event.real.cell.speech_stt"
    ],
    "default_action": "log_only"
  }
}
```

---

## Clients

**Publishers:** Cells, Nerves, Organs (publish heartbeats and state changes)
**Router:** NATS (dumb pipe, topic-based routing)
**Gateway/Escalation Service:** Watches low-attention, escalates to high-attention, routes to tiers

**Client architecture:** → [`Gateway-Architecture.md`](Gateway-Architecture.md) (routing tiers, Function Gemma boundary)

---

## Workflow: Message Flow

```
1. Cell publishes HeartbeatSignal
   └─→ Router delivers to: Escalation Service, Command Center

2. Escalation Service evaluates rules
   └─→ If condition matches: publishes StateChangeDetail to high-attention
   └─→ Router delivers to: Young Nyx, Command Center

3. Young Nyx processes StateChangeDetail
   └─→ Makes decision
   └─→ Publishes command to nimmerverse.command.<target>

4. Target nerve/cell receives command
   └─→ Executes action
   └─→ Publishes new HeartbeatSignal reflecting new state

5. Nyx adjusts attention (optional)
   └─→ Publishes new AttentionFocus
   └─→ Escalation Service updates its rules
```

---

## Advantages of Router-Centric Architecture

1. **Dumb core can't fail smart:** The router either works or crashes. No subtle bugs from misunderstood logic.

2. **Clients are replaceable:** Swap out the Escalation Service. Replace the Command Center. Nyx doesn't care.

3. **Testable in isolation:** Each client can be tested independently against a mock NATS.

4. **Observable:** Command Center sees everything by subscribing to `nimmerverse.>`.

5. **Scalable:** Add more cells, more nerves - just more publishers. Router handles it.

6. **Bootstrap-friendly:** Router exists before any intelligence. Escalation Service can start with hardcoded rules. Nyx connects later.

---

## Bootstrap Sequence

1. **Start Router (NATS)** - Infrastructure first
2. **Start Escalation Service** - With minimal hardcoded rules
3. **Start Cells/Nerves** - Begin publishing heartbeats
4. **Start Command Center** - Observe the system
5. **Start Young Nyx** - Connect, subscribe, begin cognition
6. **Nyx publishes AttentionFocus** - Takes control of her attention

The system can run at any step. Earlier steps are "reflexive" only. Nyx adds deliberation.

---

## Implementation Notes

**Router:** Use NATS (https://nats.io). Lightweight, fast, designed for this.
- Consider NATS JetStream for message persistence if needed
- Topic wildcards: `>` matches all, `*` matches one level

**Message Format:** JSON for human readability during development. Consider MessagePack or Protobuf for production if performance requires.

**Escalation Service:** Python asyncio daemon using `nats-py` and `simpleeval` for rule evaluation. Stateless except for current rules. Can be restarted without losing system state. (Go considered for future optimization if scale demands.)

**Command Center:** Godot application connecting to NATS via GDScript or native plugin.

---

**Version:** 1.1 | **Created:** 2025-12-13 | **Updated:** 2026-02-14

*"Dumb core, smart edges. The router routes. Clients think."*
