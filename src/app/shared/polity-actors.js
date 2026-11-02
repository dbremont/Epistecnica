
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
      if (typeof timeline !== 'undefined') timeline.render();
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

    // Data Model
    const DataModel = {
      actors: [], events: [],
      activeTypes: { private: true, hybrid: true, public: true },
      searchQuery: '',

      async init() {
        try {
          const params = new URLSearchParams(window.location.search);
          const pathCode = (window.location.pathname.match(/polity\/([^/]+)\//) || [])[1] || '';
          const code = (pathCode || params.get('code') || 'irl').toLowerCase();
          this.code = code;
          const response = await fetch('data/actors.json');
          if (!response.ok) throw new Error('Network error');
          this.processData(await response.json());
        } catch (e) {
          console.error('Failed to load actor data:', e);
        }
      },

      processData(raw) {
        // --- Dynamic Metadata Injection ---
        // setText() guards: a missing element logs instead of killing the render.
        const setText = function (id, value) {
          var el = document.getElementById(id);
          if (el) el.textContent = value;
          else if (typeof console !== 'undefined' && console.warn) console.warn('polity-actors: missing element #' + id);
        };
        const meta = raw.metadata || raw;

        // 1. Title and Hero Country Name
        if (meta.country) {
          setText('docTitle', meta.flag + ' Actor Space');
          setText('heroRegion', meta.country);
          // Header identity: the subtitle carries the country name and links
          // to the polity's directory view in the notes catalog (mirrors
          // polity-entry.js on the per-polity entry page).
          var subtitle = document.getElementById('projectSubtitle');
          if (subtitle) {
            subtitle.textContent = meta.country;
            if (this.code) {
              subtitle.href = '/note/web/index.html?dir=' +
                encodeURIComponent('social/collective/actor/public/polity/' + this.code);
            }
          }
        }

        // 2. Introduction Text
        if (meta.introduction) {
          setText('introText', meta.introduction);
        }

        // 3. Footer Status Fields
        // Handle JSON typo "peerReview'" by checking both keys
        const peerReview = meta.peerReview || meta["peerReview'"];
        if (peerReview) {
          setText('footerPeerReview', peerReview);
        }

        if (meta.evidenceConfidence) {
          setText('footerConfidence', meta.evidenceConfidence);
        }

        if (meta.region) {
          setText('footerRegion', meta.region);
        }

        if (meta.lastUpdated) {
          // Parse "2026-02-16" to "2026.02" format
          try {
            const d = new Date(meta.lastUpdated);
            if (!isNaN(d)) {
              const formatted = d.getFullYear() + '.' + String(d.getMonth() + 1).padStart(2, '0');
              setText('footerLastRevised', formatted);
            } else {
              setText('footerLastRevised', meta.lastUpdated);
            }
          } catch {
            setText('footerLastRevised', meta.lastUpdated);
          }
        }
        // -----------------------------------

        this.actors = raw.actors || (Array.isArray(raw) ? raw : []);
        this.events = [];
        this.actors.forEach(actor => {
          (actor.events || []).forEach(ev => {
            const d = new Date(ev.date);
            if (!isNaN(d)) {
              this.events.push({
                id: `${actor.id}-${ev.date}`,
                date: d,
                type: ev.category || 'other',
                desc: ev.description,
                actorId: actor.id,
                actorName: actor.name,
                actorType: actor.type
              });
            }
          });
        });
        this.events.sort((a, b) => a.date - b.date);

        document.getElementById('stat-actors').textContent = this.actors.length;
        document.getElementById('stat-events').textContent = this.events.length;

        if (this.events.length > 0) {
          const minYear = this.events[0].date.getFullYear();
          const maxYear = this.events[this.events.length - 1].date.getFullYear();
          const range = maxYear - minYear;
          document.getElementById('stat-range').textContent = range;
          document.getElementById('stat-decades').textContent = Math.ceil(range / 10);
        }

        const roles = new Set(this.actors.map(a => a.role).filter(Boolean));
        document.getElementById('stat-roles').textContent = roles.size;

        const regions = new Set(this.actors.map(a => a.regionOfActivity).filter(Boolean));
        document.getElementById('stat-regions').textContent = regions.size;
      },

      getFiltered() {
        const q = this.searchQuery.toLowerCase();
        return this.events.filter(ev => {
          if (!this.activeTypes[ev.actorType]) return false;
          if (!q) return true;

          const actor = this.getActorById(ev.actorId);
          if (!actor) return false;

          const searchFields = [
            actor.id,
            actor.name,
            actor.type,
            actor.role,
            actor.regionOfActivity,
            actor.description,
            ev.desc,
            ev.type
          ];

          return searchFields.some(field =>
            field && String(field).toLowerCase().includes(q)
          );
        });
      },

      getActorById(id) { return this.actors.find(a => a.id === id); }
    };

    // Timeline Engine
    class Timeline {
      constructor() {
        this.state = { zoom: 1, panY: 0 };
        this.container = document.getElementById('timelineContainer');
        this.canvas = document.getElementById('timelineCanvas');
        this.ctx = this.canvas.getContext('2d');

        this.axisCanvas = document.getElementById('axisCanvas');
        this.axisCtx = this.axisCanvas.getContext('2d');

        this.minimapCanvas = document.getElementById('minimapCanvas');
        this.minimapCtx = this.minimapCanvas.getContext('2d');
        this.minimapContainer = document.getElementById('minimapContainer');

        this.layout = { ml: 10, mt: 20, mb: 20, mr: 10, laneW: 0, cols: {} };

        this.hoveredEvents = [];
        this.packed = new Map();
        this.isTooltipHovered = false;

        this.keyboardState = {
          yearBuffer: '',
          yearInputActive: false,
          yearInputTimeout: null
        };

        this.init();
      }

      init() {
        this.resize();
        this.bindEvents();
        this.render();
      }

      resize() {
        const dpr = window.devicePixelRatio || 1;

        const rect = this.container.getBoundingClientRect();
        this.canvas.width = rect.width * dpr;
        this.canvas.height = rect.height * dpr;
        this.ctx.scale(dpr, dpr);
        this.layout.w = rect.width;
        this.layout.h = rect.height;

        const axisRect = this.axisCanvas.parentElement.getBoundingClientRect();
        this.axisCanvas.width = axisRect.width * dpr;
        this.axisCanvas.height = axisRect.height * dpr;
        this.axisCtx.scale(dpr, dpr);

        const mmRect = this.minimapContainer.getBoundingClientRect();
        this.minimapCanvas.width = mmRect.width * dpr;
        this.minimapCanvas.height = mmRect.height * dpr;
        this.minimapCtx.scale(dpr, dpr);

        const chartW = this.layout.w - this.layout.ml - this.layout.mr;
        this.layout.laneW = chartW / 3;
        this.layout.cols.private = this.layout.ml;
        this.layout.cols.hybrid = this.layout.ml + this.layout.laneW;
        this.layout.cols.public = this.layout.ml + this.layout.laneW * 2;

        this.pack();
        this.render();
      }

      bindEvents() {
        window.addEventListener('resize', () => this.resize());

        this.canvas.addEventListener('wheel', e => { e.preventDefault(); this.zoom(e.deltaY > 0 ? 0.9 : 1.1); }, { passive: false });
        this.canvas.addEventListener('mousedown', e => this.onDragStart(e));
        this.canvas.addEventListener('mousemove', e => this.onHover(e));

        this.canvas.addEventListener('mouseleave', () => {
          setTimeout(() => {
            if (!this.isTooltipHovered) {
              this.hoveredEvents = [];
              this.hideTooltip();
              this.render();
            }
          }, 50);
        });

        const tooltipEl = document.getElementById('tooltip');
        tooltipEl.addEventListener('mouseenter', () => { this.isTooltipHovered = true; });
        tooltipEl.addEventListener('mouseleave', () => {
          this.isTooltipHovered = false;
          this.hoveredEvents = [];
          this.hideTooltip();
          this.render();
        });

        this.canvas.addEventListener('click', () => {
          if (this.hoveredEvents.length > 0) {
            this.openSidebar(DataModel.getActorById(this.hoveredEvents[0].actorId));
          }
        });

        this.container.addEventListener('keydown', e => this.onKeyDown(e));

        const searchInput = document.getElementById('searchInput');
        searchInput.addEventListener('input', e => {
          DataModel.searchQuery = e.target.value;
          this.applyFilters();
        });

        // Blur search on Escape and return focus to canvas
        searchInput.addEventListener('keydown', (e) => {
          if (e.key === 'Escape') {
            e.preventDefault();
            searchInput.value = '';
            DataModel.searchQuery = '';
            searchInput.blur();
            this.container.focus();
            this.applyFilters();
          }
        });

        this.minimapContainer.addEventListener('mousedown', e => this.onMinimapDragStart(e));

        document.getElementById('btnZoomIn').addEventListener('click', () => this.zoom(1.4));
        document.getElementById('btnZoomOut').addEventListener('click', () => this.zoom(0.7));
        document.getElementById('btnReset').addEventListener('click', () => this.resetView());
        document.getElementById('btnFitAll').addEventListener('click', () => this.fit());

        const helpBackdrop = document.getElementById('helpBackdrop');
        document.getElementById('btnHelp').addEventListener('click', () => this.showHelp());
        document.getElementById('closeHelp').addEventListener('click', () => this.hideHelp());
        helpBackdrop.addEventListener('click', (e) => { if (e.target === helpBackdrop) this.hideHelp(); });

        document.getElementById('sidebarBackdrop').addEventListener('click', () => this.closeSidebar());
        document.getElementById('close-sidebar').addEventListener('click', () => this.closeSidebar());

        document.addEventListener('keydown', (e) => {
          if (e.key === 'Escape') {
            if (helpBackdrop.classList.contains('visible')) {
              this.hideHelp();
              e.preventDefault();
            }
            if (document.getElementById('sidebar').classList.contains('open')) {
              this.closeSidebar();
              e.preventDefault();
            }
          }
        });
      }

      onKeyDown(e) {
        const key = e.key;

        if (this.keyboardState.yearInputActive) {
          this.handleYearInputKey(e);
          return;
        }

        if (document.activeElement.id === 'searchInput') {
          return;
        }

        if (key === 'ArrowUp' || key === 'k' || key === 'K') {
          e.preventDefault();
          this.panUp();
          return;
        }

        if (key === 'ArrowDown' || key === 'j' || key === 'J') {
          e.preventDefault();
          this.panDown();
          return;
        }

        if (key === '+' || key === '=') {
          e.preventDefault();
          this.zoom(1.4);
          return;
        }

        if (key === '-') {
          e.preventDefault();
          this.zoom(0.7);
          return;
        }

        if (key === 'r' || key === 'R') {
          e.preventDefault();
          this.resetView();
          return;
        }

        if (key === 'f' || key === 'F') {
          e.preventDefault();
          this.fit();
          return;
        }

        if (key === '?' || key === 'h' || key === 'H') {
          e.preventDefault();
          this.showHelp();
          return;
        }

        // Search focus
        if (key === 's' || key === 'S') {
          e.preventDefault();
          document.getElementById('searchInput').focus();
          return;
        }

        if (/^[0-9]$/.test(key)) {
          e.preventDefault();
          this.startYearInput(key);
          return;
        }
      }

      handleYearInputKey(e) {
        const key = e.key;

        if (/^[0-9]$/.test(key)) {
          if (this.keyboardState.yearBuffer.length < 4) {
            this.keyboardState.yearBuffer += key;
            this.updateYearInputDisplay();
          }
          this.resetYearInputTimeout();
          return;
        }

        if (key === 'Enter') {
          e.preventDefault();
          this.navigateToYear();
          return;
        }

        if (key === 'Backspace') {
          e.preventDefault();
          this.keyboardState.yearBuffer = this.keyboardState.yearBuffer.slice(0, -1);
          if (this.keyboardState.yearBuffer.length === 0) {
            this.cancelYearInput();
          } else {
            this.updateYearInputDisplay();
            this.resetYearInputTimeout();
          }
          return;
        }

        if (key === 'Escape') {
          e.preventDefault();
          this.cancelYearInput();
          return;
        }

        if (key === 'ArrowUp' || key === 'k') {
          e.preventDefault();
          this.panUp();
          return;
        }
        if (key === 'ArrowDown' || key === 'j') {
          e.preventDefault();
          this.panDown();
          return;
        }
      }

      startYearInput(digit) {
        this.keyboardState.yearInputActive = true;
        this.keyboardState.yearBuffer = digit;
        this.updateYearInputDisplay();
        this.resetYearInputTimeout();
      }

      resetYearInputTimeout() {
        if (this.keyboardState.yearInputTimeout) {
          clearTimeout(this.keyboardState.yearInputTimeout);
        }
        this.keyboardState.yearInputTimeout = setTimeout(() => {
          this.cancelYearInput();
        }, 3000);
      }

      updateYearInputDisplay() {
        const indicator = document.getElementById('yearInputIndicator');
        const valueEl = document.getElementById('yearInputValue');
        valueEl.textContent = this.keyboardState.yearBuffer;
        indicator.classList.add('visible');
      }

      navigateToYear() {
        const year = parseInt(this.keyboardState.yearBuffer, 10);
        if (!isNaN(year) && year >= 1800 && year <= 2025) {
          this.goToYear(year);
        }
        this.cancelYearInput();
      }

      cancelYearInput() {
        if (this.keyboardState.yearInputTimeout) {
          clearTimeout(this.keyboardState.yearInputTimeout);
        }
        this.keyboardState.yearInputActive = false;
        this.keyboardState.yearBuffer = '';
        document.getElementById('yearInputIndicator').classList.remove('visible');
      }

      goToYear(year) {
        const range = (2025 - 1800) / this.state.zoom;
        this.state.panY = (1912.5 - year) / range;
        this.render();
      }

      panUp() {
        const panAmount = 0.05 / this.state.zoom;
        this.state.panY += panAmount;
        this.render();
      }

      panDown() {
        const panAmount = 0.05 / this.state.zoom;
        this.state.panY -= panAmount;
        this.render();
      }

      resetView() {
        this.state.zoom = 1;
        this.state.panY = 0;
        this.render();
      }

      showHelp() {
        document.getElementById('helpBackdrop').classList.add('visible');
        document.getElementById('closeHelp').focus();
      }

      hideHelp() {
        document.getElementById('helpBackdrop').classList.remove('visible');
        this.container.focus();
      }

      applyFilters() {
        this.pack();
        this.render();
      }

      yearToY(y) {
        const range = (2025 - 1800) / this.state.zoom;
        const center = (1800 + 2025) / 2 - this.state.panY * range;
        return this.layout.mt + ((y - (center - range / 2)) / range) * (this.layout.h - this.layout.mt - this.layout.mb);
      }

      pack() {
        this.packed.clear();
        const events = DataModel.getFiltered();
        const groups = { private: {}, hybrid: {}, public: {} };
        events.forEach(d => {
          const y = d.date.getFullYear();
          if (!groups[d.actorType][y]) groups[d.actorType][y] = [];
          groups[d.actorType][y].push(d);
        });
        Object.keys(groups).forEach(type => {
          const laneX = this.layout.cols[type] + this.layout.laneW / 2;
          Object.keys(groups[type]).forEach(year => {
            const evts = groups[type][year];
            const step = Math.min(30, (this.layout.laneW - 20) / evts.length);
            const startX = laneX - (evts.length - 1) * step / 2;
            evts.forEach((e, i) => this.packed.set(e.id, { x: startX + i * step }));
          });
        });
      }

      render() {
        this.renderAxis();
        this.renderMain();
        this.renderMinimap();
      }

      renderAxis() {
        const ctx = this.axisCtx;
        const w = this.axisCanvas.width / (window.devicePixelRatio || 1);
        const h = this.axisCanvas.height / (window.devicePixelRatio || 1);
        const isDark = document.documentElement.classList.contains('dark');

        ctx.clearRect(0, 0, w, h);

        const cssVar = (name) =>
          getComputedStyle(document.documentElement).getPropertyValue(name).trim();
        const textColor = cssVar('--muted');
        const tickColor = cssVar('--muted');
        const majorTickColor = cssVar(isDark ? '--text-secondary' : '--fg');

        const range = (2025 - 1800) / this.state.zoom;
        const center = (1800 + 2025) / 2 - this.state.panY * range;
        const start = Math.ceil(center - range / 2);

        let majorStep = 25;
        let minorStep = 5;
        if (range < 100) { majorStep = 20; minorStep = 5; }
        if (range < 60) { majorStep = 10; minorStep = 5; }
        if (range < 30) { majorStep = 5; minorStep = 1; }

        const tickAnchorX = 30;

        for (let y = Math.floor(start / minorStep) * minorStep; y < start + range; y += minorStep) {
          const py = this.yearToY(y);
          if (py < 20 || py > h - 20) continue;

          const isMajor = y % majorStep === 0;
          const isCentury = y % 100 === 0;

          ctx.lineWidth = 1;
          ctx.beginPath();

          if (isMajor) {
            ctx.strokeStyle = majorTickColor;
            ctx.moveTo(tickAnchorX, py);
            ctx.lineTo(tickAnchorX + 10, py);
            ctx.stroke();

            ctx.font = isCentury
              ? '600 12px "Cormorant Garamond", Georgia, serif'
              : '500 11px "Cormorant Garamond", Georgia, serif';
            ctx.textAlign = 'right';
            ctx.textBaseline = 'middle';
            ctx.fillStyle = isCentury ? cssVar('--fg') : textColor;
            ctx.fillText(y.toString(), tickAnchorX - 6, py);
          } else {
            ctx.strokeStyle = tickColor;
            ctx.globalAlpha = 0.5;
            ctx.moveTo(tickAnchorX + 4, py);
            ctx.lineTo(tickAnchorX + 7, py);
            ctx.stroke();
            ctx.globalAlpha = 1;
          }
        }
      }

      getActorColor(type) {
        const style = getComputedStyle(document.documentElement);
        if (type === 'private') return style.getPropertyValue('--private').trim();
        if (type === 'hybrid') return style.getPropertyValue('--hybrid').trim();
        return style.getPropertyValue('--public').trim();
      }

      _drawNode(ctx, x, y, type, color, isHovered) {
        const radius = isHovered ? 5.5 : 4;

        ctx.save();

        if (isHovered) {
          ctx.strokeStyle = color;
          ctx.lineWidth = 1;
          ctx.globalAlpha = 0.3;
          ctx.beginPath();
          ctx.arc(x, y, radius + 4, 0, Math.PI * 2);
          ctx.stroke();
          ctx.globalAlpha = 1;
        }

        ctx.fillStyle = color;
        ctx.strokeStyle = color;
        ctx.lineWidth = 1.5;

        if (type === 'private') {
          ctx.beginPath();
          ctx.arc(x, y, radius, 0, Math.PI * 2);
          ctx.fill();
        } else if (type === 'hybrid') {
          ctx.beginPath();
          ctx.arc(x, y, radius, 0, Math.PI * 2);
          ctx.stroke();
        } else if (type === 'public') {
          ctx.fillRect(x - radius, y - radius, radius * 2, radius * 2);
        }

        ctx.restore();
      }

      renderMain() {
        const ctx = this.ctx;
        const w = this.layout.w, h = this.layout.h;
        const events = DataModel.getFiltered();

        ctx.clearRect(0, 0, w, h);

        const style = getComputedStyle(document.documentElement);
        ctx.strokeStyle = style.getPropertyValue('--border').trim();
        ctx.lineWidth = 1;
        ctx.globalAlpha = 0.15;
        ctx.beginPath();
        ctx.moveTo(this.layout.cols.hybrid, 0); ctx.lineTo(this.layout.cols.hybrid, h);
        ctx.moveTo(this.layout.cols.public, 0); ctx.lineTo(this.layout.cols.public, h);
        ctx.stroke();
        ctx.globalAlpha = 1;

        events.forEach(d => {
          const py = this.yearToY(d.date.getFullYear());
          if (py < -20 || py > h + 20) return;
          const pos = this.packed.get(d.id);
          if (!pos) return;

          const isHovered = this.hoveredEvents.some(he => he.id === d.id);
          const color = this.getActorColor(d.actorType);

          this._drawNode(ctx, pos.x, py, d.actorType, color, isHovered);
        });
      }

      renderMinimap() {
        const ctx = this.minimapCtx;
        const w = this.minimapCanvas.width / (window.devicePixelRatio || 1);
        const h = this.minimapCanvas.height / (window.devicePixelRatio || 1);

        ctx.clearRect(0, 0, w, h);

        const events = DataModel.getFiltered();
        const centerX = w / 2;

        events.forEach(d => {
          const py = ((d.date.getFullYear() - 1800) / 225) * h;
          const color = this.getActorColor(d.actorType);
          ctx.fillStyle = color;
          ctx.globalAlpha = 0.6;

          if (d.actorType === 'public') {
            ctx.fillRect(centerX - 1.5, py - 1.5, 3, 3);
          } else {
            ctx.beginPath();
            ctx.arc(centerX, py, 2, 0, Math.PI * 2);
            ctx.fill();
          }
        });
        ctx.globalAlpha = 1;

        const range = (2025 - 1800) / this.state.zoom;
        const centerYear = (1800 + 2025) / 2 - this.state.panY * range;
        const totalRange = 225;
        const centerPos = ((centerYear - 1800) / totalRange) * h;

        const vpHeight = 40;
        const topBuffer = 10;

        let vpTop = centerPos - (vpHeight / 2);
        vpTop = Math.max(topBuffer, Math.min(h - vpHeight - topBuffer, vpTop));

        const vp = document.getElementById('minimapViewport');
        vp.style.top = vpTop + 'px';
        vp.style.height = vpHeight + 'px';
      }

      zoom(f) {
        this.state.zoom = Math.max(1, Math.min(20, this.state.zoom * f));
        this.render();
      }

      fit() {
        const evs = DataModel.getFiltered();
        if (!evs.length) return;
        const yrs = evs.map(d => d.date.getFullYear());
        const range = Math.max(...yrs) - Math.min(...yrs) + 20;
        this.state.zoom = 225 / range;
        this.render();
      }

      onDragStart(e) {
        const startY = e.clientY;
        const startPan = this.state.panY;
        const onMove = (me) => {
          this.state.panY = startPan + (startY - me.clientY) * 20 / (this.state.zoom * this.layout.h);
          this.render();
        };
        const onUp = () => { window.removeEventListener('mousemove', onMove); window.removeEventListener('mouseup', onUp); };
        window.addEventListener('mousemove', onMove);
        window.addEventListener('mouseup', onUp);
      }

      onMinimapDragStart(e) {
        e.preventDefault();
        const h = this.minimapCanvas.height / (window.devicePixelRatio || 1);

        const onMove = (me) => {
          const rect = this.minimapContainer.getBoundingClientRect();
          const mouseY = me.clientY - rect.top;
          const mouseRatio = Math.max(0, Math.min(1, mouseY / h));
          const targetYear = 1800 + (mouseRatio * 225);
          this.goToYear(targetYear);
        };

        const onUp = () => { window.removeEventListener('mousemove', onMove); window.removeEventListener('mouseup', onUp); };
        onMove(e);
        window.addEventListener('mousemove', onMove);
        window.addEventListener('mouseup', onUp);
      }

      onHover(e) {
        const rect = this.canvas.getBoundingClientRect();
        const x = e.clientX - rect.left, y = e.clientY - rect.top;
        const hitRadius = 15;

        const found = [];
        for (const d of DataModel.getFiltered()) {
          const py = this.yearToY(d.date.getFullYear());
          const pos = this.packed.get(d.id);
          if (!pos) continue;
          const dist = Math.hypot(x - pos.x, y - py);
          if (dist < hitRadius) {
            found.push({ ...d, dist: dist, x: pos.x, py: py });
          }
        }

        found.sort((a, b) => a.dist - b.dist);

        const currentIds = this.hoveredEvents.map(e => e.id).sort().join(',');
        const newIds = found.map(e => e.id).sort().join(',');

        if (currentIds !== newIds) {
          this.hoveredEvents = found;
          this.canvas.style.cursor = found.length ? 'pointer' : 'default';
          if (found.length) this.showTooltip(found, e.clientX, e.clientY);
          else this.hideTooltip();
          this.render();
        }
      }

      showTooltip(events, mx, my) {
        const el = document.getElementById('tooltip');
        const rect = this.container.getBoundingClientRect();

        const cardsHtml = events.map(d => {
          return `
            <div class="tooltip-card" onclick="timeline.openSidebar(DataModel.getActorById('${d.actorId}'))">
              <div class="tooltip-header">
                <span>${d.date.getFullYear()}</span>
                <div class="tooltip-diamond"></div>
                <span>${d.type}</span>
              </div>
              <div class="tooltip-body">${d.desc}</div>
              <div class="tooltip-actor">${d.actorName}</div>
            </div>
          `;
        }).join('');

        el.innerHTML = cardsHtml;

        const tooltipWidth = 300;
        const padding = 15;
        const containerWidth = this.layout.w;

        let left = mx - rect.left + padding;
        let top = my - rect.top + padding;

        if (left + tooltipWidth + padding > containerWidth) {
          left = (mx - rect.left) - tooltipWidth - padding;
        }

        const estimatedHeight = (events.length * 130) + 20;
        if (top + estimatedHeight > this.layout.h) {
          const shift = (top + estimatedHeight) - this.layout.h;
          top -= shift;
        }

        if (top < 0) top = 10;

        el.style.left = left + 'px';
        el.style.top = top + 'px';
        el.style.opacity = 1;
      }

      hideTooltip() {
        const el = document.getElementById('tooltip');
        el.style.opacity = 0;
        setTimeout(() => {
          if (el.style.opacity === '0') {
            el.innerHTML = '';
          }
        }, 150);
      }

      openSidebar(actor) {
        if (!actor) return;
        const sidebar = document.getElementById('sidebar');
        document.getElementById('sb-name').textContent = actor.name;
        document.getElementById('sb-role').textContent = actor.role;
        document.getElementById('sb-desc').textContent = actor.description;
        document.getElementById('sb-timeline').innerHTML = actor.events.map(e => `
          <div class="text-xs border-l-2 border-[var(--border)] pl-3 py-1">
            <div class="font-mono text-muted">${e.date}</div>
            <div class="font-weight text-fg">${e.category}</div>
            <div class="text-muted">${e.description}</div>
          </div>
        `).join('');
        sidebar.classList.add('open');
        document.getElementById('sidebarBackdrop').classList.add('visible');
      }

      closeSidebar() {
        document.getElementById('sidebar').classList.remove('open');
        document.getElementById('sidebarBackdrop').classList.remove('visible');
        this.container.focus();
      }
    }

    let timeline;
    window.addEventListener('DOMContentLoaded', async () => {
      await DataModel.init();
      timeline = new Timeline();
    });
