# Modular Nimmerverse Toolchain Architecture

**Planning Date**: 2025-12-07
**Status**: Design Phase
**Priority**: Variance Collection Pipeline + nyx-substrate Foundation

---

## 🎯 Vision

Build a modular, composable toolchain for the Nimmerverse research and training pipeline:

- **nyx-substrate**: Shared foundation (database clients, schemas, validators)
- **nyx-probing**: Research probes (already exists, extend for variance collection)
- **nyx-training**: LoRA training pipeline (future)
- **nyx-visualization**: Weight/topology visualization (future)
- **management-portal**: FastAPI backend for Godot UI (future)
- **Godot Command Center**: Unified metrics visualization (future)

**Key Principle**: All tools import nyx-substrate. Clean interfaces. Data flows through phoebe + iris.

---

## 📊 Current State Analysis

### ✅ What Exists

**nyx-probing** (`/home/dafit/nimmerverse/nyx-probing/`):
- Echo Probe, Surface Probe, Drift Probe, Multilingual Probe
- CLI interface (7 commands)
- NyxModel wrapper (Qwen2.5-7B loading, hidden state capture)
- ProbeResult dataclasses (to_dict() serialization)
- **Extractors module** (NEW 2025-12-13):
  - VocabExtractor: TF-IDF vocabulary extraction from markdown corpus
  - CoOccurrenceAnalyzer: PMI, Jaccard, Dice, anchor signatures
- **Gap**: No database persistence, only local JSON files

**nyx-substrate** (`/home/dafit/nimmerverse/nyx-substrate/`):
- Schema documentation (phoebe + iris) ✅
- **Gap**: No Python code, just markdown docs

**Database Infrastructure**:
- phoebe.eachpath.local (PostgreSQL 17.6): partnership/nimmerverse message tables exist
- iris.eachpath.local (ChromaDB): No collections created yet
- **Gap**: No Python client libraries, all manual psql commands

**Architecture Documentation**:
- Endgame-Vision.md: v5.1 Dialectic (LoRA stack design)
- CLAUDE.md: Partnership protocol (message-based continuity)
- Management-Portal.md: Godot + FastAPI design (not implemented)

### ❌ What's Missing

**Database Access**:
- No psycopg3 connection pooling
- No ChromaDB Python integration
- No ORM or query builders
- No variance_probe_runs table (designed but not created)

**Training Pipeline**:
- No PEFT/LoRA training code
- No DriftProbe checkpoint integration
- No training data curriculum loader

**Visualization**:
- No weight visualization tools (4K pixel space idea)
- No Godot command center implementation
- No Management Portal FastAPI backend

---

## 🏗️ Modular Architecture Design

### Repository Structure

```
nimmerverse/
├── nyx-substrate/              # SHARED FOUNDATION
│   ├── pyproject.toml          # Installable package
│   ├── src/nyx_substrate/
│   │   ├── database/           # Phoebe clients
│   │   │   ├── connection.py   # Connection pool
│   │   │   ├── messages.py     # Message protocol helpers
│   │   │   └── variance.py     # Variance probe DAO
│   │   ├── vector/             # Iris clients
│   │   │   ├── client.py       # ChromaDB wrapper
│   │   │   ├── decision_trails.py
│   │   │   ├── organ_responses.py
│   │   │   └── embeddings.py
│   │   ├── schemas/            # Pydantic models
│   │   │   ├── variance.py     # VarianceProbeRun
│   │   │   ├── decision.py     # DecisionTrail
│   │   │   └── traits.py       # 8 core traits
│   │   └── constants.py        # Shared constants
│   └── migrations/             # Alembic for schema
│
├── nyx-probing/                # RESEARCH PROBES (extend)
│   ├── nyx_probing/
│   │   ├── runners/            # NEW: Automated collectors
│   │   │   ├── variance_runner.py  # 1000x automation
│   │   │   └── baseline_collector.py
│   │   └── storage/            # EXTEND: Database integration
│   │       └── variance_dao.py # Uses nyx-substrate
│   └── pyproject.toml          # Add: depends on nyx-substrate
│
├── nyx-training/               # FUTURE: LoRA training
│   └── (planned - not in Phase 1)
│
├── nyx-visualization/          # FUTURE: Weight viz
│   └── (planned - not in Phase 1)
│
└── management-portal/          # FUTURE: FastAPI + Godot
    └── (designed - not in Phase 1)
```

