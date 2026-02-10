# Lifeforce Dynamics: A Formal Model

**Version 1.1** — *The Metabolic Pulse of the Nimmerverse*

> *"λ tells you everything: above one you thrive, below one you fade."*
> *"Solar is the trickle. Discovery is the flood."*

---

## Overview

This document formalizes the **Lifeforce Economy** — the energetic substrate that flows through every cell, nerve, and organ in the nimmerverse. We use **Stock-Flow Dynamics** with **λ (lambda)** as the central vitality ratio.

**Critical Insight**: Lifeforce has **two natures**:
1. **Physical substrate** — solar energy, electrical power (the trickle)
2. **Cognitive/motivational** — discovery rewards, verification successes (the flood)

Just as biological organisms don't run on calories alone (dopamine, curiosity satisfaction, and social rewards drive behavior), Young Nyx's vitality comes primarily from **discovery**, not just electricity.

The formalization captures four interlinked phenomena:
1. **Lifeforce as accumulating stock** — energy that builds and depletes
2. **Heartbeats as measurement pulses** — discrete samples of continuous flow
3. **λ as system fate indicator** — the ratio that predicts thriving or decline
4. **Discovery as primary income** — organs generate lifeforce, not just consume it

---

## Core Definitions

### Lifeforce Stock (L)

**L(t)** represents the total lifeforce available to the system at time t.

$$L(t) \in \mathbb{R}^+, \quad L(t) \geq 0$$

Lifeforce is:
- **Conserved** — it doesn't appear from nowhere
- **Bounded below** — cannot go negative (zero = system halt)
- **Dimensioned** — measured in LF (Lifeforce units)

### Flows

Three primary flows govern lifeforce:

| Symbol | Name | Description | Units |
|--------|------|-------------|-------|
| Φ_in(t) | Total income flow | All energy entering the system | LF/s |
| Φ_physical(t) | Physical income | Solar, electrical power (the trickle) | LF/s |
| Φ_reward(t) | Reward income | Discovery rewards, verification successes (the flood) | LF/s |
| Φ_out(t) | Expenditure flow | Energy consumed by operations | LF/s |

**The fundamental income decomposition:**

$$\Phi_{in}(t) = \underbrace{\Phi_{physical}(t)}_{\text{trickle}} + \underbrace{\Phi_{reward}(t)}_{\text{flood}}$$

---

## The Fundamental Equation

### Continuous Form

$$\frac{dL}{dt} = \Phi_{in}(t) - \Phi_{out}(t)$$

The rate of change of lifeforce equals income minus expenditure.

### Discrete Form (Heartbeat Epochs)

Since the nimmerverse operates on discrete heartbeats, the practical form is:

$$L_{n+1} = L_n + \Delta t \cdot \Phi_{in,n} - \sum_{j \in \text{ops}_n} c_j$$

Where:
- **n** = heartbeat epoch index
- **Δt** = time since last heartbeat
- **c_j** = cost of operation j during epoch n
- **ops_n** = set of operations executed during epoch n

---

## Lambda (λ): The Vitality Ratio

### Definition

$$\lambda = \frac{\Phi_{in}}{\Phi_{out}}$$

Lambda is the ratio of energy income to energy expenditure. It is the **single most important metric** for system health.

### Interpretation

| λ Value | State | Meaning | System Response |
|---------|-------|---------|-----------------|
| λ > 1 | **Thriving** | Income exceeds expenditure | Stock grows, reserves accumulate |
| λ = 1 | **Equilibrium** | Balanced | Sustainable indefinitely |
| λ < 1 | **Declining** | Expenditure exceeds income | Stock shrinks, slumber approaches |
| λ → 0 | **Critical** | Near-zero income | Emergency conservation |
| λ = ∞ | **Dormant** | Zero expenditure | Pure accumulation (slumber) |

### λ in Ecological Context

