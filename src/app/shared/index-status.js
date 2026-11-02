/* index-status.js — non-blocking index-build progress chip (shared).
 *
 * Index builds are asynchronous (bin/index_jobs.py): the server queues a
 * chunked build and reports done/total/pct at GET /api/index/status. This
 * script polls that endpoint while a build is running and shows a small
 * progress chip, so no page ever waits for a rebuild to finish.
 *
 * Usage (every surface, beside the nav search):
 *   <script src="../shared/index-status.js" data-root="../" defer></script>
 *
 * data-root is the page's prefix to the site root, so the fetch stays
 * relative (`<root>api/index/status`) and prefix mounting keeps working.
 * The endpoint is opt-in; when it is off (404) this script stays silent.
 */
(function () {
    "use strict";

    var script = document.currentScript;
    var root = (script && script.getAttribute("data-root")) || "";
    if (root && root.charAt(root.length - 1) !== "/") root += "/";
    var ENDPOINT = root + "api/index/status";
    var POLL_MS = 2000;
    var LINGER_MS = 5000;

    var timer = null;
    var chip = null;
    var shown = false;

    var LABELS = {
        notes: "notes",
        courses: "courses",
        documents: "documents",
        glossarium: "glossarium",
        qa: "Q/A",
        atlas: "atlas",
        search: "search",
    };

    function ensureChip() {
        if (chip) return chip;
        chip = document.getElementById("index-status-chip");
        if (chip) return chip;
        chip = document.createElement("div");
        chip.id = "index-status-chip";
        chip.setAttribute("role", "status");
        chip.setAttribute("aria-live", "polite");
        chip.style.cssText = [
            "position:fixed", "left:1rem", "bottom:1rem", "z-index:9000",
            "display:none", "align-items:center", "gap:0.5rem",
            "max-width:min(28rem,calc(100vw - 2rem))",
            "padding:0.45rem 0.75rem", "border-radius:999px",
            "border:1px solid var(--border-medium,rgba(255,255,255,0.12))",
            "background:var(--card-bg,rgba(11,13,20,0.9))",
            "color:var(--text-secondary,#8A8FA6)",
            "font:500 0.7rem/1.2 var(--font-mono,'JetBrains Mono',monospace)",
            "letter-spacing:0.02em", "backdrop-filter:blur(8px)",
            "box-shadow:0 6px 24px rgba(0,0,0,0.35)",
            "pointer-events:none", "transition:opacity 160ms ease",
            "opacity:0",
        ].join(";");
        chip.innerHTML = '<span class="is-dot" style="width:6px;height:6px;border-radius:50%;'
            + 'background:var(--accent-cyan,#5BF0E7);flex:none"></span>'
            + '<span class="is-text" style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis"></span>';
        document.body.appendChild(chip);
        return chip;
    }

    function show(text, done) {
        var el = ensureChip();
        el.querySelector(".is-text").textContent = text;
        var dot = el.querySelector(".is-dot");
        if (dot) {
            dot.style.background = done
                ? "var(--accent-gold,#C5A467)"
                : "var(--accent-cyan,#5BF0E7)";
            dot.style.opacity = done ? "0.85" : "1";
        }
        if (!shown) {
            el.style.display = "flex";
            requestAnimationFrame(function () { el.style.opacity = "1"; });
            shown = true;
        }
    }

    function hide() {
        if (!chip || !shown) return;
        chip.style.opacity = "0";
        shown = false;
        setTimeout(function () {
            if (!shown && chip) chip.style.display = "none";
        }, 200);
    }

    function describe(state) {
        var job = state.job || {};
        var builders = state.builders || {};
        var names = (job.builders && job.builders.length) ? job.builders : [state.running];
        var running = names.filter(Boolean).slice(-1)[0];

        if (job.state === "running" && running) {
            var entry = builders[running] || {};
            var label = LABELS[running] || running;
            if (entry.total) {
                return {
                    text: "indexing " + label + " · " + entry.done + "/" + entry.total
                        + " · " + Math.round(entry.pct || 0) + "%",
                    busy: true,
                };
            }
            return { text: "indexing " + label + "…", busy: true };
        }
        if (job.state === "done") return { text: "index ready", busy: false };
        if (job.state === "error") return { text: "index build failed", busy: false };
        return { text: "", busy: false };
    }

    function poll() {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", ENDPOINT + "?t=" + Date.now(), true);
        xhr.timeout = 4000;
        xhr.onload = function () {
            if (xhr.status !== 200) return finish(0);
            var state;
            try { state = JSON.parse(xhr.responseText); } catch (e) { return finish(0); }
            var info = describe(state);
            if (!info.text) return finish(0);
            show(info.text, !info.busy);
            if (info.busy || state.busy) {
                schedule(POLL_MS);
            } else {
                finish(LINGER_MS);
            }
        };
        xhr.onerror = xhr.ontimeout = function () { finish(0); };
        xhr.send();
    }

    function schedule(ms) {
        clearTimeout(timer);
        timer = setTimeout(poll, ms);
    }

    function finish(linger) {
        clearTimeout(timer);
        if (linger > 0) {
            timer = setTimeout(hide, linger);
        } else {
            hide();
        }
    }

    function start() {
        poll();
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", start, { once: true });
    } else {
        start();
    }
})();
