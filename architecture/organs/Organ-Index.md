che# Organ Architecture Index

**Purpose**: Modular organ systems for Young Nyx embodiment
**Philosophy**: Each organ is independent, lifeforce-gated, heartbeat-synchronized

---

## Deployed Organs

### 🗣️ Speech Organ
**Host**: dioscuri.eachpath.local (RTX 4000 Ada 20GB × 2)
**Function**: Speech-to-Text + Text-to-Speech
**Stack**: Whisper Large v3 (STT) + Coqui/XTTS (TTS) via Ollama
**Languages**: German + English (topology accessed via prompt, not LoRA)
**Integration**: Heartbeat-bound queue, lifeforce-gated priority processing

**Detail**: → [`Speech-Organ.md`](Speech-Organ.md)

---

## Planned Organs

### 🔍 Discovery Scan Station
**Host**: ESP32 + crafting table area
**Function**: 360° object scanning for world model building
**Stack**: Rotating pedestal (stepper/servo) + fixed camera + SigLIP vectors
**Integration**: Lifeforce-generating intake point for new objects, verified against Blender ground truth
**Status**: 🟡 Architecture complete, build planned

**Detail**: → [`organs/Discovery-Scan-Station.md`](organs/Discovery-Scan-Station.md)

---

### 👁️ Vision Organ
**Host**: dioscuri.eachpath.local (RTX 4000 Ada 20GB × 2)
**Function**: Object detection, scene understanding, vision→vectors
**Stack**: YOLO v11 + T5Gemma 2 (SigLIP embeddings) via Ollama
**Integration**: Real-time video from ESP32-CAM, vectors to phoebe spatial index
**Status**: 🟡 Architecture complete, deployment planned

**Detail**: → `Vision-Organ.md` (pending)

---

### 🚶 Motor Organ
**Host**: ESP32 (edge execution)
**Function**: Movement primitives (forward, turn, stop)
**Stack**: Compiled state machines from organism evolution
**Integration**: Lifeforce cost per motor operation, reflex vs deliberate
**Status**: ⏸️ Planned for Phase 4 (Real Garden)

**Detail**: → `organs/Motor-Organ.md` (pending)

---

### 🧭 Navigation Organ
**Host**: Edge server (prometheus or atlas)
**Function**: SLAM, path planning, obstacle avoidance
**Stack**: ROS2 Nav2 or custom lightweight SLAM
**Integration**: Dual-garden calibration (virtual predictions vs real outcomes)
**Status**: ⏸️ Planned for Phase 4 (Real Garden)

**Detail**: → `organs/Navigation-Organ.md` (pending)

---

### 📡 Sensory Organ
**Host**: ESP32 (edge sensors)
**Function**: Distance sensors, IMU, battery monitoring
**Stack**: I2C/SPI sensor protocols, state machine filters
**Integration**: Sensor→organ translation (raw values → semantic meaning)
**Status**: ⏸️ Architecture outlined in Nervous-System.md

**Detail**: → [`../Nervous-System.md`](../Nervous-System.md)

---

