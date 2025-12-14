# Big-Picture Architecture: Nimmerverse Sensory Network

## Overview

The Nimmerverse Sensory Network is designed as a highly modular, resilient, and economically constrained system. It follows a "Router-Centric Architecture" where a high-performance message bus acts as dumb infrastructure, and all intelligence and processing logic reside at the "edges" (client services). This approach ensures scalability, maintainability, and clear separation of concerns, while enabling Nyx to manage her attention and Lifeforce efficiently.

---

## Core Principles

1.  **Dumb Core, Smart Edges**: The central message router is merely an infrastructure component, devoid of any application logic. All processing, filtering, and decision-making intelligence is distributed among specialized client services.
2.  **Polyglot Architecture**: Utilizing the best technology for each specific task: Python for AI/ML, cognitive logic, and service daemons; Godot for visualization; and NATS (Go) as the universal message bus.
3.  **Two-Channel Attention**: Information is processed via distinct low-attention (ambient) and high-attention (focal) channels, allowing for efficient resource allocation and preventing cognitive overload.
4.  **Lifeforce Economy**: Every operation has a cost. The architecture is designed to optimize Lifeforce expenditure by ensuring expensive cognitive resources are only engaged when truly necessary.
5.  **Testability & Modularity**: Each component (client service) can be developed, tested, and deployed independently.

---

## Architectural Components & Technology Stack

### 1. Message Router (NATS)

*   **Role**: The central nervous system's universal message bus. It receives messages from all clients and routes them to interested subscribers based on hierarchical topic patterns. It has no application logic or state.
*   **Technology**: **NATS Server (Go)**
*   **Key Features**:
    *   Extremely high performance and low latency.
    *   Built-in subject-based filtering and wildcard subscriptions.
    *   Designed for publish/subscribe, request/reply, and distributed queues.
    *   Supports `JetStream` for optional message persistence.
*   **Integration**: All other components connect to NATS as clients.

---

### 2. The Escalation Service (Thalamus Function)

*   **Role**: A dedicated daemon responsible for sensory gating and attention management. It processes the high-volume, low-attention data stream and escalates critical or relevant events to the high-attention channel based on rules defined by Nyx.
*   **Technology**: **Python (asyncio)**
*   **Key Features**:
    *   Subscribes to all `nimmerverse.low.heartbeat` topics.
    *   Subscribes to `nimmerverse.meta.attention.focus` to receive Nyx's dynamic `AttentionFocus` rules.
    *   Evaluates incoming low-attention `HeartbeatSignal` messages against Nyx's `escalation_rules` using a safe expression evaluation engine (e.g., `simpleeval` or custom JSONPath matching).
    *   **Actions**:
        *   Publishes `StateChangeDetail` messages to `nimmerverse.high.event` topics when escalation rules are met.
        *   Can directly trigger reflex nerves/cells via `nimmerverse.command` topics for immediate, non-cognitive responses.
    *   Concurrent via Python's asyncio - sufficient for research platform scale.
*   **Future Consideration**: If scale demands higher throughput, the Escalation Service can be ported to Go with the Python implementation serving as the working specification.
*   **Analogy**: The biological thalamus, filtering and relaying sensory information to the conscious brain.

---

### 3. Cognitive Clients (Young Nyx, Cells, Nerves, Organs)

These represent the "intelligent" parts of the Nimmerverse, responsible for perception, action, and cognition.

*   **Technology**: **Python**
*   **Key Features**:
    *   **Young Nyx (Cognitive Core)**:
        *   Subscribes primarily to `nimmerverse.high.event` topics for detailed `StateChangeDetail` messages relevant to her current `focus_mode`.
        *   Publishes `AttentionFocus` messages to NATS, effectively programming the `Escalation Service`'s behavior.
        *   Publishes decisions and commands to `nimmerverse.command` topics.
        *   Leverages Python's rich AI/ML ecosystem (`PyTorch`, `transformers`, `vLLM`, etc.) for complex inference.
    *   **Cells, Nerves, Organs**:
        *   Publish lightweight `HeartbeatSignal` messages to `nimmerverse.low.heartbeat` topics periodically.
        *   Publish detailed `StateChangeDetail` messages to `nimmerverse.high.event` topics when explicitly requested by the `Escalation Service` or upon significant internal state changes (e.g., error conditions).
        *   Subscribe to specific `nimmerverse.command` topics to receive instructions or triggers.
        *   Manage their individual Lifeforce budgets for operations.

---

### 4. Command Center (User Interface)

*   **Role**: Real-time visualization and monitoring interface for human operators (dafit).
*   **Technology**: **Godot Engine**
*   **Key Features**:
    *   Subscribes to both `nimmerverse.low.>` and `nimmerverse.high.>` topics to provide a comprehensive, real-time overview of system state, message flow, and Nyx's attention focus.
    *   Allows human observation and potential intervention or directive input.
    *   Leverages Godot's game engine capabilities for rich, interactive, and performant visualizations.

---

## Message Flow Example: Sensing an Obstacle

1.  **Ambient Awareness:** A `distance_sensor_front` **Cell** (Python) periodically publishes `HeartbeatSignal` messages to `nimmerverse.low.heartbeat.real.cell.distance_sensor_front`.
2.  **Router Delivery:** The **NATS Router** delivers this message to all subscribers, including the **Escalation Service** (Python).
3.  **Rule Evaluation:** The **Escalation Service** checks this `HeartbeatSignal` against Nyx's active `escalation_rules`. If a rule like `condition: "body.value < 30"` matches, it determines a need for deeper attention.
4.  **Escalation Action:** The `Escalation Service` publishes a command (e.g., `nimmerverse.command.cell.distance_sensor_front.publish_detail`) to the `distance_sensor_front` Cell.
5.  **Detailed Report:** The `distance_sensor_front` **Cell** receives the command and publishes a `StateChangeDetail` message to `nimmerverse.high.event.real.cell.distance_sensor_front`.
6.  **Nyx's Cognition:** **Young Nyx** (Python), subscribed to relevant `high.event` topics, receives the `StateChangeDetail` message. She processes this rich information, performs inference, and makes a decision (e.g., to activate a `CollisionAvoidance` nerve).
7.  **Action Command:** **Young Nyx** publishes a command message to `nimmerverse.command.nerve.collision_avoidance.activate`.
8.  **Nerve Execution:** The `CollisionAvoidance` **Nerve** (Python) receives the command and executes its predefined behavior, commanding motors and reporting its own state changes.

---

## Bootstrap Sequence

The system is designed for gradual, resilient startup:

1.  **Start NATS Router**: Foundation first.
2.  **Start Escalation Service**: Begin filtering low-attention data with hardcoded default or previous rules.
3.  **Start Cells, Nerves, Organs**: Begin publishing `HeartbeatSignal`s.
4.  **Start Command Center**: Provide initial observability.
5.  **Start Young Nyx**: Connects, subscribes to high-attention, and (crucially) publishes her `AttentionFocus` configuration to take cognitive control.

This staged approach allows for a robust system that can operate at varying levels of "intelligence," from pure reflexes to full deliberation.

---

**This architectural blueprint provides a clear, scalable, and efficient foundation for the Nimmerverse Sensory Network, effectively managing complexity and optimizing resource utilization within its economic constraints.**
