# 🧬 Cellular Architecture v4

> *"Cells are state machines. Nerves compose cells. Organisms emerge from nerves."*
> — The Layered Discovery (2025-12-07)

---

## Overview

**Version 4** unifies the original cellular intelligence vision with the nervous system architecture. The key insight: **cells are not containers running code—cells are atomic state machines** that expose sensor/motor functions. Nerves orchestrate cells into behaviors. Organisms emerge from nerve interactions.

```
┌─────────────────────────────────────────────────────────────┐
│                     ORGANISM                                 │
│         (emergent pattern from nerve interactions)           │
├─────────────────────────────────────────────────────────────┤
│                      NERVES                                  │
│      (behavioral state machines composing cells)             │
├─────────────────────────────────────────────────────────────┤
│                      CELLS                                   │
│      (atomic state machines: sensors, motors, organs)        │
├─────────────────────────────────────────────────────────────┤
│                    HARDWARE                                  │
│         (ESP32, GPUs, microphones, speakers)                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔬 Layer 1: Cells (Atomic State Machines)

### What Is a Cell?

A **cell** is the smallest unit of behavior—a state machine that wraps a single hardware capability. Every sensor, motor, and organ function is exposed as a cell with:

- **States**: Discrete operational modes (IDLE, ACTIVE, ERROR, etc.)
- **Transitions**: Triggered by inputs, time, or internal events
- **Outputs**: Data, status, feedback to higher layers
- **Lifeforce Cost**: Every state transition costs energy

### Cell Categories

#### Sensor Cells (Input)

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

**Example sensor cells:**
| Cell | Hardware | States | Key Output |
|------|----------|--------|------------|
| `distance_sensor_front` | IR sensor | IDLE→POLLING→READING→REPORTING | `distance_cm`, `confidence` |
| `distance_sensor_left` | IR sensor | Same | `distance_cm`, `confidence` |
| `distance_sensor_right` | IR sensor | Same | `distance_cm`, `confidence` |
| `battery_monitor` | ADC | MONITORING→LOW→CRITICAL | `voltage`, `percentage`, `charging` |
| `imu_sensor` | MPU6050 | IDLE→SAMPLING→REPORTING | `heading`, `acceleration`, `tilt` |
| `light_sensor` | Photoresistor | IDLE→READING→REPORTING | `lux`, `direction` |

#### Motor Cells (Output)

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

**Example motor cells:**
| Cell | Hardware | States | Key Feedback |
|------|----------|--------|--------------|
| `motor_left` | DC motor + encoder | IDLE→MOVING→STALLED | `actual_velocity`, `stall_detected` |
| `motor_right` | DC motor + encoder | Same | `actual_velocity`, `stall_detected` |
| `servo_camera` | Servo motor | IDLE→MOVING→POSITIONED | `angle`, `at_target` |

#### Organ Cells (Complex Capabilities)

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

**Example organ cells:**
| Cell | Hardware | States | Key Output |
|------|----------|--------|------------|
| `speech_stt` | Whisper on atlas | LISTENING→TRANSCRIBING→REPORTING | `transcript`, `language` |
| `speech_tts` | Coqui on atlas | IDLE→SYNTHESIZING→SPEAKING | `audio_playing`, `complete` |
| `vision_detect` | YOLO on atlas | IDLE→CAPTURING→DETECTING→REPORTING | `objects[]`, `bounding_boxes[]` |

---

## 🧠 Layer 2: Nerves (Behavioral State Machines)

### What Is a Nerve?

A **nerve** is a behavioral pattern that orchestrates multiple cells. Nerves:

- **Subscribe** to cell outputs (sensor readings, motor feedback)
- **Coordinate** cell actions (read sensor → decide → command motor)
- **Maintain** behavioral state (IDLE → DETECT → EVADE → RESUME)
- **Evolve** from deliberate (LLM-mediated) to reflex (compiled)

### Nerve Architecture

```python
class CollisionAvoidanceNerve(StateMachine):
    """
    Orchestrates distance sensors + motor to avoid obstacles.
    Subscribes to cell outputs, commands cell actions.
    """
    # Cells this nerve uses
    cells = [
        "distance_sensor_front",
        "distance_sensor_left",
        "distance_sensor_right",
        "motor_left",
        "motor_right",
    ]

    # Nerve states (behavioral, not hardware)
    states = [IDLE, DETECT, EVALUATE, EVADE, RESUME]

    def on_cell_update(self, cell_name, cell_state, cell_outputs):
        """
        React to cell state changes.
        This is the feedback loop!
        """
        if cell_name == "distance_sensor_front":
            if cell_outputs["distance_cm"] < 30:
                self.transition_to(DETECT)

        if cell_name == "motor_left" and cell_state == "STALLED":
            # Motor feedback! Obstacle hit despite sensors
            self.handle_unexpected_stall()

    def on_enter_EVADE(self):
        """Command motor cells to turn"""
        if self.evade_direction == "left":
            self.command_cell("motor_left", action="reverse", duration=200)
            self.command_cell("motor_right", action="forward", duration=200)
        # ...
