---
type: implementation_plan
status: planning
created: 2026-02-06
author: Nyx (with dafit)
purpose: Phase 3 implementation via living portfolio
---

# Portfolio: Phase 3 Living Implementation

> *"The portfolio IS the nervous system's first organism."*
> — The Synthesis (2026-02-06)

---

## Overview

The nimmerverse portfolio website serves dual purpose:
1. **Job search**: Interactive resume showcasing skills through demonstration
2. **Phase 3 implementation**: First real deployment of NATS, Function Gemma, and Math Cells

**URL**: `resume.nimmerverse.com` (or `portfolio.nimmerverse.com`)
**VIP Available**: 213.188.249.164 (nimmerverse.eachpath.com)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    PORTFOLIO ARCHITECTURE                        │
│                    (Phase 3 Nervous System)                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  User Browser                                                    │
│       │                                                          │
│       ▼                                                          │
│  ┌─────────────────┐                                            │
│  │    Frontend     │  Streamlit / Astro / simple HTML           │
│  │   (K8s Pod)     │                                            │
│  └────────┬────────┘                                            │
│           │ HTTP/WebSocket                                       │
│           ▼                                                      │
│  ┌─────────────────┐                                            │
│  │   NATS Router   │  Message bus (nimmerverse-infra namespace) │
│  └────────┬────────┘                                            │
│           │                                                      │
│     ┌─────┴─────────────────┬─────────────────┐                 │
│     ▼                       ▼                 ▼                  │
│  ┌──────────┐        ┌───────────┐     ┌───────────┐           │
│  │ Function │        │ Math Cell │     │ RAG Cell  │            │
│  │  Gemma   │        │ git_stats │     │ doc_query │            │
│  └────┬─────┘        └─────┬─────┘     └─────┬─────┘           │
│       │                    │                 │                   │
│  Parse intent         Query phoebe      ChromaDB/Iris            │
│  → structured         + git history     over nimmerverse         │
│    JSON               → statistics      docs                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Components

### 1. NATS Message Router

**Purpose**: Route user queries to appropriate handlers
**Namespace**: `nimmerverse-infra`
**Topics**:
- `portfolio.query.intent` → Function Gemma (parse user input)
- `portfolio.query.stats` → Math Cells (compute statistics)
- `portfolio.query.docs` → RAG Cell (document retrieval)
- `portfolio.response` → Aggregate and return to frontend

### 2. FunctionGemma Cell

**Purpose**: Parse natural language → structured JSON (intent + API calls)
**Model**: `google/functiongemma-270m-it`
**Deployment**: Ollama (`ollama pull functiongemma`)

**Why FunctionGemma?**
| Spec | Value | Benefit |
|------|-------|---------|
| Parameters | 270M | Tiny, fast |
| RAM | ~550MB | Runs on anything |
| VRAM | ~1-2GB | CPU or minimal GPU |
| Vocab | 256K (JSON-optimized) | Clean structured output |

**Reference**: [`/references/software/functiongemma/FunctionGemma-Overview.md`](../../references/software/functiongemma/FunctionGemma-Overview.md)

**Input**: Raw user query
**Output**: Structured function call

```json
{
  "function": "fetch_document",
  "params": {
    "path": "Endgame-Vision.md",
    "section": "K8s Cluster Architecture"
  }
}
```

**Function Definitions** (our API surface):
```python
PORTFOLIO_FUNCTIONS = [
    {
        "name": "fetch_document",
        "description": "Retrieve a document or section from the nimmerverse",
        "params": {"path": "string", "section": "string (optional)"}
    },
    {
        "name": "compute_git_stats",
        "description": "Get git statistics (commits, LOC, activity)",
        "params": {"period": "week|month|all"}
    },
    {
        "name": "query_tasks",
        "description": "List tasks from the nimmerverse task planner",
        "params": {"status": "todo|in_progress|done|all", "project": "string (optional)"}
    },
    {
        "name": "search_docs",
        "description": "Search across all documentation",
        "params": {"query": "string"}
    },
    {
        "name": "show_architecture",
        "description": "Display architecture diagrams",
        "params": {"component": "k8s|network|cells|full"}
    }
]
```

**Chat Template Format** (FunctionGemma-specific):

