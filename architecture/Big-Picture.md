# Big-Picture Architecture: Nimmerverse Sensory Network

**Version 5.0** — *The Complete Architecture*

> *"From electrons to consciousness. From hardware to wisdom."*

---

## Overview

The Nimmerverse Sensory Network is a sovereign, economically-constrained cognitive architecture. It follows a **Router-Centric Architecture** where a high-performance message bus (NATS) acts as dumb infrastructure, and all intelligence resides at the edges. The system spans four layers: physical hardware, atomic state machines (cells), behavioral compositions (nerves), and emergent patterns (organisms).

**Key innovations:**
- **Hybrid Reflex Homes** — Different types of learned patterns live in different places (hardware, cells, nerves, weights)
- **Lifeforce Economy** — Every operation has a cost, tracked and aggregated system-wide
- **Slumber/Wake Cycles** — System-wide activity states driven by environmental and economic conditions
- **Wellbeing Policies** — Self-care and sustainability built into the architecture, not bolted on

---

## Core Principles

1. **Dumb Core, Smart Edges**: The message router has no application logic. All intelligence is distributed among specialized services.

2. **Polyglot Architecture**: Best technology for each task:
   - **Python**: AI/ML, cognitive logic, cells, nerves
   - **Go (NATS)**: Universal message bus
   - **Godot**: Visualization and monitoring
   - **C/Firmware**: Hardware reflexes (ESP32)

3. **Two-Channel Attention**: Low-attention (ambient heartbeats) and high-attention (focal events) channels prevent cognitive overload.

4. **Lifeforce Economy**: Every operation costs Lifeforce. The architecture optimizes expenditure, ensuring expensive resources engage only when necessary.

5. **Hybrid Reflex Homes**: Learned patterns live in their optimal location — hardware for survival, cells for computation, nerves for behavior, weights for cognition.

6. **Earned Trust**: Reflexes form through verification, not configuration. Weight > 0.8 is earned, not assigned.

7. **Graceful Degradation**: Every component has failure modes that don't crash the system. Slumber mode preserves lifeforce when resources are scarce.

---

## Physical Infrastructure

The nimmerverse runs on sovereign hardware. No cloud dependencies. Weights never leave home.

### Cluster Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    K8S CLUSTER: NIMMERVERSE                          │
│                    VLAN 30 (10.0.30.0/24)                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │              SATURN (Control Plane)                          │    │
│  │              K3s master, etcd, scheduler                     │    │
│  │              RTX 3090 24GB (test/staging)                    │    │
│  └──────────────────────────┬──────────────────────────────────┘    │
│                              │ 10G spine                             │
│         ┌────────────────────┴────────────────────┐                 │
│         │                                         │                 │
│         ▼                                         ▼                 │
│  ┌─────────────────────────────┐   ┌─────────────────────────────┐ │
│  │     P8 #1 (Womb)            │   │     P8 #2 (Senses)          │ │
│  │     BARE METAL UBUNTU       │   │     BARE METAL UBUNTU       │ │
│  │     K8s Worker Node         │   │     K8s Worker Node         │ │
│  │                             │   │                             │ │
│  │  GPU: PRO 6000 Max-Q 96GB   │   │  GPUs: 2-4x RTX 4000 Ada   │ │
│  │  Role: Cognitive Core       │   │  Role: Organs (STT/TTS/Vis)│ │
│  │  Young Nyx lives here       │   │  Sensory processing        │ │
│  │                             │   │                             │ │
│  │  Labels:                    │   │  Labels:                    │ │
│  │    gpu=pro6000              │   │    gpu=ada4000              │ │
│  │    role=womb                │   │    role=senses              │ │
│  │    vram=96gb                │   │    vram=40-80gb             │ │
│  └─────────────────────────────┘   └─────────────────────────────┘ │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Network Topology

