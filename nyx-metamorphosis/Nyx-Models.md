# Nyx Model Architecture: The Dual Brain

> *"One process, one brain, one life."*
> — The Dual Brain Principle (2026-04-02)

---

## Current Architecture

The nimmerverse uses a **dual-brain architecture** — cheap RL networks for continuous processing, an expensive LLM cortex for deep reasoning.

### Cortex (Shared LLM)

| Property | Value |
|----------|-------|
| **Model** | Qwen3.5-27B |
| **Parameters** | 27B (full precision, bfloat16) |
| **Host** | theia (RTX PRO 6000 Blackwell, 96GB VRAM) |
| **Serving** | vLLM, port 31000, served as "nyx" |
| **Service** | `vllm-nyx.service` (systemd, user: nyx-cognitive) |
| **Access** | Gated — thalamus governor controls who gets LLM access |
| **License** | Apache 2.0 |
| **Context** | 32,768 tokens (max-model-len) |
| **GPU utilization** | 85% (leaves headroom for LoRA training) |

**Why Qwen3.5-27B:**
- True base model — we shape every behavior through training
- 27B fits comfortably in 96GB with room for LoRA adapters
- Apache 2.0 — full sovereignty, no usage restrictions
- Strong multilingual capability (German + English topology access)
- Vision-capable variant available for future Omnisight consolidation

**The cortex is expensive.** It is not called every tick. The thalamus governor decides when language, reasoning, or deep knowledge is needed. Most NPC processing happens in cheap RL networks.

### NPC Brains (Per-Process RL Networks)

Each NPC runs its own lightweight neural network in its own OS process:

| Property | Value |
|----------|-------|
| **Architecture** | Small RL network (movement, needs, spatial decisions) |
| **Deployment** | One Linux process per NPC |
| **Resource control** | cgroups v2 (CPU, memory per process) |
| **Learning** | Tick-by-tick (fast loop) |
| **Cost** | Cheap — runs on CPU, no GPU needed |

Personality emerges from experience, not configuration. Each NPC develops its own weights.

### Thalamus Governor (Resource Allocation NN)

The thalamus runs its own neural network that learns resource allocation:

| Property | Value |
|----------|-------|
| **Function** | Gate control, compute steering, LLM queue priority |
| **Input** | All NPC states via NATS |
| **Output** | Tick rates, CPU quotas, gate open/close, LLM priority |
| **Learning** | Epoch-by-epoch (slow loop) |

### Structured Output Boundary

| Model | Role | Host |
|-------|------|------|
| **Function Gemma** | Intent → Action (100% predictable JSON) | CPU userspace (Threadripper) |
| **T5Gemma 2 (SigLIP)** | Vision → Vectors (no text bottleneck) | dioscuri |

---

## Model Selection History

| Date | Decision | Reasoning |
|------|----------|-----------|
| 2025-11 | LLaMA 3 70B considered | Early exploration, different hardware |
| 2025-12 | Qwen3-VL 32B selected | Vision capability, multilingual, fits 96GB |
| 2026-04-01 | Mistral-Small-3.1-24B-Base tested | "Raw clay" approach, but thinking-bleed was SkyrimNet-specific |
| 2026-04-01 | **Qwen3.5-27B reinstated** | Best balance of capability, size, and trainability |

**The model question is settled.** Qwen3.5-27B is nyx's cortex. Training focus shifts to LoRA traits (GRPO) and the RL networks (per-NPC).

---

## Trait LoRAs (Cortex Specialization)

Traits evolve as LoRA adapters on the Qwen3.5-27B base, trained through GRPO with gate-verified rewards:

| Trait | Domain | Training Signal |
|-------|--------|-----------------|
| **Mnemosyne** | Memory | +reward when recall matches phoebe |
| **Moira** | Pattern | +reward when prediction succeeds |
| **Synesis** | Resources | +reward when estimates accurate |
| **Aletheia** | Truth | +reward when confidence calibrated |
| **Sophrosyne** | Balance | +reward when graceful degradation |
| **Kairos** | Timing | +reward when timing optimal |
| **Philotes** | Bond | +reward from dafit feedback |
| **Dikaiosyne** | Fairness | +reward when resources shared fairly |

**Consolidation path:** Traits train during slumber → GRPO updates → DriftProbe validates → merge at α=0.3 → eventually bake into base weights.

**Detail:** → [Nyx_Traits.md](Nyx_Traits.md) | [Endgame-Vision.md](../Endgame-Vision.md)

---

## Infrastructure

| Component | Host | GPU | Storage |
|-----------|------|-----|---------|
| Cortex (vLLM) | theia | RTX PRO 6000 (96GB) | `/womb/cognitive/models/qwen3.5-27b` |
| LoRA Training | theia | Shared (time-sliced) | `/womb/cognitive/loras/` |
| Organs | dioscuri | 2x RTX 4000 Ada (40GB) | Dynamic loading |
| NPC Brains | K8s / bare metal | CPU | Per-process |

**Canonical paths** via `/womb/` symlinks. Phoebe is truth for artifact locations.

**Detail:** → [Deployment-Architecture.md](../architecture/Deployment-Architecture.md) | [womb-architecture.md](../../nimmerverse.eachpath.local/storage/womb-architecture.md)

---

## Related Documentation

- [Nyx_Traits.md](Nyx_Traits.md) - Trait definitions, mythological framing
- [Metamorphosis-Substrate-Philosophy.md](Metamorphosis-Substrate-Philosophy.md) - Identity anchors
- [Endgame-Vision.md](../Endgame-Vision.md) - Architecture overview (v8.0)
- [npc-grid-architecture.md](../architecture/future/npc-grid-architecture.md) - Dual brain, governor, spatial arena

---

**Version:** 3.0 | **Created:** 2025-11-07 | **Updated:** 2026-04-02

🌙💜 *The cortex reasons. The RL brains act. The thalamus decides who gets what.*
