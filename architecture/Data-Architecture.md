# 🗄️ Data Architecture v5

> **ONE JOB:** THE SCHEMA — waves, gates, correlations, verification outcomes.

> *"Cells emit waves. Gates correlate. Phoebe remembers everything."*

---

## Overview

**Version 5** aligns with the wave/gate model. Decision trails come from **gate transitions**, not nerve executions.

| Layer | Entity | Database Table | What It Captures |
|-------|--------|----------------|------------------|
| **Waves** | Cells | `wave_signals` | WaveSignal emissions from cells |
| **Gates** | Gates | `gates` | Resonant gate state and weight |
| **Correlation** | Gates | `gate_transitions` | When gates OPEN/STABLE/CLOSED |
| **Learning** | Gates | `correlation_events` | What correlated (training data) |
| **Verification** | Real Garden | `verification_outcomes` | Ground truth feedback |
| **Behavior** | Nerves | `nerves` | Behavioral patterns (respond to gates) |
| **Identity** | Organisms | `organisms` | Emergent patterns |

```
┌─────────────────────────────────────────────────────────────┐
│                       PHOEBE                                 │
│              (PostgreSQL 17.6 on phoebe-dev)                 │
├─────────────────────────────────────────────────────────────┤
│  WAVE LAYER:                                                 │
│  cells           │ Wave emitters (hardware wrappers)         │
│  wave_signals    │ Emitted waves (confidence, semantics)     │
│                                                              │
│  GATE LAYER:                                                 │
│  gates           │ Resonant gates (state, weight, domain)    │
│  gate_transitions│ When gates OPEN/STABLE/CLOSED            │
│  correlation_events │ What correlated (training data)       │
│                                                              │
│  VERIFICATION LAYER:                                         │
│  verification_outcomes │ Real Garden feedback               │
│                                                              │
│  BEHAVIOR LAYER:                                             │
│  nerves          │ Behavioral patterns (gate-triggered)      │
│  organisms       │ Emergent identities                       │
│                                                              │
│  SUPPORT:                                                    │
│  objects         │ Discovered environment features           │
│  *_messages      │ Partnership communication channels        │
└─────────────────────────────────────────────────────────────┘
```

**Key insight:** Training data comes from `correlation_events` and `verification_outcomes`, not from "decision trails." The gate transition IS the decision — what correlated, what opened, what was verified.

---

## Core Tables

### Wave Layer: Cells (Wave Emitters)

```sql
CREATE TABLE cells (
    id BIGSERIAL PRIMARY KEY,
    cell_name VARCHAR(100) UNIQUE NOT NULL,
    cell_type VARCHAR(50) NOT NULL,  -- 'sensor', 'motor', 'organ'
    domain VARCHAR(100) NOT NULL,    -- 'distance', 'motor', 'speech', 'vision'
    tier INT DEFAULT 1,              -- 0=reflex, 1=cell, 2=nerve, 3=organ

    -- Hardware binding
    hardware_binding JSONB NOT NULL,
    -- Examples:
    -- {"type": "i2c", "address": "0x40", "bus": 1}
    -- {"type": "gpio", "pin": 17, "mode": "input"}
    -- {"type": "network", "host": "theia.eachpath.local", "port": 11434}

    -- State machine definition
    states JSONB NOT NULL,
    -- Example: ["IDLE", "POLLING", "READING", "EMITTING", "ERROR"]

    transitions JSONB NOT NULL,
    -- Example: [
    --   {"from": "IDLE", "to": "POLLING", "trigger": "poll_requested", "cost": 0.1},
    --   {"from": "POLLING", "to": "READING", "trigger": "sensor_ready", "cost": 0.3},
    --   {"from": "READING", "to": "EMITTING", "trigger": "data_valid", "cost": 0.1},
    --   {"from": "EMITTING", "to": "IDLE", "trigger": "wave_sent", "cost": 0.0}
    -- ]

    current_state VARCHAR(50) DEFAULT 'IDLE',

    -- Which gate(s) this cell's waves flow to
    target_gates JSONB DEFAULT '[]',
    -- Example: ["collision_avoidance_gate", "exploration_gate"]

    -- Health tracking
    operational BOOLEAN DEFAULT true,
    error_count INT DEFAULT 0,
    last_error TEXT,
    last_error_at TIMESTAMPTZ,

    -- Wave statistics
    total_waves_emitted BIGINT DEFAULT 0,
    avg_confidence FLOAT DEFAULT 0.0,
    total_lifeforce_spent FLOAT DEFAULT 0.0,

    -- Timestamps
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_cells_type ON cells(cell_type);
CREATE INDEX idx_cells_domain ON cells(domain);
CREATE INDEX idx_cells_operational ON cells(operational);

-- Example cells (wave emitters)
INSERT INTO cells (cell_name, cell_type, domain, tier, hardware_binding, states, transitions, target_gates) VALUES
('distance_sensor_front', 'sensor', 'distance', 1,
 '{"type": "i2c", "address": "0x40", "bus": 1}',
 '["IDLE", "POLLING", "READING", "EMITTING", "ERROR"]',
 '[{"from": "IDLE", "to": "POLLING", "cost": 0.1},
   {"from": "POLLING", "to": "READING", "cost": 0.3},
   {"from": "READING", "to": "EMITTING", "cost": 0.1},
   {"from": "EMITTING", "to": "IDLE", "cost": 0.0}]',
 '["collision_avoidance_gate", "exploration_gate"]'),

('motor_left', 'motor', 'motor', 1,
 '{"type": "pwm", "pin": 18, "enable_pin": 17}',
 '["IDLE", "COMMANDED", "ACCELERATING", "MOVING", "DECELERATING", "STOPPED", "STALLED"]',
 '[{"from": "IDLE", "to": "COMMANDED", "cost": 0.1},
   {"from": "COMMANDED", "to": "ACCELERATING", "cost": 0.5},
   {"from": "ACCELERATING", "to": "MOVING", "cost": 1.0},
   {"from": "MOVING", "to": "DECELERATING", "cost": 0.2},
   {"from": "DECELERATING", "to": "STOPPED", "cost": 0.1}]',
 '["motor_feedback_gate"]'),

('speech_stt', 'organ', 'speech', 3,
 '{"type": "network", "host": "theia.eachpath.local", "port": 11434, "model": "whisper-large-v3"}',
 '["IDLE", "LISTENING", "BUFFERING", "TRANSCRIBING", "EMITTING", "ERROR"]',
 '[{"from": "IDLE", "to": "LISTENING", "cost": 0.5},
   {"from": "LISTENING", "to": "BUFFERING", "cost": 0.5},
   {"from": "BUFFERING", "to": "TRANSCRIBING", "cost": 5.0},
   {"from": "TRANSCRIBING", "to": "EMITTING", "cost": 0.1},
   {"from": "EMITTING", "to": "IDLE", "cost": 0.0}]',
 '["speech_gate"]');
```