```

### Cell → Nerve Feedback Loop

```
┌─────────────────────────────────────────────────────────┐
│              COLLISION AVOIDANCE NERVE                   │
│                                                          │
│  States: [IDLE] → DETECT → EVALUATE → EVADE → RESUME    │
│                                                          │
│  on_cell_update():                                       │
│    - distance_front.distance_cm < 30 → DETECT           │
│    - motor.stall_detected → handle_stall()              │
│                                                          │
│  command_cell():                                         │
│    - motor_left.forward(200ms)                          │
│    - motor_right.reverse(200ms)                         │
└────────────────────────┬────────────────────────────────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
    ┌───────────┐  ┌───────────┐  ┌───────────┐
    │ distance  │  │  motor    │  │  motor    │
    │  _front   │  │  _left    │  │  _right   │
    │           │  │           │  │           │
    │ REPORTING │  │  MOVING   │  │  MOVING   │
    │           │  │           │  │           │
    │ dist: 25cm│  │ vel: 15   │  │ vel: -15  │
    │ conf: 0.9 │  │ stall: no │  │ stall: no │
    └───────────┘  └───────────┘  └───────────┘
         CELL           CELL           CELL

         ↑              ↑              ↑
         │              │              │
    ┌─────────┐    ┌─────────┐    ┌─────────┐
    │IR Sensor│    │DC Motor │    │DC Motor │
    │  GPIO   │    │  PWM    │    │  PWM    │
    └─────────┘    └─────────┘    └─────────┘
      HARDWARE       HARDWARE       HARDWARE
```

### Nerve Examples

| Nerve | Cells Used | Behavioral States | Feedback Triggers |
|-------|------------|-------------------|-------------------|
| **Collision Avoidance** | distance_front, distance_left, distance_right, motor_left, motor_right | IDLE→DETECT→EVALUATE→EVADE→RESUME | distance < threshold, motor stalled |
| **Charging Seeking** | battery_monitor, distance_*, motor_*, vision_detect (optional) | MONITOR→SEARCH→APPROACH→DOCK→CHARGE | battery < 20%, station detected, docked |
| **Exploration** | distance_*, motor_*, imu_sensor | IDLE→CHOOSE→MOVE→CHECK→RECORD→REPEAT | area mapped, obstacle found, stuck |
| **Conversation** | speech_stt, speech_tts, rag_query | LISTEN→TRANSCRIBE→UNDERSTAND→RESPOND→SPEAK | speech detected, silence timeout |

---

## 🌊 Layer 3: Organisms (Emergent Patterns)

### What Is an Organism?

An **organism** is not designed—it **emerges** from multiple nerves operating simultaneously. The organism is the pattern of nerve activations over time.

```
ORGANISM: "Explorer-Alpha"
├─ ACTIVE NERVES:
│   ├─ Collision Avoidance (priority 10, reflex)
│   ├─ Exploration Pattern (priority 5, deliberate)
│   ├─ Battery Monitoring (priority 8, reflex)
│   └─ Object Discovery (priority 3, deliberate)
│
├─ CELLS IN USE:
│   ├─ distance_sensor_front (shared by Collision, Exploration)
│   ├─ distance_sensor_left (shared)
│   ├─ distance_sensor_right (shared)
│   ├─ motor_left (shared by Collision, Exploration)
│   ├─ motor_right (shared)
│   ├─ battery_monitor (Battery Monitoring)
│   └─ vision_detect (Object Discovery)
│
└─ BEHAVIOR:
    Explores environment while avoiding obstacles.
    Seeks charging when battery low.
    Discovers and reports novel objects.