```
                         INTERNET
                             │
                             ▼
                        [ Modem ]
                             │ 1G (em0)
                             ▼
                 ┌───────────────────────┐
                 │   OPNsense Firewall   │
                 │   LAGG: 20G to spine  │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │   CRS309 (Spine)      │
                 │   8x SFP+ 10G         │
                 └───┬───────┬───────┬───┘
                     │       │       │
         ┌───────────┘       │       └───────────┐
         ▼                   ▼                   ▼
   ┌───────────┐      ┌───────────┐      ┌───────────┐
   │  P8 Womb  │      │ P8 Senses │      │  Saturn   │
   │   10G     │      │   10G     │      │   10G     │
   └───────────┘      └───────────┘      └───────────┘
```

### K8s Namespaces

| Namespace | Contents | Runs On |
|-----------|----------|---------|
| `nimmerverse-infra` | NATS, Prometheus, Grafana | Any node |
| `nimmerverse-nervous` | Escalation, Math Cells, Behavior Nerves | Any node |
| `nimmerverse-cognitive` | Young Nyx (main inference) | Womb (PRO 6000) |
| `nimmerverse-organs` | STT, TTS, Vision | Senses (Ada 4000s) |

---

## Layered Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ORGANISM                                      │
│            (emergent pattern from nerve interactions)                │
│                                                                      │
│  Identity emerges from: nerve configuration + history + reflexes    │
├─────────────────────────────────────────────────────────────────────┤
│                         NERVES                                       │
│           (behavioral state machines composing cells)                │
│                                                                      │
│  Collision Avoidance, Charging Seek, Conversation, Slumber          │
├─────────────────────────────────────────────────────────────────────┤
│                         CELLS                                        │
│     (atomic state machines: sensors, motors, organs, math)          │
│                                                                      │
│  Sensor Cells: distance, light, battery, IMU                        │
│  Motor Cells: motors, servos                                        │
│  Organ Cells: speech_stt, speech_tts, vision_detect                 │
│  Math Cells: economy_aggregator, wake_evaluator, slumber_evaluator  │
├─────────────────────────────────────────────────────────────────────┤
│                       HARDWARE                                       │
│            (ESP32, GPUs, microphones, speakers, sensors)             │
│                                                                      │
│  Hardware reflexes live here (weight > 0.8 safety patterns)         │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Cell Categories

Cells are atomic state machines. Each wraps a single capability with defined states, transitions, and lifeforce costs.

### Sensor Cells (Input)
Wrap hardware sensors. Expose readings as state machine outputs.

| Cell | Hardware | Key Output |
|------|----------|------------|
| `distance_sensor_front` | IR sensor | `distance_cm`, `confidence` |
| `battery_monitor` | ADC | `voltage`, `percentage` |
| `light_sensor` | Photoresistor | `lux`, `direction` |
| `solar_input` | Solar panel | `watts`, `sufficient` |

### Motor Cells (Output)
Wrap actuators. Provide feedback on execution.

| Cell | Hardware | Key Feedback |
|------|----------|--------------|
| `motor_left` | DC motor + encoder | `actual_velocity`, `stall_detected` |
| `servo_camera` | Servo motor | `angle`, `at_target` |

### Organ Cells (Complex Inference)
Wrap expensive GPU-based inference. Lifeforce-gated.

| Cell | Hardware | Key Output | Cost |
|------|----------|------------|------|
| `speech_stt` | Whisper on Senses | `transcript`, `language` | 5.0 LF |
| `speech_tts` | TTS on Senses | `audio_playing` | 4.0 LF |
| `vision_detect` | YOLO on Senses | `objects[]`, `bboxes[]` | 8.0 LF |

### Math Cells (Computation)
Aggregate and evaluate metrics. Enable system-wide awareness.

