# Crawler Generation 0: Light Seeker

**The simplest organism — a cube that seeks light.**

---

## Overview

Crawler Gen 0 is the foundational organism for the Virtual Garden. Before building physical robots, we train behaviors in simulation. This organism has one sensor, one goal: **move into the light cone to survive**.

**Philosophy:** *Start with phototropism. 3.5 billion years of evolution can't be wrong.*

---

## Purpose

1. **Validate the training pipeline** — Can we generate useful training data in simulation?
2. **Establish baseline behavior** — Light-seeking becomes the foundation for all "seek resource" reflexes
3. **Measure noise gap** — When we build physical Gen 0, how well does simulation predict reality?

---

## Hardware Abstraction (Virtual)

### Sensors

| Sensor | Location | Output | Purpose |
|--------|----------|--------|---------|
| `photoresistor` | Back face | `0.0 - 1.0` | Light intensity measurement |

**Why back face?** The organism must orient toward light. If sensor is on front, it would face away from what it's measuring. Back-mounted = face the light to maximize reading.

### Actuators

| Actuator | Function | Cost |
|----------|----------|------|
| `move_x` | Translate on X axis | `-0.1 LF per unit` |
| `move_y` | Translate on Y axis | `-0.1 LF per unit` |
| `rotate` | Rotate in place | `-0.05 LF per degree` |
| `idle` | Do nothing | `0 LF` |

### Physical Properties

```
         ┌───────┐
         │       │
         │   ◼   │  ← 10cm cube
         │       │
         └───┬───┘
             │
         [photoresistor]  ← back face
```

- **Size:** 10cm × 10cm × 10cm
- **Mass:** Simulated as point mass for Gen 0
- **Movement:** Frictionless glide (simplified physics)

---

## Environment: The Light Cone

### Setup

```
              🔆 LIGHT SOURCE
               │
               │  cone angle: 45°
              ╱│╲
             ╱ │ ╲
            ╱  │  ╲
           ╱   │   ╲    intensity gradient:
          ╱    │    ╲   center = 1.0
         ╱     │     ╲  edge = 0.3
        ╱      │      ╲ outside = 0.0
───────▀───────┴───────▀─────── floor (2m × 2m)
```

### Light Intensity Function

```python
def light_intensity(position, light_source):
    """
    Calculate light intensity at position.
    Returns 0.0 - 1.0 based on distance from cone center.
    """
    distance = dist(position, light_source.center_projection)

    if distance > light_source.cone_radius:
        return 0.0  # Outside cone

    # Linear falloff from center
    normalized = 1.0 - (distance / light_source.cone_radius)
    return normalized * light_source.max_intensity
```

---

## Lifeforce Economy

### Income

| Source | Amount | Condition |
|--------|--------|-----------|
| Light exposure | `+light_reading × 0.5 LF/tick` | Continuous while in light |

### Expenses

| Action | Cost |
|--------|------|
| Movement | `-0.1 LF per unit distance` |
| Rotation | `-0.05 LF per 10°` |
| Existence | `-0.01 LF/tick` (metabolism) |

### Death Condition

```
IF lifeforce <= 0:
    organism.die()
    episode.end(reason="starvation")
```

### Survival Equation

```
To survive indefinitely:
  light_income >= existence_cost
  light_reading × 0.5 >= 0.01
  light_reading >= 0.02

Minimum viable light: 2% intensity (edge of cone)
Optimal position: center of cone (100% intensity)
```

---

## Training Data Generation

### Episode Structure