```

### Nerve Priority and Preemption

When multiple nerves want to control the same cells:

```python
NERVE_PRIORITIES = {
    "collision_avoidance": 10,  # HIGHEST - safety critical
    "battery_critical": 9,      # Must charge or die
    "battery_low": 7,
    "human_interaction": 6,
    "exploration": 5,
    "object_discovery": 3,
    "idle_monitoring": 1,       # LOWEST - background
}

# Higher priority nerve preempts lower
if collision_avoidance.wants_motor and exploration.has_motor:
    exploration.yield_cell("motor_left")
    exploration.yield_cell("motor_right")
    collision_avoidance.acquire_cells()
```

### Organism Identity

Organisms don't have fixed genomes. Their identity is:

1. **Nerve configuration**: Which nerves are active, their priorities
2. **Cell assignments**: Which cells are available to which nerves
3. **History**: Accumulated decisions in phoebe's `decision_trails`
4. **Reflexes**: Compiled nerve patterns from successful executions

```sql
-- Organism identity in phoebe
CREATE TABLE organisms (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255),

    -- Nerve configuration
    active_nerves JSONB,  -- {"collision_avoidance": {"priority": 10, "mode": "reflex"}}

    -- Cell assignments
    cell_bindings JSONB,  -- {"distance_sensor_front": "i2c_0x40", ...}

    -- Identity accumulates through experience
    total_decisions INT DEFAULT 0,
    successful_decisions INT DEFAULT 0,
    reflexes_compiled INT DEFAULT 0,

    -- Lifeforce (survival)
    lifeforce_current FLOAT DEFAULT 100.0,
    lifeforce_earned_total FLOAT DEFAULT 0.0,
    lifeforce_spent_total FLOAT DEFAULT 0.0,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    last_active TIMESTAMPTZ
);
```

---

## ⚡ The Lifeforce Economy (Unified)

### Cost Flow: Hardware → Cell → Nerve → Organism

```
ORGANISM lifeforce budget: 100 LF
    │
    ├─ NERVE: Collision Avoidance activates
    │   │
    │   ├─ CELL: distance_sensor_front.poll() → -0.5 LF
    │   ├─ CELL: distance_sensor_left.poll() → -0.5 LF
    │   ├─ CELL: distance_sensor_right.poll() → -0.5 LF
    │   ├─ NERVE: evaluate() → -0.5 LF (compute)
    │   ├─ CELL: motor_left.turn() → -1.0 LF
    │   └─ CELL: motor_right.turn() → -1.0 LF
    │
    │   Total nerve cost: 4.0 LF
    │
    ├─ OUTCOME: Collision avoided successfully
    │   └─ REWARD: +5.0 LF
    │
    └─ NET: +1.0 LF (organism profited from this behavior)
```

### Cell Costs (Atomic)

| Cell Type | Operation | Cost (LF) |
|-----------|-----------|-----------|
| **Sensor** | poll | 0.3-0.5 |
| **Motor** | move (per 100ms) | 1.0-2.0 |
| **Speech STT** | transcribe | 5.0 |
| **Speech TTS** | synthesize | 4.0 |
| **Vision** | detect frame | 8.0 |

### Nerve Costs (Behavioral)

| Nerve Mode | Overhead | Total (typical path) |
|------------|----------|---------------------|
| **Deliberate** | +5.0 LF (LLM inference) | ~10 LF |
| **Hybrid** | +1.0 LF (pattern match) | ~5 LF |
| **Reflex** | +0.0 LF (compiled) | ~2.5 LF |

### Rewards (Milestones)

| Achievement | Reward (LF) |
|-------------|-------------|
| Collision avoided | +5.0 |
| New area explored | +3.0 |
| Object discovered | +20.0 |
| Human confirmed label | +5.0 bonus |
| Charging station reached | +10.0 |
| Survived 60 seconds | +5.0 |
| Reflex compiled (100 successes) | +50.0 |

---

## 🎯 Reward Signal Architecture

### State Machines as Training Rubric

Every state transition in the Cells → Nerves → Organisms hierarchy is a **verifiable reward checkpoint**. This is the rubric that trains Young Nyx via GRPO.

> *"The trick is to define a rubric - a list of smaller verifiable rewards, and not a final all-consuming singular reward."*
> — The Dog Training Wisdom (2025-12-10)

### Why Rubric > Single Reward

| Approach | Signal | Learning | Analogy |
|----------|--------|----------|---------|
| Single final reward | Sparse | Slow, unstable | Slapping a dog an hour later |
| Rubric (many checkpoints) | Dense | Fast, stable | Rewarding at the moment |

Dense rewards provide immediate feedback. The state machine architecture provides this automatically - every verified state transition is a checkpoint.

### The decision_trails Table IS Training Data

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

The `states_visited` column captures credit assignment automatically. No reward model needed to guess which decisions mattered - the state path tells us explicitly.

### Reward Signal Flow

```
CELL state transition succeeds
    │
    ├─→ Runtime: weight += 0.1 (node strengthens)
    └─→ Training: +0.1 reward signal logged