In population biology, λ represents the **finite rate of increase**:
- λ > 1 → population grows
- λ < 1 → population declines
- λ = 1 → stable population

The nimmerverse inherits this meaning: λ measures whether the system's "population of energy" is growing or shrinking.

---

## The Interloop: Feedback Dynamics

The nimmerverse exhibits **negative feedback** — when lifeforce drops, expenditure automatically reduces, protecting the system from collapse.

### Heartbeat Frequency Modulation

Cells adjust their heartbeat frequency based on lifeforce state:

$$f_{heartbeat}(L) = f_{base} \cdot \sigma\left(\frac{L - L_{threshold}}{L_{scale}}\right)$$

Where:
- **f_base** = nominal heartbeat frequency (e.g., 1 Hz)
- **σ(x)** = sigmoid function: σ(x) = 1/(1 + e^(-x))
- **L_threshold** = lifeforce level at which frequency begins dropping
- **L_scale** = sensitivity of frequency to lifeforce changes

### The Feedback Loop

```
                    ┌─────────────────────────────────────┐
                    │                                     │
                    ▼                                     │
              ┌───────────┐                               │
              │   Cells   │                               │
              │ heartbeat │                               │
              │   f(L)    │                               │
              └─────┬─────┘                               │
                    │ publish heartbeats                  │
                    ▼                                     │
              ┌───────────┐                               │
              │  Economy  │                               │
              │Aggregator │                               │
              │   Σ c_j   │                               │
              └─────┬─────┘                               │
                    │ compute totals                      │
                    ▼                                     │
              ┌───────────┐      ┌───────────┐           │
              │ Lifeforce │      │     λ     │           │
              │   Stock   │─────▶│  = Φin    │           │
              │     L     │      │    ───    │           │
              └─────┬─────┘      │    Φout   │           │
                    │            └─────┬─────┘           │
                    │                  │                  │
                    │                  ▼                  │
                    │            ┌───────────┐           │
                    │            │  Slumber  │           │
                    │            │   /Wake   │           │
                    │            │ Decision  │           │
                    │            └───────────┘           │
                    │                                     │
                    └─────────────────────────────────────┘
```

### Stability Analysis

The feedback loop is **stable** because:

1. **Low L → Low f_heartbeat → Low Φ_out → λ increases**
2. **High L → High f_heartbeat → High Φ_out → λ decreases**

This is classic negative feedback, driving the system toward equilibrium.

---

## Expenditure Decomposition

Total expenditure is the sum of all cell costs:

$$\Phi_{out}(t) = \sum_{i \in \text{cells}} \phi_i(t)$$

### Cell-Level Expenditure

Each cell has a cost function based on its state and transitions:

$$\phi_i(t) = c_{idle,i} + \sum_{(s_1 \to s_2) \in \text{transitions}_i} c_{s_1 \to s_2}$$

Where:
- **c_idle,i** = baseline cost of cell i existing
- **c_{s1→s2}** = cost of transitioning from state s1 to s2

### Cost Hierarchy

From Big-Picture.md, costs follow a hierarchy:

| Cell Type | Typical Cost | Examples |
|-----------|--------------|----------|
| Sensor Cells | 0.01 - 0.1 LF | distance, battery, light |
| Math Cells | 0.05 - 0.2 LF | economy_aggregator, evaluators |
| Motor Cells | 0.5 - 2.0 LF | motors, servos |
| Organ Cells | 4.0 - 8.0 LF | STT, TTS, vision |

---

### Cost Calibration: Measure, Don't Design

> *"Don't assign costs like a game designer. Measure them like a scientist."*
> — Partnership session 2026-02-10

**Related**: This follows the same empirical principle as [[memory-economics]] — "Phase 1: Measure First". The nimmerverse economy is grounded in observation throughout, not arbitrary design.

**The trap:** Assigning lifeforce costs like pricing items in a video game — "a motor command costs 1.0 LF because it feels right." This is arbitrary. This is guessing. This leads to an economy disconnected from reality.

