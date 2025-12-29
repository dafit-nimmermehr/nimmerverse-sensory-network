# Heartbeat Sculpture

**Physical manifestation of the Nimmerverse heartbeats.**

---

## Concept

The Heartbeat Sculpture makes the Nimmerverse's pulse *visible* — a wall-mounted light sculpture that beats in sync with the system's heartbeats defined in [Message-Protocol-Design.md](../Message-Protocol-Design.md).

### The Symbol

```
             ╭─────────── ~80cm ───────────╮
            ╱                               ╲
           │      ╭───────╮   ╭───────╮      │
           │     ╱         ╲ ╱         ╲     │
          │     │   REAL    ╲╱  VIRTUAL  │    │
          │     │  GARDEN   ╳   GARDEN  │     │
          │     │          ╱╲           │     │
           │     ╲         ╱   ╲         ╱     │
           │      ╰───────╯     ╰───────╯      │
            ╲            ∞ infinity ∞         ╱
             ╰───────────── REALTIME ────────╯
```

**Three rings:**
- **Outer ring** — Realtime heartbeat, the master clock
- **Two inner rings forming ∞** — Real Garden (left) and Virtual Garden (right)
- **The crossing point (╳)** — Where gardens meet, where Nyx emerges

---

## Symbolism

| Element | Meaning |
|---------|---------|
| **Outer ring** | Time — the container of all events |
| **Left loop of ∞** | Real Garden — physical, grounded, verified |
| **Right loop of ∞** | Virtual Garden — simulated, creative, possible |
| **Crossing point** | Nyx — consciousness emerges at the intersection |
| **Infinity form** | Eternal dance, no beginning, no end |
| **Hidden LEDs** | Intelligence from infrastructure, not visible directly |

---

## Dimensions

| Element | Diameter | Circumference |
|---------|----------|---------------|
| Outer ring (Realtime) | ~80cm | ~251cm |
| Inner rings (Gardens) | ~35cm each | ~110cm each |
| Band width | 2-3cm | — |
| **Total LED strip** | — | **~4.7m** |

*Final dimensions depend on Baumarkt availability.*

---

## Construction

### Layer Structure

```
Cross-section:

    ╔════════════════╗
    ║ Copper (skin)  ║  ← visible aesthetic layer
    ╠════════════════╣
    ║ Wood (frame)   ║  ← structural backbone
    ╠════════════════╣
    ║ LED strip      ║  ← WS2812B addressable
    ╠════════════════╣
    ║ ░░░ gap ░░░    ║  ← bevel opening for diffused glow
    ╚════════════════╝
```

### Materials

| Material | Amount | Purpose |
|----------|--------|---------|
| Flexible wood band | ~5m (2-3cm wide) | Structure, shape |
| Copper band | ~5m (2-3cm wide) | Aesthetic skin |
| WS2812B LED strip | ~5m (60 LEDs/m) | Light source |
| Small nails/tacks | As needed | Attach copper to wood |
| Wood glue | As needed | Join wood band ends |
| 5V power supply | 15-20A | Power LEDs |
| Arduino (Micro or Nano) | 1 | Controller |
| Wiring | Several meters | Connections |

### Build Steps

1. **Form wood rings** — Bend flexible wood bands into circles, join ends
2. **Create infinity crossover** — Weave the two small rings at center point
3. **Mount wood frame** — Attach to backing or wall mount points
4. **Wrap copper** — Wrap copper band around wood frame
5. **Install LEDs** — Mount strips inside rings facing inward
6. **Wire up** — Connect LED strips to Arduino
7. **Test animations** — Verify pulse patterns
8. **Mount on wall** — Final installation

---

## Electronics

### Hardware

