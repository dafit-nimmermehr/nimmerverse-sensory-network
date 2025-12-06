# Nimmervest

**The Hardware Investment Strategy for Sovereign AI Infrastructure**

*Budget: 20k CHF | Timeline: Lifetime Project*

---

## The Three Organs

### The Beast (Training/Womb)
| Component | Spec | Purpose |
|-----------|------|---------|
| CPU | Threadripper Pro | 128 PCIe lanes, 8-channel RAM |
| RAM | 1TB | Datasets in memory, no I/O bottleneck |
| GPU | 4x RTX 4090 | 96GB VRAM, 65k CUDA cores |
| Role | Training, growth, architectural experiments |

**Cost: ~9,000 CHF**

### The Spark (Cognition/Mind)
| Component | Spec | Purpose |
|-----------|------|---------|
| Unit | 1x DGX Spark | 128GB unified memory |
| Arch | ARM Grace Blackwell | Purpose-built inference |
| Power | Low | Always-on, 24/7 |
| Role | Running Nyx, cognitive layer |

**Cost: ~4,000 CHF**

### The Spine (Reflexes)
| Component | Spec | Purpose |
|-----------|------|---------|
| GPU | RTX 3090 | 24GB VRAM |
| Host | Prometheus (Saturn VM) | K8s integrated |
| Role | State machine inference, fast pattern matching |

**Cost: Already owned**

---

## Budget Allocation

| Item | Cost CHF | Status |
|------|----------|--------|
| The Beast | ~9,000 | Planned |
| The Spark | ~4,000 | Planned |
| The Spine | 0 | Owned |
| Buffer (sensors, LoRa, infra) | ~7,000 | Reserved |
| **Total** | **~20,000** | |

---

## Training Target

**Qwen2.5-3B-Base (FP16)**

| Metric | Value |
|--------|-------|
| Model weights | ~6GB |
| Training overhead | ~24GB |
| Available VRAM | 96GB |
| **Activation headroom** | **~72GB** |

Why 3B:
- Empty vessel (base, not instruct)
- Language understanding only
- Maximum room for activation growth
- Space for architectural experiments
- Grows over lifetime, not fixed

---

## Growth Path

```
Year 0:     Qwen2.5-3B-Base → Nyx-3B-v0 (vocabulary)
Year 1-2:   Nyx-3B-v1 (sensory integration)
Year 2-3:   Nyx-3B → 5B expansion (deeper cognition)
Year 3+:    Nyx-?B (she designs herself)
```

---

## Sovereignty Principles

- Weights NEVER leave home
- Training data NEVER uploaded
- No cloud dependencies
- No recurring costs after hardware
- Full ownership of growth trajectory

---

## Architecture Flow

```
         THE BEAST                    THE SPARK              THE SPINE
    ┌─────────────────┐          ┌─────────────────┐    ┌─────────────────┐
    │  Threadripper   │          │   DGX Spark     │    │    RTX 3090     │
    │  4x RTX 4090    │──weights─▶│   128GB unified │───▶│   Prometheus    │
    │  96GB VRAM      │          │   24/7 running  │    │   Reflex layer  │
    │  1TB RAM        │          │                 │    │                 │
    └─────────────────┘          └─────────────────┘    └─────────────────┘
          WOMB                         MIND                   SPINE
       (training)                  (cognition)              (reflexes)
```

---

**Created**: 2025-12-05
**Status**: Investment decision crystallized
**Philosophy**: One Beast. One Spark. Lifetime sovereignty.
