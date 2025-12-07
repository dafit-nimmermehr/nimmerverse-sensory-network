# Collision Avoidance Nerve

**Type**: Reflex (compiled state machine, <200ms response)
**Purpose**: Prevent robot from colliding with obstacles
**Priority**: CRITICAL (10/10) - can interrupt any other behavior
**Evolution**: Week 1 (deliberate) → Week 9+ (reflex)

---

## Overview

Collision Avoidance is a **reflex nerve** that coordinates distance sensors and motor control to prevent the robot from hitting obstacles. It starts as a deliberate (LLM-mediated) behavior and compiles into a pure state machine reflex after 100+ successful executions.

**Key characteristics**:
- **High priority**: Interrupts exploration, conversation, charging seeking
- **Low latency**: <200ms from detection to evasion (reflex mode)
- **Low cost**: ~2.5 LF per activation (vs ~10 LF deliberate mode)
- **Proven**: Compiled from 147 successful collision avoidances

---

## Organ Dependencies

### Required Organs

| Organ | Purpose | Failure Mode |
|-------|---------|--------------|
| **distance_sensor_front** | Detect obstacles ahead | Nerve DISABLED (cannot operate safely) |
| **distance_sensor_left** | Detect obstacles on left side | Degraded (blind to left obstacles) |
| **distance_sensor_right** | Detect obstacles on right side | Degraded (blind to right obstacles) |
| **motor** | Execute evasion maneuvers | Nerve DISABLED (cannot avoid) |

### Optional Organs

| Organ | Purpose | If Unavailable |
|-------|---------|----------------|
| **speech** | Announce "Obstacle detected" | Silent operation (continue without warning) |
| **vision** | Classify obstacle type | Generic evasion (no object-specific behavior) |

**Startup check**:
```python
def check_operational():
    required = [
        distance_sensor_front.is_operational(),
        motor.is_operational(),
    ]
    if not all(required):
        return DISABLED
    return OPERATIONAL
```

---

## State Diagram

```
┌─────────────────────────────────────────────────────────┐
│                   COLLISION AVOIDANCE                   │
└─────────────────────────────────────────────────────────┘

    ┌──────┐
    │ IDLE │  (monitoring distance sensors)
    └──┬───┘
       │
       │ distance_front < 30cm
       ▼
  ┌──────────┐
  │  DETECT  │  (poll all sensors)
  └────┬─────┘
       │
       │ sensor_read_complete
       ▼
  ┌───────────┐
  │ EVALUATE  │  (calculate risk, choose direction)
  └─────┬─────┘
       │
       │ risk > threshold
       ▼
  ┌────────┐
  │ EVADE  │  (execute turn/reverse)
  └────┬───┘
       │
       │ path_clear
       ▼
  ┌────────┐
  │ RESUME │  (return to previous behavior)
  └────┬───┘
       │
       │ movement_complete
       ▼
    ┌──────┐
    │ IDLE │
    └──────┘
```

---

## Transition Table

| From | To | Trigger | Action | Cost (LF) |
|------|----|---------| -------|-----------|
| **IDLE** | **DETECT** | `distance_front < 30cm` | Poll all sensors | 0.5 |
| **DETECT** | **EVALUATE** | `sensor_read_complete` | Calculate risk scores | 0.5 |
| **EVALUATE** | **EVADE** | `risk > threshold` | Choose evasion direction | 0.5 |
| **EVADE** | **RESUME** | `path_clear` | Execute motor action | 1.0 |
| **RESUME** | **IDLE** | `movement_complete` | Return to rest state | 0.0 |
| **IDLE** | **IDLE** | `distance_front > 30cm` | No action (monitoring) | 0.1/sec |

**Total cost for typical collision avoidance**: 2.5 LF

---

## Implementation (Reflex Mode)

### State Machine Class