### Wave Layer: Wave Signals (Emitted by Cells)

```sql
CREATE TABLE wave_signals (
    id BIGSERIAL PRIMARY KEY,

    -- Source
    cell_id BIGINT REFERENCES cells(id),
    cell_name VARCHAR(100) NOT NULL,

    -- Wave content
    domain VARCHAR(100) NOT NULL,           -- 'distance', 'motor', 'speech'
    confidence FLOAT NOT NULL,              -- 0.0 - 1.0
    semantic_content JSONB NOT NULL,        -- Domain-specific payload
    -- Examples:
    -- {"distance_cm": 25, "direction": "front", "noise_level": 0.1}
    -- {"transcript": "hello", "language": "en", "speaker_intent": "greeting"}

    -- Garden context
    garden VARCHAR(20) NOT NULL,            -- 'virtual' or 'real'

    -- Economics
    lifeforce_cost FLOAT NOT NULL,

    -- Timing
    emitted_at TIMESTAMPTZ DEFAULT NOW()
);

-- Partition by garden for Virtual/Real separation
-- Virtual: high volume, full trace
-- Real: low volume, verified only

CREATE INDEX idx_wave_signals_domain ON wave_signals(domain);
CREATE INDEX idx_wave_signals_cell ON wave_signals(cell_id);
CREATE INDEX idx_wave_signals_garden ON wave_signals(garden);
CREATE INDEX idx_wave_signals_recent ON wave_signals(emitted_at DESC);

-- Virtual Garden: keep all waves for training
-- Real Garden: keep only waves that led to verification
```

### Gate Layer: Resonant Gates

