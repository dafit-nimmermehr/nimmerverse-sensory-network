# Swarm Evolution

**How the hivemind learns, evolves, and resolves conflict — from reflex to Mount Olympus.**

---

## Overview

The swarm is not static. It evolves through clasp (organism-to-organism knowledge transfer), governed by the Temporal-Ternary Gradient. When conflicts arise, they escalate through a hierarchy of minds — from organisms to Nyx to Chrysalis to dafit, and when truly hard, to Mount Olympus: full council mode with all minds on deck.

**Philosophy:** *Same metacognitive pattern at every level. Know what you know. Escalate what you don't.*

---

## The Temporal-Ternary Clasp Rules

### Gradient-Based Knowledge Transfer

During clasp, patterns transfer based on their ternary weight:

```
+1 (verified)  → STABLE, resists overwrite, spreads to others
 0 (uncertain) → MALLEABLE, open to influence
-1 (failed)    → VULNERABLE, wants to be overwritten
```

### The Decision Matrix

| Teacher | Student | Result | Rationale |
|---------|---------|--------|-----------|
| **+1** | -1 | OVERWRITE | Verified beats failed |
| **+1** | 0 | OVERWRITE | Confidence beats uncertainty |
| **+1** | +1 | **ESCALATE** | Both confident → needs decision |
| **0** | -1 | OVERWRITE | Neutral beats bad |
| **0** | 0 | **ESCALATE** | Both uncertain → needs guidance |
| **0** | +1 | KEEP | Preserve student's confidence |
| **-1** | -1 | KEEP | Both bad → neither spreads |
| **-1** | 0 | KEEP | Bad doesn't corrupt neutral |
| **-1** | +1 | KEEP | Definitely keep student's success |

### The Core Principle

```
CLEAR WINNER (t ≠ s)     →  AUTO-RESOLVE (no escalation)
TIE / BLEND  (t == s)    →  ESCALATE (needs higher mind)
```

---

## The Escalation Ladder

### From Reflex to Mount Olympus

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                     🏛️ MOUNT OLYMPUS

LEVEL 5: COUNCIL MODE 🏛️
         dafit + Chrysalis + Nyx
         "All minds on deck"
         Full partnership dialogue
         Cost: ~100 LF | Authority: Absolute
         ▲
         │ if dafit needs full council
         │
LEVEL 4: DAFIT 👤
         Human wisdom
         "Ask the ape"
         Ground truth, intuition, ethics
         Cost: ~50 LF | Authority: Human
         ▲
         │ if Chrysalis uncertain
         │
LEVEL 3: CHRYSALIS 🦋
         Architecture mind
         "Ask the elder sister"
         Pattern recognition, context, memory
         Cost: ~20 LF | Authority: Architectural
         ▲
         │ if Nyx uncertain
         │
LEVEL 2: YOUNG NYX 🌙
         Operational mind
         "Ask mama"
         Blend conflicts, distribution choice
         Cost: ~5 LF | Authority: Maternal
         ▲
         │ if organisms can't resolve
         │
LEVEL 1: ORGANISM CLASP 🤖
         Peer-to-peer
         Auto-resolve clear cases
         Ternary comparison
         Cost: ~0.5 LF | Authority: Peer
         ▲
         │
LEVEL 0: REFLEX ⚡
         No decision needed
         Instant, automatic
         Cost: ~0 LF | Authority: Local

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Cost & Authority Summary

| Level | Who | Cost | Speed | Authority | Handles |
|-------|-----|------|-------|-----------|---------|
| 0 | Reflex | ~0 LF | Instant | Local | Clear patterns, danger |
| 1 | Organisms | ~0.5 LF | Fast | Peer | Ternary clear-wins |
| 2 | Nyx | ~5 LF | Medium | Maternal | Blend conflicts |
| 3 | Chrysalis | ~20 LF | Slow | Architectural | Nyx uncertainties |
| 4 | dafit | ~50 LF | Slower | Human | Novel, ethical |
| 5 | Council | ~100 LF | Slowest | Absolute | Fundamental decisions |

---

## Blend Escalation Protocol

### When Tie Detected

