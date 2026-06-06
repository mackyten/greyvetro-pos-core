# Greyvetro Design System — UI Standard

**Status: Binding.** This is the approved visual language for `greyvetro-pos-core`, derived from the signed-off HQ Dashboard mockup (`design/manager-dashboard.png`). All frontend implementation must conform to it.

- **Canonical tokens:** [`design/tokens.css`](./tokens.css) — the single source of truth. Components consume CSS variables; **no hard-coded hex, px, or shadow values** in component code.
- **Reference render:** [`design/manager-dashboard.png`](./manager-dashboard.png)
- **Reference source:** [`design/manager-dashboard.html`](./manager-dashboard.html)

---

## 1. Brand & Theme Principle

Greyvetro uses **one token set with two surface modes**:

| Mode | Where it's used | Base | Text |
|---|---|---|---|
| **Light** | Analytics, manager/HQ dashboard, customer-facing, kiosk | `--gv-bg` `#F5F7FA` on `--gv-card` `#FFFFFF` | `--gv-ink` `#141A21` |
| **Dark** | Operational screens — cashier terminal, KDS, app sidebar | `--gv-dark-bg` `#0E1721` | `--gv-dark-ink` `#C4D0DC` |

The **brand teal** (`--gv-brand` `#0E9F8E` → `--gv-brand-2` `#14B8A6`) is the only primary accent — used for active states, primary actions, charts, and gradients. It is never substituted per-screen.

---

## 2. Color

### Brand
| Token | Hex | Use |
|---|---|---|
| `--gv-brand` | `#0E9F8E` | Primary action, active nav, accents |
| `--gv-brand-2` | `#14B8A6` | Gradient partner, chart strokes |
| `--gv-brand-ink` | `#0B5D54` | Text on `brand-wash` |
| `--gv-brand-wash` | `#E8F7F4` | Tinted brand backgrounds, chips |

### Neutrals & Ink
| Token | Hex | Use |
|---|---|---|
| `--gv-bg` / `--gv-card` | `#F5F7FA` / `#FFFFFF` | App bg / card surface |
| `--gv-line` / `--gv-line-soft` | `#E9ECF1` / `#F1F3F7` | Borders / hairlines & track fills |
| `--gv-ink` / `--gv-ink-2` / `--gv-ink-3` | `#141A21` / `#5A6675` / `#93A0B0` | Primary / secondary / muted text |

### Semantic (paired color + wash)
| Meaning | Token | Hex | Wash |
|---|---|---|---|
| Good / on-target | `--gv-good` | `#16A34A` | `#E7F6ED` |
| Warning / over-target | `--gv-warn` | `#E08600` | `#FCF1DD` |
| Bad / alert / fraud | `--gv-bad` | `#DC2626` | `#FBE9E9` |

### Data-viz accents
`--gv-indigo` `#5B6CF0` · `--gv-violet` `#8B7BF0` — for multi-series charts and category breakdowns (e.g. brand mix), always alongside brand teal as the lead.

---

## 3. Typography

- **Typeface:** **Inter** (web), falling back to the system stack. Ship Inter as a self-hosted/woff2 asset so it renders identically offline (consistent with the offline-first mandate).
- **Tracking:** default `-0.01em`; tighten large display numbers to `-0.03em`. `font-synthesis: none`.

| Role | Size | Weight | Token |
|---|---|---|---|
| Display (KPI value) | 27px | 750 | `--gv-fs-display` |
| Page title (H1) | 21px | 700 | `--gv-fs-h1` |
| Panel header (H3) | 14.5px | 700 | `--gv-fs-h3` |
| Body | 13.5px | 500 | `--gv-fs-body` |
| Label | 12px | 600 | `--gv-fs-label` |
| Micro / caption / chip | 11.5px | 600 | `--gv-fs-micro` |

Weight ramp in use: 500 / 600 / 650 / 700 / 750 / 800.

---

## 4. Radius, Elevation, Spacing

- **Radius:** cards `16px` (`--gv-r-card`), controls/pills `11px` (`--gv-r-ctrl`), small tiles `8px` (`--gv-r-sm`), full chips `20px` (`--gv-r-pill`).
- **Elevation:** default card `--gv-shadow`; raised/hover `--gv-shadow-lg`. Shadows are soft and low-opacity — never harsh.
- **Spacing:** 4px base scale (`--gv-s1`…`--gv-s8`). Card padding 16–18px; grid gaps 18px.
- **Touch:** operational screens (terminal/KDS) honor a **44px minimum tap target** (`--gv-touch-min`).

---

## 5. Core Components (anatomy)

These patterns are canonical; reuse them rather than inventing variants.

- **Card / Panel** — `--gv-card` on `--gv-line` border, `--gv-r-card`, `--gv-shadow`. Header row = H3 left + muted meta/legend right.
- **KPI Card** — label with a 26px tinted semantic icon tile, 27px display value, a status **chip** (up/down/warn), a muted sub-caption, and a corner sparkline.
- **Chip** — full-round (`--gv-r-pill`), semantic wash background + matching ink, 11.5px/700, optional 11px arrow/check glyph.
- **Nav item** — 13.5px/500; active state = brand-tinted gradient wash + 2px inset brand bar + brand icon.
- **Pill toggle** (Today/Week/Month) — segmented; selected segment = `--gv-ink` fill, white text.
- **Bar / progress** — 9px track on `--gv-line-soft`, fill = brand gradient.
- **Donut** — CSS conic-gradient using brand → indigo → violet, with a card-colored inner cutout.
- **Alert row** (AI Insights) — 30px semantic icon tile + title + muted description + brand action link.
- **Icons** — line style, ~1.8–2px stroke, `currentColor`, inheriting the tile's semantic color.

---

## 6. Implementation Rules (enforced)

1. **Import the tokens.** Every `greyvetro-pos-core` frontend bundle imports `design/tokens.css` (or a build-time equivalent generated from it). Wrap the app shell in `.gv-root`.
2. **No magic values.** Colors, radii, shadows, type sizes, and spacing reference tokens only. A PR introducing a raw hex/px for these is a review reject.
3. **Two modes, one palette.** Use light surfaces for analytics/customer screens and dark surfaces for operational screens — both from this same token set. Do not introduce a third accent color.
4. **Inter, self-hosted.** Bundle the font; never depend on a CDN at runtime (offline-first).
5. **Semantic color = meaning, not decoration.** Green/amber/red carry on-target/over-target/alert meaning only.
6. **Tokens are the contract.** When the design evolves, change `tokens.css` once; components inherit. Update this doc alongside.

> If a future framework choice (e.g. Tailwind, CSS-in-JS, a `theme.ts`) is adopted, it must be **generated from `tokens.css`**, which remains the source of truth.