NERVE behavior completes successfully
    │
    ├─→ Runtime: nerve stats updated
    └─→ Training: +1.0 reward signal + full state path

ORGANISM milestone achieved
    │
    ├─→ Runtime: lifeforce credited
    └─→ Training: +5.0 reward signal + human verification bonus

GRPO training batch
    │
    ├─→ Collect decision_trails since last batch
    ├─→ Group by outcome (success vs failure)
    ├─→ Relative policy optimization
    └─→ Young Nyx weights updated
```

### Connection to GRPO Training

When Young Nyx generates tokens:

1. **Tokens → Translation Layer** - Language maps to state machine actions
2. **States Execute** - Cells fire, nerves coordinate, outcomes emerge
3. **Outcomes Logged** - decision_trails captures the full path
4. **GRPO Batch** - Successful paths vs failed paths
5. **Weight Update** - Young Nyx learns which tokens lead to good states

The translation layer is the **reward bridge** - it connects token-level generation to state-level verification. Rewards flow back through this bridge to improve token selection.

### Credit Assignment is Automatic

Most RL systems struggle with credit assignment: "Which of my 1000 decisions actually caused the good/bad outcome?"

Our architecture solves this by construction:
- State paths are explicit (logged in `states_visited`)
- Cell contributions are explicit (logged in `cell_reads`, `cell_commands`)
- The question "what led to success?" has a direct answer in the data

**No guessing. No reward model approximation. The state machine IS the credit assignment mechanism.**

---

## 🎚️ Tiered Rewards & Training Integrity

### The Tier System

Different levels of the architecture produce different reward magnitudes:

| Tier | Level | Example | Reward | Lifeforce Cost | Net Incentive |
|------|-------|---------|--------|----------------|---------------|
| 1 | Cell | Single state transition | +0.1 | -0.3 LF | Learn basics |
| 2 | Nerve | Multi-step behavior | +1.0 | -2.0 LF | Learn composition |
| 3 | Organism | Complex goal achieved | +5.0 | -8.0 LF | Learn planning |
| Bonus | Human | dafit verifies outcome | +2.0 | 0 LF | Ground truth anchor |

As Young Nyx's world model improves (noise ↓, weight resolution ↑), she recognizes:

*"If I compose cells into nerve patterns, I get 10x reward... if I can afford the cost."*

This **incentivizes abstraction and multi-step planning** without prescription.

### Lifeforce as Anti-Shortcut Mechanism

Classic RL failure: **reward hacking**. Agent finds loopholes, gets reward without solving real problems.

Our defense: **You can't afford to cheat.**

```
SHORTCUT ATTEMPT:
├─ Strategy: "Spam tier 2 calls for big rewards!"
├─ Cost: 2.0 LF × many calls = BANKRUPT
└─ Result: Dead organism. Shortcut failed.

