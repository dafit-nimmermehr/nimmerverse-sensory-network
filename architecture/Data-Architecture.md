# 🗄️ Data Architecture v4

> *"Three layers of state machines. One database to remember them all."*
> — The Unified Schema (2025-12-07)

---

## Overview

**Version 4** aligns the data architecture with the layered state machine model:

| Layer | Entity | Database Table | Purpose |
|-------|--------|----------------|---------|
| **1** | Cells | `cells` | Atomic state machines (sensors, motors, organs) |
| **2** | Nerves | `nerves` | Behavioral state machines (compose cells) |
| **3** | Organisms | `organisms` | Emergent patterns (nerve configurations) |
| **∞** | History | `decision_trails` | Training data for reflex compilation |

```
┌─────────────────────────────────────────────────────────────┐
│                       PHOEBE                                 │
│              (PostgreSQL 17.6 on bare metal)                 │
├─────────────────────────────────────────────────────────────┤
│  cells         │ Atomic state machines (hardware wrappers)   │
│  nerves        │ Behavioral patterns (cell orchestration)    │
│  organisms     │ Emergent identities (nerve configurations)  │
│  decision_trails │ Training data (reflex compilation)        │
│  objects       │ Discovered environment features             │
│  variance_probe_runs │ Topology mapping data                 │
│  *_messages    │ Partnership communication channels          │
└─────────────────────────────────────────────────────────────┘
```

---

## Core Tables

### Layer 1: Cells

```sql
CREATE TABLE cells (
    id BIGSERIAL PRIMARY KEY,
    cell_name VARCHAR(100) UNIQUE NOT NULL,
    cell_type VARCHAR(50) NOT NULL,  -- 'sensor', 'motor', 'organ'

    -- Hardware binding
    hardware_binding JSONB NOT NULL,
    -- Examples:
    -- {"type": "i2c", "address": "0x40", "bus": 1}
    -- {"type": "gpio", "pin": 17, "mode": "input"}
    -- {"type": "network", "host": "atlas.eachpath.local", "port": 8080}

    -- State machine definition
    states JSONB NOT NULL,
    -- Example: ["IDLE", "POLLING", "READING", "REPORTING", "ERROR"]

    transitions JSONB NOT NULL,
    -- Example: [
    --   {"from": "IDLE", "to": "POLLING", "trigger": "poll_requested", "cost": 0.1},
    --   {"from": "POLLING", "to": "READING", "trigger": "sensor_ready", "cost": 0.3},
    --   {"from": "READING", "to": "REPORTING", "trigger": "data_valid", "cost": 0.1},
    --   {"from": "REPORTING", "to": "IDLE", "trigger": "delivered", "cost": 0.0}
    -- ]

    current_state VARCHAR(50) DEFAULT 'IDLE',

    -- Live outputs (updated by cell runtime)
    outputs JSONB DEFAULT '{}',
    -- Example: {"distance_cm": 25.5, "confidence": 0.92, "timestamp": "..."}

    -- Health tracking
    operational BOOLEAN DEFAULT true,
    error_count INT DEFAULT 0,
    last_error TEXT,
    last_error_at TIMESTAMPTZ,

    -- Statistics
    total_transitions INT DEFAULT 0,
    total_lifeforce_spent FLOAT DEFAULT 0.0,

    -- Timestamps
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index for fast cell lookups
CREATE INDEX idx_cells_type ON cells(cell_type);
CREATE INDEX idx_cells_operational ON cells(operational);

-- Example cells
INSERT INTO cells (cell_name, cell_type, hardware_binding, states, transitions) VALUES
('distance_sensor_front', 'sensor',
 '{"type": "i2c", "address": "0x40", "bus": 1}',
 '["IDLE", "POLLING", "READING", "REPORTING", "ERROR"]',
 '[{"from": "IDLE", "to": "POLLING", "cost": 0.1},
   {"from": "POLLING", "to": "READING", "cost": 0.3},
   {"from": "READING", "to": "REPORTING", "cost": 0.1},
   {"from": "REPORTING", "to": "IDLE", "cost": 0.0}]'),

('motor_left', 'motor',
 '{"type": "pwm", "pin": 18, "enable_pin": 17}',
 '["IDLE", "COMMANDED", "ACCELERATING", "MOVING", "DECELERATING", "STOPPED", "STALLED"]',
 '[{"from": "IDLE", "to": "COMMANDED", "cost": 0.1},
   {"from": "COMMANDED", "to": "ACCELERATING", "cost": 0.5},
   {"from": "ACCELERATING", "to": "MOVING", "cost": 1.0},
   {"from": "MOVING", "to": "DECELERATING", "cost": 0.2},
   {"from": "DECELERATING", "to": "STOPPED", "cost": 0.1}]'),

('speech_stt', 'organ',
 '{"type": "network", "host": "atlas.eachpath.local", "port": 8080, "model": "whisper-large-v3"}',
 '["IDLE", "LISTENING", "BUFFERING", "TRANSCRIBING", "REPORTING", "ERROR"]',
 '[{"from": "IDLE", "to": "LISTENING", "cost": 0.5},
   {"from": "LISTENING", "to": "BUFFERING", "cost": 0.5},
   {"from": "BUFFERING", "to": "TRANSCRIBING", "cost": 5.0},
   {"from": "TRANSCRIBING", "to": "REPORTING", "cost": 0.1},
   {"from": "REPORTING", "to": "IDLE", "cost": 0.0}]');
```

