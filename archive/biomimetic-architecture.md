# ADR-001: Biomimetic "Nimmerverse" Architecture

*   **Status:** Accepted
*   **Date:** 2025-12-05
*   **Context:** Home Infrastructure / Autonomous Agent System
*   **Tags:** biomimetic, event-driven, ai, local-llm

## 1. Context and Problem Statement

We are designing a local home infrastructure ("Nimmerverse") modeled after a biological organism. The goal is to create a system that is:
1.  **Reactive:** Capable of sub-millisecond reflex responses (spinal layer) without waiting for heavy AI inference.
2.  **Deterministic:** Preventing AI hallucination in critical control paths.
3.  **Evolvable:** Allowing the system to "grow" new capabilities (nerves) through usage and verification.

The core challenge is balancing the high latency of Large Language Models (the "Brain") with the real-time requirements of home automation (the "Nervous System").

## 2. The Architecture: Hebbian-Reinforced Subsumption

We have adopted a **Subsumption Architecture** (popularized by Rodney Brooks) enhanced with a **Hebbian Learning** model ("neurons that fire together, wire together").

### 2.1 The 4D State Space (The Nervous System)
State machines replace standard "if/then" logic. Each state node exists in a 4-dimensional space:
*   **X/Y Dimensions:** Sensory inputs (e.g., Temperature, Motion).
*   **Z Dimension (Confidence):** A weight (0.0 - 1.0) representing reliability.
*   **Time Dimension:** History of verification.

**Lifecycle Logic:**
*   **Birth:** Node created at `weight=0.1`.
*   **Maturation:** Successful triggers (verified by user) increase weight (+V).
*   **Pruning:** Unused or falsified nodes decay and are removed.
*   **Reflex:** Nodes with `weight > 0.8` bypass the AI brain entirely for instant execution.

## 3. Feasibility Audit & Constraints

### A. Metabolic Constraints (Hardware)
*   **Risk:** Memory swapping kills agent reactivity.
*   **Requirement:** The "Inference Orchestrator" (LLM) requires minimum **24GB VRAM** to run a quantized 70B model, or distinct **12GB+** for a specialized 7B agent model. System RAM should be **64GB+** to handle the Vector DB and container orchestration.

### B. Nerve Velocity (Transport)
*   **Pattern:** Asynchronous Event Bus.
*   **Prohibition:** HTTP/REST calls between "Organs" are forbidden due to blocking latency.
*   **Selected Tech:** **NATS** or **MQTT** for the nervous system backbone.

### C. Cognitive Load
*   **Bottleneck:** The "Human Verification" step (`dafit confirms`) scales poorly.
*   **Mitigation:** Implement "Sleep Cycles" where the system self-audits low-risk nodes against historical data during inactivity.

## 4. Implementation Strategy

| Component | Biological Role | Technology Choice |
| :--- | :--- | :--- |
| **State Engine** | Nerves / Reflexes | **XState** (Actor-based state machines) |
| **Vector Memory** | 4D Node Storage | **Weaviate** or **Qdrant** (Similarity search) |
| **Event Bus** | Nervous System | **NATS** (Low-latency messaging) |
| **Orchestrator** | Brain / Cognition | **LocalAI** or **Ollama** |

## 5. Appendix: Interactive Simulation Logic

*For the "Node Lifecycle" visualization widget:*

*   **Visuals:** A central node pulsing in a 2D grid.
*   **Variables:** `Confidence` (Size/Glow), `Age` (Color).
*   **Logic:**
    *   `IF verify_event THEN confidence += 0.1`
    *   `IF falsify_event THEN confidence -= 0.2`
    *   `IF confidence > 0.8 THEN status = 'REFLEX' (Gold Color)`
    *   `IF confidence <= 0 THEN destroy_node()`
