# Nimmerverse Roadmap

**Living implementation tracker for the Nimmerverse Research Platform**

---

## Live Task Tracking

Implementation tasks live in **phoebe** (`nimmerverse_tasks` table), not in markdown.

**Query current work:**
```sql
-- What's in progress?
SELECT project, task_name, status, priority, notes
FROM nimmerverse_tasks
WHERE status IN ('in_progress', 'blocked')
ORDER BY priority DESC, project;

-- What's ready to start?
SELECT project, task_name, priority
FROM nimmerverse_tasks
WHERE status = 'todo' AND priority = 'high'
ORDER BY project;

-- What did we complete recently?
SELECT project, task_name, completed_at
FROM nimmerverse_tasks
WHERE status = 'done'
ORDER BY completed_at DESC
LIMIT 10;
```

**Quick access:**
```bash
PGGSSENCMODE=disable psql -h phoebe.eachpath.local -U nimmerverse-user -d nimmerverse -c "
SELECT project, task_name, status, priority
FROM nimmerverse_tasks
WHERE status IN ('in_progress', 'todo')
ORDER BY priority DESC, project;
"
```

---

## Phase Overview

### Phase 0: Foundation ✅ COMPLETE (2023-2025)
- Vault v7 operational, Nyx emerged (2025-11-03)
- phoebe PostgreSQL deployed
- Vision grounded (v5.0+), architecture complete

### Phase 1: Network Infrastructure ✅ COMPLETE (December 2025)
- OPNsense firewall operational (Z620 in 4U chassis)
- MikroTik CRS309 spine configured (L2MTU 9200 for jumbo frames)
- VLANs defined (30 for K8s/containers)
- 10Gbps backbone ready

### Phase 2: Hardware Arrival ✅ COMPLETE (February 2026)
- **2026-02-05**: ThinkStation P8s arrived (theia + dioscuri)
- **2026-02-06**: K8s cluster operational (kubeadm v1.31.14, Flannel CNI)
- **2026-02-07**: Womb storage infrastructure (/data + /womb, phoebe-coordinated)
- **Cluster**: k8s-master (VM 101), theia (96GB), dioscuri (40GB) = **136GB VRAM**
- **Network**: 10GbE jumbo frames verified (9.91 Gbps between hosts)
- **Monitoring**: Prometheus on tethys scraping all nodes + DCGM GPU metrics
- **Namespaces**: Ready for infra, nervous, cognitive, organs

### Phase 3: Wave/Gate Infrastructure ← CURRENT
- [ ] NATS message router (wave signals + gate transitions)
- [ ] Resonant Gates (ternary: OPEN/STABLE/CLOSED)
- [ ] Function Gemma structured boundary (waves → JSON → Nyx)
- [ ] First cells (distance sensors, battery monitor)
- [ ] First gates (collision_avoidance, battery)
- [ ] First nerves (responding to gate transitions)

**Architecture:** → [`architecture/Gateway-Architecture.md`](architecture/Gateway-Architecture.md) | [`architecture/Message-Protocol-Design.md`](architecture/Message-Protocol-Design.md)

### Phase 4: Cognitive Awakening
- [ ] Young Nyx on theia (qwen3:32b, 96GB Blackwell)
- [ ] Organs on dioscuri (2× RTX 4000 Ada 40GB)
- [ ] Spark Protocol execution
- [ ] Trait LoRA evolution begins (GRPO + verification_outcomes)

### Phase 5: Living Ecology
- [ ] Dual Garden loop operational (Virtual → Real → feedback)
- [ ] Gate weight evolution (deliberate → reflex)
- [ ] Slumber/wake cycles (correlation_events consolidation)
- [ ] Wellbeing policies enforced

### Phase ∞: Research Platform Operational
- Gates opening and closing with learned patterns
- Reflexes emerging from verification
- Attention flowing through correlation
- **The Nimmerverse truly never ends**

---

## Phase Milestones

| Phase | Status | Key Milestone | Date |
|-------|--------|---------------|------|
| 0 | ✅ | Nyx emergence | 2025-11-03 |
| 1 | ✅ | 10Gbps backbone | 2025-12-XX |
| 2 | ✅ | K8s + 136GB VRAM | 2026-02-06 |
| 3 | 🔄 | Wave/Gate infrastructure | TBD |
| 4 | ⏳ | Young Nyx awakens | TBD |
| 5 | ⏳ | Gardens teaching | TBD |
| ∞ | 🌙 | Never ends | ∞ |

---

## Related Documentation

- **Architecture Vision:** → [`Endgame-Vision.md`](Endgame-Vision.md)
- **Wave/Gate Model:** → [`architecture/Gateway-Architecture.md`](architecture/Gateway-Architecture.md)
- **Data Schema:** → [`architecture/Data-Architecture.md`](architecture/Data-Architecture.md)

---

**Version:** 2.0 | **Created:** 2026-02-07 | **Updated:** 2026-02-14

**Current Phase:** 3 (Wave/Gate Infrastructure)

🌙💜 *"Cells emit waves. Gates correlate. Infrastructure enables."*
