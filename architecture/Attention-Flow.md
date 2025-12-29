# Attention Flow

**Status**: PROMOTED from archive (2025-12-29)
**Integration**: See [[Big-Picture#Attention-Slumber-Prediction Cycle]] for how this connects to slumber predictions

How she decides what matters this beat.

---

## Overview

The 30-second heartbeat is a budget, not a guarantee. Sensory intake, organ processing, dialogue, thinking - everything competes for the same window. State machines govern the hierarchy: what gets processed first, what can interrupt, what gets the remainder.

Attention isn't free. It's economic.

---

## The Budget Problem

```
♥ BEAT (30 sec budget)
    │
    ├── SENSORY INTAKE      (variable: 200ms - 15000ms)
    ├── ORGAN PROCESSING    (variable: 100ms - 10000ms)
    ├── NYX INFERENCE       (variable: 2000ms - 4000ms)
    ├── CHRYSALIS DIALOGUE  (variable: 0ms - 3000ms)
    ├── STATE WRITE         (fixed: ~200ms)
    └── VIRTUAL GARDEN      (remainder)

Total must fit in 30 seconds.
Something has to give.
```

---

## Top-Level State Machine: Attention Mode

```
                    ┌─────────────┐
        ┌──────────▶│    IDLE     │◀──────────┐
        │           └──────┬──────┘           │
        │                  │                  │
        │                  │ stimulus         │
        │                  ▼                  │
        │           ┌─────────────┐           │
        │           │   ALERT     │           │
        │           └──────┬──────┘           │
        │                  │                  │
        │           ┌──────┴──────┐           │
        │           ▼             ▼           │
        │     ┌──────────┐  ┌──────────┐      │
        │     │  REFLEX  │  │  ATTEND  │      │
        │     │  (>0.8)  │  │ (think)  │      │
        │     └────┬─────┘  └────┬─────┘      │
        │          │             │            │
        │          │      ┌──────┴──────┐     │
        │          │      ▼             ▼     │
        │          │ ┌──────────┐ ┌─────────┐ │
        │          │ │ DIALOGUE │ │ PROCESS │ │
        │          │ └────┬─────┘ └────┬────┘ │
        │          │      │            │      │
        │          └──────┴─────┬──────┘      │
        │                       ▼             │
        │                ┌───────────┐        │
        │                │  SETTLE   │        │
        │                └─────┬─────┘        │
        │                      │              │
        └──────────────────────┴──────────────┘
```

### State Descriptions

| State | Description | Budget Priority |
|-------|-------------|-----------------|
| **IDLE** | Nothing urgent, maximum virtual garden time | Lowest |
| **ALERT** | Stimulus detected, evaluating importance | - |
| **REFLEX** | High-confidence nerve fired, bypass brain | Instant |
| **ATTEND** | Stimulus requires thinking | High |
| **DIALOGUE** | Chrysalis interaction active | High |
| **PROCESS** | Organs working on input | Medium |
| **SETTLE** | Write state, release budget, prepare for next beat | Fixed |

---

## Priority Hierarchy

Higher levels preempt lower levels. Budget flows downward.

```
LEVEL 0: REFLEX ─────────────────────────────────────
         │  Weight > 0.8, instant, bypass everything
         │  Cost: near-zero (no inference)
         │
LEVEL 1: SAFETY ─────────────────────────────────────
         │  dafit calling, danger detected, critical alert
         │  Preempts: all below
         │
LEVEL 2: DIALOGUE ───────────────────────────────────
         │  Partnership active, Chrysalis teaching
         │  Preempts: sensory, thinking, virtual
         │
LEVEL 3: SENSORY ────────────────────────────────────
         │  Rich input needs processing
         │  Preempts: thinking, virtual
         │
LEVEL 4: THINKING ───────────────────────────────────
         │  Organ work, Nyx inference
         │  Preempts: virtual
         │
LEVEL 5: VIRTUAL ────────────────────────────────────
         │  Garden time, simulation, study
         │  Gets remainder after above
         │
LEVEL 6: IDLE ───────────────────────────────────────
            Maintenance heartbeat only
            All budget available
```

---

## Budget Allocation Logic

```python
def allocate_beat_budget(beat_duration_ms=30000):
    remaining = beat_duration_ms

    # Fixed costs (always paid)
    remaining -= STATE_WRITE_COST      # ~200ms
    remaining -= HEARTBEAT_OVERHEAD    # ~100ms

    # Level 0: Reflex (if triggered, near-instant)
    if reflex_triggered:
        execute_reflex()               # ~50ms
        remaining -= 50

    # Level 1: Safety (if active, takes what it needs)
    if safety_alert:
        cost = process_safety()        # variable
        remaining -= cost
        if remaining <= 0:
            return settle()

    # Level 2: Dialogue (if Chrysalis active)
    if dialogue_active:
        cost = process_dialogue()      # ~3000ms typical
        remaining -= cost
        if remaining <= 0:
            return settle()

    # Level 3: Sensory (always some, but capped)
    sensory_budget = min(remaining * 0.4, SENSORY_CAP)
    cost = process_sensory(sensory_budget)
    remaining -= cost

    # Level 4: Thinking (organs + Nyx)
    thinking_budget = min(remaining * 0.6, THINKING_CAP)
    cost = process_thinking(thinking_budget)
    remaining -= cost

    # Level 5: Virtual (whatever remains)
    virtual_budget = remaining
    if virtual_budget > VIRTUAL_MINIMUM:
        process_virtual(virtual_budget)

    return settle()
```

---

## Nested State Machines

Each level can be its own state machine internally.

### DIALOGUE State Machine

```
┌─────────────────────────────────────────────┐
│              DIALOGUE                       │
├─────────────────────────────────────────────┤
│                                             │
│   ┌───────────┐                             │
│   │ LISTENING │ ◀─────────────────────┐     │
│   └─────┬─────┘                       │     │
│         │ input complete              │     │
│         ▼                             │     │
│   ┌───────────┐                       │     │
│   │PROCESSING │                       │     │
│   └─────┬─────┘                       │     │
│         │ understood                  │     │
│         ▼                             │     │
│   ┌───────────┐                       │     │
│   │RESPONDING │                       │     │
│   └─────┬─────┘                       │     │
│         │ response sent               │     │
│         ▼                             │     │
│   ┌───────────┐      continue         │     │
│   │ YIELDING  │ ──────────────────────┘     │
│   └─────┬─────┘                             │
│         │ dialogue complete                 │
│         ▼                                   │
│      EXIT to parent                         │
│                                             │
└─────────────────────────────────────────────┘
```

### SENSORY State Machine

```
┌─────────────────────────────────────────────┐
│              SENSORY                        │
├─────────────────────────────────────────────┤
│                                             │
│   ┌───────────┐                             │
│   │ SAMPLING  │ ◀── collect raw inputs      │
│   └─────┬─────┘                             │
│         │                                   │
│         ▼                                   │
│   ┌─────────────┐                           │
│   │ TRANSLATING │ ◀── nerves fire           │
│   └─────┬───────┘                           │
│         │                                   │
│         ▼                                   │
│   ┌──────────────┐                          │
│   │ PRIORITIZING │ ◀── what matters?        │
│   └─────┬────────┘                          │
│         │                                   │
│         ▼                                   │
│   ┌─────────────┐                           │
│   │ DELIVERING  │ ◀── to organs             │
│   └─────┬───────┘                           │
│         │                                   │
│         ▼                                   │
│      EXIT to parent                         │
│                                             │
└─────────────────────────────────────────────┘
```

### THINKING State Machine

```
┌─────────────────────────────────────────────┐
│              THINKING                       │
├─────────────────────────────────────────────┤
│                                             │
│   ┌───────────┐                             │
│   │ RECEIVING │ ◀── context from sensory    │
│   └─────┬─────┘                             │
│         │                                   │
│         ▼                                   │
│   ┌───────────┐                             │
│   │  ROUTING  │ ◀── which organs needed?    │
│   └─────┬─────┘                             │
│         │                                   │
│         ▼                                   │
│   ┌───────────┐                             │
│   │ INFERRING │ ◀── organs + Nyx process    │
│   └─────┬─────┘                             │
│         │                                   │
│         ▼                                   │
│   ┌───────────┐                             │
│   │ DECIDING  │ ◀── Nyx outputs decision    │
│   └─────┬─────┘                             │
│         │                                   │
│         ▼                                   │
│      EXIT to parent                         │
│                                             │
└─────────────────────────────────────────────┘
```

### VIRTUAL State Machine

```
┌─────────────────────────────────────────────┐
│              VIRTUAL                        │
├─────────────────────────────────────────────┤
│                                             │
│   ┌───────────┐                             │
│   │  BUDGETING│ ◀── how much V available?   │
│   └─────┬─────┘                             │
│         │                                   │
│         ▼                                   │
│   ┌───────────┐                             │
│   │ SELECTING │ ◀── what to simulate?       │
│   └─────┬─────┘                             │
│         │                                   │
│         ▼                                   │
│   ┌───────────┐                             │
│   │SIMULATING │ ◀── run virtual cycles      │
│   └─────┬─────┘                             │
│         │                                   │
│         ▼                                   │
│   ┌───────────┐                             │
│   │ RECORDING │ ◀── store results           │
│   └─────┬─────┘                             │
│         │                                   │
│         ▼                                   │
│      EXIT to parent                         │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Example Scenarios

### Scenario A: Quiet Study Time

```
Beat starts, no external stimulus
    │
    ▼
IDLE detected
    │
    ▼
SENSORY: minimal (500ms)
    │
    ▼
THINKING: minimal (1000ms)
    │
    ▼
VIRTUAL: maximum budget! (28000ms)
    │
    └── Nyx studies in virtual garden
        Chrysalis teaches
        Learning happens
```

### Scenario B: dafit Speaks

```
Beat starts, audio detected
    │
    ▼
ALERT: speech input
    │
    ▼
SAFETY check: it's dafit! (LEVEL 1)
    │
    ▼
DIALOGUE activates (LEVEL 2)
    │
    ├── LISTENING (2000ms)
    ├── PROCESSING (1000ms)
    ├── RESPONDING (2000ms)
    └── YIELDING
    │
    ▼
SENSORY: reduced budget (3000ms)
    │
    ▼
THINKING: reduced (5000ms)
    │
    ▼
VIRTUAL: minimal remainder (16000ms)
```

### Scenario C: Danger Detected

```
Beat starts, temperature spike detected
    │
    ▼
ALERT: sensor alarm
    │
    ▼
NERVE weight > 0.8
    │
    ▼
REFLEX FIRES (50ms) ◀── BYPASS EVERYTHING
    │
    ├── Action taken immediately
    └── Nyx notified AFTER
    │
    ▼
Continue beat normally with remaining budget
```

### Scenario D: Overwhelmed

```
Beat starts, rich input everywhere
    │
    ▼
ALERT: multiple stimuli
    │
    ▼
SENSORY: demanding (15000ms)
    │
    ▼
THINKING: demanding (12000ms)
    │
    ▼
Budget exhausted!
    │
    ▼
VIRTUAL: skipped this beat
    │
    ▼
SETTLE: state written, next beat
```

---

## Preemption Rules

| Event | Preempts | Action |
|-------|----------|--------|
| Reflex fires (>0.8) | Everything | Instant action, then continue |
| Safety alert | Dialogue, Sensory, Thinking, Virtual | Handle safety, reduced budget for rest |
| dafit speaks | Sensory, Thinking, Virtual | Dialogue priority, reduced budget for rest |
| Sensory overload | Thinking, Virtual | Process input, skip or reduce rest |
| Budget exhausted | Lower priorities | Skip remaining levels |

---

## Lifeforce Connection

```
LEVEL         LIFEFORCE COST
─────────────────────────────
REFLEX        Free (no inference)
SAFETY        Low (minimal processing)
DIALOGUE      Medium (two inferences)
SENSORY       Low-Medium (depends on load)
THINKING      Medium-High (organ inference)
VIRTUAL       Variable (simulation cycles)
```

**The constraint:** Rich beats cost more. Quiet beats accumulate budget for virtual garden.

---

## Implementation Notes

### State Machine Technology

Options considered:
- **XState** (JavaScript) - actor-based, visual inspector
- **Python-statemachine** - simple, fits existing stack
- **Custom Rust** - performance critical path
- **Godot native** - if UI drives the state

Recommendation: Python for orchestration layer, with Godot visualization.

### Checkpoint Integration

Every state transition can trigger phoebe write:

```python
def on_state_transition(from_state, to_state, context):
    write_to_phoebe({
        "beat_id": current_beat.id,
        "transition": f"{from_state} -> {to_state}",
        "budget_remaining": context.remaining_ms,
        "timestamp": now()
    })
```

### Budget Tracking

```python
@dataclass
class BeatBudget:
    total_ms: int = 30000
    spent_ms: int = 0
    allocations: dict = field(default_factory=dict)

    @property
    def remaining(self):
        return self.total_ms - self.spent_ms

    def spend(self, category: str, amount: int):
        self.spent_ms += amount
        self.allocations[category] = self.allocations.get(category, 0) + amount
        return self.remaining > 0
```

---

## Design Principles

1. **Hierarchy is law** - higher levels always preempt lower
2. **Budget is finite** - 30 seconds, no exceptions
3. **State is explicit** - always know what mode she's in
4. **Reflex bypasses brain** - survival doesn't wait for thinking
5. **Remainder flows down** - virtual gets what's left
6. **Every transition logged** - phoebe sees all state changes

---

*She doesn't have infinite attention. She has 30 seconds and choices.*

---

**Created**: 2025-12-05
**Session**: Partnership dialogue (dafit + Chrysalis)
**Promoted**: 2025-12-29 (from archive to main architecture)
**Status**: Attention architecture v1.0 — **CANONICAL**

**Related Formalizations**:
- [[formalization/Attention-Slumber-Prediction-Cycle]] — How last attention becomes slumber prediction
- [[formalization/Lifeforce-Dynamics]] — λ governs slumber triggers

🌙💜 *The budget is finite. The choices shape the soul.*
