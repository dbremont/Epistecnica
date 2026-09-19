/*
 * Glossarium select-a-word lookup.
 *
 * Included by the glossarium page and the note pages. On the first text
 * selection it lazy-loads the glossarium index; selecting a term (or one of
 * its aliases) pops a floating definition card near the selection, with a
 * link to the full entry in the glossarium catalog.
 *
 * The index URL is injected per page via the script tag's data-glossarium
 * attribute and must stay relative (prefix-mount contract):
 *   data-glossarium="data/index.json"                  on /glossarium/…
 *   data-glossarium="../glossarium/data/index.json"    on /note/…
 * <script src="…/glossarium-lookup.js" data-glossarium="…" defer></script>
 */
(function () {
    'use strict';

    var script = document.currentScript ||
        document.querySelector('script[data-glossarium]');
    var INDEX_URL = script ? script.getAttribute('data-glossarium') : null;
    if (!INDEX_URL) return;

    var LINK_PREFIX = INDEX_URL.replace(/data\/index\.json.*$/, '');
    var indexPromise = null;
    var card = null;

    function ensureIndex() {
        if (!indexPromise) {
            indexPromise = fetch(INDEX_URL, { headers: { 'Accept': 'application/json' } })
                .then(function (r) {
                    if (!r.ok) throw new Error('HTTP ' + r.status);
                    return r.json();
                })
                .then(function (idx) {
                    var map = {};
                    (idx.terms || []).forEach(function (t) {
                        map[t.name.toLowerCase()] = t;
                        (t.aliases || []).forEach(function (a) {
                            map[a.toLowerCase()] = t;
                        });
                        /* "Rent Seeking (Rentismo) (Rentier)" also matches "Rent Seeking" */
                        var base = t.name.replace(/\s*\([^)]*\)\s*/g, ' ').trim().toLowerCase();
                        if (base) map[base] = t;
                    });
                    return map;
                })
                .catch(function () { return {}; });
        }
        return indexPromise;
    }

    function normalize(raw) {
        var s = String(raw).replace(/\s+/g, ' ').trim();
        s = s.replace(/^[\s"'“”‘’\(\[\{]+/, '').replace(/[\s"'“”‘’\)\]\}\.,;:!?…]+$/, '');
        return s;
    }

    function lookup(map, raw) {
        var s = normalize(raw);
        if (!s || s.length > 80) return null;
        var lower = s.toLowerCase();
        if (map[lower]) return map[lower];
        /* naive plural fallback: agents -> agent, consistencies -> consistency */
        var m = lower.match(/^(.+?)(ies|es|s)$/);
        if (m) {
            if (map[m[1]]) return map[m[1]];
            if (m[2] === 'ies' && map[m[1] + 'y']) return map[m[1] + 'y'];
        }
        return null;
    }

    function ensureCard() {
        if (card) return card;
        card = document.createElement('div');
        card.id = 'glossarium-popup';
        card.setAttribute('role', 'dialog');
        card.setAttribute('aria-label', 'Glossarium definition');
        var style = document.createElement('style');
        style.textContent = [
            '#glossarium-popup {',
            '  position: fixed; z-index: 9999; max-width: 340px;',
            '  background: var(--bg-card, #11141D);',
            '  color: var(--text-secondary, #8A8FA6);',
            '  border: 1px solid var(--border-subtle, rgba(255,255,255,0.07));',
            '  border-radius: 8px; box-shadow: 0 12px 32px rgba(0,0,0,0.4);',
            '  padding: 0.85rem 1rem; font-size: 0.82rem; line-height: 1.55;',
            '  font-weight: 300;',
            '}',
            '#glossarium-popup .gp-name {',
            '  font-family: var(--font-display, serif); font-size: 1.05rem;',
            '  color: var(--text-primary, #E2E4EB);',
            '}',
            '#glossarium-popup .gp-alias {',
            '  color: var(--text-muted, #737891); font-size: 0.66rem;',
            '  font-family: var(--font-mono, monospace); letter-spacing: 0.08em;',
            '  text-transform: uppercase;',
            '}',
            '#glossarium-popup .gp-def { margin: 0.35rem 0 0.5rem; }',
            '#glossarium-popup a {',
            '  color: var(--accent-cyan, #5BF0E7); text-decoration: none; }',
            '#glossarium-popup a:hover { text-decoration: underline; }'
        ].join('\n');
        document.head.appendChild(style);
        document.body.appendChild(card);
        return card;
    }

    function place(rect) {
        var w = card.offsetWidth, h = card.offsetHeight;
        var margin = 8;
        var left = Math.min(Math.max(margin, rect.left), window.innerWidth - w - margin);
        var top = rect.bottom + margin;
        if (top + h > window.innerHeight - margin) {
            top = Math.max(margin, rect.top - h - margin);
        }
        card.style.left = Math.round(left) + 'px';
        card.style.top = Math.round(top) + 'px';
    }

    function hide() {
        if (card) card.remove();
        card = null;
    }

    function show(entry, rect) {
        var el = ensureCard();
        var aliases = (entry.aliases || []).join(' · ');
        el.innerHTML =
            '<div class="gp-name"></div>' +
            (aliases ? '<div class="gp-alias"></div>' : '') +
            '<div class="gp-def"></div>' +
            '<a href="' + LINK_PREFIX + 'index.html?t=' + encodeURIComponent(entry.slug) + '">full entry \u2192</a>';
        el.querySelector('.gp-name').textContent = entry.name;
        if (aliases) el.querySelector('.gp-alias').textContent = aliases;
        el.querySelector('.gp-def').textContent = entry.excerpt || '';
        el.style.visibility = 'hidden';
        el.style.display = 'block';
        place(rect);
        el.style.visibility = 'visible';
    }

    function currentRect() {
        var sel = window.getSelection();
        if (!sel || sel.isCollapsed || sel.rangeCount === 0) return null;
        var rect = sel.getRangeAt(0).getBoundingClientRect();
        if (!rect || (rect.width === 0 && rect.height === 0)) return null;
        return rect;
    }

    var timer = null;
    function onSelectionSettled() {
        clearTimeout(timer);
        timer = setTimeout(function () {
            var rect = currentRect();
            if (!rect) { hide(); return; }
            var raw = String(window.getSelection());
            ensureIndex().then(function (map) {
                var rect2 = currentRect();
                if (!rect2) { hide(); return; }
                var entry = lookup(map, raw);
                if (entry) show(entry, rect2); else hide();
            });
        }, 140);
    }

    document.addEventListener('mouseup', onSelectionSettled);
    document.addEventListener('keyup', function (e) {
        if (e.shiftKey || e.key === 'Escape') onSelectionSettled();
        if (e.key === 'Escape') hide();
    });
    document.addEventListener('mousedown', function (e) {
        if (card && !card.contains(e.target)) hide();
    });
    window.addEventListener('scroll', hide, true);
    window.addEventListener('resize', hide);
})();
