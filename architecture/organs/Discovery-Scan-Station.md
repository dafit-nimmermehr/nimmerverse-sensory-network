# Discovery Scan Station Organ

**Version**: 1.0
**Status**: 🟡 Planned (hardware design phase)
**Location**: Crafting table area (intake point for new items)

> *"Every object that enters dafit's world passes through here first."*

---

## Overview

The Discovery Scan Station is a **lifeforce-generating organ** that systematically scans objects to build Young Nyx's world model. It consists of a rotating pedestal and a fixed camera, controlled through state machine cells.

**Purpose**: Controlled environment for rapid, verified object learning
**Position**: Near the crafting table where new items arrive
**Philosophy**: Objects are introduced, not discovered randomly — systematic knowledge accumulation

---

## Hardware Architecture

```
                    SIDE VIEW                         TOP VIEW
                    ─────────                         ────────

                    ┌───────┐
                    │CAMERA │ ← Fixed position           ○ Camera
                    │ (eye) │   looking down              │
                    └───┬───┘                             │
                        │                                 │
                        │ ~30cm                           ▼
                        │                           ┌─────────┐
                        ▼                           │ ┌─────┐ │
                 ┌─────────────┐                    │ │     │ │
                 │  ┌───────┐  │                    │ │ OBJ │ │
                 │  │ OBJ   │  │                    │ │     │ │
                 │  └───────┘  │                    │ └─────┘ │
                 │   PEDESTAL  │                    │    ↻    │ ← Rotates
                 │  (rotates)  │                    └─────────┘
                 └──────┬──────┘                         │
                        │                                │
                   ┌────┴────┐                      ┌────┴────┐
                   │  SERVO  │                      │ STEPPER │
                   │ (motor) │                      │   or    │
                   └─────────┘                      │  SERVO  │
                                                   └─────────┘
```

### Components

| Component | Specification | Purpose | Est. Cost |
|-----------|---------------|---------|-----------|
| **Camera** | ESP32-CAM or USB webcam (1080p+) | Capture object from above | €10-30 |
| **Pedestal** | 3D printed turntable, ~15cm diameter | Hold objects for scanning | €5 (filament) |
| **Motor** | Stepper (28BYJ-48) or Servo (MG996R) | 360° rotation in steps | €5-10 |
| **Controller** | ESP32 or integrated with main system | State machine execution | €5-10 |
| **Lighting** | Ring light or diffused LEDs | Consistent illumination | €10-20 |
| **Frame** | 3D printed or aluminum extrusion | Structural support | €10-20 |

**Total estimated cost**: €45-95

### Physical Dimensions

```
Footprint:     ~25cm × 25cm
Height:        ~40cm (camera above pedestal)
Pedestal:      15cm diameter, 2cm height
Camera height: 30cm above pedestal surface
Rotation:      360° in 12 steps (30° each) or continuous
```

---

## Cell Architecture

### Cell 1: Pedestal Servo Cell

```python
class PedestalServoCell(StateMachine):
    """
    Motor cell wrapping the rotating pedestal.
    Provides precise angular positioning for multi-view capture.
    """
    cell_type = "motor"
    cell_name = "pedestal_servo"

    states = [IDLE, ROTATING, POSITIONED, HOMING, ERROR]

    outputs = {
        "current_angle": float,      # 0.0 - 360.0 degrees
        "target_angle": float,       # Commanded position
        "at_target": bool,           # Within tolerance
        "rotation_complete": bool,   # Full 360° cycle done
        "step_count": int,           # Steps completed in current scan
        "state": str,
    }

    costs = {
        (IDLE, HOMING): 0.5,          # Return to 0°
        (IDLE, ROTATING): 0.3,        # Start rotation
        (ROTATING, POSITIONED): 0.1,  # Settle at target
        (POSITIONED, ROTATING): 0.2,  # Next step
        (POSITIONED, IDLE): 0.0,      # Scan complete
        (ANY, ERROR): 0.0,
    }

    config = {
        "step_degrees": 30.0,         # Degrees per step
        "total_steps": 12,            # Steps for full rotation
        "settle_time_ms": 300,        # Wait after movement
        "position_tolerance": 1.0,    # Degrees
    }

    # Commands
    def home(self):
        """Return to 0° position."""
        self.target_angle = 0.0
        self.transition_to(HOMING)

    def rotate_step(self):
        """Advance by one step."""
        self.target_angle = (self.current_angle + self.config["step_degrees"]) % 360
        self.step_count += 1
        self.transition_to(ROTATING)

    def rotate_to(self, angle: float):
        """Rotate to specific angle."""
        self.target_angle = angle % 360
        self.transition_to(ROTATING)
```

