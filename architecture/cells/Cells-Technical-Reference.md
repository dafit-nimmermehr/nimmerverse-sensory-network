# Cells Technical Reference

> *Implementation details: Python classes, SQL tables, code patterns.*

**Conceptual overview:** → [`../Cellular-Architecture.md`](../Cellular-Architecture.md)
**Index:** → [`Cells-Index.md`](Cells-Index.md)

---

## Python Class Patterns

### Base Cell Pattern

All cells follow this state machine pattern:

```python
class Cell(StateMachine):
    """Base pattern for all cells."""

    # Define discrete states
    states = [IDLE, ACTIVE, ERROR]

    # Outputs available to higher layers
    outputs = {
        "state": str,
        "last_updated": timestamp,
    }

    # Lifeforce costs per transition
    costs = {
        (FROM_STATE, TO_STATE): float,
    }
```

---

### Sensor Cell Example

```python
class DistanceSensorCell(StateMachine):
    """
    Wraps IR/ultrasonic distance sensor.
    Exposes raw hardware as state machine.
    """
    states = [IDLE, POLLING, READING, REPORTING, ERROR]

    # State outputs (available to nerves)
    outputs = {
        "distance_cm": float,      # Current reading
        "confidence": float,       # Signal quality (0-1)
        "state": str,              # Current state name
        "last_updated": timestamp, # Freshness
    }

    # Lifeforce costs
    costs = {
        (IDLE, POLLING): 0.1,      # Wake up sensor
        (POLLING, READING): 0.3,   # Perform measurement
        (READING, REPORTING): 0.1, # Process result
        (REPORTING, IDLE): 0.0,    # Return to rest
        (ANY, ERROR): 0.0,         # Error transition free
    }
```

---

### Motor Cell Example

```python
class MotorCell(StateMachine):
    """
    Wraps DC motor with feedback.
    Exposes actuation as state machine.
    """
    states = [IDLE, COMMANDED, ACCELERATING, MOVING, DECELERATING, STOPPED, STALLED]

    outputs = {
        "actual_velocity": float,  # Measured speed
        "target_velocity": float,  # Commanded speed
        "power_draw": float,       # Current consumption
        "state": str,              # Current state
        "stall_detected": bool,    # Motor blocked?
    }

    costs = {
        (IDLE, COMMANDED): 0.1,
        (COMMANDED, ACCELERATING): 0.5,
        (ACCELERATING, MOVING): 1.0,  # High power during accel
        (MOVING, MOVING): 0.3,        # Sustain cost per tick
        (MOVING, DECELERATING): 0.2,
        (DECELERATING, STOPPED): 0.1,
        (ANY, STALLED): 0.0,          # Stall is failure, not cost
    }

    # Feedback triggers state changes
    def on_current_spike(self):
        """Motor drawing too much current = stall"""
        self.transition_to(STALLED)
        self.emit_event("stall_detected", obstacle_likely=True)
```

---

### Organ Cell Example

```python
class SpeechSTTCell(StateMachine):
    """
    Wraps Whisper speech-to-text.
    Expensive organ, lifeforce-gated.
    """
    states = [IDLE, LISTENING, BUFFERING, TRANSCRIBING, REPORTING, ERROR]

    outputs = {
        "transcript": str,
        "language": str,
        "confidence": float,
        "state": str,
    }

    costs = {
        (IDLE, LISTENING): 0.5,
        (LISTENING, BUFFERING): 0.5,
        (BUFFERING, TRANSCRIBING): 5.0,  # GPU inference!
        (TRANSCRIBING, REPORTING): 0.1,
        (REPORTING, IDLE): 0.0,
    }
```

---

## SQL Table Definitions

### cells Table