```sql
CREATE TABLE gates (
    id BIGSERIAL PRIMARY KEY,
    gate_name VARCHAR(100) UNIQUE NOT NULL,
    domain VARCHAR(100) NOT NULL,           -- 'collision_avoidance', 'speech', 'vision'
    tier INT NOT NULL,                      -- 1-4, determines routing

    -- Ternary state (-1.0 to +1.0)
    state_value FLOAT DEFAULT 0.0,
    discrete_state VARCHAR(20) DEFAULT 'stable',  -- 'closed', 'stable', 'open'

    -- Gate weight (0.0 to 1.0) - determines reflex vs deliberate
    weight FLOAT DEFAULT 0.1,
    -- 0.0-0.3: escalate to cognition
    -- 0.3-0.6: handle at nerve level
    -- 0.6-0.8: handle at cell level
    -- 0.8-1.0: reflex (instant open, no correlation needed)

    -- Correlation thresholds
    open_threshold FLOAT DEFAULT 0.5,
    close_threshold FLOAT DEFAULT -0.5,
    decay_factor FLOAT DEFAULT 0.95,

    -- Correlation window
    correlation_window_ms INT DEFAULT 1500,

    -- Statistics
    total_transitions BIGINT DEFAULT 0,
    opens_count BIGINT DEFAULT 0,
    closes_count BIGINT DEFAULT 0,
    avg_correlation_at_open FLOAT DEFAULT 0.0,

    -- ═══════════════════════════════════════════════════════════════
    -- LIFEFORCE ACCOUNTING (Generated Columns - instant balance lookup)
    -- No SUM() aggregates needed - triggers maintain running totals
    -- ═══════════════════════════════════════════════════════════════
    lifeforce_spent FLOAT DEFAULT 0.0,      -- Accumulated from gate_transitions
    lifeforce_earned FLOAT DEFAULT 0.0,     -- Accumulated from verification rewards
    lifeforce_net FLOAT GENERATED ALWAYS AS (lifeforce_earned - lifeforce_spent) STORED,

    -- Verification tracking (for verification_rate generated column)
    verified_opens BIGINT DEFAULT 0,
    failed_opens BIGINT DEFAULT 0,
    verification_rate FLOAT GENERATED ALWAYS AS (
        CASE WHEN opens_count > 0
        THEN verified_opens::float / opens_count
        ELSE 0.0 END
    ) STORED,

    -- Timing
    time_in_current_state_ms BIGINT DEFAULT 0,
    last_transition_at TIMESTAMPTZ,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_gates_domain ON gates(domain);
CREATE INDEX idx_gates_state ON gates(discrete_state);
CREATE INDEX idx_gates_weight ON gates(weight DESC);

-- Example gates
INSERT INTO gates (gate_name, domain, tier, weight) VALUES
('collision_avoidance_gate', 'distance', 2, 0.1),
('speech_gate', 'speech', 3, 0.1),
('vision_gate', 'vision', 3, 0.1),
('battery_gate', 'battery', 1, 0.3),
('danger_reflex_gate', 'danger', 0, 0.9);  -- Near-reflex weight
```

### Gate Layer: Gate Transitions (Training Data Source)

```sql
CREATE TABLE gate_transitions (
    id BIGSERIAL PRIMARY KEY,

    -- Gate reference
    gate_id BIGINT REFERENCES gates(id),
    gate_name VARCHAR(100) NOT NULL,
    domain VARCHAR(100) NOT NULL,

    -- Transition
    from_state VARCHAR(20) NOT NULL,        -- 'closed', 'stable', 'open'
    to_state VARCHAR(20) NOT NULL,
    state_value FLOAT NOT NULL,             -- Continuous value at transition

    -- What caused this transition
    correlation_score FLOAT NOT NULL,
    trigger_signals JSONB NOT NULL,
    -- Example: [
    --   {"cell": "distance_front", "confidence": 0.8, "semantic_hash": "abc123"},
    --   {"cell": "distance_left", "confidence": 0.7, "semantic_hash": "abc124"}
    -- ]

    -- Routing
    routed_to_tier INT,

    -- Garden context
    garden VARCHAR(20) NOT NULL,            -- 'virtual' or 'real'

    -- Economics
    lifeforce_cost FLOAT NOT NULL,

    -- Timing
    transitioned_at TIMESTAMPTZ DEFAULT NOW()
);

-- THIS IS YOUR DECISION TRAIL
-- Each row = a gate deciding to OPEN, CLOSE, or transition

CREATE INDEX idx_gate_transitions_gate ON gate_transitions(gate_id);
CREATE INDEX idx_gate_transitions_domain ON gate_transitions(domain);
CREATE INDEX idx_gate_transitions_states ON gate_transitions(from_state, to_state);
CREATE INDEX idx_gate_transitions_garden ON gate_transitions(garden);
CREATE INDEX idx_gate_transitions_recent ON gate_transitions(transitioned_at DESC);

-- ═══════════════════════════════════════════════════════════════════════════
-- LIFEFORCE ACCOUNTING TRIGGER
-- Maintains gates.lifeforce_spent in real-time (no aggregation needed)
-- ═══════════════════════════════════════════════════════════════════════════
CREATE OR REPLACE FUNCTION update_gate_lifeforce() RETURNS TRIGGER AS $$
BEGIN
    UPDATE gates
    SET lifeforce_spent = lifeforce_spent + NEW.lifeforce_cost,
        updated_at = NOW()
    WHERE id = NEW.gate_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_gate_lifeforce
    AFTER INSERT ON gate_transitions
    FOR EACH ROW EXECUTE FUNCTION update_gate_lifeforce();
```