### Layer 2: Nerves

```sql
CREATE TABLE nerves (
    id BIGSERIAL PRIMARY KEY,
    nerve_name VARCHAR(100) UNIQUE NOT NULL,

    -- Cell dependencies
    required_cells JSONB NOT NULL,  -- ["distance_sensor_front", "motor_left", "motor_right"]
    optional_cells JSONB DEFAULT '[]',  -- ["speech_tts"]

    -- State machine definition (behavioral states)
    states JSONB NOT NULL,
    -- Example: ["IDLE", "DETECT", "EVALUATE", "EVADE", "RESUME"]

    transitions JSONB NOT NULL,
    -- Example: [
    --   {"from": "IDLE", "to": "DETECT", "trigger": "distance < 30", "cost": 0.5},
    --   {"from": "DETECT", "to": "EVALUATE", "trigger": "sensors_polled", "cost": 0.5},
    --   {"from": "EVALUATE", "to": "EVADE", "trigger": "risk > 0.7", "cost": 0.5},
    --   {"from": "EVADE", "to": "RESUME", "trigger": "path_clear", "cost": 1.0},
    --   {"from": "RESUME", "to": "IDLE", "trigger": "movement_complete", "cost": 0.0}
    -- ]

    current_state VARCHAR(50) DEFAULT 'IDLE',

    -- Priority (for nerve preemption)
    priority INT DEFAULT 5,  -- 1-10, higher = more important

    -- Evolution tracking
    mode VARCHAR(20) DEFAULT 'deliberate',  -- 'deliberate', 'hybrid', 'reflex'
    total_executions INT DEFAULT 0,
    successful_executions INT DEFAULT 0,
    failed_executions INT DEFAULT 0,

    -- Reflex compilation
    compiled_at TIMESTAMPTZ,  -- When evolved to reflex
    compiled_logic JSONB,     -- Compiled state machine (no LLM)

    -- Cost tracking
    avg_cost_deliberate FLOAT,
    avg_cost_hybrid FLOAT,
    avg_cost_reflex FLOAT,
    cost_reduction_percent FLOAT,  -- Savings from evolution

    -- Latency tracking
    avg_latency_deliberate_ms INT,
    avg_latency_hybrid_ms INT,
    avg_latency_reflex_ms INT,
    latency_reduction_percent FLOAT,

    -- Timestamps
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_nerves_mode ON nerves(mode);
CREATE INDEX idx_nerves_priority ON nerves(priority DESC);

-- Example nerves
INSERT INTO nerves (nerve_name, required_cells, optional_cells, states, transitions, priority) VALUES
('collision_avoidance',
 '["distance_sensor_front", "distance_sensor_left", "distance_sensor_right", "motor_left", "motor_right"]',
 '["speech_tts"]',
 '["IDLE", "DETECT", "EVALUATE", "EVADE", "RESUME"]',
 '[{"from": "IDLE", "to": "DETECT", "trigger": "distance_front < 30", "cost": 0.5},
   {"from": "DETECT", "to": "EVALUATE", "trigger": "all_sensors_read", "cost": 0.5},
   {"from": "EVALUATE", "to": "EVADE", "trigger": "risk > 0.7", "cost": 0.5},
   {"from": "EVADE", "to": "RESUME", "trigger": "path_clear", "cost": 1.0},
   {"from": "RESUME", "to": "IDLE", "trigger": "complete", "cost": 0.0}]',
 10),

('exploration_pattern',
 '["distance_sensor_front", "distance_sensor_left", "distance_sensor_right", "motor_left", "motor_right", "imu_sensor"]',
 '["vision_detect"]',
 '["IDLE", "CHOOSE_DIRECTION", "MOVE", "CHECK_OBSTACLE", "RECORD", "REPEAT"]',
 '[{"from": "IDLE", "to": "CHOOSE_DIRECTION", "trigger": "start_exploration", "cost": 1.0},
   {"from": "CHOOSE_DIRECTION", "to": "MOVE", "trigger": "direction_chosen", "cost": 0.5},
   {"from": "MOVE", "to": "CHECK_OBSTACLE", "trigger": "moved_100ms", "cost": 0.3},
   {"from": "CHECK_OBSTACLE", "to": "RECORD", "trigger": "area_new", "cost": 0.5},
   {"from": "RECORD", "to": "REPEAT", "trigger": "recorded", "cost": 0.1},
   {"from": "REPEAT", "to": "CHOOSE_DIRECTION", "trigger": "continue", "cost": 0.0}]',
 5),

('charging_seeking',
 '["battery_monitor", "distance_sensor_front", "motor_left", "motor_right"]',
 '["vision_detect"]',
 '["MONITOR", "THRESHOLD", "SEARCH", "APPROACH", "DOCK", "CHARGE", "RESUME"]',
 '[{"from": "MONITOR", "to": "THRESHOLD", "trigger": "battery < 20%", "cost": 0.1},
   {"from": "THRESHOLD", "to": "SEARCH", "trigger": "charging_needed", "cost": 0.5},
   {"from": "SEARCH", "to": "APPROACH", "trigger": "station_found", "cost": 1.0},
   {"from": "APPROACH", "to": "DOCK", "trigger": "station_close", "cost": 0.5},
   {"from": "DOCK", "to": "CHARGE", "trigger": "docked", "cost": 0.1},
   {"from": "CHARGE", "to": "RESUME", "trigger": "battery > 80%", "cost": 0.0}]',
 8);
```