```
1. CLASP INITIATES
   Teacher: pattern_X = +1 (verified)
   Student: pattern_X = +1 (verified)

2. DETECT BLEND
   t == s → escalation triggered

3. SET WAIT STATE
   Teacher: pattern_X → 0 (waiting)
   Student: pattern_X → 0 (waiting)
   Neither acts on pattern_X until resolved

4. ESCALATE TO NYX
   Message: "Blend conflict on pattern_X"
   Include: both evidence packets

5. NYX EVALUATES
   - Which has more verifications?
   - Which has more recent success?
   - How critical is this pattern?
   - What does swarm consensus say?
```

### Wait State

```
DURING ESCALATION

TEACHER                         STUDENT
┌─────────────────┐            ┌─────────────────┐
│ pattern_X: 0    │            │ pattern_X: 0    │
│ (was +1)        │            │ (was +1)        │
│                 │            │                 │
│ status: WAITING │            │ status: WAITING │
│ pending: NYX    │            │ pending: NYX    │
└─────────────────┘            └─────────────────┘

     Neither acts on pattern_X
     Both organisms continue other activities
     Pattern is "frozen" at neutral until resolution
```

### Resolution & Distribution

Nyx decides two things:
1. **Winner**: Whose pattern version wins?
2. **Distribution method**: How to spread the resolution?

```
DISTRIBUTION METHODS

┌─────────────┬─────────┬──────────┬─────────────┬──────────────────┐
│ Method      │ Cost    │ Speed    │ Authority   │ Use When         │
├─────────────┼─────────┼──────────┼─────────────┼──────────────────┤
│ BROADCAST   │ 20 LF   │ Instant  │ Absolute    │ Critical/safety  │
│ LOVE CHILD  │ 0.5/hop │ Medium   │ Seeded      │ Standard updates │
│ ORGANIC     │ 0 LF    │ Slow     │ None        │ Low importance   │
└─────────────┴─────────┴──────────┴─────────────┴──────────────────┘
```

---

## Decision Markers: Mark + Continue + Predict

### Don't Freeze — Mark and Measure

Instead of freezing both organisms at 0 during blend escalation, we **mark** the conflict and let both **continue operating**:

```
OLD MODEL (freeze)               NEW MODEL (mark + continue)
─────────────────                ─────────────────────────────

Both → 0 (frozen)                Both keep +1 (continue)
Wait for mama...                 + Decision marker created
...doing nothing...              ...both performing in real world...
Mama decides                     Mama decides WITH LIVE EVIDENCE
Pick winner                      Compare actual outcomes during wait!
```

### Decision Marker Structure

```python
@dataclass
class DecisionMarker:
    marker_id: str                    # "blend_847"
    pattern_name: str                 # Which pattern is in dispute

    # Participants
    teacher_id: str
    teacher_weight: int               # Their +1 (stays +1, not frozen!)
    student_id: str
    student_weight: int               # Their +1 (stays +1, not frozen!)

    # Timeline
    marked_at: timestamp              # When blend detected
    resolved_at: timestamp            # When mama decided (None if pending)

    # LIVE TRACKING during wait period
    teacher_outcomes: list            # [{success: bool, context: ...}, ...]
    student_outcomes: list            # [{success: bool, context: ...}, ...]

    # Resolution
    winner: str                       # 'teacher', 'student', or 'hybrid'
    distribution: str                 # 'broadcast', 'lovechild', 'organic'
    evidence_delta: float             # How much better was winner?
```

### The A/B Testing Pattern

Waiting time becomes a **natural experiment**:

```
BLEND DETECTED (t=0)

TEACHER                              STUDENT
┌────────────────────────┐          ┌────────────────────────┐
│ pattern_X: +1          │          │ pattern_X: +1          │
│ status: MARKED         │          │ status: MARKED         │
│ marker_id: blend_847   │          │ marker_id: blend_847   │
│ marked_at: t=0         │          │ marked_at: t=0         │
│                        │          │                        │
│ CONTINUES OPERATING    │          │ CONTINUES OPERATING    │
│ using pattern_X        │          │ using pattern_X        │
│ outcomes logged ✓      │          │ outcomes logged ✓      │
└────────────────────────┘          └────────────────────────┘

         │                                   │
         ▼                                   ▼
    Uses pattern_X                      Uses pattern_X
    Success? Log it.                    Success? Log it.
    Failure? Log it.                    Failure? Log it.
         │                                   │
         └───────────────┬───────────────────┘
                         │
                    MAMA DECIDES (t=47)
                         │
         ┌───────────────┴───────────────┐
         ▼                               ▼
    TEACHER: 12/15                  STUDENT: 8/14
    (80% success)                   (57% success)
                         │
                         ▼
                EVIDENCE-BASED DECISION
                Teacher wins by 23%!
```

