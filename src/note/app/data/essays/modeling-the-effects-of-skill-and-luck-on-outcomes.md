---
tags: [miscellanea, model]
---

# Modeling the Effects of Skill and Luck on Outcomes

> …
>

- Talent:  Normally Distributed.
- → Results (Usually Exponentially Distributed)
- What explains this discrepancy ? Luck (Favorable Events - Others Factors)?
- …

1. **Initialization of Agents** Each agent $A_i$ is placed in a **fixed random position**. Their **talent ($T_i$)** is a time-independent value following a **Gaussian distribution** (mean $m_T = 0.6$, standard deviation $\sigma_T = 0.1$) truncated within the interval $$. Every agent starts with an equal **capital ($C_i$) of 10 units**.
2. **Initialization of Events** The world contains **500 moving event-points** ($N_E$). Half are **lucky (green)** and half are **unlucky (red)**. These points are initially distributed uniformly across the lattice.
3.  **The Simulation Loop** For each of the **80 iterations**:
    - **Movement:** Every event-point moves **two patches** in a random direction. Because the world is toroidal, points that move off one edge reappear on the opposite side.
    - **Intersection:** An agent is "intercepted" if an event-point falls within a **radius of 1 patch**. Note that event-points do not disappear after an intersection.
    - **Action Rules:**
        - **Lucky Event:** The agent doubles their capital ($C_k(t) = 2C_k(t-1)$) only if a random number $rand < T_k$. This represents the agent being "smart enough" to profit from the opportunity.
        - **Unlucky Event:** The agent's capital is halved ($C_k(t) = C_k(t-1)/2$). Talent plays no role in avoiding bad luck.

```bash
const N = 1000; // Total individuals [1]
const NE = 500; // Total event points [9]
const WORLD_SIZE = 201; // 201x201 patches [1]
const STEPS = 80; // 40 years, 6-month intervals [4, 6]

// Helper for Gaussian distribution (not in sources)
function gaussianRandom(mean = 0.6, stdev = 0.1) {
    let u = 1 - Math.random();
    let v = Math.random();
    let z = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    let val = z * stdev + mean;
    return Math.max(0, Math.min(1, val)); // Truncated to [5] [3]
}

// Initialize Agents [3, 6]
let agents = Array.from({ length: N }, () => ({
    x: Math.random() * WORLD_SIZE,
    y: Math.random() * WORLD_SIZE,
    talent: gaussianRandom(0.6, 0.1), // [7, 8]
    capital: 10 // [6, 7]
}));

// Initialize Events [4, 9]
let events = Array.from({ length: NE }, (_, i) => ({
    x: Math.random() * WORLD_SIZE,
    y: Math.random() * WORLD_SIZE,
    type: i < NE / 2 ? 'lucky' : 'unlucky' // 50/50 split [4]
}));

// Simulation Loop [10-12]
for (let t = 0; t < STEPS; t++) {
    // 1. Move Events [10]
    events.forEach(e => {
        let angle = Math.random() * 2 * Math.PI;
        e.x = (e.x + 2 * Math.cos(angle) + WORLD_SIZE) % WORLD_SIZE; // Toroidal [1]
        e.y = (e.y + 2 * Math.sin(angle) + WORLD_SIZE) % WORLD_SIZE;
    });

    // 2. Check Intersections [10]
    agents.forEach(a => {
        events.forEach(e => {
            let dx = Math.abs(a.x - e.x);
            let dy = Math.abs(a.y - e.y);
            // Account for toroidal distance
            if (dx > WORLD_SIZE / 2) dx = WORLD_SIZE - dx;
            if (dy > WORLD_SIZE / 2) dy = WORLD_SIZE - dy;
            let dist = Math.sqrt(dx*dx + dy*dy);

            if (dist <= 1) { // Radius 1 patch [10]
                if (e.type === 'lucky') {
                    if (Math.random() < a.talent) {
                        a.capital *= 2; // [11, 12]
                    }
                } else {
                    a.capital /= 2; // [12]
                }
            }
        });
    });
}
```

## Specification

This tool visualizes the "Talent vs. Luck" model. It includes:

1. **The Main Canvas**: Displays the agents (static dots) and events (moving particles). Agents change color based on their accumulated Capital (Wealth).
2. **Control Panel**: Play, Pause, Reset, and Speed control.
3. **Real-time Analytics**: A histogram showing the distribution of wealth to visualize the emergence of inequality over the 80 steps.
4. …

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Talent vs. Luck Simulation</title>
    <style>
            --bg-color: #0f172a;
            --panel-bg: #1e293b;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
            --accent: #38bdf8;
            --success: #22c55e;
            --danger: #ef4444;
            --border: #334155;
            --font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: var(--font-family);
            background-color: var(--bg-color);
            color: var(--text-main);
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        /* Header */
        header {
            padding: 1rem 2rem;
            background-color: var(--panel-bg);
            border-bottom: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        h1 {
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--accent);
        }

        .stats-summary {
            display: flex;
            gap: 20px;
            font-size: 0.9rem;
        }

        .stat-item span {
            color: var(--text-muted);
            margin-right: 5px;
        }

        /* Main Layout */
        main {
            flex: 1;
            display: flex;
            overflow: hidden;
        }

        /* Canvas Area */
        #simulation-container {
            flex: 2;
            position: relative;
            background: #000;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        canvas {
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
            background-color: #020617;
            cursor: crosshair;
        }

        /* Sidebar Controls */
        aside {
            flex: 1;
            min-width: 320px;
            max-width: 400px;
            background-color: var(--panel-bg);
            border-left: 1px solid var(--border);
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            overflow-y: auto;
        }

        .panel-section {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }

        .panel-title {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
            font-weight: 700;
            border-bottom: 1px solid var(--border);
            padding-bottom: 0.5rem;
        }

        /* Controls */
        .control-group {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }

        button {
            padding: 0.6rem 1rem;
            border: none;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            font-family: inherit;
        }

        .btn-primary { background: var(--accent); color: #000; }
        .btn-primary:hover { background: #0ea5e9; }

        .btn-secondary { background: var(--border); color: var(--text-main); }
        .btn-secondary:hover { background: #475569; }

        .slider-group {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }

        label { font-size: 0.85rem; color: var(--text-muted); }

        input[type="range"] {
            width: 100%;
            height: 6px;
            background: var(--border);
            border-radius: 3px;
            appearance: none;
            outline: none;
        }
        input[type="range"]::-webkit-slider-thumb {
            appearance: none;
            width: 16px;
            height: 16px;
            background: var(--accent);
            border-radius: 50%;
            cursor: pointer;
        }

        /* Interactive Legend */
        .legend {
            display: flex;
            flex-direction: column;
            gap: 8px;
            font-size: 0.8rem;
            background: rgba(0,0,0,0.2);
            padding: 10px;
            border-radius: 6px;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 4px;
            border-radius: 4px;
            cursor: pointer;
            user-select: none;
            transition: background 0.2s;
        }

        .legend-item:hover {
            background: rgba(255,255,255,0.05);
        }

        /* State when hidden */
        .legend-item.hidden {
            opacity: 0.4;
            text-decoration: line-through;
        }

        .dot { width: 10px; height: 10px; border-radius: 50%; }
        .dot.agent { background: var(--text-muted); }
        .dot.rich { background: #fbbf24; box-shadow: 0 0 5px #fbbf24; }
        .dot.lucky { background: var(--success); }
        .dot.unlucky { background: var(--danger); }

        /* Histogram Chart */
        #chart-container {
            height: 150px;
            width: 100%;
            background: rgba(0,0,0,0.2);
            border-radius: 6px;
            position: relative;
            display: flex;
            align-items: flex-end;
            padding: 0 5px;
            gap: 1px;
        }

        .bar {
            flex: 1;
            background: var(--accent);
            opacity: 0.7;
            transition: height 0.2s;
            min-width: 2px;
        }
        .bar:hover { opacity: 1; background: #fff; }

        /* Tooltip overlay for chart */
        #chart-tooltip {
            position: absolute;
            top: 0;
            left: 0;
            background: rgba(0,0,0,0.8);
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.1s;
            z-index: 10;
        }

        /* Progress Bar */
        .progress-container {
            width: 100%;
            height: 4px;
            background: var(--border);
            margin-top: 5px;
            border-radius: 2px;
            overflow: hidden;
        }
        .progress-bar {
            height: 100%;
            background: var(--accent);
            width: 0%;
            transition: width 0.1s linear;
        }

    </style>
</head>
<body>

<header>
    <h1>Talent vs. Luck</h1>
    <div class="stats-summary">
        <div class="stat-item"><span>Step:</span><strong id="step-display">0</strong>/80</div>
        <div class="stat-item"><span>Time:</span><strong id="time-display">0</strong> yrs</div>
        <div class="stat-item"><span>Max Capital:</span><strong id="max-cap-display">10</strong></div>
    </div>
</header>

<main>
    <div id="simulation-container">
        <canvas id="simCanvas"></canvas>
    </div>

    <aside>
        <div class="panel-section">
            <div class="panel-title">Simulation Controls</div>
            <div class="control-group">
                <button id="btn-toggle" class="btn-primary">Start</button>
                <button id="btn-reset" class="btn-secondary">Reset</button>
            </div>
            <div class="slider-group">
                <label for="speed-range">Simulation Speed</label>
                <input type="range" id="speed-range" min="1" max="20" value="5">
            </div>
            <div class="progress-container">
                <div class="progress-bar" id="sim-progress"></div>
            </div>
        </div>

        <div class="panel-section">
            <div class="panel-title">Legend (Click to Toggle)</div>
            <div class="legend">
                <div class="legend-item" id="legend-agents" onclick="toggleLayer('agents')">
                    <div class="dot agent"></div> Agents (All)
                    <div style="margin-left:auto; font-size: 10px; color: #64748b;">[Show]</div>
                </div>
                <div class="legend-item" id="legend-lucky" onclick="toggleLayer('lucky')">
                    <div class="dot lucky"></div> Lucky Events
                    <div style="margin-left:auto; font-size: 10px; color: #64748b;">[Show]</div>
                </div>
                <div class="legend-item" id="legend-unlucky" onclick="toggleLayer('unlucky')">
                    <div class="dot unlucky"></div> Unlucky Events
                    <div style="margin-left:auto; font-size: 10px; color: #64748b;">[Show]</div>
                </div>
                <!-- Just an informational line, not clickable -->
                <div class="legend-item" style="opacity: 0.6; cursor: default;">
                    <div class="dot rich"></div> <i>High Wealth Agents</i>
                </div>
            </div>
        </div>

        <div class="panel-section" style="flex: 1;">
            <div class="panel-title">Wealth Distribution</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 5px;">
                Histogram of Capital (Log Scale)
            </div>
            <div id="chart-container">
                <!-- Bars injected via JS -->
            </div>
            <div id="chart-tooltip"></div>
        </div>

        <div class="panel-section">
            <div class="panel-title">Description</div>
            <p style="font-size: 0.85rem; line-height: 1.5; color: var(--text-muted);">
                Agents (grey) are stationary. Events (green/red) move randomly.
                When a lucky event hits an agent, their capital doubles based on talent.
                Unlucky events halve capital. Watch how inequality emerges over 40 years (80 steps).
            </p>
        </div>
    </aside>
</main>

<script>
/**
 * Visualization for the Talent vs. Luck Model
 * Based on the provided user snippet.
 */

// --- Constants from User Model ---
const N = 1000; // Total individuals
const NE = 500; // Total event points
const WORLD_SIZE = 201; // 201x201 patches
const STEPS = 80; // Total steps

// --- Visualization Config ---
const SCALE = 4; // Pixels per patch (201 * 4 = ~804px canvas)
const CANVAS_SIZE = WORLD_SIZE * SCALE;
const EVENT_RADIUS = 1 * SCALE;
const AGENT_RADIUS = 1.5 * SCALE;

// --- State Variables ---
let agents = [];
let events = [];
let currentStep = 0;
let isRunning = false;
let animationId = null;
let stepsPerFrame = 1;

// --- Visibility State ---
const visibility = {
    agents: true,
    lucky: true,
    unlucky: true
};

// --- DOM Elements ---
const canvas = document.getElementById('simCanvas');
const ctx = canvas.getContext('2d');
const btnToggle = document.getElementById('btn-toggle');
const btnReset = document.getElementById('btn-reset');
const speedRange = document.getElementById('speed-range');
const stepDisplay = document.getElementById('step-display');
const timeDisplay = document.getElementById('time-display');
const maxCapDisplay = document.getElementById('max-cap-display');
const progressBar = document.getElementById('sim-progress');
const chartContainer = document.getElementById('chart-container');

// Initialize Canvas Size
canvas.width = CANVAS_SIZE;
canvas.height = CANVAS_SIZE;

// --- Helper Functions (From User Snippet) ---
function gaussianRandom(mean = 0.6, stdev = 0.1) {
    let u = 1 - Math.random();
    let v = Math.random();
    let z = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    let val = z * stdev + mean;
    return Math.max(0, Math.min(1, val));
}

// --- Core Model Logic ---

function initModel() {
    // Initialize Agents
    agents = Array.from({ length: N }, () => ({
        x: Math.random() * WORLD_SIZE,
        y: Math.random() * WORLD_SIZE,
        talent: gaussianRandom(0.6, 0.1),
        capital: 10
    }));

    // Initialize Events
    events = Array.from({ length: NE }, (_, i) => ({
        x: Math.random() * WORLD_SIZE,
        y: Math.random() * WORLD_SIZE,
        type: i < NE / 2 ? 'lucky' : 'unlucky'
    }));

    currentStep = 0;
    updateUI();
    draw();
    updateChart();
}

function runStep() {
    // 1. Move Events
    events.forEach(e => {
        let angle = Math.random() * 2 * Math.PI;
        e.x = (e.x + 2 * Math.cos(angle) + WORLD_SIZE) % WORLD_SIZE;
        e.y = (e.y + 2 * Math.sin(angle) + WORLD_SIZE) % WORLD_SIZE;
    });

    // 2. Check Intersections
    agents.forEach(a => {
        events.forEach(e => {
            let dx = Math.abs(a.x - e.x);
            let dy = Math.abs(a.y - e.y);

            // Account for toroidal distance
            if (dx > WORLD_SIZE / 2) dx = WORLD_SIZE - dx;
            if (dy > WORLD_SIZE / 2) dy = WORLD_SIZE - dy;

            let dist = Math.sqrt(dx*dx + dy*dy);

            if (dist <= 1) {
                if (e.type === 'lucky') {
                    if (Math.random() < a.talent) {
                        a.capital *= 2;
                    }
                } else {
                    a.capital /= 2;
                }
            }
        });
    });

    currentStep++;
}

// --- Visibility Toggle Handler ---
function toggleLayer(layerName) {
    visibility[layerName] = !visibility[layerName];

    // Update Legend UI
    const legendItem = document.getElementById(`legend-${layerName}`);
    const statusText = legendItem.querySelector('div:last-child');

    if (visibility[layerName]) {
        legendItem.classList.remove('hidden');
        statusText.textContent = "[Show]";
    } else {
        legendItem.classList.add('hidden');
        statusText.textContent = "[Hidden]";
    }

    // Redraw immediately
    draw();
}

// --- Rendering ---

function getWealthColor(capital) {
    // Logarithmic color scaling
    if (capital <= 10) return '#475569'; // Slate 600 (Poor)
    const logCap = Math.log10(capital);
    const intensity = Math.min(1, (logCap - 1) / 4);

    // Interpolate from Grey to Gold
    const r = Math.floor(71 + (251 - 71) * intensity);
    const g = Math.floor(85 + (191 - 85) * intensity);
    const b = Math.floor(105 + (36 - 105) * intensity);
    return `rgb(${r},${g},${b})`;
}

function draw() {
    // Clear Canvas
    ctx.fillStyle = '#020617';
    ctx.fillRect(0, 0, CANVAS_SIZE, CANVAS_SIZE);

    // Draw Agents
    if (visibility.agents) {
        agents.forEach(a => {
            ctx.beginPath();
            ctx.arc(a.x * SCALE, a.y * SCALE, AGENT_RADIUS, 0, Math.PI * 2);
            ctx.fillStyle = getWealthColor(a.capital);
            ctx.fill();
        });
    }

    // Draw Events
    events.forEach(e => {
        let shouldDraw = false;
        if (e.type === 'lucky' && visibility.lucky) shouldDraw = true;
        if (e.type === 'unlucky' && visibility.unlucky) shouldDraw = true;

        if (shouldDraw) {
            ctx.beginPath();
            ctx.arc(e.x * SCALE, e.y * SCALE, EVENT_RADIUS, 0, Math.PI * 2);
            ctx.fillStyle = e.type === 'lucky' ? '#22c55e' : '#ef4444';
            ctx.globalAlpha = 0.8;
            ctx.fill();
            ctx.globalAlpha = 1.0;
        }
    });
}

// --- Analytics (Histogram) ---
function updateChart() {
    chartContainer.innerHTML = '';
    const bins = new Array(20).fill(0);
    let maxCapital = 0;

    agents.forEach(a => {
        if (a.capital > maxCapital) maxCapital = a.capital;

        let binIdx = 0;
        if (a.capital >= 10) {
            const logVal = Math.log10(a.capital);
            binIdx = Math.floor(logVal) + 1;
        }

        if (binIdx >= bins.length) binIdx = bins.length - 1;
        bins[binIdx]++;
    });

    const maxCount = Math.max(...bins);

    bins.forEach((count, i) => {
        const bar = document.createElement('div');
        bar.className = 'bar';
        const heightPercent = (count / maxCount) * 100;
        bar.style.height = `${heightPercent}%`;

        if (i <= 1) bar.style.backgroundColor = '#475569';
        else if (i < 5) bar.style.backgroundColor = '#38bdf8';
        else bar.style.backgroundColor = '#fbbf24';

        bar.onmouseenter = (e) => {
            const tooltip = document.getElementById('chart-tooltip');
            tooltip.style.opacity = 1;
            let rangeText = "";
            if (i===0) rangeText = "< 10";
            else if (i===1) rangeText = "10";
            else rangeText = `10^${i-1} - 10^${i}`;

            tooltip.textContent = `Range: ${rangeText} | Count: ${count}`;
            tooltip.style.left = e.pageX + 10 + 'px';
            tooltip.style.top = e.pageY - 20 + 'px';
        };
        bar.onmouseleave = () => {
             document.getElementById('chart-tooltip').style.opacity = 0;
        };

        chartContainer.appendChild(bar);
    });

    maxCapDisplay.textContent = Math.floor(maxCapital).toLocaleString();
}

// --- UI & Loop Control ---

function updateUI() {
    stepDisplay.textContent = currentStep;
    timeDisplay.textContent = (currentStep / 2).toFixed(1);
    const progress = (currentStep / STEPS) * 100;
    progressBar.style.width = `${progress}%`;

    if (currentStep >= STEPS) {
        isRunning = false;
        btnToggle.textContent = "Finished";
        btnToggle.classList.replace('btn-primary', 'btn-secondary');
        cancelAnimationFrame(animationId);
    }
}

function loop() {
    if (!isRunning) return;

    for(let i=0; i<stepsPerFrame; i++) {
        if (currentStep < STEPS) {
            runStep();
        }
    }

    draw();
    // Update chart slightly less frequently for performance if needed,
    // but modern browsers can handle this N=1000 size well every frame.
    updateChart();
    updateUI();

    if (isRunning) {
        animationId = requestAnimationFrame(loop);
    }
}

// --- Event Listeners ---

btnToggle.addEventListener('click', () => {
    if (currentStep >= STEPS) {
        initModel();
        isRunning = true;
        btnToggle.textContent = "Pause";
        btnToggle.classList.replace('btn-secondary', 'btn-primary');
        loop();
    } else {
        isRunning = !isRunning;
        btnToggle.textContent = isRunning ? "Pause" : "Resume";
        if (isRunning) loop();
    }
});

btnReset.addEventListener('click', () => {
    isRunning = false;
    cancelAnimationFrame(animationId);
    initModel();
    btnToggle.textContent = "Start";
    btnToggle.classList.replace('btn-secondary', 'btn-primary');
});

speedRange.addEventListener('input', (e) => {
    stepsPerFrame = parseInt(e.target.value);
});

// --- Initialization ---
initModel();

</script>

</body>
</html>
```

## References

- [‣](https://app.notion.com/p/2e0598edb7908090adf7fa1bba038409?pvs=21)

## Provenance

- Notion export: `Modelo/Miscellanea/Miscellanea/Modeling the Effects of Skill and Luck on Outcomes 2e0c0f5171ec8053b19ff953b3fe4323.md`