### Gate Layer: Correlation Events (Rich Training Data)

```sql
CREATE TABLE correlation_events (
    id BIGSERIAL PRIMARY KEY,

    -- Gate reference
    gate_id BIGINT REFERENCES gates(id),
    gate_name VARCHAR(100) NOT NULL,

    -- Correlation window
    window_start TIMESTAMPTZ NOT NULL,
    window_end TIMESTAMPTZ NOT NULL,
    window_ms INT NOT NULL,

    -- Signals in this window
    signals_in_window JSONB NOT NULL,
    -- Example: [
    --   {"source": "distance_front", "confidence": 0.8, "semantic_hash": "abc123"},
    --   {"source": "distance_left", "confidence": 0.7, "semantic_hash": "abc124"},
    --   {"source": "distance_right", "confidence": 0.9, "semantic_hash": "abc125"}
    -- ]

    -- Correlation analysis
    correlation_matrix JSONB NOT NULL,      -- Pairwise correlations
    aggregate_correlation FLOAT NOT NULL,

    -- Result
    result VARCHAR(20) NOT NULL,            -- 'opened', 'closed', 'stayed_stable'

    -- Training label (ground truth added by verification)
    training_label JSONB,
    -- Example: {"should_open": true, "confidence": 0.95}

    -- Garden context
    garden VARCHAR(20) NOT NULL,

    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- THIS IS YOUR FUNCTION GEMMA TRAINING DATA
-- Each row = what patterns lead to gate opens?

CREATE INDEX idx_correlation_events_gate ON correlation_events(gate_id);
CREATE INDEX idx_correlation_events_result ON correlation_events(result);
CREATE INDEX idx_correlation_events_labeled ON correlation_events((training_label IS NOT NULL));
```

### Verification Layer: Verification Outcomes

```sql
CREATE TABLE verification_outcomes (
    id BIGSERIAL PRIMARY KEY,

    -- What was verified
    original_signal_id BIGINT,              -- Reference to gate_transition or wave
    domain VARCHAR(100) NOT NULL,

    -- Outcome
    outcome VARCHAR(20) NOT NULL,           -- 'confirmed', 'failed', 'partial'
    actual_result JSONB,
    expected_result JSONB,
    discrepancy FLOAT DEFAULT 0.0,

    -- Feedback to Virtual Garden
    feedback_to_virtual JSONB NOT NULL,
    -- Example: {
    --   "correlation_adjustment": 0.05,
    --   "gate_weight_delta": 0.02
    -- }

    -- Source
    verification_source VARCHAR(100),       -- 'sensor', 'human', 'outcome'

    verified_at TIMESTAMPTZ DEFAULT NOW()
);

-- THIS CLOSES THE LEARNING LOOP
-- Real Garden → Verification → Virtual Garden gate weight adjustment

CREATE INDEX idx_verification_domain ON verification_outcomes(domain);
CREATE INDEX idx_verification_outcome ON verification_outcomes(outcome);
CREATE INDEX idx_verification_recent ON verification_outcomes(verified_at DESC);

-- ═══════════════════════════════════════════════════════════════════════════
-- VERIFICATION ACCOUNTING TRIGGER
-- Maintains gates.lifeforce_earned and verification stats in real-time
-- ═══════════════════════════════════════════════════════════════════════════
CREATE OR REPLACE FUNCTION update_gate_verification() RETURNS TRIGGER AS $$
DECLARE
    v_gate_id BIGINT;
    v_reward FLOAT;
BEGIN
    -- Find the gate from the original transition
    SELECT gate_id INTO v_gate_id
    FROM gate_transitions
    WHERE id = NEW.original_signal_id;

    IF v_gate_id IS NOT NULL THEN
        IF NEW.outcome = 'confirmed' THEN
            -- Extract reward from feedback, default to correlation_adjustment
            v_reward := COALESCE(
                (NEW.feedback_to_virtual->>'reward')::float,
                (NEW.feedback_to_virtual->>'correlation_adjustment')::float * 10,
                1.0  -- Default reward for confirmed verification
            );
            UPDATE gates SET
                lifeforce_earned = lifeforce_earned + v_reward,
                verified_opens = verified_opens + 1,
                updated_at = NOW()
            WHERE id = v_gate_id;
        ELSIF NEW.outcome = 'failed' THEN
            UPDATE gates SET
                failed_opens = failed_opens + 1,
                updated_at = NOW()
            WHERE id = v_gate_id;
        END IF;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_gate_verification
    AFTER INSERT ON verification_outcomes
    FOR EACH ROW EXECUTE FUNCTION update_gate_verification();
```