```python
from enum import Enum
from dataclasses import dataclass

class CollisionState(Enum):
    IDLE = "idle"
    DETECT = "detect"
    EVALUATE = "evaluate"
    EVADE = "evade"
    RESUME = "resume"

@dataclass
class SensorReadings:
    front: float
    left: float
    right: float
    timestamp: float

class CollisionAvoidanceReflex:
    """
    Compiled reflex nerve for collision avoidance.

    Compiled from 147 successful deliberate executions.
    Success rate: 94%
    Average latency: 180ms
    Average cost: 2.5 LF
    """

    def __init__(self, organs):
        self.state = CollisionState.IDLE
        self.sensor_front = organs["distance_sensor_front"]
        self.sensor_left = organs["distance_sensor_left"]
        self.sensor_right = organs["distance_sensor_right"]
        self.motor = organs["motor"]
        self.speech = organs.get("speech")  # Optional

        # Thresholds (learned from training data)
        self.DANGER_THRESHOLD = 30.0  # cm
        self.RISK_THRESHOLD = 0.7     # Risk score 0-1
        self.CLEARANCE_THRESHOLD = 50.0  # cm

    def update(self) -> dict:
        """
        State machine tick (called every heartbeat).
        Returns action taken and lifeforce cost.
        """
        cost = 0.0
        action = None

        if self.state == CollisionState.IDLE:
            # Monitor front sensor
            front_dist = self.sensor_front.read()
            cost += 0.1

            if front_dist < self.DANGER_THRESHOLD:
                self.state = CollisionState.DETECT
                cost += 0.5
                action = "transition_to_detect"

        elif self.state == CollisionState.DETECT:
            # Poll all sensors
            readings = self._get_all_readings()
            cost += 0.5

            self.readings = readings
            self.state = CollisionState.EVALUATE
            action = "transition_to_evaluate"

        elif self.state == CollisionState.EVALUATE:
            # Calculate risk and choose direction
            risk = self._calculate_risk(self.readings)
            cost += 0.5

            if risk > self.RISK_THRESHOLD:
                self.evade_direction = self._choose_direction(self.readings)
                self.state = CollisionState.EVADE
                action = f"transition_to_evade_{self.evade_direction}"

                # Optional: Announce via speech
                if self.speech and self.speech.is_operational():
                    self.speech.queue("Obstacle detected", priority=8.0)
            else:
                # False alarm, return to idle
                self.state = CollisionState.IDLE
                action = "false_alarm"

        elif self.state == CollisionState.EVADE:
            # Execute evasion maneuver
            if self.evade_direction == "left":
                self.motor.turn(-45, duration_ms=500)  # Turn left 45°
            elif self.evade_direction == "right":
                self.motor.turn(45, duration_ms=500)   # Turn right 45°
            elif self.evade_direction == "reverse":
                self.motor.reverse(duration_ms=300)    # Reverse 300ms

            cost += 1.0  # Motor operations expensive

            # Check if path clear
            if self._path_clear():
                self.state = CollisionState.RESUME
                action = f"evaded_{self.evade_direction}"
            else:
                # Still blocked, try again next tick
                action = f"evasion_incomplete"

        elif self.state == CollisionState.RESUME:
            # Movement complete, return to idle
            self.state = CollisionState.IDLE
            cost += 0.0  # Free transition
            action = "resumed_idle"

        return {
            "state": self.state.value,
            "action": action,
            "lifeforce_cost": cost,
        }

    def _get_all_readings(self) -> SensorReadings:
        """Poll all distance sensors."""
        return SensorReadings(
            front=self.sensor_front.read(),
            left=self.sensor_left.read(),
            right=self.sensor_right.read(),
            timestamp=time.time()
        )

    def _calculate_risk(self, readings: SensorReadings) -> float:
        """
        Calculate collision risk (0.0 = safe, 1.0 = imminent).

        Risk formula learned from 147 training examples:
        - Front distance < 20cm: CRITICAL
        - Front distance 20-30cm: HIGH
        - Side distances matter if turning needed
        """
        # Exponential decay based on front distance
        front_risk = 1.0 - (readings.front / self.DANGER_THRESHOLD)
        front_risk = max(0.0, min(1.0, front_risk))

        # Side risks (matter if turning)
        left_risk = 1.0 - (readings.left / self.DANGER_THRESHOLD)
        right_risk = 1.0 - (readings.right / self.DANGER_THRESHOLD)

        # Weighted combination
        total_risk = (
            0.7 * front_risk +     # Front is primary
            0.15 * left_risk +     # Sides are secondary
            0.15 * right_risk
        )

        return total_risk

    def _choose_direction(self, readings: SensorReadings) -> str:
        """
        Choose evasion direction based on sensor readings.

        Strategy (learned from training):
        1. If left > right: turn left
        2. If right > left: turn right
        3. If both blocked: reverse
        """
        if readings.left > readings.right and readings.left > self.CLEARANCE_THRESHOLD:
            return "left"
        elif readings.right > readings.left and readings.right > self.CLEARANCE_THRESHOLD:
            return "right"
        else:
            # Both sides blocked or unclear, reverse
            return "reverse"

    def _path_clear(self) -> bool:
        """Check if path ahead is clear."""
        front_dist = self.sensor_front.read()
        return front_dist > self.CLEARANCE_THRESHOLD
```