```sql
CREATE TABLE cells (
    id BIGSERIAL PRIMARY KEY,
    cell_type VARCHAR(50),           -- 'sensor', 'motor', 'organ'
    cell_name VARCHAR(100) UNIQUE,   -- 'distance_sensor_front'
    hardware_binding JSONB,          -- {"type": "i2c", "address": "0x40"}

    -- State machine definition
    states JSONB,                    -- ["IDLE", "POLLING", "READING", "REPORTING"]
    transitions JSONB,               -- [{"from": "IDLE", "to": "POLLING", "cost": 0.1}]
    current_state VARCHAR(50),

    -- Outputs (live values)
    outputs JSONB,                   -- {"distance_cm": 25.5, "confidence": 0.9}

    -- Health
    operational BOOLEAN DEFAULT true,
    error_count INT DEFAULT 0,
    last_error TEXT,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

### decision_trails Table (Training Data)

```sql
CREATE TABLE decision_trails (
    id BIGSERIAL PRIMARY KEY,
    organism_id BIGINT REFERENCES organisms(id),
    nerve_id BIGINT REFERENCES nerves(id),

    -- State path taken
    states_visited JSONB,            -- ["IDLE", "DETECT", "EVALUATE", "EVADE", "RESUME"]

    -- Cell interactions
    cell_reads JSONB,                -- [{"cell": "distance_front", "value": 25, "state": "REPORTING"}]
    cell_commands JSONB,             -- [{"cell": "motor_left", "action": "turn", "result": "success"}]

    -- Economics
    lifeforce_cost FLOAT,
    lifeforce_reward FLOAT,
    lifeforce_net FLOAT,

    -- Outcome
    outcome VARCHAR(20),             -- 'success', 'failure', 'timeout'

    -- Timing
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    latency_ms INT
);
```

---

## Common Queries

### Cell Health Dashboard

```sql
SELECT cell_name, cell_type, current_state, operational,
       outputs->>'distance_cm' as distance,
       outputs->>'confidence' as confidence
FROM cells
WHERE cell_type = 'sensor';
```

### Training Data for GRPO

```sql
-- Each row is a training example with automatic credit assignment
SELECT
    states_visited,      -- The path taken (which decisions led here?)
    cell_reads,          -- Which cells contributed (sensor inputs)
    cell_commands,       -- What actions were taken (motor outputs)
    outcome,             -- Success/failure (ground truth)
    lifeforce_cost,      -- Cost of this path
    lifeforce_reward     -- Reward earned
FROM decision_trails
WHERE nerve_id = ?;
```

### State Path Analysis

```sql
SELECT states_visited, COUNT(*) as occurrences,
       AVG(lifeforce_cost) as avg_cost,
       SUM(CASE WHEN outcome = 'success' THEN 1 ELSE 0 END)::float / COUNT(*) as success_rate
FROM decision_trails
WHERE nerve_id = (SELECT id FROM nerves WHERE nerve_name = 'collision_avoidance')
GROUP BY states_visited
ORDER BY occurrences DESC;
```

---

## Lifeforce Cost Reference

### Sensor Cells

| Cell Type | Operation | Cost (LF) |
|-----------|-----------|-----------|
| Distance sensor | poll | 0.3-0.5 |
| Battery monitor | read | 0.1 |
| IMU sensor | sample | 0.3 |
| Light sensor | read | 0.2 |

### Motor Cells

| Cell Type | Operation | Cost (LF) |
|-----------|-----------|-----------|
| DC motor | move (per 100ms) | 1.0-2.0 |
| Servo | position | 0.5 |

### Organ Cells

| Cell Type | Operation | Cost (LF) |
|-----------|-----------|-----------|
| Speech STT | transcribe | 5.0 |
| Speech TTS | synthesize | 4.0 |
| Vision detect | detect frame | 8.0 |

---

## Tiered Reward Reference

| Tier | Level | Reward | Lifeforce Cost |
|------|-------|--------|----------------|
| 1 | Cell | +0.1 | -0.3 LF |
| 2 | Nerve | +1.0 | -2.0 LF |
| 3 | Organism | +5.0 | -8.0 LF |
| Bonus | Human verification | +2.0 | 0 LF |

---

## Ternary State Pattern

```python
state = {
    "value": 0,           # -1 (failed), 0 (uncertain), +1 (success)
    "confidence": 0.6,    # 0.0 - 1.0 confidence gradient
    "trend": +0.1,        # direction of change
    "domain": "virtual"   # "virtual" or "real" garden
}
```

---

**Created**: 2025-12-10
**Extracted from**: Cellular-Architecture.md v4.2
**Status**: Technical reference