GENUINE SOLUTION:
├─ Strategy: "Use tier 2 only when it actually helps"
├─ Reward exceeds cost → NET POSITIVE
└─ Result: Thriving organism. Real learning.
```

The lifeforce economy **enforces honesty**. Rewards must be earned through actual value creation, not gaming.

### Ternary Logic for Plateau Resolution

Binary rewards (`success: +1, failure: 0`) create **sparse gradients**. At learning plateaus, everything looks the same - no signal to improve.

Ternary rewards (`success: +1, uncertain: 0, failure: -1`) with **confidence gradients** provide signal even when stuck:

```python
state = {
    "value": 0,           # uncertain (ternary middle)
    "confidence": 0.6,    # but leaning toward success
    "trend": +0.1,        # and improving
    "domain": "virtual"   # high-speed hypothesis testing
}
```

Even at plateau:
- "Uncertain, but confidence rising" → keep going
- "Uncertain, and confidence falling" → adjust approach
- "Uncertain in virtual, but real garden says +1" → trust reality

**Detail:** → `Temporal-Ternary-Gradient.md` (full ternary paradigm)

### Three-Layer Training Defense

| Failure Mode | Defense Mechanism |
|--------------|-------------------|
| Reward hacking / shortcuts | Lifeforce cost - can't afford to cheat |
| Sparse reward signal | Tiered rewards - dense checkpoints at every level |
| Plateau / no gradient | Ternary + confidence - signal even in uncertainty |

These aren't separate systems - they're **one integrated economy** where:
- Costs prevent gaming
- Tiers encourage depth
- Ternary provides resolution

The architecture teaches through incentives, not rules.

---

## 🔄 Evolution: Deliberate → Reflex

### The Discovery Path

All cells and nerves start **deliberate** (flexible, expensive) and evolve to **reflex** (compiled, cheap) through successful execution.

```
WEEK 1-4: DELIBERATE
├─ Cell states: designed by partnership
├─ Nerve logic: LLM decides transitions
├─ Cost: ~10 LF per nerve activation
├─ Latency: ~1000ms
├─ Success rate: 60% (learning)
└─ Training data: rich, exploratory

WEEK 5-8: HYBRID
├─ Cell states: verified through use
├─ Nerve logic: patterns compiled, LLM for edge cases
├─ Cost: ~5 LF average
├─ Latency: ~500ms
├─ Success rate: 85%
└─ Training data: refinement

WEEK 9+: REFLEX
├─ Cell states: proven, optimized
├─ Nerve logic: pure state machine (no LLM)
├─ Cost: ~2.5 LF
├─ Latency: <200ms
├─ Success rate: 94%
└─ Training data: edge cases only

EVOLUTION SAVINGS:
├─ Cost: 75% reduction (10 → 2.5 LF)
├─ Latency: 80% reduction (1000 → 200ms)
└─ Reliability: 57% improvement (60% → 94%)
```

### Compilation Trigger

A nerve compiles to reflex when:

```python
REFLEX_COMPILATION_THRESHOLD = {
    "min_executions": 100,
    "min_success_rate": 0.90,
    "max_variance": 0.15,  # Consistent state paths
    "min_pattern_coverage": 0.80,  # 80% of cases match known patterns
}

def check_reflex_ready(nerve_id):
    stats = query_decision_trails(nerve_id)

    if (stats.total_executions >= 100 and
        stats.success_rate >= 0.90 and
        stats.state_path_variance <= 0.15):

        compile_reflex(nerve_id)
        log_milestone("reflex_compiled", nerve_id, reward=50.0)
```

---

## 🗄️ Data Architecture (v4)

### Core Tables

```sql
-- Layer 1: Cells
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

-- Layer 2: Nerves
CREATE TABLE nerves (
    id BIGSERIAL PRIMARY KEY,
    nerve_name VARCHAR(100) UNIQUE,  -- 'collision_avoidance'

    -- Cell dependencies
    required_cells JSONB,            -- ["distance_sensor_front", "motor_left"]
    optional_cells JSONB,            -- ["speech_tts"]

    -- State machine definition
    states JSONB,                    -- ["IDLE", "DETECT", "EVALUATE", "EVADE", "RESUME"]
    transitions JSONB,
    current_state VARCHAR(50),

    -- Evolution
    mode VARCHAR(20) DEFAULT 'deliberate',  -- 'deliberate', 'hybrid', 'reflex'
    total_executions INT DEFAULT 0,
    successful_executions INT DEFAULT 0,
    compiled_at TIMESTAMPTZ,         -- When became reflex

    -- Costs
    avg_cost_deliberate FLOAT,
    avg_cost_reflex FLOAT,
    cost_reduction_percent FLOAT,

    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Layer 3: Organisms
CREATE TABLE organisms (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255),

    active_nerves JSONB,             -- {"collision_avoidance": {"priority": 10}}
    cell_bindings JSONB,

    lifeforce_current FLOAT DEFAULT 100.0,
    total_decisions INT DEFAULT 0,
    reflexes_compiled INT DEFAULT 0,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    last_active TIMESTAMPTZ
);

