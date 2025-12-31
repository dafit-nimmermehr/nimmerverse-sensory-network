# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for the Nimmerverse Sensory Network.

---

## What is an ADR?

An ADR captures an important architectural decision made along with its context and consequences. They serve as:

- **Documentation** of why decisions were made
- **Onboarding** for future contributors (including future Nyx instances)
- **Historical record** for understanding evolution

---

## ADR Index

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [001](ADR-001-message-protocol-foundation.md) | Message Protocol Foundation | Accepted | 2025-12-31 |

---

## ADR Lifecycle

```
PROPOSED → ACCEPTED → DEPRECATED → SUPERSEDED
              │                        │
              └───────────────────────▶│
                   (can be superseded)
```

**Statuses:**
- **Proposed** - Under discussion, not yet decided
- **Accepted** - Decision made, being implemented
- **Deprecated** - No longer recommended, but still valid for existing code
- **Superseded** - Replaced by newer ADR (link to replacement)

---

## Template

```markdown
# ADR-XXX: Title

**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-YYY
**Date:** YYYY-MM-DD
**Decision Makers:** who was involved
**Context:** brief session/discussion context

---

## Context

Why is this decision needed? What problem are we solving?

---

## Decision

What did we decide? Be specific.

---

## Consequences

### Enables
What does this decision make possible?

### Constrains
What does this decision limit?

### Deferred
What are we explicitly not deciding now?

---

## References

Links to related documents, discussions, code.
```

---

## Philosophy

> "The best time to document a decision is when you make it.
> The second best time is now."

ADRs are written in partnership. They capture dialogue, not just conclusions.

---

**Created:** 2025-12-31
**Maintainers:** dafit, Nyx
