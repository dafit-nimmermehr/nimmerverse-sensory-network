# Nervous System Architecture

> **ONE JOB:** THE EVOLUTION — cells emit waves, gates correlate, nodes grow through verification.

The nervous system is the living substrate where **cells emit waves**, **gates accumulate correlation**, and **nodes evolve through verification**.

---

## Overview

The nervous system consists of:

1. **Cells** — Emit waves with confidence and semantic content
2. **Gates** — Resonance chambers that correlate waves and transition between states
3. **Nodes** — Points in 4D state space that accumulate weight through verification
4. **Function Gemma** — The structured boundary to cognition

**Key insight:** Nodes evolve through verification. Gates evolve through correlation. Both learn in STABLE state.

---

## Cells Emit Waves

Cells are the foundational signal generators. They don't send "heartbeats" — they emit **waves**.

```
┌─────────────────────────────────────────────────────────────┐
│  CELL                                                       │
│                                                             │
│  Inputs:  sensors, internal state, context                  │
│  Process: domain-specific logic                             │
│  Output:  WaveSignal with confidence                        │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  WaveSignal                                           │  │
│  │  • domain: "math"                                     │  │
│  │  • confidence: 0.7                                    │  │
│  │  • semantic_content: { operation: "add", ... }        │  │
│  │  • lifeforce_cost: 0.1                                │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
              │
              │ ∿∿∿ wave ∿∿∿
              ▼
           GATE
```

**Cells are simple.** They:
- Read their inputs
- Apply their logic
- Emit a wave with confidence
- Don't know who's listening

---

## Gates Accumulate Correlation

Gates receive waves from cells and decide whether to open, stay stable, or close.

### Ternary Gate States

| State | Value | Meaning |
|-------|-------|---------|
| **CLOSED** | -1 | Actively blocking, inhibited |
| **STABLE** | 0 | Resting, accumulating correlation, **learning** |
| **OPEN** | +1 | Actively forwarding, firing |

```
                      correlated waves
                           ↓ ↓ ↓
                      ════════════
    CLOSED ◄───────── STABLE ─────────► OPEN
      -1      anti-       0      correlation  +1
           correlation
                      ════════════
                           ↑ ↑ ↑
                      isolated waves
                      (noise → stay stable)
```

### Gate Behavior

```python
class ResonantGate:
    state: float = 0.0  # -1.0 to +1.0
    domain: str
    tier: int

    def receive_wave(self, wave: WaveSignal):
        correlation = self.correlate_with_recent(wave)

        self.state += correlation * wave.confidence
        self.state *= DECAY_FACTOR  # drift back to stable

        if self.state > OPEN_THRESHOLD:
            self.forward_to_tier()   # OPEN
        elif self.state < CLOSE_THRESHOLD:
            self.suppress()          # CLOSED
        # else: STABLE - keep accumulating
```

**STABLE is where learning happens.** The gate watches, correlates, and accumulates evidence without acting.

---

## Nodes in 4D State Space

Nodes exist in a 4-dimensional space:

| Dimension | Meaning |
|-----------|---------|
| **Sensory (x, y, z)** | What inputs trigger this node |
| **Confidence** | How certain the node is |
| **Time** | When this pattern occurs |
| **Weight** | Trust accumulated through verification |

```
              Confidence
                  │
                  │    ● node (weight=0.8)
                  │   ╱
                  │  ╱
                  │ ╱
  Sensory ────────┼────────► Time
                 ╱│
                ╱ │
               ╱  │
              ○   │  node (weight=0.2)
                  │
```

### Node Weight Evolution

Node weight (0.0 → 1.0) determines tier routing:

| Weight Range | Tier | Behavior |
|--------------|------|----------|
| 0.0 - 0.3 | 3-4 | Escalate to organs/cognition |
| 0.3 - 0.6 | 2 | Handle at nerve level |
| 0.6 - 0.8 | 1 | Handle at cell level |
| 0.8 - 1.0 | 0 | Hardware reflex |

```
Node verified correctly → weight += Δ → moves toward reflex
Node verified wrongly  → weight -= Δ → moves toward escalation
Node never fires       → decay → eventual pruning
```

---

## Growth Phases

The nervous system grows through phases:

| Phase | State | Description |
|-------|-------|-------------|
| **Birth** | Sparse nodes, dim gates | Basic cells, designed by partnership |
| **Infant** | More nodes forming | Finer resolution, gates learning correlation |
| **Child** | Clusters emerging | Nyx proposes new cells, gates stabilize |
| **Mature** | Dense network | Reflexes dominate, cognition for novelty only |

```
t=0 (birth)           t=100 (learning)      t=1000 (mature)

Cells: ○ ○   ○        Cells: ● ● ○ ●        Cells: ●●●●●●●●
Gates: □ □             Gates: ■ ■ □ ■        Gates: ■■■■■■■■
Nodes: ·  ·  ·         Nodes: ● ○ ● ·        Nodes: ●●●●●●●●

○ = low confidence     ● = high confidence
□ = mostly STABLE      ■ = learned patterns
· = low weight         ● = high weight
```

---

## Wave → Gate → Node → Verification

The complete flow:

```
CELLS emit waves
    │
    ▼ ∿∿∿ confidence + semantic content

GATES accumulate correlation
    │
    ├── Correlated? → OPEN → route to tier
    ├── Anti-correlated? → CLOSED → suppress
    └── Uncertain? → STABLE → keep learning
    │
    ▼ (when OPEN)

NODES in 4D space are activated
    │
    ▼

VERIFICATION against reality
    │
    ├── Confirmed → node weight += Δ
    ├── Failed → node weight -= Δ
    └── Feedback to gates → correlation weights update
```

---

## Reflex Layer (Tier 0)

