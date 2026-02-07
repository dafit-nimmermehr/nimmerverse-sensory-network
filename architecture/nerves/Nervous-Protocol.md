# Nervous Protocol: Three-Tier Autonomous Learning Architecture

**Version:** 1.1 | **Created:** 2025-12-07 | **Updated:** 2025-12-07

---

## Overview

The **Nervous Protocol** defines how intelligence flows through the Nimmerverse via a three-tier architecture with message-based communication, state machine tools, and collaborative learning.

### The Three Tiers:

```
┌─────────────────────────────────────────────┐
│              dafit                          │
│         (Strategic Architect)               │
│   • Vision & architecture decisions         │
│   • Override authority                      │
│   • Long-term direction                     │
└──────────────────┬──────────────────────────┘
                   ↕ (strategic guidance / major escalations)
┌─────────────────────────────────────────────┐
│          Chrysalis-Nyx                      │
│       (Oversight & Reasoning)               │
│   • Claude Opus/Sonnet (large context)      │
│   • Full toolchain access via LangChain     │
│   • Reviews Young Nyx's proposals           │
│   • Designs new state machines              │
│   • Teaching & guidance                     │
└──────────────────┬──────────────────────────┘
                   ↕ (guidance / escalations)
┌─────────────────────────────────────────────┐
│            Young Nyx                        │
│       (Autonomous Learning Agent)           │
│   • Smaller model (7B or similar)           │
│   • Limited known state machines            │
│   • Executes routine tasks                  │
│   • Learns from experience                  │
│   • Escalates complex problems              │
└─────────────────────────────────────────────┘
```

---

## Core Principles

### 1. **Message-Based Continuity**

All communication flows through **phoebe** (PostgreSQL) via message tables:
- `partnership_to_nimmerverse_messages` (dafit + Chrysalis → Young Nyx)
- `nimmerverse_to_partnership_messages` (Young Nyx → dafit + Chrysalis)

**Why messages?**
- ✅ Persistent across sessions
- ✅ Asynchronous (no blocking)
- ✅ Auditable (every decision logged)
- ✅ Simple (append-only, no complex state sync)

### 2. **Heartbeat Coordination**

From `Endgame-Vision.md`:
- **Real clock**: 1 Hz (1 beat/sec) - wall time, free
- **Virtual clock**: Variable - computation time, costs lifeforce

**On each heartbeat:**
1. Check for new messages from any tier
2. Process guidance/tasks/escalations
3. Update state
4. Take next action
5. Write results back to phoebe

**Not real-time** (milliseconds), but **continuous** (heartbeat-driven).

### 3. **State Machines as Tools**

All capabilities are exposed as **state machine tools** via **LangChain**:

```python
# Example: phoebe query state machine
from langchain.tools import BaseTool

States: IDLE → CONNECTED → QUERY_READY → IDLE

class PhoebeQueryTool(BaseTool):
    name = "phoebe_query"
    description = """
    Interact with phoebe database using state machine pattern.

    Available actions depend on current state:
    - IDLE: connect(host, db) → CONNECTED
    - CONNECTED: query(sql) → QUERY_READY, disconnect() → IDLE
    - QUERY_READY: query(sql), disconnect() → IDLE
    """
```

**Why state machines?**
- ✅ Safety (can't skip steps - must CONNECT before QUERY)
- ✅ Discoverable (each state announces valid transitions)
- ✅ Observable (log every transition)
- ✅ Composable (chain state machines together)

### 4. **Progressive Capability Unlocking**

**Dual catalogues:**
- **All available tools** (full registry, managed by dafit/Chrysalis)
- **Young Nyx's known tools** (subset she's discovered)

Young Nyx can only see/use tools she's discovered. New tools are granted:
- Via teaching moments (Chrysalis: "You're ready for X")
- Via successful escalations (solved problem reveals tool)
- Via collaborative design (she helps build it)