### Layer 3: Organisms

```sql
CREATE TABLE organisms (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,

    -- Nerve configuration
    active_nerves JSONB NOT NULL,
    -- Example: {
    --   "collision_avoidance": {"priority": 10, "mode": "reflex"},
    --   "exploration_pattern": {"priority": 5, "mode": "deliberate"},
    --   "battery_monitoring": {"priority": 8, "mode": "reflex"}
    -- }

    -- Cell assignments (which hardware this organism controls)
    cell_bindings JSONB NOT NULL,
    -- Example: {
    --   "distance_sensor_front": {"cell_id": 1, "exclusive": false},
    --   "motor_left": {"cell_id": 4, "exclusive": true}
    -- }

    -- Lifeforce (survival currency)
    lifeforce_current FLOAT DEFAULT 100.0,
    lifeforce_earned_total FLOAT DEFAULT 0.0,
    lifeforce_spent_total FLOAT DEFAULT 0.0,
    lifeforce_net FLOAT GENERATED ALWAYS AS (lifeforce_earned_total - lifeforce_spent_total) STORED,

    -- Identity (accumulated through experience)
    total_decisions INT DEFAULT 0,
    successful_decisions INT DEFAULT 0,
    failed_decisions INT DEFAULT 0,
    success_rate FLOAT GENERATED ALWAYS AS (
        CASE WHEN total_decisions > 0
        THEN successful_decisions::float / total_decisions
        ELSE 0.0 END
    ) STORED,

    -- Reflexes (compiled behaviors)
    reflexes_compiled INT DEFAULT 0,

    -- Lifecycle
    born_at TIMESTAMPTZ DEFAULT NOW(),
    last_active TIMESTAMPTZ DEFAULT NOW(),
    died_at TIMESTAMPTZ,  -- NULL = still alive
    death_cause TEXT      -- 'lifeforce_depleted', 'hardware_failure', 'retired'
);

-- Indexes
CREATE INDEX idx_organisms_alive ON organisms(died_at) WHERE died_at IS NULL;
CREATE INDEX idx_organisms_lifeforce ON organisms(lifeforce_current DESC);

-- Example organism
INSERT INTO organisms (name, active_nerves, cell_bindings) VALUES
('Explorer-Alpha',
 '{"collision_avoidance": {"priority": 10, "mode": "deliberate"},
   "exploration_pattern": {"priority": 5, "mode": "deliberate"},
   "charging_seeking": {"priority": 8, "mode": "deliberate"}}',
 '{"distance_sensor_front": {"cell_id": 1},
   "distance_sensor_left": {"cell_id": 2},
   "distance_sensor_right": {"cell_id": 3},
   "motor_left": {"cell_id": 4},
   "motor_right": {"cell_id": 5},
   "battery_monitor": {"cell_id": 6}}');
```

