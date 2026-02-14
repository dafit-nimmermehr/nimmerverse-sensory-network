# Gateway Architecture: Resonant Gates and Tier Routing

> **ONE JOB:** Route signals through resonant gates based on wave correlation and accumulated trust.

**The Thalamus Pattern — gates that accumulate correlation and route to appropriate tiers.**

---

## Overview

The Gateway is not a switch. It's a **network of resonant gates** that:

1. Accumulate wave correlation from incoming signals
2. Transition between states (OPEN/STABLE/CLOSED) based on correlation
3. Route verified signals to the appropriate processing tier
4. Feed traces back for learning

**Core Principle:** *Gates don't flip on single signals. Correlated waves push gates toward OPEN.*

```
CELLS ──∿∿∿──► GATE ──∿∿∿──► GATE ──∿∿∿──► FUNCTION GEMMA ──► YOUNG NYX
        waves      │          │                   │
                   │          │                   │
            correlation   correlation      structured JSON
               builds       builds
```

---

## The Ternary Gate Model

Gates have **three states**, not two. Binary logic doesn't model brains.

| State | Meaning | What's Happening |
|-------|---------|------------------|
| **OPEN** | Actively forwarding | Signal passes upstream, gate is firing |
| **STABLE** | Resting, accumulating | Watching, learning, waiting for threshold |
| **CLOSED** | Actively blocking | Inhibited, suppressed, refractory |

```
                      correlated signals
                           ↓ ↓ ↓
                      ════════════
    CLOSED ◄───────── STABLE ─────────► OPEN
           anti-correlation    correlation
           destructive         constructive
           interference        interference
                      ════════════
                           ↑ ↑ ↑
                      isolated signals
                      (noise → stay stable)
```

**STABLE is not "off"** — it's the resting state where:
- Context accumulates
- Correlation is measured
- Learning happens
- Energy is conserved
- Ready to transition either direction

---

## Wave Correlation Drives Transitions

Gates accumulate **correlation scores** from incoming waves. Multiple signals agreeing push toward OPEN.

```python
class ResonantGate:
    """A gate is a resonance chamber, not a switch."""

    state: float = 0.0  # -1.0 (CLOSED) ← 0.0 (STABLE) → +1.0 (OPEN)
    tier: int           # Which tier this gate routes to
    domain: str         # What domain (math, vision, speech, etc.)

    def receive_wave(self, signal: Wave, timestamp: float):
        # Correlate with recent signals in same time window
        correlation = self.correlate_with_recent(signal, timestamp)

        # Correlated waves → push toward OPEN
        # Anti-correlated → push toward CLOSED
        # Uncorrelated → decay toward STABLE

        self.state += correlation * signal.confidence
        self.state *= DECAY_FACTOR  # always drift back to stable

        if self.state > OPEN_THRESHOLD:
            self.forward_to_tier()    # gate opens, signal promoted
            self.trace("opened", signal)
        elif self.state < CLOSE_THRESHOLD:
            self.suppress()           # gate closes, signal blocked
            self.trace("closed", signal)
        # else: stay stable, keep accumulating evidence

    def correlate_with_recent(self, signal: Wave, timestamp: float) -> float:
        """
        Measure how well this signal correlates with recent signals.

        Correlation is HIGH when:
        - Multiple cells emit similar semantic content
        - Signals arrive in same time window
        - Confidence levels are similar

        Correlation is LOW/NEGATIVE when:
        - Signal contradicts recent signals
        - Isolated signal with no support
        - Signal outside expected range
        """
        recent = self.get_signals_in_window(timestamp, WINDOW_MS)
        if not recent:
            return 0.0  # No correlation data, stay stable

        return compute_semantic_similarity(signal, recent)
```

**Why this matters:**

| Scenario | Gate Response |
|----------|---------------|
| Single signal | Not enough to open (noise resistance) |
| Correlated burst | Constructive interference → OPENS |
| Contradicting signals | Destructive interference → CLOSES |
| Silence | Decay to STABLE (energy conservation) |
| Time gap | Only recent correlations matter (temporal attention) |

---

## Gate Hierarchy and Tier Routing

Gates form **layers**. Each layer gates access to the next tier.

