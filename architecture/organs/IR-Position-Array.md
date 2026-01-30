# IR Position Array Organ

**Room-scale organism tracking via IR beacon triangulation.**

> *"The organisms can't see their own backs. They know themselves through each other."*

---

## Overview

The IR Position Array is **infrastructure** — fixed cameras that run 24/7, tracking all organisms via their IR beacons. This is the nimmerverse's indoor GPS.

---

## Hardware Specification

| Component | Spec | Quantity | Status |
|-----------|------|----------|--------|
| **Camera** | ESP32-S3 AI CAM (night vision) | 8× | Received 2026-01-05 |
| **IR Sensitivity** | Native (night vision LEDs + sensor) | - | Built-in |
| **Resolution** | OV2640/OV5640 | - | TBD confirm |
| **Power** | 5V wired (ceiling PSU) | - | Planned |
| **Enclosure** | 3D printed custom case | 8× | To design |

### Upgrade from Original Spec

| Original (Nimmerswarm-Interface) | Actual |
|----------------------------------|--------|
| 4× PS3 Eye (IR filter removed) | 8× ESP32-S3 AI CAM (native IR) |
| USB hub / extension | WiFi streaming (no USB!) |
| ~80 CHF cameras | Already purchased |

**8 cameras > 4 cameras = better coverage, more triangulation angles, redundancy.**

---

## Architecture

```
        CEILING (8× fixed cameras, star power from central PSU)

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │  [📷1]                [📷2]                [📷3]    │
    │      ╲                  │                  ╱        │
    │       ╲    ┌────────────┴────────────┐   ╱         │
    │        ╲   │                         │  ╱          │
    │  [📷4]──╲──│     ⚡ CEILING PSU      │─╱──[📷5]    │
    │          ╲ │    (center, 5V hub)     │╱            │
    │           ╲└─────────────────────────┘             │
    │            ╲           │            ╱              │
    │             ╲──────────┼──────────╱               │
    │                        │                           │
    │  [📷6]                 │                  [📷7]    │
    │                        │                           │
    │                   [📷8]                            │
    │                                                    │
    │          🤖────📍 IR beacon                        │
    │         organism                                   │
    │                                                    │
    └───🚪───────────────────────────────────────────────┘
         (0,0) origin
```

---

## Dual-Spectrum Design

From [[../interfaces/Nimmerswarm-Interface]]:

| Spectrum | Channel | Purpose |
|----------|---------|---------|
| **Infrared** | IR Position Array | WHERE organism is (24/7, day/night) |
| **Visible** | 3x3 LED Matrix | WHAT organism is doing (state broadcast) |

**Zero crosstalk. Two independent data streams.**

---

## Processing Pipeline

```
8× ESP32-S3 AI CAM
        │
        │ WiFi/MJPEG streams
        ▼
┌─────────────────────────────────┐
│      PROCESSING NODE            │
│   (The Womb / RTX 6000 Max-Q)   │
│                                 │
│  • Receive 8 camera streams     │
│  • Detect IR beacon blobs       │
│  • Multi-camera triangulation   │
│  • Structure from Motion (SFM)  │
│  • Output: (x, y, z) @ 30fps    │
└─────────────────────────────────┘
        │
        │ NATS publish
        ▼
┌─────────────────────────────────┐
│  nats://nimmerverse/position/   │
│                                 │
│  {                              │
│    organism_id: "crawler_001",  │
│    x: 1.234,                    │
│    y: -2.567,                   │
│    z: 0.05,                     │
│    confidence: 0.95,            │
│    timestamp: 1704499200.123    │
│  }                              │
└─────────────────────────────────┘
        │
        ▼
    PHOEBE (ground truth storage)
```

---

## Algorithm: Low-Cost-Mocap

