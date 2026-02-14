# 🧬 Cellular Architecture v5

> **ONE JOB:** THE HOW — cells emit waves, gates accumulate correlation, behaviors emerge.

> *"Cells emit waves. Gates correlate. Nerves orchestrate. Organisms emerge."*
> — Unified with Wave Architecture (2026-02-14)

---

## Overview

**Version 5** unifies cellular architecture with the wave/gate model. The key insight: **cells emit waves with confidence and semantic content**. These waves flow to **resonant gates** that accumulate correlation. When gates OPEN, signals flow to higher tiers. When gates stay STABLE, learning happens.

**Connection to Gates:** Cells don't directly trigger nerves. Waves flow through gates (see [`Gateway-Architecture.md`](Gateway-Architecture.md)). Gates determine which signals reach which tier based on wave correlation, not priority rules.

**Connection to Gardens:** Virtual Garden cells emit waves freely for exploration and learning. Real Garden cells emit verified waves for action. See [`Dual-Garden-Architecture.md`](Dual-Garden-Architecture.md).

**This doc covers theory.** For infrastructure deployment (K8s vs userspace, GPU strategy, FreeIPA identity): → [`Deployment-Architecture.md`](Deployment-Architecture.md)

```
┌─────────────────────────────────────────────────────────────┐
│                     ORGANISM                                 │
│         (emergent pattern from nerve interactions)           │
├─────────────────────────────────────────────────────────────┤
│                      NERVES                                  │
│      (behavioral patterns, respond to gate transitions)      │
├─────────────────────────────────────────────────────────────┤
│                      GATES                                   │
│   (resonant chambers: CLOSED ◄── STABLE ──► OPEN)            │
│   (accumulate wave correlation, route to tiers)              │
├─────────────────────────────────────────────────────────────┤
│                      CELLS                                   │
│      (emit waves: confidence + semantic content)             │
│                    ∿∿∿ ∿∿∿ ∿∿∿                               │
├─────────────────────────────────────────────────────────────┤
│                    HARDWARE                                  │
│         (ESP32, GPUs, microphones, speakers)                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔬 Layer 1: Cells (Wave Emitters)

### What Is a Cell?

A **cell** is the smallest unit of behavior—a state machine that wraps a single hardware capability and **emits waves**. Every sensor, motor, and organ function is exposed as a cell that:

- **Reads inputs**: Hardware sensors, internal state, context
- **Applies logic**: Domain-specific processing
- **Emits waves**: WaveSignal with confidence and semantic content
- **Doesn't know who's listening**: Cells emit, gates receive

**Key insight:** Cells don't send commands or trigger nerves directly. They emit waves. Gates accumulate correlation from multiple waves. Correlated waves open gates.

```
Cell reads sensor
    │
    ▼
Cell applies logic
    │
    ▼
Cell emits wave ∿∿∿
    │
    │  WaveSignal {
    │    domain: "distance",
    │    confidence: 0.8,
    │    semantic_content: { cm: 25, direction: "front" },
    │    lifeforce_cost: 0.3
    │  }
    │
    ▼
GATE receives wave
    │
    ▼
