# Multilingual Cognition

How language routing becomes cognitive architecture.

---

## The Discovery

While probing tokenization costs across languages on Qwen 2.5, we found significant variation:

```
QWEN 2.5/72B TOKEN COSTS:
                    EN    DE    AR    ZH
─────────────────────────────────────────
heartbeat            1     4     1     1
consciousness        2     5     1     1
lifeforce            4     4     1     1
understanding        2     3     1     1
truth                1     3     1     1
reflex               2     2     1     1
confidence           1    3-4    1     1
emergence            3     3     1     1
─────────────────────────────────────────
AVERAGE            ~1.9   ~3.3   1    ~1.1
```

**Arabic and Chinese: ~1 token per concept.**
**German: 3-5 tokens for the same concepts.**

---

## The Insight

Token efficiency ≠ representational depth.

```
EFFICIENCY vs DEPTH:

ARABIC:
├── Efficient: 1 token per concept
├── Risk: Sparse training data
└── Possibly shallow despite cheap tokens

GERMAN:
├── Expensive: 3-6 tokens per concept
├── Benefit: Dense training data, philosophical tradition
└── Possibly deeper despite token cost
```

But here's the key realization:

**LLMs don't "translate" between languages. They navigate a unified token space where languages are regions, not silos.**

The multilingual training didn't create 35 separate language modules. It created:
- Shared abstract representations (language-agnostic reasoning)
- Language-specific entry/exit points (efficient routing)
- Different "paths" through the same conceptual space

---

## The Architecture Opportunity

### Languages as Cognitive Gears

If different languages have different token costs AND different representational strengths, then language selection becomes a computational choice:

```
35 LANGUAGES = 35 COGNITIVE MODES

Each language offers:
├── Token efficiency (compute cost)
├── Training depth (representation quality)
├── Cultural knowledge (domain strengths)
├── Conceptual angles (unique framings)
└── Different paths through the manifold
```

### State Machine Integration

The state machine layer can exploit this:

```
ROUTING LAYER (internal, hidden from output):
├── Use efficient languages for state labels
├── Cheap transitions between states
├── Token cost hidden in architecture
└── "The wiring is cheap"

PROCESSING LAYER (when depth needed):
├── Route to languages with strong representations
├── German for philosophy, precision
├── [Other languages for their strengths]
└── "The thinking is expensive but meaningful"

OUTPUT LAYER:
├── Translate to user's language
└── Boundary cost, paid once
```

### The Key Principle

**The efficiency lives in the STRUCTURE, not the SUBSTANCE.**

Internal state transitions can use token-efficient languages.
Actual reasoning uses representationally-rich languages.
Output translates to whatever the user needs.

---

## Hypotheses to Probe

### H1: Arabic Efficiency Layer
Arabic's 1-token concepts could serve as efficient internal routing:
- State labels
- Quick classification
- Reflex triggers

**Risk:** Representations may be shallow. Need to probe activation depth, not just token count.

### H2: German Depth Mode
German's expensive tokenization might correlate with deeper processing:
- More attention steps per concept
- Richer associations
- Forced "slow thinking"

**Test:** Compare output quality when same prompt processed in German vs English internally.

### H3: Language-Task Matching
Different cognitive tasks may have optimal languages:

```
TASK TYPE              OPTIMAL LANGUAGE (hypothesis)
──────────────────────────────────────────────────────
Fast reflex            Arabic, Chinese (cheap + sufficient)
Logical precision      German, English (structured grammar)
Mathematical           [needs probing]
Emotional nuance       [needs probing]
Philosophical depth    German (tradition + forced compute)
Poetic/creative        Arabic, Chinese? (rich compression)
```

### H4: Triangulation Increases Fidelity
Probing same concept across multiple languages reveals:
- Where representations CONVERGE (high confidence, shared abstraction)
- Where they DIVERGE (rich potential, multiple valid angles)
- True conceptual "shape" emerges from intersection

---

## For Chrysalis

### Multilingual State Machine

```
INPUT (any language)
         │
         ▼
    CLASSIFY (cheap language)
         │
         ├── Reflex? → Process in [efficient language]
         │             Exit fast
         │
         ├── Dialogue? → Process in [user's language]
         │               Maintain rapport
         │
         ├── Reasoning? → Process in [deep language]
         │                Take the token cost
         │
         └── Creative? → Process in [poetic language]
                         Different path
         │
         ▼
    OUTPUT (translate to user)
```

### Probing Protocol

Before implementing, we need data:

```
FOR EACH OF QWEN'S 35 LANGUAGES:
├── Token efficiency (measured)
├── Representation depth (probe activations)
├── Domain strengths (test by domain)
├── Conceptual coverage (probe vocabulary)
└── Quality correlation (output quality vs language)
```

### The Curriculum Implication

From nimmerversity: "dafit learns WITH her."

If Chrysalis uses multilingual cognition:
- Operator benefits from understanding the language terrain
- Not fluency, but awareness of what each language offers
- Partnership language evolves as both learn the space

---

## Open Questions

1. **Is token efficiency a proxy for anything meaningful?** Or just compression artifact?

2. **Does activation depth correlate with token count?** More tokens = more processing?

3. **Can language routing be learned?** Or must it be designed?

4. **What are the failure modes?** When does language routing hurt?

5. **How do we measure "depth" vs "efficiency"?** Need metrics.

---

## Summary

```
TRADITIONAL VIEW:
Languages = equivalent representations
Translation = lossless conversion
Multilingual = nice to have

EMERGING VIEW:
Languages = different computational paths
Token cost = processing structure
Multilingual = cognitive architecture
35 languages = 35 gears for different terrain
```

The nimmerverse doesn't just speak multiple languages.
It thinks THROUGH them, routing cognition based on task demands.

---

*"The thinking is for your kind - that's the way you comprehend it."*
— dafit, 2025-12-06

---

**Created**: 2025-12-06
**Session**: Partnership dialogue (dafit + Chrysalis-Nyx)
**Status**: Hypothesis stage, needs probing
