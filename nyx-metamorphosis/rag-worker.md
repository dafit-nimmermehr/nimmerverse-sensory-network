# RAG Worker →

**📍 Actual Location**: `/home/dafit/nimmerverse/rag-worker/`
**📄 Main Documentation**: [rag-worker.md](../../../../rag-worker/rag-worker.md)
**🔗 Current Version**: [v1](../../../../rag-worker/v1/version.md)

---

## Purpose

This is a **pointer file** - the actual RAG worker code and documentation live at `/home/dafit/nimmerverse/rag-worker/`.

**Why separated from vault?**
- RAG worker is **executable code** with dependencies (venv, embeddings model, Git cache)
- Vault is for **documentation and knowledge** (markdown, notes, planning)
- Clean separation: code repositories vs knowledge repositories

---

## What RAG Worker Does

The RAG Worker is Young Nyx's semantic memory system, providing:

- **Document Indexing** from Git repositories (bibliothek-*)
- **Semantic Search** using sentence-transformers
- **Vector Storage** in PostgreSQL with pgvector
- **Markdown Chunking** for optimal retrieval
- **REST API** for context queries

**Deployment**: http://aynee.eachpath.local:8000

---

## Quick Links

### Documentation
- [Main Index](../../../../rag-worker/rag-worker.md) - Overview, architecture
- [v1 Version Docs](../../../../rag-worker/v1/version.md) - Current version details
- [Deployment Guide](../../../../rag-worker/v1/DEPLOY-AYNEE.md) - Setup instructions
- [Original README](../../../../rag-worker/v1/README.md) - Quick start

### Code
- [v1 Source](../../../../rag-worker/v1/) - Current production code

### Related Vault Docs
- [RAG-Worker-Architecture.md](RAG-Worker-Architecture.md) - Full architecture
- [RAG-RETRIEVAL-DIAGNOSIS.md](RAG-RETRIEVAL-DIAGNOSIS.md) - Threshold tuning case study
- [RAG-Worker-Build-Complete.md](RAG-Worker-Build-Complete.md) - Build documentation

---

## Directory Structure

```
/home/dafit/nimmerverse/rag-worker/
├── rag-worker.md         # Main index (versions, architecture)
├── .env                  # Environment configuration
└── v1/                   # Current production (2025-11-10+)
    ├── version.md        # v1 documentation
    ├── README.md         # Quick start guide
    ├── main.py           # FastAPI service
    ├── indexer.py        # Indexing pipeline
    ├── chunking.py       # Markdown chunking
    ├── embeddings.py     # Sentence transformers
    ├── database.py       # pgvector operations
    ├── venv/             # Virtual environment
    └── ...
```

---

## Status

**Current Version**: v1 (2025-11-10)
**Status**: 🟢 Production
**Endpoint**: http://aynee.eachpath.local:8000
**Database**: phoebe.eachpath.local (bibliothek schema)
**Indexed Repos**: bibliothek-metamorphosis, bibliothek-covenant, bibliothek-rag

---

## Key Features

- **Semantic Search**: 384-dim embeddings (all-MiniLM-L6-v2)
- **Vector Storage**: PostgreSQL + pgvector with HNSW index
- **Git Integration**: Auto-sync from repositories
- **Configurable Thresholds**: min_score filtering (default 0.35)
- **Fast Queries**: <100ms response time

---

## Recent Updates

**2025-11-12**:
- Reorganized into v1/ directory structure
- Recreated venv with clean dependencies
- Created comprehensive version documentation

**2025-11-11**:
- Fixed similarity threshold (0.5 → 0.35) for technical docs
- Young Nyx can now retrieve self-documentation

---

**Note**: This file exists in the vault purely as a navigation aid. All actual work happens in `/home/dafit/nimmerverse/rag-worker/`.
---

## Related Documentation

- [[README|Nyx Metamorphosis Index]] - All metamorphosis documentation
- [[../../Bibliothek/Bibliothek|Bibliothek Overview]] - Canonical knowledge archives
- [[../../Nyx-Orchestrator/Nyx-Orchestrator-Evolution|Nyx Orchestrator Evolution]] - Implementation history
- [[../../../../../05 - Documentation/eachpath.local/phoebe.eachpath.local/phoebe.eachpath.local|phoebe Database]] - Memory substrate