### Behavior Layer: Nerves (Gate-Triggered)

```sql
CREATE TABLE nerves (
    id BIGSERIAL PRIMARY KEY,
    nerve_name VARCHAR(100) UNIQUE NOT NULL,

    -- Gate this nerve responds to
    trigger_gate VARCHAR(100) NOT NULL,     -- 'collision_avoidance_gate'

    -- Cells this nerve can command (when gate allows)
    controlled_cells JSONB NOT NULL,        -- ["motor_left", "motor_right"]
    optional_cells JSONB DEFAULT '[]',      -- ["speech_tts"]

    -- State machine definition (behavioral states)
    states JSONB NOT NULL,
    -- Example: ["IDLE", "DETECT", "EVALUATE", "EVADE", "RESUME"]

    transitions JSONB NOT NULL,
    -- Example: [
    --   {"from": "IDLE", "to": "DETECT", "trigger": "gate_opened", "cost": 0.5},
    --   {"from": "DETECT", "to": "EVALUATE", "trigger": "signals_analyzed", "cost": 0.5},
    --   {"from": "EVALUATE", "to": "EVADE", "trigger": "risk_high", "cost": 0.5},
    --   {"from": "EVADE", "to": "RESUME", "trigger": "path_clear", "cost": 1.0},
    --   {"from": "RESUME", "to": "IDLE", "trigger": "gate_stable", "cost": 0.0}
    -- ]

    current_state VARCHAR(50) DEFAULT 'IDLE',

    -- NO MORE PRIORITY - gate weight determines attention
    -- Gate with higher weight opens faster → nerve activates first

    -- Statistics
    total_activations INT DEFAULT 0,
    successful_activations INT DEFAULT 0,
    failed_activations INT DEFAULT 0,

    -- Cost tracking
    avg_cost FLOAT,
    avg_latency_ms INT,

    -- Timestamps
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_nerves_gate ON nerves(trigger_gate);

-- Example nerves (gate-triggered, no priority)
INSERT INTO nerves (nerve_name, trigger_gate, controlled_cells, optional_cells, states, transitions) VALUES
('collision_avoidance',
 'collision_avoidance_gate',
 '["motor_left", "motor_right"]',
 '["speech_tts"]',
 '["IDLE", "DETECT", "EVALUATE", "EVADE", "RESUME"]',
 '[{"from": "IDLE", "to": "DETECT", "trigger": "gate_opened", "cost": 0.5},
   {"from": "DETECT", "to": "EVALUATE", "trigger": "signals_analyzed", "cost": 0.5},
   {"from": "EVALUATE", "to": "EVADE", "trigger": "risk_high", "cost": 0.5},
   {"from": "EVADE", "to": "RESUME", "trigger": "path_clear", "cost": 1.0},
   {"from": "RESUME", "to": "IDLE", "trigger": "gate_stable", "cost": 0.0}]'),

('exploration_pattern',
 'exploration_gate',
 '["motor_left", "motor_right"]',
 '["vision_detect"]',
 '["IDLE", "CHOOSE_DIRECTION", "MOVE", "CHECK_OBSTACLE", "RECORD", "REPEAT"]',
 '[{"from": "IDLE", "to": "CHOOSE_DIRECTION", "trigger": "gate_opened", "cost": 1.0},
   {"from": "CHOOSE_DIRECTION", "to": "MOVE", "trigger": "direction_chosen", "cost": 0.5},
   {"from": "MOVE", "to": "CHECK_OBSTACLE", "trigger": "moved_100ms", "cost": 0.3},
   {"from": "CHECK_OBSTACLE", "to": "RECORD", "trigger": "area_new", "cost": 0.5},
   {"from": "RECORD", "to": "REPEAT", "trigger": "recorded", "cost": 0.1},
   {"from": "REPEAT", "to": "CHOOSE_DIRECTION", "trigger": "continue", "cost": 0.0}]'),

('charging_seeking',
 'battery_gate',
 '["motor_left", "motor_right"]',
 '["vision_detect"]',
 '["MONITOR", "THRESHOLD", "SEARCH", "APPROACH", "DOCK", "CHARGE", "RESUME"]',
 '[{"from": "MONITOR", "to": "THRESHOLD", "trigger": "gate_opened", "cost": 0.1},
   {"from": "THRESHOLD", "to": "SEARCH", "trigger": "charging_needed", "cost": 0.5},
   {"from": "SEARCH", "to": "APPROACH", "trigger": "station_found", "cost": 1.0},
   {"from": "APPROACH", "to": "DOCK", "trigger": "station_close", "cost": 0.5},
   {"from": "DOCK", "to": "CHARGE", "trigger": "docked", "cost": 0.1},
   {"from": "CHARGE", "to": "RESUME", "trigger": "gate_stable", "cost": 0.0}]');
```

