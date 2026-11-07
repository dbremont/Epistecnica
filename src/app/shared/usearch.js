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
    var UTAGS = [];                 /* [{tag, count}] built from the index */
    var UTAGSET = Object.create(null);  /* tag -> count */
    var uflat = [];   /* visible rows for keyboard nav ({e}|{tag}|{random}) */
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
        ['document', 'Documents'],
        ['glossarium', 'Glossarium'],
        ['qa', 'Q/A log']
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
            if (e.kind === 'live') return root + 'course/courses/' + p;
            return e.kind === 'course' ? root + 'course/course.html?c=' + p : root + 'course/lecture.html?l=' + p;
        }
        if (e.surface === 'document') return root + 'document/document.html?d=' + p;
        if (e.surface === 'glossarium') return root + 'glossarium/?t=' + encodeURIComponent(e.path);
        if (e.surface === 'qa') return root + 'qa/entry.html?id=' + encodeURIComponent(e.path);
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

    function utags(e) {
        return (e.tags || []).map(function (t) { return String(t).toLowerCase(); });
    }

    function ucleanTag(t) {
        return String(t).replace(/^@+/, '').replace(/[.,;:!?]+$/, '');
    }

    function uindexTags() {
        var counts = Object.create(null);
        UENTRIES.forEach(function (e) {
            e._utags = utags(e);
            e._utags.forEach(function (t) {
                if (t) counts[t] = (counts[t] || 0) + 1;
            });
        });
        UTAGS = Object.keys(counts).map(function (t) {
            return { tag: t, count: counts[t] };
        });
        UTAGS.sort(function (a, b) { return a.tag.localeCompare(b.tag); });
        UTAGSET = Object.create(null);
        UTAGS.forEach(function (t) { UTAGSET[t.tag] = t.count; });
    }

    function usuggestTags(prefix) {
        var out = [];
        for (var i = 0; i < UTAGS.length; i++) {
            if (!prefix || UTAGS[i].tag.indexOf(prefix) === 0) out.push(UTAGS[i]);
        }
        out.sort(function (a, b) { return b.count - a.count || a.tag.localeCompare(b.tag); });
        return out.slice(0, 8);
    }

    /* Parse `@tag` filters out of the query. The trailing token is a
       suggestion prefix while it is still being typed — unless it already is
       an exact tag, in which case it filters immediately. */
    function uparse(raw) {
        var src = String(raw || '');
        var toks = src.toLowerCase().split(/\s+/);
        var endsSpace = /\s$/.test(src);
        var tags = [];
        var words = [];
        var partial = null;
        for (var i = 0; i < toks.length; i++) {
            var t = toks[i];
            if (!t) continue;
            if (t.charAt(0) === '@') {
                var tag = ucleanTag(t);
                if (i === toks.length - 1 && !endsSpace && UTAGSET[tag] === undefined) {
                    partial = tag;
                } else if (tag) {
                    tags.push(tag);
                }
            } else {
                words.push(t);
            }
        }
        return { text: words.join(' '), tags: tags, partial: partial };
    }

    function uhasTags(e, tags) {
        var have = e._utags || utags(e);
        for (var i = 0; i < tags.length; i++) {
            if (have.indexOf(tags[i]) < 0) return false;
        }
        return true;
    }

    function ufilter(p) {
        var out = [];
        for (var i = 0; i < UENTRIES.length; i++) {
            var e = UENTRIES[i];
            if (p.tags.length && !uhasTags(e, p.tags)) continue;
            var s = p.text ? uscore(e, p.text) : 0;
            if (s < 0) continue;
            out.push({ e: e, s: s });
        }
        out.sort(function (a, b) {
            return a.s - b.s || a.e.title.localeCompare(b.e.title);
        });
        return out;
    }

    /* Entries the dice should sample: the current filter when one is typed,
       otherwise the whole index. */
    function uactiveList() {
        var p = uparse(uinput.value);
        if (!p.text && !p.tags.length) return UENTRIES;
        return ufilter(p).map(function (x) { return x.e; });
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

    function uentryRow(e, q) {
        var idx = uflat.length;
        uflat.push({ e: e });
        return '<a class="urow" role="option" id="usearch-opt-' + idx + '" data-idx="' + idx + '" aria-selected="false" href="' + uurl(e) + '">' +
            '<div class="urow-title">' + uhl(e.title, q) + '</div>' +
            '<div class="urow-sub">' + uhl(usub(e), q) + '</div>' +
            '</a>';
    }

    function urender() {
        var p = uparse(uinput.value);
        var active = !!(p.text || p.tags.length || p.partial !== null);
        if (!active || !UENTRIES.length) {
            usurprise.title = 'Surprise me — open a random entry (r)';
            uhide();
            return;
        }
        usurprise.title = (p.text || p.tags.length)
            ? 'Open a random match (r)'
            : 'Surprise me — open a random entry (r)';

        var matches = (p.text || p.tags.length) ? ufilter(p) : [];
        var suggestions = p.partial !== null ? usuggestTags(p.partial) : [];

        var byGroup = {};
        matches.forEach(function (x) {
            var g = x.e.surface;
            if (!byGroup[g]) byGroup[g] = [];
            if (byGroup[g].length < 6) byGroup[g].push(x.e);
        });

        uflat = [];
        var out = [];
        var shown = 0;

        if (suggestions.length) {
            out.push('<div class="ugroup-label">Tags</div>');
            suggestions.forEach(function (t) {
                var idx = uflat.length;
                uflat.push({ tag: t.tag });
                out.push(
                    '<button type="button" class="urow utag-row" role="option" id="usearch-opt-' + idx + '" data-idx="' + idx + '" data-tag="' + uesc(t.tag) + '" aria-selected="false">' +
                    '<div class="urow-title">@' + uesc(t.tag) + '</div>' +
                    '<div class="urow-sub">' + t.count + (t.count === 1 ? ' entry' : ' entries') + '</div>' +
                    '</button>'
                );
            });
        }

        var groupsHtml = [];
        UGROUPS.forEach(function (g) {
            var list = byGroup[g[0]];
            if (!list || !list.length) return;
            groupsHtml.push('<div class="ugroup-label">' + uesc(g[1]) + '</div>');
            list.forEach(function (e) {
                groupsHtml.push(uentryRow(e, p.text));
                shown++;
            });
        });

        if (matches.length > shown) {
            var label = p.tags.length
                ? '@' + p.tags.join(' @')
                : p.text;
            out.push('<div class="usearch-summary">' + matches.length + ' matches for ' +
                uesc(label) + ' · showing ' + shown + '</div>');
        }

        out = out.concat(groupsHtml);

        if (!suggestions.length && !matches.length) {
            out.push('<div class="urow-hint">nothing found.</div>');
        }

        if (matches.length) {
            var ridx = uflat.length;
            uflat.push({ random: true });
            out.push(
                '<button type="button" class="urow urandom-row" role="option" id="usearch-opt-' + ridx + '" data-idx="' + ridx + '" aria-selected="false">' +
                '<div class="urow-title">Random from these ' + matches.length + ' matches</div>' +
                '<div class="urow-sub">click the dice, or Enter on this row</div>' +
                '</button>'
            );
        }

        udrop.innerHTML = out.join('');
        udrop.hidden = false;
        uinput.setAttribute('aria-expanded', 'true');
        ukb = -1;
    }

    function uact(row) {
        if (!row) return;
        if (row.tag != null) { ucompleteTag(row.tag); return; }
        if (row.random) { ugoRandom(); return; }
        if (row.e) window.location.href = uurl(row.e);
    }

    function ucompleteTag(tag) {
        var v = uinput.value;
        var m = v.match(/(^|\s)@[^\s]*$/);
        if (m) {
            v = v.slice(0, m.index + m[1].length) + '@' + tag + ' ';
        } else {
            v = (v.trim() ? v.replace(/\s+$/, '') + ' ' : '') + '@' + tag + ' ';
        }
        uinput.value = v;
        uinput.focus();
        urender();
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

    function upick(list) {
        if (!list || !list.length) return null;
        if (window.crypto && window.crypto.getRandomValues) {
            var buf = new Uint32Array(1);
            window.crypto.getRandomValues(buf);
            return list[buf[0] % list.length];
        }
        return list[Math.floor(Math.random() * list.length)];
    }

    function ugoRandom() {
        var e = upick(uactiveList());
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
            uact(uflat[ukb]);
        }
    });

    udrop.addEventListener('click', function (e) {
        var tagRow = e.target.closest('.utag-row');
        if (tagRow) {
            e.preventDefault();
            ucompleteTag(tagRow.getAttribute('data-tag'));
            return;
        }
        if (e.target.closest('.urandom-row')) {
            e.preventDefault();
            ugoRandom();
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
            uindexTags();
            usurprise.disabled = !UENTRIES.length;
        })
        .catch(function () {
            UENTRIES = [];
            usurprise.disabled = true;
            uinput.placeholder = 'search index unavailable';
        });
})();
