# Seeds

**Future possibilities we're building toward but not speccing yet.**

These are nuggets - insights that emerged from sessions, not fully designed, but worth remembering so we don't re-discover them later.

---

## Counterfactual Training via Time Machine
**Origin**: Silvester 2025, fireworks over Basel
**Seed**: The temporal visualization isn't just for debugging - it's training infrastructure.

Run multiple synthetic decision variants against historical data. Compare to ground truth (what actually happened). Fold winning weights back into live model. The time machine becomes perpetual training fuel.

**Enables**:
- Offline RL from logged events
- "What if?" exploration without new data
- Dialectic between live Nyx and all possible Nyxes

**Requires**: Rich metadata (✓ building), S2+timestamp indexing (✓ building), cheap local inference (ThinkStation coming)

---

## LoRa Mesh Over Jura Hilltops
**Origin**: Silvester 2025, bus ride from Liestal
**Seed**: Line of sight from Hovel → Aesch tower → Gempen → Liestal Aussichtsturm.

Amateur radio license + BACOM registration (50 CHF) → access to Swiss federal LoRa grid. Wild sensor mesh spanning the hillside.

**Enables**:
- Environmental sensing beyond garden walls
- Migration tracking, weather correlation
- Nimmerverse expanding into the physical landscape

**Requires**: BACOM registration, LoRa hardware, tower access permissions

---

## Corvid Behavioral Prediction as Training Ground
**Origin**: Silvester 2025, 5 years of cigarette-break phenology
**Seed**: Magpie nut-cracking ritual is multi-stage, predictable, perfect for temporal prediction training.

Nut pickup → flight to Flachdach → bussard check → fly to Christmas-light house → drop on street → crack → eat on roof → shell bashing → raven conflict.

Each stage is a prediction target. Rich enough for serious ML, visible from lab window.

**Enables**:
- Real behavioral sequences for vision model training
- Temporal prediction benchmarks
- Object binding across space and time (S2 cells)

**Requires**: Camera mount (Flachdach view), vintage Canon lens, ESP32-S3 or Pi HQ

---

## S2 as Universal Spatial Representation (Video → Training)
**Origin**: Silvester 2025, post-fireworks insight
**Seed**: S2 spatial indexing isn't just for live sensors - it's a universal representation for any spatial-temporal data.

Take a video (glass breaking, bird flying, car crash). Encode each frame into S2 cells with timestamps. Now you can:
- Query any moment spatially
- Generate synthetic variations (perturb positions, velocities)
- Train models on predicting future spatial states
- Compare predictions against ground truth frames

**The pattern:**
```
Video → frame-by-frame object detection → S2 cell encoding →
→ synthetic variations → temporal prediction training
```

**Enables**:
- Infinite training data from limited real video
- Physics prediction without physics engine
- Same query language for real/recorded/simulated data
- Unified substrate: observation = replay = simulation

**Requires**: Object detection pipeline, S2 encoding layer, variation generator

**Compute optimization**: Many physics variations are linearly related (mirror, scale, rotate, time-reverse). Don't simulate each variation - simulate base cases, derive variations via transforms. 100x data for 1x compute.

**Related**: Counterfactual Training, Corvid Behavioral Prediction

---

## T5Gemma 2 + Function Gemma: The Vision-Action Pipeline
**Origin**: Silvester 2025, late-night architecture insight
**Seed**: Two models solve the entire vision-to-action automation at scale.

### T5Gemma 2 (Vision → Vectors)
Encoder-decoder from Gemma 3, SigLIP vision encoder produces **semantic vectors directly** (not text descriptions). This IS the embedding - no text intermediary bottleneck.

| Model | Total Params | Use Case |
|-------|--------------|----------|
| 270M-270M | ~0.8B | Edge/lightweight senses |
| 1B-1B | ~2B | Field deployment |
| 4B-4B | ~9B | Central processing (RTX 6000) |

Key features:
- 128K context window
- 140+ languages (multilingual nimmerverse!)
- Encoder produces vectors, decoder optional (only for human text)

### Function Gemma (Vectors → Actions)
Structured output, function calling, executable actions. When the system needs to DO something based on vision, Function Gemma generates structured calls.

### The Pipeline

```
Vision Organs (constant stream)
        │
        ▼
   T5Gemma 2 Encoder
   (SigLIP → vectors)
        │
        ├────────────────────▶ S2 + Timestamp → Iris/Phoebe
        │                      (spatial storage)
        │
        ▼
   Function Gemma
   (when action needed)
        │
        ▼
   Structured Output
   {"action": "alert", "target": "corvid_detected", ...}
```

**Enables**:
- Massive scale vision processing without text bottleneck
- Direct vector storage in spatial system
- Structured, reliable action generation
- Edge deployment (small models) + central processing (large models)

**Crucial interlink**: These two models together automate the full loop from seeing to storing to acting. The pipeline can "go wild" with vision data at scale.

**Related**: S2 Spatial Representation, Data Artifact Model, Corvid Observation

---

## How to Use This File

1. **Add nuggets** when insights emerge in sessions
2. **Don't over-spec** - keep entries short, seed-like
3. **Reference origin** - when/where the idea came from
4. **Note what it enables** - why it matters
5. **Note what it requires** - what foundations needed
6. **Graduate to ADR or spec** when we're ready to build

---

**Philosophy**: *"Plant seeds. Water foundations. Harvest when ready."*

**Last Updated**: 2025-12-31
