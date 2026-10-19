# Epistecnica — Shared Design System

The visual language used by the hub (`index.html`) and, with per-project
variations, by both subprojects. Source of truth for tokens and rules; the
per-project pages are the reference implementations.

## 1. Design philosophy

- **Editorial density:** high signal-to-noise. Whitespace is structural
  (dividers, padding), not decorative.
- **Epistemic layering:** a fixed structural background (the graph substrate)
  beneath a foreground of human-readable narrative and data.
- **System visibility:** the interface always communicates its state (time,
  schema version, load state) via peripheral monospaced metadata.

## 2. Color tokens

```css
--bg-void: #04050A;          /* deepest — page background            */
--bg-surface: #0B0D14;       /* elevated — panels, inputs            */
--bg-card: #11141D;          /* interactive — cards, chips           */
--text-primary: #E2E4EB;     /* headers                              */
--text-secondary: #8A8FA6;   /* body                                 */
--text-muted: #737891;       /* metadata / labels                    */
--accent-gold: #C5A467;      /* structural / narrative accents       */
--accent-gold-dim: rgba(197, 164, 103, 0.15);
--accent-cyan: #5BF0E7;      /* computational / active accents       */
--accent-cyan-dim: rgba(91, 240, 231, 0.1);
--border-subtle: rgba(255, 255, 255, 0.07);
```

- **Gold** for structural/narrative elements: borders, eyebrows, primary
  hovers, quotes.
- **Cyan** for computational/active elements: focus states, live data,
  highlights, links, metric values.
- **Borders:** `1px solid var(--border-subtle)` defines structure without
  visual weight. Avoid heavy shadows; use hairline borders and background
  shifts for elevation.

### Light theme

Dark is the brand's home and the default. Every page also carries a light
palette under `html[data-theme="light"]` — warm paper, slate text, and
darkened accents so contrast holds:

```css
html[data-theme="light"] {
  --bg-void: #F7F5F0;          /* warm paper                            */
  --bg-surface: #F1EEE7;       /* elevated                              */
  --bg-card: #FFFFFF;          /* interactive                           */
  --text-primary: #1A1D24;
  --text-secondary: #4A4F5E;
  --text-muted: #696E7D;       /* darkened for ≥4.5:1 on paper          */
  --accent-gold: #84682F;      /* darkened for ≥4.5:1 on paper          */
  --accent-gold-dim: rgba(132, 104, 47, 0.12);
  --accent-cyan: #0E7C72;      /* deep teal                             */
  --accent-cyan-dim: rgba(14, 124, 114, 0.08);
  --border-subtle: rgba(20, 22, 30, 0.10);
  --nav-bg: rgba(247, 245, 240, 0.85);
  --footer-bg: rgba(247, 245, 240, 0.75);
}
```

Mechanics (identical on every themed surface; the hub is the reference
implementation):

- `localStorage` key **`epistecnica-theme`** (`dark` | `light`), shared
  across surfaces — a choice made anywhere applies everywhere.
- A one-line inline `<head>` script applies the saved theme **before first
  paint** (no flash). No saved value → dark.
