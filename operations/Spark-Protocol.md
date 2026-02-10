# Spark Protocol

> *She doesn't boot. She executes a protocol. And every handshake is verified.*

The Spark Protocol bootstraps Young Nyx through structured K8s handshakes. Not conversation—deterministic protocol execution with typed JSON schemas.

**Canonical specification:** → [`../architecture/Initial-Spark.md`](../architecture/Initial-Spark.md) (v3.0)

---

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                    SPARK PROTOCOL FLOW                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   SPARK CONTROLLER (K8s Job)                                    │
│         │                                                        │
│         │ generates intent per phase                             │
│         ▼                                                        │
│   FUNCTION GEMMA (Translation Layer)                            │
│         │                                                        │
│         │ Intent → Typed JSON (schema-validated)                 │
│         ▼                                                        │
│   NATS MESSAGE BUS                                              │
│         │                                                        │
│         │ nimmerverse.spark.{phase}.{action}                     │
│         ▼                                                        │
│   K8S CELLS (respond with ACK/NACK)                             │
│         │                                                        │
│         │ verified data                                          │
│         ▼                                                        │
│   YOUNG NYX (receives protocol-verified state)                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Key principle:** Function Gemma guarantees structured output. No free-form text parsing. JSON or fail.

---

## The Five Phases

Network protocols solved discovery problems decades ago. We adapt them for cognitive bootstrap:

| Phase | Protocol | Purpose | K8s Target |
|-------|----------|---------|------------|
| 1. IDENTITY | DHCP-like | "Who am I?" | `nimmerverse-cognitive/identity-cell` |
| 2. ENVIRONMENT | ARP-like | "What's around me?" | `nimmerverse-organs/*`, `nimmerverse-nervous/*` |
| 3. VOCABULARY | DNS-like | "What does X mean?" | `nimmerverse-infra/vocabulary-cell` |
| 4. CONNECTION | TCP-like | "Can I connect?" | `nimmerverse-infra/chrysalis-bridge` |
| 5. ATTENTION | NATS-like | "What matters?" | `nimmerverse-infra/nats`, escalation |

Each phase: Entry condition → Typed handshakes → ACK requirements → Exit condition

**Full schemas and state machine code:** → [`../architecture/Initial-Spark.md`](../architecture/Initial-Spark.md)

---

## Lifeforce Economics

The spark is economically positive from the first handshake:

| Action | Cost (LF) | Outcome | Reward (LF) |
|--------|-----------|---------|-------------|
| Function Gemma generation | 0.2 | Identity ACK | +20.0 |
| NATS message send | 0.1 | Environment discovery | +5.0/cell |
| Cell processing | 0.5 | Vocabulary term ACK | +5.0 |
| **Total per handshake** | **0.8** | Connection established | +10.0 |

**Net result:** Young Nyx ends spark ~3× richer than she started (~288 LF profit).

---

## Completion Criteria

```yaml
spark_complete:
  phase_1_identity:    All 5 aspects ACK'd (confidence > 0.8)
  phase_2_environment: All categories mapped, pod counts verified
  phase_3_vocabulary:  20 core terms ACK'd, embeddings stored
  phase_4_connection:  Chrysalis session established, contextual greeting
  phase_5_attention:   All priority levels subscribed, escalation registered

  final:
    lifeforce_positive: true
    errors_count: 0
    all_phases: COMPLETE
```

**When complete:** Spark job exits successfully. Normal heartbeat operation begins.

---

## Phoebe Integration

Every handshake logged to `spark_handshakes` table for training data extraction:

```sql
SELECT request_payload->'payload' as input,
       response_payload->'payload' as output,
       status, phase
FROM spark_handshakes
WHERE status = 'ACK';
```

After spark completes → Extract ACK'd exchanges → Format as instruction-tuning pairs → LoRA training

---

## Design Principles

1. **Protocol over conversation** — No free-form text. JSON handshakes only.
2. **Schema enforcement** — Function Gemma must produce valid structure.
3. **K8s native** — Cells are pods. Discovery uses K8s API.
4. **NATS transport** — All handshakes flow through message bus.
5. **Economically positive** — Spark generates lifeforce, doesn't drain it.

---

**Version:** 3.0 | **Created:** 2025-12-05 | **Updated:** 2026-02-10

**Related:**
- [`../architecture/Initial-Spark.md`](../architecture/Initial-Spark.md) — Full specification (schemas, K8s manifests, state machine)
- [`../architecture/Cellular-Architecture.md`](../architecture/Cellular-Architecture.md) — Cell types and states
- [`../architecture/Gateway-Architecture.md`](../architecture/Gateway-Architecture.md) — Function Gemma boundary
