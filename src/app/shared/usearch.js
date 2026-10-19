/* Epistecnica — shared universal nav search.
   One implementation for every surface. The page provides the nav markup:

     <div class="usearch-wrap">
       <svg class="usearch-icon" …></svg>
       <input type="search" id="usearch" …>
       <button type="button" id="usurprise" …></button>
       <div class="usearch-drop" id="usearch-drop" hidden></div>
     </div>

   and loads this file with a data-root prefix to the site root:
     data-root=""     at the root (hub, docs)
     data-root="../"  one directory deep (note/, course/, document/)

   The prefix resolves both the index (root + data/search-index.json) and the
   destination links, keeping the architecture's "relative paths only" rule. */

(function () {
    'use strict';

    var script = document.currentScript;
    var root = (script && script.getAttribute('data-root')) || '';
    if (root && root.charAt(root.length - 1) !== '/') root += '/';

    var uinput = document.getElementById('usearch');
    var udrop = document.getElementById('usearch-drop');
    var usurprise = document.getElementById('usurprise');
    if (!uinput || !udrop || !usurprise) return;

    var UENTRIES = [];
    var uflat = [];   /* visible rows for keyboard nav */
    var ukb = -1;
    var utimer = null;

    function uhide() {
        udrop.hidden = true;
        udrop.innerHTML = '';
        uinput.setAttribute('aria-expanded', 'false');
        uinput.removeAttribute('aria-activedescendant');
        uflat = [];
        ukb = -1;
    }

    var UGROUPS = [
        ['note', 'Notes'],
        ['course', 'Courses & lectures'],
        ['document', 'Documents']
    ];

    function uesc(s) {
        var d = document.createElement('div');
        d.textContent = s == null ? '' : String(s);
        return d.innerHTML;
    }

    function uencPath(p) {
        return String(p).split('/').map(encodeURIComponent).join('/');
    }

    function uurl(e) {
        var p = uencPath(e.path);
        if (e.surface === 'note') {
            return e.kind === 'live' ? root + 'note/data/' + p : root + 'note/note.html?n=' + p;
        }
        if (e.surface === 'course') {
            return e.kind === 'course' ? root + 'course/course.html?c=' + p : root + 'course/lecture.html?l=' + p;
        }
        if (e.surface === 'document') return root + 'document/document.html?d=' + p;
        return '#';
    }

    function usub(e) {
        var bits = [];
        if (e.type) bits.push(e.type);
        if (e.kind && e.kind !== e.type) bits.push(e.kind);
        if (e.tags && e.tags.length) bits.push(e.tags.slice(0, 3).join(', '));
        if (e.excerpt) bits.push(e.excerpt.slice(0, 120));
        return bits.join(' · ');
    }

    function uscore(e, q) {
        var title = (e.title || '').toLowerCase();
        if (title.indexOf(q) === 0) return 0;
        if (title.indexOf(q) > 0) return 1;
        if (((e.type || '') + ' ' + (e.tags || []).join(' ')).toLowerCase().indexOf(q) >= 0) return 2;
        if ((e.aliases || []).join(' ').toLowerCase().indexOf(q) >= 0) return 2;
        if ((e.path || '').toLowerCase().indexOf(q) >= 0) return 2;
        if ((e.excerpt || '').toLowerCase().indexOf(q) >= 0) return 3;
        return -1;
    }

    function uhl(text, q) {
        var e = uesc(text);
        if (!q) return e;
        var i = String(text).toLowerCase().indexOf(q);
        if (i < 0) return e;
        return uesc(String(text).slice(0, i)) + '<mark>' +
            uesc(String(text).slice(i, i + q.length)) + '</mark>' +
            uesc(String(text).slice(i + q.length));
    }

    function urender() {
        var q = uinput.value.trim().toLowerCase();
        if (!q || !UENTRIES.length) { uhide(); return; }
        var scored = [];
        for (var i = 0; i < UENTRIES.length; i++) {
            var s = uscore(UENTRIES[i], q);
            if (s >= 0) scored.push({ e: UENTRIES[i], s: s });
        }
        scored.sort(function (a, b) { return a.s - b.s || a.e.title.localeCompare(b.e.title); });
        var byGroup = {};
        scored.forEach(function (x) {
            var g = x.e.surface;
            if (!byGroup[g]) byGroup[g] = [];
            if (byGroup[g].length < 6) byGroup[g].push(x.e);
        });
        var out = [];
        uflat = [];
        if (!scored.length) {
            out.push('<div class="urow-hint">nothing found.</div>');
        }
        UGROUPS.forEach(function (g) {
            var list = byGroup[g[0]];
            if (!list || !list.length) return;
            out.push('<div class="ugroup-label">' + uesc(g[1]) + '</div>');
            list.forEach(function (e) {
                var idx = uflat.length;
                uflat.push(e);
                out.push(
                    '<a class="urow" role="option" id="usearch-opt-' + idx + '" data-idx="' + idx + '" aria-selected="false" href="' + uurl(e) + '">' +
                    '<div class="urow-title">' + uhl(e.title, q) + '</div>' +
                    '<div class="urow-sub">' + uhl(usub(e), q) + '</div>' +
                    '</a>'
                );
            });
        });
        udrop.innerHTML = out.join('');
        udrop.hidden = false;
        uinput.setAttribute('aria-expanded', 'true');
        ukb = -1;
    }

    function umove(d) {
        if (!uflat.length) return;
        ukb = (ukb + d + uflat.length) % uflat.length;
        var rows = udrop.querySelectorAll('.urow');
        rows.forEach(function (r) {
            r.classList.remove('kb-focus');
            r.setAttribute('aria-selected', 'false');
        });
        var el = udrop.querySelector('.urow[data-idx="' + ukb + '"]');
        if (el) {
            el.classList.add('kb-focus');
            el.setAttribute('aria-selected', 'true');
            uinput.setAttribute('aria-activedescendant', el.id);
            el.scrollIntoView({ block: 'nearest' });
        }
    }

    function upick() {
        if (!UENTRIES.length) return null;
        if (window.crypto && window.crypto.getRandomValues) {
            var buf = new Uint32Array(1);
            window.crypto.getRandomValues(buf);
            return UENTRIES[buf[0] % UENTRIES.length];
        }
        return UENTRIES[Math.floor(Math.random() * UENTRIES.length)];
    }

    function ugoRandom() {
        var e = upick();
        if (e) window.location.href = uurl(e);
    }

    uinput.addEventListener('input', function () {
        clearTimeout(utimer);
        utimer = setTimeout(urender, 120);
    });

    uinput.addEventListener('focus', function () { if (uinput.value.trim()) urender(); });

    uinput.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { uhide(); uinput.blur(); return; }
        if (e.key === 'ArrowDown') { e.preventDefault(); umove(1); return; }
        if (e.key === 'ArrowUp') { e.preventDefault(); umove(-1); return; }
        if (e.key === 'Enter' && ukb >= 0 && uflat[ukb]) {
            e.preventDefault();
            window.location.href = uurl(uflat[ukb]);
        }
    });

    document.addEventListener('click', function (e) {
        if (!e.target.closest('.usearch-wrap')) uhide();
    });

    document.addEventListener('keydown', function (e) {
        var el = document.activeElement;
        var typing = !!el && (el === uinput || el.tagName === 'INPUT' || el.tagName === 'TEXTAREA' || el.isContentEditable);
        if (e.key === '/' && !typing && !e.ctrlKey && !e.metaKey && !e.altKey) { e.preventDefault(); uinput.focus(); return; }
        if ((e.key === 'r' || e.key === 'R') && !typing && !e.ctrlKey && !e.metaKey && !e.altKey) { e.preventDefault(); ugoRandom(); }
    });

    usurprise.addEventListener('click', ugoRandom);

    fetch(root + 'data/search-index.json', { headers: { 'Accept': 'application/json' } })
        .then(function (r) {
            if (!r.ok) throw new Error('HTTP ' + r.status);
            return r.json();
        })
        .then(function (idx) {
            UENTRIES = idx.entries || [];
            usurprise.disabled = !UENTRIES.length;
        })
        .catch(function () {
            UENTRIES = [];
            usurprise.disabled = true;
            uinput.placeholder = 'search index unavailable';
        });
})();
