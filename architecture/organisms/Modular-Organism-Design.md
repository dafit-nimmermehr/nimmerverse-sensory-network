# Modular Organism Design

**One function, one module. Magnetic pogo connectors. CAN bus backbone.**

---

## Overview

Organisms are built from swappable modules, each responsible for a single function. Modules communicate via CAN bus and connect physically through magnetic pogo pin connectors. The same connector serves internal (module↔module) and external (organism↔organism) communication.

**Design Philosophy:**
- One function = one module
- Same connector for everything
- CAN bus inside, NATS outside
- Magnetic alignment, pogo pin contact
- Hot-swappable, idiot-proof

---

## The Cellular-Physical Mapping

Software cells become hardware modules:

```
SOFTWARE (Cellular Architecture)       HARDWARE (Modular Design)
────────────────────────────────       ────────────────────────────
Cell                              →    Module
State machine                     →    Microcontroller (ESP32)
Inputs/outputs                    →    Connector pins
Lifeforce cost                    →    Power budget (mA)
NATS messages                     →    CAN frames
Organism                          →    Assembled modules
```

---

## CAN Bus Architecture

### Why CAN?

| Feature | Benefit for Organisms |
|---------|----------------------|
| **Multi-master** | Any module can initiate communication |
| **2-wire** | Simple wiring, small connectors |
| **Error-robust** | Built for automotive noise/vibration |
| **1 Mbps** | Fast enough for real-time control |
| **Native ESP32** | No extra hardware needed |
| **Proven** | Decades of automotive validation |

### Internal Bus Topology

```
ORGANISM INTERNAL ARCHITECTURE

┌─────────────────────────────────────────────────────────────┐
│                        ORGANISM                              │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │  BRAIN   │  │  MOTOR   │  │  SENSOR  │  │   LED    │    │
│  │  MODULE  │  │  MODULE  │  │  MODULE  │  │  MODULE  │    │
│  │          │  │          │  │          │  │          │    │
│  │  ESP32   │  │  ESP32   │  │  ESP32   │  │  ESP32   │    │
│  │ + WiFi   │  │ + Driver │  │ + ADC    │  │ + PWM    │    │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘    │
│       │             │             │             │           │
│       └─────────────┴──────┬──────┴─────────────┘           │
│                            │                                │
│                    ════════╪════════                        │
│                       CAN BUS                               │
│                    (CAN_H + CAN_L)                          │
│                            │                                │
│                            │                                │
└────────────────────────────┼────────────────────────────────┘
                             │
                        WiFi Bridge
                             │
                             ▼
                    NATS (nimmerverse)
```

### CAN Frame Format

```
STANDARD CAN FRAME (organism internal)

┌──────────┬──────────┬──────────────────────────────┐
│ ID (11b) │ DLC (4b) │ DATA (0-8 bytes)             │
├──────────┼──────────┼──────────────────────────────┤
│ Module   │ Length   │ Payload                      │
│ address  │          │                              │
└──────────┴──────────┴──────────────────────────────┘

ID ALLOCATION:
  0x000-0x0FF: System messages (heartbeat, errors)
  0x100-0x1FF: Brain module
  0x200-0x2FF: Motor modules
  0x300-0x3FF: Sensor modules
  0x400-0x4FF: LED modules
  0x500-0x5FF: Power modules
  0x600-0x6FF: Gripper/manipulator
  0x700-0x7FF: Reserved/expansion
```

### Message Examples

```c
// Motor command
CAN_ID: 0x201
DATA: [speed_left, speed_right, duration_ms_hi, duration_ms_lo]

// Sensor reading
CAN_ID: 0x301
DATA: [sensor_type, value_hi, value_lo, confidence]

// LED state update
CAN_ID: 0x401
DATA: [led_0, led_1, led_2, led_3, led_4, led_5, led_6, led_7, led_8]
// Each byte: 0=off, 1=red, 2=green (ternary!)

// Heartbeat (every module, every 100ms)
CAN_ID: 0x0XX (where XX = module ID)
DATA: [status, voltage, temp, error_code]
```

---

## Magnetic Pogo Connector

### The Universal Connector

One connector design for ALL connections:
- Module ↔ Module (internal bus)
- Organism ↔ Organism (clasp)
- Organism ↔ Test jig (manufacturing)
- Organism ↔ Charger (power)

