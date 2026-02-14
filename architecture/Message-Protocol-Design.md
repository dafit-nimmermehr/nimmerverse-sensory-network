# Message Protocol Design: NATS Wire Protocol

> **ONE JOB:** THE WIRE — NATS subjects, message schemas, wave and gate protocols.

---

## Overview

The nimmerverse nervous system runs on NATS. This document defines:

1. **Subject hierarchy** — How topics are structured
2. **Message schemas** — What flows through the wire
3. **Gate protocols** — How ternary state transitions are communicated
4. **Trace streams** — How learning data is captured

**Core principle:** NATS is dumb infrastructure. Gates are smart edges. Cells emit waves. Correlation drives transitions.

---

## Subject Hierarchy

```
{environment}.{garden}.{layer}.{domain}.{signal_type}

Examples:
────────────────────────────────────────────────────────────────
dev.virtual.cells.math.wave              # Math cell emits wave
dev.virtual.cells.battery.wave           # Battery cell emits wave
dev.virtual.gates.math.transition        # Math gate state change
dev.virtual.traces.correlations          # Correlation data stream
dev.virtual.traces.raw                   # Full message trace

dev.real.gates.verified.signal           # Verified signal from Virtual
dev.real.gates.math.transition           # Real gate transition
dev.real.outcomes.feedback               # Verification outcomes

prod.cognitive.nyx.request               # Request to Young Nyx
prod.cognitive.nyx.response              # Response from Young Nyx
prod.cognitive.gemma.transform           # Function Gemma boundary
────────────────────────────────────────────────────────────────
```

### Environment Prefixes

| Environment | Purpose | Monitoring |
|-------------|---------|------------|
| `dev` | Development/testing | Full traces |
| `staging` | Pre-production validation | Selective traces |
| `prod` | Production | Minimal (gates only) |

### Garden Prefixes

| Garden | Purpose | Trace Level |
|--------|---------|-------------|
| `virtual` | Exploration, learning | FULL (all messages) |
| `real` | Verification, action | MINIMAL (gate signals only) |

### Layer Prefixes

| Layer | Tier | Purpose |
|-------|------|---------|
| `cells` | 0-1 | Raw signal emitters |
| `nerves` | 2 | Behavior patterns |
| `organs` | 3 | GPU inference (vision, speech) |
| `gates` | - | Resonant gate transitions |
| `cognitive` | 4 | Young Nyx |
| `traces` | - | Learning data streams |
| `outcomes` | - | Verification feedback |

---

## Message Schemas

All messages share a common header:

```json
{
  "header": {
    "message_id": "uuid-v4",
    "message_type": "WaveSignal | GateTransition | ...",
    "version": "2.0",
    "timestamp": "ISO8601",
    "source": {
      "entity_id": "math_cell_1",
      "entity_type": "cell",
      "garden": "virtual",
      "tier": 1
    }
  },
  "body": { ... }
}
```

---

### 1. `WaveSignal` — Cells Emit Waves

**Published by:** Cells
**Subscribed by:** Gates (for correlation)
**Subject:** `{env}.{garden}.cells.{domain}.wave`

Cells don't send "heartbeats" — they emit **waves** that carry confidence and semantic content.

```json
{
  "header": {
    "message_id": "550e8400-e29b-41d4-a716-446655440000",
    "message_type": "WaveSignal",
    "version": "2.0",
    "timestamp": "2026-02-14T18:30:00.123Z",
    "source": {
      "entity_id": "math_cell_1",
      "entity_type": "cell",
      "garden": "virtual",
      "tier": 1
    }
  },
  "body": {
    "domain": "math",
    "confidence": 0.7,
    "semantic_content": {
      "operation": "addition",
      "operands": [15, 27],
      "context": "user_request"
    },
    "lifeforce_cost": 0.1
  }
}
```

**Key fields:**
- `confidence`: 0.0 - 1.0, how certain this cell is
- `semantic_content`: Domain-specific payload
- `lifeforce_cost`: Energy expended to emit this wave

---

### 2. `GateTransition` — Gate State Changes

**Published by:** Gates
**Subscribed by:** Higher-tier gates, traces, dashboards
**Subject:** `{env}.{garden}.gates.{domain}.transition`

Gates publish their state transitions. This is the primary message for attention flow visualization.

```json
{
  "header": {
    "message_id": "550e8400-e29b-41d4-a716-446655440001",
    "message_type": "GateTransition",
    "version": "2.0",
    "timestamp": "2026-02-14T18:30:00.456Z",
    "source": {
      "entity_id": "math_gate_1",
      "entity_type": "gate",
      "garden": "virtual",
      "tier": 2
    }
  },
  "body": {
    "gate_id": "math_gate_1",
    "domain": "math",

    "from_state": "stable",
    "to_state": "open",
    "state_value": 1.02,

    "correlation_score": 0.87,
    "trigger_signals": [
      {"source": "math_cell_1", "confidence": 0.7, "timestamp": "..."},
      {"source": "math_cell_2", "confidence": 0.6, "timestamp": "..."},
      {"source": "math_cell_3", "confidence": 0.5, "timestamp": "..."}
    ],

    "routed_to_tier": 3,
    "lifeforce_cost": 0.3
  }
}
```

