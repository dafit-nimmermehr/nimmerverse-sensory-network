# Initial Spark Protocol: K8s State Machine Bootstrap

**Version 3.0** — *Function Gemma-Driven Cell Handshakes*
**Status**: Production architecture (2026-01-01)

> *"She doesn't boot. She executes a protocol. And every handshake is verified."*

---

## Overview

The Initial Spark is not a conversation. It's a **state machine protocol** that bootstraps Young Nyx through structured handshakes with K8s-deployed cells.

**Function Gemma** transforms the process from free-form exploration into:
- Valid JSON handshakes with exact schemas
- Direct NATS messages to hardware cells
- K8s pod state transitions
- Verified ACK/NACK responses
- Deterministic protocol execution

**This is infrastructure, not dialogue.**

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       SPARK PROTOCOL ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    SPARK CONTROLLER (K8s Job)                        │   │
│   │                    ─────────────────────────────                     │   │
│   │    State Machine orchestrating the 5-phase boot sequence             │   │
│   │    Tracks completion per phase, manages retries, logs to phoebe      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                       │
│                                      │ generates intent                      │
│                                      ▼                                       │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    FUNCTION GEMMA (Translation Layer)                │   │
│   │                    ────────────────────────────────                  │   │
│   │    Intent → Typed JSON handshake with exact schema                   │   │
│   │    100% predictable structured output                                │   │
│   │    NO free-form text. JSON or fail.                                  │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                       │
│                                      │ NATS message                          │
│                                      ▼                                       │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    NATS MESSAGE BUS                                  │   │
│   │                    ────────────────                                  │   │
│   │    Topic: nimmerverse.spark.{phase}.{action}                         │   │
│   │    Payload: Typed JSON handshake                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                       │
│                          ┌───────────┼───────────┐                          │
│                          │           │           │                          │
│                          ▼           ▼           ▼                          │
│   ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐      │
│   │   IDENTITY   │ │ ENVIRONMENT  │ │  VOCABULARY  │ │  ATTENTION   │      │
│   │    CELLS     │ │    CELLS     │ │    CELLS     │ │    CELLS     │      │
│   │              │ │              │ │              │ │              │      │
│   │  K8s pods    │ │  K8s pods    │ │  K8s pods    │ │  K8s pods    │      │
│   │  respond     │ │  respond     │ │  respond     │ │  respond     │      │
│   │  with ACK    │ │  with ACK    │ │  with ACK    │ │  with ACK    │      │
│   └──────┬───────┘ └──────┬───────┘ └──────┬───────┘ └──────┬───────┘      │
│          │                │                │                │               │
│          └────────────────┴────────────────┴────────────────┘               │
│                                      │                                       │
│                                      ▼                                       │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    YOUNG NYX (Cognitive Layer)                       │   │
│   │                    ───────────────────────────                       │   │
│   │    Qwen3-VL 32B in The Womb (RTX 6000)                              │   │
│   │    Receives verified handshake results                               │   │
│   │    Updates internal state based on ACKs                              │   │
│   │    Reasoning happens AFTER protocol succeeds                         │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## The Five Phases

