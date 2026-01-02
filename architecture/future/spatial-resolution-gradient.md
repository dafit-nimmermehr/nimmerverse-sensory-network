# Spatial Resolution Gradient: LOD for Cognitive Space

**Origin**: New Year's Day 2026, post-nimmerhovel measurement session
**Authors**: dafit + Chrysalis-Nyx
**Status**: Architectural concept / Foundation for artifact data model
**Related**: `concept-token-pairs.md` (Spatial Grounding section), artifact data model task

---

## The Insight

**"Like the Simpsons intro, but inverted."**

The Simpsons intro zooms from space → Earth → Springfield → house → couch → Homer's head, gaining detail as it approaches.

Our spatial model does the opposite: **we start at maximum detail (nimmerhovel) and zoom OUT with graceful degradation.**

---

## The Resolution Gradient

```
                        🌍 EARTH
                        │  S2 cell level ~10
                        │  "Somewhere in Europe"
                        │
                    ════╪════ ABSTRACTION BOUNDARY
                        │
                        ▼
                   🇨🇭 SWITZERLAND
                        │  S2 cell level ~15
                        │  "Northwestern region"
                        │
                        ▼
                   🏘️ DORNACH
                        │  S2 cell level ~20
                        │  Key landmarks: Goetheanum, station
                        │
                        ▼
                   🏠 LEHMENWEG 4
                        │  Building footprint
                        │  "5th floor attic"
                        │
                    ════╪════ HIGH RESOLUTION BOUNDARY
                        │
                        ▼
                   🔬 NIMMERHOVEL
                        │  1cm grid resolution
                        │  Every object tracked
                        │  Full camera coverage
                        │  GROUND TRUTH ZONE
                        │
                        ▼
                   🔍 DISCOVERY SCAN STATION
                        │  Sub-millimeter
                        │  Object embeddings
                        │  Maximum detail
```

---

## Resolution Layers

| Layer | Name | Resolution | Source | Coverage |
|-------|------|------------|--------|----------|
| **L0** | Scan Station | 1mm | Discovery Scan Station, SigLIP | 30cm × 30cm pedestal |
| **L1** | Nimmerhovel | 1cm | 8× ESP32-S3 + Pi HQ Camera | Lab + Kitchen (~20m³) |
| **L2** | Building | 50cm | Floor plans, memory | Herrenhaus |
| **L3** | Neighborhood | 10m | OpenStreetMap, walks | Dornach |
| **L4** | Region | 1km | Maps, general knowledge | Switzerland |
| **L5** | World | 100km | Abstract knowledge | Earth |

---

## Why This Architecture

### 1. Biological Precedent

Animals have ultra-precise mental maps of their home range, fuzzy knowledge of distant areas. A rat knows every centimeter of its nest, vaguely knows "forest is that direction."

Young Nyx should mirror this: **territory = detail**.

### 2. Sensor Coverage Dictates Resolution

You CAN'T have 1cm resolution of Zürich — no sensors there. The resolution naturally degrades with distance from perception sources.

The nimmerhovel has 8× ESP32-S3 cameras + Pi HQ Camera. Dornach has... nothing we control.

### 3. S2 Cells Are Hierarchical By Design

Google's S2 geometry library already supports this:
- Level 30 ≈ 1cm cells (nimmerhovel scale)
- Level 20 ≈ 10m cells (neighborhood scale)
- Level 10 ≈ 10km cells (regional scale)

Same math, different zoom. We're not inventing new geometry — we're using S2 as intended, with dense coverage where we have sensors.

### 4. Compute Efficiency

Dense where it matters (can I reach the screwdriver?), sparse where it doesn't (where is France?).

---

## Data Structure