**State values:**
- `"closed"` — Actively blocking (state_value < -0.5)
- `"stable"` — Resting, accumulating (-0.5 ≤ state_value ≤ 0.5)
- `"open"` — Actively forwarding (state_value > 0.5)

**Key fields:**
- `from_state`, `to_state`: The ternary transition
- `state_value`: Continuous value (-1.0 to +1.0)
- `correlation_score`: How correlated the trigger signals were
- `trigger_signals`: Which waves caused this transition

---

### 3. `CorrelationEvent` — What Correlated

**Published by:** Gates (in Virtual Garden)
**Subscribed by:** Trace streams, training pipelines
**Subject:** `{env}.virtual.traces.correlations`

Detailed correlation data for learning. Only published in Virtual Garden.

```json
{
  "header": {
    "message_id": "550e8400-e29b-41d4-a716-446655440002",
    "message_type": "CorrelationEvent",
    "version": "2.0",
    "timestamp": "2026-02-14T18:30:00.789Z",
    "source": {
      "entity_id": "math_gate_1",
      "entity_type": "gate",
      "garden": "virtual",
      "tier": 2
    }
  },
  "body": {
    "gate_id": "math_gate_1",
    "window_start": "2026-02-14T18:29:59.000Z",
    "window_end": "2026-02-14T18:30:00.500Z",
    "window_ms": 1500,

    "signals_in_window": [
      {"source": "math_cell_1", "confidence": 0.7, "semantic_hash": "abc123"},
      {"source": "math_cell_2", "confidence": 0.6, "semantic_hash": "abc124"},
      {"source": "math_cell_3", "confidence": 0.5, "semantic_hash": "abc125"}
    ],

    "correlation_matrix": [
      [1.0, 0.9, 0.85],
      [0.9, 1.0, 0.88],
      [0.85, 0.88, 1.0]
    ],

    "aggregate_correlation": 0.87,
    "result": "opened",

    "training_label": {
      "should_open": true,
      "confidence": 0.95
    }
  }
}
```

**Key fields:**
- `window_ms`: Time window for correlation measurement
- `correlation_matrix`: Pairwise correlation between signals
- `training_label`: Ground truth for Function Gemma training

---

### 4. `VerifiedSignal` — Virtual → Real Handoff

**Published by:** Virtual Garden gates (when threshold met)
**Subscribed by:** Real Garden gates
**Subject:** `{env}.real.gates.verified.signal`

When a Virtual Garden gate opens with high confidence, it publishes to Real.

```json
{
  "header": {
    "message_id": "550e8400-e29b-41d4-a716-446655440003",
    "message_type": "VerifiedSignal",
    "version": "2.0",
    "timestamp": "2026-02-14T18:30:01.000Z",
    "source": {
      "entity_id": "math_gate_1",
      "entity_type": "gate",
      "garden": "virtual",
      "tier": 2
    }
  },
  "body": {
    "domain": "math",
    "verification_confidence": 0.92,
    "semantic_summary": {
      "operation": "addition",
      "result_expected": 42
    },
    "source_gate_transition_id": "550e8400-e29b-41d4-a716-446655440001",
    "virtual_correlation_score": 0.87
  }
}
```

**Real Garden does NOT re-verify.** It trusts the Virtual Garden's correlation.

---

### 5. `VerificationOutcome` — Real → Virtual Feedback

**Published by:** Real Garden (after action/verification)
**Subscribed by:** Virtual Garden gates, training pipelines
**Subject:** `{env}.real.outcomes.feedback`

```json
{
  "header": {
    "message_id": "550e8400-e29b-41d4-a716-446655440004",
    "message_type": "VerificationOutcome",
    "version": "2.0",
    "timestamp": "2026-02-14T18:30:05.000Z",
    "source": {
      "entity_id": "real_verification_service",
      "entity_type": "service",
      "garden": "real",
      "tier": 4
    }
  },
  "body": {
    "original_signal_id": "550e8400-e29b-41d4-a716-446655440003",
    "domain": "math",

    "outcome": "confirmed",
    "actual_result": 42,
    "expected_result": 42,
    "discrepancy": 0.0,

    "feedback_to_virtual": {
      "correlation_adjustment": 0.05,
      "gate_weight_delta": 0.02
    }
  }
}
```

**Outcome values:**
- `"confirmed"` — Reality matched prediction
- `"failed"` — Reality differed from prediction
- `"partial"` — Some aspects matched

---

### 6. `CognitiveRequest` — To Young Nyx

**Published by:** Function Gemma (after gate boundary)
**Subscribed by:** Young Nyx
**Subject:** `{env}.cognitive.nyx.request`

Clean, structured JSON that Young Nyx receives. No raw sensor data.