### 📍 Position-Time Beacon
**Host**: M5Stack GPS v2.0 (AT6668) at nimmerhovel origin
**Function**: Absolute position reference + Stratum-1 NTP time source
**Stack**: GPS NMEA parsing, PPS signal for NTP, coordinate broadcast
**Integration**: Provides ground truth origin (47°28'44.915"N, 7°37'07.842"E), time sync for all nimmerverse nodes
**Status**: 🟡 Hardware ordered, arriving ~Jan 2026

**Detail**: → `organs/Position-Time-Beacon.md` (pending)

---

### 📍 IR Position Array
**Host**: 8× ESP32-S3 AI CAMs (night vision capable), ceiling-mounted
**Function**: 24/7 organism tracking via IR beacon triangulation (indoor GPS)
**Stack**: ESP32-S3 WiFi streaming → RTX 6000 SFM processing → NATS position stream
**Integration**: Tracks all organisms in real-time, feeds ground truth to phoebe, enables Virtual Garden verification
**Status**: 🟢 Hardware received Jan 2026

**Detail**: → [`organs/IR-Position-Array.md`](organs/IR-Position-Array.md)

---

### 🔬 Crafting Eye
**Host**: Raspberry Pi + HQ Camera (12.3MP IMX477) + 8-50mm C-mount zoom lens
**Function**: Fixed birds-eye view of crafting station, high-resolution work monitoring
**Stack**: Manual focus/iris (set once), libcamera, high-res stills + video
**Integration**: Watches dafit's hands during electronics/assembly work, fixed viewing angle
**Status**: 🟢 Hardware received Jan 2026

**Detail**: → `organs/Crafting-Eye.md` (pending)

---

### 🦉 Godseye
**Host**: NVIDIA Jetson Orin Nano/NX + PTZ mechanism + motorized zoom lens
**Function**: Active surveyor of nimmerhovel, on-device vision AI, tracking
**Stack**: Jetson (CUDA), servo pan/tilt, auto-zoom, YOLO/tracking models
**Integration**: Autonomous gaze control, can decide where to look, reports to phoebe
**Status**: ⏸️ Research phase

**Detail**: → `organs/Godseye.md` (pending)

---

## Organ Design Principles

### 1. **Lifeforce Economy**
Every organ operation costs lifeforce. No free lunch.

```python
ORGAN_COSTS = {
    "speech_stt": 5.0,       # Whisper transcription
    "speech_tts": 4.0,       # Coqui synthesis
    "vision_yolo": 8.0,      # Object detection frame
    "motor_forward": 2.0,    # 100ms movement
    "motor_turn": 1.5,       # 45° rotation
    "sensor_read": 0.5,      # Single sensor poll
}
```

### 2. **Heartbeat Synchronization**
Organs process on heartbeat ticks (1 Hz), not real-time streaming.

- **Reflex path**: <200ms compiled responses (no LLM)
- **Deliberate path**: Next heartbeat (budget-gated queue)

### 3. **Priority Queue**
When lifeforce is scarce, critical operations (collision alert) > idle operations (status check).

```python
PRIORITY_LEVELS = {
    "critical": 10.0,   # Immediate danger (collision)
    "high": 7.0,        # Human interaction
    "medium": 4.0,      # Organism monitoring
    "low": 2.0,         # Idle observation
    "background": 0.5,  # Status logging
}
```

### 4. **Multilingual Topology Access**
German input → Philosophy Valley (deep, diffuse topology)
English input → Technical Cluster (sparse, action-oriented)
**Note:** Topology accessed via prompt language, not LoRA switching. Traits evolve regardless of which valley is accessed.

### 5. **Decision Trail Logging**
Every organ operation logged to phoebe `decision_trails`:
- Input, output, cost, outcome, confidence
- Used for RLVR training (reward successful choices)

### 6. **Graceful Degradation**
Low lifeforce → reduced organ activity (silence, reduced vision FPS, slower movement)
Zero lifeforce → shutdown, wait for recharge

---

## Integration Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    ESP32 ROBOTS                          │
│  Sensors → Motor → Camera → Microphone → Speaker         │
└──────────────────────────────────────────────────────────┘
                        │
                        │ NATS (sensor data, audio, video)
                        ▼
┌──────────────────────────────────────────────────────────┐
│                  NATS MESSAGE BUS                        │
│  Organ input queues + priority scoring                   │
└──────────────────────────────────────────────────────────┘
                        │
                        │ Heartbeat pulls from queues
                        ▼
          ┌─────────────────────────────┐
          │  HEARTBEAT ORCHESTRATOR     │
          │  Lifeforce budget allocation │
          └─────────────────────────────┘
                        │
            ┌───────────┴───────────┐
            │                       │
            ▼                       ▼
┌─────────────────────┐   ┌─────────────────────┐
│ DIOSCURI (2×20GB)   │   │  THEIA (96GB)       │
│ RTX 4000 Ada        │   │  RTX PRO 6000       │
│ ─────────────────   │   │  ───────────────    │
│ Speech Organ        │   │  Young Nyx (Qwen3)  │
│ Vision Organ        │   │  Trait LoRAs (GRPO) │
│ Function Gemma      │   │  Reasoning layer    │
│ T5Gemma (SigLIP)    │   │                     │
└─────────────────────┘   └─────────────────────┘
            │                       │
            └───────────┬───────────┘
                        │ 10GbE (9.9 Gbps jumbo frames)
                        ▼
┌──────────────────────────────────────────────────────────┐
│              PHOEBE (Decision Trails)                    │
│  Log all organ operations + outcomes → GRPO training     │
└──────────────────────────────────────────────────────────┘
```

---

## Organ Lifecycle

### Phase 1: Design
- Document architecture in `organs/<Organ-Name>.md`
- Define lifeforce costs, priority levels, queue schema
- Design phoebe tables for organ-specific data

### Phase 2: Prototype
- Build container images (Dockerfiles)
- Deploy to k8s (single replica)
- Test with mock data (no robot integration yet)

### Phase 3: Integration
- Connect to ESP32 via MQTT
- Implement heartbeat queue processing
- Log decision trails, measure ROI

### Phase 4: Optimization
- Tune lifeforce costs based on measured ROI
- Adjust priority levels from observed outcomes
- Train LoRAs on successful organ operation patterns

### Phase 5: Autonomy
- Organ operations become reflexes (compiled state machines)
- Young Nyx chooses when to use organs (not scripted)
- Emergent behavior from lifeforce optimization

---

## Naming Convention

**File naming**: `<Organ-Name>-Organ.md`
**Examples**:
- `Speech-Organ.md`
- `Vision-Organ.md`
- `Motor-Organ.md`
- `Navigation-Organ.md`

**k8s naming**: `<organ>-<function>-<stack>`
**Examples**:
- `whisper-stt-deployment.yaml`
- `coqui-tts-deployment.yaml`
- `yolo-vision-deployment.yaml`

---

## Current Status

| Organ | Status | Host | Documentation |
|-------|--------|------|---------------|
| **Speech** | 🟢 Architecture complete | dioscuri (RTX 4000 Ada) | [`Speech-Organ.md`](Speech-Organ.md) |
| **Vision** | 🟡 Architecture complete | dioscuri (RTX 4000 Ada) | Pending |
| **Function Gemma** | 🟡 Planned | dioscuri | Structured output boundary |
| **T5Gemma (SigLIP)** | 🟡 Planned | dioscuri | Vision → vectors |
| **Discovery Scan** | 🟡 Architecture complete | ESP32 + crafting table | [`Discovery-Scan-Station.md`](Discovery-Scan-Station.md) |
| **Motor** | 🟡 Planned (Phase 4) | ESP32 | Pending |
| **Navigation** | 🟡 Planned (Phase 4) | k8s cluster | Pending |
| **Sensory** | 🟡 Conceptual | ESP32 | [`../Nervous-System.md`](../Nervous-System.md) |
| **Position-Time Beacon** | 🟡 Hardware ordered | M5Stack GPS AT6668 | Pending |
| **IR Position Array** | 🟢 Hardware received | 8× ESP32-S3 AI CAM | [`IR-Position-Array.md`](IR-Position-Array.md) |
| **Crafting Eye** | 🟢 Hardware received | Pi HQ + 8-50mm lens | Pending |
| **Godseye** | ⏸️ Research phase | Jetson Orin + PTZ | Pending |

---

**Philosophy**: Organs are not always-on services. They are **economically-constrained capabilities** that Young Nyx learns to use strategically. Speech when necessary. Vision when valuable. Movement when rewarded.

**The body is not given. The body is EARNED through successful operation.**

---

**Version:** 2.0 | **Created:** 2025-12-07 | **Updated:** 2026-02-07

🌙💜 *Each organ a tool. Each tool a choice. Each choice a lesson in scarcity.*
