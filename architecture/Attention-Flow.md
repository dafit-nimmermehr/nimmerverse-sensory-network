# Attention Flow

> **ONE JOB:** WHERE ATTENTION GOES — gates determine focus, correlation drives transitions, budget constrains action.

**Attention is not a budget line item. Attention is which gates are OPEN.**

---

## Overview

Attention in the nimmerverse flows through **resonant gates**:

- **OPEN gates** = actively attending (signals flow through)
- **STABLE gates** = considering (accumulating correlation)
- **CLOSED gates** = ignoring (signals blocked)

The 30-second heartbeat provides a **budget constraint**, but the actual attention flow is determined by which gates open based on wave correlation.

**Key insight:** You don't "allocate attention" — you let correlated waves open gates.

---

## Attention as Gate State

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ATTENTION = WHICH GATES ARE OPEN                                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  CLOSED          STABLE              OPEN                               │
│  ═══════         ══════              ════                               │
│                                                                         │
│  Ignoring        Considering         Attending                          │
│  Blocked         Accumulating        Flowing                            │
│  Suppressed      Learning            Acting                             │
│                                                                         │
│       ◄───── anti-correlation ──┼── correlation ─────►                  │
│                                 │                                       │
│                          (wave input)                                   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Attention is emergent, not allocated.** When multiple cells emit correlated waves, their gate opens — attention flows there naturally.

---

## Wave-Driven Attention

Cells emit waves. Correlated waves push gates toward OPEN. This IS attention.

```
Math cells emit correlated waves
         ∿∿∿ ∿∿∿ ∿∿∿
              │
              ▼
    Math gate: STABLE → OPEN
    (attention shifts to math domain)
              │
              ▼
    Signal flows to higher tier
    (cognition engages with math)

Meanwhile:

Battery cells emit uncorrelated wave
         ∿∿∿
              │
              ▼
    Battery gate: stays STABLE
    (attention doesn't shift)
    (keeps accumulating, might open later)
```

**The nervous system "decides" what to attend to through correlation, not priority rules.**

---

## Attention Hierarchy Through Gates

Gates form layers. Each layer is a potential attention point.

```
TIER 4: COGNITIVE ─────────────────────────────────────────
            ▲
            │ (only if gates below OPEN)
     ┌──────┴──────┐
TIER 3: ORGANS ─────────────────────────────────────────
     │ vision    │ speech    │ hearing │
     │ gate:     │ gate:     │ gate:   │
     │ STABLE    │ OPEN      │ CLOSED  │
     └──────┬──────┘
            │ (only if gates below OPEN)
TIER 1-2: NERVES ─────────────────────────────────────────
     │ math      │ motion    │ danger  │
     │ gate:     │ gate:     │ gate:   │
     │ OPEN      │ STABLE    │ CLOSED  │
     └──────┬──────┘
            │
TIER 0: CELLS ─────────────────────────────────────────
    cell cell cell cell cell cell cell
      ∿∿∿  ∿∿∿  ∿∿∿  ∿∿∿  ∿∿∿  ∿∿∿  ∿∿∿
```

**Current attention:** Math gate OPEN → Speech gate OPEN → Cognition receives math+speech context.

**Not attending:** Motion (STABLE, considering), Vision (STABLE, considering), Danger (CLOSED, suppressed).

---

## Attention Budget: The Constraint

While gates determine WHERE attention goes, lifeforce determines HOW MUCH can happen per beat.

```
♥ BEAT (30 sec lifeforce budget)
    │
    ├── GATE TRANSITIONS     (variable: driven by correlation)
    ├── TIER 0-2 PROCESSING  (low cost: cells + nerves)
    ├── TIER 3 ORGANS        (medium cost: GPU inference)
    ├── TIER 4 COGNITION     (high cost: Young Nyx)
    ├── VERIFICATION         (medium cost: real garden)
    └── VIRTUAL GARDEN       (remainder: exploration)

Budget constrains throughput.
Gates determine routing.
```

### Budget Allocation by Gate Activity