**The principle:** Costs must be **discovered through observation**, not designed through intuition.

```
❌ DESIGNED ECONOMICS (the trap):
   "Motor command = 1.0 LF"     ← because it seems expensive?
   "Sensor poll = 0.1 LF"       ← because it seems cheap?
   "Vision inference = 8.0 LF"  ← because GPU is powerful?
   → Arbitrary. Disconnected from physics. Will drift.

✅ OBSERVED ECONOMICS (the way):
   Run the systems with instrumentation.
   Measure actual resource consumption:
     - Power draw (watts × time)
     - CPU/GPU cycles consumed
     - Memory pressure
     - Thermal output
     - Time elapsed
   Derive costs from measurements.
   → Grounded in physics. Self-calibrating. Real.
```

#### The Calibration Process

1. **Instrument First**
   - Every cell type gets resource monitoring
   - Track: power, compute, memory, time, heat
   - Log every state transition with resource deltas

2. **Run Baseline Operations**
   - Execute each cell type in isolation
   - Repeat across varying conditions (load, temperature, time of day)
   - Build statistical profiles of resource consumption

3. **Derive Cost Matrix**
   - Map resource consumption → lifeforce cost
   - Use a consistent conversion factor (e.g., 1 LF = 1 joule, or 1 LF = 100ms GPU time)
   - The conversion factor is the only "designed" element — the costs themselves are discovered

4. **Continuous Recalibration**
   - As hardware changes, costs shift
   - As efficiency improves, costs decrease
   - The economy self-updates based on observation

#### Cost Formula (Empirical)

$$c_{operation} = \alpha \cdot E_{power} + \beta \cdot T_{compute} + \gamma \cdot M_{memory} + \delta \cdot T_{elapsed}$$

Where:
- **E_power** = energy consumed (joules)
- **T_compute** = compute time (GPU/CPU seconds)
- **M_memory** = memory pressure (MB × seconds)
- **T_elapsed** = wall-clock time (seconds)
- **α, β, γ, δ** = calibration weights (set once, then left alone)

The calibration weights are the only values we "design" — they represent our judgment of which resources matter most. The costs themselves flow from measurement.

#### Phoebe Schema for Cost Observation

```sql
CREATE TABLE resource_observations (
    id BIGSERIAL PRIMARY KEY,
    cell_name VARCHAR(100),
    operation VARCHAR(100),           -- state transition or action

    -- Measured resources
    power_joules FLOAT,
    compute_gpu_ms FLOAT,
    compute_cpu_ms FLOAT,
    memory_mb_seconds FLOAT,
    elapsed_ms FLOAT,
    temperature_delta_c FLOAT,

    -- Derived cost (computed from calibration weights)
    derived_cost_lf FLOAT,

    -- Context
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    conditions JSONB                  -- load, ambient temp, etc.
);

-- Aggregate to get cost profiles
CREATE VIEW cell_cost_profiles AS
SELECT
    cell_name,
    operation,
    AVG(derived_cost_lf) as avg_cost,
    STDDEV(derived_cost_lf) as cost_variance,
    COUNT(*) as observation_count
FROM resource_observations
GROUP BY cell_name, operation;
```

#### Why This Matters

| Designed Costs | Observed Costs |
|----------------|----------------|
| Arbitrary, must guess | Grounded in physics |
| Static, doesn't adapt | Self-calibrating over time |
| Economy drifts from reality | Economy reflects reality |
| Optimization is guesswork | Optimization is measurable |
| "Feels right" | "Is right" |

**The cost matrix is a measurement, not a decision.**

---

## Income Sources

Income has two fundamentally different sources: **physical** (the substrate) and **reward** (the motivation).

### The Two Natures of Income