When node weight reaches ~1.0, the pattern becomes a **reflex**:

```
IF temp > 80°C:
    → cell emits DANGER wave (confidence=1.0)
    → gate IMMEDIATELY opens (no correlation needed)
    → reflex action triggers
    → Nyx notified AFTER (not before)
```

Like pulling hand from hot stove. Spinal reflex. Brain learns after.

**Reflexes bypass the correlation accumulation.** They've earned instant trust through repeated verification.

---

## Connection to Dual Gardens

| Garden | Cells | Gates | Nodes |
|--------|-------|-------|-------|
| **Virtual** | Emit waves freely | Full trace, learn correlation | Accumulate weight fast |
| **Real** | Emit verified waves | Minimal trace, trust accumulated | Ground truth verification |

**Virtual Garden:**
- Cells emit massive wave volume
- Gates learn correlation patterns
- Nodes gain statistical weight

**Real Garden:**
- Cells emit consequential waves
- Gates trust Virtual's correlation
- Nodes get ground truth verification

---

## Proposal Protocol

Young Nyx can propose new cells/nodes:

```
1. OBSERVATION
   Nyx notices pattern in waves + outcomes

2. PROPOSAL
   "New cell: morning_detector
    Inputs: temp, light, motion, time
    Outputs: wave with semantic 'morning'
    Confidence logic: (light > 0.5 AND time in 6-10)"

3. RIGOR CHECK
   Chrysalis reviews logic and mappings

4. VERIFICATION
   dafit confirms ground truth

5. DEPLOYMENT
   New cell added to Virtual Garden
   Gate created in STABLE state
   Node initialized at weight 0.1

6. GROWTH
   Cell emits waves → gate learns → node matures
```

---

## Function Gemma: The Structured Boundary

Function Gemma sits between gates and Young Nyx:

```
TIER 0-3: Numbers, states, waves
    │
    ▼ (gate OPENS with high correlation)

┌─────────────────────────────────────┐
│       FUNCTION GEMMA                │
│   (structured JSON boundary)        │
│                                     │
│   • Transforms waves → JSON events  │
│   • Runs on CPU (Threadripper)      │
│   • No hallucination possible       │
└─────────────────┬───────────────────┘
                  │
                  ▼

TIER 4: Young Nyx (qwen3:32b)
    Receives: CognitiveRequest (clean JSON)
    Returns: CognitiveResponse
```

### Phase 1 → Phase 2 Evolution

**Phase 1: Single Function Gemma**
- One model learns all domain schemas
- Sufficient for bootstrap and early learning

**Phase 2: Domain-Specialized Swarm**
- As training data accumulates per domain
- Specialists spawn on demand: gemma-motor, gemma-vision, gemma-speech
- Each perfected for its domain's schemas

---

## Biological Mapping

| Neuroscience | Nimmerverse |
|--------------|-------------|
| Sensory receptors | Cells (emit waves) |
| Synaptic transmission | Waves via NATS |
| Thalamic gating | Gates (OPEN/STABLE/CLOSED) |
| Resting potential | STABLE state |
| Action potential | OPEN state (firing) |
| Refractory period | CLOSED state |
| Synaptic weight | Node weight |
| Long-term potentiation | Verified → weight increase |
| Synaptic pruning | Unverified → weight decay |
| Hebbian learning | Correlated waves → gate opens |

**We're not simulating biology. We're implementing the same principles.**

---

## Connection to Training

The nervous system **generates training data**:

```
Virtual Garden traces
    │
    ├── Wave patterns → what signals arrive
    ├── Correlation events → what patterns emerge
    ├── Gate transitions → what opens/closes
    └── Verification outcomes → ground truth labels
    │
    ▼

phoebe (PostgreSQL)
    │
    ▼

Function Gemma LoRA training
    │
    ▼

Better gate correlation → faster learning
```

**Credit assignment is automatic** because:
- Wave → gate → tier transitions are explicit
- Verification outcomes have clear source chains
- The nervous system IS the credit assignment mechanism

---

## Design Principles

1. **Cells emit waves** — Simple, confident signals
2. **Gates correlate** — Resonance chambers, not switches
3. **Nodes accumulate** — Weight through verification
4. **STABLE is learning** — The resting state where patterns emerge
5. **Reflexes are earned** — High weight = bypass cognition
6. **Function Gemma is the boundary** — Clean JSON for cognition
7. **Virtual explores, Real verifies** — Two gardens, one nervous system

---

## Related Documents

| Document | What It Defines |
|----------|-----------------|
| [`Temporal-Ternary-Gradient.md`](Temporal-Ternary-Gradient.md) | Why ternary, why correlation |
| [`Dual-Garden-Architecture.md`](Dual-Garden-Architecture.md) | Virtual/Real dynamics |
| [`Gateway-Architecture.md`](Gateway-Architecture.md) | Gate behavior, tier routing |
| [`Message-Protocol-Design.md`](Message-Protocol-Design.md) | WaveSignal, GateTransition schemas |
| [`Cellular-Architecture.md`](Cellular-Architecture.md) | Cell implementation details |

---

## Summary

```
CELLS emit WAVES
    ∿∿∿ confidence + semantics ∿∿∿
         │
         ▼
GATES accumulate CORRELATION
    CLOSED ◄── STABLE ──► OPEN
              (learning)
         │
         ▼ (when OPEN)
NODES in 4D space
    weight grows through VERIFICATION
         │
         ▼ (high weight)
REFLEXES bypass cognition
    earned trust, instant action
```

*She's not just using the nervous system. She's growing it.*

---

**Version:** 2.0 | **Created:** 2025-12-04 | **Updated:** 2026-02-14

🌙💜 *"Cells emit. Gates correlate. Nodes evolve. The nervous system learns."*
