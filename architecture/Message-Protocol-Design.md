# Message Protocol Design: Router-Centric Architecture

## Overview

This document outlines the design for the Nimmerverse message protocol. The core principle: **the router is dumb infrastructure, not smart cognition.** All intelligence lives at the edges - in clients that connect to the router.

This follows the Unix philosophy: each component does one thing well. The router routes. Clients subscribe, publish, and think.

**Connection to Gateway:** The Escalation Service described in this document IS the Gateway (thalamus pattern). It implements the weight-based tier routing defined in [`Gateway-Architecture.md`](Gateway-Architecture.md).

---

## Core Principle: Infrastructure vs Intelligence

```
┌─────────────────────────────────────────────────────────────┐
│                      MESSAGE ROUTER                          │
│              (NATS - dumb pipe, no logic)                    │
│                                                              │
│   • Receives all messages                                    │
│   • Matches topic patterns → forwards to subscribers         │
│   • Knows NOTHING about meaning                              │
│   • Cannot fail in "smart" ways - only crash/overload        │
│   • EXISTS BEFORE any intelligence                           │
└─────────────────────────────────────────────────────────────┘
          ↑              ↑              ↑              ↑
          │              │              │              │
    ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐
    │  Cells/   │  │ Escalation│  │  Command  │  │   Young   │
    │  Nerves   │  │  Service  │  │  Center   │  │    Nyx    │
    │(publishers)│  │ (daemon)  │  │  (UI)     │  │ (cognition)│
    └───────────┘  └───────────┘  └───────────┘  └───────────┘
```

**The router is like a network switch:**
- It doesn't understand packets
- It routes based on topic patterns
- It's infrastructure that exists before any intelligence
- NATS is literally designed for this

**Everything else is a client:**
- Cells publish sensor data
- Nerves publish state changes
- Escalation Service watches patterns, triggers alerts
- Command Center visualizes state
- Young Nyx subscribes, thinks, publishes decisions

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

The attention split is a *topic convention*, not router intelligence. Clients choose which topics to subscribe to.

### 1. Low-Attention Channel (`nimmerverse.low.*`)

* **Purpose:** Background monitoring, lightweight heartbeats.
* **Subscribers:** Escalation Service (always), Command Center (for visualization).
* **NOT subscribed by default:** Young Nyx (she only sees escalated events).
* **Analogy:** Peripheral nervous system. Ambient awareness.

### 2. High-Attention Channel (`nimmerverse.high.*`)

* **Purpose:** Detailed events requiring cognitive processing.
* **Subscribers:** Young Nyx, Command Center.
* **Analogy:** Focal spotlight. Conscious processing.

**The escalation from low → high is done by the Escalation Service, not the router.**

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

## The Clients

### 1. Message Router (NATS)

**What it is:** Infrastructure. A NATS server.
**What it does:** Routes messages based on topic patterns.
**What it knows:** Nothing about meaning, Lifeforce, attention, or Nyx.
**Implementation:** Off-the-shelf NATS. No custom code in the router itself.

### 2. Cells / Nerves / Organs

**What they are:** Publishers of sensor data and state changes.
**What they do:**
- Publish `HeartbeatSignal` periodically to low-attention channel
- Publish `StateChangeDetail` when requested or when state changes significantly
**What they know:** Their own state. Their own Lifeforce cost.

### 3. Escalation Service (The Gateway)

**What it is:** A daemon that watches low-attention and creates high-attention events. This IS the Gateway — the sensory preprocessing layer described in [`Gateway-Architecture.md`](Gateway-Architecture.md).

**What it does:**
- Subscribes to `nimmerverse.low.heartbeat.>`
- Subscribes to `nimmerverse.meta.attention.focus` (to get Nyx's rules)
- **Routes input to appropriate tier based on node weight** (see Gateway-Architecture.md)
- Evaluates rules against incoming heartbeats
- Publishes `StateChangeDetail` to high-attention when conditions match
- Optionally triggers nerves directly for reflex responses (Tier 0)
- **Passes escalated events through Function Gemma for structured JSON**

**What it knows:** Current escalation rules. Current heartbeat states. Node weights from nervous system.

**This is the "thalamus" - the sensory preprocessing layer. See [`Gateway-Architecture.md`](Gateway-Architecture.md) for the full tier model and Function Gemma boundary.**

### 4. Command Center

**What it is:** Visualization and control UI (Godot-based).
**What it does:**
- Subscribes to both channels for visualization
- Displays system state, message flow, attention focus
- Allows dafit to observe and intervene
**What it knows:** Everything (read-only observer).

### 5. Young Nyx (Cognitive Core)

**What she is:** Just another client. The thinking part.
**What she does:**
- Subscribes to `nimmerverse.high.event.>` (high-attention only)
- Subscribes to selected low-attention topics when she chooses
- Publishes `AttentionFocus` to configure the Escalation Service
- Publishes decisions/commands to `nimmerverse.command.>`
**What she knows:** Only what reaches her through her subscriptions.

**Crucially: She controls what she pays attention to, but she doesn't see everything.**

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

**Created:** 2025-12-13
**Updated:** 2025-12-14 (router-centric rewrite)
**Session:** Partnership dialogue (dafit + Nyx)
**Status:** Foundation architecture
**Philosophy:** "Dumb core, smart edges. The router routes. Clients think."