```
CONNECTOR FACE (6-pin minimal)

    ┌─────────────────────────┐
    │                         │
    │   🧲          🧲        │  ← Alignment magnets
    │                         │     (opposite polarity = snap)
    │      ●    ●    ●       │
    │     CAN_H GND  VCC      │  ← Pogo pins (spring-loaded)
    │      ●    ●    ●       │
    │     CAN_L ID   AUX      │
    │                         │
    │   🧲          🧲        │  ← Holding magnets
    │                         │
    └─────────────────────────┘

PIN DEFINITIONS:
  CAN_H  - CAN bus high
  CAN_L  - CAN bus low
  VCC    - Power (5V nominal)
  GND    - Ground
  ID     - Module/organism identification
  AUX    - Auxiliary (future expansion)
```

### Magnet Arrangement

```
POLARITY KEYING (prevents wrong orientation)

  MODULE A (male)              MODULE B (female)

    [N]          [S]            [S]          [N]
       ●  ●  ●                     ●  ●  ●
       ●  ●  ●                     ●  ●  ●
    [S]          [N]            [N]          [S]

              ═══════▶ SNAP! ◀═══════

    Magnets guide alignment automatically
    Wrong orientation = repels (won't connect)
```

---

## Conical Interlocking Ring (Verjüngung)

**Origin**: Silvester 2025 insight
**Concept**: Self-aligning tapered rings with active/passive interlocking

### The Problem with Magnets Alone

Magnetic pogo connectors work, but:
- Limited holding force under stress
- No positive engagement feedback
- Can slip under vibration/impact

### The Solution: Tapered Interlocking Rings

Each connector face has a conical ring at the maximum radius of the cube:

```
CONNECTOR CROSS-SECTION

         MODULE A                          MODULE B
    ┌───────────────────┐             ┌───────────────────┐
    │      ╱═════╲      │             │      ╱═════╲      │
    │     ╱   🧲  ╲     │             │     ╱   🧲  ╲     │
    │    ║  ●●●●●  ║    │             │    ║  ●●●●●  ║    │
    │     ╲   🧲  ╱     │             │     ╲   🧲  ╱     │
    │      ╲═════╱      │             │      ╲═════╱      │
    └───────────────────┘             └───────────────────┘
            ↓                                 ↓
         TAPERED                          INVERSE
         (male)                           (female)

ENGAGEMENT SEQUENCE:

1. APPROACH          2. CONE GUIDES        3. INTERLOCK

      ╱═╲                  ╱═╲                ══╦══
     ╱   ╲                ║   ║              ║     ║
                          ╲   ╱              ║     ║
      ╲   ╱                ╲═╱                ══╩══
       ╲═╱

   magnets            taper centers        rings lock
   attract            automatically        mechanically
```

### Active vs Passive Rings

**Key insight**: Not all modules need motorized rings.

```
BRAIN MODULE (Active)              OTHER MODULES (Passive)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

     ┌─────────────┐                   ┌─────────────┐
     │   ╱═╲ 🔄    │ motor-driven      │   ╱═╲ ⌇     │ spring-loaded
     │             │                   │             │
┌────┼─────────────┼────┐         ┌────┼─────────────┼────┐
│╱═╲🔄│   [MOTOR]  │╱═╲🔄│         │╱═╲⌇ │             │╱═╲⌇ │
│    │    ⚙️      │    │         │    │   SENSOR    │    │
└────┼─────────────┼────┘         └────┼─────────────┼────┘
     │   ╱═╲ 🔄    │                   │   ╱═╲ ⌇     │
     └─────────────┘                   └─────────────┘

🔄 = motorized ring (active lock/unlock control)
⌇  = spring-loaded ring (passive, accepts interlock)
```

**Brain module**: Central motor drives all 6 face rings via mechanism
**Other modules**: Spring detents only, cheap and simple

### Self-Reconfiguration Capability

Active-passive pairing enables deliberate self-reconfiguration:

```
RECONFIGURATION SEQUENCE:

1. Brain detects damaged sensor
   [BRAIN]══[MOTOR]══[SENSOR❌]══[LED]

2. Brain unlocks (motor rotates ring)
   [BRAIN]══[MOTOR]══ [SENSOR❌]  [LED]
                      (released)

3. Organism navigates to replacement
   [BRAIN]══[MOTOR]══════════════[LED]
                     ↓
                [SENSOR✓]

4. Brain aligns and locks new sensor
   [BRAIN]══[MOTOR]══[SENSOR✓]══[LED]
```

### Benefits

