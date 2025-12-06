# ADR-002: Temporal-Ternary Gradient & Sim2Real Strategy

*   **Status:** Accepted
*   **Date:** 2025-12-05
*   **Context:** Autonomous Agent Decision Making / Uncertainty Management
*   **Tags:** ternary-logic, sim2real, active-learning, economics

## 1. Context and Problem Statement

In the Nimmerverse, the agent (Nyx) frequently encounters the **"0-State"** (Unknown/Uncertainty).

*   **Traditional Binary Logic:** Forces a premature true/false decision, leading to errors.
*   **Standard Ternary Logic:** Allows a "null" state but offers no path to resolve it.
*   **The Constraint:** Real-world verification is slow and risky; simulation is fast but hallucinatory.

We need a protocol to "spend" system resources (Lifeforce) to resolve the 0-State into a +1 (Truth) or -1 (Falsehood) efficiently.

## 2. The Solution: Temporal-Ternary Gradient

We treat the **0-State** not as a static void, but as a **gradient of investment** across two time domains.

### The Two Domains
1.  **Virtual Garden (Simulation):**
    *   **Currency:** Lifeforce (Compute Energy).
    *   **Time Physics:** Malleable (1000x speed).
    *   **Output:** Statistical Confidence (Epistemic Probability).
2.  **Real Garden (Physical Reality):**
    *   **Currency:** Time (Wall-clock).
    *   **Time Physics:** Fixed (1x speed).
    *   **Output:** Ground Truth (Ontological Fact).

## 3. Strategic Logic: The Fidelity Discount

To prevent **Sim2Real Hallucinations** (where an agent is confident in simulation but fails in reality), we introduce a mandatory **Fidelity Discount** variable.

*   **Risk:** `Virtual Confidence 0.99` in a `50% Accurate Sim` = `Real Confidence 0.495`.
*   **Mandate:** Nyx must never act on raw virtual confidence. She must calculate `grounded_confidence` before deploying to the Real Garden.

## 4. Data Structure Standard

The state object for any pattern or nerve must track both the **Value** (Ternary) and the **Economic Investment** (Temporal).

```python
state = {
    "value": 0,              # -1 (Fail), 0 (Unknown), 1 (Pass)

    # The Sim2Real Bridge
    "raw_confidence": 0.95,  # Statistical confidence from Virtual runs
    "sim_fidelity": 0.70,    # CONSTANT: How accurate is the simulation?

    # The Decision Metric (The Anchor)
    # Nyx uses THIS to decide when to trigger a Real World test.
    "grounded_confidence": 0.665, # (raw_confidence * sim_fidelity)

    "economics": {
        "lifeforce_spent": 45.0,      # Compute cost sunk
        "real_time_saved_min": 120    # Time bought via simulation
    }
}
```

## 5. Decision Protocol (The Exchange Rate)

Nyx calculates the **Opportunity Cost** of the 0-State:

1.  **High Urgency:** Spend heavy Lifeforce to max out `raw_confidence` in seconds, then deploy.
2.  **Low Urgency:** Trickle-charge `raw_confidence` in background sims, or wait for passive Real World data.
3.  **The Cap:** Virtual optimization stops when `raw_confidence > sim_fidelity`. Beyond this point, simulation yields diminishing returns. Only Reality can increase confidence further.
