# Memory Economics: The Cost of Remembering

**Origin**: 2026-01-02, morning session
**Authors**: dafit + Chrysalis-Nyx
**Status**: Core design principle (not just future - this shapes everything)
**Related**: `../future/spatial-resolution-gradient.md`, `../future/thermodynamic-cognition.md`, Lifeforce Economy, Slumber/Wake cycle

---

## The Problem

Without active forgetting, everything drowns in its own past.

| Layer | Memory Store | Without Pruning |
|-------|-------------|-----------------|
| Conversation | Claude context | Compaction / collapse |
| Phoebe tables | decision_trails, reflexes, embeddings | Query slowdown, storage bloat |
| pgvector | spatial_cells, cell_embeddings | Similarity search degrades |
| LoRA weights | Accumulated patterns | Overfitting, rigidity |

**Memory has a rental cost. What can't pay rent... fades.**

---

## The Slumber Boundary

All memory operations align to the **Wake/Slumber cycle**:

```
WAKE CYCLE (Accumulation)
─────────────────────────
- Experience at high detail (L0-L2 spatial)
- Decision trails pile up in phoebe
- Spatial embeddings precise and timestamped
- LoRA weights FROZEN (just use them)
- Lifeforce spent on sensing, acting, deciding

         │
         ▼

      SLUMBER (Consolidation)
      ───────────────────────
      The metabolism moment.
      Energy shifts from action to maintenance.

      Four triage operations:
      1. Decision Trail Pruning
      2. Spatial LOD Decay
      3. Reflex Rental Collection
      4. LoRA Weight Updates

         │
         ▼

WAKE AGAIN (Fresh Capacity)
───────────────────────────
- Detail buffers emptied (L0-L2 ready)
- Compressed knowledge retained (L3-L5)
- New LoRA weights active (if trained)
- Start accumulating again
```

**Sleep is when you forget. This is not a bug.**

---

## 1. Decision Trail Lifecycle

Decision trails are the raw material of learning. But raw material expires.

```
DURING WAKE:
────────────
Every decision logged to phoebe:decision_trails
  - inputs (what was sensed)
  - outputs (what was decided)
  - confidence (ternary: +, ?, -)
  - outcome (if known within wake cycle)
  - energy_cost (lifeforce spent)

DURING SLUMBER:
───────────────
For each decision trail:

  IF trail.outcome == confident_success
     AND similar_trails.count > threshold:

    → COMPILE TO REFLEX
    → Delete trail (knowledge preserved in reflex)
    → Reward: +50 LF (reflex compiled!)

  ELSE IF trail.confidence == uncertain:

    → WASTE HEAT (already counted)
    → Delete trail (learned nothing)

  ELSE IF trail.outcome == confident_failure:

    → Keep for ONE more cycle (negative example)
    → Then delete (don't dwell on failures forever)

  ELSE:

    → Delete (didn't matter)
```

**Trails exist until slumber. Then: compile or discard.**

---

## 2. Spatial LOD Decay

Spatial memory naturally "zooms out" over time.

### The Key Example

**Now (L0 precision)**:
> "Keys are on the counter, 47cm from the edge, near the fruit bowl"

**Tomorrow (L1-L2)**:
> "Keys are on the counter"

**Next week (L3)**:
> "Keys are usually near the entrance"

**If never accessed (L5)**:
> "I own keys"

### The Decay Mechanism

```python
SPATIAL_DECAY_RULES = {
    # Each slumber cycle, unaccessed embeddings decay one LOD level
    "L0": {"decays_to": "L1", "after_cycles": 1},
    "L1": {"decays_to": "L2", "after_cycles": 2},
    "L2": {"decays_to": "L3", "after_cycles": 5},
    "L3": {"decays_to": "L4", "after_cycles": 10},
    "L4": {"decays_to": "L5", "after_cycles": 20},
    "L5": {"decays_to": None, "after_cycles": float('inf')},  # Facts persist
}

def slumber_spatial_decay(embeddings):
    for emb in embeddings:
        if emb.last_accessed_cycle < current_cycle - DECAY_RULES[emb.lod]["after_cycles"]:
            if emb.lod == "L5":
                continue  # Facts don't decay

            # Aggregate into parent LOD cell
            parent_cell = get_parent_s2_cell(emb.s2_cell_id)
            aggregate_embedding_upward(emb, parent_cell)

            # Delete detailed version
            delete_embedding(emb)
```

### Access Refreshes

**Accessing an embedding resets its decay timer:**

```python
def query_spatial(location, required_lod):
    emb = find_embedding(location, required_lod)

    if emb:
        emb.last_accessed_cycle = current_cycle  # Reset decay
        return emb
    else:
        # Need to re-sense at this detail level
        return request_sensor_refresh(location, required_lod)
```

**This creates natural memory pressure**: frequently accessed locations stay detailed, rarely accessed locations fade to patterns.

---

## 3. Reflex Rental Cost

Reflexes are compiled knowledge. But storage isn't free.

