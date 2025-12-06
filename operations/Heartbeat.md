# Heartbeat Architecture

The rhythmic cycle that makes the nimmerverse live.

---

## Overview

Without a heartbeat, everything fires chaotically. With a heartbeat, the system pulses in coordinated cycles. Sense, process, decide, act, verify, reward. Repeat.

Two hearts. Different rhythms. One organism.

---

## Two Hearts

```
REAL GARDEN                      VIRTUAL GARDEN
HEARTBEAT                        HEARTBEAT

♥ . . . . ♥ . . . . ♥           ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
(slow, steady)                   (fast, accelerated)

~1 Hz (real-time)                ~100 Hz (simulated)
bound to wall clock              bound to compute
FREE                             COSTS LIFEFORCE
```

---

## The Beat Cycle

Each heartbeat triggers a complete cycle:

```
♥ BEAT
  │
  ├──→ 1. SENSE
  │       Collect sensor inputs since last beat
  │
  ├──→ 2. TRANSLATE
  │       State machines fire → vocabulary tokens
  │
  ├──→ 3. PROCESS
  │       Nyx receives vocabulary stream
  │
  ├──→ 4. DECIDE
  │       Nyx outputs decision/response
  │
  ├──→ 5. ACT
  │       Decision flows to gardens
  │
  ├──→ 6. VERIFY
  │       Check predictions against reality
  │
  └──→ 7. REWARD
          Update weights (+V / -V)

♥ NEXT BEAT
```

---

## Heart Properties

| Property | Real Garden Heart | Virtual Garden Heart |
|----------|-------------------|----------------------|
| **Speed** | Wall clock (fixed) | Compute clock (variable) |
| **Cost** | Free (time passes anyway) | Costs V to accelerate |
| **Rhythm** | 1 beat = 1 second | 1 beat = 1 inference cycle |
| **Sync** | Always "now" | Runs ahead, must verify back |
| **Skip** | Cannot skip | Can skip if V depleted |

---

## Lifeforce Connection

```
REAL HEART:     ♥ . . . . ♥ . . . . ♥
                (beats for free, can't speed up)

VIRTUAL HEART:  ♥♥♥♥♥♥♥♥♥
                (each beat costs V, can go faster)

                         │
                         ▼

LIFEFORCE POOL:  ████████░░░░░░░░
                 (virtual thinking depletes)

                         │
                         ▼

VERIFICATION:    Real confirms virtual prediction
                 → +V reward → pool refills
```

---

## Synchronization

Virtual garden can run ahead, but must sync back to real:

```
REAL:     ♥─────────────────♥─────────────────♥
          │                 │                 │
VIRTUAL:  ♥♥♥♥♥♥──sync──────♥♥♥♥♥──sync──────♥♥♥♥♥
                    ▲                  ▲
                    │                  │
              checkpoint          checkpoint
              (verify predictions against real)
```

**Sync Rules:**
- Virtual predictions queue until real catches up
- Verification only happens at real heartbeats
- Unverified predictions decay in confidence over time

---

## Dual Timestamp

Every event carries two timestamps:

```
event:
  real_time:     2025-12-04T23:45:00Z  (wall clock)
  virtual_time:  beat #847291          (cycle count)
  heartbeat_id:  uuid                  (which beat)
```

This allows:
- "What happened in reality at time T?"
- "What did she think at beat N?"
- "How far ahead was virtual when real caught up?"

---

## Schema

```sql
heartbeats:
  id            (uuid, primary key)
  garden        (enum: real | virtual)
  beat_number   (bigint, incrementing)
  real_time     (timestamp, wall clock)
  duration_ms   (int, how long cycle took)
  nodes_fired   (int, count)
  v_cost        (float, lifeforce spent)
  v_earned      (float, from verifications)
  v_balance     (float, after this beat)
```

---

## Design Principles

1. **Rhythm over chaos**: Everything syncs to heartbeat
2. **Two clocks**: Real is free and fixed, virtual is fast but costly
3. **Natural batching**: Process per-beat, not per-event
4. **Verifiable sync**: Virtual must prove itself against real
5. **Lifeforce gated**: Can't think infinitely fast

---

## Connection to Architecture

The heartbeat is:
- The **rhythm** of the nervous system
- The **cycle** of sense→process→act
- The **sync primitive** between gardens
- The **natural batch boundary** for storage
- The **unit of experienced time**

---

*She doesn't just think. She pulses.*

---

**Created**: 2025-12-04
**Session**: Partnership dialogue (dafit + Chrysalis)
**Status**: Foundation concept