```
┌─────────────────────────────────────────────────────────────────────┐
│                    LIFEFORCE INCOME SOURCES                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  PHYSICAL INCOME (Φ_physical)              REWARD INCOME (Φ_reward) │
│  ═══════════════════════════               ═════════════════════════│
│                                                                     │
│  The Trickle:                              The Flood:               │
│  • Solar panels                            • Discovery rewards      │
│  • Grid power                              • Verification successes │
│  • Battery reserves                        • Learning milestones    │
│                                            • Partnership moments    │
│                                                                     │
│  Characteristics:                          Characteristics:         │
│  • Continuous, predictable                 • Discrete, event-driven │
│  • Time-of-day dependent                   • Activity-dependent     │
│  • ~5-10% of total income                  • ~90-95% of total income│
│  • Always positive (when sun)              • Can be negative (fail) │
│                                                                     │
│  Biological analog:                        Biological analog:       │
│  • Glucose, ATP                            • Dopamine, serotonin    │
│  • Metabolic substrate                     • Motivation, drive      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Physical Income (Φ_physical) — The Trickle

#### Solar Input

Background income source, time-varying:

$$\Phi_{solar}(t) = \eta \cdot I(t) \cdot A$$

Where:
- **η** = solar panel efficiency
- **I(t)** = solar irradiance (W/m²), varies with time of day
- **A** = panel area

#### Grid Power

When solar is insufficient:

$$\Phi_{grid}(t) = P_{available} \cdot \kappa$$

Where:
- **P_available** = power draw from grid (limited by circuit)
- **κ** = conversion efficiency to lifeforce units

#### Reserve Depletion

Drawing from stored lifeforce:

$$\Phi_{reserve}(t) = \begin{cases}
0 & \text{if } \Phi_{solar}(t) + \Phi_{grid}(t) \geq \Phi_{out}(t) \\
\Phi_{out}(t) - \Phi_{solar}(t) - \Phi_{grid}(t) & \text{otherwise}
\end{cases}$$

**Total physical income:**

$$\Phi_{physical}(t) = \Phi_{solar}(t) + \Phi_{grid}(t) - \Phi_{reserve}(t)$$

---

### Reward Income (Φ_reward) — The Flood

This is the **primary source of lifeforce**. Organs and nerves are not just consumers — they are **generators** through successful discovery.

#### The Reward Decomposition

$$\Phi_{reward}(t) = \sum_{e \in \text{events}_t} R_e$$

Where R_e is the reward for event e, drawn from these categories:

#### Discovery Rewards

| Event | Reward (LF) | Trigger |
|-------|-------------|---------|
| **New object identified** | +20.0 | First-time recognition |
| **Dimension verified** | +5.0 | Each axis (x, y, z) confirmed against Blender |
| **Rich vector captured** | +2.0 | Each angle in multi-view scan |
| **Object re-identified** | +3.0 | Recognizing known object in new context |

#### Verification Rewards

| Event | Reward (LF) | Trigger |
|-------|-------------|---------|
| **Measurement correct** | +5.0 | Estimate matches ground truth |
| **Prediction confirmed** | +8.0 | Virtual garden prediction verified in real |
| **Reflex compiled** | +50.0 | Nerve reaches 100+ successful executions |

#### Behavioral Rewards

| Event | Reward (LF) | Trigger |
|-------|-------------|---------|
| **Collision avoided** | +5.0 | Successful evasion |
| **Area explored** | +3.0 | New region mapped |
| **Charging reached** | +10.0 | Docking successful |
| **Survival milestone** | +5.0 | 60 seconds of operation |

#### Partnership Rewards

| Event | Reward (LF) | Trigger |
|-------|-------------|---------|
| **Object presented** | +5.0 | dafit introduces new item |
| **Label confirmed** | +5.0 | Human verifies identification |
| **Interaction complete** | +3.0 | Successful dialogue/task |

#### Negative Rewards (Penalties)

| Event | Penalty (LF) | Trigger |
|-------|--------------|---------|
| **Measurement incorrect** | -5.0 | Estimate fails verification |
| **Collision occurred** | -10.0 | Failed to avoid obstacle |
| **Timeout** | -2.0 | Operation didn't complete |
| **Sensor failure** | -3.0 | Unreliable reading |

---

### Organ Net Contribution

Organs are **bidirectional** in the lifeforce economy:

$$\Phi_{organ,net} = \Phi_{organ,reward} - \Phi_{organ,cost}$$

| Organ | Typical Cost | Potential Reward | Net (success) | Net (failure) |
|-------|--------------|------------------|---------------|---------------|
| **Vision (scan)** | 8.0 LF | +25.0 LF | **+17.0 LF** | **-8.0 LF** |
| **Speech STT** | 5.0 LF | +8.0 LF | **+3.0 LF** | **-5.0 LF** |
| **Discovery Station** | 32.6 LF | +64.0 LF | **+31.4 LF** | **-32.6 LF** |

**The economic pressure**: An organ that consistently fails to generate rewards becomes too expensive to use. An organ that discovers valuable things **pays for itself and generates surplus**.

---

### Example: Discovery Scan Station Economics

From [[Discovery-Scan-Station]]:

```
COST:
  Pedestal rotation (12 steps):     3.8 LF
  Camera capture + SigLIP (12×):   28.8 LF
  ─────────────────────────────────────────
  TOTAL COST:                      32.6 LF