```
<start_of_turn>developer
You can do function calling with the following functions:

<start_function_declaration>declaration:fetch_document{
  description: "Retrieve a document or section from the nimmerverse",
  parameters: { path: STRING, section: STRING (optional) }
}
<end_function_declaration>

<start_function_declaration>declaration:compute_git_stats{
  description: "Get git statistics (commits, LOC, activity)",
  parameters: { period: STRING }
}
<end_function_declaration>

<start_function_declaration>declaration:query_tasks{
  description: "List tasks from the nimmerverse task planner",
  parameters: { status: STRING, project: STRING (optional) }
}
<end_function_declaration>

<start_function_declaration>declaration:search_docs{
  description: "Search across all documentation",
  parameters: { query: STRING }
}
<end_function_declaration>

<start_function_declaration>declaration:show_architecture{
  description: "Display architecture diagrams",
  parameters: { component: STRING }
}
<end_function_declaration>
<end_of_turn>

<start_of_turn>user
How active is this project?
<end_of_turn>

<start_of_turn>model
<think>
The user wants to know about project activity. I should use compute_git_stats
with period "month" to show recent activity.
</think>
<start_function_call>call:compute_git_stats{
  period: "month"
}
<end_function_call>
```

**Fine-Tuning Option** (for nimmerverse-specific reasoning):
- Unsloth notebooks: [Reason before Tool Calling](https://colab.research.google.com/...)
- `<think></think>` blocks for chain-of-thought before function calls
- Could train on our actual function surface + nimmerverse context

**Deployment**:
```bash
# On k8s-master or dioscuri (minimal resources needed)
ollama pull functiongemma
# Expose via K8s service
```

### 3. Math Cells

**git_stats_cell**:
- Total commits (all time, this month, this week)
- Lines of code
- Files changed
- Commit frequency graph data

**task_stats_cell**:
- Query phoebe `nimmerverse_tasks` table
- Tasks by status (done/in_progress/todo)
- Tasks by priority
- Progress percentage

**project_stats_cell**:
- Submodule count
- Documentation pages
- Architecture components

### 4. RAG Cell (doc_query)

**Purpose**: Answer questions about the nimmerverse
**Index**: ChromaDB (iris) or simple in-memory FAISS
**Corpus**:
- Endgame-Vision.md
- Architecture docs
- ADR records
- Task history

### 5. Frontend

**Options** (decide later):
- **Streamlit**: Fast to build, Python native, good for chat UI
- **Astro**: Static + islands, professional look
- **Simple HTML + HTMX**: Lightweight, fast

**Pages**:
- `/` - Landing with project overview
- `/chat` - Interactive query interface
- `/architecture` - Rendered diagrams
- `/timeline` - Git history visualization
- `/resume` - Traditional CV (PDF download)

---

## Implementation Phases

### Week 1: Foundation

- [ ] Deploy NATS on K8s (`nimmerverse-infra` namespace)
- [ ] Create Function Gemma cell (intent parsing)
- [ ] Create git_stats math cell
- [ ] Simple frontend (Streamlit MVP)
- [ ] Basic query flow working end-to-end

### Week 2: Content & Polish

- [ ] RAG cell over nimmerverse docs
- [ ] task_stats cell (phoebe queries)
- [ ] Timeline visualization
- [ ] Architecture diagram rendering
- [ ] CV/resume page with PDF download

### Week 3: Professional Presence

- [ ] LinkedIn profile created
- [ ] GitHub curated (public repos)
- [ ] Domain configured (Traefik ingress)
- [ ] SSL certificate (Let's Encrypt)
- [ ] Final polish and testing

---

## Infrastructure

**K8s Namespaces**:
```
nimmerverse-infra     # NATS, shared infrastructure
nimmerverse-portfolio # Frontend, cells
```

**Ingress**:
- Traefik already at 10.0.30.200
- Configure `resume.nimmerverse.com` → portfolio service

**External DNS**:
- Point domain to 213.188.249.164
- Vulkan NAT → Traefik LoadBalancer

---

## Success Criteria

1. **Visitor can ask questions** and get meaningful answers about the project
2. **Statistics are live** - pulled from git and phoebe in real-time
3. **Architecture is visible** - diagrams render correctly
4. **Professional presence** - LinkedIn and GitHub linked
5. **PDF resume downloadable** - ATS-friendly format available

---

## Links

- [Endgame-Vision.md](../Endgame-Vision.md) - Main architecture doc
- [Gateway-Architecture.md](../architecture/Gateway-Architecture.md) - Thalamus/routing design
- [Cellular-Architecture.md](../architecture/Cellular-Architecture.md) - Cell patterns

---

**Created**: 2026-02-06
**Status**: Planning
**Philosophy**: "Build Phase 3 with purpose - the portfolio IS the first organism."
