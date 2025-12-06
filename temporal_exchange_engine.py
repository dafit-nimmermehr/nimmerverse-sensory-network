"""
Temporal Exchange Engine
========================
ADR-003 Implementation: The economics calculator for sim2real decisions.

This module implements the core decision-making primitive for Nyx's
uncertainty resolution. Given a target confidence level, it determines
whether simulation is worth the lifeforce cost, or if reality is the
only remaining teacher.

Reference: ADR-002-temporal-ternary-gradient.md
"""

import math
from dataclasses import dataclass
from typing import Literal


@dataclass
class TemporalState:
    """Represents the current state of a pattern or nerve's confidence."""
    confidence: float
    source: Literal['virtual', 'real']
    cost_incurred: float


class TemporalExchangeEngine:
    """
    The Exchange Rate Calculator.

    Determines optimal strategy for resolving uncertainty:
    - When to invest lifeforce in simulation
    - When simulation is futile and reality must teach
    """

    def __init__(self, sim_fidelity: float = 0.75):
        """
        Args:
            sim_fidelity (0.0-1.0): The 'Truth Ceiling' of the Virtual Garden.
                                    Even perfect simulation is only this % real.
        """
        self.fidelity_cap = sim_fidelity
        # Calibration: How much Lifeforce buys 1 unit of raw confidence?
        self.learning_rate = 0.1

    def calculate_virtual_confidence(self, lifeforce_spent: float) -> float:
        """
        Calculate grounded confidence from lifeforce investment.

        Diminishing returns: The first 10 LF buys a lot of confidence.
        The next 10 buys less. It never exceeds the fidelity_cap.

        Formula: Cap * (1 - e^(-k * LF))
        """
        raw_knowledge = 1.0 - math.exp(-self.learning_rate * lifeforce_spent)
        grounded_confidence = raw_knowledge * self.fidelity_cap
        return grounded_confidence

    def get_optimal_strategy(self, target_confidence: float) -> dict:
        """
        Ask Nyx: 'Is it worth simulating this?'

        Returns:
            dict with keys:
                - action: 'SIMULATE' or 'DEPLOY_TO_REALITY'
                - reason: Human-readable explanation
                - lifeforce_budget: Required LF (0 if reality is needed)
        """
        # 1. Check if the target is even possible in Virtual
        if target_confidence > self.fidelity_cap:
            return {
                "action": "DEPLOY_TO_REALITY",
                "reason": f"Target {target_confidence} exceeds Sim Fidelity ({self.fidelity_cap}). Simulation is futile.",
                "lifeforce_budget": 0
            }

        # 2. Calculate required Lifeforce to reach possible target
        # Inverse of the exponential decay formula
        required_lf = -math.log(1 - (target_confidence / self.fidelity_cap)) / self.learning_rate

        return {
            "action": "SIMULATE",
            "reason": f"Spend {required_lf:.2f} LF to reach {target_confidence} confidence.",
            "lifeforce_budget": round(required_lf, 2)
        }


# --- Usage Example ---
if __name__ == "__main__":
    engine = TemporalExchangeEngine(sim_fidelity=0.8)

    # Scenario A: Nyx wants 99% certainty (Impossible in Sim)
    print(engine.get_optimal_strategy(0.99))
    # Output: DEPLOY_TO_REALITY (Simulation is futile)

    # Scenario B: Nyx wants 70% certainty (Possible)
    print(engine.get_optimal_strategy(0.70))
    # Output: SIMULATE (Spend ~20 LF)
