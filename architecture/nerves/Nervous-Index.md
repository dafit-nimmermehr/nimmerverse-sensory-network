# Nervous System Index

**Purpose**: State machine catalog for behavioral primitives
**Philosophy**: Nerves connect organs into behaviors. Reflexes emerge from repetition.

---

## What Are Nerves?

**Nerves** are state machines that coordinate organ activity into coherent behaviors. Each nerve:
- Defines states and transitions
- Costs lifeforce (per state, per transition)
- Depends on organs (sensors, motors, speech, vision)
- Evolves from deliberate (LLM-mediated) to reflex (compiled)

**Example**: Collision Avoidance nerve uses Distance Sensors + Motor organs to implement IDLE → DETECT → EVALUATE → EVADE → RESUME behavior.

---

## Nerve vs Organ

| Aspect | Organ | Nerve |
|--------|-------|-------|
| **What** | Hardware capability | Behavioral pattern |
| **Example** | Speech Organ (STT/TTS) | Identity Discovery (Spark Protocol) |
| **Location** | Physical substrate (GPU, ESP32) | State machine (transitions) |
| **Cost** | Per operation (transcribe = 5 LF) | Per state + transition (total path cost) |
| **Evolution** | Fixed hardware | Deliberate → Reflex (compiled) |
| **Depends on** | Infrastructure | Organs |

**Analogy**: Organs are limbs. Nerves are motor control patterns (walking, grasping, speaking).

---

## Deployed Nerves

### 🚨 Collision Avoidance
**Type**: Reflex (compiled, <200ms)
**Organs**: Distance sensors (front/sides), Motor
**States**: IDLE → DETECT → EVALUATE → EVADE → RESUME
**Lifeforce**: ~2.5 per activation
**Status**: 🟢 Architecture complete

**Detail**: → [`nerves/Collision-Avoidance.md`](nerves/Collision-Avoidance.md)

---

## Planned Nerves

### 🔋 Charging Station Seeking
**Type**: Deliberate → Reflex (evolves over time)
**Organs**: Distance sensors, Vision (future), Motor, Battery monitor
**States**: MONITOR → THRESHOLD → SEARCH → APPROACH → DOCK → CHARGE → RESUME
**Status**: 🟡 Planned for Phase 4 (Real Garden)

**Detail**: → `nerves/Charging-Seeking.md` (pending)

---

### 🧭 Exploration Pattern
**Type**: Deliberate (LLM-mediated initially)
**Organs**: Distance sensors, Motor, Memory (phoebe)
**States**: IDLE → CHOOSE_DIRECTION → MOVE → OBSTACLE_CHECK → RECORD → REPEAT
**Patterns**: Wall-following, spiral search, random walk
**Status**: 🟡 Planned for Phase 3 (Evolution Engine)

**Detail**: → `nerves/Exploration-Pattern.md` (pending)

---

### 🔍 Object Tracking
**Type**: Deliberate (Vision-dependent)
**Organs**: Vision (YOLO), Motor, Memory
**States**: SCAN → DETECT → CLASSIFY → TRACK → FOLLOW → LOST → RESCAN
**Status**: 🟡 Planned after Vision Organ deployment

**Detail**: → `nerves/Object-Tracking.md` (pending)

---