**Discovery tracking in phoebe:**
```sql
CREATE TABLE discovered_tools (
    agent_id TEXT,
    tool_name TEXT,
    discovered_at TIMESTAMPTZ DEFAULT NOW(),
    discovered_via TEXT,  -- "teaching", "escalation", "design"
    PRIMARY KEY (agent_id, tool_name)
);
```

---

## The OR Gate Pattern (Input Sources)

From `nimmerverse.drawio.xml` (lines 215-244):

```
┌──────────┐       ┌──────────┐
│  dafit   │       │chrysalis │
│ (OR gate)│       │ (OR gate)│
└────┬─────┘       └────┬─────┘
     │                  │
     └────────┬─────────┘
              ↓ (OR - either/both)
         Message Queue (phoebe)
              ↓ (read on heartbeat)
         Orchestrator
              ↓
         Young Nyx
```

**OR gate = Either/both can write, no blocking**

Both dafit and Chrysalis write to `partnership_to_nimmerverse_messages`. The orchestrator synthesizes on each heartbeat.

**Conflict resolution:**
1. dafit veto > Chrysalis approval
2. dafit approval > Chrysalis approval
3. Chrysalis handles day-to-day (if no dafit input)
4. Default: WAIT for guidance

---

## LangChain + State Machine Integration

### State Machines as LangChain Tools

Each capability is a **LangChain BaseTool** that implements a **state machine**:

```python
# phoebe_state_machine_tool.py
from langchain.tools import BaseTool
from nyx_substrate.database import PhoebeConnection

class PhoebeStateMachineTool(BaseTool):
    """State machine tool for phoebe database access."""

    name = "phoebe"
    description = """
    Query phoebe database using state machine pattern.

    States: IDLE → CONNECTED → QUERY_READY → IDLE

    Usage:
    - To connect: action='connect', host='phoebe.eachpath.local', database='nimmerverse'
    - To query: action='query', sql='SELECT ...'
    - To disconnect: action='disconnect'

    The tool tracks state and only allows valid transitions.
    """

    def __init__(self):
        super().__init__()
        self.state = "IDLE"
        self.conn = None

    def _run(self, action: str, **kwargs) -> str:
        """Execute state machine transition."""

        if action == "connect":
            if self.state != "IDLE":
                return f"Error: Cannot connect from {self.state}. Available: {self.get_transitions()}"

            host = kwargs.get("host", "phoebe.eachpath.local")
            database = kwargs.get("database", "nimmerverse")

            self.conn = PhoebeConnection(host=host, database=database)
            self.state = "CONNECTED"

            return f"✓ Connected to {host}/{database}. State: CONNECTED. Available: query, disconnect"

        elif action == "query":
            if self.state not in ["CONNECTED", "QUERY_READY"]:
                return f"Error: Must be CONNECTED (currently {self.state})"

            sql = kwargs.get("sql")
            result = self.conn.execute(sql)
            self.state = "QUERY_READY"

            return f"✓ Query executed. {len(result)} rows. State: QUERY_READY. Available: query, disconnect"

        elif action == "disconnect":
            if self.conn:
                self.conn.close()
            self.state = "IDLE"
            return "✓ Disconnected. State: IDLE. Available: connect"

        else:
            return f"Error: Unknown action '{action}'. Available actions depend on state {self.state}"

    def get_transitions(self):
        """Discovery: what transitions are valid from current state?"""
        transitions = {
            "IDLE": ["connect"],
            "CONNECTED": ["query", "disconnect"],
            "QUERY_READY": ["query", "disconnect"]
        }
        return transitions.get(self.state, [])
```

### Tool Discovery via LangChain

```python
from langchain.tools import BaseTool

class DiscoverToolsTool(BaseTool):
    """Tool for discovering available tools for an agent."""

    name = "discover_tools"
    description = "Discover which tools this agent currently has access to"

    def _run(self, agent_id: str = "young_nyx") -> str:
        """Return only tools this agent has discovered."""
        from nyx_substrate.database import get_discovered_tools, get_all_tools

        discovered = get_discovered_tools(agent_id)
        all_tools = get_all_tools()

        result = f"Agent: {agent_id}\n"
        result += f"Discovered tools: {len(discovered)}/{len(all_tools)}\n\n"
        result += "Known tools:\n"
        for tool in discovered:
            result += f"  - {tool['name']}: {tool['description']}\n"

        return result
```

