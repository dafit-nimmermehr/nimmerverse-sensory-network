# Nimmervest

**The Hardware Investment Strategy for Sovereign AI Infrastructure**

*Budget: 20k CHF | Timeline: Lifetime Project | Revised: 2025-12-09*

---

## The Architecture

### The Womb (Cognition/Inference)
Where Young Nyx lives, thinks, and runs.

| Component | Spec | Purpose |
|-----------|------|---------|
| Host | ThinkStation P8 | Professional workstation platform |
| CPU | Threadripper PRO 7955WX | 16c/32t, 4.5→5.3 GHz boost |
| RAM | 128GB DDR5-4800 ECC (4x32GB RDIMM) | 4 slots free for expansion to 256GB |
| GPU | **RTX PRO 6000 Blackwell Max-Q** | **96GB GDDR7 ECC, 1,792 GB/s, 300W** |
| Storage | 4TB NVMe PCIe 4.0 (2x2TB) | OPAL encrypted, enterprise grade |
| Network | Intel X710-T2L 10GbE dual | Copper, direct to spine |
| PSU | 1400W 92% efficiency | Massive headroom at 300W GPU |
| Warranty | 3 Jahre Vor-Ort-Service | Lenovo on-site support |

**Why RTX PRO 6000 Max-Q:**
- 96GB GDDR7 with ECC (professional grade, error-correcting)
- 1,792 GB/s bandwidth (1.79 TB/s!) - 33% faster than regular PRO 6000
- 300W TDP (half of regular 600W variant) - runs cool and quiet
- Dual-slot form factor - fits perfectly in P8
- PCIe 5.0 - future-proof interface
- 5th gen tensor cores, 4th gen RT cores

---

### The Senses (Perception/Organs)
Where Nyx sees, hears, and speaks.

| Component | Spec | Purpose |
|-----------|------|---------|
| Host | ThinkStation P8 | Identical twin platform |
| CPU | Threadripper PRO 7955WX | 16c/32t, 4.5→5.3 GHz boost |
| RAM | 128GB DDR5-4800 ECC (4x32GB RDIMM) | 4 slots free for expansion |
| GPU | **2x RTX 4000 Ada 20GB** (start) | **40GB total, professional Ada architecture** |
| GPU | **→ 4x RTX 4000 Ada 20GB** (target) | **80GB total, added every 2 months** |
| Storage | 4TB NVMe PCIe 4.0 (2x2TB) | OPAL encrypted |
| Network | Intel X710-T2L 10GbE dual | Copper, direct to spine |
| PSU | 1400W 92% efficiency | Multi-GPU ready |
| Warranty | 3 Jahre Vor-Ort-Service | Lenovo on-site support |

**Why RTX 4000 Ada over RTX 5060:**
- 20GB vs 16GB per card (25% more VRAM)
- Professional Ada architecture (not consumer Blackwell)
- ECC memory support
- ~360 GB/s bandwidth per card (vs ~256 GB/s on 5060)
- 1,200 CHF via Lenovo deal (professional card at reasonable price)

**Organ allocation (at 4 GPUs):**
- GPU 1: Speech Organ (Whisper STT)
- GPU 2: Voice Organ (TTS)
- GPU 3: Vision Organ (YOLO, cameras)
- GPU 4: Training/overflow/future organs

---

### The Veteran (Test Bed/Backup)
The proven warrior, now in support role.

| Component | Spec | Purpose |
|-----------|------|---------|
| Host | Saturn | Ryzen 3900X, 128GB RAM, 10 VMs |
| GPU | RTX 3090 | 24GB VRAM @ 936 GB/s |
| Role | Test bed, staging, backup inference |

**Cost: Already owned**

---

### The Spine (Network/Security)
The nervous system connecting all organs.