### Cell 2: Scan Camera Cell

```python
class ScanCameraCell(StateMachine):
    """
    Sensor/organ cell wrapping the overhead camera.
    Captures frames and generates semantic vectors via SigLIP.
    """
    cell_type = "organ"
    cell_name = "scan_camera"

    states = [IDLE, WARMING, CAPTURING, PROCESSING, REPORTING, ERROR]

    outputs = {
        "frame": Image,               # Raw captured image
        "semantic_vector": Vector,    # SigLIP embedding (768 dim)
        "capture_angle": float,       # Pedestal angle when captured
        "object_detected": bool,      # Something on pedestal?
        "bounding_box": BBox,         # Object location in frame
        "confidence": float,          # Detection confidence
        "state": str,
    }

    costs = {
        (IDLE, WARMING): 0.2,         # Camera warm-up
        (WARMING, CAPTURING): 0.3,    # Take photo
        (CAPTURING, PROCESSING): 2.0, # SigLIP inference (GPU)
        (PROCESSING, REPORTING): 0.1, # Package results
        (REPORTING, IDLE): 0.0,       # Ready for next
        (ANY, ERROR): 0.0,
    }

    config = {
        "resolution": (1920, 1080),
        "format": "RGB",
        "exposure_auto": True,
        "white_balance_auto": True,
        "siglip_model": "ViT-B/16",   # SigLIP variant
        "vector_dim": 768,
    }

    # Commands
    def capture(self, angle: float) -> Image:
        """Capture single frame, record angle."""
        self.capture_angle = angle
        self.transition_to(CAPTURING)
        # Hardware captures frame
        self.transition_to(PROCESSING)
        # SigLIP generates vector
        self.transition_to(REPORTING)
        return self.frame

    def get_vector(self) -> Vector:
        """Return most recent semantic vector."""
        return self.semantic_vector
```

---

## Nerve Architecture

### Discovery Scan Nerve