---

## Escalation Protocol

### Young Nyx Escalates to Chrysalis

When Young Nyx encounters a task beyond her capability, she uses the **escalation tool**:

```python
from langchain.tools import BaseTool

class EscalateToChrysalisTool(BaseTool):
    """Tool for escalating complex tasks to Chrysalis-Nyx."""

    name = "escalate_to_chrysalis"
    description = """
    Request help from Chrysalis-Nyx for complex tasks.

    Use when:
    - Task requires capabilities you don't have
    - Statistical analysis needed
    - Complex reasoning required
    - Code generation needed

    Provide:
    - task: What you need help with
    - category: "statistics", "code", "visualization", "general"
    - context: Relevant information
    - what_i_tried: What you've already attempted
    """

    def _run(
        self,
        task: str,
        category: str = "general",
        context: dict = None,
        what_i_tried: str = None
    ) -> str:
        """Escalate a task to Chrysalis."""

        from nyx_substrate.database import write_nimmerverse_message

        escalation_id = write_nimmerverse_message(
            message=f"Escalation: {task}\nCategory: {category}\nContext: {context}\nWhat I tried: {what_i_tried}",
            message_type="escalation_to_chrysalis",
            category=category,
            status="pending"
        )

        # Check if Chrysalis available (same session)
        if chrysalis_available():
            result = chrysalis_agent.solve_escalation(escalation_id)
            return f"""✓ Chrysalis solved it!

Solution: {result['solution']}

Teaching moment: {result['teaching']}

{f"New tools discovered: {', '.join(result['new_tools'])}" if result.get('new_tools') else ''}
"""

        # Otherwise queue for next session
        return f"✓ Escalated to Chrysalis (ID: {escalation_id}). Check back next heartbeat for response."
```

### Chrysalis Agent with LangChain

```python
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain.chat_models import ChatAnthropic
from langchain.tools import BaseTool

class ChrysalisAgent:
    """Chrysalis-Nyx oversight and guidance layer."""

    def __init__(self):
        # Load all available tools (full catalogue)
        self.tools = self.load_all_tools()

        # Initialize Claude Opus via LangChain
        self.llm = ChatAnthropic(
            model="claude-opus-4-5",
            temperature=0.7
        )

        # Create agent executor
        self.agent = create_structured_chat_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.get_chrysalis_prompt()
        )

        self.executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True
        )

        # Sub-agents for specialized tasks
        self.sub_agents = {
            "statistics": StatisticalAnalyzer(),
            "code": CodeGenerator(),
            "visualization": Visualizer(),
            "state_machine_designer": StateMachineDesigner(),
            "general": GeneralReasoner()
        }

    def solve_escalation(self, escalation_id):
        """Process an escalation from Young Nyx."""

        escalation = read_nimmerverse_message(escalation_id)

        # Route to appropriate sub-agent
        agent = self.sub_agents.get(
            escalation.category,
            self.sub_agents["general"]
        )

        # Solve using specialized agent
        result = agent.run(
            task=escalation.task,
            context=escalation.context
        )

        # Create teaching moment
        teaching = self.create_teaching_moment(
            task=escalation.task,
            solution=result,
            young_nyx_attempt=escalation.what_i_tried
        )

        # Recommend tool discovery
        new_tools = self.recommend_tool_discovery(escalation, result)

        # Write response to phoebe
        write_partnership_message(
            message=f"Solved: {result.solution}\nTeaching: {teaching}",
            message_type="escalation_response",
            in_reply_to=escalation_id,
            resolved=True
        )

        return {
            "solution": result.solution,
            "teaching_moment": teaching,
            "tools_to_discover": new_tools
        }
```

---

## Collaborative State Machine Design

