
    const typeIcons = {
      Temporal: `<svg class="type-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 12V8M6 12V5M9 12V9M12 12V4" stroke-linecap="round"/></svg>`,
      Spatial: `<svg class="type-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M8 3L13 6V10L8 13L3 10V6L8 3Z" stroke-linejoin="round"/></svg>`,
      Network: `<svg class="type-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="8" cy="8" r="1.5"/><circle cx="4" cy="5" r="1"/><circle cx="12" cy="11" r="1"/><path d="M8 6.5L4.5 5.5M8 9.5L11.5 10.5" stroke-linecap="round"/></svg>`
    };
    typeIcons.Corpus = `<svg class="type-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="3" y="5" width="10" height="8" rx="1"/><path d="M5 5V4a1 1 0 011-1h7v8"/></svg>`;
    typeIcons.note = `<svg class="type-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 2h6l3 3v9H4z" stroke-linejoin="round"/><path d="M10 2v3h3" stroke-linejoin="round"/></svg>`;

    // Preview icons
    const previewIcons = {
      Temporal: `<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M8 40V24M16 40V16M24 40V28M32 40V12M40 40V20" stroke-linecap="round"/></svg>`,
      Spatial: `<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M24 8L40 18V30L24 40L8 30V18L24 8Z" stroke-linejoin="round"/></svg>`,
      Network: `<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="24" cy="24" r="4"/><circle cx="12" cy="14" r="3"/><circle cx="36" cy="34" r="3"/><path d="M24 20L12 17M24 28L36 31" stroke-linecap="round"/></svg>`
    };
    previewIcons.Corpus = `<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="10" y="16" width="28" height="24" rx="2"/><path d="M16 16v-4a2 2 0 012-2h20v24"/></svg>`;
    previewIcons.note = `<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M14 6h14l8 8v28H14z" stroke-linejoin="round"/><path d="M28 6v8h8" stroke-linejoin="round"/></svg>`;

    // Theme & Scroll Logic
    const themeToggle = document.getElementById('themeToggle');
    const scrollProgress = document.getElementById('scrollProgress');
    const projectHeader = document.getElementById('projectHeader');
    const htmlElement = document.documentElement;

    const getStoredTheme = () => localStorage.getItem('naturgnosis-theme');

    function setTheme(theme) {
      htmlElement.classList.toggle('dark', theme === 'dark');
      localStorage.setItem('naturgnosis-theme', theme);
    }
    
    setTheme(getStoredTheme() || 'dark');

    themeToggle.addEventListener('click', () => {
      const newTheme = htmlElement.classList.contains('dark') ? 'light' : 'dark';
      setTheme(newTheme);
    });

    function updateScrollProgress() {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? scrollTop / docHeight : 0;
      scrollProgress.style.transform = `scaleX(${progress})`;
      if (scrollTop > 10) projectHeader.classList.add('scrolled');
      else projectHeader.classList.remove('scrolled');
    }

    window.addEventListener('scroll', updateScrollProgress, { passive: true });
    updateScrollProgress();

    // Reveal Animation
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce').matches;
    if (!prefersReducedMotion) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
      document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    } else {
      document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
    }

    // Data Loading & Rendering
    // Works are precomputed by the manifest builder from each polity dir:
    // representation links are polity-relative ("actor.html"), explanation
    // links are ready note-viewer URLs. Legacy node works used a "rep/..."
    // path we still remap for safety.
    function polityWorkLink(link) {
      if (!link) return link;
      if (/^(https?:|\/|\.\.\/)/.test(link)) return link;
      if (/^rep\//.test(link)) return '/nation/web/' + link;
      return link;
    }

    async function initPage() {
      try {
        const pathCode = (window.location.pathname.match(/polity\/([^/]+)\//) || [])[1] || '';
        const params = new URLSearchParams(window.location.search);
        const code = (pathCode || params.get('code') || '').toLowerCase();
        const [nodeRes, manRes] = await Promise.all([
          fetch('data/node.json'),
          fetch('../data.json')
        ]);
        // data/node.json is the polity's own node (source of truth); codes
        // without one fall back to the manifest entry alone.
        const node = nodeRes.ok ? await nodeRes.json() : null;
        let manifestEntry = null;
        if (manRes.ok) {
          const manifest = await manRes.json();
          manifestEntry = (manifest.codes && manifest.codes[code]) || null;
        }
        const fb = {
          name: (manifestEntry && manifestEntry.name) || code.toUpperCase(),
          native: (manifestEntry && manifestEntry.native) || '',
          flag: (manifestEntry && manifestEntry.flag) || '\u{1F3F3}\uFE0F'
        };
        if (!node && !manifestEntry) throw new Error('Polity not found: ' + code);
        const sp = (node && node.specific) || {};
        const works = (manifestEntry && manifestEntry.works) || sp.works || [];
        const data = node ? {
          meta: {
            title: ((sp.flagEmoji || '') + ' ' + (node.name || '')).trim(),
            flagEmoji: sp.flagEmoji || '',
            breadcrumbName: node.name || ''
          },
          identity: {
            category: node.category || 'Polity',
            name: node.name || '',
            nativeName: sp.nativeName || '',
            tags: node.tags || []
          },
          definition: { text: node.description || '' },
          statistics: sp.statistics || [],
          works: works,
          references: node.references || [],
          footer: sp.footer || {}
        } : {
          meta: { title: fb.name, flagEmoji: fb.flag, breadcrumbName: fb.name },
          identity: { category: 'Polity', name: fb.name, nativeName: fb.native, tags: [] },
          definition: { text: 'Corpus entries for this polity are listed below.' },
          statistics: [], works: works, references: [],
          footer: { entityCode: code.toUpperCase(), region: '', lastRevised: '',
            links: [
              { label: 'Polity Index', href: '/note/data/social/collective/actor/public/polity/index.html' },
              { label: 'Catalog', href: '/note/web/index.html' }
            ] }
        };
        renderData(data);

        // Header identity: the subtitle carries the country name and links to
        // the polity's directory view in the notes catalog.
        const subtitle = document.getElementById('projectSubtitle');
        if (subtitle) {
          subtitle.textContent = data.identity.name;
          subtitle.href = '/note/web/index.html?dir=' +
            encodeURIComponent('social/collective/actor/public/polity/' + code);
        }
      } catch (error) {
        console.error('Failed to load country data:', error);
        document.getElementById('definitionText').textContent = "Error loading data. Please check console.";
      }
    }

    function renderFooter(data) {
        // Footer Metadata - Matching Source Style
        const footerMeta = document.getElementById('footerMetadata');
        footerMeta.innerHTML = `
            <div class="flex justify-center md:justify-end items-baseline gap-3">
                <span class="footer-meta-label">Entity Code</span>
                <span class="font-medium tabular-nums footer-meta-value">${data.footer.entityCode}</span>
            </div>
            <div class="flex justify-center md:justify-end items-baseline gap-3">
                <span class="footer-meta-label">Region</span>
                <span class="font-medium footer-meta-value">${data.footer.region}</span>
            </div>
            <div class="flex justify-center md:justify-end items-baseline gap-3">
                <span class="footer-meta-label">Last Revised</span>
                <span class="footer-meta-value">${data.footer.lastRevised}</span>
            </div>
        `;
        
        // Dynamic Links - Matching Source Style
        const linksContainer = document.getElementById("footerLinks");
        linksContainer.innerHTML = "";

        (data.footer.links || []).forEach(link => {
            const a = document.createElement("a");
            a.href = link.href;
            a.textContent = link.label;
            // Using the .footer-link class defined in CSS for colors
            a.className = "footer-link font-body text-xs"; 
            linksContainer.appendChild(a);
        });
    }


    function renderData(data) {
      // Meta
      document.title = data.meta.title;
      document.getElementById('breadcrumbCurrent').textContent = data.meta.breadcrumbName;

      // Identity
      document.getElementById('flagIcon').textContent = data.meta.flagEmoji;
      document.getElementById('countryName').textContent = data.identity.name;
      document.getElementById('nativeName').textContent = data.identity.nativeName;

      const tagContainer = document.getElementById('tagContainer');
      tagContainer.innerHTML = '';
      data.identity.tags.forEach(tag => {
        const span = document.createElement('span');
        span.className = 'tag-pill';
        span.textContent = tag;
        tagContainer.appendChild(span);
      });

      // Definition
      document.getElementById('definitionText').textContent = data.definition.text;

      // Statistics
      const statsGrid = document.getElementById('statsGrid');
      statsGrid.innerHTML = '';
      data.statistics.forEach(stat => {
        const card = document.createElement('div');
        card.className = 'data-card';
        card.tabIndex = 0;
        
        let indicatorHtml = '';
        if (stat.hasIndicator) {
          indicatorHtml = `<div class="data-indicator"><div class="data-indicator-fill" style="width: ${stat.indicatorValue}%;"></div></div>`;
        }

        let labelHtml = stat.label;
        if (stat.id === 'area') {
          labelHtml = `Area km<sup>2</sup>`;
        }

        card.innerHTML = `
          <div class="font-display type-data-value font-medium text-fg">${stat.value}</div>
          <div class="font-body type-label text-muted uppercase font-medium">${labelHtml}</div>
          ${indicatorHtml}
        `;
        statsGrid.appendChild(card);
      });

      // Works
      const worksGrid = document.getElementById('worksGrid');
      worksGrid.innerHTML = '';
      
      data.works.forEach(work => {
        const isActive = work.status === 'active';
        const tagType = isActive ? 'a' : 'article';
        const card = document.createElement(tagType);

        card.className = 'entity-card group';
        card.setAttribute('data-state', work.status);
        card.setAttribute('data-type', work.type);
        card.setAttribute('data-work-id', work.id);
        
        if (isActive) {
          card.setAttribute('href', polityWorkLink(work.link) || '#');
          card.setAttribute('target', '_blank');
          card.setAttribute('aria-label', `View ${work.title} dataset`);
        } else {
          card.setAttribute('aria-disabled', 'true');
          card.setAttribute('role', 'article');
        }

        const previewSvg = previewIcons[work.type] || previewIcons['Temporal'];
        const typeIconSvg = typeIcons[work.type] || typeIcons['Temporal'];
        const statusText = isActive ? 'Active' : 'Pending';

        const ctaHtml = !isActive
          ? `<span class="font-meta type-meta text-muted uppercase">Coming MMXXV</span>`
          : `<span class="card-cta type-secondary">View<svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>`;

        card.innerHTML = `
          <div class="card-preview">${previewSvg}</div>
          <div class="card-content">
            <div class="flex items-center justify-between mb-3">
              <span class="card-tag" data-type="${work.type}">${typeIconSvg}${work.type}</span>
              <span class="status-badge">
                <span class="status-dot" data-state="${work.status}"></span>
                ${statusText}
              </span>
            </div>
            <h3 class="font-display type-card-title font-medium text-fg mb-1.5 card-title">${work.title}</h3>
            <p class="font-body type-secondary text-muted leading-relaxed card-description">${work.description}</p>
            ${ctaHtml}
          </div>
        `;

        worksGrid.appendChild(card);
      });

      // References
      const referencesGrid = document.getElementById('referencesGrid');
      referencesGrid.innerHTML = '';
      if (!data.references.length) {
        const p = document.createElement('p');
        p.className = 'ref-empty md:col-span-2';
        p.textContent = 'No references yet.';
        referencesGrid.appendChild(p);
      } else {
        data.references.forEach(ref => {
          const a = document.createElement('a');
          a.className = 'ref-card';
          a.href = ref.link || '#';
          a.setAttribute('aria-label', ref.title || 'Reference');
          const h = document.createElement('h3');
          h.textContent = ref.title || '(untitled)';
          const d = document.createElement('p');
          d.textContent = ref.description || '';
          a.appendChild(h);
          a.appendChild(d);
          referencesGrid.appendChild(a);
        });
      }

      renderFooter(data)
    }

    initPage();