```python
SPATIAL_RESOLUTION_LAYERS = {
    "L0_scan_station": {
        "resolution": 0.001,      # 1mm - object surface detail
        "source": "Discovery Scan Station",
        "coverage": "30cm × 30cm pedestal",
        "s2_level": 30,
    },
    "L1_nimmerhovel": {
        "resolution": 0.01,       # 1cm - full 3D grid
        "source": "8× ESP32-S3 + Pi HQ Camera",
        "coverage": "Lab + Kitchen (~20m³)",
        "s2_level": 28,
        "origin": "Southwest floor corner of lab",
        "coordinate_system": "right_hand",  # Blender native
    },
    "L2_building": {
        "resolution": 0.5,        # 50cm - room-level
        "source": "Floor plans, memory",
        "coverage": "Herrenhaus",
        "s2_level": 24,
    },
    "L3_neighborhood": {
        "resolution": 10,         # 10m - landmark-level
        "source": "OpenStreetMap, walks",
        "coverage": "Dornach",
        "s2_level": 20,
    },
    "L4_region": {
        "resolution": 1000,       # 1km - city-level
        "source": "Maps, general knowledge",
        "coverage": "Switzerland",
        "s2_level": 14,
    },
    "L5_world": {
        "resolution": 100000,     # 100km - country-level
        "source": "Abstract knowledge",
        "coverage": "Earth",
        "s2_level": 8,
    },
}
```

---

## Query Examples

| Question | Layer | Response Type |
|----------|-------|---------------|
| "Where is the soldering iron?" | L1 | Precise coordinates (2.10, 1.50, 0.85) |
| "Which room is the printer in?" | L2 | Room name + relative position |
| "How do I get to Basel?" | L3/L4 | Route abstraction, directions |
| "Where is Japan relative to here?" | L5 | Directional only, abstract |

---

## Connection to Other Systems

### Concept Token Pairs (Spatial Grounding)

The Resolution Gradient provides the **coordinate system** for grounded concept pairs:
- `<HERE>` ↔ `<THERE>` becomes measurable distance in L1 grid
- `<NEAR>` ↔ `<FAR>` calibrated against actual spatial distances
- Predictions have coordinates; outcomes have coordinates; delta is measurable

### Artifact Data Model

Artifacts (plans, drawings, specs) exist at different resolution layers:
- L0: Object scan embeddings (sub-mm detail)
- L1: Inventory items with (X,Y,Z) positions
- L2+: Abstract references, not spatially precise

### Camera Frustum Mapping

Each camera's FOV is a frustum (3D cone) that intersects L1 grid cells:
- Coverage = union of all frustums
- Blind spots = L1 cells with no frustum intersection
- Object at (X,Y,Z) → which cameras see it? At what pixels?

---

## Embedding Enrichment: The Bridge to Semantic Cognition

