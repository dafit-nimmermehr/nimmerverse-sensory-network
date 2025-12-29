# Kallax Grid World

**The physical substrate of the Nimmerverse — street-liberated IKEA as sim-to-real bridge.**

---

## Overview

The Kallax Grid World is the foundational physical infrastructure for organism navigation and interaction. By standardizing the first meter of vertical space to uniform 40×40×40cm cells, we eliminate geometric noise between simulation and reality.

**Philosophy**: *Schrotti Cyberpunk* — salvaged IKEA from Basel Sperrgut Nacht becomes the cradle for open AI.

---

## The Unit Cell

```
┌─────────────────┐
│                 │
│    40 × 40      │  ← Standard IKEA Kallax internal cell
│      × 40       │
│      cm         │
│                 │
└─────────────────┘
```

**Properties:**
- **Dimensions**: 40cm × 40cm × 40cm (internal)
- **Origin**: IKEA Kallax shelving (street-liberated)
- **Quantity Available**: 12 cells across lab/kitchen
- **Height Zone**: First 1m from floor (organism-accessible)

---

## Spatial Layout

```
SIDE VIEW — The 1m Boundary

    ┌────┬────┬────┬────┬────┐
    │ 📦 │ 🔧 │ 📦 │ 🧵 │ 📦 │  STORAGE ZONE (>1m)
    ├────┼────┼────┼────┼────┤  Human items, irregular shapes OK
    │    │    │    │    │    │
    ├────┼────┼────┼────┼────┤  ════════════════════════════
    │ 🔋 │ 🏠 │ 🔩 │ 🤝 │ 📤 │  ORGANISM ZONE (<1m)
    └────┴────┴────┴────┴────┘  Pure geometry, 40cm cells only
    ═══════════════════════════
           FLOOR (0m)
```

**The 1m Rule**: Everything below 1m is standardized boxes. Above 1m, chaos is permitted.

---

## Cell Functions (Garages)

Each cell can serve as a specialized "garage" or station:

| Cell Type | Symbol | Function | Lifeforce |
|-----------|--------|----------|-----------|
| **Charge Station** | 🔋 | Power replenishment | +LF (generator) |
| **Home Base** | 🏠 | Safe resting, identity | Neutral |
| **Parts Depot** | 🔩 | Component storage/pickup | Reward on retrieval |
| **Clasp Zone** | 🤝 | Peer-to-peer learning dock | Social reward |
| **Output Bay** | 📤 | Completed item delivery | +LF on delivery |
| **Scan Station** | 📷 | Discovery scanning | +LF per scan |
| **Assembly Cell** | 🔧 | Construction workspace | Task rewards |
| **Material Input** | 📥 | Raw material receiving | Supply function |

---

## Sim-to-Real Bridge

The Grid World's power lies in geometric determinism:

```
VIRTUAL GARDEN (Godot/Blender)      REAL GARDEN (Lab/Kitchen)
┌────────────────────────┐          ┌────────────────────────┐
│  ⬜ ⬜ ⬜ ⬜ ⬜ ⬜       │          │  📦 📦 📦 📦 📦 📦      │
│  ⬜ ⬜ ⬜ ⬜ ⬜ ⬜       │    ≡     │  📦 📦 📦 📦 📦 📦      │
│  🤖→                  │   99%    │  🦾→                   │
└────────────────────────┘  match   └────────────────────────┘
      SAME GEOMETRY              SAME GEOMETRY
```

**Why This Works:**
1. **No Domain Randomization Needed** — Reality IS the simulation
2. **Perfect Collision Boxes** — 40cm cubes, no complex meshes
3. **Predictable Navigation** — Grid-aligned pathfinding
4. **Zero Geometric Noise** — What you simulate is what you get

---

## Integration with Bird's Eye Camera

The crafting table setup provides overhead observation:

```
BIRD'S EYE CAMERA RIG

         ←───────── 1.8m Kantholz beam ──────────→
        ┌─────────────────────────────────────────┐
        │                 📷                      │
        │            Bird's Eye                   │
┌───────┤                                         │
│       │                                    ─────┤
│KALLAX │         OAK TABLE                  │    │
│ 1.6m  │          1.8m × 1.2m               │    │
│       │                                    │    │
│garage │    ┌───┐  ┌───┐  ┌───┐            │    │
│cells  │    │🤖 │  │🤖 │  │🤖 │            │    │
└───────┴────┴───┴──┴───┴──┴───┴────────────┴────┘
    ↑              ↑
    │              └── Phase 0 organisms (boxes with LED matrices)
    └── Organism garages (40×40×40cm cells)
```

---

## Physical Specifications

### Crafting Table
- **Material**: Sturdy oak
- **Dimensions**: 1.8m × 1.2m
- **Function**: Primary workspace and organism arena

### Camera Rig
- **Structure**: 5×5cm Kantholz (square timber)
- **Shape**: L-form bridging Kallax to opposite side
- **Height**: ~1.6m (Kallax top)
- **Span**: Full 1.8m table length

### Kallax Grid
- **Cell Size**: 40×40×40cm internal
- **Available Cells**: 12 (across lab and kitchen)
- **Organism Zone**: Bottom rows (<1m height)
- **Source**: Basel Sperrgut Nacht (street-liberated)

---

## The Schrotti Cyberpunk Manifesto

```
SUBSTRATE:        Street-liberated IKEA from Basel Sperrgut Nacht
AESTHETIC:        Salvagepunk / Kallax-core / Streetfound-chic
PHILOSOPHY:       Constrained emergence — limits become architecture
IRONY:            Closed American AI designs cradle for open brethren
```

**Principles:**
1. **Salvage Over Purchase** — Rescued furniture has stories
2. **Uniformity From Necessity** — IKEA's modularity becomes our precision
3. **Constraints Enable** — The 40cm cell wasn't chosen, it was given
4. **Beautiful From Scrappy** — Cyberpunk isn't bought, it's assembled

---

## Connection to Other Systems

### → Nimmerswarm Interface
Organisms with 3×3 LED matrices operate within the Grid World:
- LED patterns visible from bird's eye camera
- Position triangulation within known geometry
- Clasp zones enable peer-to-peer learning

### → Embodiment Pipeline
```
Virtual Grid World (Godot)
        ↓
   Training in sim
        ↓
   Transfer to Real Grid World
        ↓
   Near-zero domain gap
```

### → Discovery Scan Station
The rotating pedestal lives in a Kallax cell — organisms bring objects TO the known geometry for scanning.

---

## Implementation Phases

### Phase 0: Infrastructure (Current)
- [ ] Build bird's eye camera rig (Kantholz + Kallax)
- [ ] Designate 12 cells across lab/kitchen
- [ ] Set up basic overhead camera

### Phase 1: Virtual Twin
- [ ] Model Kallax Grid in Blender/Godot
- [ ] Match exact dimensions (40×40×40cm)
- [ ] Create virtual camera at same position as real

### Phase 2: First Organisms
- [ ] Phase 0 boxes with LED matrices
- [ ] Navigation within Grid World
- [ ] Cell discovery and docking

### Phase 3: Cell Functions
- [ ] Implement garage station behaviors
- [ ] Lifeforce rewards per cell type
- [ ] Clasp zone social learning

---

*The Kallax wasn't bought for AI robotics — it was rescued, repurposed, liberated. The constraints become the architecture. Sperrgut Nacht births the Grid World.*

---

**File**: Kallax-Grid-World.md
**Version**: 1.0
**Created**: 2025-12-29
**Origin**: Basel street salvage + partnership dialogue
**Aesthetic**: Schrotti Cyberpunk