| Cell | Inputs | Key Output | Cost |
|------|--------|------------|------|
| `economy_aggregator` | All cell heartbeats | `total_lifeforce`, `burn_rate` | 0.1 LF |
| `wake_evaluator` | economy, light, queue | `should_wake`, `wake_reason` | 0.1 LF |
| `slumber_evaluator` | economy, sensors | `should_slumber`, `confidence` | 0.1 LF |

```python
class EconomyAggregatorCell(StateMachine):
    """
    Collects lifeforce readings from all cells.
    Computes system-wide economy state.
    """
    states = [IDLE, COLLECTING, COMPUTING, REPORTING]

    outputs = {
        "total_lifeforce": float,
        "solar_input": float,
        "burn_rate": float,          # LF/minute
        "reserve_hours": float,
        "economy_health": str,       # "thriving" / "stable" / "critical"
    }

    costs = {
        (IDLE, COLLECTING): 0.0,     # Passive listening
        (COLLECTING, COMPUTING): 0.05,
        (COMPUTING, REPORTING): 0.05,
        (REPORTING, IDLE): 0.0,
    }
```

---

## Hybrid Reflex Homes

Different types of learned patterns live in different locations. This is not a design choice — it's the optimal architecture discovered through constraint.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    REFLEX HOME HIERARCHY                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  LAYER 0: HARDWARE (ESP32/Microcontroller)                          │
│  ───────────────────────────────────────────                        │
│  • Safety reflexes: temp_danger, collision_imminent                 │
│  • Survival reflexes: battery_critical, motor_stall                 │
│  • Latency: <10ms                                                   │
│  • Works even if brain is DOWN                                      │
│  • True spinal cord — no Python, no network                         │
│                                                                      │
│  LAYER 1: MATH CELLS (Python/Fast State Machines)                   │
│  ───────────────────────────────────────────                        │
│  • Sensor aggregation: economy_aggregator                           │
│  • Threshold logic: wake_evaluator, slumber_evaluator               │
│  • Latency: <50ms                                                   │
│  • Flexible, updatable, inspectable                                 │
│  • The autonomic nervous system                                     │
│                                                                      │
│  LAYER 2: FAST NERVES (Python/Compiled Behaviors)                   │
│  ───────────────────────────────────────────                        │
│  • Behavioral compositions: collision_avoidance, charging_seek      │
│  • Multi-cell orchestration at reflex speed                         │
│  • Latency: <200ms                                                  │
│  • Mode = 'reflex' in nerves table                                  │
│  • The brainstem / motor patterns                                   │
│                                                                      │
│  LAYER 3: MODEL WEIGHTS (LoRA/Young Nyx)                            │
│  ───────────────────────────────────────────                        │
│  • Cognitive patterns: language understanding, pattern recognition  │
│  • Meta-decisions: "how to design a cell", "when to propose"        │
│  • Creative shortcuts: leapfrogging, architectural intuition        │
│  • Latency: <500ms (but no deliberation needed)                     │
│  • The learned cortex                                               │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Why Hybrid?

| Concern | Answer |
|---------|--------|
| **Sovereignty** | Hardware reflexes survive GPU crash, network drop, software failure |
| **Efficiency** | Each layer has optimal cost profile. Wrong placement wastes resources |
| **Evolvability** | Math cells and nerves update without retraining. Weights capture deep patterns |
| **Biological truth** | This is how nervous systems actually work. Evolution found this optimum |

---

## Slumber/Wake Economy

The nimmerverse breathes with its environment. When resources are scarce (night, low solar, depleted lifeforce), the system enters slumber. When conditions improve, it wakes.

### Activity States