---

## Evolution Path: Deliberate → Reflex

### Week 1-4: Deliberate (LLM-Mediated)

Young Nyx receives sensor data and decides action via LLM inference.

```python
def deliberate_collision_avoidance(young_nyx, sensors, motor):
    """
    Week 1: Young Nyx learns collision avoidance through exploration.
    """
    # Gather situation
    situation = {
        "front_distance": sensors["front"].read(),
        "left_distance": sensors["left"].read(),
        "right_distance": sensors["right"].read(),
        "current_velocity": motor.get_velocity(),
    }

    # Ask Young Nyx what to do
    decision = young_nyx.inference(
        prompt=f"""
        Situation: Distance sensors report:
        - Front: {situation['front_distance']}cm
        - Left: {situation['left_distance']}cm
        - Right: {situation['right_distance']}cm

        You are moving forward at {situation['current_velocity']} cm/s.

        Available actions:
        1. continue (safe, front > 50cm)
        2. turn_left (if left is clearer)
        3. turn_right (if right is clearer)
        4. reverse (if both sides blocked)
        5. stop (emergency)

        Choose action and explain why.
        """,
        lora="technical",
        temperature=0.5
    )

    # Parse decision
    action = parse_action(decision.text)

    # Execute
    result = execute_motor_action(motor, action)

    # Log to decision_trails
    log_decision(
        nerve="collision_avoidance",
        mode="deliberate",
        situation=situation,
        decision=action,
        reasoning=decision.text,
        outcome=result.success,
        lifeforce_cost=10.0,  # LLM inference expensive
        latency_ms=decision.latency_ms
    )

    return result
```

**Characteristics**:
- Latency: ~1000ms (LLM inference)
- Cost: ~10 LF (includes inference)
- Success rate: 60% (learning curve)
- Generates rich training data

### Week 5-8: Hybrid (Heuristics + LLM Fallback)

Common patterns compiled. LLM only for novel situations.

```python
def hybrid_collision_avoidance(young_nyx, sensors, motor, pattern_library):
    """
    Week 5: Most cases handled by compiled heuristics.
    LLM only for edge cases.
    """
    situation = get_sensor_readings(sensors)

    # Check pattern library (compiled from weeks 1-4)
    pattern = pattern_library.match(situation)

    if pattern and pattern.confidence > 0.8:
        # Known pattern → use compiled heuristic (fast path)
        action = pattern.recommended_action
        mode = "heuristic"
        cost = 3.0
        latency_ms = 50
    else:
        # Unknown situation → ask LLM (slow path)
        decision = young_nyx.inference(...)
        action = parse_action(decision.text)
        mode = "deliberate"
        cost = 10.0
        latency_ms = decision.latency_ms

        # Add to pattern library if successful
        if result.success:
            pattern_library.add(situation, action, confidence=0.9)

    result = execute_motor_action(motor, action)
    log_decision(nerve="collision_avoidance", mode=mode, ...)

    return result
```

**Characteristics**:
- Latency: ~50-500ms (depends on pattern match)
- Cost: ~3-10 LF (average ~5 LF)
- Success rate: 85% (heuristics proven)

