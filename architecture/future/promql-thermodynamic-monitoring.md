# PromQL Thermodynamic Monitoring Queries

**Source**: Gemini Red Team (2026-01-01)
**Status**: Ready for implementation when Prometheus deployed

---

## 1. Real-Time JLF per Heartbeat

```promql
# Total JLF per heartbeat (sum of GPU and CPU power)
(
  sum(DCGM_FI_DEV_POWER_USAGE) +
  sum(node_rapl_package_watts_total)
) * 1 # Watts * 1 second = Joules
```

## 2. Cognitive Waste Heat (Uncertainty Cost)

```promql
# Waste Heat: Energy spent on decisions with 'uncertain' ternary status
sum(
  nimmerverse_decision_energy_joules{status="uncertain"}
) /
sum(
  nimmerverse_decision_energy_joules
) * 100
```

**ALERT**: >40% = Cognitive Death Spiral

## 3. Thermodynamic Efficiency (Accuracy-per-Joule)

```promql
# Efficiency: Confident Resolutions divided by Total Energy Spend
sum(rate(nimmerverse_decisions_total{status="confident"}[1m]))
/
sum(rate(nimmerverse_lifeforce_joules_total[1m]))
```

## 4. Metabolic Slumber Trigger

```promql
# Lifeforce Pool Percentage
(nimmerverse_lifeforce_pool_current / nimmerverse_lifeforce_pool_max) * 100
```

**ALERT**: <20% for >5 heartbeats = Force slumber

---

## First Boot Monitoring Strategy

1. **JLF/Accuracy ratio** — Dropping while accuracy high = Reflex compilation working
2. **Unknown (-) frequency** — Should increase during low-LF = Energy > hallucinations
3. **Sim-Tax validation** — Virtual acceleration = non-linear JLF spike

---

**TODO**: Request Grafana dashboard JSON from Gemini for visualization