- The nav toggle (`◐ LIGHT/DARK`, showing the theme you'd switch to) swaps
  through a **curtain fade**: `body` fades out ~180 ms, `data-theme` flips
  while hidden, content fades back in. Guarded against re-clicks;
  `prefers-reduced-motion` swaps instantly. `html` carries
  `background: var(--bg-void)` so the reveal is always themed.
- The ambient constellation's dot/link colors follow the active theme.

## 3. Typography

Three typefaces establish a strict hierarchy between narrative, function, and
data:

| Role | Face | Use |
|------|------|-----|
| Display | Cormorant Garamond | page titles, narrative quotes, section headers; often italic |
| Body | Inter | explanatory paragraphs, standard UI text (300–600) |
| Mono | JetBrains Mono | metadata, data values, inputs, triggers; **uppercase** for labels, standard case for values |

Google Fonts link (offline-safe: pages still render with fallbacks):

```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
```

## 4. Layout & structure

- Content widths: standard reading `1000px`; wide system `1200px` (the hub).
  Corpus surfaces share the note-viewer page shell: `max-width: 1280px;
  margin: 0 auto; padding: 2.5rem 2rem 3.5rem` (`.layout`), so catalogs,
  viewers, docs, and live notes share one vertical rhythm.
- Structural dividers: `1px solid var(--border-subtle)`, horizontal and
  vertical.
- Narrative accent: a `1px solid var(--accent-gold)` left border isolates a
  quote or core concept.
- Grid matrices (dense data / navigation): `gap: 1px;
  background: var(--border-subtle)` on the container creates hairline grid
  borders between children — the hub's group lists use this.
- Section headers: mono index (`01`, `02`, …) + display title + hairline rule.
- Group-label variant (the hub's index): a display-italic lead-in question +
  hairline rule opens the section, followed by mono uppercase group labels
  (one per group), each marked up as a real heading inside a labelled
  `<section>`; groups sit in two columns split by a vertical hairline.

## 5. Generic component rules

- **Inputs:** mono font, `--bg-surface` background, `1px` subtle border; focus
  transitions border to `--accent-cyan` with a faint glow
  (`box-shadow: 0 0 15px rgba(91, 240, 231, 0.05)`). Never default browser
  outlines.
- **Data strips / metrics:** `Value` (mono, ~1.4–1.5rem, cyan) over `Label`
  (mono, ~0.6rem, muted, uppercase, letterspaced).
- **Interactive cells / cards:** `--bg-void` background; hover shifts to
  `--bg-surface`; active/selected shifts top border or text to `--accent-cyan`.
- **Chips / links:** mono, ~0.6–0.65rem, uppercase, `--bg-card` fill; hover
  adopts cyan text and border. Primary variant uses the gold border.
- **Primary navigation rows (the hub's index):** `--bg-void` cells in a
  hairline grid; a body-set name (`--text-primary`, ~1.05rem) in a fixed
  first column, a muted gloss in the flexible column, and a trailing mono
  arrow (`→` internal / `↗` external) pinned right. Hover **and**
  `:focus-within` shift the row to `--bg-surface`, the name/arrow to
  `--accent-cyan`, and nudge the arrow. Not the mono uppercase chip style.

## 6. Interaction & motion

- Hub entrance: labels and navigation rows enter via a `rise` keyframe —
  `opacity: 0; translateY(12px)` → `opacity: 1; translateY(0)`,
  `0.55s cubic-bezier(.22,1,.36,1)`, with a small per-row stagger.
- Scroll reveal (long-form / live pages): optional `.reveal` —
  `opacity: 0; translateY(20px)` → `opacity: 1; translateY(0)`, `0.8s ease-out`.
- Hover transitions: `0.3s ease`.
- Focus: `:focus-visible` → cyan outline (`1px`, offset ~3px) for
  links/buttons, or border-color shift + subtle glow for inputs. Never
  default browser outlines.

## 7. Atmospheric layer

Every page carries an **ambient canvas** as a fixed background
(`z-index: 0`, low opacity, `pointer-events: none`): a slow-moving
constellation of drifting points joined by fading proximity lines. It
reinforces the graph topology of the datasets without obstructing the UI or
reproducing actual data.

## 8. Voice

- Titles: sentence or fragment, quiet, no exclamation. Latin name + English
  gloss where apt (*Epistecnica — Epistemic & Technical Ontologies*).
- Labels/metadata: uppercase mono, letterspaced (`0.18–0.35em`).
- Metric emptiness: em dash `—` in muted/gold, never `0` or `N/A` invented.

## 9. Nav bar standard

Every surface's nav follows the hub (`index.html`), the reference
implementation. Do not invent per-page variants.

- **Left — brand lockup:** the graph mark (`img/mark-alpha.png`, ~26px, true
  transparency — never blend-mode tricks, never the raw black-backed
  masters) + the two-tone wordmark as **live typography** (`Episte` in
  `--text-primary`, `cnica` italic in `--accent-gold`). The lockup links
  to the hub (`/`). Never embed the wordmark as an image.
- **Right — the universal search, then the theme toggle** (`◐` + label
  showing the theme you'd switch to). Every surface — hub, docs, catalogs,
  viewers, and corpus live notes — carries the same search (one shared
  implementation: `src/app/shared/usearch.css` + `usearch.js`), with `/` to
  focus and `r` to open a random entry. Contextual page links live in the
  page body, not in the nav.
- Themes, persistence, boot script, and the curtain fade per §2.

Surfaces are one directory deep (`/note/`, …): reference shared root
assets relatively (`../img/mark-alpha.png`).