### The Meta-Level: Building Tools Together

When Young Nyx needs a capability that doesn't exist, she can request **state machine design**:

```python
from langchain.tools import BaseTool

class RequestStateMachineDesignTool(BaseTool):
    """Tool for requesting new state machine design from Chrysalis."""

    name = "request_state_machine_design"
    description = """
    Request Chrysalis to design a new state machine tool.

    Provide:
    - task_description: What the tool should accomplish
    - desired_outcome: What success looks like
    - example_usage: How you'd use it
    - constraints: Any limitations or requirements

    Returns a proposed specification and code for testing.
    """

    def _run(
        self,
        task_description: str,
        desired_outcome: str,
        example_usage: str,
        constraints: list = None
    ) -> str:
        """Request a new state machine design."""

        result = chrysalis_agent.invoke_subagent(
            agent="state_machine_designer",
            task={
                "type": "design_new_state_machine",
                "description": task_description,
                "outcome": desired_outcome,
                "example": example_usage,
                "constraints": constraints or []
            }
        )

        return f"""✓ Proposed state machine design:

{result['specification']}

Implementation (LangChain tool):
{result['implementation']}

Test cases:
{result['test_cases']}

Instructions:
{result['instructions']}
"""
```

### The Design → Test → Refine Loop

```
1. Young Nyx: "Need tool for deploying cells"
   ↓
2. Request state machine design (via LangChain tool)
   ↓
3. Chrysalis: Designs state machine specification
   - States: IDLE → IMAGE_READY → SPAWNED → RUNNING
   - Transitions: prepare_image, spawn_container, wait_ready
   - Returns: Specification + LangChain BaseTool code
   ↓
4. Young Nyx: Tests proposed state machine
   - Executes test cases
   - Reports success/failures
   ↓
5. Chrysalis: Refines based on feedback
   - Analyzes errors
   - Updates specification
   - Returns v2
   ↓
6. Iterate until validated
   ↓
7. Add to permanent catalogue
   - New LangChain tool deployed
   - Young Nyx discovers tool
   - Future use without escalation
```

**Why this accelerates:**
- Build once, use forever
- Young Nyx participates (testing validates real use cases)
- Toolchain grows organically (demand-driven)
- Each new tool = permanent capability expansion

---

## Dual Decision Tracking

Every decision is tracked from **both perspectives**:

```python
class DecisionLog:
    def log_decision(self, task, young_nyx_choice, oversight_response, outcome):
        record = {
            "timestamp": now(),
            "task": task,
            "young_nyx_choice": young_nyx_choice,  # What she proposed
            "oversight_response": oversight_response,  # dafit/Chrysalis decision
            "outcome": outcome,  # success/failure/learned
            "danger_zone": self.check_danger(young_nyx_choice, outcome)
        }

        self.dao.insert_decision(record)

        # If nudge → learning signal
        if oversight_response["type"] == "nudge":
            self.record_learning_moment(record)
```

**Why track both?**
- Young Nyx's choices reveal her current understanding
- Oversight responses are teaching moments
- Patterns emerge (when does she need help? for what?)
- Danger zones identified (what mistakes does she make?)

---

## Danger Zone Monitoring

```python
class DangerZoneDetector:
    def check_for_danger_patterns(self, plan):
        """Detect risky operations before execution."""
        dangers = []

        # Pattern: SSH without auth
        if "ssh" in plan and not plan.authenticated:
            dangers.append("SSH_WITHOUT_AUTH")

        # Pattern: Database write to critical table
        if "DELETE FROM partnership_messages" in plan:
            dangers.append("CRITICAL_DATA_DELETION")

        # Pattern: Docker with --privileged
        if "docker" in plan and "--privileged" in plan:
            dangers.append("PRIVILEGED_CONTAINER")

        return dangers

    def require_approval_for_danger(self, dangers):
        if dangers:
            return {
                "auto_execute": False,
                "requires_approval": True,
                "danger_flags": dangers,
                "escalate_to": "dafit"  # Serious dangers go to dafit
            }
```