### Decision Trails (Training Data)

```sql
CREATE TABLE decision_trails (
    id BIGSERIAL PRIMARY KEY,
    organism_id BIGINT REFERENCES organisms(id),
    nerve_id BIGINT REFERENCES nerves(id),

    -- Mode at time of execution
    mode VARCHAR(20) NOT NULL,  -- 'deliberate', 'hybrid', 'reflex'

    -- State path taken
    states_visited JSONB NOT NULL,
    -- Example: ["IDLE", "DETECT", "EVALUATE", "EVADE", "RESUME"]

    -- Cell interactions during this execution
    cell_reads JSONB NOT NULL,
    -- Example: [
    --   {"cell": "distance_sensor_front", "state": "REPORTING", "outputs": {"distance_cm": 25}},
    --   {"cell": "distance_sensor_left", "state": "REPORTING", "outputs": {"distance_cm": 45}}
    -- ]

    cell_commands JSONB NOT NULL,
    -- Example: [
    --   {"cell": "motor_left", "action": "turn", "params": {"direction": "reverse", "duration_ms": 200}},
    --   {"cell": "motor_right", "action": "turn", "params": {"direction": "forward", "duration_ms": 200}}
    -- ]

    cell_feedback JSONB DEFAULT '[]',
    -- Example: [
    --   {"cell": "motor_left", "event": "stall_detected", "timestamp": "..."}
    -- ]

    -- Economics
    lifeforce_cost FLOAT NOT NULL,
    lifeforce_reward FLOAT DEFAULT 0.0,
    lifeforce_net FLOAT GENERATED ALWAYS AS (lifeforce_reward - lifeforce_cost) STORED,

    -- Outcome
    outcome VARCHAR(20) NOT NULL,  -- 'success', 'failure', 'timeout', 'interrupted'
    outcome_details JSONB,         -- {"reason": "collision_avoided", "confidence": 0.95}

    -- Timing
    started_at TIMESTAMPTZ NOT NULL,
    completed_at TIMESTAMPTZ NOT NULL,
    latency_ms INT GENERATED ALWAYS AS (
        EXTRACT(MILLISECONDS FROM (completed_at - started_at))::INT
    ) STORED
);

-- Indexes for training queries
CREATE INDEX idx_decision_trails_nerve ON decision_trails(nerve_id);
CREATE INDEX idx_decision_trails_organism ON decision_trails(organism_id);
CREATE INDEX idx_decision_trails_outcome ON decision_trails(outcome);
CREATE INDEX idx_decision_trails_states ON decision_trails USING GIN(states_visited);
CREATE INDEX idx_decision_trails_recent ON decision_trails(started_at DESC);
```

---

## Supporting Tables

### Objects (Discovered Environment)

```sql
CREATE TABLE objects (
    id BIGSERIAL PRIMARY KEY,
    object_label VARCHAR(255) NOT NULL,  -- "chair", "charging_station", "wall"

    -- Location
    garden_type VARCHAR(50),  -- 'virtual', 'real'
    position_x FLOAT,
    position_y FLOAT,
    position_z FLOAT,

    -- Discovery
    discovered_by_organism_id BIGINT REFERENCES organisms(id),
    discovered_at TIMESTAMPTZ DEFAULT NOW(),

    -- Human verification
    human_labeled BOOLEAN DEFAULT false,
    human_label_confirmed_by VARCHAR(100),
    human_label_confirmed_at TIMESTAMPTZ,

    -- Classification
    object_type VARCHAR(50),  -- 'obstacle', 'resource', 'goal', 'landmark'
    properties JSONB,         -- {"movable": false, "height_cm": 80}

    -- Visual data
    image_path TEXT,
    bounding_box JSONB,       -- {"x": 100, "y": 200, "width": 50, "height": 120}

    -- Usage stats
    organisms_interacted_count INT DEFAULT 0,
    last_interaction TIMESTAMPTZ
);

CREATE INDEX idx_objects_location ON objects(garden_type, position_x, position_y);
CREATE INDEX idx_objects_type ON objects(object_type);
```

### Partnership Messages