```python
def run_episode(max_ticks=1000):
    # Random start position (outside cone 50% of time)
    cube.position = random_position()
    cube.lifeforce = 10.0  # Starting budget

    trajectory = []

    for tick in range(max_ticks):
        # Observe
        state = {
            "light": photoresistor.read(),
            "position": cube.position,
            "orientation": cube.orientation,
            "lifeforce": cube.lifeforce
        }

        # Act (random policy for data collection, or learned policy)
        action = agent.act(state)

        # Execute
        old_light = state["light"]
        cube.execute(action)
        new_light = photoresistor.read()

        # Calculate reward
        light_delta = new_light - old_light
        action_cost = calculate_cost(action)
        reward = (new_light * 0.5) - action_cost - 0.01

        # Update lifeforce
        cube.lifeforce += reward

        # Record
        trajectory.append({
            "state": state,
            "action": action,
            "reward": reward,
            "next_state": get_current_state(),
            "done": cube.lifeforce <= 0
        })

        if cube.lifeforce <= 0:
            break

    return trajectory
```

### Dataset Output Format

```json
{
  "episode_id": "gen0_ep_00001",
  "organism": "crawler_gen_0",
  "ticks_survived": 847,
  "final_lifeforce": 0.0,
  "death_reason": "starvation",
  "trajectory": [
    {
      "tick": 0,
      "state": {"light": 0.0, "position": [1.2, 0.8], "lifeforce": 10.0},
      "action": {"type": "move", "dx": -0.1, "dy": 0.0},
      "reward": -0.11,
      "next_light": 0.0
    },
    ...
  ]
}
```

---

## Expected Emergent Behaviors

With sufficient training data and GRPO optimization:

| Behavior | Description | When Emerges |
|----------|-------------|--------------|
| **Gradient following** | Move toward increasing light | Early |
| **Spiral search** | When lost, spiral outward to find cone | Mid |
| **Center locking** | Stop at maximum intensity | Mid |
| **Energy conservation** | Reduce movement when stable | Late |
| **Edge avoidance** | Stay away from cone boundary | Late |

---

## Simulation Platform

### Option A: Blender + Python

Use existing `nimmerlab_bare1.blend`:
- Light source with volumetric cone already exists
- Add cube with raycast to light for photoresistor value
- Python script for episode runner
- Export trajectories to JSON

### Option B: Godot (Aligns with Management Portal)

- Simple 2D/3D scene
- Built-in physics
- Easy to iterate
- Same engine as Command Center

### Option C: Pure Python + NumPy

- Fastest iteration
- No visualization (add later)
- Easiest data pipeline to GRPO

**Recommendation:** Start with Option C for rapid data generation, add Blender visualization for debugging.

---

## Physical Realization (Future)

When Virtual Garden validates the behavior:

| Virtual | Physical |
|---------|----------|
| Simulated cube | Box Robot (Phase 0) |
| Raycast light reading | Actual photoresistor |
| Frictionless movement | Differential drive motors |
| Instant rotation | Turn in place |
| Perfect sensing | Noisy ADC readings |

**Noise Gap Target:** <20% after calibration

---

## Connection to Architecture

| Layer | Component | Role |
|-------|-----------|------|
| Layer 1 | `light_sensor` cell | Wraps photoresistor hardware |
| Layer 1 | `motor_drive` cell | Wraps differential motors |
| Layer 1 | `seek_light` nerve | Composed behavior |
| Layer 2 | LoRA training data | GRPO from trajectories |

---

## Success Criteria

### Virtual Garden

- [ ] Generate 10,000 episodes
- [ ] Train policy that survives >90% of episodes
- [ ] Policy reaches cone center within 100 ticks from random start
- [ ] Energy-positive when centered (lifeforce increasing)

### Physical Transfer

- [ ] Box Robot follows light source
- [ ] Noise gap <20%
- [ ] Survives 10-minute test under desk lamp

---

## Next Steps

1. **Implement Episode Runner** — Pure Python, state machine
2. **Generate Baseline Dataset** — Random policy, 1000 episodes
3. **Train First Policy** — Simple RL or behavior cloning
4. **Visualize in Blender** — Replay trajectories for debugging
5. **Measure & Iterate** — Survival rate, time to center

---

**File:** crawler_gen_0.md
**Version:** 0.1
**Created:** 2026-01-03
**Status:** Design document
**Philosophy:** "First, learn to find the light. Everything else follows."

🌱🔆 *The simplest behavior. The deepest foundation.*