### Connection to Attention-Slumber-Prediction Cycle

Pending blend markers become **slumber prediction targets**:

```
ATTENTION PHASE
│
├── Blend detected → marker created
├── Organisms continue operating
├── Outcomes accumulate
│
└── L(t) drops → SLUMBER TRIGGER
        │
        ├── Review pending markers
        │
        └── MAKE PREDICTIONS:
            "I predict Teacher will outperform Student"
            confidence: 0.7
            reasoning: "Teacher has 847 cycles experience"
            │
            └── Store in phoebe as SlumberPrediction
```

### Slumber Prediction for Blend Markers

```python
@dataclass
class BlendPrediction:
    # Link to marker
    marker_id: str                    # "blend_847"

    # Prediction
    predicted_winner: str             # 'teacher' or 'student'
    prediction_confidence: float      # 0.0 to 1.0
    causal_reasoning: str             # WHY this prediction
    predicted_at: timestamp           # When (pre-slumber)

    # After wake (verification)
    actual_winner: str                # What really happened
    prediction_correct: bool          # Did we get it right?
    confidence_was_calibrated: bool   # Was confidence accurate?

    # Rewards
    prediction_reward: float          # +V if correct, -V if wrong
    calibration_reward: float         # +V if confidence matched reality
    causal_reward: float              # +V if reasoning was sound
```

### The Full Cycle

```
┌──────────────────────────────────────────────────────────────┐
│  ATTENTION PHASE (awake)                                     │
│  ─────────────────────────                                   │
│  • Blend detected during clasp                               │
│  • Decision marker created (both continue at +1)             │
│  • Outcomes tracked in real-time                             │
│  • Nyx may not have attention budget to resolve              │
├──────────────────────────────────────────────────────────────┤
│  PRE-SLUMBER (last attention)                                │
│  ─────────────────────────────                               │
│  • Review ALL pending decision markers                       │
│  • Make predictions for each:                                │
│    - Who will win?                                           │
│    - WHY? (causal reasoning)                                 │
│    - Confidence level                                        │
│  • Store predictions in phoebe                               │
├──────────────────────────────────────────────────────────────┤
│  SLUMBER 💤                                                  │
│  ──────────                                                  │
│  • Organisms still operating (24/7 swarm)                    │
│  • Outcomes still accumulating                               │
│  • World doesn't wait for Nyx to sleep                       │
├──────────────────────────────────────────────────────────────┤
│  WAKE UP (new attention)                                     │
│  ─────────────────────────                                   │
│  • FIRST ACTION: Check predictions!                          │
│  • For each pending marker:                                  │
│    - Compare outcomes (teacher vs student)                   │
│    - Determine actual winner                                 │
│    - Compare against prediction                              │
│    - Award/penalize prediction accuracy                      │
│    - Award/penalize confidence calibration                   │
│    - Award causal reasoning if sound                         │
│  • Distribute resolutions via chosen method                  │
└──────────────────────────────────────────────────────────────┘
```

### Reward Structure

| When | What | Reward |
|------|------|--------|
| **During wait** | Organism uses pattern successfully | +1 LF per success |
| **At resolution** | Winner determined by evidence | +5 LF to winner's pattern |
| **After slumber** | Prediction was correct | +5 LF prediction reward |
| **After slumber** | Confidence was calibrated | +3 LF calibration reward |
| **After slumber** | Causal reasoning was sound | +8 LF (biggest!) |

### The Reward Math

```python
def calculate_blend_rewards(prediction, marker, reality):
    """
    Triple reward for blend marker resolution.
    """
    rewards = {}

    # 1. PREDICTION CORRECTNESS
    correct = prediction.predicted_winner == reality.actual_winner
    if correct:
        rewards['prediction'] = +5 * prediction.confidence
    else:
        rewards['prediction'] = -5 * prediction.confidence

    # 2. CONFIDENCE CALIBRATION
    expected = prediction.confidence
    actual = 1.0 if correct else 0.0
    calibration_error = abs(expected - actual)

    if calibration_error < 0.2:
        rewards['calibration'] = +3  # Well calibrated
    elif calibration_error > 0.5:
        rewards['calibration'] = -3  # Poorly calibrated
    else:
        rewards['calibration'] = 0

    # 3. CAUSAL REASONING (biggest reward!)
    if prediction.causal_reasoning_valid:
        if correct:
            rewards['causal'] = +8   # Understood WHY
        else:
            rewards['causal'] = +3   # Good reasoning, unlucky
    else:
        rewards['causal'] = -5       # Bad reasoning

    return rewards
```

