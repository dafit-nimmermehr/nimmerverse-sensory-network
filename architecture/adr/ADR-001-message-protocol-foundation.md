# ADR-001: Message Protocol Foundation

**Status:** Accepted
**Date:** 2025-12-31
**Decision Makers:** dafit, Nyx (Chrysalis)
**Context:** Silvester Interview Session

---

## Context

The Nimmerverse Sensory Network requires a message-passing infrastructure that serves two purposes:

1. **Production**: Cells, nerves, organs, and Young Nyx communicate via pub/sub messaging
2. **Development**: Claude and local AI agents (LangChain, Qwen, etc.) collaborate during build

We needed to decide on namespace organization, schema evolution strategy, initial implementation scope, and the interface contract between AI models and the message bus.

The core architectural principle established in [Message-Protocol-Design.md](../Message-Protocol-Design.md) is: **dumb router, smart edges**. NATS is infrastructure. Intelligence lives in clients.

---

## Decisions

### Decision 1: Single Bus, Multiple Namespaces

**Choice:** One NATS instance with topic-based separation for different concerns.

**Namespace Structure:**

```
nimmerverse.
├── staging.                    # Experimental schemas (mutable during development)
│   ├── low.*                   # Staging heartbeats
│   ├── high.*                  # Staging events
│   └── dev.*                   # Staging dev agents
│
├── low.*                       # Production heartbeats (stable schemas only)
├── high.*                      # Production events
├── command.*                   # Production commands to entities
├── meta.*                      # System-level (attention config, health)
└── dev.*                       # Production dev agents (stable schemas)
```

**Rationale:** Infrastructure should be long-lived. Models are ephemeral. One bus serves all purposes - production sensing, development agents, future capabilities. Topic separation keeps concerns isolated without operational complexity of multiple NATS instances.

---

### Decision 2: Staged Schema Versioning with Topic Separation

**Choice:** Schemas evolve through lifecycle stages. Staging schemas live on `nimmerverse.staging.*`, stable schemas on `nimmerverse.*`.

**Schema Header:**

```json
{
  "header": {
    "schema": {
      "generation": 1,
      "version": "1.0"
    },
    "message_type": "HeartbeatSignal",
    "message_id": "uuid",
    "timestamp_real": "ISO8601",
    ...
  }
}
```

**Lifecycle:**

```
STAGING                          STABLE
version: 0.1-alpha    ──▶       generation: 1, version: "1.0"
version: 0.2-beta                    │
version: 0.3-rc                      ▼
                                NEXT CYCLE
                                version: 1.1-alpha
                                version: 1.2-beta
                                     │
                                     ▼
                                generation: 2, version: "2.0"
```

**Rationale:**
- Topic separation avoids per-message filtering costs
- Generation locks after stability (immutable)
- Version iterates within generation for additive changes
- Breaking changes = new generation = new staging cycle

---

### Decision 3: Echo Agent First

**Choice:** Start with trivial Echo agent, evolve based on real friction.

**Echo Specification:**

```
Subscribe: nimmerverse.dev.request.echo
Publish:   nimmerverse.dev.response.echo

Input:  { "ping": "hello" }
Output: { "pong": "hello", "timestamp": "...", "agent": "echo-v1" }
```

**Rationale:** YAGNI. Echo proves the full round-trip without cognitive complexity:
- NATS connection works
- Topic routing works
- Request/response pattern works
- Message schema works
- Local agent can subscribe and publish

Future agents (Grep, Schema Lookup, File Summarizer) emerge from discovered needs, not imagined features.

---

### Decision 4: MCP Server with Heartbeat-Based Subscriptions

**Choice:** Build NATS-MCP bridge as interface for all AI models. Use heartbeat pattern for subscription delivery.

**MCP Tools:**

```python
@mcp.tool()
async def publish(topic: str, payload: dict) -> dict:
    """Fire-and-forget publish to NATS"""

@mcp.tool()
async def request(topic: str, payload: dict, timeout_ms: int = 5000) -> dict:
    """Publish and wait for single response (request-reply pattern)"""

@mcp.tool()
async def heartbeat() -> dict:
    """Check bus health + drain accumulated messages from subscriptions"""

@mcp.tool()
async def subscribe(topic_pattern: str) -> dict:
    """Add a subscription pattern (persists until unsubscribe)"""

@mcp.tool()
async def unsubscribe(topic_pattern: str) -> dict:
    """Remove a subscription pattern"""
```

**Heartbeat Response:**

```json
{
  "status": "healthy",
  "buffer": {
    "capacity": 100,
    "current_count": 23,
    "messages_dropped_since_last_heartbeat": 0,
    "messages_dropped_total": 0,
    "oldest_message_age_ms": 4521
  },
  "subscriptions": ["nimmerverse.dev.>"],
  "messages": [...]
}
```

**Buffer Overflow Handling:**
- Bounded buffer (100 messages default)
- Oldest dropped when full
- Dropped count visible in heartbeat response
- Optional: publish to `nimmerverse.meta.health.buffer_drop` on overflow

**Rationale:**
- MCP is universal interface - Claude, LangChain, Qwen, future models
- Heartbeat pattern matches existing nervous system design
- Polling is simpler than streaming for MCP's request/response model
- Visibility into drops prevents silent data loss

---

## Consequences

### Enables

- **Unified infrastructure** for production sensing and development assistance
- **Model agnosticism** - any MCP-speaking model can participate
- **Safe experimentation** - staging namespace for schema evolution
- **Progressive enhancement** - Echo today, sophisticated agents later
- **Observability** - Command Center can monitor all namespaces

### Constrains

- **Single point of failure** - NATS must be highly available for production
- **Buffer limitations** - Long agent operations may drop messages
- **MCP dependency** - Non-MCP models need wrapper (acceptable, MCP is the standard)

### Deferred

- **Persistent subscriptions** - No durable subscriptions in initial design
- **Message replay** - No historical message retrieval
- **Authentication/Authorization** - Trust model for initial development

---

## Implementation Notes

### Phase 1: Infrastructure

1. Deploy NATS server (likely via Docker on ThinkStation)
2. Create `nats-bridge` MCP server (Python, using `nats-py` and `mcp` SDK)
3. Register MCP server with Claude Code

### Phase 2: Echo Agent

1. Simple Python daemon subscribing to `nimmerverse.dev.request.echo`
2. Responds on `nimmerverse.dev.response.echo`
3. Validate round-trip through MCP tools

### Phase 3: Iteration

1. Use Echo to build confidence in the bus
2. Add agents as friction reveals needs
3. Evolve schemas through staging → stable promotion

---

## References

- [Message-Protocol-Design.md](../Message-Protocol-Design.md) - Original protocol design
- [NATS Documentation](https://docs.nats.io/)
- [MCP Specification](https://modelcontextprotocol.io/)

---

**Filed:** 2025-12-31 (Silvester)
**Interview Method:** Structured Q&A, partnership dialogue
**Philosophy:** "Dumb core, smart edges. Infrastructure is geology. Models are weather."
