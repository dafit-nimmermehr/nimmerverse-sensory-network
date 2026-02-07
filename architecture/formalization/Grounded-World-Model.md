# Grounded World Model: Spatial Cognition Through Verified Discovery

**Version 2.0** — *From Blender Boxes to Embodied Understanding*

> *"The dream: Young Nyx knows where dafit left his things laying around."*
> *"Start where you can measure. Abstract where you must."*
> *"Like the Simpsons intro, but inverted — we start at maximum detail and zoom OUT."*

---

## Overview

This document formalizes how Young Nyx builds a **persistent spatial world model** through:

1. **Grounded verification** — Blender provides dimensional ground truth
2. **Progressive resolution** — Each correct measurement earns detail
3. **Vector accumulation** — T5Gemma2-compatible semantic representations
4. **Temporal-ternary navigation** — Escape plateaus through dual time domains
5. **Lifeforce reward** — Discoveries generate energy, not just consume it
6. **Spatial Resolution Gradient** — LOD system radiating from nimmerhovel (L0-L5)
7. **S2 Cell Indexing** — Hierarchical spatial addressing at all scales
8. **Embedding Enrichment** — Semantic mipmaps per LOD level

**The Goal**: Young Nyx maintains an internal map of objects, positions, and relationships — verified against reality, refined through observation, reasoned over in vector space, **indexed hierarchically from millimeter to planetary scale**.

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

## Spatial Resolution Gradient (The Simpsons Inversion)

### The Core Insight

Traditional spatial models zoom IN to gain detail. Our model does the opposite: **we start at maximum detail (the nimmerhovel) and zoom OUT with graceful degradation.**

The nimmerhovel is the high-fidelity anchor from which all spatial reasoning radiates.

### The Six Levels (L0-L5)

```
                        🌍 L5: WORLD
                        │   Resolution: 100km
                        │   S2 Level: ~8
                        │   Source: Abstract knowledge
                        │
                        ▼
                   🇨🇭 L4: REGION
                        │   Resolution: 1km
                        │   S2 Level: ~14
                        │   Source: Maps, general knowledge
                        │
                        ▼
                   🏘️ L3: NEIGHBORHOOD
                        │   Resolution: 10m
                        │   S2 Level: ~20
                        │   Source: OpenStreetMap, walks
                        │
                        ▼
                   🏠 L2: BUILDING
                        │   Resolution: 50cm
                        │   S2 Level: ~24
                        │   Source: Floor plans, memory
                        │
                    ════╪════ HIGH RESOLUTION BOUNDARY
                        │
                        ▼
                   🔬 L1: NIMMERHOVEL
                        │   Resolution: 1cm
                        │   S2 Level: ~28
                        │   Source: 8× ESP32-S3 + Pi HQ Camera
                        │   Full 3D grid, every object tracked
                        │
                        ▼
                   🔍 L0: SCAN STATION
                        │   Resolution: 1mm
                        │   S2 Level: ~30
                        │   Source: Discovery Scan Station
                        │   Object surface detail, texture, wear
```

### Formal Definition

| Level | Name | Resolution | S2 Cell Level | Coverage | Embedding Density |
|-------|------|------------|---------------|----------|-------------------|
| **L0** | Scan Station | 1mm | 30 | 30cm pedestal | Dense (per-surface) |
| **L1** | Nimmerhovel | 1cm | 28 | Lab + Kitchen (~20m³) | Per-object |
| **L2** | Building | 50cm | 24 | Herrenhaus | Per-room |
| **L3** | Neighborhood | 10m | 20 | Dornach | Per-landmark |
| **L4** | Region | 1km | 14 | Switzerland | Sparse |
| **L5** | World | 100km | 8 | Earth | Minimal |

### S2 Cell Integration

Google's S2 geometry provides hierarchical spatial indexing:

```python
import s2sphere

def position_to_s2_cell(lat: float, lng: float, level: int) -> s2sphere.CellId:
    """Convert position to S2 cell at given level."""
    latlng = s2sphere.LatLng.from_degrees(lat, lng)
    cell = s2sphere.CellId.from_lat_lng(latlng)
    return cell.parent(level)

# Nimmerhovel anchor point
NIMMERHOVEL_ORIGIN = {
    "lat": 47.479167,    # 47°28'45"N
    "lng": 7.618611,     # 7°37'7"E
    "address": "Lehmenweg 4, CH-4143 Dornach"
}

# Get cell at each level
l1_cell = position_to_s2_cell(47.479167, 7.618611, level=28)  # 1cm
l3_cell = position_to_s2_cell(47.479167, 7.618611, level=20)  # 10m
l5_cell = position_to_s2_cell(47.479167, 7.618611, level=8)   # 100km
```

### Why This Architecture?