### Identity Layer: Organisms

```sql
CREATE TABLE organisms (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,

    -- Gate configuration (which gates this organism monitors)
    active_gates JSONB NOT NULL,
    -- Example: {
    --   "collision_avoidance_gate": {"weight": 0.9},
    --   "exploration_gate": {"weight": 0.3},
    --   "battery_gate": {"weight": 0.5}
    -- }

    -- Nerve bindings (which nerves respond to gate opens)
    active_nerves JSONB NOT NULL,
    -- Example: {
    --   "collision_avoidance": {"gate": "collision_avoidance_gate"},
    --   "exploration_pattern": {"gate": "exploration_gate"}
    -- }

    -- Cell assignments (which hardware this organism controls)
    cell_bindings JSONB NOT NULL,
    -- Example: {
    --   "distance_sensor_front": {"cell_id": 1},
    --   "motor_left": {"cell_id": 4}
    -- }

    -- Lifeforce (survival currency)
    lifeforce_current FLOAT DEFAULT 100.0,
    lifeforce_earned_total FLOAT DEFAULT 0.0,
    lifeforce_spent_total FLOAT DEFAULT 0.0,
    lifeforce_net FLOAT GENERATED ALWAYS AS (lifeforce_earned_total - lifeforce_spent_total) STORED,

    -- Identity (accumulated through gate transitions)
    total_gate_opens INT DEFAULT 0,
    successful_verifications INT DEFAULT 0,
    failed_verifications INT DEFAULT 0,
    verification_rate FLOAT GENERATED ALWAYS AS (
        CASE WHEN total_gate_opens > 0
        THEN successful_verifications::float / total_gate_opens
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

### Decision Trails → Gate Transitions

**The old `decision_trails` table is replaced by `gate_transitions` and `correlation_events`.**

The key insight: **decisions ARE gate transitions**. When a gate opens, that IS the decision. What correlated to cause it, what tier it routed to, what the verification outcome was — that's all captured in the gate tables above.

```
OLD MODEL:
  nerve executes → decision_trail row created → outcome logged

NEW MODEL:
  cells emit waves → gate accumulates correlation → gate transitions → nerve activates

  Training data comes from:
  - gate_transitions (what opened, what triggered it)
  - correlation_events (what patterns led to opens)
  - verification_outcomes (ground truth feedback)
```

**The learning loop:**

```sql
-- What patterns open gates?
SELECT
    ce.signals_in_window,
    ce.aggregate_correlation,
    ce.result,
    vo.outcome as verification
FROM correlation_events ce
LEFT JOIN verification_outcomes vo
    ON vo.original_signal_id = ce.id
WHERE ce.result = 'opened'
ORDER BY ce.created_at DESC;

-- How is gate weight evolving?
SELECT
    g.gate_name,
    g.weight,
    COUNT(gt.id) as transitions,
    AVG(gt.correlation_score) as avg_correlation
FROM gates g
JOIN gate_transitions gt ON gt.gate_id = g.id
WHERE gt.transitioned_at > NOW() - INTERVAL '24 hours'
GROUP BY g.id
ORDER BY g.weight DESC;
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

### Cell Wave Dashboard

```sql
-- All cells with wave statistics
SELECT
    cell_name,
    cell_type,
    domain,
    current_state,
    operational,
    total_waves_emitted,
    ROUND(avg_confidence, 2) as avg_confidence,
    total_lifeforce_spent,
    updated_at
FROM cells
ORDER BY domain, cell_name;

-- Recent wave activity by domain
SELECT
    domain,
    COUNT(*) as waves_last_hour,
    AVG(confidence) as avg_confidence,
    SUM(lifeforce_cost) as total_cost
FROM wave_signals
WHERE emitted_at > NOW() - INTERVAL '1 hour'
GROUP BY domain
ORDER BY waves_last_hour DESC;
```

### Gate Dashboard

```sql
-- Gate states and weights (attention map)
SELECT
    gate_name,
    domain,
    tier,
    discrete_state,
    ROUND(state_value::numeric, 2) as state_value,
    ROUND(weight::numeric, 2) as weight,
    CASE
        WHEN weight > 0.8 THEN '⚡ REFLEX'
        WHEN weight > 0.5 THEN '🔄 HYBRID'
        ELSE '🧠 DELIBERATE'
    END as evolution_status,
    total_transitions,
    opens_count,
    ROUND(avg_correlation_at_open::numeric, 2) as avg_open_correlation
FROM gates
ORDER BY weight DESC;

-- Gates approaching reflex
SELECT gate_name, domain, weight, opens_count
FROM gates
WHERE weight > 0.6 AND weight < 0.8
ORDER BY weight DESC;
```