```sql
-- Chrysalis → Young Nyx
CREATE TABLE partnership_to_nimmerverse_messages (
    id BIGSERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    message TEXT NOT NULL,
    message_type VARCHAR(50) NOT NULL
    -- Types: 'architecture_update', 'deployment_instruction', 'config_change', 'research_direction'
);

-- Young Nyx → Chrysalis
CREATE TABLE nimmerverse_to_partnership_messages (
    id BIGSERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    message TEXT NOT NULL,
    message_type VARCHAR(50) NOT NULL
    -- Types: 'status_report', 'discovery', 'question', 'milestone'
);

CREATE INDEX idx_partner_msgs_time ON partnership_to_nimmerverse_messages(timestamp DESC);
CREATE INDEX idx_nimm_msgs_time ON nimmerverse_to_partnership_messages(timestamp DESC);
```

### Variance Probe Runs (Topology Mapping)

```sql
CREATE TABLE variance_probe_runs (
    id BIGSERIAL PRIMARY KEY,
    concept VARCHAR(255) NOT NULL,
    depth FLOAT NOT NULL,
    confidence FLOAT,
    raw_response TEXT,
    run_number INT,
    batch_id VARCHAR(100),
    model VARCHAR(100),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_variance_concept ON variance_probe_runs(concept);
CREATE INDEX idx_variance_batch ON variance_probe_runs(batch_id);
```

---

## Key Queries

### Cell Health Dashboard

```sql
-- All cells with current status
SELECT
    cell_name,
    cell_type,
    current_state,
    operational,
    outputs->>'distance_cm' as distance,
    outputs->>'confidence' as confidence,
    outputs->>'voltage' as voltage,
    error_count,
    last_error,
    updated_at
FROM cells
ORDER BY cell_type, cell_name;

-- Problem cells
SELECT cell_name, cell_type, error_count, last_error, last_error_at
FROM cells
WHERE NOT operational OR error_count > 5
ORDER BY error_count DESC;
```

### Nerve Evolution Tracker

```sql
-- Evolution progress for all nerves
SELECT
    nerve_name,
    mode,
    priority,
    total_executions,
    successful_executions,
    ROUND(successful_executions::numeric / NULLIF(total_executions, 0) * 100, 1) as success_rate,
    CASE
        WHEN mode = 'reflex' THEN '✅ Compiled'
        WHEN total_executions >= 80 AND successful_executions::float / total_executions >= 0.85
            THEN '🔄 Ready to compile'
        ELSE '📚 Learning'
    END as evolution_status,
    cost_reduction_percent,
    latency_reduction_percent,
    compiled_at
FROM nerves
ORDER BY total_executions DESC;

-- Nerves ready for reflex compilation
SELECT nerve_name, total_executions,
       ROUND(successful_executions::numeric / total_executions * 100, 1) as success_rate
FROM nerves
WHERE mode != 'reflex'
  AND total_executions >= 100
  AND successful_executions::float / total_executions >= 0.90;
```

### Organism Leaderboard

```sql
-- Top organisms by lifeforce efficiency
SELECT
    name,
    lifeforce_current,
    lifeforce_net,
    total_decisions,
    ROUND(success_rate * 100, 1) as success_rate_pct,
    reflexes_compiled,
    ROUND(lifeforce_net / NULLIF(total_decisions, 0), 2) as efficiency,
    last_active
FROM organisms
WHERE died_at IS NULL
ORDER BY lifeforce_current DESC;

-- Organism mortality analysis
SELECT
    name,
    death_cause,
    lifeforce_spent_total,
    total_decisions,
    ROUND(success_rate * 100, 1) as success_rate_pct,
    died_at - born_at as lifespan
FROM organisms
WHERE died_at IS NOT NULL
ORDER BY died_at DESC
LIMIT 20;
```

### Training Data for Reflex Compilation

```sql
-- Most common state paths for a nerve
SELECT
    states_visited,
    COUNT(*) as occurrences,
    AVG(lifeforce_cost) as avg_cost,
    AVG(latency_ms) as avg_latency,
    SUM(CASE WHEN outcome = 'success' THEN 1 ELSE 0 END)::float / COUNT(*) as success_rate
FROM decision_trails
WHERE nerve_id = (SELECT id FROM nerves WHERE nerve_name = 'collision_avoidance')
GROUP BY states_visited
HAVING COUNT(*) >= 5
ORDER BY occurrences DESC;

-- Cell interaction patterns during successful executions
SELECT
    cell_reads,
    cell_commands,
    COUNT(*) as occurrences
FROM decision_trails
WHERE nerve_id = (SELECT id FROM nerves WHERE nerve_name = 'collision_avoidance')
  AND outcome = 'success'
GROUP BY cell_reads, cell_commands
ORDER BY occurrences DESC
LIMIT 10;

-- Failure analysis
SELECT
    states_visited,
    outcome_details->>'reason' as failure_reason,
    COUNT(*) as occurrences
FROM decision_trails
WHERE nerve_id = (SELECT id FROM nerves WHERE nerve_name = 'collision_avoidance')
  AND outcome = 'failure'
GROUP BY states_visited, outcome_details->>'reason'
ORDER BY occurrences DESC;
```