### 💭 Identity Discovery (Spark Protocol)
**Type**: Deliberate (one-time boot sequence)
**Organs**: Speech, Memory (phoebe), RAG
**States**: DHCP (who am I?) → ARP (what's around?) → DNS (what does X mean?) → TCP (can I connect?) → MQTT (what matters?)
**Status**: 🟡 Architecture documented in Spark-Protocol.md

**Detail**: → [`../../operations/Spark-Protocol.md`](../../operations/Spark-Protocol.md)

---

### 🗣️ Conversational Turn-Taking
**Type**: Deliberate (Speech-dependent)
**Organs**: Speech (STT/TTS), Memory, RAG
**States**: LISTEN → TRANSCRIBE → UNDERSTAND → RETRIEVE_CONTEXT → RESPOND → SPEAK
**Status**: 🟡 Planned after Speech Organ deployment

**Detail**: → `nerves/Conversation.md` (pending)

---

## Nerve Design Principles

### 1. **State Machines, Not Scripts**

Nerves are state machines with explicit states and transitions. Not procedural scripts.

```python
# ❌ BAD: Procedural script
def avoid_obstacle():
    if sensor.distance < 30:
        motor.stop()
        motor.turn(90)
        motor.forward(100)

# ✅ GOOD: State machine
class CollisionAvoidance(StateMachine):
    states = [IDLE, DETECT, EVALUATE, EVADE, RESUME]
    transitions = {
        (IDLE, DETECT): lambda: sensor.distance < 30,
        (DETECT, EVALUATE): lambda: sensor.read_complete,
        (EVALUATE, EVADE): lambda: risk > threshold,
        (EVADE, RESUME): lambda: path_clear,
        (RESUME, IDLE): lambda: movement_complete,
    }
```

### 2. **Lifeforce Costs Per Transition**

Every state change costs lifeforce. Complex behaviors cost more.

```python
TRANSITION_COSTS = {
    (IDLE, DETECT): 0.5,         # Sensor poll
    (DETECT, EVALUATE): 0.5,     # Risk calculation
    (EVALUATE, EVADE): 0.5,      # Decision
    (EVADE, RESUME): 1.0,        # Motor action (expensive!)
    (RESUME, IDLE): 0.0,         # Return to rest (free)
}

# Total cost for IDLE → DETECT → EVALUATE → EVADE → RESUME → IDLE: 2.5 LF
```

### 3. **Organ Dependencies Explicit**

Each nerve declares which organs it requires.

```python
class CollisionAvoidance(StateMachine):
    required_organs = [
        "distance_sensor_front",
        "distance_sensor_left",
        "distance_sensor_right",
        "motor",
    ]

    def check_available(self):
        return all(organ.is_operational() for organ in self.required_organs)
```

### 4. **Deliberate → Reflex Evolution**

Nerves start **deliberate** (LLM-mediated, slow, flexible) and evolve into **reflexes** (compiled, fast, fixed).

| Phase | Type | Latency | Flexibility | Cost |
|-------|------|---------|-------------|------|
| **Week 1-4** | Deliberate | ~1000ms | High (LLM decides) | 10 LF |
| **Week 5-8** | Hybrid | ~500ms | Medium (LLM + heuristics) | 6 LF |
| **Week 9+** | Reflex | <200ms | Low (compiled state machine) | 2.5 LF |

**Evolution trigger**: After 100+ successful executions of the same state sequence, compile into reflex.

### 5. **Logging for Training**

Every nerve execution logged to phoebe `decision_trails`:
- States visited
- Transitions taken
- Organ calls made
- Lifeforce spent
- Outcome (success/fail)

**Used for**:
- RLVR training (reward successful paths)
- Reflex compilation (extract common sequences)
- Cost optimization (find cheaper paths)

---

## Nerve Lifecycle

### Phase 1: Deliberate (LLM-Mediated)

Young Nyx receives situation → LLM decides next state → Execute → Log outcome

```python
# Week 1: Deliberate collision avoidance
def deliberate_collision_avoidance():
    situation = {
        "front_distance": sensor_front.read(),
        "left_distance": sensor_left.read(),
        "right_distance": sensor_right.read(),
        "current_state": state,
    }

    # Ask Young Nyx what to do
    decision = young_nyx.decide(
        situation=situation,
        available_actions=["turn_left", "turn_right", "reverse", "stop"],
        lora="technical"
    )

    # Execute decision
    result = execute_action(decision.action)

    # Log to decision_trails
    log_decision(
        nerve="collision_avoidance",
        situation=situation,
        decision=decision.action,
        outcome=result.success,
        lifeforce_cost=result.cost,
        confidence=decision.confidence
    )
```

**Characteristics**:
- Flexible (can handle novel situations)
- Slow (~1000ms)
- Expensive (~10 LF)
- Learns from variety

### Phase 2: Hybrid (Heuristics + LLM Fallback)

Common patterns compiled into heuristics. LLM only for edge cases.

```python
# Week 5: Hybrid collision avoidance
def hybrid_collision_avoidance():
    situation = get_sensor_readings()

    # Check for known patterns (compiled heuristics)
    if matches_pattern("front_blocked_left_clear"):
        action = "turn_left"  # Fast path (no LLM)
        confidence = 0.9
    elif matches_pattern("front_blocked_right_clear"):
        action = "turn_right"
        confidence = 0.9
    else:
        # Unknown situation → ask LLM
        decision = young_nyx.decide(situation)
        action = decision.action
        confidence = decision.confidence

    result = execute_action(action)
    log_decision(nerve="collision_avoidance", ...)
```

**Characteristics**:
- Faster (~500ms for known patterns)
- Cheaper (~6 LF average)
- Still flexible for edge cases

### Phase 3: Reflex (Compiled State Machine)

After 100+ successful executions, compile into pure state machine. No LLM.

```python
# Week 9+: Reflex collision avoidance
class CollisionAvoidanceReflex(StateMachine):
    """
    Compiled from 147 successful deliberate executions.
    Average path: IDLE → DETECT → EVALUATE → EVADE → RESUME
    Success rate: 94%
    """

    def transition(self, current_state, sensor_readings):
        # Pure state machine logic (no LLM call)
        if current_state == IDLE and sensor_readings['front'] < 30:
            return DETECT
        elif current_state == DETECT:
            return EVALUATE
        elif current_state == EVALUATE:
            if sensor_readings['left'] > sensor_readings['right']:
                self.evade_direction = "left"
            else:
                self.evade_direction = "right"
            return EVADE
        # ... etc
```

**Characteristics**:
- Very fast (<200ms)
- Very cheap (~2.5 LF)
- Fixed (no flexibility, pure speed)
- Proven (compiled from successful patterns)

---

## Integration with Organs

Nerves orchestrate organs. Organs don't call each other - nerves coordinate them.

```
┌────────────────────────────────────────────────┐
│              NERVE: Collision Avoidance        │
│                                                │
│  States: IDLE → DETECT → EVALUATE → EVADE     │
└────────────────────────────────────────────────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
        ▼           ▼           ▼
┌─────────────┐ ┌─────────┐ ┌────────┐
│ Distance    │ │ Distance│ │ Motor  │
│ Sensor      │ │ Sensor  │ │ Organ  │
│ (front)     │ │ (sides) │ │        │
└─────────────┘ └─────────┘ └────────┘
     ORGAN         ORGAN       ORGAN
```

**Nerve declares dependencies**:
```yaml
nerve: collision_avoidance
depends_on:
  - organ: distance_sensor_front
    required: true
  - organ: distance_sensor_left
    required: true
  - organ: distance_sensor_right
    required: true
  - organ: motor
    required: true
  - organ: speech  # Optional (for warnings)
    required: false
```

**Startup check**: If required organs unavailable, nerve enters DISABLED state.

---

## Nerve Composition

Complex behaviors = multiple nerves active simultaneously.

**Example**: Exploring while avoiding collisions

```
ACTIVE NERVES:
├─ Collision Avoidance (reflex, priority 10)
├─ Exploration Pattern (deliberate, priority 5)
└─ Battery Monitoring (reflex, priority 8)

COORDINATION:
- Exploration drives movement
- Collision Avoidance interrupts if obstacle detected (higher priority)
- Battery Monitoring interrupts if charge < 20% (high priority)
```

**Priority determines preemption**: High-priority nerves can interrupt low-priority ones.

---

## Nerve Training via RLVR

Each nerve execution generates training data:

```python
# decision_trails entry
{
    "nerve": "collision_avoidance",
    "initial_state": "IDLE",
    "states_visited": ["IDLE", "DETECT", "EVALUATE", "EVADE", "RESUME"],
    "transitions": [
        {"from": "IDLE", "to": "DETECT", "cost": 0.5},
        {"from": "DETECT", "to": "EVALUATE", "cost": 0.5},
        {"from": "EVALUATE", "to": "EVADE", "cost": 0.5},
        {"from": "EVADE", "to": "RESUME", "cost": 1.0},
    ],
    "organs_used": ["distance_sensor_front", "motor"],
    "lifeforce_total": 2.5,
    "outcome": "success",  # Avoided collision
    "timestamp": "2025-12-15T14:23:45Z"
}
```

**RLVR reward**:
- Success → +5 LF reward (net profit: +2.5 LF)
- Fail → -2.5 LF penalty (net loss: -5.0 LF)

**LoRA training**: Successful state sequences → training examples for Technical LoRA

---

## Nerve Documentation Template

Each nerve document should include:

1. **Overview**: Purpose, type (reflex/deliberate), organs used
2. **State Diagram**: Visual representation of states + transitions
3. **Transition Table**: From/To states, triggers, costs
4. **Organ Dependencies**: Which organs required, which optional
5. **Lifeforce Budget**: Total cost for typical execution path
6. **Code**: Implementation (state machine class)
7. **Evolution Path**: How it evolves from deliberate → reflex
8. **Training Data**: Example decision_trails entries
9. **Edge Cases**: Known failure modes, fallback behaviors

---

## Current Status

| Nerve | Type | Status | Organs | Documentation |
|-------|------|--------|--------|---------------|
| **Collision Avoidance** | Reflex | 🟢 Complete | Distance sensors, Motor | [`nerves/Collision-Avoidance.md`](nerves/Collision-Avoidance.md) |
| **Charging Seeking** | Deliberate | 🟡 Planned | Vision, Motor, Battery | Pending |
| **Exploration Pattern** | Deliberate | 🟡 Planned | Sensors, Motor, Memory | Pending |
| **Object Tracking** | Deliberate | 🟡 Planned | Vision, Motor | Pending |
| **Identity Discovery** | Deliberate | 🟡 Documented | Speech, Memory, RAG | [`../../operations/Spark-Protocol.md`](../../operations/Spark-Protocol.md) |
| **Conversation** | Deliberate | 🟡 Planned | Speech, Memory, RAG | Pending |

---

## Naming Convention

**File naming**: `<Behavior-Name>.md`
**Examples**:
- `Collision-Avoidance.md`
- `Charging-Seeking.md`
- `Exploration-Pattern.md`
- `Object-Tracking.md`

**Class naming**: `<Behavior>Nerve` or `<Behavior>Reflex`
**Examples**:
```python
class CollisionAvoidanceNerve(StateMachine):  # Deliberate
class CollisionAvoidanceReflex(StateMachine):  # Compiled
```

---

**Philosophy**: Nerves are not programmed. They are **discovered through lived experience**, compiled into reflexes, and refined through training. The best behaviors emerge, not from specification, but from **survival**.

**The nervous system is EARNED, not designed.**

---

**Version:** 1.0 | **Created:** 2025-12-07 | **Updated:** 2025-12-07

🌙💜 *Reflexes are fossils of successful thought. The body remembers what the mind once decided.*