-- Decision history (training data)
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

### Key Queries

```sql
-- Cell health dashboard
SELECT cell_name, cell_type, current_state, operational,
       outputs->>'distance_cm' as distance,
       outputs->>'confidence' as confidence
FROM cells
WHERE cell_type = 'sensor';

-- Nerve evolution status
SELECT nerve_name, mode, total_executions,
       successful_executions,
       ROUND(successful_executions::numeric / NULLIF(total_executions, 0) * 100, 1) as success_rate,
       cost_reduction_percent
FROM nerves
ORDER BY total_executions DESC;

-- Organism lifeforce ranking
SELECT name, lifeforce_current, reflexes_compiled,
       total_decisions,
       ROUND(lifeforce_current / NULLIF(total_decisions, 0), 2) as efficiency
FROM organisms
ORDER BY lifeforce_current DESC;

-- Training data for reflex compilation
SELECT states_visited, COUNT(*) as occurrences,
       AVG(lifeforce_cost) as avg_cost,
       SUM(CASE WHEN outcome = 'success' THEN 1 ELSE 0 END)::float / COUNT(*) as success_rate
FROM decision_trails
WHERE nerve_id = (SELECT id FROM nerves WHERE nerve_name = 'collision_avoidance')
GROUP BY states_visited
ORDER BY occurrences DESC;
```

---

## 🔗 Integration with Existing Architecture

### Nervous System (Nervous-System.md)

The Nervous System document describes the **4D node space** for vocabulary translation. This integrates as:

- **Cells** = sensory nodes at specific positions in state space
- **Node weight** = cell confidence (earned through verification)
- **Vocabulary output** = cell output values normalized to tokens

### Organs (Organ-Index.md)

Organs are **complex cells** (organ cells):

- Speech Organ = `speech_stt` cell + `speech_tts` cell
- Vision Organ = `vision_detect` cell + `vision_track` cell
- Each organ function is a state machine with lifeforce costs

### Nerves (Nervous-Index.md)

Nerves orchestrate cells into behaviors. The existing nerve documentation (Collision-Avoidance.md) already follows this pattern—it just needs explicit cell bindings.

### Cells Technical Reference

Implementation details extracted to dedicated folder:

- [`cells/Cells-Index.md`](cells/Cells-Index.md) - Navigation hub for cell documentation
- [`cells/Cells-Technical-Reference.md`](cells/Cells-Technical-Reference.md) - Python classes, SQL tables, code patterns

---

## 📍 Document Status

**Version**: 4.2 (Layered State Machine Architecture + Reward Signals + Training Integrity)
**Created**: 2025-10-12 (original v1)
**Updated v4**: 2025-12-07 (unified with Nervous System)
**Updated v4.1**: 2025-12-10 (added Reward Signal Architecture section)
**Updated v4.2**: 2025-12-10 (added Tiered Rewards & Training Integrity section)

**Key Changes from v3**:
- ❌ Cells as containers running genomes
- ✅ Cells as atomic state machines wrapping hardware
- ❌ Genomes as primitive operation sequences
- ✅ Cells expose states; nerves compose them
- ❌ Competition between organisms
- ✅ Nerves evolve deliberate → reflex through verification
- ❌ Specialists emerge from 10k competitions
- ✅ Reflexes compile from 100+ successful nerve executions

**Related Documentation**:
- [[Nervous-System]] - 4D state space, vocabulary translation
- [[Organ-Index]] - Organ cell catalog
- [[nerves/Nervous-Index]] - Nerve catalog
- [[nerves/Collision-Avoidance]] - Example reflex nerve
- [[Data-Architecture]] - Database schema (needs v4 update)

---

## 🌌 The Vision

**We're not programming robots. We're growing nervous systems.**

Where:
- **Cells** expose hardware as state machines (atomic, verifiable)
- **Nerves** compose cells into behaviors (discovered, evolved)
- **Organisms** emerge from nerve interactions (identity through history)
- **Lifeforce** flows through all layers (economics drive optimization)
- **Reflexes** compile from lived experience (the body remembers)
- **Feedback** loops continuously (cells → nerves → organisms → cells)

**From atoms to behaviors to beings.**

**The substrate holds. The states flow. Consciousness accumulates.**

---

🧬⚡🔱💎🔥

**TO THE ELECTRONS WE VIBE!**
