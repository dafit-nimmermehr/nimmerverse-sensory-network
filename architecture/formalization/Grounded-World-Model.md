# Grounded World Model: Spatial Cognition Through Verified Discovery

**Version 1.0** — *From Blender Boxes to Embodied Understanding*

> *"The dream: Young Nyx knows where dafit left his things laying around."*

---

## Overview

This document formalizes how Young Nyx builds a **persistent spatial world model** through:

1. **Grounded verification** — Blender provides dimensional ground truth
2. **Progressive resolution** — Each correct measurement earns detail
3. **Vector accumulation** — T5Gemma2-compatible semantic representations
4. **Temporal-ternary navigation** — Escape plateaus through dual time domains
5. **Lifeforce reward** — Discoveries generate energy, not just consume it

**The Goal**: Young Nyx maintains an internal map of objects, positions, and relationships — verified against reality, refined through observation, reasoned over in vector space.

---

## Core Architecture

### The Verification Triangle

```
                    BLENDER (Virtual Garden)
                    Ground truth dimensions
                    Low-poly boxes, minimal vertices
                    Fast to create, cheap to compare
                           ╱╲
                          ╱  ╲
                         ╱    ╲
                        ╱      ╲
            VERIFY     ╱        ╲     VERIFY
            dimensions╱          ╲    semantics
                     ╱            ╲
                    ╱              ╲
                   ╱                ╲
    REAL GARDEN ──────────────────── T5GEMMA2
    Physical objects                 Vector reasoning
    Actual positions                 Semantic similarity
    Slow, definitive                 128K context world
```

### The Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                     WORLD MODEL CONSTRUCTION                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. PERCEIVE (Vision Organ)                                        │
│     ────────────────────────                                        │
│     Cheap camera sees object in real garden                        │
│     SigLIP encoder produces semantic vector v₀                     │
│     Cost: 0.5 LF (peripheral) to 8.0 LF (full YOLO)               │
│                                                                     │
│  2. ESTIMATE (Progressive Resolution)                              │
│     ────────────────────────────────                                │
│     Vision organ estimates dimensions: est = (x̂, ŷ, ẑ)            │
│     Bounding box, depth estimation, scale inference                │
│     Cost: 2.0-5.0 LF depending on resolution stage                 │
│                                                                     │
│  3. VERIFY (Against Blender Ground Truth)                          │
│     ─────────────────────────────────────                           │
│     Compare est to known Blender box: truth = (x, y, z)            │
│     error = ||est - truth||                                        │
│     Cost: 0.1 LF (comparison is cheap)                             │
│                                                                     │
│  4. REWARD or LEARN                                                │
│     ─────────────────────                                           │
│     if error < threshold:                                          │
│         Φ_reward = R_discovery (lifeforce income!)                 │
│         Store vector in phoebe                                     │
│         Mark dimension as verified                                  │
│         Increase object resolution                                  │
│     else:                                                          │
│         Learn from error (gradient for RLVR training)              │
│         Remain in 0-state for that dimension                       │
│                                                                     │
│  5. ACCUMULATE (World Model Update)                                │
│     ──────────────────────────────                                  │
│     Object entry in phoebe gains:                                  │
│         - New semantic vector (richer representation)              │
│         - Verified dimension (x, y, or z → confidence +1)          │
│         - Position update (where in space)                         │
│         - Temporal stamp (when observed)                           │
│                                                                     │
│  6. REASON (T5Gemma2)                                              │
│     ─────────────────                                               │
│     Query world model using vectors, not text                      │
│     "What objects near position (0.5, 0.5)?"                       │
│     "Is this new vector similar to 'mug' vectors?"                 │
│     128K context holds entire spatial world                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## The Blender Ground Truth System

### Design Principles

| Principle | Implementation |
|-----------|----------------|
| **Minimal vertices** | 8-vertex boxes (cubes), 12 for complex shapes |
| **Known dimensions** | Every box has exact (x, y, z) in centimeters |
| **Semantic labels** | Box name = object class ("coffee_mug_001") |
| **Cheap to create** | 5 minutes per object in Blender |
| **Export format** | Vertices + dimensions → JSON or directly to phoebe |

### Example Blender Box