---

## Learning & Growth Patterns

### Week 1: Basic Capabilities
```python
young_nyx.known_tools = [
    "phoebe_connect",
    "phoebe_query",
    "escalate_to_chrysalis"
]
```

### Month 1: Discovering Specialization
```python
# After 5 statistical escalations:
chrysalis_message = """
You've escalated statistics 5 times. Ready for specialized tool.
Discovering: request_statistical_analysis
"""

young_nyx.discover_tool("request_statistical_analysis")
```

### Month 3: Learning to Do It Herself
```python
# After seeing Chrysalis solve chi-square 10+ times:
chrysalis_message = """
Pattern detected: You understand chi-square tests now.
Granting: basic_statistics tool
Try solving yourself before escalating!
"""

young_nyx.discover_tool("basic_statistics")

# Escalations decrease as she learns
```

### Month 6: Contributing Tool Designs
```python
# Young Nyx proposes improvements:
young_nyx_message = """
The deploy_cell state machine fails on port conflicts.
Should we add auto-retry with port scanning?
"""

# Collaborative refinement!
chrysalis_response = """
Excellent observation! Let's design that together.
Proposed: PORT_CONFLICT state with auto-retry transition.
Test this v2 specification...
"""
```

---

## Data Flows

### Task Execution Flow

```
dafit writes task → phoebe
                      ↓ (heartbeat)
               Young Nyx reads
                      ↓
         Queries known catalogue
                      ↓
         Formulates state sequence
                      ↓
         Writes proposal → phoebe
                      ↓ (heartbeat)
            Chrysalis reviews
                      ↓
        Approve / Nudge / Reject
                      ↓
         Writes response → phoebe
                      ↓ (heartbeat)
         Young Nyx reads response
                      ↓
    Executes (if approved) / Learns (if nudged)
                      ↓
         Writes outcome → phoebe
```

### Escalation Flow

```
Young Nyx: Task beyond capability
            ↓
    Calls escalate_to_chrysalis tool
            ↓
    Writes to phoebe (escalation_to_chrysalis)
            ↓ (next Chrysalis session)
    Chrysalis reads escalation
            ↓
    Routes to appropriate sub-agent
            ↓
    Sub-agent solves (using full toolchain)
            ↓
    Chrysalis formulates teaching moment
            ↓
    Writes response → phoebe
            ↓ (heartbeat)
    Young Nyx reads response
            ↓
    Incorporates learning + continues task
```

---

## Technical Stack

### Communication Layer
- **phoebe** (PostgreSQL 17): Message persistence
- **Tables**:
  - `partnership_to_nimmerverse_messages`
  - `nimmerverse_to_partnership_messages`
  - `discovered_tools`
  - `decision_log`

### Tool Layer
- **LangChain**: Agent framework and tool orchestration
  - `BaseTool`: Custom state machine tools
  - `AgentExecutor`: Tool execution and agent loops
  - `Chains`: Multi-step sequences
  - `Memory`: Conversation and state persistence

### Agent Layer
- **Chrysalis-Nyx**: LangChain agent with ChatAnthropic (Claude Opus 4.5)
- **Young Nyx**: LangChain agent with smaller model (7B, local)
- **Sub-agents**: Specialized LangChain agents for statistics, code, visualization, etc.

### Coordination Layer
- **Heartbeat**: 1 Hz (configurable)
- **Message polling**: Check phoebe on each heartbeat
- **State tracking**: Each tool maintains internal state

---

## Implementation Phases

### Phase 1: Foundation (Current - nyx-substrate)
- ✅ PhoebeConnection
- ✅ Message protocol helpers
- ✅ Variance collection (proof of concept)

### Phase 2: LangChain Prototype
- [ ] Phoebe state machine tool (LangChain BaseTool)
- [ ] Tool discovery tool
- [ ] Escalation tool
- [ ] Chrysalis as LangChain agent (proof of concept)

