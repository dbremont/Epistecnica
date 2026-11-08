/* Epistecnica — tree catalog viewer.
 *
 * The corpus-tree presentation of /tree.html, applied to a taxonomy:
 * a sticky collapsible tree on the left, a detail viewer on the right.
 * Selecting a node renders that node's detail; non-leaf nodes also list
 * their children so the pane can be used to drill down.
 *
 *   TreeCatalog.mount('#treeCatalog', {
 *       rootLabel: 'HS 2022',
 *       nodes: [{ id, label, parent, level, ... }],
 *       searchPlaceholder: 'Search code or description…',
 *       detail: {
 *           code:  function (n) { return n.code; },
 *           body:  function (n) { return '<h4>Description</h4><p>…</p>'; },
 *           chips: function (n) { return ['section', 'chapter']; }
 *       }
 *   });
 *
 * The page owns the design tokens (--bg-void, --accent-gold, …); this file
 * injects the layout, the nav/masthead/footer chrome and the tree styles.
 */
(function (global) {
    'use strict';

    var CSS = [
        /* ---------- page chrome (nav, masthead, footer) ---------- */
        '.nav{position:sticky;top:0;z-index:10;background:var(--nav-bg);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--border-subtle);}',
        '.nav-inner{max-width:1400px;margin:0 auto;padding:.95rem 2rem;display:flex;align-items:center;justify-content:space-between;gap:1rem;}',
        '.nav-brand{display:inline-flex;align-items:center;gap:.55rem;font-family:var(--font-display);font-size:1.2rem;font-weight:400;letter-spacing:.03em;color:var(--text-primary);text-decoration:none;}',
        '.nav-mark{height:26px;width:auto;}',
        '.nav-brand em{font-style:italic;color:var(--accent-gold);}',
        '.nav-right{display:flex;align-items:center;gap:.8rem;}',
        '.theme-toggle{font-family:var(--font-mono);font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;color:var(--text-secondary);background:var(--bg-card);border:1px solid var(--border-subtle);padding:.45rem .75rem;cursor:pointer;transition:color .3s ease,border-color .3s ease;}',
        '.theme-toggle:hover{color:var(--accent-cyan);border-color:var(--accent-cyan);}',
        '.masthead{max-width:1400px;margin:0 auto;padding:1.6rem 2rem 0;}',
        '.crumbs{font-family:var(--font-mono);font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;color:var(--text-muted);margin-bottom:1rem;}',
        '.crumbs a{color:var(--text-muted);text-decoration:none;}',
        '.crumbs a:hover{color:var(--accent-cyan);}',
        '.crumbs .sep{margin:0 .5em;opacity:.5;}',
        '.crumbs .here{color:var(--accent-gold);}',
        '.note-title{font-family:var(--font-display);font-weight:300;font-size:clamp(1.8rem,3.6vw,2.6rem);line-height:1.1;padding-bottom:.8rem;border-bottom:1px solid var(--border-subtle);}',
        '.subtitle{color:var(--text-secondary);margin:.85rem 0 0;max-width:88ch;line-height:1.6;font-size:.88rem;}',
        '.subtitle a{color:var(--accent-cyan);}',
        '.page-foot{max-width:1400px;margin:2.4rem auto 0;padding:1rem 2rem 2rem;border-top:1px solid var(--border-subtle);color:var(--text-muted);font-size:.7rem;line-height:1.6;}',
        '.page-foot a{color:var(--text-secondary);}',
        '.page-foot code{font-family:var(--font-mono);font-size:.66rem;}',

        /* ---------- shell ---------- */
        '.tc-shell{display:grid;grid-template-columns:300px minmax(0,1fr);gap:2.5rem;max-width:1400px;margin:0 auto;padding:1.6rem 2rem 3rem;}',
        '.tc-tree{position:sticky;top:4.2rem;align-self:start;max-height:calc(100vh - 5.5rem);overflow:auto;border-right:1px solid var(--border-subtle);padding-right:1rem;}',
        '.tc-tree h2,.tc-content h2{font-family:var(--font-mono);font-size:.62rem;font-weight:400;letter-spacing:.22em;text-transform:uppercase;color:var(--accent-gold);margin-bottom:.8rem;}',
        '.tc-tools{display:flex;gap:.35rem;margin-bottom:.7rem;}',
        '.tc-tools button{flex:1;border:1px solid var(--border-subtle);background:transparent;color:var(--text-muted);font-family:var(--font-mono);font-size:.54rem;letter-spacing:.1em;text-transform:uppercase;padding:.3rem .2rem;border-radius:3px;cursor:pointer;}',
        '.tc-tools button:hover{color:var(--accent-cyan);border-color:var(--accent-cyan);}',
        '.tc-q{width:100%;margin-bottom:.7rem;font-family:var(--font-mono);font-size:.68rem;color:var(--text-primary);background:var(--bg-surface);border:1px solid var(--border-subtle);padding:.4rem .55rem;border-radius:3px;outline:none;}',
        '.tc-q:focus{border-color:var(--accent-cyan);}',
        '.tc-tree details{margin-bottom:.15rem;}',
        '.tc-tree details[hidden]{display:none;}',
        '.tc-tree details>summary{cursor:pointer;list-style:none;display:flex;align-items:baseline;gap:.4rem;padding:.28rem .4rem;border-radius:3px;color:var(--text-secondary);font-size:.8rem;}',
        '.tc-tree details>summary::-webkit-details-marker{display:none;}',
        '.tc-tree details>summary:hover{background:var(--bg-surface);color:var(--text-primary);}',
        '.tc-tree .tw{color:var(--accent-gold);font-family:var(--font-mono);font-size:.6rem;width:.7rem;flex:0 0 .7rem;}',
        '.tc-tree details[open]>summary .tw{transform:rotate(90deg);display:inline-block;}',
        '.tc-tree details[data-haskids="0"]>summary .tw{visibility:hidden;}',
        '.tc-name{cursor:pointer;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}',
        '.tc-name:hover{color:var(--accent-cyan);}',
        '.tc-name.active{color:var(--accent-cyan);font-weight:500;}',
        '.tc-count{color:var(--text-muted);font-family:var(--font-mono);font-size:.66rem;}',
        '.tc-kids{margin-left:.75rem;border-left:1px solid var(--border-subtle);padding-left:.35rem;}',
        '.tc-content{min-width:0;}',

        /* ---------- detail ---------- */
        '.tc-head{display:flex;justify-content:space-between;align-items:baseline;gap:1rem;flex-wrap:wrap;margin-bottom:1.2rem;}',
        '.tc-head h1{font-family:var(--font-display);font-size:clamp(1.7rem,3vw,2.2rem);font-weight:400;line-height:1.15;}',
        '.tc-head p{color:var(--text-muted);font-size:.72rem;font-family:var(--font-mono);margin-top:.35rem;overflow-wrap:anywhere;}',
        '.tc-detail{border:1px solid var(--border-subtle);border-radius:8px;background:var(--bg-card);padding:1.1rem 1.2rem 1.3rem;margin-bottom:1.6rem;}',
        '.tc-detail .code{font-family:var(--font-mono);font-size:.78rem;color:var(--accent-cyan);}',
        '.tc-chips{display:flex;flex-wrap:wrap;gap:.35rem;margin:.55rem 0 .2rem;}',
        '.tc-chip{font-family:var(--font-mono);font-size:.55rem;letter-spacing:.08em;text-transform:uppercase;border:1px solid var(--border-medium);border-radius:999px;padding:.14rem .5rem;color:var(--text-secondary);}',
        '.tc-detail h4{font-family:var(--font-mono);font-size:.58rem;letter-spacing:.12em;text-transform:uppercase;color:var(--text-muted);margin:.9rem 0 .3rem;}',
        '.tc-detail p{color:var(--text-secondary);font-size:.84rem;line-height:1.6;white-space:pre-wrap;}',
        '.tc-detail a{color:var(--accent-cyan);}',

        /* ---------- lists ---------- */
        '.tc-list{border-top:1px solid var(--border-subtle);}',
        '.tc-item{display:grid;grid-template-columns:1.8rem minmax(0,1fr) auto;gap:1rem;align-items:baseline;padding:.7rem .4rem;border-bottom:1px solid var(--border-subtle);cursor:pointer;background:none;border-left:0;border-right:0;border-top:0;width:100%;text-align:left;color:inherit;font:inherit;}',
        '.tc-item:hover{background:var(--bg-surface);}',
        '.tc-badge{display:inline-flex;align-items:center;justify-content:center;width:1.55rem;height:1.35rem;border:1px solid var(--border-subtle);border-radius:2px;color:var(--text-muted);font-family:var(--font-mono);font-size:.5rem;flex-shrink:0;}',
        '.tc-item-title{font-size:.92rem;color:var(--text-primary);}',
        '.tc-item-sub{display:block;margin-top:.12rem;font-family:var(--font-mono);font-size:.66rem;color:var(--text-muted);}',
        '.tc-item-tag{font-family:var(--font-mono);font-size:.62rem;color:var(--text-muted);text-align:right;}',
        '.tc-empty{color:var(--text-muted);padding:2rem 0;font-style:italic;}',
        '.tc-more{font-family:var(--font-mono);font-size:.56rem;letter-spacing:.12em;text-transform:uppercase;color:var(--text-muted);margin:1.4rem 0 .8rem;}',

        '@media (max-width:900px){.nav-inner,.masthead,.tc-shell,.page-foot{padding-left:1.2rem;padding-right:1.2rem;}.tc-shell{grid-template-columns:1fr;gap:1.4rem;}.tc-tree{position:static;max-height:46vh;border-right:0;border-bottom:1px solid var(--border-subtle);padding:0 0 1rem;}.tc-item{grid-template-columns:1.8rem minmax(0,1fr);}.tc-item-tag{display:none;}}'
    ].join('\n');

    function injectCSS() {
        if (document.getElementById('tc-style')) return;
        var s = document.createElement('style');
        s.id = 'tc-style';
        s.textContent = CSS;
        document.head.appendChild(s);
    }

    function esc(s) {
        return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
            return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
        });
    }

    function fmt(n) { return Number(n || 0).toLocaleString(); }

    function mount(target, cfg) {
        injectCSS();
        cfg = cfg || {};
        var host = typeof target === 'string' ? document.querySelector(target) : target;
        if (!host) return null;

        /* ---------- model ---------- */
        var list = [], byId = {}, kids = {}, roots = [];
        (cfg.nodes || []).forEach(function (raw) {
            var id = String(raw.id);
            if (byId[id]) return;
            var parent = (raw.parent === null || raw.parent === undefined || raw.parent === '') ? null : String(raw.parent);
            var rec = {
                id: id,
                label: String(raw.label || raw.title || id),
                parent: parent,
                level: String(raw.level || ''),
                raw: raw
            };
            list.push(rec);
            byId[id] = rec;
        });
        list.forEach(function (n) {
            if (n.parent && byId[n.parent]) (kids[n.parent] = kids[n.parent] || []).push(n.id);
            else roots.push(n.id);
        });

        var COUNT = {};
        function count(id) {
            if (COUNT[id] !== undefined) return COUNT[id];
            var c = 1, ch = kids[id] || [], i;
            for (i = 0; i < ch.length; i++) c += count(ch[i]);
            COUNT[id] = c;
            return c;
        }
        list.forEach(function (n) { count(n.id); });

        var detail = cfg.detail || {};
        function codeOf(n) { return detail.code ? (detail.code(n.raw) || '') : ''; }
        function bodyOf(n) { return detail.body ? (detail.body(n.raw) || '') : ''; }
        function chipsOf(n) {
            var out = detail.chips ? (detail.chips(n.raw) || []).slice() : [];
            if (!detail.chips && n.level) out.push(n.level);
            var ch = (kids[n.id] || []).length;
            if (ch) out.push(ch + (ch === 1 ? ' child' : ' children'));
            out.push(count(n.id) + (count(n.id) === 1 ? ' node' : ' nodes'));
            return out;
        }
        function pathOf(id) {
            var out = [], n = byId[id];
            var byCode = detail.pathStyle === 'code';
            while (n) {
                out.unshift(byCode ? (codeOf(n) || n.label) : n.label);
                n = n.parent ? byId[n.parent] : null;
            }
            return out;
        }

        /* ---------- shell ---------- */
        host.innerHTML =
            '<div class="tc-shell">' +
                '<aside class="tc-tree">' +
                    '<h2>' + esc(cfg.rootLabel || 'Taxonomy') + '</h2>' +
                    '<div class="tc-tools">' +
                        '<button type="button" data-act="top">top</button>' +
                        '<button type="button" data-act="expand">expand</button>' +
                        '<button type="button" data-act="collapse">collapse</button>' +
                    '</div>' +
                    '<input class="tc-q" type="search" placeholder="' + esc(cfg.searchPlaceholder || 'Search…') + '" autocomplete="off" aria-label="Filter the tree">' +
                    '<div class="tc-tree-body"></div>' +
                '</aside>' +
                '<section class="tc-content">' +
                    '<div class="tc-head"><div><h1 class="tc-title"></h1><p class="tc-meta"></p></div></div>' +
                    '<div class="tc-body"></div>' +
                '</section>' +
            '</div>';

        var treeEl = host.querySelector('.tc-tree-body');
        var titleEl = host.querySelector('.tc-title');
        var metaEl = host.querySelector('.tc-meta');
        var bodyEl = host.querySelector('.tc-body');
        var qEl = host.querySelector('.tc-q');

        var T = {};                 /* id -> built tree record */
        var OPEN = {}, CLOSED = {};
        var SELECTED = null;
        var QUERY = '';
        var MATCH = {}, HIT = {};
        var BUILT = false;

        /* ---------- tree ---------- */
        function makeNode(id, depth) {
            if (T[id]) return T[id].el;
            var n = byId[id];
            if (!n) return null;
            var el = document.createElement('details');
            el.dataset.id = id;
            el.dataset.haskids = (kids[id] || []).length ? '1' : '0';

            var summary = document.createElement('summary');
            var tw = document.createElement('span');
            tw.className = 'tw';
            tw.textContent = '\u25b8';
            var name = document.createElement('span');
            name.className = 'tc-name';
            name.textContent = n.label;
            var cnt = document.createElement('span');
            cnt.className = 'tc-count';
            cnt.textContent = fmt(count(id));
            summary.appendChild(tw);
            summary.appendChild(name);
            summary.appendChild(cnt);
            el.appendChild(summary);

            var box = document.createElement('div');
            box.className = 'tc-kids';
            el.appendChild(box);

            T[id] = {
                el: el, nameEl: name, countEl: cnt, box: box,
                depth: depth, built: false, open: false, hidden: false, active: false, count: null
            };

            name.addEventListener('click', function (ev) {
                ev.preventDefault();
                ev.stopPropagation();
                select(id, true);
            });
            el.addEventListener('toggle', function () {
                if (el.open) { delete CLOSED[id]; OPEN[id] = true; fill(id); }
                else { OPEN[id] = false; CLOSED[id] = true; }
                T[id].open = el.open;
            });
            return el;
        }

        function fill(id) {
            var rec = T[id];
            if (!rec || rec.built) return;
            rec.built = true;
            var frag = document.createDocumentFragment();
            (kids[id] || []).forEach(function (kid) {
                var el = makeNode(kid, rec.depth + 1);
                if (el) frag.appendChild(el);
            });
            rec.box.appendChild(frag);
        }

        function buildTree() {
            if (BUILT) return;
            BUILT = true;
            var frag = document.createDocumentFragment();
            roots.forEach(function (id) {
                var el = makeNode(id, 0);
                if (el) frag.appendChild(el);
            });
            treeEl.appendChild(frag);
        }

        function ancestorsOf(id) {
            var out = {}, n = byId[id];
            while (n && n.parent && byId[n.parent]) { out[n.parent] = true; n = byId[n.parent]; }
            return out;
        }

        function paint() {
            buildTree();
            var filtering = !!QUERY;
            var chain = SELECTED ? ancestorsOf(SELECTED) : {};

            /* filling a node adds it to T mid-pass; repeat until the built set
               stops growing so nothing created late stays stuck visible */
            var passes = 0;
            while (passes < 8) {
                var ids = Object.keys(T);
                for (var i = 0; i < ids.length; i++) {
                    var id = ids[i], rec = T[id];
                    var visible = !filtering || !!MATCH[id] || !!HIT[id];
                    if (rec.hidden === visible) { rec.el.hidden = !visible; rec.hidden = !visible; }
                    var active = id === SELECTED;
                    if (rec.active !== active) {
                        rec.nameEl.classList.toggle('active', active);
                        rec.active = active;
                    }
                    var c = fmt(filtering ? (HIT[id] || 0) + (MATCH[id] ? 1 : 0) : count(id));
                    if (rec.count !== c) { rec.countEl.textContent = c; rec.count = c; }
                    var open = CLOSED[id] ? false : (!!OPEN[id] || !!chain[id] || (filtering && visible));
                    if (rec.open !== open) {
                        rec.el.open = open;
                        rec.open = open;
                        if (open) fill(id);
                    }
                }
                if (Object.keys(T).length === ids.length) break;
                passes++;
            }
        }

        /* ---------- detail ---------- */
        function itemRow(n) {
            var code = codeOf(n);
            var sub = [n.level, code].filter(Boolean).join(' \u00b7 ');
            var tag = (kids[n.id] || []).length ? fmt((kids[n.id] || []).length) + ' children' : '';
            return '<button type="button" class="tc-item" data-id="' + esc(n.id) + '">' +
                '<span class="tc-badge">' + esc(n.level ? n.level.slice(0, 3) : '\u00b7') + '</span>' +
                '<span><span class="tc-item-title">' + esc(n.label) + '</span>' +
                '<span class="tc-item-sub">' + esc(sub) + '</span></span>' +
                '<span class="tc-item-tag">' + esc(tag) + '</span></button>';
        }

        function listHtml(ids) {
            return '<div class="tc-list">' + ids.map(function (id) { return itemRow(byId[id]); }).join('') + '</div>';
        }

        function renderOverview() {
            titleEl.textContent = cfg.rootLabel || 'Taxonomy';
            metaEl.textContent = fmt(list.length) + ' nodes \u00b7 ' + fmt(roots.length) + ' top level' +
                (cfg.subtitle ? ' \u00b7 ' + cfg.subtitle : '');
            bodyEl.innerHTML = roots.length
                ? listHtml(roots)
                : '<div class="tc-empty">No nodes.</div>';
        }

        function renderDetail(n) {
            if (!n) { renderOverview(); return; }
            var chips = chipsOf(n);
            var path = pathOf(n.id);
            var body = bodyOf(n);
            titleEl.textContent = (detail.title ? detail.title(n.raw) : n.label) || n.label;
            metaEl.textContent = path.join(' \u203a ');
            var html = '<div class="tc-detail">' +
                (codeOf(n) ? '<div class="code">' + esc(codeOf(n)) + '</div>' : '') +
                (chips.length ? '<div class="tc-chips">' + chips.map(function (c) {
                    return '<span class="tc-chip">' + esc(c) + '</span>';
                }).join('') + '</div>' : '') +
                body +
                '</div>';
            var ch = kids[n.id] || [];
            if (ch.length) {
                html += '<div class="tc-more">Contains \u00b7 ' + fmt(ch.length) + '</div>' + listHtml(ch);
            }
            bodyEl.innerHTML = html;
        }

        function select(id, openNode) {
            if (!byId[id]) return;
            SELECTED = id;

            /* open the chain root-down, filling as we go: a parent must be
               built before its child exists in the tree */
            var chain = [], n = byId[id];
            while (n && n.parent && byId[n.parent]) { chain.unshift(n.parent); n = byId[n.parent]; }
            buildTree();
            chain.forEach(function (pid) {
                delete CLOSED[pid];
                OPEN[pid] = true;
                if (T[pid]) { T[pid].el.open = true; fill(pid); }
            });
            if (openNode && (kids[id] || []).length) { delete CLOSED[id]; OPEN[id] = true; }
            if (T[id]) T[id].el.open = !!OPEN[id] && !CLOSED[id];

            renderDetail(byId[id]);
            try {
                history.replaceState(null, '', location.pathname + location.search + '#' + encodeURIComponent(id));
            } catch (e) { /* ignore */ }
            paint();

            /* the paint pass may have built the node during its own iteration;
               mark it directly so the highlight never lags a pass behind */
            if (T[id] && !T[id].active) {
                T[id].nameEl.classList.add('active');
                T[id].active = true;
            }
            revealInTree(id);
        }

        /* keep the selected row inside the sticky tree's own scroll box
           without moving the page */
        function revealInTree(id) {
            var rec = T[id];
            if (!rec) return;
            var sc = host.querySelector('.tc-tree');
            if (!sc) return;
            var r = rec.el.getBoundingClientRect();
            var sr = sc.getBoundingClientRect();
            if (r.top < sr.top) sc.scrollTop -= (sr.top - r.top) + 10;
            else if (r.bottom > sr.bottom) sc.scrollTop += (r.bottom - sr.bottom) + 10;
        }

        bodyEl.addEventListener('click', function (ev) {
            var row = ev.target.closest ? ev.target.closest('.tc-item[data-id]') : null;
            if (row) { ev.preventDefault(); select(row.getAttribute('data-id'), true); }
        });

        /* ---------- search ---------- */
        function computeMatches(q) {
            MATCH = {};
            HIT = {};
            if (!q) return;
            var term = q.toLowerCase();
            list.forEach(function (n) {
                var hay = (n.label + ' ' + n.level + ' ' + codeOf(n)).toLowerCase();
                if (hay.indexOf(term) >= 0) MATCH[n.id] = true;
            });
            list.forEach(function (n) {
                if (!MATCH[n.id]) return;
                var p = n.parent;
                while (p && byId[p]) { HIT[p] = (HIT[p] || 0) + 1; p = byId[p].parent; }
            });
        }

        function applyQuery(q) {
            QUERY = String(q || '').trim();
            if (QUERY && !qEl.value) qEl.value = QUERY;
            computeMatches(QUERY);
            if (QUERY) {
                /* open everything visible so matches surface */
                for (var id in HIT) { OPEN[id] = true; delete CLOSED[id]; }
            }
            paint();
        }

        var timer = null;
        qEl.addEventListener('input', function () {
            clearTimeout(timer);
            timer = setTimeout(function () { applyQuery(qEl.value); }, 140);
        });
        qEl.addEventListener('keydown', function (ev) {
            if (ev.key === 'Escape') { qEl.value = ''; applyQuery(''); }
        });

        /* the nav's universal search filters this tree in place */
        document.addEventListener('epistecnica-search', function (ev) {
            var q = (ev.detail && ev.detail.query) || '';
            if (qEl.value !== q) qEl.value = q;
            applyQuery(q);
        });

        /* ---------- tools ---------- */
        host.querySelector('.tc-tools').addEventListener('click', function (ev) {
            var btn = ev.target.closest ? ev.target.closest('button[data-act]') : null;
            if (!btn) return;
            var act = btn.getAttribute('data-act');
            if (act === 'top') {
                SELECTED = null;
                OPEN = {};
                CLOSED = {};
                renderOverview();
                paint();
                try { history.replaceState(null, '', location.pathname + location.search); } catch (e) { /* ignore */ }
                treeEl.scrollTop = 0;
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } else if (act === 'expand') {
                CLOSED = {};
                (function openAll(ids) {
                    ids.forEach(function (id) {
                        OPEN[id] = true;
                        fill(id);
                        openAll(kids[id] || []);
                    });
                })(roots);
                paint();
            } else if (act === 'collapse') {
                OPEN = {};
                CLOSED = {};
                for (var id in T) {
                    CLOSED[id] = true;
                    if (T[id].el.open) { T[id].el.open = false; T[id].open = false; }
                }
            }
        });

        /* ---------- theme ---------- */
        var themeBtn = document.getElementById('themeToggle');
        if (themeBtn) {
            var label = document.getElementById('themeLabel');
            function paintLabel() {
                if (label) label.textContent = document.documentElement.dataset.theme === 'light' ? 'DARK' : 'LIGHT';
            }
            paintLabel();
            themeBtn.addEventListener('click', function () {
                var root = document.documentElement;
                var swap = function () {
                    root.dataset.theme = root.dataset.theme === 'light' ? 'dark' : 'light';
                    try { localStorage.setItem('epistecnica-theme', root.dataset.theme); } catch (e) { /* ignore */ }
                    paintLabel();
                    root.classList.remove('theme-fading');
                };
                root.classList.add('theme-fading');
                setTimeout(swap, 170);
            });
        }

        /* ---------- boot ---------- */
        renderOverview();
        paint();

        var hash = '';
        try { hash = decodeURIComponent((location.hash || '').replace(/^#/, '')); } catch (e) { hash = ''; }
        if (hash && byId[hash]) select(hash, true);

        var qs = '';
        try { qs = new URLSearchParams(location.search).get('q') || ''; } catch (e) { qs = ''; }
        if (qs) { qEl.value = qs; applyQuery(qs); }

        return {
            select: select,
            filter: applyQuery,
            nodes: list
        };
    }

    global.TreeCatalog = { mount: mount };
})(window);