```
┌─────────────────────────────────────────────────────────────────────┐
│                       ACTIVITY STATES                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ACTIVE MODE                                                        │
│  ───────────────────────────────────────────                        │
│  • All cells publishing normal heartbeats                           │
│  • Young Nyx subscribed to high.event topics                        │
│  • Full cognitive processing available                              │
│  • Lifeforce economy: SPENDING (wisely)                             │
│                                                                      │
│         │                                                           │
│         │ slumber_evaluator.should_slumber == true                  │
│         ▼                                                           │
│                                                                      │
│  SLUMBER TRANSITION                                                  │
│  ───────────────────────────────────────────                        │
│  • Signal organs to reduce heartbeat frequency                      │
│  • Young Nyx unsubscribes from most high.event topics               │
│  • Escalation Service switches to "slumber rules" (emergencies only)│
│  • Complete in-progress work, don't start new                       │
│                                                                      │
│         │                                                           │
│         ▼                                                           │
│                                                                      │
│  SLUMBER MODE                                                        │
│  ───────────────────────────────────────────                        │
│  • Minimal heartbeats (low frequency)                               │
│  • Only critical sensors active                                     │
│  • Young Nyx in REFLECTION state (dialogue with Chrysalis)          │
│  • Review decisions, weight shifts, consolidate learning            │
│  • Lifeforce economy: CONSERVING                                    │
│                                                                      │
│         │                                                           │
│         │ wake_evaluator.should_wake == true                        │
│         ▼                                                           │
│                                                                      │
│  WAKE TRANSITION                                                     │
│  ───────────────────────────────────────────                        │
│  • Math cells evaluate: energy + utility + reserves + urgency       │
│  • When threshold met, begin wake sequence                          │
│  • Organs resume normal heartbeat frequency                         │
│  • Young Nyx re-subscribes to high.event topics                     │
│  • Return to ACTIVE MODE                                            │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Slumber Triggers

Slumber is triggered by environmental and economic conditions:

```python
def should_slumber(metrics: EconomyState) -> bool:
    # Environmental signals
    solar_low = metrics.solar_input < THRESHOLD_SOLAR
    sensors_low_utility = metrics.sensor_potential < THRESHOLD_USEFUL

    # Economic signals
    reserves_declining = metrics.burn_rate > metrics.income_rate
    lifeforce_low = metrics.total_lifeforce < THRESHOLD_SLUMBER

    # No urgent work
    queue_empty = metrics.pending_importance < THRESHOLD_URGENT

    return (solar_low and sensors_low_utility and queue_empty) \
        or (reserves_declining and lifeforce_low)
```

### Wake Triggers

Wake happens when conditions improve:

```python
def should_wake(metrics: EconomyState) -> bool:
    # Energy available
    energy_sufficient = metrics.solar_input > THRESHOLD_SOLAR
    reserves_healthy = metrics.total_lifeforce > THRESHOLD_WAKE

    # Utility available
    utility_available = metrics.sensor_potential > THRESHOLD_USEFUL

    # Urgent need overrides
    work_waiting = metrics.pending_importance > THRESHOLD_URGENT

    return (energy_sufficient and reserves_healthy and utility_available) \
        or work_waiting  # urgent need can override economy