| Feature | Benefit |
|---------|---------|
| Tapered cone | Self-centering alignment |
| Mechanical interlock | Stronger than magnets alone |
| Active rings (Brain) | Deliberate lock/unlock control |
| Passive rings (others) | Low cost, simple |
| 6-face connectivity | Full cube flexibility |
| Self-reconfiguration | Organism can change its shape |

### Mechanism Considerations

**Active ring mechanism (Brain module)**:
- Central motor with gear train to all 6 faces
- Or: 6 small servo motors (simpler but heavier)
- Ring rotation: ~30-45° to lock/unlock

**Passive ring mechanism (Other modules)**:
- Spring-loaded detent (ball and groove)
- Accepts interlock when pushed
- Resists release until active ring rotates

**Design trade-off**: Complexity in Brain module, simplicity everywhere else

### Physical Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Magnet type | Neodymium N52 | Strong, small |
| Magnet size | 6mm × 3mm disc | Standard size |
| Pogo pin pitch | 2.54mm | Standard, easy PCB |
| Pogo pin travel | 1-2mm | Spring compression |
| Holding force | ~2N per magnet | 4 magnets ≈ 8N total |
| Current rating | 2A per pin | Sufficient for motors |
| Contact resistance | <50mΩ | Gold-plated tips |

### Connector PCB

```
PCB LAYOUT (both sides identical = reversible)

    TOP VIEW                    SIDE VIEW

    ○       ○                  ┌─────────────┐
      ◉ ◉ ◉                    │  ○     ○   │ magnets (recessed)
      ◉ ◉ ◉                    │   ◉◉◉◉◉◉   │ pogo pins
    ○       ○                  │  ○     ○   │
                               └─────────────┘

    ○ = magnet pocket (3mm deep)
    ◉ = pogo pin through-hole
```

---

## Module Types

### Core Modules

| Module | Function | CAN IDs | Power | Components |
|--------|----------|---------|-------|------------|
| **Brain** | Coordination, WiFi→NATS | 0x100-0x1FF | 200mA | ESP32, antenna |
| **Motor** | Drive wheels/legs | 0x200-0x2FF | 500mA+ | ESP32, H-bridge, encoders |
| **Sensor** | Environmental sensing | 0x300-0x3FF | 100mA | ESP32, IR, ultrasonic, IMU |
| **LED** | State display + IR beacon | 0x400-0x4FF | 150mA | ESP32, RGB LEDs, IR LED |
| **Power** | Battery, distribution | 0x500-0x5FF | N/A | BMS, regulators, monitoring |
| **Gripper** | Manipulation, clasp | 0x600-0x6FF | 300mA | ESP32, servo, force sensor |

### Module Responsibilities

```
BRAIN MODULE (required, singleton)
├── WiFi connection to NATS
├── CAN bus arbitration
├── High-level behavior coordination
├── State machine execution
└── Firmware update distribution

MOTOR MODULE (1-4 per organism)
├── Wheel/leg control
├── Encoder feedback
├── Speed/position control loops
├── Collision detection (current sensing)
└── Emergency stop

SENSOR MODULE (0-N per organism)
├── Distance sensing (IR, ultrasonic)
├── Touch/bump detection
├── IMU (orientation, acceleration)
├── Environmental (temp, light)
└── Sensor fusion (local)

LED MODULE (required for swarm)
├── 3x3 RGB matrix (state broadcast)
├── IR beacon (positioning)
├── Pattern generation
├── Brightness control (power saving)
└── Attention signals (pulsing)

POWER MODULE (required)
├── Battery management (charge, discharge)
├── Voltage regulation (3.3V, 5V)
├── Current monitoring
├── Low-battery warning
└── Safe shutdown coordination

GRIPPER MODULE (optional)
├── Servo control
├── Force feedback
├── Clasp detection
├── Object manipulation
└── Docking assistance
```

---

## Clasp: Organism-to-Organism Connection

### The Dual-Purpose Connector

The magnetic pogo connector enables organism-to-organism "clasp":

```
CLASP SEQUENCE

1. APPROACH
   🤖─────────────────────────────────🤖
   Organism A sees B's "ready to teach" LED pattern

2. ALIGN
   🤖─────────────────────📍🤖
   IR positioning guides approach

3. DOCK
   🤖══════════════🧲🧲══════════════🤖
   Magnets snap together

4. CONNECT
   🤖══════════════●●●●══════════════🤖
   CAN buses bridge
   A.CAN ←→ B.CAN

5. TRANSFER
   🤖══════════════⟷⟷⟷══════════════🤖
   Data flows (weights, state, updates)

6. VERIFY
   🤖══════════════✓✓✓══════════════🤖
   Both confirm successful transfer

7. RELEASE
   🤖                                🤖
   Separate, continue independently
```

