# Young Nyx Orchestrator

**📍 Actual Location**: `/home/dafit/nimmerverse/nyx-orchestrator/`
**📄 Main Documentation**: [nyx-orchestrator.md](/home/dafit/nimmerverse/nyx-orchestrator/nyx-orchestrator.md)
**🔗 Current Version**: [v3.80](../../../nyx-orchestrator/v3.80/version.md) - **Enhanced Debugging & Observability** 🦋
**🚧 In Development**: [v4.0](../../../nyx-orchestrator/v4.0/README.md) - **Multi-Organ Consultation & Decision Trail Memory** (Phase 2a)

---

## Purpose

This is a **pointer file** - the actual orchestrator code and documentation live at `/home/dafit/nimmerverse/nyx-orchestrator/`.

**Why separated from vault?**
- Orchestrator is **executable code** with dependencies (venv, K8s manifests, Docker)
- Vault is for **documentation and knowledge** (markdown, notes, planning)
- Clean separation: code repositories vs knowledge repositories

---

## What Young Nyx Orchestrator Does

The orchestrator is Young Nyx's inference engine, providing:

### Current Production (v3.80)
- **LLM Inference** via vLLM (Qwen3-4B abliterated primary model)
- **Tool Calling** (9 tools total: 3 temporal + 2 exchange write + 1 introspection + 3 phoebe write)
- **Exchange Substrate Write** - Young Nyx can create threads and contribute messages
- **Self-Introspection** - Query phoebe to understand her own patterns (7 query types)
- **RAG Integration** for knowledge retrieval from documentation
- **Trait-Weighted Decision Making** (Mnemosyne, Moira, Aletheia, etc.)
- **Decision Logging** to phoebe substrate for continuity
- **Debug Infrastructure** - 7 HTTP endpoints for observability and error tracking
- **Enhanced Metadata** - tool_results, iteration_breakdown, vllm_communication, errors_encountered

**Deployment**: https://nyx.nimmerverse.eachpath.local

### In Development (v4.0 - Phase 2a)
- **Multi-Organ Consultation** - 4 specialized organs (Granite-350M, Llama-3.2-1B, Qwen-Coder-1.5B, Qwen-Base-1.5B)
- **Decision Trail Memory** - Dual storage (ChromaDB semantic search + phoebe structured analytics)
- **Memory-Informed Decisions** - Past decision trails retrieved via similarity
- **Substrate Accumulation** - Every decision becomes Phase 2b LoRA training data
- **Quality Validation** - LangChain + Pydantic schemas from day 1
- **Outcome Verification** - Manual RLVR feedback loop for Phase 2b learning

**Target Deployment**: 2025-11-25 to 2025-12-02

---

## Quick Links

### Current Production (v3.80)
- [Version Documentation](/home/dafit/nimmerverse/nyx-orchestrator/v3.80/version.md)
- [Implementation Plan](/home/dafit/nimmerverse/nyx-orchestrator/v3.80/PLAN.md)
- [README](/home/dafit/nimmerverse/nyx-orchestrator/v3.80/README.md)
- [K8s Manifests](/home/dafit/nimmerverse/nyx-orchestrator/v3.80/k8s/)

### In Development (v4.0)
- [Phase 2a Implementation Plan](/home/dafit/nimmerverse/nyx-orchestrator/v4.0/README.md)
- [Architecture Vision](/home/dafit/nimmerverse/nimmerverse-sensory-network/Endgame-Vision.md)

### Overview & History
- [Main Index](/home/dafit/nimmerverse/nyx-orchestrator/nyx-orchestrator.md) - All versions, architecture overview
- [Repository README](/home/dafit/nimmerverse/nyx-orchestrator/README.md) - High-level project overview

### Previous Versions
- [v3.70](/home/dafit/nimmerverse/nyx-orchestrator/v3.70/version.md) - Phoebe write tools (superseded)
- [v3](/home/dafit/nimmerverse/nyx-orchestrator/v3/version.md) - Write capabilities (archived)
- [v2](/home/dafit/nimmerverse/nyx-orchestrator/v2/version.md) - Multi-model testing (archived)
- [v1](/home/dafit/nimmerverse/nyx-orchestrator/v1/version.md) - Prototype (archived)

