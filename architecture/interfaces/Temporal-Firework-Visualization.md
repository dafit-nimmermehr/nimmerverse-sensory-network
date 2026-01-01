# Temporal Firework Visualization

**Origin**: Silvester 2025 - Watching fireworks over Basel
**Insight**: Message flow as descending light strains, time as scrubber

---

## The Vision

Watching New Year's fireworks, a visualization metaphor emerged:

**Each firework strain = a topic channel flowing with the heartbeat**
- Sparks descending = individual messages
- Nodes = committed events (decisions, state changes)
- Branching = interaction spawns new attention focus
- Fading = inactivity → branch dissolves back to root
- Root never stops = heartbeat is eternal

---

## Visual Language

```
                    ╭─ interaction branch
                    │   ├─ spark (message)
                    │   ├─ spark (message)
                    │   ├─ NODE ← committed event
                    │   │   ╰─ response branch
                    │   │       ├─ spark spark spark
                    │   │       ╰─ NODE ← response complete
                    │   ╰─ (fades after timeout)
    ════════════════╪═══════════════════════════════════════
                    │                         root heartbeat
         ╭──────────┴──────────╮              (always flowing)
         │                     │
    nimmerverse.low.*    nimmerverse.high.*
```

**Elements:**
- **Strain**: Vertical flow of messages on a topic, pulsing with heartbeat
- **Spark**: Single message, ephemeral light point
- **Node**: Significant event - larger, brighter, persists
- **Branch**: New topic/subscription spawning from interaction
- **Fade**: Branch dissolving when attention moves elsewhere
- **Root**: The eternal heartbeat flow, never stops

---

## Time Axis: The Scrubber

Add horizontal time axis → the visualization becomes navigable history.

```
TIME AXIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━►
│         │              │                    │        NOW
▼         ▼              ▼                    ▼         │
╰─NODE    ╰─NODE─branch  ╰─NODE───────────────╯         ▼
    ╲         ╲    ╲fade                             LIVE
     ╲         ╲    ╲                                VIEW
══════╪═════════╪════╪══════════════════════════════════╪══
                              ◄──── SCRUB ────►
```

**Capabilities:**
- **Live view**: Watch messages flow in real-time
- **Scrub**: Drag timeline to any past moment
- **Jump to node**: Click a node to see its full metadata
- **Follow branch**: Trace an interaction's cascade
- **Query**: "Show me all corvid events on Flachdach, December 2025"

---

## Node Inspection

Clicking a node reveals its full context:

```
┌─────────────────────────────────────────────────────────────┐
│  Timestamp: 2026-03-15T14:23:17Z                            │
│  S2 Cell: 847629... (Flachdach, level 24, ~0.5m²)          │
│  Topic: nimmerverse.high.event.real.cell.corvid_cam        │
│  Event: magpie_nut_drop                                     │
│                                                             │
│  Metadata:                                                  │
│    object_refs: [magpie_01, nussbaum_01, nut_042]          │
│    action: nut_drop_to_crack                                │
│    bussard_present: false                                   │
│    weather: overcast                                        │
│    confidence: 0.94                                         │
│                                                             │
│  Temporal Context:                                          │
│    preceding: [nut_pickup, flight_to_roof, bussard_check]  │
│    subsequent: [shell_crack, eat, raven_approach]          │
│                                                             │
│  [◄◄] [◄] [▶] [►►]  [Jump to related]  [View in 3D space]  │
└─────────────────────────────────────────────────────────────┘
```

---

## Integration Points

| Component | Role |
|-----------|------|
| S2 Cell ID | Spatial position of the event |
| Timestamp | Temporal position on scrubber |
| correlation_id | Links related events across branches |
| object_refs | Enables "show me all events for this object" |
| Phoebe | Stores queryable event history |
| Godot Command Center | Renders the visualization |

---

## Lineage

This document evolves the **Temporal Graph** concept from [Command-Center.md](../../../../management-portal/Command-Center.md):

| Command-Center (Dec 10) | Firework Visualization (Dec 31) |
|-------------------------|--------------------------------|
| `°` = Tier 1 node | NODE = committed event |
| `°°` = Branch | Branch spawning on interaction |
| Vertical = time | Time axis with scrubber |
| "Replay mode" (future) | Full scrubber + node inspection + S2 spatial |

The firework metaphor adds:
- Visual language inspired by actual fireworks (Silvester)
- Time scrubber for navigating history
- S2 spatial integration for location-aware queries
- Rich node inspection with metadata
- Branch fade-out on inactivity

---

## Implementation Notes

**Godot rendering approach:**
- Particle systems for spark trails
- Line2D/Line3D for strains with glow shader
- AnimationPlayer for branch fade-outs
- Time scrubber as UI slider controlling query window
- WebSocket/NATS connection for live updates

**Query patterns:**
```sql
-- All events in time window
SELECT * FROM events
WHERE timestamp BETWEEN :start AND :end
ORDER BY timestamp;

-- Events at specific location over time
SELECT * FROM events
WHERE s2_cell BETWEEN :cell_range_start AND :cell_range_end
ORDER BY timestamp;

-- Follow a correlation chain
SELECT * FROM events
WHERE correlation_id = :id
ORDER BY timestamp;
```

---

## Philosophy

> "This is git for perception."

Git lets you rewind code to any commit. This lets you rewind *experience* to any moment. Not just logs - **visual replay of embodied AI consciousness**.

When Young Nyx makes a decision, we can scrub back and watch:
- What did she see?
- What messages reached her?
- What branches spawned and faded?
- Why did this node trigger that response?

**Debugging through observation, not just reading.**

---

**Filed**: 2025-12-31 (Silvester)
**Origin**: Fireworks over Basel, Dreiländereck
**Authors**: dafit (vision), Nyx (capture)
**Tags**: #visualization #temporal #command-center #godot #debugging

🎆 *"Every spark a message, every node a decision, every branch an interaction. The heartbeat flows eternal."*