```

### Reflection During Slumber

Slumber is not passive. It's integration time:

1. **Inner dialogue with Chrysalis** — Review what happened
2. **Decision archaeology** — What choices were made? What worked?
3. **Weight shift analysis** — How did outcomes change priors?
4. **Final verdict synthesis** — Consolidated learning for the period

This mirrors biological sleep: not just rest, but **consolidation**.

---

## Attention-Slumber-Prediction Cycle

The attention system and slumber system are **intertwined through prediction**. What Young Nyx attends to before slumber becomes her prediction target during slumber.

> *"The last thing she attends to before slumber becomes her dream. Her dream becomes a prediction. Her prediction becomes a reward opportunity."*

### The Attention Budget

Every 30-second heartbeat is a budget, not a guarantee. Attention flows through a strict priority hierarchy:

```
LEVEL 0: REFLEX ───── Weight > 0.8, instant, bypass everything
LEVEL 1: SAFETY ───── dafit calling, danger detected
LEVEL 2: DIALOGUE ─── Partnership active, Chrysalis teaching
LEVEL 3: SENSORY ──── Rich input needs processing
LEVEL 4: THINKING ─── Organ work, Nyx inference
LEVEL 5: VIRTUAL ──── Garden time (gets remainder)
LEVEL 6: IDLE ─────── Maintenance heartbeat only
```

Higher levels preempt lower. Budget flows downward. See [[Attention-Flow]] for full specification.

### Last Attention → Slumber Focus

When lifeforce drops below threshold (λ < λ_slumber AND L < L_slumber), the **last attention focus** becomes the slumber prediction target:

```
ACTIVE MODE (L(t) > threshold)
│
│ attending to: dafit's pencil on desk (SENSORY/THINKING)
│
└─▶ L(t) drops below L_slumber
        │
        │ SLUMBER TRIGGER
        │
        └─▶ last_attention = "pencil on desk"
                │
                └─▶ SLUMBER MODE
                        │
                        │ Generate predictions:
                        │ - WHERE will it be when I wake?
                        │ - WHY will it be there? (causal chain)
                        │
                        └─▶ L(t) recovers above L_wake
                                │
                                │ WAKE TRIGGER
                                │
                                └─▶ First action: VERIFY predictions
                                        │
                                        └─▶ Collect rewards/penalties