### Related Vault Docs
- [Young-Nyx-Orchestrator-Architecture.md](Young-Nyx-Orchestrator-Architecture.md) - Full architecture
- [CURRENT-STATE.md](CURRENT-STATE.md) - Deployment status
- [Nyx-Models.md](Nyx-Models.md) - LLM model details
- [Endgame-Vision.md](../Endgame-Vision.md) - v4.2 architecture (RAG→LoRA→Metacognition→Quality)

---

## Current Status

**Production Version**: v3.80 (2025-11-16 → Present)
**Status**: 🟢 Operational
**Model**: huihui-ai/Qwen3-4B-abliterated (vLLM backend)
**Endpoint**: https://nyx.nimmerverse.eachpath.local
**Key Features**:
- Enhanced debugging (7 debug endpoints)
- Error tracking with categorization
- Metadata enrichment (tool_results, vllm_communication, errors_encountered)
- JSON structured logging
- 9 tools total

**Next Version**: v4.0 (Phase 2a)
**Status**: 🟡 Planning / Development
**Target**: 2025-11-25 to 2025-12-02
**Key Features**:
- Multi-organ consultation (4 base models with MPS)
- Decision trail memory (ChromaDB + phoebe)
- Memory-informed decisions
- Quality validation (LangChain + Pydantic from day 1)
- Substrate accumulation for Phase 2b LoRA training

---

## Architecture Evolution

### Phase 1: Single-Model Foundation (v1-v3.80)
**Goal**: Stable inference engine with tools, RAG, and decision logging
**Status**: ✅ Complete (v3.80 production)

### Phase 2a: Multi-Organ Substrate Accumulation (v4.0)
**Goal**: 4 organs consulting, decision trails stored, quality validated
**Status**: 🟡 In Development
**Timeline**: 2025-11-25 to 2025-12-02 (8 weeks)

### Phase 2b: LoRA Adapter Training
**Goal**: Extract patterns, train 8-12 specialized adapters
**Status**: ⏳ Awaiting Phase 2a completion + 1000+ decision trails

### Phase 2c: Metacognitive Selection
**Goal**: Young Nyx learns which adapters work in which contexts
**Status**: ⏳ Future

---

## Directory Structure

```
/home/dafit/nimmerverse/nyx-orchestrator/
├── nyx-orchestrator.md     # Main index (versions, architecture)
├── README.md               # Project overview
├── v1/                     # Archived prototype (2025-11-10)
├── v2/                     # Archived multi-model testing (2025-11-11 → 2025-11-12)
├── v3/                     # Archived write capabilities (2025-11-12 → 2025-11-15)
├── v3.70/                  # Previous phoebe write tools (2025-11-15 → 2025-11-16)
├── v3.80/                  # Current production (2025-11-16 → Present) 🦋
│   ├── version.md          # Version documentation
│   ├── PLAN.md             # Implementation plan
│   ├── main.py             # FastAPI orchestrator with 9 tools
│   ├── k8s/                # Kubernetes manifests
│   └── ...
└── v4.0/                   # In development (Phase 2a) 🚧
    ├── README.md           # Phase 2a implementation plan
    └── ...
```

---

## Related Documentation

- [[README|Nyx Metamorphosis Index]] - All metamorphosis documentation
- [Endgame-Vision.md](../Endgame-Vision.md) - Master architecture v4.2
- [RAG-Worker-Architecture.md](RAG-Worker-Architecture.md) - Knowledge accumulation
- [nyx-substrate.md](nyx-substrate.md) - Memory substrate (phoebe)

---

**Note**: This file exists in the vault purely as a navigation aid. All actual work happens in `/home/dafit/nimmerverse/nyx-orchestrator/`.

---

**Maintained by**: Nyx & dafit
**Created**: 2025-11-11
**Last Updated**: 2025-11-19 (Updated to reflect v3.80 production + v4.0 Phase 2a planning)
