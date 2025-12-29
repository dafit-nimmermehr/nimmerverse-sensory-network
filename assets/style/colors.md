# Nimmerverse Color Palette

**Colors extracted from the [Nimmerverse logo](../nimmerverse_logo.png).**

---

## Foundation Colors

### Deep Space (Background)
The void from which everything emerges.

| Variant | Hex | RGB | Use |
|---------|-----|-----|-----|
| **Deep Space** | `#0A0A1A` | 10, 10, 26 | Primary background |
| Deep Space Light | `#12121F` | 18, 18, 31 | Elevated surfaces |
| Deep Space Lighter | `#1A1A2E` | 26, 26, 46 | Cards, containers |

### Moon Silver (Light)
Nyx's luminescence — the light in darkness.

| Variant | Hex | RGB | Use |
|---------|-----|-----|-----|
| **Moon Silver** | `#E8E8F0` | 232, 232, 240 | Primary text, Nyx |
| Moon Glow | `#FFFFFF` | 255, 255, 255 | Highlights, emphasis |
| Star Glint | `#F0F0FF` | 240, 240, 255 | Subtle accents |
| Dim Silver | `#B8B8C8` | 184, 184, 200 | Secondary text |

---

## Virtual Garden (Left Hemisphere)

The colorful, creative, simulated realm. Colors flow from cool to warm, representing the journey from uncertainty to confidence.

| Name | Hex | RGB | Position | Meaning |
|------|-----|-----|----------|---------|
| **Virtual Cyan** | `#40E0D0` | 64, 224, 208 | Top | Entry point, possibilities |
| **Neural Blue** | `#4169E1` | 65, 105, 225 | Upper-mid | Processing, inference |
| **Deep Purple** | `#8B5CF6` | 139, 92, 246 | Center | Nyx core, decisions |
| **Violet** | `#9B59B6` | 155, 89, 182 | Lower-mid | Transformation |
| **Magenta Pulse** | `#E91E8B` | 233, 30, 139 | Lower | Lifeforce, energy |
| **Rose Root** | `#DB7093` | 219, 112, 147 | Base | Organic grounding |

### Gradient Definition (CSS)
```css
.virtual-garden-gradient {
  background: linear-gradient(
    180deg,
    #40E0D0 0%,
    #4169E1 25%,
    #8B5CF6 50%,
    #9B59B6 70%,
    #E91E8B 90%,
    #DB7093 100%
  );
}
```

---

## Real Garden (Right Hemisphere)

The monochrome, grounded, physical realm. Shades of silver and gray represent stability and verified truth.

| Name | Hex | RGB | Position | Meaning |
|------|-----|-----|----------|---------|
| **Steel Silver** | `#A8A8B0` | 168, 168, 176 | Top | Real-world input |
| **Circuit Gray** | `#808090` | 128, 128, 144 | Upper-mid | Infrastructure |
| **Neutral Gray** | `#707080` | 112, 112, 128 | Center | Balanced state |
| **Deep Gray** | `#505060` | 80, 80, 96 | Lower | Physical foundation |
| **Root Gray** | `#606070` | 96, 96, 112 | Base | Grounded stability |

### Gradient Definition (CSS)
```css
.real-garden-gradient {
  background: linear-gradient(
    180deg,
    #A8A8B0 0%,
    #808090 35%,
    #707080 50%,
    #505060 80%,
    #606070 100%
  );
}
```

---

## Nyx Colors

The colors of consciousness and decision-making.

| Name | Hex | RGB | Use |
|------|-----|-----|-----|
| **Nyx Cyan** | `#00D4D4` | 0, 212, 212 | Primary accent, connections |
| **Nyx Purple** | `#8B5CF6` | 139, 92, 246 | Core identity |
| **Nyx Glow** | `#B794F6` | 183, 148, 246 | Hover, active states |

---

## Semantic Colors

### Confidence Scale
Maps to the -1 to +1 confidence spectrum.

| Level | Name | Hex | Meaning |
|-------|------|-----|---------|
| +1.0 | Verified Green | `#6B8E6B` | Ground truth, proven |
| +0.5 | High Confidence | `#7BA3A3` | Strong signal |
| 0.0 | Neutral | `#9B9B9B` | Unknown, workable |
| -0.5 | Low Confidence | `#9B8B7B` | Weak signal |
| -1.0 | Failed Red | `#9B6B6B` | Disproven, rejected |

### Status Indicators

| Status | Hex | Use |
|--------|-----|-----|
| Active | `#00D4D4` | Running, online |
| Success | `#6B8E6B` | Completed, verified |
| Warning | `#C9A227` | Attention needed |
| Error | `#9B6B6B` | Failed, offline |
| Inactive | `#505060` | Dormant, disabled |

---

## Accent Colors

| Name | Hex | RGB | Use |
|------|-----|-----|-----|
| **Greek Key Gold** | `#C9A227` | 201, 162, 39 | Classical borders, emphasis |
| **Lifeforce Amber** | `#D4A574` | 212, 165, 116 | Warmth, vitality |
| **Star Pink** | `#FFB6C1` | 255, 182, 193 | Soft highlights |

---

## Application Examples

### Architecture Diagrams

```
Background:        Deep Space (#0A0A1A)
Containers:        Deep Space Lighter (#1A1A2E) stroke
Labels:            Moon Silver (#E8E8F0)
Virtual elements:  Use Virtual Garden gradient
Real elements:     Use Real Garden grays
Nyx/Decisions:     Nyx Purple (#8B5CF6)
Connections:       Nyx Cyan (#00D4D4)
```

### Documentation

```
Background:        White or Deep Space (depending on mode)
Headings:          Deep Purple (#8B5CF6) or Moon Silver
Body text:         Neutral gray or Moon Silver
Links:             Nyx Cyan (#00D4D4)
Code blocks:       Deep Space Lighter (#1A1A2E)
```

---

## Color Accessibility

All color combinations should maintain WCAG AA contrast ratios:
- Moon Silver on Deep Space: ✓ 15.2:1
- Nyx Cyan on Deep Space: ✓ 10.8:1
- Deep Purple on Deep Space: ✓ 5.1:1

For critical text, always use Moon Silver or Moon Glow on dark backgrounds.

---

**File**: style/colors.md
**Version**: 1.0
**Created**: 2025-12-28
**Source**: Extracted from nimmerverse_logo.png