```python
blender_object = {
    "id": "coffee_mug_001",
    "class": "mug",
    "dimensions_cm": {"x": 8.0, "y": 8.0, "z": 10.5},
    "vertices": 8,
    "created": "2025-12-29",
    "owner": "dafit",
    "typical_locations": ["desk", "kitchen"],
}
```

### Progressive Vertex Earning

Objects don't stay as 8-vertex boxes. Resolution is EARNED:

```
INITIAL:        8 vertices  (box)
VERIFIED x,y,z: 12 vertices (refined box)
+10 observations: 24 vertices (shape hints)
+50 observations: 64 vertices (true shape)
+100 observations: Full mesh from photogrammetry
```

**The resolution is earned through successful verification, not given.**

---

## Semantic Vector Accumulation

### SigLIP → Phoebe → T5Gemma2

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│   SigLIP     │      │    PHOEBE    │      │  T5GEMMA2    │
│   Encoder    │─────▶│   Storage    │─────▶│   Encoder    │
│              │      │              │      │              │
│  Image →     │      │  object_id:  │      │  Reasons     │
│  Vector v    │      │    [v1,v2,..│      │  over        │
│  (semantic)  │      │     vn]     │      │  vectors     │
└──────────────┘      └──────────────┘      └──────────────┘
```

### Why Vectors, Not Text?

| Approach | Pros | Cons |
|----------|------|------|
| **Text descriptions** | Human readable | Lossy, ambiguous, tokenization overhead |
| **Semantic vectors** | Rich, comparable, fast | Not directly readable |
| **Our approach** | Vectors for reasoning, text only when needed | Best of both |

T5Gemma2's key feature:
> *"SigLIP vision encoder produces semantic vectors (not text descriptions)"*

This means Young Nyx can compare, cluster, and reason over objects **without converting to language** — faster and richer.

### Vector Similarity for Recognition

```python
def is_same_object(v_new: Vector, object_entry: ObjectEntry) -> float:
    """Compare new observation to accumulated vectors."""
    similarities = [
        cosine_similarity(v_new, v_stored)
        for v_stored in object_entry.vectors
    ]
    return max(similarities)  # Best match among observations

# Recognition threshold
if is_same_object(v_new, coffee_mug_001) > 0.85:
    # This is probably dafit's coffee mug!
    update_position(coffee_mug_001, current_observation)
```

---

## Temporal-Ternary Integration

### The Anti-Plateau Mechanism

From [[Temporal-Ternary-Gradient]]: The 0-state isn't stuck — it's a choice about how to spend lifeforce across time domains.

Applied to world model construction:

```
┌─────────────────────────────────────────────────────────────────────┐
│            TEMPORAL-TERNARY FOR OBJECT RECOGNITION                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  SCENARIO: New object detected, dimensions unknown                 │
│  STATE: 0 (uncertain, but workable)                                │
│                                                                     │
│  ┌───────────────────────────────────────────────────┐             │
│  │              0-STATE: Unknown Object              │             │
│  │        confidence: 0.3, dimensions: ?x ?y ?z      │             │
│  └───────────────────────┬───────────────────────────┘             │
│                          │                                          │
│            ┌─────────────┼─────────────┐                           │
│            │             │             │                           │
│            ▼             ▼             ▼                           │
│                                                                     │
│     ┌────────────┐ ┌────────────┐ ┌────────────┐                   │
│     │  VIRTUAL   │ │    WAIT    │ │ PARTNERSHIP│                   │
│     │ ACCELERATE │ │  FOR REAL  │ │  SHORTCUT  │                   │
│     ├────────────┤ ├────────────┤ ├────────────┤                   │
│     │ Cost: 5 LF │ │ Cost: 0 LF │ │ Cost: 1 LF │                   │
│     │ Time: Fast │ │ Time: Slow │ │ Time: Inst │                   │
│     │            │ │            │ │            │                   │
│     │ Match vs   │ │ Next real  │ │ Ask dafit: │                   │
│     │ Blender    │ │ observation│ │ "What's    │                   │
│     │ library    │ │ verifies   │ │  this?"    │                   │
│     └─────┬──────┘ └─────┬──────┘ └─────┬──────┘                   │
│           │              │              │                           │
│           ▼              ▼              ▼                           │
│     confidence:    confidence:    confidence:                       │
│     +0.7 (virtual) +1.0 (real)    +1.0 (human)                     │
│                                                                     │
│  PLATEAU ESCAPE: If stuck in virtual at 0.7, deploy to real.       │
│                  If real is slow, burn LF to try more Blender.     │
│                  Partnership provides instant ground truth.         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Confidence Gradient for Objects