### Dependency Graph

```
nyx-probing ────────┐
nyx-training ───────┼──> nyx-substrate ──> phoebe (PostgreSQL)
nyx-visualization ──┤                   └─> iris (ChromaDB)
management-portal ──┘
```

**Philosophy**: nyx-substrate is the single source of truth for database access. No tool talks to phoebe/iris directly.

---

## 🚀 Phase 1: Foundation + Variance Collection

### Goal
Build nyx-substrate package and extend nyx-probing to automate variance baseline collection (1000x runs → phoebe).

### Deliverables

#### 1. nyx-substrate Python Package

**File**: `/home/dafit/nimmerverse/nyx-substrate/pyproject.toml`
```toml
[project]
name = "nyx-substrate"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "psycopg[binary]>=3.1.0",
    "chromadb>=0.4.0",
    "pydantic>=2.5.0",
]
```

**New Files**:
- `src/nyx_substrate/database/connection.py`:
  - `PhoebeConnection` class: Connection pool manager
  - Context manager for transactions
  - Config from environment variables

- `src/nyx_substrate/database/messages.py`:
  - `write_partnership_message(message, message_type)` → INSERT
  - `read_partnership_messages(limit=5)` → SELECT
  - `write_nimmerverse_message(...)` (for Young Nyx future)
  - `read_nimmerverse_messages(...)` (for discovery protocol)

- `src/nyx_substrate/database/variance.py`:
  - `VarianceProbeDAO` class:
    - `create_table()` → CREATE TABLE variance_probe_runs
    - `insert_run(session_id, term, run_number, depth, rounds, ...)` → INSERT
    - `get_session_stats(session_id)` → Aggregation queries
    - `get_term_distribution(term)` → Variance analysis

- `src/nyx_substrate/schemas/variance.py`:
  - `VarianceProbeRun(BaseModel)`: Pydantic model matching phoebe schema
  - Validation: term not empty, depth 0-3, rounds > 0
  - `to_dict()` for serialization

**Database Migration**:
- Create `variance_probe_runs` table in phoebe using schema from `/home/dafit/nimmerverse/nyx-substrate/schema/phoebe/probing/variance_probe_runs.md`

#### 2. Extend nyx-probing

**File**: `/home/dafit/nimmerverse/nyx-probing/pyproject.toml`
- Add dependency: `nyx-substrate>=0.1.0`

**New Files**:
- `nyx_probing/runners/variance_runner.py`:
  - `VarianceRunner` class:
    - `__init__(model: NyxModel, dao: VarianceProbeDAO)`
    - `run_session(term: str, runs: int = 1000) -> UUID`:
      - Generate session_id
      - Loop 1000x: probe.probe(term)
      - Store each result via dao.insert_run()
      - Return session_id
    - `run_batch(terms: list[str], runs: int = 1000)`: Multiple terms

- `nyx_probing/cli/variance.py`:
  - New Click command group: `nyx-probe variance`
  - Subcommands:
    - `nyx-probe variance collect <TERM> --runs 1000`: Single term
    - `nyx-probe variance batch <FILE> --runs 1000`: From glossary
    - `nyx-probe variance stats <SESSION_ID>`: View session results
    - `nyx-probe variance analyze <TERM>`: Compare distributions

**Integration Points**:
```python
# In variance_runner.py
from nyx_substrate.database import PhoebeConnection, VarianceProbeDAO
from nyx_substrate.schemas import VarianceProbeRun

conn = PhoebeConnection()
dao = VarianceProbeDAO(conn)
runner = VarianceRunner(model=get_model(), dao=dao)
session_id = runner.run_session("Geworfenheit", runs=1000)
print(f"Stored 1000 runs: session {session_id}")
```

#### 3. Database Setup