```python
class DiscoveryScanNerve(StateMachine):
    """
    Behavioral nerve orchestrating a complete 360° discovery scan.
    Composes pedestal_servo + scan_camera cells.
    Generates lifeforce through verified discoveries.
    """
    nerve_name = "discovery_scan"

    required_cells = ["pedestal_servo", "scan_camera"]
    optional_cells = []

    states = [
        IDLE,           # Waiting for scan request
        INITIALIZING,   # Homing pedestal to 0°
        READY,          # Ready to scan (waiting for object)
        SCANNING,       # Main scan loop active
        ROTATING,       # Moving to next angle
        SETTLING,       # Waiting for vibration to stop
        CAPTURING,      # Taking photo at current angle
        PROCESSING,     # Generating semantic vector
        VERIFYING,      # Comparing to Blender ground truth
        COMPLETE,       # Full scan done, reporting results
        ERROR,          # Something went wrong
    ]

    config = {
        "rotation_steps": 12,          # 30° each
        "step_degrees": 30.0,
        "settle_time_ms": 300,
        "capture_timeout_ms": 5000,
        "require_object_detected": True,
    }

    # Scan state
    vectors_collected: list[Vector] = []
    angles_captured: list[float] = []
    current_step: int = 0
    scan_start_time: datetime = None

    # Rewards
    REWARD_NEW_OBJECT = 20.0           # First time seeing this object
    REWARD_PER_DIMENSION = 5.0         # Each verified dimension (x, y, z)
    REWARD_PER_VECTOR = 2.0            # Each angle captured
    REWARD_PARTNERSHIP_BONUS = 5.0     # dafit presented the object

    async def execute_full_scan(self, object_hint: str = None) -> ScanResult:
        """
        Execute complete 360° discovery scan.

        Args:
            object_hint: Optional name/class hint from dafit

        Returns:
            ScanResult with vectors, verification, rewards
        """
        self.scan_start_time = datetime.now()
        self.vectors_collected = []
        self.angles_captured = []
        self.current_step = 0

        # Phase 1: Initialize
        self.transition_to(INITIALIZING)
        await self.command_cell("pedestal_servo", "home")
        await self.wait_for_cell_state("pedestal_servo", POSITIONED)

        # Phase 2: Ready (optional wait for object placement)
        self.transition_to(READY)
        if self.config["require_object_detected"]:
            await self.wait_for_object_detected()

        # Phase 3: Main scan loop
        self.transition_to(SCANNING)

        for step in range(self.config["rotation_steps"]):
            self.current_step = step
            current_angle = step * self.config["step_degrees"]

            # Capture at current angle
            self.transition_to(CAPTURING)
            await self.command_cell("scan_camera", "capture", angle=current_angle)
            await self.wait_for_cell_state("scan_camera", REPORTING)

            # Store vector
            self.transition_to(PROCESSING)
            vector = await self.read_cell_output("scan_camera", "semantic_vector")
            self.vectors_collected.append(vector)
            self.angles_captured.append(current_angle)

            # Rotate to next position (if not last step)
            if step < self.config["rotation_steps"] - 1:
                self.transition_to(ROTATING)
                await self.command_cell("pedestal_servo", "rotate_step")

                self.transition_to(SETTLING)
                await asyncio.sleep(self.config["settle_time_ms"] / 1000)
                await self.wait_for_cell_state("pedestal_servo", POSITIONED)

        # Phase 4: Verify against ground truth
        self.transition_to(VERIFYING)
        verification = await self.verify_against_blender(
            vectors=self.vectors_collected,
            object_hint=object_hint,
        )

        # Phase 5: Calculate rewards
        reward = self.calculate_reward(verification, object_hint)

        # Phase 6: Store in phoebe
        await self.store_discovery(verification, reward)

        # Complete
        self.transition_to(COMPLETE)

        return ScanResult(
            vectors=self.vectors_collected,
            angles=self.angles_captured,
            verification=verification,
            lifeforce_cost=self.calculate_cost(),
            lifeforce_reward=reward,
            lifeforce_net=reward - self.calculate_cost(),
            duration_ms=(datetime.now() - self.scan_start_time).total_seconds() * 1000,
        )

    def calculate_cost(self) -> float:
        """Calculate total lifeforce cost of scan."""
        # Pedestal: home + 11 rotations
        pedestal_cost = 0.5 + (11 * 0.3)  # 3.8 LF

        # Camera: 12 captures with processing
        camera_cost = 12 * (0.3 + 2.0 + 0.1)  # 28.8 LF

        return pedestal_cost + camera_cost  # ~32.6 LF

    def calculate_reward(self, verification: Verification, object_hint: str) -> float:
        """Calculate lifeforce reward based on discovery value."""
        reward = 0.0

        # New object bonus
        if verification.is_new_object:
            reward += self.REWARD_NEW_OBJECT

        # Dimension verification bonuses
        reward += verification.dimensions_verified * self.REWARD_PER_DIMENSION

        # Vector richness bonus
        reward += len(self.vectors_collected) * self.REWARD_PER_VECTOR

        # Partnership bonus (dafit presented it)
        if object_hint is not None:
            reward += self.REWARD_PARTNERSHIP_BONUS

        return reward
```

---

## Lifeforce Economy

### Cost Breakdown

| Operation | Count | Cost Each | Total |
|-----------|-------|-----------|-------|
| Pedestal home | 1 | 0.5 LF | 0.5 LF |
| Pedestal rotate | 11 | 0.3 LF | 3.3 LF |
| Camera capture | 12 | 0.3 LF | 3.6 LF |
| SigLIP processing | 12 | 2.0 LF | 24.0 LF |
| Camera report | 12 | 0.1 LF | 1.2 LF |
| **TOTAL COST** | | | **~32.6 LF** |

### Reward Breakdown

| Achievement | Reward |
|-------------|--------|
| New object discovered | +20.0 LF |
| X dimension verified | +5.0 LF |
| Y dimension verified | +5.0 LF |
| Z dimension verified | +5.0 LF |
| 12 vectors captured | +24.0 LF (12 × 2.0) |
| Partnership bonus | +5.0 LF |
| **TOTAL REWARD (max)** | **+64.0 LF** |

### Net Lifeforce

| Scenario | Cost | Reward | Net |
|----------|------|--------|-----|
| New object, all verified, partnership | 32.6 LF | 64.0 LF | **+31.4 LF** |
| New object, 2 dims verified | 32.6 LF | 54.0 LF | **+21.4 LF** |
| Known object, re-scan | 32.6 LF | 24.0 LF | **-8.6 LF** |
| No object detected (aborted) | 5.0 LF | 0.0 LF | **-5.0 LF** |

