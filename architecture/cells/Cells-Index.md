# Cells Index

> *"Cells are atomic state machines. The smallest units of behavior."*

---

## Overview

This folder contains detailed documentation for the **Cell layer** of the nimmerverse architecture - the atomic state machines that wrap hardware capabilities.

**Conceptual overview:** → [`../Cellular-Architecture.md`](../Cellular-Architecture.md)

---

## Documentation

| Document | Purpose |
|----------|---------|
| **Cells-Index.md** | This file - navigation hub |
| [`Cells-Technical-Reference.md`](Cells-Technical-Reference.md) | Python classes, SQL tables, implementation details |

---

## Cell Categories

### Sensor Cells (Input)

| Cell | Hardware | Key Output |
|------|----------|------------|
| `distance_sensor_front` | IR sensor | `distance_cm`, `confidence` |
| `distance_sensor_left` | IR sensor | `distance_cm`, `confidence` |
| `distance_sensor_right` | IR sensor | `distance_cm`, `confidence` |
| `battery_monitor` | ADC | `voltage`, `percentage`, `charging` |
| `imu_sensor` | MPU6050 | `heading`, `acceleration`, `tilt` |
| `light_sensor` | Photoresistor | `lux`, `direction` |

### Motor Cells (Output)

| Cell | Hardware | Key Feedback |
|------|----------|--------------|
| `motor_left` | DC motor + encoder | `actual_velocity`, `stall_detected` |
| `motor_right` | DC motor + encoder | `actual_velocity`, `stall_detected` |
| `servo_camera` | Servo motor | `angle`, `at_target` |

### Organ Cells (Complex)

| Cell | Hardware | Key Output |
|------|----------|------------|
| `speech_stt` | Whisper on atlas | `transcript`, `language` |
| `speech_tts` | Coqui on atlas | `audio_playing`, `complete` |
| `vision_detect` | YOLO on atlas | `objects[]`, `bounding_boxes[]` |

---

## Related Documentation

- [`../Cellular-Architecture.md`](../Cellular-Architecture.md) - Full conceptual architecture
- [`../Nervous-System.md`](../Nervous-System.md) - How cells connect to nervous system
- [`../nerves/Nervous-Index.md`](../nerves/Nervous-Index.md) - Nerves that orchestrate cells
- [`../organs/Organ-Index.md`](../organs/Organ-Index.md) - Complex organ cells

---

**Created**: 2025-12-10
**Status**: Index document