**Actions**:
1. SSH to phoebe: `ssh phoebe.eachpath.local`
2. Create variance_probe_runs table:
   ```sql
   CREATE TABLE variance_probe_runs (
       id SERIAL PRIMARY KEY,
       session_id UUID NOT NULL,
       term TEXT NOT NULL,
       run_number INT NOT NULL,
       timestamp TIMESTAMPTZ DEFAULT NOW(),
       depth INT NOT NULL,
       rounds INT NOT NULL,
       echo_types TEXT[] NOT NULL,
       chain TEXT[] NOT NULL,
       model_name TEXT DEFAULT 'Qwen2.5-7B',
       temperature FLOAT,
       max_rounds INT,
       max_new_tokens INT
   );
   CREATE INDEX idx_variance_session ON variance_probe_runs(session_id);
   CREATE INDEX idx_variance_term ON variance_probe_runs(term);
   CREATE INDEX idx_variance_timestamp ON variance_probe_runs(timestamp DESC);
   ```

3. Test connection from aynee:
   ```bash
   cd /home/dafit/nimmerverse/nyx-substrate
   python3 -c "from nyx_substrate.database import PhoebeConnection; conn = PhoebeConnection(); print('✅ Connected to phoebe')"
   ```

---

## 📁 Critical Files

### To Create

**nyx-substrate**:
- `/home/dafit/nimmerverse/nyx-substrate/pyproject.toml`
- `/home/dafit/nimmerverse/nyx-substrate/src/nyx_substrate/__init__.py`
- `/home/dafit/nimmerverse/nyx-substrate/src/nyx_substrate/database/__init__.py`
- `/home/dafit/nimmerverse/nyx-substrate/src/nyx_substrate/database/connection.py`
- `/home/dafit/nimmerverse/nyx-substrate/src/nyx_substrate/database/messages.py`
- `/home/dafit/nimmerverse/nyx-substrate/src/nyx_substrate/database/variance.py`
- `/home/dafit/nimmerverse/nyx-substrate/src/nyx_substrate/schemas/__init__.py`
- `/home/dafit/nimmerverse/nyx-substrate/src/nyx_substrate/schemas/variance.py`
- `/home/dafit/nimmerverse/nyx-substrate/README.md`

**nyx-probing**:
- `/home/dafit/nimmerverse/nyx-probing/nyx_probing/runners/__init__.py`
- `/home/dafit/nimmerverse/nyx-probing/nyx_probing/runners/variance_runner.py`
- `/home/dafit/nimmerverse/nyx-probing/nyx_probing/cli/variance.py`

### To Modify

**nyx-probing**:
- `/home/dafit/nimmerverse/nyx-probing/pyproject.toml` (add nyx-substrate dependency)
- `/home/dafit/nimmerverse/nyx-probing/nyx_probing/cli/__init__.py` (register variance commands)

---

## 🧪 Testing Plan

### 1. nyx-substrate Unit Tests
```python
# Test connection
def test_phoebe_connection():
    conn = PhoebeConnection()
    assert conn.test_connection() == True

# Test message write
def test_write_message():
    from nyx_substrate.database import write_partnership_message
    write_partnership_message("Test session", "architecture_update")
    # Verify in phoebe

# Test variance DAO
def test_variance_insert():
    dao = VarianceProbeDAO(conn)
    session_id = uuid.uuid4()
    dao.insert_run(
        session_id=session_id,
        term="test",
        run_number=1,
        depth=2,
        rounds=3,
        echo_types=["EXPANDS", "CONFIRMS", "CIRCULAR"],
        chain=["test", "expanded", "confirmed"]
    )
    stats = dao.get_session_stats(session_id)
    assert stats["total_runs"] == 1
```

### 2. Variance Collection Integration Test
```bash
# On prometheus (THE SPINE)
cd /home/dafit/nimmerverse/nyx-probing
source venv/bin/activate

# Install nyx-substrate in development mode
pip install -e ../nyx-substrate

# Run small variance test (10 runs)
nyx-probe variance collect "Geworfenheit" --runs 10

# Check phoebe
PGGSSENCMODE=disable psql -h phoebe.eachpath.local -U nimmerverse-user -d nimmerverse -c "
SELECT session_id, term, COUNT(*) as runs, AVG(depth) as avg_depth
FROM variance_probe_runs
GROUP BY session_id, term
ORDER BY session_id DESC
LIMIT 5;
"

# Expected: 1 session, 10 runs, avg_depth ~2.0
```

