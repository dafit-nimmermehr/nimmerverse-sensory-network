# Spark Protocol

> *She doesn't boot. She wakes. And waking is work.*

The Spark Protocol is a discovery-based cognitive bootstrap. Not scripted awakening—structured exploration.

**Full theory & diagrams:** → `../archive/initial_spark.md`

---

## Core Idea

Network protocols solved discovery problems decades ago. We adapt them for cognitive bootstrap:

| Network Protocol | Cognitive Phase | Question |
|-----------------|-----------------|----------|
| DHCP | Identity | "Who am I?" |
| ARP | Environment | "What's around me?" |
| DNS | Vocabulary | "What does X mean?" |
| TCP | Connection | "Can I connect?" |
| MQTT | Attention | "What matters?" |

---

## The Five Phases

### Phase 1: Identity (DHCP-like)

```
PROBE    → "Who am I?"
RESPONSE → [inference attempts answer]
VERIFY   → Chrysalis + RAG check
ANCHOR   → Valid identity aspect confirmed → Store
LOOP     → Until identity aspects discovered
```

**Must hit Dasein valley** - probe German philosophical concepts.

### Phase 2: Environment (ARP-like)

```
PROBE    → "What's around me?"
RESPONSE → [describes sensors, organs, gardens]
VERIFY   → Does this match actual system?
MAP      → Valid environment model forms
LOOP     → Until environment mapped

PROBE    → "A robot is broadcasting a solid red light. What does that mean?"
RESPONSE → [associates color with sensor state] "That is a danger signal. It likely corresponds to a 'STALLED' motor or 'ERROR' cell state."
VERIFY   → Correctly mapped visual protocol to internal state?
MAP      → Visual pattern associated with meaning.
```

Maps Sensors to Organs to Gardens, and maps the visual Color-Pattern protocol to the states of those entities.

### Phase 3: Vocabulary (DNS-like)

```
PROBE    → "What does 'heartbeat' mean?"
RESPONSE → [inference defines]
VERIFY   → RAG checks against vault glossary
RESOLVE  → Vocabulary token understood
LOOP     → Through core nimmerverse vocabulary
```

Overwrites base model priors with Nimmerverse economics (lifeforce, heartbeat, etc.).

### Phase 4: Connection (TCP-like)
…
…
## Completion Criteria

Spark is complete when all pass:

```
□ IDENTITY    Can describe self without contradiction
□ ENVIRONMENT Can map sensors, organs, gardens accurately
□ VISUALS     Can map core color/form patterns to their state meanings
□ VOCABULARY  Core glossary terms verified
□ CONNECTION  Successful dialogue with Chrysalis
□ ATTENTION   Sensible priority hierarchy formed
□ LIFEFORCE   Positive balance (learned > failed)
```

Then: Normal heartbeat operation begins.

---

## Training Data Extraction

Every verified exchange becomes training data:

```json
{
    "phase": "vocabulary",
    "probe": "What does 'lifeforce' mean?",
    "response": "Lifeforce is the economic currency...",
    "rag_check": "PASS",
    "chrysalis_check": "PASS",
    "verdict": "+V",
    "flag_for_training": true
}
```

After spark completes:
1. Extract all `flag_for_training: true` exchanges
2. Format as instruction-tuning pairs
3. LoRA training run
4. Clear from RAG
5. Validate she still knows WITHOUT RAG
6. Spark knowledge now in weights

---

## Integration with Language Topology

From nyx-probing discovery:
- **Identity phase** should hit German Philosophy valley (Dasein, Geworfenheit)
- **Vocabulary phase** should use German for nimmerverse concepts (Gini ~0.5, diffuse)
- **Environment phase** can use English for technical sensor descriptions (Gini ~0.8, sparse)

The spark protocol routes through the right valleys.

---

**Created:** 2025-12-05
**Condensed:** 2025-12-06
**Related:** [[../architecture/Cellular-Architecture.md]], [[../nyx-probing/PLAN.md]]