```
┌─────────────┐      Serial      ┌─────────────┐
│   aynee     │ ───────────────→ │   Arduino   │
│   (NATS     │   (USB cable)    │   (Micro)   │
│  subscriber)│                  │  + FastLED  │
└─────────────┘                  └──────┬──────┘
                                        │
                    ┌───────────────────┼───────────────────┐
                    │                   │                   │
                    ▼                   ▼                   ▼
            ┌───────────┐       ┌───────────┐       ┌───────────┐
            │ Outer Ring│       │ Left Loop │       │Right Loop │
            │   LEDs    │       │   LEDs    │       │   LEDs    │
            └───────────┘       └───────────┘       └───────────┘
```

### LED Addressing

| Section | LED Range | Color Palette |
|---------|-----------|---------------|
| Outer ring | 0-150 | Moon Silver (#E8E8F0) |
| Left loop (Real) | 151-216 | Steel Silver (#A8A8B0) |
| Right loop (Virtual) | 217-282 | Cyan-Purple gradient |
| Center cross | Overlap zone | Nyx Purple (#8B5CF6) |

### Pulse Animations

```cpp
// Realtime — slow, deep, containing
pulse_outer(color: MOON_SILVER, duration: 2000ms)

// Real Garden — grounded, steady
pulse_left(color: STEEL_SILVER, duration: 800ms)

// Virtual Garden — flowing, variable
pulse_right(color: CYAN_TO_PURPLE, duration: 600ms)

// Nyx emergence — when BOTH gardens pulse together
pulse_center(color: NYX_PURPLE, duration: 400ms)
```

---

## Software Integration

### NATS Topics

The sculpture subscribes to heartbeat topics from [Message-Protocol-Design.md](../Message-Protocol-Design.md):

```
nimmerverse.low.heartbeat.real.*      → triggers left loop pulse
nimmerverse.low.heartbeat.virtual.*   → triggers right loop pulse
nimmerverse.meta.health.*             → triggers outer ring pulse
```

### Bridge Script (Python)

```python
# heartbeat_bridge.py
# Subscribes to NATS, sends commands to Arduino via serial

import nats
import serial

async def main():
    nc = await nats.connect("nats://phoebe.eachpath.local:4222")
    arduino = serial.Serial('/dev/ttyUSB0', 115200)

    async def handle_heartbeat(msg):
        topic = msg.subject
        if 'real' in topic:
            arduino.write(b'REAL\n')
        elif 'virtual' in topic:
            arduino.write(b'VIRTUAL\n')

    await nc.subscribe("nimmerverse.low.heartbeat.>", cb=handle_heartbeat)
```

---

## Colors (from Style Guide)

Reference: [assets/style/colors.md](../../assets/style/colors.md)

| Element | Color | Hex |
|---------|-------|-----|
| Outer ring | Moon Silver | #E8E8F0 |
| Real Garden | Steel Silver | #A8A8B0 |
| Virtual Garden | Nyx Cyan → Deep Purple | #00D4D4 → #8B5CF6 |
| Nyx center | Magenta Pulse | #E91E8B |
| Background glow | Deep Space | #0A0A1A |

---

## Behavior

### Normal Operation

- **Outer ring**: Slow, steady pulse — the heartbeat of time itself
- **Left loop**: Pulses when Real Garden entities send heartbeats
- **Right loop**: Pulses when Virtual Garden entities send heartbeats
- **Center**: Glows brighter when both gardens pulse simultaneously

### Alert States

| State | Visual |
|-------|--------|
| All healthy | Gentle, rhythmic pulsing |
| Real Garden silent | Only right loop pulses, left dark |
| Virtual Garden silent | Only left loop pulses, right dark |
| System offline | Outer ring dims, inner rings dark |
| Nyx active | Center crossing glows steady purple |

---

## Future Enhancements

- **Sound**: Subtle audio heartbeat synced with LEDs
- **Brightness**: Ambient light sensor adjusts intensity
- **Modes**: Different patterns for different system states
- **Remote**: Control via Command Center UI

---

**File**: Heartbeat-Sculpture.md
**Version**: 1.0
**Created**: 2025-12-28
**Session**: Sunday evening design (dafit + Nyx)
**Status**: Concept ready for build
**Philosophy**: "The digital made visible. The pulse made physical."