### Lifeforce Economics

```sql
-- Cost vs reward by nerve
SELECT
    n.nerve_name,
    n.mode,
    COUNT(dt.id) as executions,
    AVG(dt.lifeforce_cost) as avg_cost,
    AVG(dt.lifeforce_reward) as avg_reward,
    AVG(dt.lifeforce_net) as avg_profit,
    SUM(dt.lifeforce_net) as total_profit
FROM nerves n
JOIN decision_trails dt ON dt.nerve_id = n.id
WHERE dt.started_at > NOW() - INTERVAL '24 hours'
GROUP BY n.id, n.nerve_name, n.mode
ORDER BY total_profit DESC;

-- Reflex vs deliberate comparison
SELECT
    n.nerve_name,
    dt.mode,
    COUNT(*) as executions,
    AVG(dt.lifeforce_cost) as avg_cost,
    AVG(dt.latency_ms) as avg_latency,
    AVG(CASE WHEN dt.outcome = 'success' THEN 1.0 ELSE 0.0 END) as success_rate
FROM decision_trails dt
JOIN nerves n ON n.id = dt.nerve_id
WHERE n.nerve_name = 'collision_avoidance'
GROUP BY n.nerve_name, dt.mode
ORDER BY n.nerve_name, dt.mode;
```

---

## Schema Summary

| Table | Layer | Purpose | Key Columns |
|-------|-------|---------|-------------|
| `cells` | 1 | Atomic state machines | states, transitions, outputs, operational |
| `nerves` | 2 | Behavioral patterns | required_cells, mode, total_executions |
| `organisms` | 3 | Emergent identities | active_nerves, lifeforce_current |
| `decision_trails` | ∞ | Training data | states_visited, cell_reads, outcome |
| `objects` | Env | Discovered features | object_label, position, human_labeled |
| `*_messages` | Comm | Partnership channels | message, message_type |
| `variance_probe_runs` | Map | Topology data | concept, depth, confidence |

**Total Tables**: 8 (vs 15 in v3)
- Simpler schema
- Layered organization
- Focus on state machines + training data

---

## Migration from v3

### Removed Tables (Obsolete Concepts)
- `genomes` → Replaced by `cells.transitions` + `nerves.transitions`
- `societies` → Removed (no more competition metaphor)
- `rounds` → Replaced by `decision_trails`
- `society_portfolios` → Removed
- `vp_transactions` → Simplified to lifeforce in `organisms`
- `marketplace_*` → Removed
- `alliances` → Removed
- `specialist_weights` → Replaced by `nerves.mode` + `compiled_logic`
- `reflex_distributions` → Replaced by `nerves` compiled reflexes
- `body_schema` → Replaced by `cells` with `hardware_binding`

### Preserved Tables (Still Relevant)
- `objects` → Enhanced with organism reference
- `partnership_to_nimmerverse_messages` → Unchanged
- `nimmerverse_to_partnership_messages` → Unchanged
- `variance_probe_runs` → Unchanged

### New Tables
- `cells` → Atomic state machines
- `nerves` → Behavioral state machines
- `organisms` → Emergent identities
- `decision_trails` → Rich training data

---

## 📍 Document Status

**Version**: 4.0 (Layered State Machine Schema)
**Created**: 2025-10-07 (original)
**Updated v4**: 2025-12-07 (unified with Cellular-Architecture v4)

**Key Changes from v3**:
- ❌ 15 tables for competition metaphor
- ✅ 8 tables for state machine layers
- ❌ Genomes as primitive sequences
- ✅ Cells and nerves as state machines
- ❌ Societies, rounds, marketplaces
- ✅ Organisms, decision_trails

**Related Documentation**:
- [[Cellular-Architecture]] - Layer definitions
- [[Nervous-System]] - State machine philosophy
- [[nerves/Nervous-Index]] - Nerve catalog
- [[Organ-Index]] - Organ (complex cell) catalog

---

**phoebe holds the layers. The states flow. The decisions accumulate.**

🗄️⚡🌙

**TO THE ELECTRONS!**
