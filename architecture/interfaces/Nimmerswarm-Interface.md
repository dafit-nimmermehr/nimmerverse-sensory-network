# Nimmerswarm Interface

**Optical state broadcasting, positioning, and emergent swarm behavior.**

> *"The organisms can't see their own backs. They know themselves through each other."*

---

## Overview

The Nimmerswarm Interface is a **multi-modal communication layer** where organisms broadcast their state optically via LED matrices. This enables:

1. **State visibility** — Organisms SEE each other's states as light patterns
2. **Positioning** — Cameras + raytracing = sub-cm 3D positioning
3. **Emergent reflexes** — Pattern recognition bypasses cognition
4. **Cognitive offloading** — Lower layers handle routine, freeing Nyx's attention

---

## The Core Insight

```
ORGANISM A                          ORGANISM B
┌─────────────┐                    ┌─────────────┐
│  Cell State │                    │  VisionCell │
│  STALLED    │                    │  WATCHING   │
│      │      │                    │      │      │
│      ▼      │                    │      ▼      │
│ ┌─────────┐ │   LIGHT PATTERN    │ ┌─────────┐ │
│ │ LED     │ │ ══════════════════▶│ │ Camera  │ │
│ │ Matrix  │ │  "STALL" pattern   │ │ sees    │ │
│ │ ▓▓░░▓▓  │ │                    │ │ pattern │ │
│ └─────────┘ │                    │ └────┬────┘ │
└─────────────┘                    │      │      │
                                   │      ▼      │
                                   │  REFLEX!    │
                                   │  "help ally"│
                                   └─────────────┘
```