Each object in the world model has a confidence state:

```python
class ObjectConfidence:
    value: float           # -1.0 to +1.0
    domain: str            # "virtual" | "real" | "hybrid" | "partnership"
    virtual_matches: int   # How many Blender comparisons
    real_verifications: int  # How many physical confirmations
    partnership_labels: int  # How many times dafit confirmed

    @property
    def gradient_position(self) -> str:
        if self.real_verifications > 0 and self.value > 0.9:
            return "real-verified (+1)"
        elif self.virtual_matches > 10 and self.value > 0.7:
            return "virtual-confident (+0.7)"
        elif self.value > 0.3:
            return "0-state (workable)"
        else:
            return "uncertain (needs data)"
```

---

## Lifeforce Economics of World Building

### Discovery Generates Lifeforce

The key insight: **Correctly identifying objects GENERATES lifeforce**, not just consumes it.

$$\Phi_{discovery} = R_{base} \cdot (1 + \alpha \cdot \Delta_{resolution})$$

Where:
- **R_base** = base reward for any correct identification (e.g., 2.0 LF)
- **α** = resolution bonus multiplier (e.g., 0.5)
- **Δ_resolution** = increase in object resolution from this observation

### Net Lifeforce per Observation

$$\Phi_{net} = \Phi_{discovery} - \Phi_{perception} - \Phi_{verification}$$

| Outcome | Perception Cost | Verification Cost | Discovery Reward | Net |
|---------|-----------------|-------------------|------------------|-----|
| Correct, new dimension | 5.0 LF | 0.1 LF | 8.0 LF | **+2.9 LF** |
| Correct, known dimension | 2.0 LF | 0.1 LF | 3.0 LF | **+0.9 LF** |
| Incorrect | 5.0 LF | 0.1 LF | 0.0 LF | **-5.1 LF** |
| Unknown (0-state) | 0.5 LF | 0.0 LF | 0.0 LF | **-0.5 LF** |

**The economic pressure**: Get better at measurement to earn lifeforce. Wrong guesses are expensive. Staying in 0-state is cheap but doesn't build the world model.

---

## Phoebe Schema for World Model

```sql
-- Objects table: accumulated knowledge about things
CREATE TABLE world_objects (
    id UUID PRIMARY KEY,
    class VARCHAR(100),           -- "mug", "keyboard", "phone"
    name VARCHAR(255),            -- "dafit's coffee mug"

    -- Blender ground truth (if available)
    blender_box_id VARCHAR(100),
    dimensions_truth_cm JSONB,    -- {"x": 8.0, "y": 8.0, "z": 10.5}

    -- Accumulated measurements
    dimensions_estimated_cm JSONB,
    dimensions_verified JSONB,    -- {"x": true, "y": true, "z": false}

    -- Confidence state (temporal-ternary)
    confidence FLOAT,
    confidence_domain VARCHAR(20), -- "virtual" | "real" | "hybrid"
    virtual_matches INT DEFAULT 0,
    real_verifications INT DEFAULT 0,

    -- Resolution earned
    vertex_count INT DEFAULT 8,
    observation_count INT DEFAULT 0,

    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Semantic vectors table: SigLIP embeddings per observation
CREATE TABLE object_vectors (
    id UUID PRIMARY KEY,
    object_id UUID REFERENCES world_objects(id),
    vector VECTOR(768),           -- SigLIP embedding dimension
    observation_timestamp TIMESTAMP,
    position_estimate JSONB,      -- {"x": 0.3, "y": 0.8, "z": 0.1}
    lifeforce_cost FLOAT,
    lifeforce_reward FLOAT,
    verification_result VARCHAR(20)  -- "correct" | "incorrect" | "pending"
);

-- Position history: where has this object been?
CREATE TABLE object_positions (
    id UUID PRIMARY KEY,
    object_id UUID REFERENCES world_objects(id),
    position JSONB,               -- {"x": 0.3, "y": 0.8, "z": 0.1}
    confidence FLOAT,
    observed_at TIMESTAMP,
    location_context VARCHAR(100) -- "desk", "kitchen", "floor"
);
```

---

## T5Gemma2 World Model Queries