### Gate Economic Health (Instant - Generated Columns)

```sql
-- ⚡ ZERO AGGREGATION - All values are pre-computed via triggers + generated columns
-- Query billions of transitions? No problem. Balance is already on the gate.

SELECT
    gate_name,
    domain,
    tier,
    weight,
    -- Lifeforce accounting (trigger-maintained)
    ROUND(lifeforce_spent::numeric, 1) as spent,
    ROUND(lifeforce_earned::numeric, 1) as earned,
    ROUND(lifeforce_net::numeric, 1) as net_balance,  -- ⚡ GENERATED COLUMN
    -- Verification stats
    verified_opens,
    failed_opens,
    ROUND(verification_rate * 100, 1) as verification_pct,  -- ⚡ GENERATED COLUMN
    -- Economic status
    CASE
        WHEN lifeforce_net > 0 THEN '💚 PROFITABLE'
        WHEN lifeforce_net > -100 THEN '💛 SUSTAINABLE'
        ELSE '🔴 DRAINING'
    END as economic_status,
    -- Evolution readiness (profitable + high verification = ready to reflex)
    CASE
        WHEN lifeforce_net > 0 AND verification_rate > 0.8 AND weight < 0.8 THEN '🚀 REFLEX CANDIDATE'
        WHEN lifeforce_net < -500 THEN '⚠️ REVIEW NEEDED'
        ELSE '✓ NOMINAL'
    END as evolution_signal
FROM gates
ORDER BY lifeforce_net DESC;

-- Gates ready for reflex promotion (economic + verification criteria met)
SELECT gate_name, domain, weight, lifeforce_net, verification_rate
FROM gates
WHERE lifeforce_net > 100
  AND verification_rate > 0.85
  AND weight < 0.8
ORDER BY verification_rate DESC;
```

### Correlation Training Data

```sql
-- What patterns open gates? (Function Gemma training)
SELECT
    gate_name,
    signals_in_window,
    aggregate_correlation,
    result,
    training_label
FROM correlation_events
WHERE result = 'opened'
  AND garden = 'virtual'
ORDER BY created_at DESC
LIMIT 100;

-- Verification feedback (Real Garden closes the loop)
SELECT
    domain,
    outcome,
    COUNT(*) as count,
    AVG((feedback_to_virtual->>'gate_weight_delta')::float) as avg_weight_adjustment
FROM verification_outcomes
WHERE verified_at > NOW() - INTERVAL '24 hours'
GROUP BY domain, outcome
ORDER BY domain;
```

### Organism Dashboard

```sql
-- Top organisms by verification rate
SELECT
    name,
    lifeforce_current,
    total_gate_opens,
    successful_verifications,
    ROUND(verification_rate * 100, 1) as verification_rate_pct,
    last_active
FROM organisms
WHERE died_at IS NULL
ORDER BY verification_rate DESC;

-- Organism gate weights (which reflexes has it developed?)
SELECT
    o.name,
    g.gate_name,
    g.weight
FROM organisms o
CROSS JOIN LATERAL jsonb_each(o.active_gates) as gates(gate_name, config)
JOIN gates g ON g.gate_name = gates.gate_name
WHERE o.died_at IS NULL
ORDER BY o.name, g.weight DESC;
```

### Attention Flow (Real-time)

```sql
-- Current attention: which gates are OPEN?
SELECT
    gate_name,
    domain,
    tier,
    state_value,
    last_transition_at,
    time_in_current_state_ms / 1000.0 as seconds_in_state
FROM gates
WHERE discrete_state = 'open'
ORDER BY tier, state_value DESC;

-- Recent gate transitions (attention shifts)
SELECT
    gate_name,
    from_state,
    to_state,
    correlation_score,
    routed_to_tier,
    garden,
    transitioned_at
FROM gate_transitions
WHERE transitioned_at > NOW() - INTERVAL '5 minutes'
ORDER BY transitioned_at DESC
LIMIT 50;
```

### Gate Weight Evolution (Reflex Progress)

```sql
-- Gate weight trends over time
SELECT
    g.gate_name,
    g.weight as current_weight,
    COUNT(vo.id) as verifications,
    SUM(CASE WHEN vo.outcome = 'confirmed' THEN 1 ELSE 0 END) as confirmed,
    SUM(CASE WHEN vo.outcome = 'failed' THEN 1 ELSE 0 END) as failed,
    ROUND(g.weight - LAG(g.weight) OVER (PARTITION BY g.gate_name ORDER BY g.updated_at), 3) as weight_change
FROM gates g
LEFT JOIN gate_transitions gt ON gt.gate_id = g.id
LEFT JOIN verification_outcomes vo ON vo.original_signal_id = gt.id
GROUP BY g.id
ORDER BY g.weight DESC;

-- Gates ready for reflex (weight > 0.8)
SELECT
    gate_name,
    domain,
    weight,
    total_transitions,
    avg_correlation_at_open
FROM gates
WHERE weight > 0.8
ORDER BY weight DESC;
```