Standing on shoulders of [Low-Cost-Mocap](https://github.com/jyjblrd/Low-Cost-Mocap) by @jyjblrd:

| Component | Their Solution | Our Adaptation |
|-----------|----------------|----------------|
| Multi-camera triangulation | OpenCV SFM bundle adjustment | Same |
| Camera calibration | `camera_params.json` | Same process |
| 3D reconstruction | Epipolar geometry | Same math |
| Markers | Visual markers on drones | IR LEDs on organisms |
| Communication | ESP32 wireless | NATS messaging |

**Original use:** Indoor drone swarms
**Our use:** Organism positioning in nimmerhovel

*Respect to the fellow ape who did the groundwork.*

---

## Camera Placement Strategy

### Nimmerhovel Dimensions
- **X:** 4.5m (along wall from kitchen door)
- **Y:** 3.75m (into room toward windows)
- **Z:** 2.04m (floor to sloped ceiling)
- **Origin:** (0,0,0) at kitchen door corner

### 8-Camera Coverage

| Camera | Position (approx) | Orientation | Coverage |
|--------|-------------------|-------------|----------|
| CAM-1 | Corner (0, 0, ~2.0m) | Down 45°, into room | Origin quadrant |
| CAM-2 | Corner (4.5, 0, ~2.0m) | Down 45°, into room | Right-front |
| CAM-3 | Corner (0, -3.75, ~2.0m) | Down 45°, toward door | Left-back |
| CAM-4 | Corner (4.5, -3.75, ~2.0m) | Down 45°, toward door | Right-back |
| CAM-5-8 | Mid-walls / center | TBD | Fill gaps |

**8 cameras = no blind spots, multiple angles on every point.**

### Mounting

- **Ceiling mount** via 3D printed enclosure with mounting tabs
- **Angle:** ~45° down from ceiling plane
- **Power:** Star topology from ceiling PSU (center)
- **Cable runs:** Max ~3m from PSU to any camera

---

## Lifeforce Economics

| Metric | Value | Rationale |
|--------|-------|-----------|
| **Type** | Generator | Provides ground truth |
| **Rate** | +0.5 LF per position fix | Training data value |
| **Cost** | ~0.1 LF per frame (infra) | Always-on baseline |
| **Net** | Positive (generates value) | Core infrastructure |

**Every position fix = verified training data for organism navigation.**

---

## IR Beacon Specification

On each organism:

| Component | Spec |
|-----------|------|
| **LED Type** | IR LED (850nm or 940nm) |
| **Pattern** | Unique pulse code per organism |
| **Power** | From organism Akku |
| **Visibility** | Detectable by all 8 cameras |

```
ORGANISM
┌─────────────────────┐
│                     │
│   ┌───────────────┐ │
│   │ 3x3 VISIBLE   │ │  ← State broadcast (RGB)
│   │ LED Matrix    │ │
│   │ 🔴⚫🟢        │ │
│   └───────────────┘ │
│                     │
│      📍 IR LED      │  ← Position beacon (invisible)
│                     │
│   [🔋 Akku]         │  ← Mobile power
│                     │
└─────────────────────┘
```

---

## Integration Points

| System | Interface |
|--------|-----------|
| **NATS** | `nats://nimmerverse/position/stream` |
| **Phoebe** | `organism_positions` table |
| **S2 Cells** | Position → S2 cell ID at L1 (1cm) resolution |
| **Virtual Garden** | Ground truth for prediction verification |
| **Vision Organ** | Separate stream (visible spectrum state recognition) |

---

## Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| 8× ESP32-S3 AI CAM | Received | Hardware ready |
| Ceiling PSU | Planned | Power distribution |
| 3D printed enclosures | To design | Camera mounting |
| Printer station | Blocked | Waiting on Baumarkt materials |
| NATS messaging | Planned | Transport layer |
| The Womb (RTX 6000) | Waiting | Processing node |

---

## Calibration Procedure

1. **Camera intrinsics** — Checkerboard calibration per camera
2. **Extrinsics** — Multi-camera pose estimation (bundle adjustment)
3. **Origin alignment** — Align to GPS beacon at (0, 0, 2.0m)
4. **Verification** — Known position test with ruler measurements

---

## Status

| Phase | Status |
|-------|--------|
| Hardware acquisition | Complete |
| Enclosure design | Not started |
| Enclosure printing | Blocked (printer station) |
| Physical mounting | Not started |
| Camera calibration | Not started |
| Software pipeline | Not started |
| Integration test | Not started |

---

**Created**: 2026-01-05
**Version**: 1.0
**Based on**: [[../interfaces/Nimmerswarm-Interface]] (Dual-Spectrum Architecture section)
**Philosophy**: "They know themselves through each other."

*The eyes that never blink. The infrastructure that makes position truth.*