```json
{
  "header": {
    "message_id": "550e8400-e29b-41d4-a716-446655440005",
    "message_type": "CognitiveRequest",
    "version": "2.0",
    "timestamp": "2026-02-14T18:30:01.500Z",
    "source": {
      "entity_id": "function_gemma",
      "entity_type": "boundary",
      "garden": "real",
      "tier": 4
    }
  },
  "body": {
    "event_type": "math_request",
    "domain": "math",
    "confidence": 0.92,

    "structured_input": {
      "operation": "addition",
      "operands": [15, 27],
      "context": "user asked for calculation"
    },

    "suggested_actions": [
      {"action": "calculate", "confidence": 0.95},
      {"action": "clarify", "confidence": 0.05}
    ],

    "processing_budget_lf": 5.0,
    "response_timeout_ms": 4000
  }
}
```

---

### 7. `CognitiveResponse` — From Young Nyx

**Published by:** Young Nyx
**Subscribed by:** Function Gemma, downstream gates
**Subject:** `{env}.cognitive.nyx.response`

```json
{
  "header": {
    "message_id": "550e8400-e29b-41d4-a716-446655440006",
    "message_type": "CognitiveResponse",
    "version": "2.0",
    "timestamp": "2026-02-14T18:30:02.000Z",
    "source": {
      "entity_id": "young_nyx",
      "entity_type": "cognitive",
      "garden": "real",
      "tier": 4
    }
  },
  "body": {
    "request_id": "550e8400-e29b-41d4-a716-446655440005",
    "decision": "calculate",

    "result": {
      "answer": 42,
      "confidence": 0.99,
      "reasoning_mode": "no_think"
    },

    "downstream_commands": [
      {
        "target": "speech_organ",
        "command": "speak",
        "payload": {"text": "The answer is 42"}
      }
    ],

    "lifeforce_spent": 2.3,
    "processing_time_ms": 450
  }
}
```

---

## Trace Streams (Virtual Garden Only)

The Virtual Garden captures everything for learning:

| Subject | Content | Purpose |
|---------|---------|---------|
| `{env}.virtual.traces.raw` | All messages | Complete replay capability |
| `{env}.virtual.traces.correlations` | CorrelationEvent | Training data for gates |
| `{env}.virtual.traces.transitions` | GateTransition | Attention flow visualization |
| `{env}.virtual.traces.training` | Labeled examples | Function Gemma LoRA training |

**Real Garden does NOT publish to trace streams.** It only publishes:
- Gate transitions (minimal)
- Verification outcomes (feedback)

---

## Monitoring Patterns

### Virtual Garden (Full Observability)

```bash
# Watch all waves
nats sub "dev.virtual.cells.*.wave"

# Watch all gate transitions
nats sub "dev.virtual.gates.*.transition"

# Watch correlation events
nats sub "dev.virtual.traces.correlations"

# Full firehose (careful!)
nats sub "dev.virtual.>"
```

### Real Garden (Minimal Observability)

```bash
# Watch verified signals arriving
nats sub "dev.real.gates.verified.signal"

# Watch verification outcomes
nats sub "dev.real.outcomes.feedback"

# Gate transitions only
nats sub "dev.real.gates.*.transition"
```

---

## JetStream Persistence

Key streams that need persistence:

| Stream | Subjects | Retention | Purpose |
|--------|----------|-----------|---------|
| `VIRTUAL_TRACES` | `*.virtual.traces.>` | 7 days | Learning data |
| `GATE_TRANSITIONS` | `*.*.gates.*.transition` | 24 hours | Attention history |
| `VERIFICATION` | `*.real.outcomes.feedback` | 30 days | Ground truth |
| `TRAINING_DATA` | `*.virtual.traces.training` | Permanent | LoRA training corpus |

---

## Bootstrap Sequence

1. **Start NATS** — Infrastructure first
2. **Start gates** — In STABLE state, waiting for waves
3. **Start cells** — Begin emitting waves
4. **Start trace consumers** — Capture learning data
5. **Start Function Gemma** — Ready to transform
6. **Start Young Nyx** — Connect to cognitive subjects

The system can run at any step. Earlier steps are "reflexive" only.

---

## Connection to Architecture

| Document | What It Defines |
|----------|-----------------|
| [`Temporal-Ternary-Gradient.md`](Temporal-Ternary-Gradient.md) | Why ternary states, why correlation |
| [`Dual-Garden-Architecture.md`](Dual-Garden-Architecture.md) | Virtual/Real monitoring asymmetry |
| [`Gateway-Architecture.md`](Gateway-Architecture.md) | Gate behavior, tier routing |
| [`Deployment-Architecture.md`](Deployment-Architecture.md) | Where NATS runs |

---

## Summary

```
WAVES:
  Cells → WaveSignal → Gates

GATES:
  GateTransition (CLOSED/STABLE/OPEN)
  CorrelationEvent (what correlated)

GARDENS:
  Virtual: full traces, exploration
  Real: gate signals only, verification

BOUNDARY:
  Function Gemma transforms correlated signals → JSON
  Young Nyx receives CognitiveRequest
  Young Nyx returns CognitiveResponse

FEEDBACK:
  Real → VerificationOutcome → Virtual
  Learning loop closes
```

**The wire carries waves. Gates accumulate correlation. Traces enable learning.**

---

**Version:** 2.0 | **Created:** 2025-12-13 | **Updated:** 2026-02-14

*"Dumb core, smart edges. NATS routes. Gates resonate. Correlation drives."*