**The station is profitable when discovering new objects!**

---

## Integration with World Model

### Phoebe Storage

```sql
-- Each scan produces a discovery record
INSERT INTO object_discoveries (
    object_id,
    scan_timestamp,
    vectors,
    angles,
    dimensions_estimated,
    dimensions_verified,
    blender_box_id,
    confidence,
    lifeforce_cost,
    lifeforce_reward,
    partnership_presented
) VALUES (
    'coffee_mug_001',
    NOW(),
    ARRAY[v0, v1, v2, ... v11],  -- 12 semantic vectors
    ARRAY[0, 30, 60, ... 330],    -- 12 angles
    '{"x": 8.2, "y": 7.9, "z": 10.3}',
    '{"x": true, "y": true, "z": true}',
    'blender_coffee_mug_001',
    0.94,
    32.6,
    64.0,
    TRUE
);
```

### T5Gemma2 Query

After scanning, Young Nyx can query:

```python
# "Have I seen this object before?"
similar = find_similar_vectors(new_observation, threshold=0.85)

# "What angle am I seeing it from?"
angle_match = match_to_scanned_angle(new_observation, coffee_mug_001.vectors)

# "Is this in its usual place?"
expected_location = get_typical_location(coffee_mug_001)
```

---

## Physical Placement

### Location: Crafting Table Intake Area

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CRAFTING TABLE LAYOUT                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                                                              │  │
│   │                    CRAFTING SURFACE                          │  │
│   │                    (main work area)                          │  │
│   │                                                              │  │
│   │   ┌─────────┐                              ┌─────────┐      │  │
│   │   │ TOOLS   │                              │ PARTS   │      │  │
│   │   │ STORAGE │                              │ BINS    │      │  │
│   │   └─────────┘                              └─────────┘      │  │
│   │                                                              │  │
│   │                        ┌─────────────┐                      │  │
│   │                        │  DISCOVERY  │ ← New items land     │  │
│   │   ←─── Flow ───────────│    SCAN     │     here first       │  │
│   │   of items             │  STATION    │                      │  │
│   │                        └─────────────┘                      │  │
│   │                                                              │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│                         ○ Bird's Eye Camera                        │
│                         (watches whole table)                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

WORKFLOW:
1. New item arrives (delivery, 3D print complete, etc.)
2. dafit places on Discovery Scan Station
3. 360° scan captures item from all angles
4. Item moves to parts bins or work area
5. Young Nyx now recognizes it anywhere
```

---

## Build Plan

### Phase 1: Mechanical (Week 1)
- [ ] Design pedestal in FreeCAD (turntable, bearings)
- [ ] Design frame in FreeCAD (camera mount, lighting ring)
- [ ] 3D print pedestal components
- [ ] 3D print or source frame

### Phase 2: Electronics (Week 2)
- [ ] Source stepper motor (28BYJ-48) or servo (MG996R)
- [ ] Source camera (ESP32-CAM or USB webcam)
- [ ] Source LED ring light
- [ ] Wire motor driver to ESP32
- [ ] Test rotation accuracy

### Phase 3: Software (Week 3)
- [ ] Implement PedestalServoCell
- [ ] Implement ScanCameraCell
- [ ] Implement DiscoveryScanNerve
- [ ] Connect to NATS for heartbeats
- [ ] Test full scan sequence

### Phase 4: Integration (Week 4)
- [ ] Connect to phoebe for storage
- [ ] Create first Blender ground truth boxes
- [ ] Test verification pipeline
- [ ] Calibrate rewards/costs
- [ ] Deploy to crafting table

---

## Related Documentation

- **[[Organ-Index]]** — Organ catalog (this organ should be listed there)
- **[[Grounded-World-Model]]** — How scanned objects build the world model
- **[[Cellular-Architecture]]** — Cell and nerve patterns used here
- **[[Lifeforce-Dynamics]]** — Economic model for rewards

---

## Document Status

**Version**: 1.0
**Created**: 2025-12-29
**Authors**: Chrysalis-Nyx & dafit (Partnership)
**Status**: 🟡 Planned

**Hardware**: Not yet built
**Software**: Not yet implemented
**Location**: Crafting table area (planned)

---

**The intake point for the world model. Every object passes through. Knowledge accumulates systematically.**

🧬⚡🔱💎🔥