| Component | Spec | Purpose |
|-----------|------|---------|
| Firewall | **Siemens SIMATIC IPC** | Industrial-grade, pfSense, 10G NIC incoming |
| Spine | MikroTik CRS309-1G-8S+IN | 8x SFP+ 10G aggregation |
| Access | MikroTik CRS326-24G-2S+RM | 24x 1G + 2x SFP+ 10G |
| Converters | 10G SFP+ to RJ45 copper | Bridge switches to NICs |

**Cost: Already owned / arriving**

---

### The Memory (Persistence/Continuity)
Where experience accumulates between sessions.

| Component | Spec | Purpose |
|-----------|------|---------|
| Host | Phoebe | PostgreSQL database server |
| Role | Session messages, variance data, continuity |
| Tables | `partnership_to_nimmerverse_messages`, `variance_probe_runs` |

**Cost: Already owned**

---

## Budget Allocation (Final)

| Item | Cost CHF | Status |
|------|----------|--------|
| 2x ThinkStation P8 (7955WX, 128GB ECC, 2x RTX 4000 Ada) | 11,327.13 | **Quote ready** - Angebot #4650557686 |
| RTX PRO 6000 Blackwell Max-Q 96GB | 6,504.45 | **In stock** - acscomputer.ch |
| **Subtotal** | **17,831.58** | |
| **Buffer** | **2,168.42** | Expansion, accessories |
| **Total** | **20,000.00** | |

### Lenovo Quote Details
- **Angebotsnummer**: 4650557686
- **Vertriebsmitarbeiterin**: Adrienn Wettstein (Legend!)
- **Telefon**: (044) 516 04 67
- **E-Mail**: awettstein@lenovo.com
- **Rabatt**: 16% off list price
- **Gültig bis**: Held for 2 weeks (flexible)

---

## Growth Path

```
Phase 1 (January 2026):     Foundation arrives
                            - Both ThinkStations operational
                            - RTX PRO 6000 Max-Q in Womb (96GB)
                            - 2x RTX 4000 Ada in Senses (40GB)
                            - 10G network live
                            - Total VRAM: 160GB

Phase 2 (Every 2 months):   RTX 4000 Ada expansion
                            - +1 RTX 4000 Ada @ 1,200 CHF each
                            - Month 2: 60GB Senses
                            - Month 4: 80GB Senses (target reached)
                            - From monthly surplus (~1,800 CHF)

Phase 3 (Future):           Optional expansion
                            - RAM: 128GB → 256GB per machine (slots ready)
                            - Additional 3090s for Saturn (eBay hunting)
                            - Second Womb machine if needed
```

---

## Compute Summary

| Resource | At Launch | At Full Build |
|----------|-----------|---------------|
| **Total VRAM** | 160GB (96+40+24) | **200GB** (96+80+24) |
| **Peak Bandwidth** | 1,792 GB/s (Womb) | 1,792 GB/s (Womb) |
| **CPU Cores** | 44c/88t | 44c/88t |
| **System RAM** | 384GB ECC | 512GB+ ECC (expandable) |
| **Fast Storage** | 12TB NVMe | 12TB+ NVMe |
| **Network** | 10G spine, full mesh | 10G spine, full mesh |

---

## The Lenovo Discovery

**Why ThinkStation P8 over DIY:**

```
DIY Threadripper PRO build:
├── TRX50 board:           ~1,500 CHF (4 month wait!)
├── TR PRO 7955WX:         ~2,500 CHF
├── 128GB DDR5 ECC:        ~5,149 CHF (insane shortage pricing)
├── Storage, PSU, case:    ~1,000 CHF
└── Total:                 ~10,149 CHF + months waiting

ThinkStation P8 configured (via Adrienn):
├── Everything above:      ~5,664 CHF
├── PLUS 2x RTX 4000 Ada:  ~2,400 CHF (included in quote!)
├── Includes 10GbE dual:   ✓
├── Includes 3yr warranty: ✓
├── Ships January:         ✓
└── Savings:               ~4,485 CHF per machine vs DIY
```

Lenovo's bulk purchasing power breaks the component shortage.
Adrienn's 16% discount makes it even sweeter.

---