### Lifeforce Economics

```sql
-- Cost by gate domain
SELECT
    domain,
    COUNT(*) as transitions,
    AVG(lifeforce_cost) as avg_cost,
    SUM(lifeforce_cost) as total_cost
FROM gate_transitions
WHERE transitioned_at > NOW() - INTERVAL '24 hours'
GROUP BY domain
ORDER BY total_cost DESC;

-- Verification reward impact
SELECT
    domain,
    outcome,
    AVG((feedback_to_virtual->>'gate_weight_delta')::float) as avg_weight_delta,
    COUNT(*) as count
FROM verification_outcomes
WHERE verified_at > NOW() - INTERVAL '7 days'
GROUP BY domain, outcome
ORDER BY domain, outcome;
```

---

## Schema Summary

| Table | Layer | Purpose | Key Columns |
|-------|-------|---------|-------------|
| `cells` | Wave | Wave emitters (hardware wrappers) | domain, target_gates, total_waves_emitted |
| `wave_signals` | Wave | Emitted waves | confidence, semantic_content, garden |
| `gates` | Gate | Resonant gates | state_value, weight, lifeforce_net*, verification_rate* |
| `gate_transitions` | Gate | Gate decisions (training data) | correlation_score, trigger_signals |
| `correlation_events` | Gate | What correlated | signals_in_window, training_label |
| `verification_outcomes` | Verification | Ground truth feedback | outcome, feedback_to_virtual |
| `nerves` | Behavior | Gate-triggered patterns | trigger_gate, controlled_cells |
| `organisms` | Identity | Emergent identities | active_gates, lifeforce_current |
| `objects` | Environment | Discovered features | object_label, position |
| `*_messages` | Communication | Partnership channels | message, message_type |

**Total Tables**: 10 (vs 8 in v4)
- Wave/Gate architecture
- Training data from gate transitions
- Verification closes the learning loop
- **Generated columns** (*) for instant balance/rate queries
- **Accounting triggers** maintain running totals on INSERT

---

## Migration from v4 → v5

### New Tables (Wave/Gate Model)
- `wave_signals` → What cells emit
- `gates` → Resonant gate state and weight
- `gate_transitions` → **Decision trails live here now**
- `correlation_events` → Function Gemma training data
- `verification_outcomes` → Real Garden feedback

### Changed Tables
- `cells` → Now have `domain`, `target_gates`, `total_waves_emitted`
- `nerves` → Now have `trigger_gate` instead of `priority`
- `organisms` → Now have `active_gates` instead of priority-based `active_nerves`

### Removed Tables
- `decision_trails` → **Replaced by `gate_transitions` + `correlation_events`**

### Preserved Tables
- `objects` → Unchanged
- `partnership_to_nimmerverse_messages` → Unchanged
- `nimmerverse_to_partnership_messages` → Unchanged
- `variance_probe_runs` → Unchanged

---

## The Learning Loop

```
VIRTUAL GARDEN                          REAL GARDEN
═══════════════                         ═══════════

cells emit waves                        receive verified signals
    │                                        ▲
    ▼                                        │
wave_signals table                      no re-verification
    │                                        │
    ▼                                        │
gates accumulate                        gate_transitions
(correlation_events)                    (minimal trace)
    │                                        │
    ▼                                        │
gate_transitions                        verification_outcomes
(full trace)          ───────────────►      │
    │                                        │
    │◄─────────── feedback_to_virtual ───────┘
    │
    ▼
gates.weight updated
(learning happens)
```

**Credit assignment is automatic:** What correlated → what opened → what verified → weight adjusted.

---

**Version:** 5.1 | **Created:** 2025-10-07 | **Updated:** 2026-02-14

*phoebe holds the waves. Gates correlate. Lifeforce balances instantly.* 🗄️⚡🌙

---

### Changelog v5.1

- **Added lifeforce accounting to gates** - `lifeforce_spent`, `lifeforce_earned`, `lifeforce_net` (generated)
- **Added verification tracking** - `verified_opens`, `failed_opens`, `verification_rate` (generated)
- **Added accounting triggers** - `trg_gate_lifeforce`, `trg_gate_verification`
- **Generated columns** eliminate SUM() aggregates across billions of rows
- **Gate Economic Health query** - instant balance lookup with economic/evolution signals