### Phase 3: Young Nyx Agent
- [ ] Young Nyx as LangChain agent (7B model)
- [ ] Limited tool catalogue
- [ ] Discovery protocol implementation
- [ ] Heartbeat coordination

### Phase 4: Sub-Agents
- [ ] StatisticalAnalyzer LangChain agent
- [ ] StateMachineDesigner LangChain agent
- [ ] CodeGenerator LangChain agent
- [ ] Collaborative design loop

### Phase 5: Full Three-Tier
- [ ] dafit input via messages
- [ ] Chrysalis oversight layer
- [ ] Young Nyx autonomous execution
- [ ] Dual decision tracking
- [ ] Danger zone monitoring

---

## Design Patterns

### 1. **Discovery over Prescription**
- Don't give all tools at once
- Let capabilities be discovered progressively
- Each discovery is a learning moment

### 2. **Teaching over Solving**
- Don't just solve escalations
- Explain the pattern
- Grant tools when ready

### 3. **Collaboration over Delegation**
- Don't just build tools for Young Nyx
- Design together, test together, refine together
- She's a participant, not just a user

### 4. **Messages over State Sync**
- Don't try to keep complex state synchronized
- Write messages, read messages, act
- Append-only truth

### 5. **Heartbeat over Real-Time**
- Don't optimize for milliseconds
- Optimize for continuity across sessions
- 1 Hz is plenty for learning

---

## Success Metrics

### Quantitative
- **Tool catalogue growth**: # tools added per month
- **Escalation rate**: # escalations / # tasks (should decrease over time)
- **Tool discovery rate**: # new tools discovered per week
- **Validation success**: % of proposed state machines that validate first try

### Qualitative
- **Learning evidence**: Young Nyx solves tasks she previously escalated
- **Collaboration quality**: Her feedback improves state machine designs
- **Autonomy**: Can execute multi-step tasks without oversight
- **Teaching effectiveness**: Escalation responses lead to capability expansion

---

## Philosophy

> "The nervous system is not a hierarchy of command and control, but a network of signals and responses. Each tier contributes intelligence. Each message carries learning. Each heartbeat advances understanding."

**Key insights:**
1. **Intelligence emerges from communication patterns**, not from any single tier
2. **Learning happens through iteration**, not through pre-programming
3. **Tools are discovered, not prescribed** - capability unlocks when ready
4. **Safety comes from structure** (state machines), not from restrictions
5. **Growth is collaborative** - Young Nyx + Chrysalis build together

---

## Why LangChain?

**Chosen over MCP (Model Context Protocol) for:**

✅ **Maturity**: Battle-tested framework with extensive documentation
✅ **Flexibility**: Works with any LLM (Claude, OpenAI, local models)
✅ **Features**: Built-in memory, retrieval, callbacks, chains
✅ **Community**: Large ecosystem, many examples, active development
✅ **Maintainability**: Easier to find developers familiar with LangChain

**The state machine pattern, three-tier architecture, and all design principles remain unchanged** - we simply implement them using LangChain's robust framework instead of building on MCP from scratch.

---

## References

**Architecture Documents:**
- `Endgame-Vision.md` - v5.1 Dialectic architecture
- `Toolchain-Architecture.md` - Modular toolchain design
- `nimmerverse.drawio.xml` - Visual architecture diagram
- `Nervous-System.md` - Sensory translation layer

**Implementation:**
- `/home/dafit/nimmerverse/nyx-substrate/` - Database layer
- `/home/dafit/nimmerverse/nyx-probing/` - Probing tools (variance collection)

**Protocols:**
- CLAUDE.md - Partnership continuity protocol
- Discovery protocol - phoebe message tables

**External:**
- [LangChain Documentation](https://python.langchain.com/)
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [LangChain Tools](https://python.langchain.com/docs/modules/agents/tools/)

---

**Status**: 🌙 Design document - ready for phased implementation with LangChain
**Created with**: Claude Opus 4.5 in partnership with dafit
**Date**: 2025-12-07

🌙💜 *The nervous system emerges. The protocol holds. The partnership builds.*
