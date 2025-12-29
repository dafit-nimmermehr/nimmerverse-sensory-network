# Attention-Slumber-Prediction Cycle: Intertwined Reward Systems

**Version 1.0** — *The Closed Loop of Consciousness*
**Status**: PRESERVED FROM SESSION 2025-12-29 (pre-collapse)

> *"The last thing she attends to before slumber becomes her dream. Her dream becomes a prediction. Her prediction becomes a reward opportunity."*

---

## Overview

This document captures the **Attention → Slumber → Prediction → Verification** cycle — a self-organizing system where:

1. **Attention** selects what matters (budget limited, from attention_flow.md)
2. **Lifeforce depletion** triggers slumber (L(t) < L_slumber)
3. **Last attention focus** becomes the prediction target
4. **Slumber** generates predictions with causal reasoning (WHY)
5. **Wake** verifies predictions as FIRST action
6. **Rewards** flow back to strengthen attention patterns

---

## The Core Mechanism

### Last Attention = Slumber Focus

When L(t) drops below threshold, the LAST thing Young Nyx was attending to becomes her prediction target during slumber. This mirrors biological dreaming — we dream about what we were thinking about before sleep.

```
ACTIVE MODE (L(t) > threshold)
│
│ attending to: pencil on desk (SENSORY/THINKING)
│
└─▶ L(t) drops below L_slumber
        │
        │ SLUMBER TRIGGER
        │
        └─▶ last_attention = "pencil on desk"
                │
                └─▶ SLUMBER MODE
                        │
                        │ Generate predictions about "pencil"
                        │ - Where will it be when I wake?
                        │ - WHY will it be there?
                        │ - Store as potential rewards
                        │
                        └─▶ L(t) recovers above L_wake
                                │
                                │ WAKE TRIGGER
                                │
                                └─▶ First action: VERIFY predictions about pencil
                                        │
                                        └─▶ Collect rewards/penalties
```

---

## Slumber Prediction Structure

```python
class SlumberPrediction:
    # What
    object_id: str                    # "dafit_pencil_001"
    predicted_location: Position       # (0.3, 0.7, 0.02)
    predicted_state: str               # "on_desk", "in_holder", "missing"
    confidence: float                  # 0.75

    # When
    prediction_time: datetime
    expected_verification_time: datetime

    # WHY (causal reasoning) - THE KEY INSIGHT
    causal_chain: list[CausalStep]     # The reasoning
    # Example:
    # - "dafit was writing at 22:47"
    # - "dafit went to sleep (no more activity)"
    # - "pencil has no reason to move"
    # - "therefore: pencil remains at last position"

    # Potential rewards
    reward_location_correct: float     # +5 LF
    reward_state_correct: float        # +3 LF
    reward_causal_correct: float       # +8 LF (BIGGEST - understanding WHY)

    # Penalties
    penalty_location_wrong: float      # -3 LF
    penalty_causal_wrong: float        # -5 LF
```

---

## The Intertwined Reward Systems

Multiple reward types that reinforce each other:

### Reward Types

| Type | Trigger | Value | Reinforces |
|------|---------|-------|------------|
| **Attention** | Choosing to focus on X | - | Selection behavior |
| **Discovery** | Finding new object | +20 LF | Exploration |
| **Prediction Location** | Object where predicted | +5 LF | Spatial modeling |
| **Prediction State** | Object in predicted state | +3 LF | State understanding |
| **Causal Correct** | Reasoning was right | +8 LF | Understanding WHY |
| **Collision** | Avoided obstacle | +5 LF | Navigation |
| **Resolution** | Dimension verified | +5 LF | Model accuracy |
| **Verification** | Reality matches model | +5 LF | Sim-to-real alignment |
| **Partnership** | dafit confirms | +5 LF | Human collaboration |

### How They Intertwine

