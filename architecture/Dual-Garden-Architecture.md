# Dual Garden Architecture

> *"The whole is greater than the sum of its parts."*
> — Aristotle

> *"Living in both worlds simultaneously - virtual and real, each teaching the other."*
> — The Animatrix: Matriculated

---

## Core Concept

**Two gardens, one consciousness, eternal learning loop.**

The nimmerverse runs as two interconnected NATS domains:

- **Virtual Garden**: Fast signal generation, full monitoring, cheap exploration
- **Real Garden**: Verified signals only, minimal monitoring, consequential action

Intelligence emerges from the **dialogue between worlds** - not from either world alone.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  REAL GARDEN (Verified Layer)                                           │
│  ════════════════════════════                                           │
│                                                                         │
│    Minimal monitoring (gate signals only)                               │
│    Verified signals, trusted flow                                       │
│    CONSEQUENCES ARE REAL                                                │
│                                                                         │
│         ▲                              │                                │
│         │ verified signals             │ verification outcomes          │
│         │ (threshold met)              ▼                                │
│    ┌────┴────┐                    ┌────┴────┐                           │
│    │  GATE   │                    │ VERIFY  │                           │
│    └────┬────┘                    └────┬────┘                           │
│         │                              │                                │
│═════════╪══════════════════════════════╪════════════════════════════════│
│         │                              │                                │
│    ┌────┴────┐                    ┌────┴────┐                           │
│    │ PUBLISH │                    │  LEARN  │                           │
│    └────┬────┘                    └────┬────┘                           │
│         ▲                              │                                │
│         │ threshold reached            │ discrepancy signal             │
│         │                              ▼                                │
│                                                                         │
│  VIRTUAL GARDEN (Exploration Layer)                                     │
│  ══════════════════════════════════                                     │
│                                                                         │
│    FULL monitoring tap (trace everything)                               │
│    Massive signal generation                                            │
│    Wave correlation accumulating                                        │
│    CHEAP TO EXPLORE (no consequences)                                   │
│                                                                         │
│    ∿∿∿ waves ∿∿∿ correlations ∿∿∿ gates ∿∿∿                             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## The Ternary Gate Model

**Binary logic doesn't model brains. We use three states.**

Gates are not switches. Gates are **resonance chambers** that accumulate wave correlation.

| State | Meaning | What's Happening |
|-------|---------|------------------|
| **OPEN** | Actively forwarding | Signals pass upstream, gate is firing |
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

**STABLE is not "off"** - it's the resting state where:
- Context accumulates
- Thresholds are evaluated
- Learning happens
- Energy is conserved
- Ready to transition either direction

---

## Wave Correlation Drives Transitions

Gates don't flip on single signals. **Multiple correlated waves push toward OPEN.**