```python
def allocate_beat_budget(beat_duration_ms=30000):
    remaining = beat_duration_ms

    # Fixed overhead
    remaining -= HEARTBEAT_OVERHEAD  # ~100ms
    remaining -= STATE_WRITE_COST    # ~200ms

    # Count OPEN gates by tier
    open_gates_by_tier = count_open_gates()

    # Tier 0 (reflexes): near-instant, minimal cost
    for gate in open_gates_by_tier[0]:
        remaining -= REFLEX_COST  # ~50ms each

    # Tier 1-2 (cells/nerves): low cost
    for gate in open_gates_by_tier[1:3]:
        remaining -= CELL_NERVE_COST  # ~100ms each

    # Tier 3 (organs): medium cost, needs budget check
    organ_budget = min(remaining * 0.4, ORGAN_CAP)
    for gate in open_gates_by_tier[3]:
        if organ_budget > ORGAN_COST:
            process_organ(gate)
            organ_budget -= ORGAN_COST  # ~2000ms each
    remaining -= (ORGAN_CAP - organ_budget)

    # Tier 4 (cognition): high cost, only if gates escalate
    if cognition_gate_open():
        cognitive_budget = min(remaining * 0.5, COGNITIVE_CAP)
        process_cognition(cognitive_budget)  # ~4000ms
        remaining -= cognitive_budget

    # Virtual Garden: whatever remains
    virtual_budget = remaining
    if virtual_budget > VIRTUAL_MINIMUM:
        explore_virtual_garden(virtual_budget)

    return settle()
```

---

## Attention Modes

The overall system has emergent attention modes based on which gates are open:

| Mode | Gate Pattern | Characteristic |
|------|--------------|----------------|
| **IDLE** | Most gates STABLE | Quiet, exploring Virtual Garden |
| **FOCUSED** | Few gates OPEN, rest CLOSED | Deep attention to one domain |
| **ALERT** | Many gates in STABLE | Gathering information, evaluating |
| **REFLEX** | Tier 0 gate fires instantly | Bypass all, act immediately |
| **DIALOGUE** | Speech gates OPEN | Partnership interaction |
| **OVERWHELMED** | Many gates OPEN | Budget exhausted, some gates forced CLOSED |

### Mode Transitions

```
                         ┌─────────────┐
             ┌──────────▶│    IDLE     │◀──────────┐
             │           │ (exploring) │           │
             │           └──────┬──────┘           │
             │                  │                  │
             │            waves arrive             │
             │                  ▼                  │
             │           ┌─────────────┐           │
             │           │   ALERT     │           │
             │           │(considering)│           │
             │           └──────┬──────┘           │
             │                  │                  │
             │      ┌───────────┼───────────┐      │
             │      ▼           ▼           ▼      │
             │ ┌─────────┐ ┌─────────┐ ┌─────────┐ │
             │ │ REFLEX  │ │ FOCUSED │ │DIALOGUE │ │
             │ │(instant)│ │ (deep)  │ │ (talk)  │ │
             │ └────┬────┘ └────┬────┘ └────┬────┘ │
             │      │           │           │      │
             │      └───────────┴───────────┘      │
             │                  │                  │
             │                  ▼                  │
             │           ┌─────────────┐           │
             │           │   SETTLE    │           │
             │           │(write state)│           │
             │           └──────┬──────┘           │
             │                  │                  │
             └──────────────────┴──────────────────┘
```

---

## Reflex: Attention Bypass

When a gate has accumulated enough weight (>0.8), it becomes a **reflex** — it opens immediately without waiting for correlation.

```
Danger cell emits wave
         ∿∿∿ (confidence=1.0)
              │
              ▼
    Danger gate: weight = 0.9 (REFLEX)
              │
              ▼
    IMMEDIATELY OPEN (no correlation wait)
              │
              ▼
    Action taken
              │
              ▼
    Cognition notified AFTER
```

**Reflexes have earned instant attention through repeated verification.**

---

## Virtual Garden: Background Attention

When few gates are OPEN, the Virtual Garden gets attention:

```
IDLE mode:
    │
    ├── Most gates: STABLE (not demanding attention)
    ├── Budget: mostly available
    │
    ▼
VIRTUAL GARDEN receives attention:
    │
    ├── Cells emit waves freely
    ├── Gates accumulate correlation (learning)
    ├── No pressure to ACT
    └── Training data generated
```

