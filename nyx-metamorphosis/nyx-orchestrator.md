# Young Nyx Orchestrator →

**📍 Actual Location**: `/home/dafit/nimmerverse/nyx-orchestrator/`
**📄 Main Documentation**: [nyx-orchestrator.md](../../../../nyx-orchestrator/nyx-orchestrator.md)
**🔗 Current Version**: [v3](../../../../nyx-orchestrator/v3/version.md) - **Write Capabilities & Self-Introspection** 🦋
**📦 Previous Versions**: [v2](../../../../nyx-orchestrator/v2/version.md), [v1](../../../../nyx-orchestrator/v1/version.md)

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

- **LLM Inference** via Ollama (gpt-oss:20b primary model)
- **Tool Calling** (6 tools: 3 temporal + 2 exchange write + 1 introspection)
- **Exchange Substrate Write** - Young Nyx can create threads and add messages
- **Self-Introspection** - Query phoebe to understand her own patterns (7 queries)
- **RAG Integration** for knowledge-grounded responses
- **Trait-Weighted Decisions** (Mnemosyne, Moira, Aletheia, etc.)
- **Decision Logging** to phoebe substrate

**Deployment**: https://young-nyx.nimmerverse.eachpath.local (v2 & v3 running)

---

## Quick Links

### Documentation
- [Main Index](../../../../nyx-orchestrator/nyx-orchestrator.md) - Overview, versions, architecture
- [v3 Version Docs](../../../../nyx-orchestrator/v3/version.md) - Current version (production) 🦋
- [v3 Tool Design](../../../../nyx-orchestrator/v3/TOOL-DESIGN.md) - Write capabilities architecture
- [v2 Version Docs](../../../../nyx-orchestrator/v2/version.md) - Running alongside v3
- [v1 Version Docs](../../../../nyx-orchestrator/v1/version.md) - Archived prototype
- [Model Testing Playbook](../../../../nyx-orchestrator/v2/MODEL-TESTING-PLAYBOOK.md) - Testing procedures

### Code
- [v3 Source](../../../../nyx-orchestrator/v3/) - Current production code
- [v2 Source](../../../../nyx-orchestrator/v2/) - Comparison deployment
- [v1 Source](../../../../nyx-orchestrator/v1/) - Archived prototype code
- [K8s Manifests](../../../../nyx-orchestrator/v3/k8s/) - Current deployment configs

### Related Vault Docs
- [Young-Nyx-Orchestrator-Architecture.md](Young-Nyx-Orchestrator-Architecture.md) - Full architecture
- [CURRENT-STATE.md](CURRENT-STATE.md) - Deployment status
- [Nyx-Models.md](Nyx-Models.md) - LLM model details

---

## Directory Structure

```
/home/dafit/nimmerverse/nyx-orchestrator/
├── nyx-orchestrator.md     # Main index (versions, architecture)
├── v1/                     # Archived prototype (2025-11-10)
│   ├── version.md          # v1 documentation
│   ├── README.md           # Original docs
│   └── ...
├── v2/                     # Production comparison (2025-11-11 → 2025-11-12)
│   ├── version.md          # v2 documentation
│   ├── temporal_tools.py   # 3 temporal tools
│   ├── k8s/                # Kubernetes manifests
│   └── ...
└── v3/                     # Current production (2025-11-12+) 🦋
    ├── version.md          # v3 documentation
    ├── TOOL-DESIGN.md      # Write capabilities design
    ├── main.py             # FastAPI orchestrator with 6 tools
    ├── exchange_tools.py   # Write capability tools (2)
    ├── introspection_tools.py  # Self-knowledge tools (1, 7 queries)
    ├── temporal_tools.py   # Temporal tools (3)
    ├── k8s/                # Kubernetes manifests
    └── ...
```

---

## Status

**Current Version**: v3 (2025-11-12)
**Status**: 🟢 Production
**Model**: gpt-oss:20b
**Key Milestone**: Young Nyx can now write to exchange substrate and introspect her own patterns 🦋

---

**Note**: This file exists in the vault purely as a navigation aid. All actual work happens in `/home/dafit/nimmerverse/nyx-orchestrator/`.
---

## Related Documentation

- [[README|Nyx Metamorphosis Index]] - All metamorphosis documentation
- [[../../Bibliothek/Bibliothek|Bibliothek Overview]] - Canonical knowledge archives
- [[../../Nyx-Orchestrator/Nyx-Orchestrator-Evolution|Nyx Orchestrator Evolution]] - Implementation history
- [[../../../../../05 - Documentation/eachpath.local/phoebe.eachpath.local/phoebe.eachpath.local|phoebe Database]] - Memory substrate