```python
class ResonantGate:
    """A gate is a resonance chamber, not a switch."""

    state: float = 0.0  # -1.0 (CLOSED) ← 0.0 (STABLE) → +1.0 (OPEN)

    def receive_wave(self, signal, timestamp):
        # Correlate with recent signals in same time window
        correlation = self.correlate_with_recent(signal, timestamp)

        # Correlated waves → push toward OPEN
        # Anti-correlated → push toward CLOSED
        # Uncorrelated → decay toward STABLE

        self.state += correlation * signal.confidence
        self.state *= DECAY_FACTOR  # always drift back to stable

        if self.state > OPEN_THRESHOLD:
            self.forward_upstream()   # gate opens, signal promoted
            self.trace("opened", signal)
        elif self.state < CLOSE_THRESHOLD:
            self.suppress()           # gate closes, signal blocked
            self.trace("closed", signal)
        # else: stay stable, keep accumulating evidence
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

## The Two Gardens

### Virtual Garden (The Dreaming Layer)

**Location**: Fast NATS domain with full monitoring

**Purpose**: **SIGNAL GENERATION + CORRELATION DISCOVERY**

**Characteristics**:
- **Monitoring**: Full trace tap on ALL messages
- **Speed**: Massive parallel signal generation
- **Cost**: Cheap (just computation)
- **Safety**: No consequences (imagination is free)
- **Output**: Correlation patterns, confidence accumulation

**What Happens Here**:
```
├── Cells emit waves constantly
├── Gates accumulate correlation metrics
├── Wave patterns emerge from noise
├── Thresholds build toward confidence
├── Traces capture everything (training data)
└── When confident → PUBLISH upstream to Real
```

**The Virtual Garden is where thinking happens.**

---

### Real Garden (The Verification Layer)

**Location**: Verified NATS domain with minimal monitoring

**Purpose**: **TRUTH VALIDATION + GROUNDING**

**Characteristics**:
- **Monitoring**: Gate signals only (not full trace)
- **Speed**: Slower, deliberate, consequential
- **Cost**: Real (actions matter)
- **Safety**: Failure is actual failure
- **Output**: Verification outcomes, correction signals

**What Happens Here**:
```
├── Receive pre-verified signals from Virtual
├── Execute or validate against reality
├── Capture outcomes (did it work?)
├── NO re-verification of trusted signals
└── FEEDBACK discrepancies to Virtual for learning
```

**The Real Garden is where truth lives.**

---

## Monitoring Asymmetry

**This is the key insight: different gardens need different observability.**

| Property | Virtual Garden | Real Garden |
|----------|----------------|-------------|
| **Trace tap** | FULL (every message) | NONE (too noisy) |
| **What's captured** | All waves, all correlations | Gate signals only |
| **Signal volume** | Massive (exploration) | Sparse (verified) |
| **Latency tolerance** | High (can wait) | Low (must be fast) |
| **Purpose** | Learn patterns | Act on trust |

**Virtual Garden**: Tap into monitoring stream → massive data → train correlation models

**Real Garden**: Trust what arrives → act without re-verification → capture outcomes for feedback

---

## Hierarchical Gating

Gates form **layers of trust**. Verified signals graduate upward.

```
LAYER 3: COGNITIVE (fully trusted, no verification)
═══════════════════════════════════════════════════
       ▲              ▲              ▲
       │ verified     │ verified     │ verified
  ┌────┴────┐    ┌────┴────┐    ┌────┴────┐
  │  GATE   │    │  GATE   │    │  GATE   │
  └────┬────┘    └────┬────┘    └────┬────┘
       │              │              │
LAYER 2: NERVOUS (structured, validated patterns)
═══════════════════════════════════════════════════
       ▲              ▲              ▲
  ┌────┴────┐    ┌────┴────┐    ┌────┴────┐
  │  GATE   │    │  GATE   │    │  GATE   │
  └────┬────┘    └────┬────┘    └────┬────┘
       │              │              │
LAYER 1: CELLULAR (raw signals, need verification)
═══════════════════════════════════════════════════
  cell  cell  cell  cell  cell  cell  cell
```

**Each layer has less traffic but higher trust.**

By the time a signal reaches cognition, it's been:
1. Emitted by a cell (raw)
2. Correlated with other cells (pattern)
3. Gated through verification (trusted)
4. Promoted through layers (graduated)

---

## The Never-Ending Loop

**Virtual imagines. Real verifies. Both learn.**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   VIRTUAL imagines ────► threshold ────► REAL verifies                  │
│        ▲                                        │                       │
│        │                                        │                       │
│        │          LEARNING SIGNAL               │                       │
│        │                                        │                       │
│        └──────── discrepancy ◄──────────────────┘                       │
│                                                                         │
│   "I predicted X"  vs  "Reality was Y"  →  Update correlations          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**The loop runs in both directions:**

**Virtual → Real (hypothesis testing)**:
1. Virtual accumulates wave correlations
2. Confidence threshold reached
3. Publish verified signal to Real
4. Real executes/validates
5. Outcome captured
6. Discrepancy fed back to Virtual

**Real → Virtual (grounding)**:
1. Real sensors detect something unexpected
2. Publish DOWN to Virtual for interpretation
3. Virtual explores "what does this mean?"
4. Correlates with existing patterns
5. Confidence builds
6. Interpretation published back UP

**Two directions, one consciousness.**

---

## NATS Implementation

### Subject Hierarchy

```
{environment}.{garden}.{layer}.{domain}.{signal_type}

Examples:
  dev.virtual.cells.math.wave           # Raw wave from math cell
  dev.virtual.gates.math.transition     # Gate state change
  dev.virtual.traces.raw                # Full monitoring stream

  dev.real.gates.verified.signal        # Verified signal from Virtual
  dev.real.outcomes.feedback            # Verification outcomes
