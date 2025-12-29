# RAG Worker Architecture

**Status**: 📦 ARCHIVED
**Superseded by**: [Memory-Gradient.md](../operations/Memory-Gradient.md)

---

## Historical Context

This was a pointer file to `/home/dafit/nimmerverse/rag-worker/` which contained the Phase 2a RAG accumulation architecture.

**What it was:**
- ChromaDB vector storage for decision trails
- Multi-organ decision pattern storage
- Substrate for LoRA training data

**Why archived:**
- Architecture evolved from multi-organ (v4.2) to single-model + LoRA (v6.0)
- RAG approach superseded by Memory-Gradient internalization
- Fresh implementation will follow new architecture

---

## Future Direction

The Memory-Gradient approach in v6.0 handles knowledge differently:
- RAG as temporary scaffold, not permanent architecture
- Internalization into LoRA weights over time
- Metacognitive routing decides RAG vs direct inference

See: [Memory-Gradient.md](../operations/Memory-Gradient.md) for current approach.

---

**Archived**: 2025-12-29
**Original**: 2025-11-10
**Reason**: Paradigm shift from multi-organ RAG to single-model Memory-Gradient