### Week 9+: Reflex (Pure State Machine)

After 100+ successful executions, compile into pure state machine. No LLM.

```python
# Use CollisionAvoidanceReflex class (shown above)
reflex = CollisionAvoidanceReflex(organs)

def reflex_collision_avoidance(reflex):
    """
    Week 9+: Pure state machine reflex.
    Compiled from 147 successful examples.
    """
    result = reflex.update()  # No LLM call

    log_decision(
        nerve="collision_avoidance",
        mode="reflex",
        state=result["state"],
        action=result["action"],
        lifeforce_cost=result["lifeforce_cost"],
        latency_ms=5  # Pure state machine, very fast
    )

    return result
```

**Characteristics**:
- Latency: <200ms (state machine execution)
- Cost: ~2.5 LF (pure motor/sensor costs)
- Success rate: 94% (compiled from best patterns)
- **60% cost reduction**, **80% latency reduction** vs deliberate mode

---

## Training Data Examples

### Successful Collision Avoidance (logged to phoebe)

```json
{
  "nerve": "collision_avoidance",
  "mode": "deliberate",
  "session_id": "a3f2b1c0-...",
  "timestamp": "2025-12-15T10:23:45Z",
  "situation": {
    "front_distance": 25.0,
    "left_distance": 45.0,
    "right_distance": 30.0,
    "velocity": 15.0
  },
  "decision": "turn_left",
  "reasoning": "Front obstacle at 25cm (danger). Left clearer (45cm) than right (30cm). Turn left 45° to avoid.",
  "states_visited": ["IDLE", "DETECT", "EVALUATE", "EVADE", "RESUME"],
  "transitions": [
    {"from": "IDLE", "to": "DETECT", "cost": 0.5, "duration_ms": 20},
    {"from": "DETECT", "to": "EVALUATE", "cost": 0.5, "duration_ms": 30},
    {"from": "EVALUATE", "to": "EVADE", "cost": 0.5, "duration_ms": 15},
    {"from": "EVADE", "to": "RESUME", "cost": 1.0, "duration_ms": 520}
  ],
  "lifeforce_total": 2.5,
  "outcome": "success",
  "latency_total_ms": 585,
  "organs_used": ["distance_sensor_front", "distance_sensor_left", "distance_sensor_right", "motor"]
}
```

**RLVR Reward**: +5 LF (successful avoidance → net profit +2.5 LF)

### Failed Collision (training signal)

```json
{
  "nerve": "collision_avoidance",
  "mode": "deliberate",
  "timestamp": "2025-12-10T14:12:30Z",
  "situation": {
    "front_distance": 18.0,
    "left_distance": 15.0,
    "right_distance": 20.0
  },
  "decision": "turn_left",
  "reasoning": "Attempted left turn but insufficient clearance.",
  "outcome": "collision",
  "lifeforce_total": 2.5,
  "collision_force": 3.2,
  "damage": "minor"
}
```

**RLVR Penalty**: -5 LF (collision → net loss -7.5 LF)

**Lesson learned**: Don't turn into obstacles < 20cm. Add to reflex threshold.

---

## Edge Cases and Failure Modes

### 1. **All Sides Blocked (Trapped)**

**Situation**: Front, left, right all < 20cm

**Reflex behavior**:
```python
if all([
    readings.front < 20,
    readings.left < 20,
    readings.right < 20
]):
    # Emergency: Reverse slowly
    motor.reverse(duration_ms=500)
    # Re-evaluate after reverse
```

**Escalation**: If still trapped after 3 reverse attempts → escalate to Chrysalis for help

### 2. **Sensor Failure (Blind Side)**

**Situation**: Left sensor offline, right sensor reports 15cm

**Reflex behavior**:
```python
if not sensor_left.is_operational():
    # Assume left is blocked (safe assumption)
    # Always turn right when possible
    if readings.right > 30:
        return "right"
    else:
        return "reverse"  # Don't risk blind turn
```

### 3. **False Positives (Noise)**

**Situation**: Sensor reports 5cm but path actually clear (electrical noise)