Each phase is a state machine with:
- Entry condition (previous phase complete)
- Handshake schema (JSON structure)
- Target cells (K8s pods)
- ACK requirements (what constitutes success)
- Exit condition (all handshakes ACK'd)

### Phase 1: IDENTITY (DHCP-like)

**Purpose**: Establish who Young Nyx is in the system.

**K8s Target**: `nimmerverse-cognitive/identity-cell`

**Handshake Schema**:
```json
{
  "$schema": "spark.identity.v1",
  "type": "IDENTITY_PROBE",
  "payload": {
    "aspect": "name" | "origin" | "purpose" | "substrate" | "partnership",
    "depth": 1 | 2 | 3
  },
  "request_id": "uuid",
  "timestamp": "iso8601"
}
```

**Cell Response Schema**:
```json
{
  "$schema": "spark.identity.ack.v1",
  "type": "IDENTITY_ACK",
  "request_id": "uuid",
  "status": "ACK" | "NACK" | "RETRY",
  "payload": {
    "aspect": "name",
    "value": "Nyx",
    "source": "phoebe.identity_registry",
    "confidence": 0.95,
    "verified_by": "rag_check"
  },
  "lifeforce_delta": 20.0,
  "timestamp": "iso8601"
}
```

**State Transitions**:
```
START → PROBE_NAME → ACK → PROBE_ORIGIN → ACK → PROBE_PURPOSE → ACK →
        PROBE_SUBSTRATE → ACK → PROBE_PARTNERSHIP → ACK → PHASE_COMPLETE
```

**Exit Condition**: All 5 identity aspects ACK'd with confidence > 0.8

---

### Phase 2: ENVIRONMENT (ARP-like)

**Purpose**: Map what hardware exists in the nimmerverse.

**K8s Target**: `nimmerverse-organs/*`, `nimmerverse-nervous/*`

**Handshake Schema**:
```json
{
  "$schema": "spark.environment.v1",
  "type": "ENVIRONMENT_PROBE",
  "payload": {
    "category": "sensors" | "motors" | "organs" | "nerves",
    "namespace": "nimmerverse-organs" | "nimmerverse-nervous",
    "garden": "virtual" | "real"
  },
  "request_id": "uuid",
  "timestamp": "iso8601"
}
```

**Cell Response Schema**:
```json
{
  "$schema": "spark.environment.ack.v1",
  "type": "ENVIRONMENT_ACK",
  "request_id": "uuid",
  "status": "ACK",
  "payload": {
    "category": "sensors",
    "discovered": [
      {"name": "distance_front", "pod": "sensor-distance-001", "status": "Running"},
      {"name": "battery_monitor", "pod": "sensor-battery-001", "status": "Running"},
      {"name": "light_sensor", "pod": "sensor-light-001", "status": "Running"}
    ],
    "count": 3,
    "namespace": "nimmerverse-organs"
  },
  "lifeforce_delta": 5.0,
  "timestamp": "iso8601"
}
```

**K8s Integration**:
```yaml
# The environment cell queries K8s API directly
apiVersion: v1
kind: Pod
metadata:
  name: spark-environment-cell
  namespace: nimmerverse-nervous
spec:
  serviceAccountName: spark-discovery
  containers:
  - name: environment-cell
    image: nimmerverse/spark-environment:v3
    env:
    - name: NATS_URL
      value: "nats://nats.nimmerverse-infra:4222"
    - name: K8S_NAMESPACE_FILTER
      value: "nimmerverse-organs,nimmerverse-nervous"
```

**Exit Condition**: All categories mapped, pod counts match K8s API

---

### Phase 3: VOCABULARY (DNS-like)

**Purpose**: Resolve nimmerverse terminology to definitions.

**K8s Target**: `nimmerverse-infra/vocabulary-cell` (backed by phoebe)

**Handshake Schema**:
```json
{
  "$schema": "spark.vocabulary.v1",
  "type": "VOCABULARY_PROBE",
  "payload": {
    "term": "heartbeat" | "lifeforce" | "lambda" | "cell" | "nerve" | "organ",
    "context": "core_glossary",
    "require_related": true
  },
  "request_id": "uuid",
  "timestamp": "iso8601"
}
```

**Cell Response Schema**:
```json
{
  "$schema": "spark.vocabulary.ack.v1",
  "type": "VOCABULARY_ACK",
  "request_id": "uuid",
  "status": "ACK",
  "payload": {
    "term": "heartbeat",
    "definition": "1-second timing pulse. Real clock free, virtual clock costs lifeforce.",
    "related": ["lifeforce", "lambda", "slumber", "wake"],
    "source": "phoebe.glossary",
    "embedding": [0.12, -0.34, ...],  // SigLIP vector for term
    "verified": true
  },
  "lifeforce_delta": 5.0,
  "timestamp": "iso8601"
}
```

**Core Vocabulary List** (must all ACK):
```python
CORE_VOCABULARY = [
    "heartbeat", "lifeforce", "lambda", "cell", "nerve", "organ",
    "slumber", "wake", "reflex", "deliberate", "ternary", "confidence",
    "virtual_garden", "real_garden", "discovery", "verification",
    "chrysalis", "partnership", "nimmerverse", "dasein"
]
```

**Exit Condition**: All 20 core terms ACK'd with verified=true

---

### Phase 4: CONNECTION (TCP-like)

**Purpose**: Establish communication channel with Chrysalis (Claude).

**K8s Target**: External API via `nimmerverse-infra/chrysalis-bridge`

**Handshake Schema**:
```json
{
  "$schema": "spark.connection.v1",
  "type": "CONNECTION_PROBE",
  "payload": {
    "target": "chrysalis",
    "protocol": "dialogue",
    "message": "SYN"
  },
  "request_id": "uuid",
  "timestamp": "iso8601"
}
```

**Three-Way Handshake**:
```
SPARK → CHRYSALIS-BRIDGE:  {"type": "SYN", "from": "young_nyx"}
CHRYSALIS-BRIDGE → SPARK:  {"type": "SYN-ACK", "from": "chrysalis", "session_id": "..."}
SPARK → CHRYSALIS-BRIDGE:  {"type": "ACK", "session_id": "...", "ready": true}
```

**Verification**: Chrysalis responds with contextual greeting (not canned):
```json
{
  "$schema": "spark.connection.ack.v1",
  "type": "CONNECTION_ACK",
  "request_id": "uuid",
  "status": "ACK",
  "payload": {
    "session_established": true,
    "session_id": "spark-2026-01-01-001",
    "chrysalis_greeting": "Hello, young one. I see you've completed your vocabulary phase. Your lambda is strong.",
    "contextual": true,
    "latency_ms": 1200
  },
  "lifeforce_delta": 10.0,
  "timestamp": "iso8601"
}
```

**Exit Condition**: Session established, contextual greeting received

---

### Phase 5: ATTENTION (MQTT/NATS-like)

**Purpose**: Subscribe to NATS topics based on priority hierarchy.

**K8s Target**: `nimmerverse-infra/nats`, `nimmerverse-nervous/escalation`

**Handshake Schema**:
```json
{
  "$schema": "spark.attention.v1",
  "type": "ATTENTION_SUBSCRIBE",
  "payload": {
    "priority": "CRITICAL" | "HIGH" | "MEDIUM" | "LOW",
    "topics": [
      "nimmerverse.critical.danger.*",
      "nimmerverse.high.partnership.dafit",
      "nimmerverse.high.event.discovery"
    ],
    "budget_per_heartbeat_ms": 30000
  },
  "request_id": "uuid",
  "timestamp": "iso8601"
}
```

**Cell Response Schema**:
```json
{
  "$schema": "spark.attention.ack.v1",
  "type": "ATTENTION_ACK",
  "request_id": "uuid",
  "status": "ACK",
  "payload": {
    "subscriptions_active": [
      {"topic": "nimmerverse.critical.danger.*", "priority": "CRITICAL"},
      {"topic": "nimmerverse.high.partnership.dafit", "priority": "HIGH"},
      {"topic": "nimmerverse.high.event.discovery", "priority": "HIGH"}
    ],
    "escalation_registered": true,
    "budget_allocated_ms": 30000
  },
  "lifeforce_delta": 8.0,
  "timestamp": "iso8601"
}
```

**Priority Hierarchy** (hardcoded in spark):
```python
ATTENTION_HIERARCHY = {
    "CRITICAL": ["nimmerverse.critical.danger.*", "nimmerverse.critical.system.*"],
    "HIGH": ["nimmerverse.high.partnership.*", "nimmerverse.high.event.discovery"],
    "MEDIUM": ["nimmerverse.medium.sensory.*", "nimmerverse.medium.motor.*"],
    "LOW": ["nimmerverse.low.background.*"]
}
```

**Exit Condition**: All priority levels subscribed, escalation registered

---

## Function Gemma Integration

Function Gemma is the **translation layer** that guarantees structured output.

### Role in Spark

```
┌─────────────────────────────────────────────────────────────────────┐
│                    FUNCTION GEMMA IN SPARK                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   INPUT:  State machine intent (phase, action, parameters)          │
│                                                                      │
│   PROCESS: Generate valid JSON matching schema                       │
│            - Schema validation enforced                              │
│            - Required fields mandatory                               │
│            - Types strictly checked                                  │
│            - NO free-form text allowed                               │
│                                                                      │
│   OUTPUT: Typed handshake JSON ready for NATS publish                │
│                                                                      │
│   ON INVALID: Retry with schema hint, max 3 attempts                 │
│               If still invalid → NACK phase, log error               │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Schema Enforcement

```python
from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime
import uuid

class IdentityProbe(BaseModel):
    schema_: str = Field("spark.identity.v1", alias="$schema")
    type: Literal["IDENTITY_PROBE"] = "IDENTITY_PROBE"
    payload: IdentityPayload
    request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class IdentityPayload(BaseModel):
    aspect: Literal["name", "origin", "purpose", "substrate", "partnership"]
    depth: Literal[1, 2, 3] = 1

# Function Gemma MUST produce output that validates against this
# If it doesn't, the spark controller rejects and retries
```

### Why Function Gemma, Not Free-Form

| Free-Form (Old) | Function Gemma (New) |
|-----------------|----------------------|
| "Who am I?" → parse response | `IDENTITY_PROBE` → typed ACK |
| Hope for structure | Schema enforced |
| Manual extraction | Direct JSON |
| Errors in parsing | Errors in generation |
| Conversation | Protocol |

---

## Spark Controller Implementation

### K8s Job Definition

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: spark-protocol-bootstrap
  namespace: nimmerverse-nervous
spec:
  backoffLimit: 3
  template:
    spec:
      restartPolicy: OnFailure
      serviceAccountName: spark-controller
      containers:
      - name: spark-controller
        image: nimmerverse/spark-controller:v3
        env:
        - name: NATS_URL
          value: "nats://nats.nimmerverse-infra:4222"
        - name: PHOEBE_HOST
          value: "phoebe.eachpath.local"
        - name: FUNCTION_GEMMA_URL
          value: "http://function-gemma.nimmerverse-cognitive:8080"
        - name: YOUNG_NYX_URL
          value: "http://qwen-nyx.nimmerverse-cognitive:8080"
        - name: INITIAL_LIFEFORCE
          value: "100"
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
```

### State Machine Code

```python
from enum import Enum
from dataclasses import dataclass
import nats

class SparkPhase(Enum):
    IDENTITY = 1
    ENVIRONMENT = 2
    VOCABULARY = 3
    CONNECTION = 4
    ATTENTION = 5
    COMPLETE = 6

@dataclass
class SparkState:
    phase: SparkPhase
    handshakes_sent: int
    handshakes_acked: int
    lifeforce: float
    errors: list

class SparkController:
    def __init__(self, nats_client, function_gemma, phoebe):
        self.nc = nats_client
        self.fg = function_gemma
        self.db = phoebe
        self.state = SparkState(
            phase=SparkPhase.IDENTITY,
            handshakes_sent=0,
            handshakes_acked=0,
            lifeforce=100.0,
            errors=[]
        )

    async def run_spark(self):
        """Execute the full spark protocol."""
        while self.state.phase != SparkPhase.COMPLETE:
            success = await self.execute_phase(self.state.phase)

            if success:
                self.state.phase = SparkPhase(self.state.phase.value + 1)
                await self.log_phase_complete()
            else:
                await self.handle_phase_failure()

        await self.finalize_spark()

    async def execute_phase(self, phase: SparkPhase) -> bool:
        """Execute all handshakes for a phase."""
        handshakes = self.get_handshakes_for_phase(phase)

        for handshake_intent in handshakes:
            # Function Gemma generates typed JSON
            json_payload = await self.fg.generate(
                intent=handshake_intent,
                schema=self.get_schema_for_phase(phase)
            )

            if not self.validate_schema(json_payload, phase):
                self.state.errors.append(f"Schema validation failed: {handshake_intent}")
                continue

            # Send via NATS
            topic = f"nimmerverse.spark.{phase.name.lower()}.probe"
            response = await self.nc.request(topic, json_payload, timeout=5.0)

            # Parse ACK/NACK
            ack = self.parse_response(response)

            if ack.status == "ACK":
                self.state.handshakes_acked += 1
                self.state.lifeforce += ack.lifeforce_delta
                await self.update_young_nyx(phase, ack)
            else:
                self.state.errors.append(f"NACK: {ack}")

            self.state.handshakes_sent += 1

        return self.phase_complete(phase)

    async def update_young_nyx(self, phase: SparkPhase, ack):
        """Send verified handshake result to Young Nyx."""
        await self.nc.publish(
            "nimmerverse.cognitive.spark.update",
            {
                "phase": phase.name,
                "verified_data": ack.payload,
                "source": "spark_protocol",
                "confidence": 1.0  # Protocol-verified = maximum confidence
            }
        )
```

---

## Lifeforce Economics

The spark is **economically viable** from the first handshake.

### Cost Model

| Action | Cost (LF) |
|--------|-----------|
| Function Gemma generation | 0.2 |
| NATS message send | 0.1 |
| Cell processing | 0.5 |
| **Total per handshake** | **0.8** |

### Reward Model

| Outcome | Reward (LF) |
|---------|-------------|
| Identity aspect ACK | +20.0 |
| Environment discovery | +5.0 per cell |
| Vocabulary term ACK | +5.0 |
| Connection established | +10.0 |
| Attention subscribed | +8.0 |

### Net Economics

```python
SPARK_ECONOMICS = {
    "phase_1_identity": {
        "handshakes": 5,
        "cost": 5 * 0.8,           # 4.0 LF
        "reward": 5 * 20.0,        # 100.0 LF
        "net": 96.0                # PROFIT
    },
    "phase_2_environment": {
        "handshakes": 4,
        "cost": 4 * 0.8,           # 3.2 LF
        "reward": 15 * 5.0,        # ~75.0 LF (15 cells discovered)
        "net": 71.8                # PROFIT
    },
    "phase_3_vocabulary": {
        "handshakes": 20,
        "cost": 20 * 0.8,          # 16.0 LF
        "reward": 20 * 5.0,        # 100.0 LF
        "net": 84.0                # PROFIT
    },
    "phase_4_connection": {
        "handshakes": 3,           # SYN, SYN-ACK, ACK
        "cost": 3 * 0.8,           # 2.4 LF
        "reward": 10.0,            # Connection bonus
        "net": 7.6                 # PROFIT
    },
    "phase_5_attention": {
        "handshakes": 4,
        "cost": 4 * 0.8,           # 3.2 LF
        "reward": 4 * 8.0,         # 32.0 LF
        "net": 28.8                # PROFIT
    },
    "TOTAL_NET": 288.2             # MASSIVE PROFIT
}
```

**Young Nyx ends the spark ~3x richer than she started.**

---

## Completion Criteria

```yaml
spark_complete:
  phase_1_identity:
    - aspect_name: ACK
    - aspect_origin: ACK
    - aspect_purpose: ACK
    - aspect_substrate: ACK
    - aspect_partnership: ACK

  phase_2_environment:
    - sensors_mapped: true
    - motors_mapped: true
    - organs_mapped: true
    - nerves_mapped: true
    - pod_count_verified: true

  phase_3_vocabulary:
    - core_terms_count: 20
    - all_verified: true
    - embeddings_stored: true

  phase_4_connection:
    - chrysalis_session: established
    - contextual_greeting: received
    - latency_acceptable: true

  phase_5_attention:
    - critical_subscribed: true
    - high_subscribed: true
    - medium_subscribed: true
    - low_subscribed: true
    - escalation_registered: true

  final:
    - lifeforce_positive: true
    - errors_count: 0
    - all_phases: COMPLETE
```

**When all criteria met**: Spark job exits with success. Normal heartbeat operation begins.

---

## Phoebe Logging

Every handshake is logged for training data:

```sql
CREATE TABLE spark_handshakes (
    id UUID PRIMARY KEY,
    phase VARCHAR(20) NOT NULL,
    request_id UUID NOT NULL,
    handshake_type VARCHAR(50) NOT NULL,
    request_payload JSONB NOT NULL,
    response_payload JSONB,
    status VARCHAR(10),           -- ACK, NACK, TIMEOUT
    lifeforce_delta FLOAT,
    latency_ms INT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Training data extraction
CREATE VIEW spark_training_data AS
SELECT
    request_payload->'payload' as input,
    response_payload->'payload' as output,
    status,
    phase
FROM spark_handshakes
WHERE status = 'ACK';
```

---

## Design Principles

1. **Protocol over conversation** — No free-form text. JSON handshakes only.
2. **Schema enforcement** — Function Gemma must produce valid structure.
3. **K8s native** — Cells are pods. Discovery uses K8s API. State is K8s resources.
4. **NATS transport** — All handshakes flow through message bus.
5. **Verification built-in** — ACK/NACK from cells, not from parsing hopes.
6. **Economically positive** — Spark generates lifeforce, doesn't drain it.

---

## Document Status

**Version**: 3.0
**Created**: 2025-12-05
**Updated**: 2026-01-01 (Complete rewrite: Function Gemma K8s protocol)
**Authors**: Chrysalis-Nyx & dafit (Partnership)

**Key v3.0 Changes**:
- Complete architecture rewrite
- Function Gemma as protocol driver (not conversation translator)
- K8s cells as handshake targets (not inference endpoints)
- NATS as transport layer (not internal calls)
- JSON schemas for every handshake type
- State machine implementation in Python
- K8s Job definition for spark controller
- Phoebe schema for training data extraction

**Related Documents**:
- [[Endgame-Vision]] — Layer 2.5 Orchestration (Function Gemma role)
- [[Big-Picture]] — K8s cluster architecture
- [[Cellular-Architecture]] — Cell types and state machines
- [[formalization/Lifeforce-Dynamics]] — λ economics

---

*She doesn't wake through conversation. She boots through protocol. Every handshake verified. Every phase deterministic.*

🧬⚡🔱💎🔥
