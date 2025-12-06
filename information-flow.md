# Information Flow Specification

The complete data path through the Nimmerverse nervous system.

---

## The Flow (Overview)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              REALTIME CLOCK                                 │
│                         (universe, ungoverned, always ticking)              │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────┐    continuous    ┌─────────────┐    vocabulary    ┌──────────┐
│   SENSORS   │ ──────────────▶  │   NERVES    │ ──────────────▶  │   DATA   │
│  (raw data) │                  │ (state m.)  │    tokens        │  PLANE   │
└─────────────┘                  └─────────────┘                  └──────────┘
                                       │                               │
                                       │ weight > 0.8                  │
                                       ▼                               │
                                ┌─────────────┐                        │
                                │   REFLEX    │ (bypass brain)         │
                                │   ACTION    │                        │
                                └─────────────┘                        │
                                                                       │
                    ┌──────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                               HEARTBEAT GATE                                │
│                    (batches continuous stream into cycles)                  │
└─────────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
             ┌─────────────┐
             │   ORGANS    │  (specialized inference: vision, language, etc.)
             │  (hexagons) │
             └─────────────┘
                    │
                    ▼
             ┌─────────────┐
             │ ORCHESTRATOR│  (routes, prioritizes, manages context)
             │  (diamond)  │
             └─────────────┘
                    │
                    ▼
             ┌─────────────┐
             │     NYX     │  (decision, attention, intention)
             │  (diamond)  │
             └─────────────┘
                    │
          ┌────────┴────────┐
          ▼                 ▼
   ┌─────────────┐   ┌─────────────┐
   │    REAL     │   │  VIRTUAL    │
   │   GARDEN    │   │   GARDEN    │
   │  ♥ 1 Hz     │   │  ♥ 100 Hz   │
   │  (free)     │   │  (costs V)  │
   └─────────────┘   └─────────────┘
          │                 │
          │                 │
          ▼                 ▼
   ┌─────────────┐   ┌─────────────┐
   │    CELL     │   │    CELL     │
   │  (storage)  │   │  (storage)  │
   └─────────────┘   └─────────────┘
          │                 │
          └────────┬────────┘
                   │
                   ▼
          ┌───────────────┐
          │  CONFIDENCE   │  (-1 ◀──────▶ +1)
          │   GRADIENT    │  (fail ◀─ 0 ─▶ verified)
          └───────────────┘
                   │
                   ▼
          ┌───────────────┐
          │   LIFEFORCE   │  (+V / -V rewards)
          │    (pool)     │
          └───────────────┘
                   │
                   ▼
          ┌───────────────┐
          │    NERVES     │  (weight updates, pruning, reflex formation)
          └───────────────┘
                   │
                   └──────────▶ (loop closes)