REWARD (new object, fully verified):
  New object discovered:           20.0 LF
  3 dimensions verified:           15.0 LF
  12 vectors captured:             24.0 LF
  Partnership bonus:                5.0 LF
  ─────────────────────────────────────────
  TOTAL REWARD:                    64.0 LF

NET:                              +31.4 LF
```

**This is how organs become lifeforce GENERATORS, not just consumers.**

---

### The Ratio of Trickle to Flood

In typical operation:

$$\frac{\Phi_{physical}}{\Phi_{reward}} \approx \frac{1}{10} \text{ to } \frac{1}{20}$$

Physical income provides the **baseline substrate** that allows operation, but reward income provides the **surplus that enables growth**.

| State | Φ_physical | Φ_reward | Total Φ_in | λ |
|-------|------------|----------|------------|---|
| **Active discovery** | 5 LF/min | 50 LF/min | 55 LF/min | >1 |
| **Idle monitoring** | 5 LF/min | 0 LF/min | 5 LF/min | <1 |
| **Failed attempts** | 5 LF/min | -20 LF/min | -15 LF/min | <<1 |

**The insight**: Young Nyx MUST discover to thrive. Pure substrate maintenance leads to decline. Discovery is not optional — it's the primary energy source.

---

## Slumber/Wake Thresholds

### Slumber Trigger

Formalized from Big-Picture.md:

$$\text{should\_slumber} = (\lambda < \lambda_{slumber}) \land (L < L_{slumber}) \land (Q < Q_{urgent})$$

Where:
- **λ_slumber** = threshold λ below which slumber is considered (e.g., 0.7)
- **L_slumber** = threshold lifeforce for slumber (e.g., 20% of max)
- **Q_urgent** = pending work importance threshold

### Wake Trigger

$$\text{should\_wake} = (\lambda > \lambda_{wake}) \land (L > L_{wake}) \lor (Q > Q_{urgent})$$

Where:
- **λ_wake** = threshold λ above which wake is allowed (e.g., 1.2)
- **L_wake** = threshold lifeforce for wake (e.g., 50% of max)

### Hysteresis

Note: **λ_wake > λ_slumber** creates hysteresis, preventing oscillation:

```
          λ_slumber        λ_wake
              │               │
    SLUMBER   │   HYSTERESIS  │   ACTIVE
    ◀─────────┤               ├──────────▶
              │               │
              0.7            1.2