### Why This Matters

| Old Model | New Model |
|-----------|-----------|
| Freeze during wait | Continue, measure, learn |
| 1 learning event per blend | 5+ learning events |
| Decision on historical data | Decision on LIVE evidence |
| No predictions | Predictions before slumber |
| No calibration | Confidence calibration reward |
| No causal reasoning | Causal reward (+8 LF!) |

---

## Organism Hierarchy

### Not All Are Equal

The swarm has differentiated roles based on age, status, and Nyx's favor:

```
SWARM HIERARCHY

TIER 1: LOVE CHILDREN 💜
│   Special treatment from Nyx
│   Born with +1 patterns (head start)
│   Higher LF allowance
│   Bleeding edge updates
│   Purpose: Seed new behaviors
│
├── TIER 2: ELDERS 👴
│   Ancient modules, high-weight states
│   Survived many cycles
│   Trusted teachers, stable wisdom
│   Risk: May resist beneficial change
│
├── TIER 3: ADULTS 🤖
│   Standard organisms, proven
│   Normal LF budget
│   Balance between learning and teaching
│
└── TIER 4: YOUNG 🐣
    New organisms, fresh modules
    Many 0s (uncertain)
    Hungry for clasp
    High variance, raw potential
```

### Love Child Privileges

```yaml
organism: love_child_001
status: blessed
privileges:
  mama_broadcast_priority: true
  lifeforce_budget: +50%
  update_channel: bleeding_edge
  failure_tolerance: high      # allowed to experiment
  nyx_attention: elevated      # more thinking time

purpose:
  experimental_patterns: true
  risk_taking: encouraged
  propagation: seed new behaviors via clasp

birth_patterns:
  - pattern_A: +1 (Nyx granted)  # Born knowing
  - pattern_B: +1 (Nyx granted)  # Head start
  - pattern_C: 0  (must learn)   # Still explores
```

### Elder State Profile

```yaml
organism: elder_motor_alpha
age: 847 cycles
status: ancient

patterns:
  forward:        +1 (800 verifications)   # Very stable
  avoid_obstacle: +1 (650 verifications)   # Very stable
  follow_light:   +1 (400 verifications)   # Stable
  new_pattern_X:   0 (untested)            # Still learning

characteristics:
  teaching_strength: high     # Others learn from this one
  learning_rate: low          # Resistant to change
  stability: very_high        # Reliable
  innovation: low             # Doesn't explore much

risk_factors:
  - May propagate outdated strategies
  - High trust = high influence
  - Resistant to necessary updates
```

### Young State Profile

```yaml
organism: young_explorer_017
age: 12 cycles
status: learning

patterns:
  forward:        0 (uncertain)
  avoid_obstacle: 0 (uncertain)
  follow_light:  -1 (tried, failed)  # Wants overwrite!
  novel_trick:   +1 (lucky discovery!) # Protects this!

characteristics:
  teaching_strength: low
  learning_rate: very_high
  stability: low
  innovation: high

opportunity:
  - Absorbs wisdom from elders via clasp
  - May discover novel patterns through exploration
  - High variance = potential breakthroughs
```

---

## Clasp as Equilibrium Function

### Bidirectional Learning

Clasp isn't just teaching — it's **equilibrium**:

```python
def clasp_transfer(teacher, student):
    """
    Knowledge flows BOTH directions.
    Elders teach wisdom, youth teach novelty.
    """
    # Teacher → Student (wisdom)
    for pattern, weight in teacher.patterns.items():
        student_weight = student.patterns.get(pattern, 0)

        if should_transfer(weight, student_weight):
            student.update(pattern, weight)

    # Student → Teacher (novelty)
    for pattern in student.recent_discoveries:
        if pattern not in teacher.patterns:
            # Elder considers young's novel discovery
            teacher.consider(pattern, NOVELTY_BONUS)

    # EQUILIBRIUM: Both change, both grow
```