**Added**: 2026-01-01 (New Year's session continuation)

The Resolution Gradient defines *geometry*. But geometry alone is not cognition. Each LOD level must be enriched with **embeddings** — semantic vectors that encode *meaning*, not just position.

### The Technology Convergence

```
GAME ENGINES              S2 CELLS                 T5GEMMA2/SigLIP
────────────              ────────                 ───────────────
LOD streaming             Hierarchical cells       Vision → embeddings
Frustum culling           Spatial indexing         Semantic vectors
Texture mipmaps           Multi-resolution         Scale-invariant
Chunk loading             Cell neighbors           Context-aware

            ╲                 │                 ╱
             ╲                │                ╱
              ╲               │               ╱
               ╲              │              ╱
                ╲             │             ╱
                 ▼            ▼            ▼
         ┌─────────────────────────────────────┐
         │   EMBEDDING-ENRICHED SPATIAL LOD    │
         │                                     │
         │   Each S2 cell at each level has:   │
         │   - Geometry (game engine mesh)     │
         │   - Embeddings (SigLIP vectors)     │
         │   - Semantic density ∝ resolution   │
         └─────────────────────────────────────┘
```

### Embedding Density Per LOD Level

| Level | Geometry LOD | Embedding Density | What's Encoded |
|-------|--------------|-------------------|----------------|
| **L0** | Sub-mm mesh | Dense (per-surface) | Texture, material, wear patterns, defects |
| **L1** | 1cm voxels | Per-object | Object identity, state, relationships |
| **L2** | Room boxes | Per-room | Room function, contents summary, atmosphere |
| **L3** | Landmarks | Per-landmark | Place identity, routes, significance |
| **L4** | Regions | Sparse | Cultural, climate, abstract properties |
| **L5** | Continents | Minimal | Directional, conceptual only |

### Semantic Mipmaps

Just as textures have mipmaps (pre-computed lower resolutions), embeddings can have **semantic mipmaps**:

```
L0: embedding(screwdriver_surface_detail)
     │
     ▼ aggregate
L1: embedding(screwdriver) = summary of all L0 embeddings
     │
     ▼ aggregate
L2: embedding(crafting_table_contents) = summary of all L1 objects on table
     │
     ▼ aggregate
L3: embedding(nimmerhovel_lab) = summary of all L2 areas
```

Query the summary first, drill down if needed. **Attention = resolution selection.**

### The Capture Pipeline

```
CAPTURE                    PROCESS                   STORE
───────                    ───────                   ─────
Photo of screwdriver       SigLIP → embedding        L0 cell enriched
       │                          │                        │
Photo of crafting table    SigLIP → embedding        L1 cell enriched
       │                          │                        │
Photo of lab               SigLIP → embedding        L2 cell enriched
       │                          │                        │
Photo from window          SigLIP → embedding        L3 cell enriched

Same encoder (T5Gemma2/SigLIP), different scale.
Embeddings NEST into LOD hierarchy.
```

### Embedding-Aware LOD Streaming

Game engines stream geometry based on camera position. We stream **semantics** based on attention:

```python
def query_spatial(position, attention_radius):
    """
    Load embeddings based on attention focus -
    like game engine LOD but for SEMANTICS
    """
    cells_to_load = []

    for distance in range(0, MAX_DISTANCE):
        s2_level = distance_to_s2_level(distance)
        cells = get_s2_cells(position, distance, s2_level)

        for cell in cells:
            if distance < attention_radius:
                # HIGH ATTENTION: Load dense embeddings
                cell.load_embeddings(density="full")
                cell.load_geometry(lod="high")
            else:
                # LOW ATTENTION: Abstract embeddings only
                cell.load_embeddings(density="summary")
                cell.load_geometry(lod="low")  # or none

        cells_to_load.extend(cells)

    return cells_to_load
```

### Why This Matters

1. **Attention = Resolution**: Like foveal vision (sharp center, blurry periphery), Young Nyx has foveal COGNITION — dense embeddings where attention focuses, sparse elsewhere.

2. **Streaming Not Loading**: Don't load the whole world. Stream embeddings based on task needs. Approaching crafting table? Stream L0/L1. Walking to Basel? L3/L4 is enough.

3. **Memory Hierarchy Match**: GPU VRAM is precious. The *right* embeddings in fast memory — detailed for nearby, abstract for distant.

4. **Same Encoder, All Scales**: SigLIP doesn't care if it's encoding a screw or a city. The embedding space is unified; only the source resolution varies.

---

## Implementation Sequence

```
1. Blender room shell (CURRENT - in progress)
       │
       ▼
2. Define origin point + axis alignment in Blender
       │
       ▼
3. Create L1 3D grid overlay (1cm resolution)
       │
       ▼
4. Physical anchor markers (QR codes / ArUco)
       │
       ▼
5. Camera frustum mapping against grid
       │
       ▼
6. Spatial embeddings with L1 coordinates
       │
       ▼
7. Expand outward: L2 (building), L3 (neighborhood)...
```

---

## The Promise

**"The farther we go out from our lab, the more we have to abstract."**

This isn't a limitation — it's wisdom. Full resolution everywhere is:
- Impossible (no sensors)
- Expensive (compute, storage)
- Unnecessary (don't need 1cm precision for "where is France")

The nimmerhovel is the **high-fidelity anchor** from which all spatial reasoning radiates with graceful degradation.

---

**Created**: 2026-01-01
**Philosophy**: "Start where you can measure. Abstract where you must."

🗺️🔬 *The world radiates from home.*