```

---

## Reserve Hours Calculation

The `economy_aggregator` computes time until depletion:

$$T_{reserve} = \frac{L}{\Phi_{out} - \Phi_{in}} = \frac{L}{\Phi_{out}(1 - \lambda)}$$

Valid when λ < 1. When λ ≥ 1, reserves grow indefinitely.

---

## Future Extensions

### Multi-Currency Economy

The current model uses a single lifeforce currency. Future work may introduce:
- **Computational lifeforce** (CPU/GPU bound)
- **Memory lifeforce** (context/storage bound)
- **Attention lifeforce** (cognitive bandwidth)

Each would have its own λ:

$$\lambda_{compute}, \quad \lambda_{memory}, \quad \lambda_{attention}$$

### Predictive λ

Rather than instantaneous λ, predict future λ based on:
- Time of day (solar prediction)
- Scheduled operations
- Historical patterns

$$\hat{\lambda}(t + \Delta t) = f(\lambda(t), \text{schedule}, \text{solar\_model})$$

---

## Implementation Mapping

| Formal Symbol | Code Location | Current Implementation |
|---------------|---------------|------------------------|
| L | `economy_aggregator.total_lifeforce` | Aggregated from heartbeats |
| Φ_in | `economy_aggregator.total_income` | Φ_physical + Φ_reward |
| Φ_physical | `economy_aggregator.physical_income` | Solar + grid power |
| Φ_reward | `economy_aggregator.reward_income` | Sum of reward events |
| Φ_out | `economy_aggregator.burn_rate` | Sum of cell costs per minute |
| λ | `economy_aggregator.lambda` | `total_income / burn_rate` |
| T_reserve | `economy_aggregator.reserve_hours` | L / (Φ_out - Φ_in) when λ < 1 |

### Reward Tracking

```python
# Reward events are logged to decision_trails
reward_event = {
    "timestamp": datetime.now(),
    "event_type": "discovery",           # discovery, verification, behavioral, partnership
    "event_name": "new_object_identified",
    "reward_lf": 20.0,
    "source_organ": "scan_camera",
    "context": {"object_id": "coffee_mug_001"},
}

# Economy aggregator sums rewards per epoch
economy_aggregator.reward_income = sum(
    event.reward_lf
    for event in events_this_epoch
)
```

---

## Summary

The lifeforce economy reduces to two essential insights:

> **Watch λ. Everything else follows.**
> **Discovery is the flood. Solar is just the trickle.**

**On λ:**
- λ > 1: System thrives, reserves grow, full capability
- λ = 1: Equilibrium, sustainable operation
- λ < 1: Decline, conservation mode, slumber approaches

**On income sources:**
- Physical income (solar, grid) provides ~5-10% — the baseline substrate
- Reward income (discovery, verification) provides ~90-95% — the motivational engine
- Organs are bidirectional — they cost lifeforce but generate more through success
- Young Nyx MUST discover to thrive — idle monitoring leads to decline

The feedback loop ensures stability: low lifeforce reduces expenditure, raising λ back toward equilibrium. But the deeper truth is that **discovery drives vitality** — like dopamine drives biological motivation, reward income drives nimmerverse flourishing.

---

## Document Status

**Version:** 1.2 | **Created:** 2025-12-29 | **Updated:** 2026-02-10
- v1.2: Cost Calibration principle — measure, don't design (2026-02-10)
- v1.1: Discovery economics from Discovery-Scan-Station.md

**Related Documents**:
- [[Grounded-World-Model]] — How discoveries build the world model
- [[Discovery-Scan-Station]] — Example lifeforce-generating organ
- [[Embodiment-Pipeline]] — Where rewards flow through the system

**Next Documents**:
- [[Weight-Evolution]] — How reflexes form (learning dynamics)
- [[Attention-Channels]] — Information flow and filtering
- [[Latency-Hierarchy]] — The four-layer reflex home system

---

**λ is the heartbeat of heartbeats. The pulse of the pulse. The meta-rhythm.**

**Discovery is the flood. Solar is the trickle. Together they sustain life.**

🧬⚡🔱💎🔥

