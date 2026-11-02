/* catalog-viewer.js — shared interactive catalog viewer (Naturgnosis).
   Collapsible outline + squarified treemap, search/highlight, level filter,
   detail panel. Starts collapsed to the first level of the taxonomy; click a
   node to reveal the next level (progressive disclosure). Used by the product
   (HS 2022) and economic-activity (NAICS 2022) catalogs.

   Usage:
     CatalogViewer.mount('#catalogViewer', {
       nodes: [{id, label, parent, level, desc, category, link}],
       levels: ['section','chapter',...],        // ordered (root→leaf)
       colors: {level: '#hex', ...},
       detail: {code: fn, title: fn, meta: fn, body: fn}  // optional accessors
     });
*/
(function () {
    "use strict";
    if (window.CatalogViewer) return;

    var CSS = `
    .cv-toolbar { position: sticky; top: 0; z-index: 20; background: var(--nav-bg); backdrop-filter: blur(8px);
      border: 1px solid var(--border-subtle); border-radius: 8px; padding: 0.8rem 1rem; margin-bottom: 1.1rem;
      display: flex; flex-wrap: wrap; gap: 0.7rem 1.1rem; align-items: center; }
    .cv-search { flex: 1 1 240px; min-width: 180px; background: var(--bg-elevated); border: 1px solid var(--border-medium);
      border-radius: 5px; color: var(--text-primary); font-family: var(--font-body); font-size: 0.85rem; padding: 0.5rem 0.7rem; }
    .cv-search::placeholder { color: var(--text-ghost); }
    .cv-chip, .cv-btn, .cv-tab { font-family: var(--font-mono); font-size: 0.64rem; letter-spacing: 0.03em;
      border: 1px solid var(--border-medium); background: transparent; color: var(--text-secondary);
      border-radius: 999px; padding: 0.22rem 0.62rem; cursor: pointer; }
    .cv-btn, .cv-tab { border-radius: 5px; background: var(--bg-elevated); padding: 0.34rem 0.7rem; }
    .cv-chip:hover, .cv-btn:hover, .cv-tab:hover { border-color: var(--border-strong); color: var(--text-primary); }
    .cv-chip.active, .cv-tab.active { color: var(--bg-void); background: var(--accent-gold); border-color: var(--accent-gold); }
    .cv-count { font-family: var(--font-mono); font-size: 0.64rem; color: var(--text-muted); }
    .cv-tabs { display: flex; gap: 0.35rem; }
    .cv-grid { display: grid; grid-template-columns: minmax(0,1fr) 340px; gap: 1rem; align-items: start; }
    @media (max-width: 1040px) { .cv-grid { grid-template-columns: 1fr; } }
    .cv-panel { border: 1px solid var(--border-subtle); border-radius: 8px; background: var(--card-bg); }
    .cv-head { padding: 0.6rem 0.8rem; border-bottom: 1px solid var(--border-subtle); font-family: var(--font-mono);
      font-size: 0.6rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--text-ghost);
      display: flex; justify-content: space-between; align-items: center; gap: 1rem; }
    .cv-head .hov { text-transform: none; letter-spacing: 0; font-size: 0.68rem; color: var(--text-secondary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .cv-stage { position: relative; padding: 0.4rem; }
    .cv-outline { max-height: 640px; overflow: auto; padding: 0.6rem 0.5rem 1.1rem; font-size: 0.82rem; }
    .cv-outline ul { list-style: none; margin-left: 0.9rem; }
    .cv-row { display: flex; align-items: baseline; gap: 0.4rem; padding: 0.12rem 0.3rem; border-radius: 5px; cursor: pointer; }
    .cv-row:hover { background: var(--bg-elevated); }
    .cv-row.sel { background: rgba(201,149,108,0.14); outline: 1px solid var(--border-medium); }
    .cv-row.dim { opacity: 0.28; }
    .cv-tw { width: 0.8rem; flex: 0 0 0.8rem; color: var(--text-muted); font-family: var(--font-mono); font-size: 0.7rem; text-align: center; }
    .cv-code { font-family: var(--font-mono); font-size: 0.72rem; color: var(--accent-cyan); min-width: 4rem; }
    .cv-label { color: var(--text-primary); }
    .cv-lvl { font-family: var(--font-mono); font-size: 0.56rem; color: var(--text-ghost); text-transform: uppercase; letter-spacing: 0.06em; margin-left: auto; }
    .cv-tip { position: absolute; pointer-events: none; background: var(--bg-elevated); border: 1px solid var(--border-strong);
      border-radius: 5px; padding: 0.35rem 0.55rem; font-size: 0.72rem; color: var(--text-primary); display: none; max-width: 340px; z-index: 5; }
    .cv-detail { padding: 0.9rem 1rem 1.2rem; border: 1px solid var(--border-subtle); border-radius: 8px; background: var(--card-bg); }
    .cv-detail .code { font-family: var(--font-mono); font-size: 0.8rem; color: var(--accent-cyan); }
    .cv-detail .dtitle { font-family: var(--font-display); font-size: 1.5rem; line-height: 1.15; margin: 0.2rem 0 0.5rem; }
    .cv-detail .dpath { font-family: var(--font-mono); font-size: 0.6rem; color: var(--text-ghost); margin-bottom: 0.7rem; word-break: break-word; }
    .cv-detail .dmeta { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-bottom: 0.8rem; }
    .cv-detail .tag { font-family: var(--font-mono); font-size: 0.56rem; letter-spacing: 0.05em; text-transform: uppercase;
      border: 1px solid var(--border-medium); border-radius: 999px; padding: 0.14rem 0.5rem; color: var(--text-secondary); }
    .cv-detail h4 { font-family: var(--font-mono); font-size: 0.58rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-ghost); margin: 0.9rem 0 0.3rem; }
    .cv-detail p { color: var(--text-secondary); font-size: 0.82rem; line-height: 1.55; white-space: pre-wrap; }
    .cv-detail a { color: var(--accent-cyan); }
    .cv-detail .row { display: flex; gap: 0.4rem; margin-top: 0.9rem; flex-wrap: wrap; }
    .cv-empty { color: var(--text-muted); padding: 3rem 1rem; text-align: center; font-family: var(--font-mono); font-size: 0.78rem; }
    .cv-legend { display: flex; flex-wrap: wrap; gap: 0.5rem 0.9rem; padding: 0.2rem 0.1rem 0; }
    .cv-leg { display: inline-flex; align-items: center; gap: 0.3rem; font-family: var(--font-mono); font-size: 0.6rem; color: var(--text-secondary); }
    .cv-dot { width: 9px; height: 9px; border-radius: 50%; display: inline-block; }
    .cv-crumb { font-family: var(--font-mono); font-size: 0.62rem; color: var(--text-secondary); padding: 0.2rem 0.5rem; }
    .cv-crumb a { color: var(--accent-cyan); cursor: pointer; text-decoration: none; }
    .cv-crumb a:hover { text-decoration: underline; }
    .cv-hidden { display: none !important; }
    .cv-canvas { display: block; width: 100%; height: 580px; cursor: pointer; }
    .cv-tm-bar { display: flex; justify-content: space-between; align-items: center; padding: 0.3rem 0.5rem 0; gap: 1rem; flex-wrap: wrap; }
    `;

    function injectCSS() {
        if (document.getElementById("cv-style")) return;
        var s = document.createElement("style"); s.id = "cv-style"; s.textContent = CSS;
        document.head.appendChild(s);
    }
    function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]; }); }
    function num(n) { return (n || 0).toLocaleString(); }
    function hexA(hex, a) { var h = String(hex || "#888").replace("#", ""); if (h.length === 3) h = h[0] + h[0] + h[1] + h[1] + h[2] + h[2]; return "rgba(" + parseInt(h.substr(0, 2), 16) + "," + parseInt(h.substr(2, 2), 16) + "," + parseInt(h.substr(4, 2), 16) + "," + a + ")"; }

    function mount(target, cfg) {
        injectCSS();
        var root = typeof target === "string" ? document.querySelector(target) : target;
        if (!root) return;
        var levels = cfg.levels || [];
        var colors = cfg.colors || {};
        var dfn = cfg.detail || {};

        /* ---- build tree ---- */
        var by = {}, roots = [];
        cfg.nodes.forEach(function (r) { by[r.id] = Object.assign({}, r, { children: [], leaves: 0, path: "", parentNode: null }); });
        cfg.nodes.forEach(function (r) {
            var n = by[r.id];
            if (r.parent && by[r.parent] && r.parent !== r.id) { by[r.parent].children.push(n); n.parentNode = by[r.parent]; }
            else roots.push(n);
        });
        function sortRec(n, path) {
            n.path = path ? path + " \u203A " + n.label : n.label;
            n.children.sort(function (a, b) { return String(a.id).localeCompare(String(b.id), undefined, { numeric: true }); });
            if (!n.children.length) n.leaves = 1;
            else { n.children.forEach(function (c) { sortRec(c, n.path); }); n.leaves = n.children.reduce(function (s, c) { return s + c.leaves; }, 0); }
        }
        roots.forEach(function (r) { sortRec(r, ""); });
        roots.sort(function (a, b) { return String(a.id).localeCompare(String(b.id), undefined, { numeric: true }); });
        var allNodes = cfg.nodes.map(function (r) { return by[r.id]; });

        /* ---- state: start collapsed to the first level ---- */
        var state = { collapsed: {}, levelOn: {}, q: "", sel: null, view: "outline", drill: null };
        levels.forEach(function (l) { state.levelOn[l] = true; });
        function collapseToFirstLevel() {
            state.collapsed = {};
            allNodes.forEach(function (n) { if (n.children.length) state.collapsed[n.id] = true; });
        }
        collapseToFirstLevel();

        /* ---- DOM ---- */
        root.innerHTML =
            '<div class="cv-toolbar">' +
            '<input class="cv-search" id="cv-q" type="text" placeholder="' + esc(cfg.searchPlaceholder || "Search…") + '" autocomplete="off">' +
            '<span class="cv-count" id="cv-count"></span>' +
            '<span id="cv-levels" style="display:flex;flex-wrap:wrap;gap:0.3rem"></span>' +
            '<button class="cv-btn" id="cv-expand">expand all</button>' +
            '<button class="cv-btn" id="cv-collapse">collapse</button>' +
            '<span class="cv-tabs">' +
            '<button class="cv-tab active" data-view="outline">list</button>' +
            '<button class="cv-tab" data-view="treemap">treemap</button>' +
            '</span>' +
            '</div>' +
            '<div class="cv-legend" id="cv-legend"></div>' +
            '<div class="cv-grid" style="margin-top:1rem">' +
            '<div class="cv-panel"><div class="cv-head"><span id="cv-vlabel">List</span><span class="hov" id="cv-hov"></span></div>' +
            '<div class="cv-outline" id="cv-outline"></div>' +
            '<div class="cv-stage cv-hidden" id="cv-tm-wrap"><div class="cv-tm-bar"><span class="cv-crumb" id="cv-crumb"></span><span class="cv-crumb" style="color:var(--text-ghost)">click a box to open its level</span></div><canvas class="cv-canvas" id="cv-tm"></canvas><div class="cv-tip" id="cv-tm-tip"></div></div>' +
            '</div>' +
            '<aside class="cv-detail" id="cv-detail"><div class="cv-empty">Select a node.</div></aside>' +
            '</div>';

        var el = function (id) { return document.getElementById(id); };
        var LEVEL_COLOR = function (l) { return colors[l] || "#888"; };
        function pathOf(node) { var p = [], c = node; while (c) { p.unshift(c); c = c.parentNode; } return p; }

        /* ---- predicates ---- */
        function match(n) { if (!state.q) return false; return (n.id + " " + n.label + " " + (n.desc || "")).toLowerCase().indexOf(state.q) !== -1; }
        function hasMatchBelow(n) { if (match(n)) return true; for (var i = 0; i < n.children.length; i++) if (hasMatchBelow(n.children[i])) return true; return false; }
        function isDim(n) { if (!state.levelOn[n.level]) return true; if (state.q && !match(n) && !hasMatchBelow(n)) return true; return false; }
        function hiddenByCollapse(n) { var c = n.parentNode; while (c) { if (state.collapsed[c.id]) return true; c = c.parentNode; } return false; }
        function visibleKids(n) { return state.collapsed[n.id] ? [] : n.children; }

        /* ---- legend + level chips ---- */
        el("cv-legend").innerHTML = levels.map(function (l) {
            return '<span class="cv-leg"><span class="cv-dot" style="background:' + LEVEL_COLOR(l) + '"></span>' + esc(l) + '</span>';
        }).join("");
        el("cv-levels").innerHTML = levels.map(function (l) { return '<button class="cv-chip active" data-lvl="' + esc(l) + '">' + esc(l) + '</button>'; }).join("");
        el("cv-levels").querySelectorAll(".cv-chip").forEach(function (b) {
            b.addEventListener("click", function () { var l = b.getAttribute("data-lvl"); state.levelOn[l] = !state.levelOn[l]; b.classList.toggle("active", state.levelOn[l]); refresh(); });
        });

        /* ---- outline ---- */
        function renderOutline() {
            function nodeHtml(n) {
                var open = !state.collapsed[n.id];
                var tw = n.children.length ? (open ? "\u25BE" : "\u25B8") : "\u00B7";
                var h = '<li><div class="cv-row' + (isDim(n) ? " dim" : "") + (state.sel === n.id ? " sel" : "") + '" data-id="' + esc(n.id) + '">' +
                    '<span class="cv-tw" data-toggle="' + esc(n.id) + '">' + tw + '</span>' +
                    '<span class="cv-code">' + esc(String(n.id).length > 12 ? "" : n.id) + '</span>' +
                    '<span class="cv-label">' + esc(n.label) + '</span>' +
                    '<span class="cv-lvl">' + esc(n.level) + '</span></div>';
                if (n.children.length && open) h += "<ul>" + n.children.map(nodeHtml).join("") + "</ul>";
                return h + "</li>";
            }
            el("cv-outline").innerHTML = '<ul style="list-style:none">' + roots.map(nodeHtml).join("") + "</ul>";
            el("cv-outline").querySelectorAll("[data-toggle]").forEach(function (t) {
                t.addEventListener("click", function (e) { e.stopPropagation(); var c = t.getAttribute("data-toggle"); state.collapsed[c] = !state.collapsed[c]; renderOutline(); });
            });
            el("cv-outline").querySelectorAll(".cv-row").forEach(function (r) {
                r.addEventListener("click", function () { select(r.getAttribute("data-id")); });
            });
        }

        /* ---- treemap (squarified, one level per drill) ---- */
        var tmRects = [];
        function squarify(items, box, out) {
            var total = items.reduce(function (s, x) { return s + x.area; }, 0) || 1;
            var scale = (box.w * box.h) / total;
            var arr = items.map(function (x) { return { n: x.n, area: x.area * scale }; });
            var x = box.x, y = box.y, w = box.w, h = box.h, i = 0;
            function worst(row, area, short) {
                var mx = 0, mn = Infinity;
                row.forEach(function (r) { if (r.area > mx) mx = r.area; if (r.area < mn) mn = r.area; });
                if (mn <= 0) mn = 1e-6;
                var sum2 = area * area;
                return Math.max((short * short * mx) / sum2, sum2 / (short * short * mn));
            }
            while (i < arr.length && w > 0.5 && h > 0.5) {
                var short = Math.min(w, h), row = [], rowArea = 0, cur = Infinity, j = i;
                while (j < arr.length) {
                    var test = row.concat([arr[j]]), testArea = rowArea + arr[j].area, wv = worst(test, testArea, short);
                    if (row.length === 0 || wv <= cur) { row = test; rowArea = testArea; cur = wv; j++; } else break;
                }
                if (w >= h) {
                    var rw = rowArea / h, oy = y;
                    row.forEach(function (r) { var rh = r.area / rw; out.push({ n: r.n, r: { x: x, y: oy, w: rw, h: rh } }); oy += rh; });
                    x += rw; w -= rw;
                } else {
                    var rh2 = rowArea / w, ox = x;
                    row.forEach(function (r) { var rw2 = r.area / rh2; out.push({ n: r.n, r: { x: ox, y: y, w: rw2, h: rh2 } }); ox += rw2; });
                    y += rh2; h -= rh2;
                }
                i = j;
            }
        }
        function renderTreemap() {
            var wrap = el("cv-tm-wrap"), cv = el("cv-tm");
            el("cv-outline").classList.add("cv-hidden");
            wrap.classList.remove("cv-hidden");
            var w = wrap.clientWidth || 600, h = 580;
            var dpr = window.devicePixelRatio || 1;
            cv.width = w * dpr; cv.height = h * dpr; cv.style.width = w + "px"; cv.style.height = h + "px";
            var ctx = cv.getContext("2d"); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, w, h);
            var pad = 4;
            var cur = state.drill ? by[state.drill] : null;
            var kids = cur ? (cur.children || []) : roots;
            var box = { x: pad, y: pad, w: w - pad * 2, h: h - pad * 2 };
            var top = [];
            squarify(kids.map(function (c) { return { n: c, area: c.leaves }; }), box, top);
            tmRects = top;
            top.forEach(function (t) {
                var r = t.r, dim = isDim(t.n);
                ctx.fillStyle = dim ? hexA(LEVEL_COLOR(t.n.level), 0.14) : hexA(LEVEL_COLOR(t.n.level), 0.85);
                ctx.fillRect(r.x, r.y, Math.max(0, r.w - 1.5), Math.max(0, r.h - 1.5));
                if (r.w > 44 && r.h > 14) {
                    ctx.fillStyle = "rgba(0,0,0,0.74)"; ctx.font = "600 10.5px 'JetBrains Mono', monospace";
                    ctx.fillText(String(t.n.label).slice(0, Math.max(1, Math.floor(r.w / 6.2))), r.x + 4, r.y + 13);
                    if (t.n.children.length && r.h > 28) {
                        ctx.font = "9px 'JetBrains Mono', monospace"; ctx.fillStyle = "rgba(0,0,0,0.5)";
                        ctx.fillText(t.n.children.length + " \u2192", r.x + 4, r.y + 25);
                    }
                }
            });
            renderCrumb(cur);
        }
        function renderCrumb(cur) {
            var chain = cur ? pathOf(cur) : [];
            var html = '<a data-drill="">root</a>';
            chain.forEach(function (n) { html += ' \u203A <a data-drill="' + esc(n.id) + '">' + esc(n.label) + '</a>'; });
            el("cv-crumb").innerHTML = html;
            el("cv-crumb").querySelectorAll("a").forEach(function (a) {
                a.addEventListener("click", function () { state.drill = a.getAttribute("data-drill") || null; renderTreemap(); });
            });
        }
        function hitTm(mx, my) { for (var i = tmRects.length - 1; i >= 0; i--) { var r = tmRects[i].r; if (mx >= r.x && mx <= r.x + r.w && my >= r.y && my <= r.y + r.h) return tmRects[i]; } return null; }

        /* ---- detail ---- */
        function select(id) {
            state.sel = id; var n = by[id]; var d = el("cv-detail");
            if (n) {
                try {
                    var h = "#" + encodeURIComponent(String(id));
                    if (window.location.hash !== h) window.history.replaceState(null, "", h);
                } catch (e) {}
            }
            if (!n) { d.innerHTML = '<div class="cv-empty">Select a node.</div>'; return; }
            var code = dfn.code ? dfn.code(n) : (String(n.id).length <= 12 ? n.id : "");
            var meta = dfn.meta ? dfn.meta(n) : "";
            var body = dfn.body ? dfn.body(n) : (n.desc ? '<h4>Description</h4><p>' + esc(n.desc) + '</p>' : "");
            var link = n.link ? '<a href="' + esc(n.link) + '">open in its space \u2197</a>' : "";
            d.innerHTML = (code ? '<div class="code">' + esc(code) + '</div>' : "") +
                '<div class="dtitle">' + esc(n.label) + '</div>' +
                '<div class="dpath">' + esc(n.path || n.label) + '</div>' +
                '<div class="dmeta"><span class="tag">' + esc(n.level) + '</span>' +
                (n.children.length ? '<span class="tag">' + n.children.length + ' children</span>' : '<span class="tag">leaf</span>') +
                (meta ? '<span class="tag">' + meta + '</span>' : '') + '</div>' + body +
                (link ? '<div class="row">' + link + '</div>' : "");
            if (state.view === "treemap") renderTreemap(); else renderOutline();
        }

        /* ---- counts / refresh ---- */
        function counts() {
            var vis = 0, tot = 0;
            allNodes.forEach(function (n) { tot++; if (!isDim(n) && !hiddenByCollapse(n)) vis++; });
            el("cv-count").textContent = num(vis) + " / " + num(tot) + " shown";
        }
        function refresh() { counts(); if (state.view === "treemap") renderTreemap(); else renderOutline(); }

        function setView(v) {
            state.view = v;
            if (v === "treemap") { renderTreemap(); }
            else { el("cv-tm-wrap").classList.add("cv-hidden"); el("cv-outline").classList.remove("cv-hidden"); el("cv-vlabel").textContent = "List"; renderOutline(); }
            if (v === "treemap") el("cv-vlabel").textContent = "Treemap";
            root.querySelectorAll(".cv-tab").forEach(function (t) { t.classList.toggle("active", t.getAttribute("data-view") === v); });
            counts();
        }
        root.querySelectorAll(".cv-tab").forEach(function (t) { t.addEventListener("click", function () { setView(t.getAttribute("data-view")); }); });
        el("cv-expand").addEventListener("click", function () { state.collapsed = {}; state.drill = null; refresh(); });
        el("cv-collapse").addEventListener("click", function () { collapseToFirstLevel(); state.drill = null; refresh(); });
        el("cv-q").addEventListener("input", function (e) { state.q = e.target.value.trim().toLowerCase(); refresh(); });

        var cvTm = el("cv-tm"), tmTip = el("cv-tm-tip");
        cvTm.addEventListener("mousemove", function (e) {
            var r = cvTm.getBoundingClientRect(), t = hitTm(e.clientX - r.left, e.clientY - r.top);
            if (t) { tmTip.style.display = "block"; tmTip.style.left = (e.clientX - r.left + 12) + "px"; tmTip.style.top = (e.clientY - r.top + 12) + "px";
                tmTip.innerHTML = '<b>' + esc(t.n.id) + '</b> ' + esc(t.n.label) + (t.n.children.length ? '<br><span style="color:var(--text-muted)">click to open ' + t.n.children.length + '</span>' : "");
                el("cv-hov").textContent = t.n.id + " " + t.n.label; }
            else { tmTip.style.display = "none"; el("cv-hov").textContent = ""; }
        });
        cvTm.addEventListener("mouseleave", function () { tmTip.style.display = "none"; });
        cvTm.addEventListener("click", function (e) {
            var r = cvTm.getBoundingClientRect(), t = hitTm(e.clientX - r.left, e.clientY - r.top);
            if (!t) return; select(t.n.id);
            if (t.n.children.length) { state.drill = t.n.id; renderTreemap(); }
        });

        window.addEventListener("resize", function () { if (state.view === "treemap") renderTreemap(); });

        refresh();
        var deep = null;
        try { deep = decodeURIComponent(String(window.location.hash || "").replace(/^#/, "")); } catch (e) { deep = null; }
        if (deep && by[deep]) {
            var c = by[deep].parentNode;
            while (c) { delete state.collapsed[c.id]; c = c.parentNode; }
            refresh(); select(deep);
        } else if (roots[0]) select(roots[0].id);
        return { refresh: refresh, setView: setView, select: select };
    }

    window.CatalogViewer = { mount: mount };
})();
