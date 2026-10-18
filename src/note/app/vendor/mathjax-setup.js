/* Epistecnica — shared MathJax 3 setup (tex-svg-full).
   Load BEFORE vendor/mathjax/tex-svg-full.js. Then:
     window.renderTeX(root?)   // typeset [data-tex] / [data-tex-display] nodes
   MathJax auto-typesets the document on load; call renderTeX() again after any
   dynamic DOM update (instance switch, viewer navigation, ...). Passing no
   argument (or `document`) typesets the whole body. */
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true
  },
  svg: { fontCache: 'local' },
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    ignoreHtmlClass: 'no-mathjax'
  },
  startup: { typeset: true }
};

window.renderTeX = function (root) {
  if (!(window.MathJax && MathJax.typesetPromise)) return Promise.resolve();
  root = root || document;
  var scope = (root === document || root === document.documentElement) ? document.body : root;
  if (!scope) return Promise.resolve();
  var nodes = scope.querySelectorAll('[data-tex],[data-tex-display]');
  for (var i = 0; i < nodes.length; i++) {
    var el = nodes[i];
    var d = el.getAttribute('data-tex-display');
    var tex = (d != null) ? d : el.getAttribute('data-tex');
    if (tex == null) continue;
    el.textContent = (d != null) ? ('\\[' + tex + '\\]') : ('\\(' + tex + '\\)');
  }
  var ready = (MathJax.startup && MathJax.startup.promise) ? MathJax.startup.promise : Promise.resolve();
  return ready.then(function () { return MathJax.typesetPromise([scope]); });
};