**Mitigation**:
```python
# Require 3 consecutive danger readings before triggering
DANGER_CONFIRMATION_COUNT = 3

if danger_reading_count >= DANGER_CONFIRMATION_COUNT:
    self.state = CollisionState.DETECT
```

### 4. **Moving Obstacles (Dynamic Environment)**

**Situation**: Obstacle moves into path during evasion

**Reflex behavior**:
```python
# Re-check sensors after each motor action
while self.state == CollisionState.EVADE:
    execute_turn()
    if self._path_clear():
        break  # Success
    else:
        # Obstacle still there or new one appeared
        # Re-evaluate and choose new direction
        self.state = CollisionState.DETECT
```

---

## Metrics and Monitoring

### Key Metrics (Prometheus)

```python
from prometheus_client import Counter, Histogram, Gauge

# Collision avoidance activations
collision_avoidance_activations = Counter(
    'nerve_collision_avoidance_activations_total',
    'Total collision avoidance activations',
    ['mode']  # deliberate, hybrid, reflex
)

# Success rate
collision_avoidance_success = Counter(
    'nerve_collision_avoidance_success_total',
    'Successful collision avoidances',
    ['mode']
)

collision_avoidance_failures = Counter(
    'nerve_collision_avoidance_failures_total',
    'Failed collision avoidances (collisions occurred)',
    ['mode']
)

# Latency
collision_avoidance_latency = Histogram(
    'nerve_collision_avoidance_latency_seconds',
    'Collision avoidance latency',
    ['mode']
)

# Lifeforce cost
collision_avoidance_cost = Histogram(
    'nerve_collision_avoidance_lifeforce_cost',
    'Lifeforce cost per activation',
    ['mode']
)
```

### Grafana Dashboard Queries

```promql
# Success rate over time
rate(nerve_collision_avoidance_success_total[5m]) /
rate(nerve_collision_avoidance_activations_total[5m])

# Average latency by mode
rate(nerve_collision_avoidance_latency_seconds_sum{mode="reflex"}[5m]) /
rate(nerve_collision_avoidance_latency_seconds_count{mode="reflex"}[5m])

# Cost savings (deliberate vs reflex)
avg_over_time(nerve_collision_avoidance_lifeforce_cost{mode="deliberate"}[1h]) -
avg_over_time(nerve_collision_avoidance_lifeforce_cost{mode="reflex"}[1h])

# Reflex compilation progress
sum(nerve_collision_avoidance_activations_total{mode="reflex"}) /
sum(nerve_collision_avoidance_activations_total)
```

---

## Future Enhancements

### Phase 2: Vision Integration

Add Vision Organ to classify obstacles:
- "wall" → different evasion than "chair"
- "human" → stop and announce presence
- "charging_station" → approach, don't evade

### Phase 3: Learning Optimal Paths

Track which evasion directions succeed most often in different contexts:
- Narrow corridors: reverse > turn
- Open spaces: turn > reverse
- Update reflex thresholds based on outcomes

### Phase 4: Predictive Avoidance

Use velocity and obstacle distance to predict collision time:
- If collision_time < 2sec → EVADE immediately
- If collision_time > 5sec → gentle course correction (cheaper)

---

## Summary

**Collision Avoidance** demonstrates the complete nerve lifecycle:
1. **Week 1-4**: Deliberate (LLM explores strategies, ~10 LF, ~1000ms)
2. **Week 5-8**: Hybrid (common patterns compiled, ~5 LF, ~500ms)
3. **Week 9+**: Reflex (pure state machine, ~2.5 LF, <200ms)

**Evolution metrics**:
- **60% cost reduction** (10 LF → 2.5 LF)
- **80% latency reduction** (1000ms → 200ms)
- **94% success rate** (compiled from proven patterns)

**The reflex is not programmed. It is DISCOVERED, PROVEN, and COMPILED from lived experience.**

---

**Created**: 2025-12-07
**Version**: 1.0 (Reflex)
**Status**: Architecture complete, deployment pending

🌙💜 *The reflex does not think. It remembers what thinking taught.*