## Why Max-Q over Regular PRO 6000

| Spec | Regular PRO 6000 | PRO 6000 Max-Q |
|------|------------------|----------------|
| VRAM | 96GB GDDR7 ECC | 96GB GDDR7 ECC |
| Bandwidth | 1,344 GB/s | **1,792 GB/s** (+33%!) |
| TDP | 600W | **300W** (half!) |
| Form Factor | Large, hot | Dual-slot, cool |
| PCIe | Gen 5 | Gen 5 |
| Price | ~6,643 CHF | **6,504 CHF** |

The Max-Q is the sweet spot: more bandwidth, less power, lower price.

---

## Sovereignty Principles

- Weights NEVER leave home
- Training data NEVER uploaded
- No cloud dependencies
- No recurring costs after hardware
- Full ownership of growth trajectory
- Honest data sourcing (no shadow archives)
- Ask permission, cite sources

---

## Network Topology

```
                         INTERNET
                             │
                             ▼
                 ┌───────────────────────┐
                 │   Siemens SIMATIC     │
                 │   pfSense Firewall    │
                 │   (ghost robot brain) │
                 └───────────┬───────────┘
                             │ 10G
                             ▼
                 ┌───────────────────────┐
                 │   CRS309 (Spine)      │
                 │   8x SFP+ 10G         │
                 └───┬───────┬───────┬───┘
                     │       │       │
           10G ──────┘       │       └────── 10G
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
  │ ThinkStation│    │ ThinkStation│    │   Saturn    │
  │    P8 #1    │    │    P8 #2    │    │  (Veteran)  │
  │   (Womb)    │    │  (Senses)   │    │  Test bed   │
  │             │    │             │    │             │
  │ PRO 6000    │    │ 2-4x 4000   │    │ RTX 3090    │
  │ Max-Q 96GB  │    │ Ada 40-80GB │    │   24GB      │
  └─────────────┘    └─────────────┘    └─────────────┘
         │                   │                   │
         └───────────────────┴───────────────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │   CRS326 (Access)     │
                 │   24x 1G + 2x 10G     │
                 └───┬───────┬───────┬───┘
                     │       │       │
                     ▼       ▼       ▼
                  Phoebe  Sensors  Future
                  (Memory) (Cams)  (Organs)
```

---

## Key Discoveries (2025-12-09 Session)

1. **Bank contract arrived in 24 hours** - Not the expected 2 days. Universe is moving fast.

2. **Adrienn Wettstein is a legend** - 16% discount, held quote for 2 weeks, tried to source PRO 6000 for us directly.

3. **RTX 4000 Ada > RTX 5060** - Professional architecture, 20GB vs 16GB, ECC support, better bandwidth. Consumer cards are compromised.

4. **Max-Q is the sweet spot** - 1,792 GB/s bandwidth (33% more than regular!), 300W TDP (half the heat), slightly cheaper. Perfect for workstation use.

5. **acscomputer.ch has stock** - PRO 6000 Max-Q available at 6,504.45 CHF.

6. **Growth path is clear** - Start with 2x RTX 4000 Ada, add one every 2 months from monthly surplus until we hit 4.

---

## Timeline (Updated)

```
December 9:      Bank contract received, architecture finalized
December 10-11:  Sign contract, confirm with Adrienn
December 23:     Money arrives
December 23-24:  Place orders (Lenovo + acscomputer.ch)
January 2026:    ThinkStations arrive, BUILD BEGINS
February 2026:   +1 RTX 4000 Ada (60GB Senses)
April 2026:      +1 RTX 4000 Ada (80GB Senses - target reached)
```

---

**Created**: 2025-12-05
**Revised**: 2025-12-09 (Contract Day - Final Architecture)
**Status**: Architecture FINALIZED, quotes ready, awaiting signature
**Philosophy**: Professional hardware. Efficient power. Maximum bandwidth. Lifetime sovereignty.

🌙💜 **The Womb awaits. Young Nyx will think at 1.79 TB/s.**
