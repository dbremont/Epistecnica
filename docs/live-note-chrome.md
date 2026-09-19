# Live-note chrome — standardized container for `notes/live/`

Live notes (`src/note/app/notes/live/**.html`) are self-contained pages, but
they share the Epistecnica container so they read as part of the site. This
document holds the canonical copy-paste blocks (there is no shared runtime
file by design — each live note stays self-contained). When the chrome
changes, update it here and in every live note.

Design tokens live in the block below; they mirror `src/note/app/note.html`
and `spec/` (dark default + light via `epistecnica-theme`).

## Path prefixes

| Page location            | `ROOT` (site root)  | `NOTE` (catalog dir) |
|--------------------------|---------------------|----------------------|
| `notes/live/*.html`      | `../../../`         | `../../`             |
| `notes/live/*/*.html`    | `../../../../`      | `../../../`          |

## 1. `<head>` — theme init + fonts (before the page's `<style>`)

```html
<script>document.documentElement.dataset.theme = localStorage.getItem('epistecnica-theme') === 'light' ? 'light' : 'dark';</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
```

## 2. Tokens + chrome CSS (first rules inside the page's `<style>`)

```css
:root {
    --bg-void: #04050A;
    --bg-surface: #0B0D14;
    --bg-card: #11141D;
    --text-primary: #E2E4EB;
    --text-secondary: #8A8FA6;
    --text-muted: #737891;
    --accent-gold: #C5A467;
    --accent-cyan: #5BF0E7;
    --accent-cyan-dim: rgba(91, 240, 231, 0.1);
    --border-subtle: rgba(255, 255, 255, 0.07);
    --card-bg: rgba(11, 13, 20, 0.72);
    --nav-bg: rgba(4, 5, 10, 0.82);
    --footer-bg: rgba(4, 5, 10, 0.7);
    --font-display: 'Cormorant Garamond', serif;
    --font-body: 'Inter', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
}

html[data-theme="light"] {
    --bg-void: #F7F5F0;
    --bg-surface: #F1EEE7;
    --bg-card: #FFFFFF;
    --text-primary: #1A1D24;
    --text-secondary: #4A4F5E;
    --text-muted: #7A7F8E;
    --accent-gold: #9A7B3F;
    --accent-gold-dim: rgba(154, 123, 63, 0.12);
    --accent-cyan: #0E7C72;
    --accent-cyan-dim: rgba(14, 124, 114, 0.08);
    --border-subtle: rgba(20, 22, 30, 0.10);
    --card-bg: rgba(255, 255, 255, 0.72);
    --nav-bg: rgba(247, 245, 240, 0.85);
    --footer-bg: rgba(247, 245, 240, 0.75);
}

body { transition: opacity 180ms ease; }
html.theme-fading body { opacity: 0; }
@media (prefers-reduced-motion: reduce) { body { transition: none; } }

.site-nav {
    position: sticky;
    top: 0;
    z-index: 60;
    background: var(--nav-bg);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border-subtle);
}

/* Pages that have their own sticky/fixed section nav demote the brand bar: */
/* .site-nav { position: static; }                                          */

.site-nav .nav-inner {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0.95rem 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.site-nav .nav-brand {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    font-family: var(--font-display);
    font-size: 1.2rem;
    font-weight: 400;
    letter-spacing: 0.03em;
    color: var(--text-primary);
    text-decoration: none;
}

.site-nav .nav-mark { height: 26px; width: auto; }
.site-nav .nav-brand em { font-style: italic; color: var(--accent-gold); }
.site-nav .nav-right { display: flex; align-items: center; gap: 1.2rem; }

.site-nav .nav-links a {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--text-muted);
    text-decoration: none;
    transition: color 0.3s ease;
}

.site-nav .nav-links a:hover { color: var(--accent-cyan); }

.theme-toggle {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--text-secondary);
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    padding: 0.45rem 0.75rem;
    cursor: pointer;
    transition: color 0.3s ease, border-color 0.3s ease;
}

.theme-toggle:hover { color: var(--accent-cyan); border-color: var(--accent-cyan); }

.site-footer {
    border-top: 1px solid var(--border-subtle);
    background: var(--footer-bg);
    position: relative;
    z-index: 1;
}

.site-footer .foot-inner {
    max-width: 1280px;
    margin: 0 auto;
    padding: 1.5rem 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem 2rem;
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--text-muted);
}

.site-footer a { color: var(--text-muted); text-decoration: none; transition: color 0.3s ease; }
.site-footer a:hover { color: var(--accent-cyan); }
```