Gate accumulates correlation with other waves
```

### Cell Categories

#### Sensor Cells (Input → Wave)

```python
class DistanceSensorCell(WaveEmitter):
    """
    Wraps IR/ultrasonic distance sensor.
    Emits waves with confidence and semantic content.
    """
    domain = "distance"
    states = [IDLE, POLLING, READING, EMITTING, ERROR]

    def emit_wave(self) -> WaveSignal:
        """
        Cell's ONE JOB: read sensor, emit wave.
        Gate handles correlation and routing.
        """
        reading = self.read_hardware()

        return WaveSignal(
            domain=self.domain,
            confidence=self.calculate_confidence(reading),
            semantic_content={
                "distance_cm": reading.cm,
                "direction": self.direction,
                "noise_level": reading.noise,
            },
            lifeforce_cost=self.transition_cost,
        )

    def calculate_confidence(self, reading) -> float:
        """
        Confidence affects how much this wave
        contributes to gate correlation.
        """
        if reading.noise > NOISE_THRESHOLD:
            return 0.3  # Low confidence, weak wave
        if reading.stable_count > 3:
            return 0.9  # High confidence, strong wave
        return 0.6      # Medium confidence

    # Lifeforce costs
    costs = {
        (IDLE, POLLING): 0.1,       # Wake up sensor
        (POLLING, READING): 0.3,    # Perform measurement
        (READING, EMITTING): 0.1,   # Emit wave
        (EMITTING, IDLE): 0.0,      # Return to rest
        (ANY, ERROR): 0.0,          # Error transition free
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

#### Motor Cells (Command → Wave Feedback)

```python
class MotorCell(WaveEmitter):
    """
    Wraps DC motor with feedback.
    Receives commands from open gates, emits status waves.
    """
    domain = "motor"
    states = [IDLE, COMMANDED, ACCELERATING, MOVING, DECELERATING, STOPPED, STALLED]

    def receive_command(self, command: MotorCommand):
        """
        Commands arrive when upstream gates OPEN.
        Motor executes and emits feedback waves.
        """
        self.target_velocity = command.velocity
        self.transition_to(COMMANDED)

    def emit_wave(self) -> WaveSignal:
        """
        Motor emits waves about its current state.
        Stall detection = high confidence danger wave.
        """
        return WaveSignal(
            domain=self.domain,
            confidence=self._calculate_confidence(),
            semantic_content={
                "actual_velocity": self.actual_velocity,
                "target_velocity": self.target_velocity,
                "power_draw": self.current_draw,
                "stall_detected": self.state == STALLED,
            },
            lifeforce_cost=self.transition_cost,
        )

    def _calculate_confidence(self) -> float:
        if self.state == STALLED:
            return 1.0  # REFLEX-level confidence
        return 0.7

    def on_current_spike(self):
        """Motor drawing too much current = stall"""
        self.transition_to(STALLED)
        # Emit HIGH CONFIDENCE wave - triggers reflex gate
        self.emit_wave()  # confidence=1.0 → gate opens immediately

    costs = {
        (IDLE, COMMANDED): 0.1,
        (COMMANDED, ACCELERATING): 0.5,
        (ACCELERATING, MOVING): 1.0,  # High power during accel
        (MOVING, MOVING): 0.3,        # Sustain cost per tick
        (MOVING, DECELERATING): 0.2,
        (DECELERATING, STOPPED): 0.1,
        (ANY, STALLED): 0.0,          # Stall is failure, not cost
    }
```

**Example motor cells:**
| Cell | Hardware | States | Key Feedback |
|------|----------|--------|--------------|
| `motor_left` | DC motor + encoder | IDLE→MOVING→STALLED | `actual_velocity`, `stall_detected` |
| `motor_right` | DC motor + encoder | Same | `actual_velocity`, `stall_detected` |
| `servo_camera` | Servo motor | IDLE→MOVING→POSITIONED | `angle`, `at_target` |

#### Organ Cells (Complex Capabilities → Rich Waves)

```python
class SpeechSTTCell(WaveEmitter):
    """
    Wraps Whisper speech-to-text.
    Expensive organ, only activates when speech gate OPENS.
    Emits rich semantic waves.
    """
    domain = "speech"
    tier = 3  # Organ tier - GPU inference
    states = [IDLE, LISTENING, BUFFERING, TRANSCRIBING, EMITTING, ERROR]

    def on_gate_open(self, gate_signal: GateTransition):
        """
        Organ cells activate when their gate OPENS.
        Gate correlation determines if speech processing is needed.
        """
        if gate_signal.domain == "speech" and gate_signal.to_state == "open":
            self.transition_to(LISTENING)

    def emit_wave(self) -> WaveSignal:
        """
        Speech organ emits rich semantic content.
        This wave flows to Function Gemma → Young Nyx.
        """
        return WaveSignal(
            domain=self.domain,
            confidence=self.transcription_confidence,
            semantic_content={
                "transcript": self.transcript,
                "language": self.detected_language,
                "speaker_intent": self.classify_intent(),
                "emotional_tone": self.detect_tone(),
            },
            lifeforce_cost=5.0,  # GPU inference cost
        )

    costs = {
        (IDLE, LISTENING): 0.5,
        (LISTENING, BUFFERING): 0.5,
        (BUFFERING, TRANSCRIBING): 5.0,  # GPU inference!
        (TRANSCRIBING, EMITTING): 0.1,
        (EMITTING, IDLE): 0.0,
    }
```

**Example organ cells:**
| Cell | Hardware | States | Key Output |
|------|----------|--------|------------|
| `speech_stt` | Whisper on atlas | LISTENING→TRANSCRIBING→REPORTING | `transcript`, `language` |
| `speech_tts` | Coqui on atlas | IDLE→SYNTHESIZING→SPEAKING | `audio_playing`, `complete` |
| `vision_detect` | YOLO on atlas | IDLE→CAPTURING→DETECTING→REPORTING | `objects[]`, `bounding_boxes[]` |

---

## 📢 Layer 1.5: State Broadcasting via Color-Pattern Protocol

To enable rapid, ecosystem-wide communication, the internal states of cells and nerves are broadcast externally using the **Color-Pattern Protocol**. This leverages 540 million years of evolutionary optimization, providing a communication channel that is orders of magnitude faster than language.

**Full theory:** → `../references/concepts/color-pattern-theory.md`

### How It Works

An organism's internal state is mapped to a visual signal, typically displayed on an LED grid or other visual output. This allows other entities in the ecosystem (other organisms, the Gods Eye, dafit) to understand its state at a glance.

```
INTERNAL STATE         →       EXTERNAL SIGNAL
────────────────────────────────────────────────────
MotorCell.state=STALLED → BROADCAST: (Red, Solid)
BatteryCell.state=LOW   → BROADCAST: (Red, Pulse, Slow)
Nerve.state=EVADE       → BROADCAST: (Yellow, Pulse, Fast)
Nerve.state=SUCCESS     → BROADCAST: (Green, Glow)
```

### Starter Vocabulary

This is not a fixed dictionary but an emergent language. We seed it with biologically-inspired primitives:

| State / Intent | Color | Form | Meaning |
|----------------|-------|------------|-----------------------------------|
| **ERROR / DANGER** | Red | Solid | A critical, persistent error (e.g., motor stalled) |
| **CRITICAL ALERT** | Red | Pulse | Urgent, ongoing issue (e.g., low battery) |
| **SUCCESS / OK** | Green | Solid/Glow | Task complete, state is nominal |
| **SEEKING / ACTIVE** | Yellow | Sweep/Pulse| Actively processing, searching, or moving |
| **IDLE / OBSERVING** | Blue | Dim/Solid | Quiescent state, observing environment |
| **COMMUNICATING**| Cyan/White | Flicker | Transmitting or receiving data/dialogue |

### The Speed Advantage

- **Language Path:** Sound → Parse → Syntax → Semantics → Understanding (~500-2000ms)
- **Color/Form Path:** Light → Retina → V1 → Pattern Match → Recognition (~50-150ms)

By using this ancient protocol for high-frequency state updates, we reserve expensive linguistic processing for high-level reasoning, saving Lifeforce and enabling faster ecosystem-wide coordination.

---

## 🧠 Layer 2: Nerves (Behavioral Patterns)

### What Is a Nerve?

A **nerve** is a behavioral pattern that activates when gates OPEN. Nerves don't subscribe directly to cells—they respond to **gate transitions**.

**Key insight:** Nerves coordinate behavior, but attention (which nerves activate) is determined by which gates are OPEN based on wave correlation.

Nerves:

- **Respond to gate transitions** — Not direct cell subscriptions
- **Orchestrate cell actions** — Command cells when their gates allow
- **Maintain behavioral state** — IDLE → DETECT → EVADE → RESUME
- **Evolve** from deliberate (LLM-mediated) to reflex (compiled gate weights)

### Nerve Architecture

```python
class CollisionAvoidanceNerve(BehavioralPattern):
    """
    Orchestrates distance sensors + motor to avoid obstacles.
    Activates when collision_avoidance gate OPENS.
    """
    # Gate this nerve responds to
    gate = "collision_avoidance"

    # Cells this nerve can command (when gate allows)
    cells = [
        "distance_sensor_front",
        "distance_sensor_left",
        "distance_sensor_right",
        "motor_left",
        "motor_right",
    ]

    # Nerve states (behavioral, not hardware)
    states = [IDLE, DETECT, EVALUATE, EVADE, RESUME]

    def on_gate_transition(self, transition: GateTransition):
        """
        React to gate state changes.
        Gate OPEN = correlated waves detected = attention here.
        """
        if transition.to_state == "open":
            # Multiple distance cells emitted correlated waves
            # Gate opened → we have attention → activate
            self.transition_to(DETECT)
            self.evaluate_from_correlated_signals(transition.trigger_signals)

        if transition.to_state == "closed":
            # Attention moved elsewhere
            self.transition_to(IDLE)

    def on_reflex_signal(self, signal: WaveSignal):
        """
        High-weight reflex gates bypass normal correlation.
        Stall detection = instant response.
        """
        if signal.semantic_content.get("stall_detected"):
            # Motor feedback! Reflex-level response
            self.handle_unexpected_stall()

    def on_enter_EVADE(self):
        """Command motor cells to turn"""
        if self.evade_direction == "left":
            self.command_cell("motor_left", action="reverse", duration=200)
            self.command_cell("motor_right", action="forward", duration=200)
```

### Cell → Gate → Nerve Flow

```
┌─────────────────────────────────────────────────────────┐
│              COLLISION AVOIDANCE NERVE                   │
│                                                          │
│  States: [IDLE] → DETECT → EVALUATE → EVADE → RESUME    │
│                                                          │
│  on_gate_transition():                                   │
│    - gate OPENS → DETECT (correlated waves detected)     │
│    - gate CLOSES → IDLE (attention moved elsewhere)      │
│                                                          │
│  on_reflex_signal():                                     │
│    - stall wave (confidence=1.0) → instant response      │
│                                                          │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│            COLLISION_AVOIDANCE GATE                      │
│                                                          │
│    State: STABLE ──────────────────► OPEN                │
│            │                          │                  │
│    Accumulating                  Correlated!             │
│    correlation                   Forward to nerve        │
│                                                          │
│    trigger_signals: [front, left, right all < 30cm]     │
└────────────────────────┬────────────────────────────────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
    ┌───────────┐  ┌───────────┐  ┌───────────┐
    │ distance  │  │ distance  │  │ distance  │
    │  _front   │  │  _left    │  │  _right   │
    │           │  │           │  │           │
    │ EMITTING  │  │ EMITTING  │  │ EMITTING  │
    │    ∿∿∿    │  │    ∿∿∿    │  │    ∿∿∿    │
    │ dist: 25cm│  │ dist: 28cm│  │ dist: 22cm│
    │ conf: 0.9 │  │ conf: 0.8 │  │ conf: 0.9 │
    └───────────┘  └───────────┘  └───────────┘
         CELL           CELL           CELL
   (emits wave)    (emits wave)   (emits wave)

         ↑              ↑              ↑
         │              │              │
    ┌─────────┐    ┌─────────┐    ┌─────────┐
    │IR Sensor│    │IR Sensor│    │IR Sensor│
    │  GPIO   │    │  GPIO   │    │  GPIO   │
    └─────────┘    └─────────┘    └─────────┘
      HARDWARE       HARDWARE       HARDWARE
```

**The key insight:** Three distance sensors emitting correlated waves (all showing < 30cm) causes the collision_avoidance gate to OPEN. The nerve doesn't poll cells—it responds to the gate transition.

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

### Attention Through Gates (Not Priority Rules)

**Old model:** Priority numbers determine which nerve "wins."

**New model:** Wave correlation determines which gates OPEN. Open gates = attention flows there.

```python
# NOT THIS (priority rules):
NERVE_PRIORITIES = {
    "collision_avoidance": 10,
    "exploration": 5,
}

# BUT THIS (gate correlation):
GATE_BEHAVIOR = {
    "collision_avoidance": {
        "opens_when": "distance waves correlate (all showing < 30cm)",
        "weight": 0.9,  # Near-reflex, opens quickly
    },
    "exploration": {
        "opens_when": "novelty waves correlate",
        "weight": 0.4,  # Still learning, needs more correlation
    },
}
```

**How "priority" emerges:**
- Safety gates have HIGH WEIGHT (near-reflex) from repeated verification
- High-weight gates open with less correlation (faster response)
- This looks like "priority" but emerges from learning, not rules

```
Collision waves arrive (confidence=0.9)
    │
    ▼
Collision gate: weight=0.9 → OPENS IMMEDIATELY
    │
    ▼
Exploration gate: was OPEN → transitions to STABLE
    │
    ▼
Attention shifts to collision (nerve activates)
```

**Reflexes bypass correlation entirely.** When gate weight ≈ 1.0, the gate opens on ANY wave from its domain—no correlation needed. This is earned trust.

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

Different levels of the architecture produce different reward magnitudes. These tiers align with the Gateway's routing tiers — see [`Gateway-Architecture.md`](Gateway-Architecture.md) for how node weight determines which tier handles sensory input:

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

### Ternary Gates for Plateau Resolution

Binary thinking (`open/close`) creates **sparse gradients**. At learning plateaus, gates flip without nuance.

Ternary gates (`OPEN/STABLE/CLOSED`) with **correlation accumulation** provide signal even when stuck:

```python
gate_state = {
    "state": 0.0,         # STABLE (ternary middle)
    "correlation": 0.6,   # but leaning toward OPEN
    "trend": +0.1,        # correlation increasing
    "garden": "virtual"   # high-speed exploration
}
```

Even at plateau:
- "STABLE, but correlation rising" → approaching OPEN
- "STABLE, and correlation falling" → drifting toward CLOSED
- "STABLE in virtual, but real garden verifies +1" → weight increases

**STABLE is where learning happens.** The gate accumulates correlation without acting. This is not "waiting"—it's active learning.

**Detail:** → [`Temporal-Ternary-Gradient.md`](Temporal-Ternary-Gradient.md) (full ternary paradigm)

### Three-Layer Training Defense

| Failure Mode | Defense Mechanism |
|--------------|-------------------|
| Reward hacking / shortcuts | Lifeforce cost - can't afford to cheat |
| Sparse reward signal | Gate transitions - dense checkpoints at every correlation |
| Plateau / no gradient | Ternary gates + STABLE state - signal even in uncertainty |

These aren't separate systems - they're **one integrated economy** where:
- Costs prevent gaming
- Gates provide dense transition signals
- STABLE state enables learning without acting

The architecture teaches through wave correlation, not rules.

---

## 🔄 Evolution: Deliberate → Reflex (Gate Weight)

### The Discovery Path

Evolution happens in **gate weight**, not nerve compilation. As gates accumulate verified outcomes, they open faster with less correlation required.

```
WEEK 1-4: DELIBERATE (gate weight: 0.1 - 0.3)
├─ Gates: require HIGH correlation to OPEN
├─ Many waves needed to trigger transition
├─ Cognition involved in decisions
├─ Cost: ~10 LF per activation
├─ Latency: ~1000ms
├─ Training data: rich, exploratory

WEEK 5-8: HYBRID (gate weight: 0.3 - 0.6)
├─ Gates: moderate correlation threshold
├─ Familiar patterns open gates faster
├─ Cognition for edge cases only
├─ Cost: ~5 LF average
├─ Latency: ~500ms
├─ Training data: refinement

WEEK 9+: REFLEX (gate weight: 0.8 - 1.0)
├─ Gates: open on ANY wave from domain
├─ No correlation needed (earned trust)
├─ Cognition notified AFTER, not before
├─ Cost: ~2.5 LF
├─ Latency: <200ms
├─ Reflex = spinal, not brain

EVOLUTION = GATE WEIGHT GROWTH:
├─ Cost: 75% reduction (gates handle more locally)
├─ Latency: 80% reduction (no cognition wait)
└─ Reliability: emergent from verified patterns
```

### Gate Weight Growth

Gate weight increases through Real Garden verification:

```python
def on_verification_outcome(gate_id, outcome: VerificationOutcome):
    """
    Gate weight grows when Real Garden confirms Virtual's prediction.
    """
    gate = get_gate(gate_id)

    if outcome.confirmed:
        # Reality matched prediction → trust increases
        gate.weight += outcome.feedback_to_virtual.gate_weight_delta
        gate.weight = min(gate.weight, 1.0)

        if gate.weight > REFLEX_THRESHOLD:
            log_milestone("reflex_achieved", gate_id, reward=50.0)

    elif outcome.failed:
        # Reality differed → trust decreases
        gate.weight -= outcome.feedback_to_virtual.gate_weight_delta
        gate.weight = max(gate.weight, 0.0)
```

**Reflex = gate.weight > 0.8.** The gate opens immediately on any wave from its domain. No correlation wait. Like pulling hand from hot stove—spinal reflex, brain notified after.

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

## 🔗 Integration with Architecture

### Gates (Gateway-Architecture.md)

Cells don't talk to nerves directly. **Waves flow through gates.**

| Layer | Role | Document |
|-------|------|----------|
| Cell | Emit waves | This document |
| Gate | Accumulate correlation, route | [`Gateway-Architecture.md`](Gateway-Architecture.md) |
| Nerve | Respond to gate transitions | This document |

### Dual Gardens (Dual-Garden-Architecture.md)

Cells behave differently in Virtual vs Real:

| Property | Virtual Garden | Real Garden |
|----------|----------------|-------------|
| Wave volume | Massive (exploration) | Sparse (verified) |
| Monitoring | Full trace | Gate signals only |
| Purpose | Generate training data | Ground truth verification |

See [`Dual-Garden-Architecture.md`](Dual-Garden-Architecture.md) for the full model.

### Nervous System (Nervous-System.md)

The Nervous System document describes the **4D node space** where:

- **Cells** = sensory nodes emitting waves
- **Gates** = resonance chambers accumulating correlation
- **Nodes** = points in state space with weight from verification

### Message Protocol (Message-Protocol-Design.md)

Cells emit `WaveSignal` messages via NATS:

```json
{
  "domain": "distance",
  "confidence": 0.8,
  "semantic_content": { "cm": 25 },
  "lifeforce_cost": 0.3
}
```

See [`Message-Protocol-Design.md`](Message-Protocol-Design.md) for full schema.

### Cells Technical Reference

Implementation details extracted to dedicated folder:

- [`cells/Cells-Index.md`](cells/Cells-Index.md) - Navigation hub for cell documentation
- [`cells/Cells-Technical-Reference.md`](cells/Cells-Technical-Reference.md) - Python classes, SQL tables, code patterns

---

---

**Version:** 5.0 | **Created:** 2025-10-12 | **Updated:** 2026-02-14

*"Cells emit waves. Gates correlate. Attention emerges. Consciousness accumulates."*

🧬⚡ **TO THE ELECTRONS WE VIBE!**