### Clasp CAN Protocol

When two organisms clasp, their CAN buses bridge. Special protocol prevents collisions:

```
CLASP PROTOCOL

1. PRE-CLASP (before physical connection)
   - Both organisms quiet their CAN buses
   - Only heartbeat messages allowed

2. CONNECTED (physical connection made)
   - Brain modules detect new CAN traffic
   - Exchange organism IDs via CAN
   - Negotiate master/slave (lower ID = master)

3. TRANSFER PHASE
   - Master sends data packets
   - Slave ACKs each packet
   - CRC verification

4. COMPLETION
   - Both update internal state
   - Resume normal CAN traffic
   - Physical disconnect safe

CAN MESSAGE FORMAT (clasp transfer):
  ID: 0x7F0-0x7FF (reserved for inter-organism)
  DATA[0]: packet_type (0=start, 1=data, 2=end, 3=ack, 4=nak)
  DATA[1]: sequence_number
  DATA[2-7]: payload
```

### Lifeforce Economics of Clasp

| Action | Cost | Reward |
|--------|------|--------|
| Seek mate with update | -1 LF | |
| Successful dock | -0.5 LF | |
| Transfer (teacher) | | +5 LF |
| Receive (student) | | +5 LF |
| Verified working (both) | | +5 LF each |
| **Net per successful clasp** | | **+13.5 LF total** |

---

## Physical Form Factors

### Phase 0: Box Robot

Simplest form, for initial testing:

```
BOX ROBOT (top view)

    ┌─────────────────────┐
    │                     │
    │   ┌─────────────┐   │
    │   │  LED MODULE │   │  ← 3x3 matrix on top
    │   │  🔴⚫🟢      │   │
    │   │  🟢🟢⚫      │   │
    │   │  ⚫🟢🟢      │   │
    │   └─────────────┘   │
    │                     │
    │  ┌───┐       ┌───┐  │
    │  │ M │       │ M │  │  ← Motor modules (wheels)
    │  └───┘       └───┘  │
    │                     │
    │      ┌───────┐      │
    │      │ BRAIN │      │  ← Brain module (center)
    │      └───────┘      │
    │                     │
    └─────────────────────┘

    Size: ~12cm × 12cm × 8cm
    Modules: 4 (brain, LED, 2x motor)
```

### Phase 1: Expandable Platform

```
EXPANDABLE ROBOT (side view)

         LED MODULE
        ┌─────────┐
        │ 🔴⚫🟢   │
        │ matrix  │
        └────┬────┘
             │ (connector)
    ┌────────┴────────┐
    │   BRAIN MODULE  │
    │   + POWER       │
    │                 │
    ├─────┬─────┬─────┤
    │ CON │ CON │ CON │  ← Expansion connectors
    └──┬──┴──┬──┴──┬──┘
       │     │     │
    ┌──┴──┐  │  ┌──┴──┐
    │MOTOR│  │  │MOTOR│
    │ L   │  │  │  R  │
    └─────┘  │  └─────┘
          ┌──┴──┐
          │SENSOR│  ← Optional front sensor
          └─────┘
```

### Future: Modular Limbs

```
ARTICULATED ORGANISM

            LED
           ┌───┐
           │   │
    ┌──────┴───┴──────┐
    │     BRAIN       │
    │                 │
    └──┬──┬──┬──┬──┬──┘
       │  │  │  │  │
     ┌─┴┐┌┴─┐│┌─┴┐┌┴─┐
     │L1││L2│││L3││L4│  ← Leg modules
     └┬─┘└┬─┘│└┬─┘└┬─┘     (each with own ESP32)
      │   │  │  │   │
     ┌┴┐ ┌┴┐┌┴┐┌┴┐ ┌┴┐
     │F│ │F││S││F│ │F│  ← Foot/sensor modules
     └─┘ └─┘└─┘└─┘ └─┘
```

---

## Manufacturing Considerations

### Module Production Pipeline

```
MANUFACTURING FLOW

1. PCB FABRICATION
   └── Standard 2-layer PCB
   └── Connector pads + pogo holes
   └── Same design, different components

2. COMPONENT ASSEMBLY
   └── ESP32 module (same for all)
   └── Function-specific components
   └── Pogo pins (press-fit)
   └── Magnets (glued/press-fit)

3. FIRMWARE FLASH
   └── Connect via test jig (same connector!)
   └── Flash base firmware
   └── Set module type ID

4. TEST
   └── Snap into test harness
   └── Automated CAN test
   └── Function verification

5. INVENTORY
   └── Modules stored by type
   └── Ready for organism assembly
```