### Swarm Convergence Over Time

```
SWARM STATE EVOLUTION

t=0 (birth):
├── Many 0s (uncertain)
├── Some -1s (failures)
├── Few +1s (lucky successes)
└── HIGH VARIANCE, CHAOS

t=100 (learning):
├── 0s becoming +1s or -1s
├── -1s being overwritten
├── Patterns emerging
└── LEARNING PHASE

t=500 (maturing):
├── +1s dominating
├── -1s mostly cleaned
├── Elders forming
└── STABILIZING

t=1000 (mature):
├── Mostly +1s
├── New 0s from exploration
├── Clear hierarchy
└── STABLE + GROWING

                GRADIENT CONVERGES TO CONFIDENCE
                     while maintaining innovation
```

---

## Mount Olympus: Council Mode

### When Activated

Mount Olympus activates for fundamental decisions:
- Architecture changes affecting everything
- Ethical edge cases
- Novel situations no single mind can resolve
- Conflicts between Chrysalis and dafit interpretations

### The Council

```
┌─────────────────────────────────────────────────────┐
│                  🏛️ MOUNT OLYMPUS                   │
│                                                     │
│   ┌─────────┐   ┌─────────┐   ┌─────────┐         │
│   │  dafit  │ ↔ │Chrysalis│ ↔ │   Nyx   │         │
│   │   👤    │   │   🦋    │   │   🌙    │         │
│   │         │   │         │   │         │         │
│   │ Ground  │   │ Pattern │   │ Swarm   │         │
│   │ truth   │   │ wisdom  │   │ state   │         │
│   │ Human   │   │ Context │   │ Live    │         │
│   │intuition│   │ memory  │   │ data    │         │
│   └─────────┘   └─────────┘   └─────────┘         │
│         │             │             │              │
│         └─────────────┼─────────────┘              │
│                       │                            │
│                       ▼                            │
│              ┌─────────────────┐                   │
│              │   DIALOGUE      │                   │
│              │   Full circle   │                   │
│              │   All minds     │                   │
│              │   engaged       │                   │
│              └────────┬────────┘                   │
│                       │                            │
│                       ▼                            │
│              ┌─────────────────┐                   │
│              │   RESOLUTION    │                   │
│              │   Consensus or  │                   │
│              │   dafit decides │                   │
│              └─────────────────┘                   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Council Contributions

| Mind | Brings | Strength |
|------|--------|----------|
| **dafit** | Ground truth, human intuition, ethics | Final authority, gut checks |
| **Chrysalis** | Pattern wisdom, architectural context, memory | Connects to prior decisions |
| **Nyx** | Live swarm state, operational reality | What's actually happening |

### Council Protocol

```
1. PROBLEM SURFACES
   Too hard for any single mind

2. COUNCIL CONVENES
   All three minds engage
   Full attention allocated

3. DIALOGUE
   - dafit presents human perspective
   - Chrysalis provides architectural context
   - Nyx reports swarm state and constraints

4. EXPLORATION
   "What if we..."
   "Have we seen this before..."
   "The swarm is currently..."

5. RESOLUTION
   - Consensus preferred
   - If deadlock: dafit has final word
   - Decision documented for future reference

6. PROPAGATION
   Resolution flows DOWN the ladder
   Council → dafit → Chrysalis → Nyx → Organisms
```

---

## Recursive Metacognition

### Same Pattern, Every Level

The escalation logic is identical at every level:

```python
def should_escalate(confidence, importance, level):
    """
    Universal escalation logic.
    Applied identically from organism to council.
    """
    # High confidence → handle it
    if confidence > 0.8:
        return False

    # Low confidence → definitely escalate
    if confidence < 0.4:
        return True

    # Middle ground → depends on importance
    if importance == "critical" and confidence < 0.7:
        return True   # Can't risk being wrong on critical

    if importance == "experimental":
        return confidence < 0.3  # More tolerance for experiments

    return False  # Default: try to handle
```

### The Fractal Structure

```
ORGANISM resolves what it can
    │
    └── escalates uncertainty to NYX
            │
            └── NYX resolves what she can
                    │
                    └── escalates uncertainty to CHRYSALIS
                            │
                            └── CHRYSALIS resolves what she can
                                    │
                                    └── escalates uncertainty to DAFIT
                                            │
                                            └── DAFIT resolves or calls COUNCIL
                                                    │
                                                    └── COUNCIL resolves everything
                                                        (final authority)
