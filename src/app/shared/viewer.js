/* Universal content viewer — one script, four thin shells.
 *
 * The note / course / lecture / document viewers are the same page frame;
 * each shell includes this script with its kind:
 *
 *     <script src="../shared/viewer.js" data-kind="note"></script>
 *
 * The shell owns the DOM skeleton (shared ids: ambientCanvas, themeToggle,
 * note-header / crumbs / note-title / note-meta chips, loading / error /
 * note-card / note-body, sidebar / toc, qa-* and hist-* modals). This
 * script owns behavior; kind-specific bits live in the KINDS table below.
 * Add a corpus by adding a table entry and a thin shell page. */
(function () {
    'use strict';

    var scriptEl = document.currentScript;
    var kindName = (scriptEl && scriptEl.getAttribute('data-kind')) || '';

    var SEG_RE = /^[a-z0-9]+(-[a-z0-9]+)*$/;
    var REPO = 'https://github.com/dbremont/Epistecnica';

    /* ---------- ambient constellation ---------- */

    var canvas = document.getElementById('ambientCanvas');
    var ctx = canvas.getContext('2d');
    var pts = [];
    var LINK_DIST = 130;

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        var count = Math.max(20, Math.floor((canvas.width * canvas.height) / 40000));
        pts = [];
        for (var i = 0; i < count; i++) {
            pts.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * 0.22,
                vy: (Math.random() - 0.5) * 0.22,
                r: Math.random() * 1.4 + 0.4
            });
        }
    }

    function tick() {
        var light = document.documentElement.dataset.theme === 'light';
        var dotRGB = light ? '26, 29, 36' : '226, 228, 235';
        var linkRGB = light ? '154, 123, 63' : '197, 164, 103';
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (var i = 0; i < pts.length; i++) {
            var p = pts[i];
            p.x += p.vx; p.y += p.vy;
            if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
            if (p.y < 0 || p.y > canvas.height) p.vy *= -1;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(' + dotRGB + ', 0.5)';
            ctx.fill();
            for (var j = i + 1; j < pts.length; j++) {
                var m = pts[j];
                var dx = p.x - m.x, dy = p.y - m.y;
                var dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < LINK_DIST) {
                    ctx.beginPath();
                    ctx.moveTo(p.x, p.y);
                    ctx.lineTo(m.x, m.y);
                    ctx.strokeStyle = 'rgba(' + linkRGB + ', ' + (0.10 * (1 - dist / LINK_DIST)) + ')';
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
            }
        }
        requestAnimationFrame(tick);
    }

    window.addEventListener('resize', resize);
    resize();
    requestAnimationFrame(tick);

    /* ---------- theme toggle (shared with the hub) ---------- */

    var themeToggle = document.getElementById('themeToggle');
    var themeLabel = document.getElementById('themeLabel');
    var themeFading = false;

    function applyThemeLabel() {
        themeLabel.textContent = document.documentElement.dataset.theme === 'light' ? 'DARK' : 'LIGHT';
    }

    themeToggle.addEventListener('click', function () {
        if (themeFading) return;
        themeFading = true;
        var root = document.documentElement;
        var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        var swap = function () {
            root.dataset.theme = root.dataset.theme === 'light' ? 'dark' : 'light';
            try { localStorage.setItem('epistecnica-theme', root.dataset.theme); } catch (e) { /* private mode */ }
            applyThemeLabel();
            root.classList.remove('theme-fading');
            themeFading = false;
        };
        if (reduced) {
            swap();
            return;
        }
        root.classList.add('theme-fading');
        setTimeout(swap, 190);
    });

    applyThemeLabel();

    /* ---------- shared loading helpers ---------- */

    function fail(msg) {
        document.getElementById('loading').hidden = true;
        document.getElementById('errorMsg').textContent = msg;
        document.getElementById('error').hidden = false;
    }

    function validMdPath(p) {
        if (!p || p.length > 200) return false;
        var parts = p.split('/');
        for (var i = 0; i < parts.length; i++) {
            var part = parts[i];
            if (i === parts.length - 1) {
                if (!/\.md$/.test(part) || !SEG_RE.test(part.slice(0, -3))) return false;
            } else if (!SEG_RE.test(part)) {
                return false;
            }
        }
        return true;
    }

    function validCourse(c) {
        return !!c && c.length <= 200 && SEG_RE.test(c);
    }

    function esc(s) {
        var d = document.createElement('div');
        d.textContent = s == null ? '' : String(s);
        return d.innerHTML;
    }

    function encPath(p) {
        return p.split('/').map(encodeURIComponent).join('/');
    }

    /* Split optional `---` front matter off; read `tags: [...]` and `qa:`. */
    function stripFrontMatter(md) {
        var tags = [];
        var qa = [];
        var body = md;
        var fm = md.match(/^---\n([\s\S]*?)\n---\n/);
        if (fm) {
            var lines = fm[1].split('\n');
            var inQa = false;
            for (var i = 0; i < lines.length; i++) {
                var line = lines[i].trim();
                if (inQa) {
                    var qm = line.match(/^-\s+(.+)$/);
                    if (qm) {
                        var q = qm[1].trim().replace(/^['"]|['"]$/g, '');
                        if (q) qa.push(q);
                        continue;
                    }
                    if (!line) continue;
                    inQa = false;
                }
                if (/^qa:\s*$/.test(line)) { inQa = true; continue; }
                var tm = line.match(/^tags:\s*\[(.*)\]\s*$/);
                if (tm) {
                    tm[1].split(',').forEach(function (raw) {
                        var t = raw.trim().replace(/^['"]|['"]$/g, '').toLowerCase();
                        if (t && tags.indexOf(t) < 0) tags.push(t);
                    });
                }
            }
            body = md.slice(fm[0].length);
        }
        return { body: body, tags: tags, qa: qa };
    }

    /* Notes typeset corpus `$…$` math: stash TeX regions before marked so
       Markdown never mangles them, then restore HTML-escaped for MathJax. */
    function renderMd(md) {
        var slots = [];
        function stash(tex) {
            slots.push(tex);
            return 'epimath' + (slots.length - 1) + 'epi';
        }
        var s = md.replace(/\$\$([\s\S]*?)\$\$/g, function (m, t) { return stash('$$' + t + '$$'); });
        s = s.replace(/\\\[([\s\S]*?)\\\]/g, function (m, t) { return stash('\\[' + t + '\\]'); });
        s = s.replace(/\\\(([\s\S]*?)\\\)/g, function (m, t) { return stash('\\(' + t + '\\)'); });
        s = s.replace(/\$([^$\n]+?)\$/g, function (m, t) { return stash('$' + t + '$'); });
        var html = marked.parse(s);
        for (var i = 0; i < slots.length; i++) {
            html = html.split('epimath' + i + 'epi').join(esc(slots[i]));
        }
        return html;
    }

    function renderTags(tags) {
        var meta = document.querySelector('.note-meta');
        tags.forEach(function (t) {
            var a = document.createElement('a');
            a.className = 'chip';
            a.href = 'index.html?q=' + encodeURIComponent('@' + t);
            a.textContent = '#' + t;
            meta.appendChild(a);
        });
    }

    /* ---------- QA list (front-matter `qa:` metadata) ---------- */

    function openQa(title, qa) {
        document.getElementById('qa-title').textContent = title;
        document.getElementById('qa-list').innerHTML = qa.map(function (q) {
            return '<li>' + esc(q) + '</li>';
        }).join('');
        document.getElementById('qa-overlay').classList.add('open');
        document.getElementById('qa-modal').classList.add('open');
    }

    function closeQa() {
        document.getElementById('qa-overlay').classList.remove('open');
        document.getElementById('qa-modal').classList.remove('open');
    }

    function wireQa(title, qa) {
        if (!qa.length) return;
        var btn = document.getElementById('meta-qa');
        btn.hidden = false;
        btn.textContent = 'QA · ' + qa.length;
        btn.onclick = function () { openQa(title, qa); };
    }

    document.getElementById('qa-overlay').addEventListener('click', closeQa);
    document.getElementById('qa-close').addEventListener('click', closeQa);
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeQa();
    });

    /* ---------- per-file changelog history (data/changelog.json) ---------- */

    var histPromise = fetch('data/changelog.json', { headers: { 'Accept': 'application/json' } })
        .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
        .then(function (d) { return Array.isArray(d) ? d : []; })
        .catch(function () { return []; });

    function historyLinks(kind, name, l) {
        if (!l.commit) return '';
        var path = kind.corpusDir + encPath(name);
        var links =
            '<a href="' + REPO + '/commit/' + encodeURIComponent(l.commit) +
            '" target="_blank" rel="noopener">commit</a>';
        if (l.before) {
            links += '<span class="sep">|</span>' +
                '<a href="' + REPO + '/blob/' + encodeURIComponent(l.before) + '/' + path +
                '" target="_blank" rel="noopener">before</a>';
        }
        links += '<span class="sep">|</span>' +
            '<a href="' + REPO + '/blob/' + encodeURIComponent(l.commit) + '/' + path +
            '" target="_blank" rel="noopener">after</a>';
        return '<div class="hist-links">' + links + '</div>';
    }

    function openHistory(kind, name, logs) {
        var body = document.getElementById('hist-body');
        document.getElementById('hist-title').textContent = name;
        body.innerHTML = logs.slice().reverse().map(function (l) {
            return '<div class="hist-row"><div class="hist-meta">' + esc(l.date || '') +
                (l.kind ? '<span class="k">' + esc(l.kind) + '</span>' : '') + '</div>' +
                '<div class="hist-text">' + esc(l.summary || '') + '</div>' +
                historyLinks(kind, name, l) + '</div>';
        }).join('');
        document.getElementById('hist-overlay').classList.add('open');
        document.getElementById('hist-modal').classList.add('open');
    }

    function closeHistory() {
        document.getElementById('hist-overlay').classList.remove('open');
        document.getElementById('hist-modal').classList.remove('open');
    }

    function wireHistory(kind, name, list) {
        var entry = null;
        for (var i = 0; i < list.length; i++) {
            if (list[i] && list[i].file_path === name) { entry = list[i]; break; }
        }
        var logs = (entry && Array.isArray(entry.logs)) ? entry.logs : [];
        if (!logs.length) return;
        var btn = document.getElementById('meta-history');
        btn.hidden = false;
        btn.textContent = 'history';
        btn.onclick = function () { openHistory(kind, name, logs); };
    }

    document.getElementById('hist-overlay').addEventListener('click', closeHistory);
    document.getElementById('hist-close').addEventListener('click', closeHistory);
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeHistory();
    });

    /* ---------- crumbs (per kind) ---------- */

    /* Path crumbs under a corpus root; intermediate segments link to the
       catalog dir browser when linkDirs (notes) or stay plain (documents). */
    function crumbsPath(root, linkDirs) {
        return function (path) {
            var parts = path.split('/');
            var html = '<a href="index.html">' + root + '</a>';
            var prefix = [];
            for (var i = 0; i < parts.length; i++) {
                html += '<span class="sep">/</span>';
                if (i === parts.length - 1) {
                    html += '<span class="here">' + esc(parts[i].replace(/\.md$/, '')) + '</span>';
                } else if (linkDirs) {
                    prefix.push(parts[i]);
                    html += '<a href="index.html?dir=' + prefix.map(encodeURIComponent).join('/') + '">' + esc(parts[i]) + '</a>';
                } else {
                    html += '<span>' + esc(parts[i]) + '</span>';
                }
            }
            document.getElementById('crumbs').innerHTML = html;
        };
    }

    function crumbsCourse(course) {
        document.getElementById('crumbs').innerHTML =
            '<a href="index.html">courses</a><span class="sep">/</span>' +
            '<span class="here">' + esc(course) + '</span>';
    }

    function crumbsLecture(name) {
        var course = name.split('/')[0];
        var file = name.split('/')[1];
        document.getElementById('crumbs').innerHTML =
            '<a href="index.html">courses</a><span class="sep">/</span>' +
            '<a href="course.html?c=' + encodeURIComponent(course) + '">' + esc(course) + '</a>' +
            '<span class="sep">/</span>' +
            '<span class="here">' + esc(file.replace(/\.md$/, '')) + '</span>';
    }

    /* ---------- kind table ---------- */

    function fileTitleFallback(name) {
        return name.split('/').pop().replace(/\.md$/, '').replace(/-/g, ' ');
    }

    var KINDS = {
        note: {
            param: 'n',
            noun: 'note',
            usage: 'note.html?n=&lt;path&gt;',
            titleSuffix: ' — Notes',
            corpusDir: 'src/note/app/data/',
            tex: true,
            valid: validMdPath,
            fetchUrl: function (name) { return 'data/' + encPath(name); },
            titleFallback: fileTitleFallback,
            crumbs: crumbsPath('notes', true),
            historyPath: function (name) { return name; }
        },
        course: {
            param: 'c',
            noun: 'course',
            usage: 'course.html?c=&lt;course&gt;',
            titleSuffix: ' — Courses',
            corpusDir: 'src/course/app/courses/',
            tex: false,
            valid: validCourse,
            fetchUrl: function (name) { return 'courses/' + encPath(name) + '/readme.md'; },
            titleFallback: function (name) { return name.replace(/-/g, ' '); },
            crumbs: crumbsCourse,
            historyPath: function (name) { return name + '/readme.md'; },
            withLectures: true
        },
        lecture: {
            param: 'l',
            noun: 'lecture',
            usage: 'lecture.html?l=&lt;course&gt;/&lt;lecture&gt;',
            titleSuffix: ' — Courses',
            corpusDir: 'src/course/app/courses/',
            tex: false,
            valid: function (p) { return validMdPath(p) && p.split('/').length === 2; },
            fetchUrl: function (name) { return 'courses/' + encPath(name); },
            titleFallback: fileTitleFallback,
            crumbs: crumbsLecture,
            historyPath: function (name) { return name; }
        },
        document: {
            param: 'd',
            noun: 'document',
            usage: 'document.html?d=&lt;path&gt;',
            titleSuffix: ' — Documents',
            corpusDir: 'src/document/app/documents/',
            tex: false,
            valid: validMdPath,
            fetchUrl: function (name) { return 'documents/' + encPath(name); },
            titleFallback: fileTitleFallback,
            crumbs: crumbsPath('documents', false),
            historyPath: function (name) { return name; }
        }
    };

    function renderLectures(course, lectures) {
        if (!lectures.length) return;
        var body = document.getElementById('note-body');
        var h2 = document.createElement('h2');
        h2.textContent = 'Lectures';
        body.appendChild(h2);
        var ul = document.createElement('ul');
        lectures.forEach(function (l) {
            var li = document.createElement('li');
            var a = document.createElement('a');
            a.href = 'lecture.html?l=' + encPath(l.path);
            a.textContent = l.title;
            li.appendChild(a);
            if (l.tags && l.tags.length) {
                li.appendChild(document.createTextNode('  ' + l.tags.map(function (t) { return '#' + t; }).join(' ')));
            }
            ul.appendChild(li);
        });
        body.appendChild(ul);
    }

    function buildToc() {
        var headings = document.querySelectorAll('#note-body h2, #note-body h3');
        var toc = document.getElementById('toc');
        toc.innerHTML = '';
        if (!headings.length) { document.getElementById('sidebar').hidden = true; return; }
        document.getElementById('sidebar').hidden = false;
        headings.forEach(function (h, i) {
            h.id = 'sec-' + i;
            var a = document.createElement('a');
            a.href = '#sec-' + i;
            a.className = 'toc-item' + (h.tagName === 'H3' ? ' sub' : '');
            a.textContent = h.textContent;
            a.addEventListener('click', function (e) {
                e.preventDefault();
                h.scrollIntoView({ behavior: 'smooth', block: 'start' });
            });
            toc.appendChild(a);
        });

        var items = toc.querySelectorAll('.toc-item');
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                var idx = Array.prototype.indexOf.call(headings, entry.target);
                items.forEach(function (it) { it.classList.remove('active'); });
                if (items[idx]) items[idx].classList.add('active');
            });
        }, { rootMargin: '-10% 0px -60% 0px' });
        headings.forEach(function (h) { observer.observe(h); });
    }

    /* ---------- load flow ---------- */

    var kind = KINDS[kindName];

    if (!kind) {
        fail('Unknown viewer kind: "' + kindName + '".');
        return;
    }

    var params = new URLSearchParams(window.location.search);
    var name = params.get(kind.param) || '';

    if (!kind.valid(name)) {
        fail(name ? 'Invalid ' + kind.noun + ' path: "' + name + '".' : 'No ' + kind.noun + ' specified. Use ' + kind.usage + '.');
    } else {
        fetch(kind.fetchUrl(name))
            .then(function (r) {
                if (!r.ok) throw new Error('HTTP ' + r.status);
                return r.text();
            })
            .then(function (md) {
                var fm = stripFrontMatter(md);
                md = fm.body;
                var title = null;
                var lines = md.split('\n');
                for (var i = 0; i < lines.length; i++) {
                    var m = lines[i].match(/^#\s+(.+?)\s*#*\s*$/);
                    if (m) { title = m[1]; break; }
                }
                if (!title) title = kind.titleFallback(name);

                document.title = title + kind.titleSuffix;
                document.getElementById('note-title').textContent = title;
                kind.crumbs(name);

                var words = md.split(/\s+/).filter(Boolean).length;
                document.getElementById('meta-words').textContent = words + ' words';
                document.getElementById('meta-time').textContent = Math.max(1, Math.ceil(words / 200)) + ' min read';
                document.getElementById('meta-raw').setAttribute('href', kind.fetchUrl(name));
                renderTags(fm.tags);
                wireQa(title, fm.qa);
                histPromise.then(function (list) { wireHistory(kind, kind.historyPath(name), list); });

                document.getElementById('note-body').innerHTML = kind.tex ? renderMd(md) : marked.parse(md);
                if (kind.withLectures) {
                    return fetch('data/index.json', { headers: { 'Accept': 'application/json' } })
                        .then(function (r) {
                            if (!r.ok) throw new Error('HTTP ' + r.status);
                            return r.json();
                        })
                        .then(function (idx) {
                            return (idx.entries || []).filter(function (e) {
                                return e.kind === 'lecture' && e.course === name;
                            });
                        })
                        .catch(function () { return []; });
                }
            })
            .then(function (lectures) {
                if (kind.withLectures && Array.isArray(lectures)) renderLectures(name, lectures);
                document.getElementById('loading').hidden = true;
                document.getElementById('note-header').hidden = false;
                document.getElementById('note-card').hidden = false;
                buildToc();
                if (kind.tex && window.renderTeX) renderTeX();
            })
            .catch(function (err) {
                fail(err.message === 'HTTP 404' ? 'The ' + kind.noun + ' "' + name + '" does not exist.' : 'Failed to load the ' + kind.noun + ' (' + err.message + ').');
            });
    }
})();