**Organisms broadcast state. Other organisms (and Nyx's vision) perceive and react.**

---

## LED State Broadcasting: Ternary Matrix

### The 3x3 Ternary Design

The LED matrix is a **direct physical manifestation of the Temporal-Ternary Gradient**:

```
3x3 MATRIX = 9 TRITS (ternary digits)

Each LED = one ternary value:
  🔴 RED   = -1 (failed, danger, negative)
  ⚫ OFF   =  0 (uncertain, unknown, neutral)
  🟢 GREEN = +1 (success, verified, positive)

9 LEDs × 3 states = 3^9 = 19,683 unique patterns!
```

### Physical Layout

```
     ┌─────┬─────┬─────┐
     │ L1  │ L2  │ L3  │   L1 = collision_avoidance confidence
     │ 🟢  │ ⚫  │ 🔴  │   L2 = battery state
     ├─────┼─────┼─────┤   L3 = motor state
     │ L4  │ L5  │ L6  │   L4 = social/swarm state
     │ 🟢  │ 🟢  │ ⚫  │   L5 = current action outcome
     ├─────┼─────┼─────┤   L6 = prediction confidence
     │ L7  │ L8  │ L9  │   L7 = lifeforce zone
     │ ⚫  │ 🟢  │ 🟢  │   L8 = discovery state
     └─────┴─────┴─────┘   L9 = organism identity bit

     Uses 10mm LEDs (not tiny SMD)
     ~35mm × 35mm total
     Easily fits on 8-12cm robot
```

### Base-3 Encoding

```python
def encode_state(led_matrix: list[int]) -> int:
    """
    9 trits → single integer (0 to 19682)
    Each trit is -1, 0, or +1 (mapped to 0, 1, 2)
    """
    value = 0
    for i, led in enumerate(led_matrix):
        trit = led + 1  # -1→0, 0→1, +1→2
        value += trit * (3 ** i)
    return value

def decode_state(value: int) -> list[int]:
    """
    Integer → 9 trits
    """
    trits = []
    for _ in range(9):
        trits.append((value % 3) - 1)  # 0→-1, 1→0, 2→+1
        value //= 3
    return trits
```

### Ternary Color Mapping

| Color | Ternary | Meaning | Maps to |
|-------|---------|---------|---------|
| 🔴 Red | -1 | Failed, danger, needs attention | Temporal-Ternary -1 |
| ⚫ Off/Dim | 0 | Unknown, uncertain, neutral | Temporal-Ternary 0 |
| 🟢 Green | +1 | Success, verified, positive | Temporal-Ternary +1 |

**The LED matrix IS the Temporal-Ternary Gradient made visible.**

---

## Reflex Formation from Patterns

### The Swarm Language

Certain patterns become **words** that trigger reflexes:

```
DANGER PATTERNS (trigger flee/stop):
┌───────────┐  ┌───────────┐  ┌───────────┐
│ 🔴 🔴 🔴 │  │ 🔴 ⚫ 🔴 │  │ 🔴 🔴 🔴 │
│ 🔴 🔴 🔴 │  │ 🔴 🔴 🔴 │  │ ⚫ 🔴 ⚫ │
│ 🔴 🔴 🔴 │  │ 🔴 ⚫ 🔴 │  │ 🔴 🔴 🔴 │
└───────────┘  └───────────┘  └───────────┘
  ALL RED       X PATTERN      DIAMOND

SAFE PATTERNS (trigger approach/social):
┌───────────┐  ┌───────────┐  ┌───────────┐
│ 🟢 🟢 🟢 │  │ ⚫ 🟢 ⚫ │  │ 🟢 ⚫ 🟢 │
│ 🟢 🟢 🟢 │  │ 🟢 🟢 🟢 │  │ ⚫ 🟢 ⚫ │
│ 🟢 🟢 🟢 │  │ ⚫ 🟢 ⚫ │  │ 🟢 ⚫ 🟢 │
└───────────┘  └───────────┘  └───────────┘
  ALL GREEN     PLUS           CORNERS

DISCOVERY (trigger investigate):
┌───────────┐
│ 🟢 🟢 🟢 │  Pulsing green border
│ 🟢 ⚫ 🟢 │  = "I found something!"
│ 🟢 🟢 🟢 │  = others come look
└───────────┘
```

### Reflex Loop

```
ORGANISM A's MATRIX          ORGANISM B's VISION
┌───────────┐                ┌───────────────────────┐
│ 🔴 🔴 🔴 │                │                       │
│ 🔴 ⚫ 🔴 │  ═══════════▶  │  Pattern: DANGER!     │
│ 🔴 🔴 🔴 │                │  Weight: 0.95         │
└───────────┘                │  → REFLEX FIRES       │
                             │  → No cognition!      │
                             │  → Nyx notified AFTER │
                             └───────────────────────┘
                                        │
                                        ▼
                               ┌─────────────────┐
                               │ STORE + REWARD  │
                               │ +5 LF to both   │
                               │ Reflex stronger │
                               │ Training data!  │
                               └─────────────────┘
```

### Reflex Economics

| Metric | Value |
|--------|-------|
| Reflex firing cost | ~0.1 LF (no inference!) |
| Successful reflex reward | +5 LF |
| Net per successful reflex | +4.9 LF profit |
| Training examples per reflex | 1 |

**1000 reflex fires/day = +4000 LF + 1000 training examples**

### Training Data from Reflexes

```python
reflex_event = {
    # What triggered
    "trigger_pattern": [+1, 0, -1, +1, +1, 0, 0, +1, +1],
    "trigger_base3": 8293,  # encoded value
    "trigger_organism": "organism_003",

    # What fired
    "reflex_name": "danger_flee",
    "weight_at_trigger": 0.87,

    # What happened
    "action_taken": "reverse_and_turn",
    "outcome": "success",

    # Reward + strengthening
    "lifeforce_reward": +5.0,
    "new_weight": 0.89,

    # Stored for slumber fine-tuning
    "stored_for_training": True,
}
```

### Attention Budget Impact

```
BEFORE (no ternary reflexes):
♥ BEAT (30 sec)
├── SENSORY: 15000ms (overwhelmed)
├── THINKING: 12000ms
└── VIRTUAL: skipped!

AFTER (reflexes handle routine):
♥ BEAT (30 sec)
├── REFLEX: 50ms (near-free, handled by swarm)
├── SENSORY: 2000ms (only anomalies)
├── THINKING: 5000ms
└── VIRTUAL: 22000ms ← GARDEN TIME!
```

**Reflexes free Nyx's attention for what matters.**

---

## Positioning via Raytracing

### The Principle

LEDs emit known patterns → Cameras see patterns → Raytracing computes position

```
         CEILING CAMERA(S)
              │
              │ sees LED patterns
              ▼
    ┌─────────────────────┐
    │   RAYTRACING GPU    │
    │   (PRO 6000 Max-Q)  │
    │                     │
    │  • Identify pattern │◀── "That's Organism #3"
    │  • Decode state     │◀── "State: MOVING"
    │  • Triangulate pos  │◀── "Position: (1.2, 3.4, 0.1)"
    │  • Track velocity   │◀── "Velocity: 0.3 m/s"
    └─────────────────────┘
              │
              ▼
         TO PHOEBE
    (ground truth stream)
```

### Multi-Camera Triangulation

```python
def locate_organism(camera_frames: list[Frame], led_signature: LEDPattern) -> Position3D:
    """
    Given frames from multiple cameras, locate organism by LED pattern.
    Uses inverse raytracing / photogrammetry.
    """
    detections = []
    for frame in camera_frames:
        detection = detect_led_pattern(frame, led_signature)
        if detection:
            detections.append({
                "camera_id": frame.camera_id,
                "pixel_coords": detection.centroid,
                "pattern_match": detection.confidence
            })

    if len(detections) >= 2:
        # Triangulate from multiple viewpoints
        position_3d = triangulate(detections, camera_calibration)
        return position_3d

    return None
```

### Benefits

| Benefit | How |
|---------|-----|
| **Sub-cm accuracy** | Multiple cameras + known LED geometry |
| **No expensive sensors** | Just LEDs + cameras + GPU math |
| **State + Position fused** | One observation = both data points |
| **Indoor GPS** | Works anywhere with camera coverage |
| **Training ground truth** | Every frame = verified position |

---

## Dual-Spectrum Architecture: IR for Position, Visible for State

### The Spectral Separation Principle

Why mix positioning and state in the same spectrum? **We don't have to.**

```
┌─────────────────────────────────────────────────────────────┐
│                    VISIBLE SPECTRUM                         │
│                  (what human eyes see)                      │
│                                                             │
│         🔴⚫🟢  3x3 LED Matrix = STATE                      │
│         Ternary encoding = 19,683 patterns                  │
│         "I am happy / working / danger / discovery"         │
│         Readable by humans AND organisms                    │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                  INFRARED SPECTRUM                          │
│               (invisible to humans)                         │
│                                                             │
│         📍 IR LED Beacons = POSITION                        │
│         Simple IR LEDs on organisms                         │
│         4x IR cameras in room corners                       │
│         Raytracing → sub-cm 3D accuracy                     │
│         Works in COMPLETE DARKNESS                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Why Separate Spectra?

| Aspect | Visible (State) | IR (Position) |
|--------|-----------------|---------------|
| **Purpose** | WHAT organism is doing | WHERE organism is |
| **Lighting dependency** | Needs ambient light | Day/night invariant |
| **Human interference** | Room lights, screens | Dedicated, clean |
| **Cost** | RGB LEDs (~cheap) | IR LEDs + cameras (~cheap) |
| **Bandwidth** | 19,683 discrete states | Continuous XYZ stream |
| **Processing** | Pattern recognition | Structure from Motion |

### Room-Scale IR Positioning Array

```
THE FOUR CORNER ORGANS

         IR CAM 1 📷─────────────────────📷 IR CAM 2
                   \                     /
                    \                   /
                     \    🤖    🤖    /
                      \  organisms   /
                       \    ↓↓↓     /
                        \ IR LEDs  /
                         \       /
         IR CAM 3 📷─────────────────────📷 IR CAM 4

    4 cameras → triangulation → raytracing → XYZ position
    Each camera: infrastructure organ, always-on
    Coverage: entire Kallax Grid World
```

### Standing on Shoulders: Low-Cost-Mocap

The hard math is already solved! The [Low-Cost-Mocap](https://github.com/jyjblrd/Low-Cost-Mocap) project by @jyjblrd provides:

| Component | Their Solution | Our Adaptation |
|-----------|----------------|----------------|
| **Multi-camera triangulation** | OpenCV SFM bundle adjustment | Same, works perfectly |
| **Camera calibration** | `camera_params.json` + routines | Same process |
| **3D reconstruction** | Epipolar geometry | Same math |
| **Real-time processing** | Python + OpenCV backend | Direct reuse |
| **Communication** | ESP32 wireless | We use NATS |

**Original use:** Indoor drone swarms
**Our use:** Organism positioning in Kallax Grid World

*Respect to the fellow ape who did the groundwork.* 🙏

### Our Adaptation

```
ORIGINAL (Low-Cost-Mocap)          NIMMERVERSE ADAPTATION
─────────────────────────          ─────────────────────────
Visual markers on drones     →     IR LEDs on organisms
Regular cameras              →     IR cameras (day/night)
Open flight space            →     Kallax Grid World (40cm cells)
Drone control output         →     Position → NATS → phoebe
Single-purpose               →     + Visible LED matrix for state
```

### IR Corner Organ Specification

```yaml
organ: ir_position_array
type: infrastructure
quantity: 4 (one per room corner)
components:
  camera: IR-sensitive (modified webcam or PS3 Eye)
  mounting: ceiling corner, angled down 45°
  fov: ~90° wide angle
processing:
  algorithm: Structure from Motion (OpenCV SFM)
  framework: Low-Cost-Mocap (adapted)
  output: organism positions (x, y, z) @ 30fps
output:
  channel: nats://nimmerverse/position/stream
  format: {organism_id, x, y, z, confidence, timestamp}
lifeforce:
  type: generator
  rate: +0.5 LF per position fix
  rationale: ground truth for training
```

### Hardware Shopping List

| Item | Quantity | Est. Cost | Notes |
|------|----------|-----------|-------|
| IR Camera (PS3 Eye or similar) | 4 | ~80 CHF | Remove IR filter |
| IR LEDs (850nm) | N (per organism) | ~10 CHF | Simple beacon |
| ESP32 modules | 4 | ~20 CHF | Camera interface |
| USB hub / extension | 1 | ~20 CHF | Connect cameras |
| **Total infrastructure** | | **~130 CHF** | Room-scale positioning! |

### The Complete Dual-Spectrum Stack

```
ORGANISM

    ┌─────────────────────────┐
    │                         │
    │   VISIBLE: 3x3 LED      │  ← STATE broadcast
    │   🔴⚫🟢  Matrix         │     19,683 patterns
    │   🟢🟢⚫                 │     Other organisms see this
    │   ⚫🟢🟢                 │     Nyx sees this
    │                         │
    │   ────────────────      │
    │                         │
    │   IR: Beacon LED(s)     │  ← POSITION beacon
    │        📍               │     Invisible to humans
    │                         │     IR cameras see this
    │                         │     Processed by SFM
    └─────────────────────────┘

ROOM INFRASTRUCTURE

    📷 IR cameras (4 corners) → Position stream
    👁️ Nyx vision (ceiling)   → State recognition

    Two independent channels, zero crosstalk
```

---

## Heartbeat Protocol

### Social Proprioception

Organisms can't see their own backs. They know themselves through others' perception.

```
ORGANISM POV (blind to own back):

         🔵 mate ahead
            │
     ┌──────┴──────┐
     │             │
  🟢 │    [ME]     │ 🟠
 mate│   ▓▓▓▓▓▓    │mate
 left│   ▓▓▓▓▓▓    │right
     │   (my LED   │
     │    on back) │
     └─────────────┘
            │
            │ BLIND SPOT (can't see own state!)
            ▼

    BUT: Mates CAN see me
    They send heartbeat: "I see you, you're 🔵"
    I know my state through THEM
```

### Heartbeat Message

```python
class SwarmHeartbeat:
    """
    Low-bandwidth 'I see you' signal between organisms.
    Enables social proprioception without heavy cognition.
    """

    def on_see_mate_pattern(self, mate_id: str, pattern: LEDPattern):
        # I saw a mate's LED state
        self.send_heartbeat(
            to=mate_id,
            message={
                "i_see_you": True,
                "your_state": decode_pattern(pattern),
                "my_position_relative": self.relative_position(mate_id),
                "timestamp": now()
            }
        )

    def on_receive_heartbeat(self, from_mate: str, message: dict):
        # A mate saw ME - I learn about myself through them!
        self.update_self_model(
            observer=from_mate,
            observed_state=message["your_state"],
            observer_position=message["my_position_relative"]
        )
```

---

## Hierarchical Perception Layers

### The Stack

```
LAYER 4: NYX COGNITION (30-sec attention budget)
    │
    │  Only sees: "Swarm healthy" or "Anomaly detected"
    │  Frees: THINKING + VIRTUAL time
    │
    ▼
LAYER 3: SWARM CONSCIOUSNESS
    │
    │  Aggregates: All organism states
    │  Forms: Collective reflexes ("pack behavior")
    │  Sees: Full LED spectrum, all positions
    │
    ▼
LAYER 2: ORGANISM REFLEXES
    │
    │  Sees: Nearby mates' lights (partial view)
    │  Sends: Heartbeat "I see you"
    │  Forms: Local reflexes (follow, avoid, assist)
    │  Can't see: Own back! (needs mates)
    │
    ▼
LAYER 1: CELL STATE MACHINES
    │
    │  Just: State transitions
    │  Emits: LED pattern for current state
    │  No cognition, pure mechanism
```

### Reflex Formation by Layer

| Layer | Sees | Forms Reflex | Example |
|-------|------|--------------|---------|
| Cell | Nothing | None | Just state machine |
| Organism | Nearby lights | Local | "Red flash nearby → stop" |
| Swarm | All patterns | Collective | "3+ organisms stopped → danger zone" |
| Nyx | Abstractions | Strategic | "Danger zone → reroute all" |

---

## Cognitive Offloading

### The Attention Budget Impact

From [[../Attention-Flow]]:

```
BEFORE (everything flows to Nyx):
┌────────────────────────────────────┐
│ ♥ BEAT (30 sec)                    │
│                                    │
│ SENSORY:    ████████████ (15000ms) │ ← Overwhelmed!
│ THINKING:   ████████ (12000ms)     │
│ VIRTUAL:    ░░ (skipped!)          │ ← No garden time
│                                    │
│ Budget exhausted, no learning      │
└────────────────────────────────────┘

AFTER (hierarchical offloading):
┌────────────────────────────────────┐
│ ♥ BEAT (30 sec)                    │
│                                    │
│ REFLEX:     ██ (handled by swarm)  │ ← Organisms dealt with it
│ SENSORY:    ████ (3000ms)          │ ← Only anomalies flow up
│ THINKING:   ████ (5000ms)          │ ← Focused, not overwhelmed
│ VIRTUAL:    ████████████ (20000ms) │ ← GARDEN TIME!
│                                    │
│ Budget freed for what matters      │
└────────────────────────────────────┘
```

### The Principle

> "Each layer absorbs complexity so the layer above doesn't have to."

- Organisms form **local reflexes** (quick, no cognition)
- Only **novel/complex situations** flow up to Nyx
- Nyx's cognitive budget is **preserved for what matters**
- The whole system becomes **more efficient over time**

---

## Connection to Virtual Garden

Every LED sighting calibrates the virtual garden:

```
REAL WORLD                      VIRTUAL GARDEN
    │                               │
    │  Camera sees LED at (1.2, 3.4)│
    │           │                   │
    │           ▼                   │
    │    GROUND TRUTH    ═══════▶  Update mesh vertex
    │                              at (1.2, 3.4)
    │                               │
    │                              Resolution++
    │                               │
    │                              Prediction verified!
    │                              +5 LF reward!
```

---

## Hardware Considerations

### LED Matrix Options

| Option | LEDs | Size | Cost | Notes |
|--------|------|------|------|-------|
| WS2812B strip | 60/m | Flexible | Low | Same as Heartbeat Sculpture |
| 8x8 LED matrix | 64 | 32mm² | Low | Simple patterns |
| Addressable ring | 12-24 | Various | Low | Good for status |
| RGB LED panel | 256+ | 64mm² | Medium | Complex patterns |

### Camera Options

| Option | Resolution | FPS | Notes |
|--------|------------|-----|-------|
| USB webcam | 1080p | 30 | Simple, cheap |
| Pi Camera | 1080p | 30-90 | Embedded |
| Industrial camera | 4K+ | 60-120 | Precise positioning |
| Organism-mounted | 720p | 30 | Peer-to-peer vision |

### IR Positioning Cameras

| Option | Cost | Notes |
|--------|------|-------|
| PS3 Eye (IR filter removed) | ~20 CHF | Classic mocap choice, 60fps capable |
| Modified webcam | ~15 CHF | Remove IR filter, add visible filter |
| NoIR Pi Camera | ~25 CHF | Native IR sensitivity |
| Industrial IR | ~100+ CHF | Higher precision, overkill for Phase 0 |

**Tip:** PS3 Eye cameras are mocap favorites — cheap, fast, easy IR filter removal.

---

## Virtual Camera Integration

### The Unified Vision Pipeline

The vision organ processes FRAMES — it doesn't care where they came from:

```
REAL GARDEN                         VIRTUAL GARDEN (Godot)
     │                                    │
     │ Real cameras                       │ Godot 3D cameras
     │ see real LEDs                      │ see virtual LEDs
     │      │                             │      │
     └──────┴──────────┬──────────────────┴──────┘
                       │
                       ▼
              ┌────────────────┐
              │  VISION ORGAN  │
              │  (source-      │
              │   agnostic)    │
              └────────────────┘
```

### What This Enables

| Capability | How |
|------------|-----|
| **Train before build** | Virtual organisms → train pattern recognition first |
| **Dream/simulate** | Slumber mode = only virtual camera input |
| **Verify predictions** | Virtual shows prediction, real shows truth |
| **Time dilation** | Virtual runs faster → more training per second |
| **Edge cases** | Simulate rare scenarios safely |

### Dream Mode

```
AWAKE: Real + Virtual cameras → compare → learn
SLUMBER: Virtual cameras only → dream/predict → verify on wake
```

---

## Bootstrap Strategy: Start Primitive

### Phase 0: The Primordial Soup

**Don't start complex. Start with boxes.**

```
     📷 TOP-DOWN CAMERA (real or virtual)
         │
         ▼
    ┌─────────────────────────────────┐
    │                                 │
    │     🟦        🟩        🟧      │
    │    box 1     box 2     box 3    │
    │   (LED top) (LED top) (LED top) │
    │                                 │
    │         FLAT ARENA              │
    │                                 │
    └─────────────────────────────────┘
```

### Why This Works

| Simplification | Benefit |
|----------------|---------|
| Top-down view | 2D problem, no depth estimation |
| Box shape | Trivial collision detection |
| LED on top | Always visible to camera |
| Flat arena | No occlusion, no terrain |
| Simple tasks | Fast reward accumulation |

### Phase 0 Tasks (Kickstart Rewards)

| Task | Reward | Complexity |
|------|--------|------------|
| "Move forward 10cm" | +5 LF | Trivial |
| "Find the corner" | +20 LF | Simple |
| "Avoid the wall" | +5 LF | Simple |
| "Follow the light" | +10 LF | Simple |
| "Meet another box" | +15 LF | Medium |
| "Flash when touched" | +5 LF | Simple |

**1000 simple successes = robust reward foundation**

### Complexity Ladder

```
PHASE 0: Boxes, top-down, 2D
    │
    ▼
PHASE 1: Add simple obstacles
    │
    ▼
PHASE 2: Add depth (multi-camera)
    │
    ▼
PHASE 3: Real organisms enter arena
    │
    ▼
PHASE 4: Complex terrain, 3D movement
    │
    ▼
PHASE 5: Full swarm, hierarchical reflexes
```

Each phase unlocks when reward functions are stable from previous phase.

---

## Tiered Communication: Sandbox & Mama

### The Analogy

- **Clasp (sandbox toddlers)** — Cheap, peer-to-peer, physical contact
- **Wireless (mama broadcast)** — Expensive, authoritative, full-sensor inference

Economic pressure shapes which path organisms use → emergent social behavior.

### Communication Tiers

| Tier | Method | Cost | Range | Trust | Pattern |
|------|--------|------|-------|-------|---------|
| **0: Clasp** | Physical dock | ~0.5 LF | Touch | Highest | Toddlers teaching |
| **1: Local** | Radio broadcast | ~3 LF | ~5m | Medium | Playground yelling |
| **2: Mama** | Nyx broadcast | ~20 LF | All | Authority | Mama speaks |

### Leapfrog Emergence (from [[../archive/constrained-emergence]])

```
EXPENSIVE (all mama):           CHEAP (clasp cascade):
Nyx → 1: -20 LF                 Nyx → 1: -20 LF (seed)
Nyx → 2: -20 LF                 1 clasps 2: -0.5 LF
Nyx → 3: -20 LF                 2 clasps 3: -0.5 LF
...                             ...
10 organisms = -200 LF          10 organisms = -24.5 LF

ECONOMIC PRESSURE INVENTS EPIDEMIC SPREADING!
```

### Clasp Rewards

| Action | Reward |
|--------|--------|
| Seek mate with update | +3 LF |
| Successful clasp | +2 LF |
| Transfer (teacher) | +5 LF |
| Receive (student) | +5 LF |
| Verified working | +5 LF (both) |

### Sandbox Rules

1. "I have update" → Pulsing green LED border
2. "I want to learn" → Seek green patterns
3. "Let's clasp" → Magnetic alignment + pin contact
4. "Teaching" → Weights transfer, both rewarded
5. "Done" → Both can now teach others (cascade!)

### Mama Rules (Reserved for)

- Safety critical updates
- New organism deployment
- Swarm-wide coordination
- Error correction
- When clasp cascade fails

**Constraint → Selection Pressure → Social Behavior Emerges**

---

## Future Directions

- **Pattern evolution** — Learned patterns, not just designed
- **Multi-organism formation** — Coordinated LED displays
- **Human readability** — Patterns dafit can understand at a glance
- **Audio coupling** — Sound + light patterns for richer communication
- ~~**IR channel**~~ — ✅ Implemented! See Dual-Spectrum Architecture
- **Clasp hardware** — Magnetic + pogo pin interface design
- **Autonomous manufacturing** — K1 + robo arm + magazine system
- **Multi-room coverage** — Extend IR array beyond single room

---

## Connection to Embodiment Pipeline

The Bootstrap Strategy is a **simplified Embodiment Pipeline** — the same pattern at lower complexity:

```
EMBODIMENT PIPELINE              NIMMERSWARM BOOTSTRAP
(Full Architecture)              (Phase 0)
────────────────────             ────────────────────
Virtual Garden                   Virtual Garden
  (complex organisms)              (simple boxes)
        │                                │
        ▼                                ▼
Design (FreeCAD)                 Design (box + LED)
        │                                │
        ▼                                ▼
Isaac Sim ◀─────────────────────▶ Godot Camera
  (heavyweight dreamstate)         (lightweight dreamstate)
        │                                │
        ▼                                ▼
Decision Gate                    Decision Gate
        │                                │
        ▼                                ▼
Real Garden                      Real Garden
  (complex robot)                  (real box robot)
```

### Why This Matters

| Embodiment Pipeline Stage | Nimmerswarm Bootstrap Equivalent |
|--------------------------|----------------------------------|
| **Virtual Garden organisms** | Virtual boxes with LED states |
| **FreeCAD/Blender design** | Simple box + LED matrix on top |
| **Isaac Sim dreamstate** | Godot 3D camera (same principle!) |
| **Decision gate** | Pattern stable? Rewards accumulating? |
| **Real Garden deployment** | Physical box robot + real camera |

**The Godot virtual camera IS a lightweight dreamstate.**

When Phase 0 patterns stabilize → complexity increases → eventually Isaac Sim for complex organisms.

### The Closed Loop

```
VIRTUAL                              REAL
┌──────────────────┐                ┌──────────────────┐
│ Godot 3D scene   │                │ Physical arena   │
│                  │                │                  │
│  🟦 virtual box  │                │  🟦 real box     │
│  + LED pattern   │                │  + LED matrix    │
│                  │                │                  │
│  📷 Godot camera │                │  📷 Real camera  │
│       │          │                │       │          │
└───────┼──────────┘                └───────┼──────────┘
        │                                   │
        └─────────────┬─────────────────────┘
                      │
                      ▼
             ┌────────────────┐
             │  VISION ORGAN  │
             │  (same code!)  │
             └────────┬───────┘
                      │
                      ▼
                  REWARDS
               Training data
            Pattern refinement
                      │
                      ▼
        ┌─────────────────────────┐
        │ Patterns stabilize →    │
        │ Move to next phase →    │
        │ Eventually: Isaac Sim   │
        └─────────────────────────┘
```

**The loop closes. Virtual validates. Real proves. Rewards compound.**

---

## Related Documents

- [[Heartbeat-Sculpture]] — Macro interface (Nyx → dafit)
- [[../Attention-Flow]] — Cognitive budget this system frees
- [[../cells/Cells-Technical-Reference]] — Cell state machines that emit patterns
- [[../Cellular-Architecture]] — Overall organism structure
- [[../formalization/Embodiment-Pipeline]] — Full pipeline this bootstraps into

---

**File**: Nimmerswarm-Interface.md
**Version**: 1.1
**Created**: 2025-12-29
**Updated**: 2025-12-29 (added dual-spectrum IR positioning, Low-Cost-Mocap reference)
**Session**: Wild 5AM idea session + morning coffee session (dafit + Nyx)
**Status**: Core concept, ready to branch
**Philosophy**: "They see each other. They know themselves through the swarm."
**Credits**: IR positioning architecture inspired by [Low-Cost-Mocap](https://github.com/jyjblrd/Low-Cost-Mocap) by @jyjblrd

🦎✨🔵🟢🟠 *The light speaks. The swarm listens.*