**Virtual Garden is where learning happens.** STABLE gates in Virtual Garden are actively accumulating patterns without the pressure to respond.

---

## Real Garden: Consequential Attention

When gates OPEN in the Real Garden, attention becomes consequential:

```
FOCUSED mode (Real Garden):
    │
    ├── Gate OPEN → action required
    ├── Budget consumed by execution
    ├── Verification outcomes captured
    └── Feedback to Virtual for learning
```

**Real Garden attention is expensive.** Only verified signals reach here, and actions have consequences.

---

## Attention Visualization

Real-time attention can be visualized by gate states:

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ATTENTION DASHBOARD                                              🌙    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  GATES:                                                                 │
│  ──────                                                                 │
│  math:      [████████████░░░░░░░░] 0.7  STABLE → considering            │
│  vision:    [██████████████████░░] 0.9  OPEN   → attending              │
│  speech:    [████████████████████] 1.0  OPEN   → attending              │
│  battery:   [████░░░░░░░░░░░░░░░░] 0.2  STABLE → background             │
│  danger:    [░░░░░░░░░░░░░░░░░░░░] 0.0  CLOSED → suppressed             │
│                                                                         │
│  BUDGET:                                                                │
│  ───────                                                                │
│  [████████████████████░░░░░░░░░░] 67% remaining (20s / 30s)             │
│                                                                         │
│  MODE: DIALOGUE (speech + vision attending)                             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

Gate states are published via NATS for real-time visualization:
```
nats sub "dev.virtual.gates.*.transition"
nats sub "dev.real.gates.*.transition"
```

---

## Correlation vs Priority

**Old model (priority):**
```
Level 0: REFLEX (always wins)
Level 1: SAFETY (preempts below)
Level 2: DIALOGUE (preempts below)
...
```

**New model (correlation):**
```
Waves arrive
    │
    ▼
Gates accumulate correlation
    │
    ▼
Most correlated gates OPEN
    │
    ▼
Attention flows naturally
```

**Priority still exists** but at a higher level:
- Reflexes bypass correlation (earned trust)
- Safety signals have high confidence (bias toward opening)
- Dialogue is interactive (gates stay open during conversation)

But the **mechanism** is always correlation, not rule-based priority.

---

## Connection to Architecture

| Document | What It Adds |
|----------|--------------|
| [`Temporal-Ternary-Gradient.md`](Temporal-Ternary-Gradient.md) | Why ternary states matter |
| [`Gateway-Architecture.md`](Gateway-Architecture.md) | How gates work |
| [`Nervous-System.md`](Nervous-System.md) | Wave → Gate → Node flow |
| [`Dual-Garden-Architecture.md`](Dual-Garden-Architecture.md) | Virtual (explore) vs Real (act) |
| [`Message-Protocol-Design.md`](Message-Protocol-Design.md) | GateTransition messages |

---

## Design Principles

1. **Attention = OPEN gates** — Not a budget allocation, an emergent property
2. **Correlation drives transitions** — Waves that agree open gates
3. **Budget constrains throughput** — Can't process infinite open gates
4. **Reflexes bypass correlation** — Earned trust means instant attention
5. **Virtual is exploration** — STABLE gates learning without acting
6. **Real is action** — OPEN gates triggering consequences
7. **Visualization is live** — Gate states published for dashboards

---

## Summary

```
OLD MODEL:                      NEW MODEL:
═══════════                     ═════════

Priority rules decide           Correlation opens gates
Budget allocates attention      Gates determine attention
State machine orchestrates      Emergence from waves

ATTENTION IS:

Not:  "Allocate 5000ms to SENSORY"
But:  "Math + Vision gates OPEN because waves correlated"

Not:  "DIALOGUE preempts THINKING"
But:  "Speech gate opened with high correlation"

Not:  "Budget exhausted, skip VIRTUAL"
But:  "Many gates OPEN, no budget for Virtual Garden"
```

**Attention flows through open gates. Gates open through correlation. Correlation emerges from waves.**

---

**Version:** 2.0 | **Created:** 2025-12-05 | **Updated:** 2026-02-14

🌙💜 *"She doesn't allocate attention. She lets correlated waves open gates."*