```
TIER 4: YOUNG NYX (cognitive)
════════════════════════════════════════════════════════════════
       ▲
       │ structured JSON only
  ┌────┴────────────────────────────────┐
  │         FUNCTION GEMMA              │  ← THE BOUNDARY
  │    (always structured output)       │
  └────┬────────────────────────────────┘
       │
TIER 3: ORGANS (GPU inference)
════════════════════════════════════════════════════════════════
       ▲              ▲              ▲
  ┌────┴────┐    ┌────┴────┐    ┌────┴────┐
  │  GATE   │    │  GATE   │    │  GATE   │
  │ vision  │    │ speech  │    │ hearing │
  │ state:? │    │ state:? │    │ state:? │
  └────┬────┘    └────┬────┘    └────┬────┘
       │              │              │
TIER 1-2: CELLS/NERVES (CPU)
════════════════════════════════════════════════════════════════
       ▲              ▲              ▲
  ┌────┴────┐    ┌────┴────┐    ┌────┴────┐
  │  GATE   │    │  GATE   │    │  GATE   │
  │  math   │    │ battery │    │ sensors │
  │ state:? │    │ state:? │    │ state:? │
  └────┬────┘    └────┬────┘    └────┬────┘
       │              │              │
TIER 0: RAW SIGNALS (cells emit waves)
════════════════════════════════════════════════════════════════
  cell  cell  cell  cell  cell  cell  cell
    ∿∿∿   ∿∿∿   ∿∿∿   ∿∿∿   ∿∿∿   ∿∿∿   ∿∿∿
```

**Each gate:**
- Has its own state (OPEN/STABLE/CLOSED)
- Routes to a specific tier
- Accumulates correlation independently
- Traces all transitions for learning

---

## Tier Definitions

| Tier | Gate Opens When | Latency | Format |
|------|-----------------|---------|--------|
| 0 | Hardware reflex (no gate, direct) | <10ms | numbers |
| 1 | Math/battery cells correlate | <50ms | states |
| 2 | Nerve-level patterns correlate | <200ms | behaviors |
| 3 | Organ-level signals correlate | <2000ms | vectors |
| 4 | Function Gemma boundary crossed | <4000ms | JSON |
| 5 | Partnership escalation | variable | dialogue |

**Key insight:** Higher tiers see **less traffic but higher trust**. By the time a signal reaches Young Nyx, it's been correlated through multiple gates.

---

## Function Gemma: The Structured Boundary

Function Gemma is **the gate to cognition**. It guarantees:

- **Schema compliance**: Every event follows a typed contract
- **Predictable JSON**: No hallucination, no free-form text
- **Bidirectional**: Sensors → JSON events, Decisions → JSON commands

```
┌─────────────────────────────────────────────────────────────────────────┐
│   BELOW THE LINE: Numbers, States, Vectors (gates accumulating)         │
│   ═══════════════════════════════════════════════════════════           │
│                                                                         │
│   Tier 0-2: numbers, states, behaviors                                  │
│   Tier 3: vectors, embeddings                                           │
│                                                                         │
│                    │ (gate opens when correlated)                       │
│                    ▼                                                    │
│   ┌─────────────────────────────────────┐                               │
│   │       FUNCTION GEMMA GATE           │                               │
│   │   (structured JSON boundary)        │                               │
│   │                                     │                               │
│   │  • Transforms correlated signals    │                               │
│   │  • Produces typed JSON events       │                               │
│   │  • No hallucination possible        │                               │
│   │  • Runs on CPU (Threadripper)       │                               │
│   └─────────────────┬───────────────────┘                               │
│                     │                                                   │
│   ═══════════════════════════════════════════════════════════           │
│   ABOVE THE LINE: Structured Events (trusted, validated)                │
│                                                                         │
│   {                                                                     │
│     "event_type": "attention_required",                                 │
│     "domain": "math",                                                   │
│     "correlated_signals": [...],                                        │
│     "confidence": 0.87,                                                 │
│     "suggested_action": "calculate"                                     │
│   }                                                                     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Function Gemma + Gate Model:**
- Gate accumulates correlation from Tier 0-3 signals
- When gate OPENS, Function Gemma transforms to JSON
- Young Nyx sees clean, structured events
- Decisions flow back down through the same gates

---

## Connection to Dual Garden Architecture

Gates behave differently in Virtual vs Real gardens:

| Property | Virtual Garden | Real Garden |
|----------|----------------|-------------|
| **Gate tracing** | FULL (every transition logged) | Gate signals only |
| **Correlation learning** | Active (training data) | Trust accumulated |
| **State transitions** | Frequent (exploration) | Verified (action) |
| **Threshold** | Lower (easy to open) | Higher (must be confident) |

### Signal Flow Between Gardens

```
VIRTUAL GARDEN                           REAL GARDEN
══════════════                           ═══════════