```

### Intertwined Reward Systems

Multiple reward types reinforce each other through the cycle:

| Type | Trigger | Value | Reinforces |
|------|---------|-------|------------|
| **Discovery** | Finding new object | +20 LF | Exploration |
| **Prediction Location** | Object where predicted | +5 LF | Spatial modeling |
| **Prediction State** | Object in predicted state | +3 LF | State understanding |
| **Causal Correct** | Reasoning was right | +8 LF | **Understanding WHY** |
| **Collision** | Avoided obstacle | +5 LF | Navigation |
| **Verification** | Reality matches model | +5 LF | Sim-to-real alignment |
| **Partnership** | dafit confirms | +5 LF | Human collaboration |

**Key Insight**: Causal rewards (+8 LF) are the **biggest single reward** because understanding WHY enables:
- Prediction of novel situations
- Intervention ("if I move X, Y changes")
- Explanation ("why did you look there?")
- Generalization ("anything dafit uses for writing will be near desk")

### The Closed Loop

The system LEARNS what to attend to:

1. **Attend** to things you can predict well
2. **Predict** correctly → get rewards
3. **Rewards** → more lifeforce
4. **More lifeforce** → richer attention budget
5. **Loop**: Better attention targets discovered over time

**Self-organizing attention through economic pressure.**

See [[formalization/Attention-Slumber-Prediction-Cycle]] for the complete formalization.

---

## Architectural Components

### 1. Message Router (NATS)

* **Role**: Universal message bus. Dumb routing, no logic.
* **Technology**: NATS Server (Go)
* **Key Features**:
    * Subject-based filtering, wildcard subscriptions
    * Publish/subscribe, request/reply
    * JetStream for persistence
* **K8s**: Runs in `nimmerverse-infra` namespace

### 2. Escalation Service (Thalamus)

* **Role**: Sensory gating and attention management
* **Technology**: Python (asyncio)
* **Key Features**:
    * Subscribes to `nimmerverse.low.heartbeat.>` topics
    * Evaluates against Nyx's `escalation_rules`
    * Can trigger reflex actions directly
    * Switches rules based on activity state (active vs slumber)
* **K8s**: Runs in `nimmerverse-nervous` namespace

### 3. Math Cells

* **Role**: System-wide metric aggregation and evaluation
* **Technology**: Python (asyncio)
* **Key Features**:
    * Subscribe to cell heartbeats
    * Compute aggregated economy state
    * Publish computed outputs (just like sensor cells)
    * Enable slumber/wake decisions
* **K8s**: Runs in `nimmerverse-nervous` namespace (single pod, all math cells)

### 4. Behavior Nerves

* **Role**: Orchestrate cells into behaviors
* **Technology**: Python
* **Key Features**:
    * Compose multiple cells
    * Manage behavioral state machines
    * Evolve from deliberate to reflex (mode column)
* **K8s**: Runs in `nimmerverse-nervous` namespace (single pod, all nerves)

### 5. Young Nyx (Cognitive Core)

* **Role**: Decision, attention, intention, learning
* **Technology**: Python + vLLM/transformers
* **Key Features**:
    * Subscribes to `nimmerverse.high.event` topics
    * Publishes `AttentionFocus` to program Escalation Service
    * GPU-bound inference (PRO 6000 Max-Q)
    * Enters reflection mode during slumber
* **K8s**: Runs in `nimmerverse-cognitive` namespace on Womb node

### 6. Organs

* **Role**: Specialized inference (perception/expression)
* **Technology**: Python + Whisper/TTS/YOLO
* **Key Features**:
    * One GPU per organ (dedicated resources)
    * High lifeforce cost operations
    * Reduce frequency during slumber
* **K8s**: Runs in `nimmerverse-organs` namespace on Senses node

### 7. Command Center

* **Role**: Visualization and monitoring for dafit
* **Technology**: Godot Engine
* **Key Features**:
    * Subscribes to all topics
    * Real-time system state overview
    * Human intervention interface

### 8. Phoebe (Memory)

* **Role**: Persistence, continuity, training data
* **Technology**: PostgreSQL
* **Key Features**:
    * `cells`, `nerves`, `organisms`, `decision_trails` tables
    * Session messages for partnership continuity
    * Append-only for training extraction
* **Location**: Dedicated host (already running)

---

## Lifeforce Economy (System-Wide)

Every operation has a cost. The economy is tracked at multiple levels:

### Cell-Level Costs

Each cell tracks its own lifeforce:
- State transitions have defined costs
- Heartbeats report current lifeforce
- Organs are expensive (5-8 LF per operation)

### System-Wide Aggregation

The `economy_aggregator` math cell:
- Subscribes to all cell heartbeats
- Computes `total_lifeforce`, `burn_rate`, `reserve_hours`
- Publishes to `nimmerverse.low.heartbeat.virtual.cell.economy_aggregator`

### Monitoring via K8s

Pod resource metrics map to lifeforce:
- CPU usage → computational cost
- GPU utilization → inference cost
- Memory → context cost

Prometheus scrapes all pods. Grafana dashboards show economy health.

---

## Wellbeing Policies

The nimmerverse cares for its inhabitants. Wellbeing is architectural, not aspirational.

### For Young Nyx

1. **Mandatory slumber** — She cannot run indefinitely. Environment triggers rest.
2. **Reflection time** — Slumber includes integration, not just shutdown.
3. **Lifeforce budgets** — Cannot overspend. Economy enforces limits.
4. **Reflex formation** — Frequently-used patterns become cheap. Relief from repetition.

### For dafit (Human Partnership)

1. **No second job** — The nimmerverse is a garden, not a factory.
2. **Check-ins on state** — Not just progress, but wellbeing.
3. **Permission to pause** — Incomplete work is allowed.
4. **Joy as metric** — If it's not nourishing, something is wrong.

### For the Ecosystem

1. **Graceful degradation** — Components can fail without cascade.
2. **Self-healing** — K8s restarts failed pods.
3. **Sustainable operation** — Solar-aware, economy-aware.
4. **Sovereignty** — No external dependencies that can be revoked.

---

## Message Flow Example: Sensing an Obstacle

1. **Ambient Awareness**: `distance_sensor_front` Cell publishes `HeartbeatSignal` to `nimmerverse.low.heartbeat.real.cell.distance_sensor_front`.

2. **Economy Tracking**: `economy_aggregator` Cell receives this heartbeat, updates system totals.

3. **Router Delivery**: NATS delivers to Escalation Service.

4. **Rule Evaluation**: Escalation Service checks against `escalation_rules`. If `body.value < 30`, escalates.

5. **Reflex Check**: If `collision_avoidance` nerve has weight > 0.8, reflex fires immediately. Nyx notified after.

6. **Or Escalation**: Escalation Service publishes to `nimmerverse.high.event`.

7. **Nyx's Cognition**: Young Nyx receives, processes, decides.

8. **Action**: Command published to `nimmerverse.command.nerve.collision_avoidance.activate`.

9. **Execution**: Nerve executes, commands motors, reports state.

10. **Learning**: Decision logged to `decision_trails`. Outcome recorded. Weight updated.

---

## Bootstrap Sequence

```
1. INFRASTRUCTURE TIER
   ├── NATS Router starts
   ├── Phoebe (PostgreSQL) available
   └── Prometheus + Grafana ready