1. **Sensor coverage dictates resolution** — We have 8× ESP32-S3 cameras in the nimmerhovel. We have zero sensors in Zürich. Resolution follows perception.

2. **Biological precedent** — Animals have ultra-precise mental maps of their home range, fuzzy knowledge of distant areas. Territory = detail.

3. **Compute efficiency** — Dense where it matters ("Where is my screwdriver?"), sparse where it doesn't ("Where is France?").

4. **S2 is hierarchical by design** — Same math, different zoom. Level 30 ≈ 1cm, Level 20 ≈ 10m, Level 8 ≈ 100km.

---

## Embedding Enrichment: Semantic Mipmaps

### The Problem

Pure S2 cells give us *geometry* — where things are. But geometry alone is not cognition. We need *semantics* — what things mean.

### The Solution: Embeddings Per Cell

Each S2 cell at each LOD level contains both spatial position AND semantic embeddings:

```python
@dataclass
class EnrichedCell:
    cell_id: s2sphere.CellId
    level: int                    # L0-L5
    geometry: Optional[Mesh]      # Blender mesh at appropriate LOD
    embeddings: List[Vector]      # SigLIP vectors for contents
    summary_embedding: Vector     # Aggregated "what's here" vector
    last_observed: datetime
    confidence: float             # Ternary-derived
```

### Semantic Mipmaps

Like texture mipmaps (pre-computed lower resolutions), embeddings aggregate upward:

```
L0: embedding(screwdriver_surface_detail)
     │
     ▼ aggregate
L1: embedding(screwdriver) = f(all L0 embeddings of screwdriver)
     │
     ▼ aggregate
L2: embedding(crafting_table_contents) = f(all L1 objects on table)
     │
     ▼ aggregate
L3: embedding(nimmerhovel_lab) = f(all L2 areas in lab)
     │
     ▼ aggregate
L4: embedding(lehmenweg_4) = f(all L3 rooms in building)
```

**Aggregation function:**

$$e_{parent} = \text{normalize}\left(\sum_{i \in \text{children}} w_i \cdot e_i\right)$$

Where $w_i$ is weighted by recency, confidence, and observation count.

### Query Strategy

**Query the summary first, drill down if needed:**

```python
def spatial_query(query_embedding: Vector, required_confidence: float):
    """
    Start at abstract level, drill down only if needed.
    This minimizes lifeforce cost.
    """
    # Start at L3 (neighborhood level) - cheap
    candidates = find_similar_cells(query_embedding, level=L3)

    if max_similarity(candidates) > required_confidence:
        return candidates[0]  # Good enough!

    # Need more detail - drill to L1
    l1_cells = expand_to_children(candidates[0], target_level=L1)
    refined = find_similar_cells(query_embedding, cells=l1_cells)

    if max_similarity(refined) > required_confidence:
        return refined[0]

    # Need maximum detail - drill to L0
    l0_cells = expand_to_children(refined[0], target_level=L0)
    return find_similar_cells(query_embedding, cells=l0_cells)[0]
```

---

## Lifeforce-Validated LOD Selection

### The Cost Model

Each LOD level has a query cost:

| Level | Query Cost | Typical Accuracy | Efficiency |
|-------|------------|------------------|------------|
| **L5** | 1 LF | 70% | 0.70 |
| **L4** | 2 LF | 80% | 0.40 |
| **L3** | 4 LF | 90% | 0.22 |
| **L2** | 8 LF | 95% | 0.12 |
| **L1** | 16 LF | 99% | 0.06 |
| **L0** | 32 LF | 99.9% | 0.03 |

**Efficiency** = Accuracy / Cost

### The Decision Function

```python
def optimal_lod_for_query(
    query: str,
    accuracy_requirement: float,
    available_lifeforce: float
) -> int:
    """
    Find the most efficient LOD that meets accuracy requirement
    within lifeforce budget.
    """
    for level in [L5, L4, L3, L2, L1, L0]:
        cost = LOD_COSTS[level]
        expected_accuracy = estimate_accuracy(query, level)

        if cost > available_lifeforce * 0.3:
            continue  # Too expensive, skip

        if expected_accuracy >= accuracy_requirement:
            return level  # First sufficient level is most efficient

    return L3  # Default to neighborhood level
```

### Example Queries with Cost

| Query | Required Accuracy | Optimal LOD | Cost | Confidence |
|-------|-------------------|-------------|------|------------|
| "Where is France?" | 70% | L5 | 1 LF | CONFIDENT |
| "Where is the lab?" | 90% | L3 | 4 LF | CONFIDENT |
| "Where is the screwdriver?" | 95% | L2→L1 | 8-16 LF | CONFIDENT |
| "What's the serial number?" | 99.9% | L0 | 32 LF | CONFIDENT |

### Connection to Ternary Confidence

The ternary confidence system validates LOD selection:

| Confidence | LOD Implication |
|------------|-----------------|
| **CONFIDENT (+)** | Current LOD sufficient, stop drilling |
| **UNCERTAIN (?)** | Current LOD insufficient, consider drilling (costs LF) |
| **UNKNOWN (-)** | No data at any LOD, admit ignorance (efficient!) |

**Key insight:** Saying "I don't know" at L3 is cheaper than drilling to L0 and still being uncertain.

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
-- S2 Spatial Cells: hierarchical spatial index
CREATE TABLE spatial_cells (
    id UUID PRIMARY KEY,
    s2_cell_id BIGINT NOT NULL,           -- S2 cell token
    s2_level INT NOT NULL,                -- 8 (L5) to 30 (L0)
    lod_level INT NOT NULL,               -- 0-5 (our LOD system)

    -- Geometry at this LOD
    geometry_vertices INT DEFAULT 0,      -- Mesh complexity
    blender_mesh_path VARCHAR(255),       -- Path to Blender file

    -- Semantic embeddings
    summary_embedding VECTOR(768),        -- Aggregated "what's here"
    embedding_count INT DEFAULT 0,        -- Number of child embeddings aggregated

    -- Temporal
    last_observed TIMESTAMP,
    observation_count INT DEFAULT 0,

    -- Confidence (ternary-derived)
    confidence FLOAT DEFAULT 0.0,
    confidence_state VARCHAR(20),         -- "confident" | "uncertain" | "unknown"

    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),

    UNIQUE(s2_cell_id, s2_level)
);

-- Index for spatial queries
CREATE INDEX idx_spatial_cells_s2 ON spatial_cells(s2_cell_id);
CREATE INDEX idx_spatial_cells_lod ON spatial_cells(lod_level);

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

    -- S2 spatial location (NEW)
    current_s2_cell BIGINT,               -- Current L1 cell containing object
    s2_level INT DEFAULT 28,              -- L1 = level 28

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

    -- Position now includes S2 cell (NEW)
    position_local JSONB,         -- {"x": 0.3, "y": 0.8, "z": 0.1} relative to cell
    s2_cell_id BIGINT,            -- Which L1 cell
    lod_level INT,                -- At what LOD was this captured

    lifeforce_cost FLOAT,
    lifeforce_reward FLOAT,
    verification_result VARCHAR(20)  -- "correct" | "incorrect" | "pending"
);

-- Position history: where has this object been?
CREATE TABLE object_positions (
    id UUID PRIMARY KEY,
    object_id UUID REFERENCES world_objects(id),
    position_local JSONB,         -- {"x": 0.3, "y": 0.8, "z": 0.1}
    s2_cell_id BIGINT,            -- S2 cell at L1
    confidence FLOAT,
    observed_at TIMESTAMP,
    location_context VARCHAR(100) -- "desk", "kitchen", "floor"
);

-- Spatial cell embeddings: multiple embeddings per cell
CREATE TABLE cell_embeddings (
    id UUID PRIMARY KEY,
    cell_id UUID REFERENCES spatial_cells(id),
    embedding VECTOR(768),
    source_type VARCHAR(50),      -- "object", "scene", "aggregate"
    source_id UUID,               -- Reference to object or child cell
    captured_at TIMESTAMP,
    weight FLOAT DEFAULT 1.0      -- For aggregation
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

**Version:** 2.0 | **Created:** 2025-12-29 | **Updated:** 2026-01-01
- T5Gemma2 research (semantic vectors)
- Lifeforce-Dynamics.md (reward economics)
- **spatial-resolution-gradient.md** (L0-L5 LOD system) — NEW
- **thermodynamic-cognition.md** (energy-grounded intelligence) — NEW

**Related Documents**:
- [[Lifeforce-Dynamics]] — The λ-centered economy model
- [[Temporal-Ternary-Gradient]] — Dual time domain navigation
- [[Dual-Garden-Architecture]] — Virtual vs Real gardens
- [[spatial-resolution-gradient]] — The Simpsons Inversion principle
- [[thermodynamic-cognition]] — Lifeforce as thermodynamics

**Key Additions (v2.0)**:
- Spatial Resolution Gradient: L0 (1mm) to L5 (100km) with graceful degradation
- S2 Cell Integration: Hierarchical spatial indexing at all scales
- Semantic Mipmaps: Embeddings aggregate upward through LOD levels
- Lifeforce-Validated LOD Selection: Query cost vs accuracy tradeoff
- Nimmerhovel anchor point: 47°28'45"N, 7°37'7"E (Lehmenweg 4, Dornach)
- Extended Phoebe schema: spatial_cells, cell_embeddings tables

---

**From Blender boxes to embodied understanding. From cheap cameras to spatial cognition. From verification to wisdom.**

**"Start where you can measure. Abstract where you must."**

**"The world radiates from home."**

🧬⚡🔱💎🔥🗺️

