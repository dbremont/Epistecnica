/* Epistecnica — shared page chrome behaviour.
   Wires the `#themeToggle` button declared by the standard nav on pages that do
   not mount a TreeCatalog (which wires it itself). Stores the choice under the
   site-wide `epistecnica-theme` key read by every page's head script. */
(function () {
    'use strict';
    if (window.__epistecnicaChromeWired) return;
    window.__epistecnicaChromeWired = true;

    var btn = document.getElementById('themeToggle');
    if (!btn) return;
    var label = document.getElementById('themeLabel');
    var root = document.documentElement;

    function paint() {
        if (label) label.textContent = root.dataset.theme === 'light' ? 'DARK' : 'LIGHT';
    }

    paint();
    btn.addEventListener('click', function () {
        root.classList.add('theme-fading');
        window.setTimeout(function () {
            root.dataset.theme = root.dataset.theme === 'light' ? 'dark' : 'light';
            try { localStorage.setItem('epistecnica-theme', root.dataset.theme); } catch (e) { /* ignore */ }
            paint();
            root.classList.remove('theme-fading');
        }, 120);
    });
})();