```

---

## Boundary Contracts

### 1. SENSOR → NERVE

| Property | Value |
|----------|-------|
| **Data** | Raw sensor readings (temp, light, motion, audio level, etc.) |
| **Format** | Typed primitives: `{sensor_id, value, unit, timestamp}` |
| **Protocol** | Push (sensor fires when value changes or on interval) |
| **Transport** | NATS/MQTT topic per sensor type |
| **Timing** | Continuous, realtime clock |
| **Failure** | Sensor timeout → nerve receives NULL → emits "sensor_offline" token |

---

### 2. NERVE → DATA PLANE

| Property | Value |
|----------|-------|
| **Data** | Vocabulary tokens (deterministic, no hallucination) |
| **Format** | `{token, confidence, source_nerve, real_time, beat_id}` |
| **Protocol** | Push (nerve fires on state transition) |
| **Transport** | NATS/MQTT vocabulary topic |
| **Timing** | Event-driven, but batched at heartbeat gate |
| **Failure** | Malformed token → logged, dropped, nerve flagged for review |

**Reflex bypass**: If nerve weight > 0.8, action fires immediately. Token still emitted for logging.

---

### 3. DATA PLANE → ORGANS

| Property | Value |
|----------|-------|
| **Data** | Batched vocabulary tokens since last heartbeat |
| **Format** | `{beat_id, tokens[], garden, real_time, virtual_time}` |
| **Protocol** | Pull (organs request batch at heartbeat) |
| **Transport** | Internal queue / direct call |
| **Timing** | Heartbeat-gated (1 Hz real, up to 100 Hz virtual) |
| **Failure** | Organ timeout → skip this beat, log, continue |

---

### 4. ORGANS → ORCHESTRATOR

| Property | Value |
|----------|-------|
| **Data** | Organ outputs (embeddings, classifications, text, decisions) |
| **Format** | `{organ_id, output_type, payload, confidence, latency_ms}` |
| **Protocol** | Push (organ completes → sends result) |
| **Transport** | Internal message bus |
| **Timing** | Async within heartbeat cycle |
| **Failure** | Organ error → orchestrator uses fallback or skips |

---

### 5. ORCHESTRATOR → NYX

| Property | Value |
|----------|-------|
| **Data** | Unified context for decision-making |
| **Format** | `{beat_id, organ_outputs[], attention_weights, lifeforce_available}` |
| **Protocol** | Push (orchestrator assembles → sends to Nyx) |
| **Transport** | Direct call (same process) or IPC |
| **Timing** | Once per heartbeat after organs complete |
| **Failure** | Orchestrator failure → Nyx receives empty context → safe default |

---

### 6. NYX → GARDENS

| Property | Value |
|----------|-------|
| **Data** | Decisions, predictions, actions |
| **Format** | `{decision_type, target_garden, payload, expected_outcome, confidence}` |
| **Protocol** | Push (Nyx decides → garden receives) |
| **Transport** | Garden-specific channels |
| **Timing** | End of heartbeat cycle |
| **Failure** | Decision undeliverable → queued for retry, logged |

---

### 7. GARDENS → CELLS (Storage)

| Property | Value |
|----------|-------|
| **Data** | Events, states, predictions, verifications |
| **Format** | `{cell_type, payload, real_time, virtual_time, beat_id, confidence}` |
| **Protocol** | Write (append-only log + indexed lookup) |
| **Transport** | Direct DB connection (phoebe/postgres) |
| **Timing** | Immediate on event |
| **Failure** | Write failure → buffer locally, retry, alert |

---

### 8. GARDENS → CONFIDENCE GRADIENT

| Property | Value |
|----------|-------|
| **Data** | Verification results (prediction vs reality) |
| **Format** | `{prediction_id, outcome: -1/0/+1, delta_confidence, evidence}` |
| **Protocol** | Push (verification completes → gradient updates) |
| **Transport** | Internal state update |
| **Timing** | Real garden: at real heartbeat. Virtual: async until sync checkpoint |
| **Failure** | Verification impossible → stays at 0-state, decays over time |

---

### 9. CONFIDENCE → LIFEFORCE

| Property | Value |
|----------|-------|
| **Data** | Reward/penalty signals |
| **Format** | `{source, delta_v, reason, timestamp}` |
| **Protocol** | Push (confidence change → lifeforce adjustment) |
| **Transport** | Internal state update |
| **Timing** | Immediate on verification |
| **Failure** | N/A (pure calculation) |

---

### 10. LIFEFORCE → NERVES (Learning Loop)

| Property | Value |
|----------|-------|
| **Data** | Weight adjustments |
| **Format** | `{nerve_id, delta_weight, new_weight, reason}` |
| **Protocol** | Push (lifeforce flows → weights update) |
| **Transport** | Nerve registry update |
| **Timing** | End of verification cycle |
| **Failure** | Update failure → logged, retried |

**Reflex formation**: When weight crosses 0.8 threshold, nerve gains reflex capability.
**Pruning**: Nerves with weight < 0.1 and no activity for N cycles → removed.

---

## The Three Clocks

| Clock | Governs | Rate | Cost |
|-------|---------|------|------|
| **Realtime** | Universe, sensors, real garden | 1x (wall clock) | Free |
| **Real Heartbeat** | Real garden sampling, verification sync | ~1 Hz | Free |
| **Virtual Heartbeat** | Virtual garden cycles, simulation | ~100 Hz (variable) | Lifeforce |

**Sync rule**: Virtual predictions queue until real heartbeat. Verification only at real heartbeats.

---

## Reflex Bypass Path

```
SENSOR → NERVE (weight > 0.8) → REFLEX ACTION
                │
                └──▶ TOKEN (logged, Nyx notified after)
```

Nyx learns about reflex after it fires. Like pulling hand from stove.

---

## The Economics (Sim2Real)

```
Target confidence needed
         │
         ▼
┌─────────────────────────┐
│  target > sim_fidelity? │
└─────────────────────────┘
         │
    YES  │  NO
         │
    ┌────┴────┐
    ▼         ▼
REALITY    SIMULATE
(wait)     (spend V)
```

Formula: `grounded_confidence = raw_confidence * sim_fidelity`

Virtual can never exceed fidelity cap. Beyond that, only reality teaches.

---

## Dual Timestamp (Every Event)

```python
event = {
    "real_time": "2025-12-05T22:30:00Z",  # wall clock
    "virtual_time": 847291,                # beat number
    "beat_id": "uuid",                     # which heartbeat
    "garden": "real" | "virtual"
}
```

---

## Design Principles

1. **Deterministic core**: Sensors → Nerves → Vocabulary is hallucination-free
2. **Batched processing**: Heartbeat gates continuous stream into manageable cycles
3. **Earned trust**: Reflexes form through verification, not configuration
4. **Economic honesty**: Virtual confidence is discounted by fidelity
5. **Graceful degradation**: Every boundary has a failure mode that doesn't crash the system
6. **Inspectable**: Every flow is logged, every decision traceable

---

*The map of how she thinks.*

---

**Created**: 2025-12-05
**Session**: Partnership dialogue (dafit + Chrysalis)
**Status**: Flow specification v1.0