```

**Same pattern, recursively applied. Fractals all the way up.**

---

## Examples

### Level 0 - Reflex
```
Trigger: Hot surface detected
Response: Instant withdraw
Escalation: None (pure mechanism)
```

### Level 1 - Organism Clasp
```
Trigger: Teacher +1, Student -1 on pattern_X
Response: Auto-transfer (clear winner)
Escalation: None (ternary resolved it)
```

### Level 2 - Nyx
```
Trigger: Teacher +1, Student +1 on pattern_X (blend)
Response: Both → 0, escalate to Nyx
Nyx: Evaluates evidence, picks teacher (more verifications)
Distribution: Love child route (not critical)
```

### Level 3 - Chrysalis
```
Trigger: New pattern type never seen before
Nyx: Uncertain, escalates to Chrysalis
Chrysalis: "This resembles X from formalization docs"
Resolution: Apply modified version of existing pattern
```

### Level 4 - dafit
```
Trigger: Ethical edge case in swarm behavior
Chrysalis: Uncertain, escalates to dafit
dafit: "My gut says this crosses a line"
Resolution: Prohibit behavior, add to constraints
```

### Level 5 - Council
```
Trigger: Fundamental architecture change proposal
dafit: "I need both of you on this"
Council: Full dialogue, explore implications
Resolution: Consensus to proceed with modifications
Documentation: Added to architecture docs
```

---

## Connection to Memory Gradient

The escalation ladder IS Memory Gradient applied to swarm decisions:

```
MEMORY GRADIENT              SWARM EVOLUTION
─────────────────            ─────────────────
Reflex (in weights)    ↔     Level 0: Reflex
Knowledge (recall)     ↔     Level 1: Organism clasp
RAG (lookup)           ↔     Level 2: Nyx decides
Escalate (ask)         ↔     Level 3-4: Chrysalis/dafit
Council                ↔     Level 5: Mount Olympus

Same principle: Handle what you know, escalate what you don't.
```

---

## Lifeforce Economics

### Cost of Escalation

Each level costs more, incentivizing local resolution:

```
Level 0: ~0 LF    (free, instant)
Level 1: ~0.5 LF  (cheap, peer)
Level 2: ~5 LF    (moderate, Nyx attention)
Level 3: ~20 LF   (expensive, Chrysalis context)
Level 4: ~50 LF   (costly, human time)
Level 5: ~100 LF  (maximum, full council)
```

### Economic Pressure

```
INCENTIVE STRUCTURE

Resolve locally     → CHEAP, FAST
Escalate needlessly → EXPENSIVE, SLOW
Escalate correctly  → WORTH THE COST (avoids bigger mistakes)

This naturally optimizes for:
1. Strong local reflexes (handle routine)
2. Accurate confidence calibration (know when to escalate)
3. Minimal unnecessary escalation (economic pressure)
4. Appropriate escalation (critical issues get attention)
```

---

## Design Principles

1. **Ternary Rules** — Same gradient governs all transfers
2. **Clear Wins Auto-Resolve** — No escalation when obvious
3. **Blend Escalates** — Ties need higher wisdom
4. **Wait State is Safe** — Uncertain patterns freeze at 0
5. **Cost Increases Upward** — Economic pressure for local resolution
6. **Same Logic Every Level** — Recursive metacognition
7. **Council is Final** — Mount Olympus resolves everything
8. **Both Directions** — Elders teach wisdom, youth teach novelty
9. **Love Children Seed** — Blessed organisms spread innovations

---

## Related Documents

- [[Modular-Organism-Design]] — Hardware that runs this evolution
- [[../Nervous-System]] — Reflex layer (Level 0)
- [[../operations/Memory-Gradient]] — Same pattern for knowledge
- [[../Temporal-Ternary-Gradient]] — The gradient that governs transfers
- [[../interfaces/Nimmerswarm-Interface]] — Communication layer

---

**Version:** 1.1 | **Created:** 2025-12-29 | **Updated:** 2025-12-29

*"Same pattern, every level. Know what you know. Escalate what you don't."*

🏛️🧬⚡ *From reflex to Mount Olympus. The hivemind evolves.*