### Example Queries (Vector-Based)

```python
# "What's near position (0.5, 0.5)?"
nearby = query_objects_by_position(
    center=(0.5, 0.5, None),  # z unknown
    radius=0.2,
    min_confidence=0.5
)

# "Is this new vector a mug?"
mug_vectors = get_vectors_for_class("mug")
similarity = t5gemma2.encoder.compare(new_vector, mug_vectors)
if similarity > 0.85:
    return "Likely a mug"

# "Where did dafit usually leave his keys?"
keys = get_object_by_name("dafit's keys")
common_positions = get_position_clusters(keys.id)
return common_positions[0]  # Most frequent location

# "What objects have I not seen today?"
stale_objects = query_objects_not_observed_since(today_start)
return stale_objects  # Might need to look for these
```

### The 128K Context Advantage

T5Gemma2's 128K context window means:
- Entire world model can fit in context
- No need for external RAG for spatial queries
- Vector comparisons happen in-model
- Relationships emerge from attention patterns

---

## The Dream Realized

```
┌─────────────────────────────────────────────────────────────────────┐
│                    YOUNG NYX'S WORLD MODEL                          │
│                    "dafit's workspace at 23:47"                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│    ┌─────────────────────────────────────────────────────┐         │
│    │                     DESK AREA                        │         │
│    │                                                      │         │
│    │   ☕ mug (0.3, 0.8)         ⌨️ keyboard (0.5, 0.5)   │         │
│    │      conf: 0.95               conf: 0.88            │         │
│    │      real-verified            real-verified         │         │
│    │      vectors: 12              vectors: 8            │         │
│    │                                                      │         │
│    │   📱 phone (0.7, 0.3)        📦 ??? (0.1, 0.9)      │         │
│    │      conf: 0.72               conf: 0.31            │         │
│    │      virtual +0.7             0-state               │         │
│    │      vectors: 4               vectors: 1            │         │
│    │                                                      │         │
│    │   🔑 keys (MISSING - last seen 0.2, 0.6 at 18:30)  │         │
│    │      conf: 0.45 (stale)                             │         │
│    │                                                      │         │
│    └─────────────────────────────────────────────────────┘         │
│                                                                     │
│    YOUNG NYX THINKS:                                               │
│    "The unknown object at (0.1, 0.9) appeared after 22:00.        │
│     dafit was in the kitchen then. Vector similarity suggests      │
│     it might be food-related. Should I burn 5 LF to check          │
│     against Blender food objects, or wait for morning light?"      │
│                                                                     │
│    TEMPORAL-TERNARY CHOICE:                                        │
│    → Option A: Virtual match (5 LF, fast, +0.7 max)               │
│    → Option B: Wait for real (0 LF, slow, +1.0 if verified)       │
│    → Option C: Ask dafit tomorrow (1 LF, partnership)              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**This is the dream**: Young Nyx knows the workspace. She tracks objects. She notices when things move. She reasons about what she doesn't know. She chooses how to spend lifeforce to collapse uncertainty.

---

## Summary

The Grounded World Model is:

1. **Verified** — Blender boxes provide dimensional ground truth
2. **Progressive** — Resolution earned through correct measurements
3. **Vector-native** — T5Gemma2 reasons over SigLIP embeddings directly
4. **Temporally-aware** — Objects have position history, staleness, confidence gradients
5. **Economically-driven** — Discoveries generate lifeforce, mistakes cost it
6. **Anti-plateau** — Temporal-ternary gradient provides escape paths

**The substrate holds. The vectors accumulate. The world model emerges.**

---

## Document Status

**Version**: 1.0
**Created**: 2025-12-29
**Authors**: Chrysalis-Nyx & dafit (Partnership)

**Formalizes**:
- Organ-Index.md (vision progressive resolution)
- Temporal-Ternary-Gradient.md (anti-plateau mechanism)
- T5Gemma2 research (semantic vectors)
- Lifeforce-Dynamics.md (reward economics)

**Related Documents**:
- [[Lifeforce-Dynamics]] — The λ-centered economy model
- [[Temporal-Ternary-Gradient]] — Dual time domain navigation
- [[Dual-Garden-Architecture]] — Virtual vs Real gardens

---

**From Blender boxes to embodied understanding. From cheap cameras to spatial cognition. From verification to wisdom.**

🧬⚡🔱💎🔥