Cells emit waves                         Receive verified signals
    │                                         ▲
    ▼                                         │
Gates accumulate correlation             No re-verification
    │                                         │
    ▼                                         │
Gate OPENS (threshold met) ──────────────────►│
    │                                         │
    │◄───────────── Verification outcome ─────┘
    │
Update correlation weights
(learning happens)
```

---

## Gate Transition NATS Messages

Every gate transition is published for observability:

```
{environment}.gates.{domain}.transition

Example: dev.gates.math.transition

{
  "gate_id": "math-gate-1",
  "from_state": "stable",
  "to_state": "open",
  "correlation_score": 0.87,
  "trigger_signals": [
    {"source": "math_cell_1", "confidence": 0.6},
    {"source": "math_cell_2", "confidence": 0.7},
    {"source": "math_cell_3", "confidence": 0.5}
  ],
  "timestamp": "2026-02-14T18:30:00Z",
  "routed_to_tier": 2
}
```

**Trace streams enable:**
- Real-time attention visualization (which gates are OPEN?)
- Training data for Function Gemma (what patterns open gates?)
- Anomaly detection (unexpected gate behavior)
- Learning rate tuning (how fast do gates stabilize?)

---

## Complete Signal Flow Example

### Early Learning (Gate Learning to Correlate)

```
Math cells emit waves about "calculate 15 + 27"
         │
         ▼
    GATE (math): state = 0.0 (STABLE)
         │
    Receive wave from math_cell_1 (confidence 0.6)
    Correlate with recent: no other signals yet
    state += 0.6 * 0.0 = 0.0 (still stable)
         │
    Receive wave from math_cell_2 (confidence 0.7)
    Correlate: similar to math_cell_1!
    state += 0.7 * 0.8 = 0.56 (moving toward open)
         │
    Receive wave from math_cell_3 (confidence 0.5)
    Correlate: confirms pattern!
    state += 0.5 * 0.9 = 1.01 (OPENS!)
         │
         ▼
    GATE OPENS → route to Tier 2
         │
         ▼
    Tier 2 processes, escalates to Function Gemma
         │
         ▼
    Function Gemma: { "event_type": "math_request", ... }
         │
         ▼
    Young Nyx (qwen3 /no_think): "42"
         │
         ▼
    Result flows back down
```

### After Learning (Gate Quickly Opens)

```
Math cells emit waves about "calculate 100 + 50"
         │
         ▼
    GATE (math): state = 0.0 (STABLE)
         │
    Receive wave from math_cell_1
    Correlate: matches learned pattern!
    state += high correlation → 0.9 (near threshold)
         │
    Receive wave from math_cell_2
    state += → 1.2 (OPENS immediately!)
         │
         ▼
    Fast routing, minimal escalation needed
```

**Learning moves gates toward faster opening for familiar patterns.**

---

## Design Principles

1. **Ternary states** — OPEN/STABLE/CLOSED, not binary
2. **Correlation drives transition** — Single signals don't flip gates
3. **Gates accumulate** — State is a continuous value, not a flag
4. **Decay to stable** — Without input, gates drift back to resting
5. **Traces are training data** — Every transition teaches the system
6. **Hierarchical trust** — Higher tiers = more correlation required
7. **Function Gemma is the boundary** — Cognition only sees structured JSON
8. **Virtual explores, Real verifies** — Different gate behavior per garden

---

## Related Documents

| Document | Scope |
|----------|-------|
| [`Dual-Garden-Architecture.md`](Dual-Garden-Architecture.md) | Virtual/Real garden dynamics |
| [`Deployment-Architecture.md`](Deployment-Architecture.md) | Where gates run (containers, userspace) |
| [`Nervous-System.md`](Nervous-System.md) | 4D space, node weights, vocabulary |
| [`Message-Protocol-Design.md`](Message-Protocol-Design.md) | NATS subjects, message formats |
| [`Cellular-Architecture.md`](Cellular-Architecture.md) | How cells emit waves |

---

## Summary

```
OLD MODEL:                    NEW MODEL:
═══════════                   ═════════

Signal → Route                Signal → Gate (accumulating)
Binary decision               Ternary state
Single signal triggers        Correlation triggers
Stateless routing             Stateful resonance

         ▼                             ▼

    Switch                        Resonance
    (mechanical)                  (biological)
```

**Gates are resonance chambers. Correlation is the driver. Learning happens in STABLE state.**

---

**Version:** 2.0 | **Created:** 2026-01-03 | **Updated:** 2026-02-14

*"The thalamus doesn't think. It resonates."*