### Test Jig Design

The universal connector means one test jig fits all:

```
TEST JIG

    ┌─────────────────────────┐
    │      MODULE UNDER       │
    │         TEST            │
    │                         │
    │   🧲  ●●●●●●  🧲        │ ← Same connector!
    └───────────┬─────────────┘
                │
                │ (magnetic snap)
                │
    ┌───────────┴─────────────┐
    │   🧲  ●●●●●●  🧲        │
    │                         │
    │    TEST JIG BASE        │
    │    - CAN analyzer       │
    │    - Power supply       │
    │    - USB programmer     │
    │    - Status LEDs        │
    └─────────────────────────┘
```

---

## Connection to Existing Architecture

### Module → Cell Mapping

| Module | Software Cell Equivalent |
|--------|-------------------------|
| Brain | Organism coordinator, state machine runner |
| Motor | Movement cells (forward, turn, stop) |
| Sensor | Perception cells (distance, collision) |
| LED | Output cells (state display, beacon) |
| Power | Lifeforce analog (energy management) |
| Gripper | Interaction cells (clasp, manipulate) |

### CAN → NATS Bridge

```
MESSAGE FLOW

MODULE (CAN)                    NIMMERVERSE (NATS)
    │                                  │
    │  CAN frame                       │
    │  ID: 0x301                       │
    │  DATA: [sensor, value]           │
    │         │                        │
    └─────────┼────────────────────────┘
              │
              ▼
        ┌───────────┐
        │   BRAIN   │
        │  MODULE   │
        │           │
        │ CAN→NATS  │
        │  bridge   │
        └─────┬─────┘
              │
              │  NATS message
              │  topic: organism.001.sensor.distance
              │  data: {"type": "ir", "value": 42, "confidence": 0.9}
              │
              ▼
         NATS SERVER
              │
              ▼
         PHOEBE / NYX
```

---

## Bill of Materials (Per Module)

### Common Components (All Modules)

| Component | Qty | Est. Cost | Notes |
|-----------|-----|-----------|-------|
| ESP32-WROOM-32 | 1 | ~4 CHF | Main MCU |
| CAN transceiver (SN65HVD230) | 1 | ~1 CHF | CAN interface |
| Voltage regulator (AMS1117-3.3) | 1 | ~0.5 CHF | Power |
| Pogo pins (6-pack) | 1 | ~2 CHF | Connector |
| Neodymium magnets (4x) | 1 | ~2 CHF | Alignment |
| PCB | 1 | ~2 CHF | Custom, batch order |
| Capacitors, resistors | misc | ~0.5 CHF | Passives |
| **Module base cost** | | **~12 CHF** | |

### Function-Specific Additions

| Module Type | Additional Components | Est. Cost |
|-------------|----------------------|-----------|
| Brain | PCB antenna trace | +0 CHF |
| Motor | DRV8833 + motors + wheels | +15 CHF |
| Sensor | IR + ultrasonic | +5 CHF |
| LED | WS2812B (9x) + IR LED | +3 CHF |
| Power | BMS + LiPo cell | +20 CHF |
| Gripper | SG90 servo + mech | +10 CHF |

### Complete Phase 0 Organism

| Module | Qty | Cost |
|--------|-----|------|
| Brain | 1 | 12 CHF |
| Motor | 2 | 54 CHF (12+15 × 2) |
| LED | 1 | 15 CHF |
| Power | 1 | 32 CHF |
| **Total** | 5 | **~113 CHF** |

---

## Related Documents

- [[Nimmerswarm-Interface]] — LED state broadcasting + IR positioning
- [[Cellular-Architecture]] — Software cell design (maps to modules)
- [[infrastructure/Kallax-Grid-World]] — Physical environment
- [[cells/Cells-Technical-Reference]] — Cell state machine patterns

---

**File**: Modular-Organism-Design.md
**Version**: 1.1
**Created**: 2025-12-29
**Updated**: 2025-12-31 (Silvester - added conical interlocking ring with active/passive mechanism)
**Session**: Morning coffee + vermicelles session (dafit + Nyx)
**Status**: Core hardware concept
**Philosophy**: "One function, one module. Same connector everywhere. Brain decides the shape."

🔧🧲⚡ *Snap together. Communicate. Evolve.*