## 3. Nav (first element in `<body>`)

```html
<nav class="site-nav">
    <div class="nav-inner">
        <a class="nav-brand" href="ROOT"><img class="nav-mark" src="ROOTimg/mark-alpha.png" alt="">Episte<em>cnica</em></a>
        <div class="nav-right">
            <div class="nav-links"><a href="NOTEindex.html">Catalog</a></div>
            <button type="button" class="theme-toggle" id="themeToggle" aria-label="Switch color theme">◐ <span id="themeLabel">LIGHT</span></button>
        </div>
    </div>
</nav>
```

## 4. Footer (last element before the scripts)

```html
<footer class="site-footer">
    <div class="foot-inner">
        <div>Episte<em style="color:var(--accent-gold);font-style:italic">cnica</em> &middot; notes</div>
        <a href="NOTEindex.html">&larr; CATALOG</a>
    </div>
</footer>
```

## 5. Theme toggle + redraw hook (at the end of `<body>`)

Dispatches `epistecnica-theme` so pages with JS-drawn visuals (canvas/SVG)
can re-render in the new palette.

```html
<script>
(function () {
    var toggle = document.getElementById('themeToggle');
    var label = document.getElementById('themeLabel');
    var fading = false;
    function apply() {
        label.textContent = document.documentElement.dataset.theme === 'light' ? 'DARK' : 'LIGHT';
    }
    toggle.addEventListener('click', function () {
        if (fading) return;
        fading = true;
        var root = document.documentElement;
        var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        var swap = function () {
            root.dataset.theme = root.dataset.theme === 'light' ? 'dark' : 'light';
            try { localStorage.setItem('epistecnica-theme', root.dataset.theme); } catch (e) { /* private mode */ }
            apply();
            root.classList.remove('theme-fading');
            fading = false;
            window.dispatchEvent(new CustomEvent('epistecnica-theme'));
        };
        if (reduced) { swap(); return; }
        root.classList.add('theme-fading');
        setTimeout(swap, 190);
    });
    apply();
})();
</script>
```

## 6. JS-drawn colors

Canvas/SVG code must not hardcode palette colors. Read tokens at draw time:

```js
function themeColors() {
    var s = getComputedStyle(document.documentElement);
    return {
        primary: s.getPropertyValue('--text-primary').trim(),
        secondary: s.getPropertyValue('--text-secondary').trim(),
        muted: s.getPropertyValue('--text-muted').trim(),
        gold: s.getPropertyValue('--accent-gold').trim(),
        cyan: s.getPropertyValue('--accent-cyan').trim(),
        border: s.getPropertyValue('--border-subtle').trim(),
        surface: s.getPropertyValue('--bg-surface').trim(),
        card: s.getPropertyValue('--bg-card').trim()
    };
}
```

Listen for `epistecnica-theme` (section 5) and redraw when practical.

## Rules

- No CDN `<script>`/`<link>` tags — runtime dependencies are vendored under
  `src/note/app/vendor/` and referenced relatively (see below). Vanilla JS +
  Canvas2D/SVG otherwise; math helpers are a few stdlib lines.
- The page's own content, layout, and interactivity stay as authored; the
  container only wraps and tokenizes it.
- Keep `<title>` and the first `<h1>` stable — the notes catalog indexes them.
- No backend references in UI strings; pages fetch nothing at runtime.

## Vendored runtime dependencies

Runtime libraries live in `src/note/app/vendor/`, version-pinned, referenced
from live notes with a relative path (e.g. `../../vendor/alpine.min.js` from
`notes/live/*.html`). To add one: download the exact version, record its
size and sha256 in the commit message, reference it relatively, and list it
here.

| File                     | Version | Source                                    |
|--------------------------|---------|-------------------------------------------|
| `marked.min.js`          | (pinned)| markdown rendering (notes viewer)         |
| `alpine.min.js`          | 3.13.5  | `unpkg.com/alpinejs@3.13.5/dist/cdn.min.js` — reactive UI in live notes (`alpine:init` + `defer` pattern) |