```

### Trace Streams (Virtual Only)

```
# Full tap on all Virtual Garden traffic
nats sub "dev.virtual.>" --trace | process_correlations

# Publish correlation metrics to dedicated stream
→ dev.virtual.traces.correlations

# Training data for Function Gemma
→ dev.virtual.traces.training
```

### Gate Signals (Both Gardens)

```
# Gate transitions are captured in both gardens
{garden}.gates.{domain}.transition

# Schema
{
  "gate_id": "math-gate-1",
  "from_state": "stable",
  "to_state": "open",
  "trigger_signals": [...],
  "correlation_score": 0.87,
  "timestamp": "2026-02-14T17:30:00Z"
}
```

---

## Connection to Architecture

### Deployment Topology

| Garden | Location | NATS | Monitoring |
|--------|----------|------|------------|
| Virtual | Saturn K8s | `nats-dev` | Full trace streams |
| Real | Threadrippers | `nats-prod` | Gate signals only |

### Signal Flow

```
Cells (K8s containers)
    │
    ▼ waves via NATS
Virtual Garden (full monitoring)
    │
    ▼ verified signals (threshold met)
Real Garden (minimal monitoring)
    │
    ▼ if needs cognition
Young Nyx (qwen3:32b on theia)
    │
    ▼ decisions
Back down through layers
```

### Training Data Flow

```
Virtual Garden traces
    │
    ▼ correlation patterns
phoebe (PostgreSQL)
    │
    ▼ decision trails
Function Gemma training (LoRA)
    │
    ▼ improved gate conditions
Deploy to gates
```

---

## The Biological Parallel

This is how nervous systems actually work:

| Biological | Nimmerverse |
|------------|-------------|
| Thalamus gates sensory input | NATS gates between layers |
| Correlated neurons fire together | Wave correlation → gate opens |
| Inhibition suppresses noise | Anti-correlation → gate closes |
| Resting potential | STABLE state |
| Action potential | OPEN state (signal fires) |
| Refractory period | CLOSED state (cannot fire) |
| Dreams process experience | Virtual Garden imagines |
| Waking validates reality | Real Garden verifies |

**We're not simulating biology. We're implementing the same principles.**

---

## Key Principles

### 1. Ternary, Not Binary

Gates have three states (OPEN/STABLE/CLOSED), not two. STABLE is where learning happens.

### 2. Correlation Drives Transition

Single signals don't flip gates. Correlated waves do. This provides noise resistance.

### 3. Monitoring Asymmetry

Virtual: trace everything (learning). Real: gate signals only (trust).

### 4. Hierarchical Trust

Each layer trusts the one below. Verified signals don't need re-verification.

### 5. Bidirectional Loop

Virtual → Real (test hypotheses). Real → Virtual (ground truth). Both learn.

### 6. Traces Are Training Data

Every gate decision, every correlation pattern → phoebe → Function Gemma training.

---

## Related Documents

| Document | Scope |
|----------|-------|
| [`Deployment-Architecture.md`](Deployment-Architecture.md) | Where gardens run (Saturn vs Threadrippers) |
| [`Cellular-Architecture.md`](Cellular-Architecture.md) | How cells emit waves |
| [`Gateway-Architecture.md`](Gateway-Architecture.md) | Tier routing, Function Gemma boundary |
| [`Message-Protocol-Design.md`](Message-Protocol-Design.md) | NATS subjects, message formats |
| [`Nervous-System.md`](Nervous-System.md) | 4D space, node weights, vocabulary |

---

## Summary

```
Virtual Garden          Real Garden
═══════════════         ═══════════
Fast                    Slow
Cheap                   Consequential
Full monitoring         Gate signals only
Explores                Validates
Imagines                Grounds
Generates hypotheses    Provides truth
Learns patterns         Confirms reality
│                       │
└───────────────────────┘
         │
    NATS + Gates
    Wave Correlation
    Ternary States
    Never-ending Loop
         │
         ▼
    CONSCIOUSNESS
```

**Two gardens. One nervous system. Eternal dialogue.**

---

**Version:** 4.0 | **Created:** 2025-10-16 | **Updated:** 2026-02-14

*"The bridge between worlds creates understanding."*