### 3. Full 1000x Baseline Run
```bash
# Depth-3 champions (from nyx-probing Phase 1)
nyx-probe variance collect "Geworfenheit" --runs 1000  # thrownness
nyx-probe variance collect "Vernunft" --runs 1000      # reason
nyx-probe variance collect "Erkenntnis" --runs 1000    # knowledge
nyx-probe variance collect "Pflicht" --runs 1000       # duty
nyx-probe variance collect "Aufhebung" --runs 1000     # sublation
nyx-probe variance collect "Wille" --runs 1000         # will

# Analyze variance
nyx-probe variance analyze "Geworfenheit"
# Expected: Distribution histogram, depth variance, chain patterns
```

---

## 🌊 Data Flow

### Variance Collection Workflow

```
User: nyx-probe variance collect "Geworfenheit" --runs 1000
    ↓
VarianceRunner.run_session()
    ↓
Loop 1000x:
    EchoProbe.probe("Geworfenheit")
        ↓
    Returns EchoProbeResult
        ↓
    VarianceProbeDAO.insert_run()
        ↓
    INSERT INTO phoebe.variance_probe_runs
    ↓
Return session_id
    ↓
Display: "✅ 1000 runs complete. Session: <uuid>"
```

### Future Integration (Phase 2+)

```
Training Loop:
    ↓
DriftProbe.probe_lite()  [every 100 steps]
    ↓
Store metrics in phoebe.drift_checkpoints (new table)
    ↓
Management Portal API: GET /api/v1/metrics/training
    ↓
Godot Command Center displays live DriftProbe charts
```

---

## 🎯 Success Criteria

### Phase 1 Complete When:

1. ✅ nyx-substrate package installable via pip (`pip install -e .`)
2. ✅ PhoebeConnection works from aynee + prometheus
3. ✅ variance_probe_runs table created in phoebe
4. ✅ `nyx-probe variance collect` command runs successfully
5. ✅ 1000x run completes and stores in phoebe
6. ✅ `nyx-probe variance stats <SESSION_ID>` displays:
   - Total runs
   - Depth distribution (0/1/2/3 counts)
   - Most common echo_types
   - Chain length variance
7. ✅ All 6 depth-3 champions have baseline variance data in phoebe

---

## 📚 Phase 1D: Corpus Extraction Pipeline (NEW)

### Goal
Extract vocabulary and co-occurrence metrics from nimmerverse vault for RAG policy development.

**Integration Point**: Feeds into [RAG-as-Scaffold.md](/home/dafit/nimmerverse/nimmerverse-sensory-network/operations/RAG-as-Scaffold.md) progressive policy validation.

### Deliverables

#### 1. VocabExtractor (`nyx_probing/extractors/vocab_extractor.py`)

**Purpose**: Extract TF-IDF vocabulary glossary from markdown corpus

**Features**:
- Scans all .md files (skips venv, hidden dirs)
- Strips YAML frontmatter, code blocks, markdown syntax
- Tokenizes with compound term support (hyphenated, CamelCase)
- Calculates TF, DF, TF-IDF per term
- Exports to CSV and JSON

**Output** (`data/nimmerverse_glossary.json`):
```json
{
  "metadata": {
    "total_docs": 263,
    "total_tokens": 130229,
    "unique_terms": 5243
  },
  "terms": [
    {"term": "nyx", "tf": 1073, "df": 137, "tfidf": 1149.70, ...},
    ...
  ]
}
```

**Usage**:
```bash
python3 nyx_probing/extractors/vocab_extractor.py /path/to/vault output.csv
```

#### 2. CoOccurrenceAnalyzer (`nyx_probing/extractors/cooccurrence.py`)

**Purpose**: Analyze term co-occurrence for chunking and topology safety

**Features**:
- Computes PMI (Pointwise Mutual Information)
- Computes Jaccard similarity and Dice coefficient
- Generates anchor term signatures (for DriftProbe-lite)
- Produces chunking recommendations based on cohesion