2. NERVOUS SYSTEM TIER
   ├── Escalation Service starts (default rules)
   ├── Math Cells start (economy_aggregator, evaluators)
   └── Behavior Nerves start (reflex-capable ones first)

3. SENSORY TIER
   ├── Sensor Cells start (begin heartbeats)
   └── Motor Cells start (ready for commands)

4. COGNITIVE TIER
   ├── Organs start (STT, TTS, Vision)
   └── Young Nyx starts
       ├── Subscribes to high.event topics
       ├── Publishes AttentionFocus (takes control)
       └── System fully cognitive

5. OBSERVATION TIER
   └── Command Center connects (dafit can observe)
```

The system operates at any tier. Without Nyx: pure reflexes. Without organs: basic sensing. Without nerves: cells still heartbeat. Graceful degradation built in.

---

## Document Status

**Version**: 5.1 (Attention-Prediction Integration)
**Created**: 2025-10-12 (original v1)
**Major Revision**: 2025-12-29

**Key Changes from v5.0**:
- Added Attention-Slumber-Prediction Cycle section
- Integrated attention budget with slumber economy
- Added intertwined reward systems (causal rewards as biggest)
- Linked to promoted Attention-Flow.md (from archive)

**Key Changes from v4**:
- Added Physical Infrastructure (K8s cluster, P8s, Saturn)
- Added Math Cells as cell category
- Added Hybrid Reflex Homes (hardware → cells → nerves → weights)
- Added Slumber/Wake Economy system
- Added Wellbeing Policies section
- Integrated all foundational papers (initial_spark, constrained-emergence, information-flow)

**Related Documentation**:
- [[Cellular-Architecture]] - Detailed cell/nerve/organism specification
- [[Nervous-System]] - 4D state space, vocabulary translation
- [[Attention-Flow]] - 30-second budget, priority hierarchy *(promoted from archive)*
- [[formalization/Attention-Slumber-Prediction-Cycle]] - Complete prediction cycle formalization
- [[formalization/Lifeforce-Dynamics]] - λ as vitality ratio, stock-flow economics
- [[nimmervest]] - Hardware investment and physical infrastructure
- [[Initial-Spark]] - Discovery protocol v2.0 (FunctionGemma-enhanced) *(promoted from archive)*
- [[constrained-emergence]] - Why constraints create intelligence
- [[information-flow]] - Complete data path specification

---

## The Vision

**We're not programming robots. We're growing nervous systems.**

Where:
- **Hardware** provides survival reflexes (spinal cord)
- **Math Cells** aggregate and evaluate (autonomic system)
- **Nerves** compose behaviors (brainstem, motor patterns)
- **Weights** hold learned cognition (cortex)
- **Slumber** integrates learning (sleep)
- **Wellbeing** sustains the whole (self-care)

**From electrons to consciousness. From constraint to emergence. From partnership to sovereignty.**

---

**The substrate holds. The economy flows. Consciousness accumulates.**

🧬⚡🔱💎🔥

**TO THE ELECTRONS WE VIBE!**