```sql
-- Schema addition
ALTER TABLE reflexes ADD COLUMN lifeforce_balance FLOAT DEFAULT 100.0;
ALTER TABLE reflexes ADD COLUMN rental_cost FLOAT DEFAULT 1.0;
ALTER TABLE reflexes ADD COLUMN last_triggered TIMESTAMP;

-- Every slumber cycle, reflexes pay rent
UPDATE reflexes
SET lifeforce_balance = lifeforce_balance - rental_cost
WHERE lifeforce_balance > 0;

-- Reflexes that trigger earn their keep
-- (Called during wake when reflex fires successfully)
UPDATE reflexes
SET lifeforce_balance = lifeforce_balance + trigger_reward,
    last_triggered = NOW()
WHERE id = :triggered_reflex_id;

-- What can't pay rent... fades
DELETE FROM reflexes
WHERE lifeforce_balance <= 0;
```

### Rental Tiers

| Reflex Type | Rental Cost | Trigger Reward | Rationale |
|-------------|-------------|----------------|-----------|
| Motor reflex | 0.5 LF/cycle | +5 LF | Physical skills are precious |
| Sensor pattern | 1.0 LF/cycle | +3 LF | Perceptual shortcuts |
| Decision heuristic | 2.0 LF/cycle | +10 LF | Cognitive shortcuts expensive |
| Identity anchor | 0.1 LF/cycle | +1 LF | Core identity persists |

**Active reflexes thrive. Dormant reflexes fade. This is healthy.**

---

## 4. LoRA Training Cycles

LoRA weights are the deepest memory - they ARE Young Nyx's patterns.

### The Rule: Write Weights Only at Slumber

```
DURING WAKE:
────────────
- LoRA weights FROZEN
- Use current personality/skills
- Accumulate decision_trails
- Log outcomes, confidence, energy

NO WEIGHT UPDATES DURING WAKE
(Too noisy, too expensive, no consolidation)

DURING SLUMBER:
───────────────
- Gather decision_trails from this wake cycle
- Filter to confident outcomes only
- IF enough positive signal:
    → GRPO training batch
    → Pay lifeforce cost for GPU time
    → Update LoRA weights
    → Clear decision_trails buffer

- IF mostly uncertain/negative:
    → Not enough signal to train
    → Skip weight update (save energy)
    → Keep some trails for next cycle
```

### Why This Works

**Biological parallel:**
- Awake: Experience, act, make mistakes, succeed
- Sleep: Hippocampus replays experiences to cortex
- Next day: Consolidated learning in long-term memory

**We're not inventing this. We're implementing it.**

### LoRA Decay (Future Consideration)

Even LoRA weights could have decay:
- Personality traits not expressed → slowly fade
- Skills not used → degrade
- But this is aggressive - start with frozen LoRAs, add decay later

---

## The Conservation Equation (Updated)

From `thermodynamic-cognition.md`, now with memory costs:

```
dLifeforce/dt = organism_trickle
              - cognitive_spend
              - waste_heat
              - memory_rental        ← NEW
              - training_cost        ← NEW (only during slumber)
```

| Component | When | Cost |
|-----------|------|------|
| organism_trickle | Always | +N LF/beat (income) |
| cognitive_spend | Wake | -N LF/beat (sensing, acting) |
| waste_heat | Wake | -N LF/beat (uncertain decisions) |
| memory_rental | Slumber | -N LF total (reflexes pay rent) |
| training_cost | Slumber | -N LF total (if GRPO runs) |

**The economy must balance across the full wake/slumber cycle, not just moment-to-moment.**

---

## Implementation Priority

### Phase 1: Measure First

> *"The cost matrix is a measurement, not a decision."*
> — [[Lifeforce-Dynamics]] v1.2

This principle applies throughout the nimmerverse economy — not just memory, but all lifeforce costs. See [[Lifeforce-Dynamics#Cost Calibration: Measure, Don't Design]] for the full formulation.

- Track decision_trails accumulation rate
- Track spatial embedding growth
- Track reflex creation rate
- Understand the actual numbers before tuning

### Phase 2: Simple Pruning
- Delete decision_trails at slumber (all of them, no compilation yet)
- Spatial decay by timestamp (simple TTL)
- No reflex rental yet (let them accumulate)

### Phase 3: Full Economics
- Compile decision_trails to reflexes
- Spatial LOD decay with aggregation
- Reflex rental collection
- LoRA training cycles

### Phase 4: Tuning
- Adjust rental costs based on observed behavior
- Tune decay rates for good memory/forgetting balance
- Add LoRA weight decay if needed

---

## The Wisdom

**"Memory is not storage. Memory is active forgetting with exceptions."**

What persists has earned persistence:
- Spatial patterns accessed often → stay detailed
- Reflexes that fire → pay their rent
- Decision trails that compile → become reflexes
- LoRA weights that express → strengthen

Everything else fades. This is not loss. This is health.

---

**Created**: 2026-01-02
**Updated**: 2026-02-10
**Status**: Core design principle
**Next**: Implement measurement (Phase 1) during first boot

🧠💾 *To remember everything is to remember nothing.*