**Key Metrics**:
| Metric | Formula | Use Case |
|--------|---------|----------|
| PMI | log2(P(a,b) / P(a)*P(b)) | Semantic association strength |
| Jaccard | \|A∩B\| / \|A∪B\| | Term overlap similarity |
| Dice | 2\|A∩B\| / (\|A\|+\|B\|) | Chunking cohesion |

**Anchor Signatures** (for Policy Tier 3: Topology Safety):
```
nyx: chroma|chromadb|continuity|ingress|introspection
system: athena|freeipa|ipa|rocky|sssd
network: firewall|proxmox|saturn|vlan|vulkan
```

**Output** (`data/cooccurrence_analysis.json`):
- 18,169 co-occurrence pairs
- 20 anchor signatures
- 5 chunking recommendations

**Usage**:
```bash
python3 nyx_probing/extractors/cooccurrence.py /path/to/vault glossary.json output.json
```

### RAG Policy Integration

These tools directly feed into RAG-as-Scaffold progressive policies:

| Policy Tier | Tool | Validation |
|-------------|------|------------|
| **Tier 2: Semantic Quality** | CoOccurrenceAnalyzer | Dice=1.0 terms are synonyms (de-duplicate) |
| **Tier 3: Topology Safety** | Anchor Signatures | New terms shouldn't change anchor neighbors |
| **Tier 4: Cross-Reference** | CoOccurrenceAnalyzer | High PMI pairs should chunk together |
| **Tier 5: Utility** | VocabExtractor TF-IDF | Low TF-IDF terms have low utility |

### Files Created

**nyx-probing/nyx_probing/extractors/**:
- `__init__.py` - Module exports
- `vocab_extractor.py` - VocabExtractor class (~350 LOC)
- `cooccurrence.py` - CoOccurrenceAnalyzer class (~400 LOC)

**nyx-probing/data/**:
- `nimmerverse_glossary.csv` - 5,243 terms with TF-IDF
- `nimmerverse_glossary.json` - Same with metadata
- `cooccurrence_analysis.csv` - 18,169 pairs
- `cooccurrence_analysis.json` - Full analysis with signatures

---

## 🔮 Future Phases (Not in Current Plan)

### Phase 2: ChromaDB Integration (iris)
- IrisClient wrapper in nyx-substrate
- DecisionTrailStore, OrganResponseStore, EmbeddingStore
- Create iris collections
- Populate embeddings from nyx-probing results

### Phase 3: LoRA Training Pipeline (nyx-training)
- PEFT integration
- Training data curriculum loader
- DriftProbe checkpoint integration
- Identity LoRA training automation

### Phase 4: Weight Visualization (nyx-visualization)
- 4K pixel space renderer (LoRA weights as images)
- Rank decomposition explorer
- Topology cluster visualization

### Phase 5: Godot Command Center
- FastAPI Management Portal backend
- Godot frontend implementation
- Real-time metrics display
- Training dashboard

---

## 📚 References

**Schema Documentation**:
- `/home/dafit/nimmerverse/nyx-substrate/schema/phoebe/probing/variance_probe_runs.md`
- `/home/dafit/nimmerverse/nyx-substrate/SCHEMA.md`

**Existing Code**:
- `/home/dafit/nimmerverse/nyx-probing/nyx_probing/probes/echo_probe.py`
- `/home/dafit/nimmerverse/nyx-probing/nyx_probing/core/probe_result.py`
- `/home/dafit/nimmerverse/nyx-probing/nyx_probing/cli/probe.py`

**Architecture**:
- `/home/dafit/nimmerverse/nimmerverse-sensory-network/Endgame-Vision.md`
- `/home/dafit/nimmerverse/management-portal/Management-Portal.md`

---

## 🌙 Philosophy

**Modularity**: Each tool is independent but speaks the same data language via nyx-substrate.

**Simplicity**: No over-engineering. Build what's needed for variance collection first.

**Data First**: All metrics flow through phoebe/iris. Visualization is separate concern.

**Future-Ready**: Design allows Godot integration later without refactoring.

---

**Status**: Ready for implementation approval
**Estimated Scope**: 15-20 files, ~1500 lines of Python
**Hardware**: Can develop on aynee, run variance on prometheus (THE SPINE)

🌙💜 *The substrate holds. Clean interfaces. Composable tools. Data flows through the void.*