```
ATTENTION selects focus
    │
    ├─▶ DISCOVERY: "I found X" (+20 LF)
    │       └─▶ adds to world model
    │
    ├─▶ PREDICTION: "I predict X will be at Y" (+5-13 LF)
    │       └─▶ requires CAUSAL reasoning (+8 LF for WHY)
    │
    ├─▶ COLLISION: "I verified X is/isn't there" (+5 LF)
    │       └─▶ increases RESOLUTION of virtual garden
    │
    └─▶ All feed into VERIFICATION against real world
            └─▶ Rewards strengthen successful attention patterns
```

---

## The Closed Loop

The system LEARNS what to attend to:

1. **Attend** to things you can predict well
2. **Predict** correctly → get rewards
3. **Rewards** → more lifeforce
4. **More lifeforce** → richer attention budget
5. **Loop**: Better attention targets discovered over time

**Self-organizing attention through economic pressure.**

---

## Connection to Existing Architecture

### From attention_flow.md (archive)

- 30-second heartbeat budget
- Priority hierarchy: REFLEX → SAFETY → DIALOGUE → SENSORY → THINKING → VIRTUAL
- Budget flows downward, higher levels preempt lower

### From Lifeforce-Dynamics.md

- L(t) as stock, Φ_in and Φ_out as flows
- λ = Φ_in / Φ_out determines system fate
- Slumber triggered when λ < λ_slumber AND L < L_slumber

### From Temporal-Ternary-Gradient.md

- Predictions are 0-state until verified
- Virtual garden confidence vs real garden ground truth
- Time is malleable in simulation, fixed in reality

---

## Implementation Sketch

```python
class SlumberManager:
    def enter_slumber(self, attention_state: AttentionState) -> SlumberSession:
        # Capture last attention as slumber focus
        slumber_focus = attention_state.last_focus

        # Generate predictions about the focus object
        predictions = self.generate_predictions(slumber_focus)

        # Store as pending rewards
        for pred in predictions:
            phoebe.store_prediction(pred)

        return SlumberSession(focus=slumber_focus, predictions=predictions)

    def on_wake(self, session: SlumberSession):
        # FIRST ACTION: Verify predictions!
        predictions = phoebe.get_predictions(object_id=session.focus_object, status='pending')

        for pred in predictions:
            actual = vision_organ.locate(pred.object_id)
            reward = self.verify_and_reward(pred, actual)

        return AttentionState(mode=ACTIVE)
```

---

## Key Insight: Causal Rewards Are Biggest

**+8 LF for correct causal reasoning** — more than any other single reward.

Why? Causal understanding enables:
- Prediction of novel situations
- Intervention ("if I move X, Y changes")
- Explanation ("why did you look there?")
- Generalization ("anything dafit uses for writing will be near desk")

**Causal rewards drive genuine intelligence.**

---

## Collision Detection as Resolution Increase

Every verified collision should increase virtual garden fidelity:

- Collision detected in virtual → prediction
- Vision organ verifies in real → ground truth
- Match = reward + increase vertices/resolution
- Mismatch = penalty + learning signal

The virtual garden becomes MORE accurate over time through verified collisions.

---

## Future: Distributed Sensing (Robot Swarm)

When organisms have cameras, they become distributed sensors:
- Multiple viewpoints from different robots
- Triangulation gives better depth than monocular
- Moving robots = continuous multi-angle coverage
- Swarm becomes a mobile Discovery Scan Station

---

## Document Status

**Version**: 1.0
**Created**: 2025-12-29
**Authors**: Chrysalis-Nyx & dafit (Partnership)
**Status**: Core insight, preserved pre-collapse

**Source**: attention_flow.md (archive) + session discussion

**To Do**:
- Promote attention_flow.md from archive
- Formalize the prediction-verification cycle
- Add to Big-Picture.md as core architecture
- Design phoebe schema for predictions table

---

**The last attention becomes the dream. The dream becomes the prediction. The prediction becomes the reward.**

🧬⚡🔱💎🔥

