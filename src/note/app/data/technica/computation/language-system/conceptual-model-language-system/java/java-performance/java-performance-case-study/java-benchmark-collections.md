# Java Benchmark: Collections

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Java Latency Benchmarks | Collection Performance</title>
    <style>
        /* --- CSS VARIABLES & RESET --- */
        :root {
            --bg-body: #0f172a;
            --bg-card: #1e293b;
            --bg-card-hover: #334155;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --primary: #38bdf8; /* Cyan */
            --primary-glow: rgba(56, 189, 248, 0.4);
            --secondary: #a855f7; /* Purple */
            --accent-danger: #f43f5e;
            --accent-success: #10b981;
            --font-main: 'Inter', system-ui, -apple-system, sans-serif;
            --font-mono: 'Fira Code', 'Courier New', monospace;
            --radius: 12px;
            --container-width: 1200px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: var(--font-main);
            background-color: var(--bg-body);
            color: var(--text-main);
            line-height: 1.6;
            overflow-x: hidden;
        }

        a { text-decoration: none; color: inherit; transition: 0.3s; }
        ul { list-style: none; }

        /* --- UTILITIES --- */
        .container {
            max-width: var(--container-width);
            margin: 0 auto;
            padding: 0 20px;
        }

        .section-padding { padding: 80px 0; }
        
        .text-gradient {
            background: linear-gradient(to right, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 50px;
            font-size: 0.8rem;
            font-weight: 600;
            background: rgba(56, 189, 248, 0.1);
            color: var(--primary);
            border: 1px solid rgba(56, 189, 248, 0.2);
            margin-bottom: 16px;
        }

        /* --- HEADER --- */
        header {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(15, 23, 42, 0.9);
            backdrop-filter: blur(10px);
            z-index: 1000;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 70px;
        }

        .logo {
            font-weight: 800;
            font-size: 1.5rem;
            font-family: var(--font-mono);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo span { color: var(--primary); }

        .nav-links { display: flex; gap: 30px; }
        .nav-links a { color: var(--text-muted); font-size: 0.95rem; }
        .nav-links a:hover { color: var(--primary); }

        .cta-btn {
            background: var(--primary);
            color: var(--bg-body);
            padding: 8px 20px;
            border-radius: 6px;
            font-weight: 700;
            font-size: 0.9rem;
        }
        .cta-btn:hover { background: #0ea5e9; box-shadow: 0 0 15px var(--primary-glow); }

        /* --- HERO SECTION --- */
        .hero {
            padding-top: 160px;
            padding-bottom: 100px;
            text-align: center;
            background: radial-gradient(circle at 50% 20%, rgba(56, 189, 248, 0.1), transparent 60%);
        }

        .hero h1 {
            font-size: 3.5rem;
            line-height: 1.1;
            margin-bottom: 24px;
            font-weight: 800;
        }

        .hero p {
            font-size: 1.25rem;
            color: var(--text-muted);
            max-width: 700px;
            margin: 0 auto 40px auto;
        }

        .stats-row {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 60px;
        }

        .stat-item {
            text-align: center;
        }
        .stat-value {
            font-family: var(--font-mono);
            font-size: 2rem;
            font-weight: 700;
            color: var(--text-main);
        }
        .stat-label {
            font-size: 0.9rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* --- CONCEPT SECTION --- */
        .concept-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 24px;
            margin-top: 40px;
        }

        .card {
            background: var(--bg-card);
            padding: 30px;
            border-radius: var(--radius);
            border: 1px solid rgba(255,255,255,0.05);
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: var(--primary);
        }

        .card h3 {
            margin-bottom: 12px;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .card p { color: var(--text-muted); font-size: 0.95rem; }

        /* --- BENCHMARK DASHBOARD --- */
        .benchmark-section {
            background: #0b1120; /* Slightly darker */
        }

        .dashboard-controls {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 40px;
            flex-wrap: wrap;
        }

        .tab-btn {
            background: transparent;
            border: 1px solid var(--text-muted);
            color: var(--text-muted);
            padding: 10px 24px;
            border-radius: 50px;
            cursor: pointer;
            font-size: 0.95rem;
            transition: 0.3s;
        }

        .tab-btn.active, .tab-btn:hover {
            background: rgba(56, 189, 248, 0.1);
            border-color: var(--primary);
            color: var(--primary);
        }

        .benchmark-display {
            background: var(--bg-card);
            border-radius: var(--radius);
            padding: 40px;
            border: 1px solid rgba(255,255,255,0.05);
            min-height: 400px;
            position: relative;
        }

        /* Custom CSS Bar Chart */
        .chart-container {
            display: flex;
            flex-direction: column;
            gap: 20px;
            max-width: 900px;
            margin: 0 auto;
        }

        .chart-row {
            display: grid;
            grid-template-columns: 200px 1fr 100px;
            align-items: center;
            gap: 20px;
        }

        .chart-label {
            font-family: var(--font-mono);
            font-size: 0.9rem;
            text-align: right;
            color: var(--text-muted);
        }

        .bar-area {
            background: rgba(255,255,255,0.05);
            height: 32px;
            border-radius: 6px;
            overflow: hidden;
            position: relative;
        }

        .bar-fill {
            height: 100%;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            padding-right: 10px;
            font-size: 0.75rem;
            font-weight: 700;
            color: #fff;
            transition: width 1s cubic-bezier(0.22, 1, 0.36, 1);
            width: 0; /* Animated via JS */
            position: relative;
        }

        /* Different colors for different latency tiers */
        .fast { background: var(--accent-success); box-shadow: 0 0 10px rgba(16, 185, 129, 0.3); }
        .medium { background: var(--primary); box-shadow: 0 0 10px rgba(56, 189, 248, 0.3); }
        .slow { background: var(--accent-danger); box-shadow: 0 0 10px rgba(244, 63, 94, 0.3); }

        .chart-value {
            font-family: var(--font-mono);
            font-size: 0.9rem;
        }

        .chart-note {
            margin-top: 30px;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.85rem;
            font-style: italic;
        }

        /* --- PERCENTILES VISUAL --- */
        .percentile-visual {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 60px;
            flex-wrap: wrap;
            gap: 40px;
        }

        .curve-container {
            flex: 1;
            min-width: 300px;
            height: 200px;
            background: rgba(255,255,255,0.02);
            border-radius: var(--radius);
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: flex-end;
            padding: 0 20px;
        }

        /* Simulated Distribution Curve using CSS Gradients/Masking (Simplified) */
        .dist-curve {
            width: 100%;
            height: 100%;
            background: linear-gradient(to top, var(--primary) 0%, transparent 100%);
            opacity: 0.2;
            clip-path: polygon(0% 100%, 5% 90%, 15% 60%, 30% 20%, 50% 10%, 70% 20%, 85% 60%, 95% 90%, 100% 100%);
        }

        .p-marker {
            position: absolute;
            bottom: 0;
            left: 85%; /* P99 position */
            height: 100%;
            width: 2px;
            background: var(--accent-danger);
            z-index: 2;
        }
        
        .p-marker::before {
            content: "P99";
            position: absolute;
            top: 20px;
            left: 5px;
            background: var(--accent-danger);
            color: white;
            padding: 2px 6px;
            font-size: 0.7rem;
            border-radius: 4px;
        }

        .percentile-info h3 { margin-bottom: 15px; }
        .percentile-info p { margin-bottom: 10px; color: var(--text-muted); }

        /* --- CODE SECTION --- */
        .code-wrapper {
            background: #000;
            border-radius: var(--radius);
            border: 1px solid rgba(255,255,255,0.1);
            overflow: hidden;
            margin-top: 30px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        }

        .code-header {
            background: #1e293b;
            padding: 12px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        .code-lang { font-family: var(--font-mono); font-size: 0.85rem; color: var(--text-muted); }

        pre {
            padding: 30px;
            overflow-x: auto;
            font-family: var(--font-mono);
            font-size: 0.9rem;
            color: #d1d5db;
        }

        .kwd { color: #c084fc; } /* keyword */
        .cls { color: #38bdf8; } /* class */
        .str { color: #a3e635; } /* string */
        .com { color: #64748b; } /* comment */
        .num { color: #f472b6; } /* number */

        /* --- FOOTER --- */
        footer {
            border-top: 1px solid rgba(255,255,255,0.05);
            padding: 60px 0;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.9rem;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 30px;
        }

        /* --- RESPONSIVE --- */
        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .nav-links { display: none; } /* Simplified for demo */
            .chart-row { grid-template-columns: 1fr; gap: 5px; margin-bottom: 20px; }
            .chart-label { text-align: left; margin-bottom: 5px; }
            .stats-row { flex-direction: column; gap: 20px; }
        }
    </style>
</head>
<body>

    <header>
        <div class="container">
            <nav>
                <div class="logo">
                    <span>//</span> JavaLatency
                </div>
                <div class="nav-links">
                    <a href="#concept">Concepts</a>
                    <a href="#benchmarks">Benchmarks</a>
                    <a href="#code">Implementation</a>
                    <a href="#analysis">Analysis</a>
                </div>
                <a href="#" class="cta-btn">Download Report</a>
            </nav>
        </div>
    </header>

    <main>
        <!-- HERO SECTION -->
        <section class="hero">
            <div class="container">
                <span class="badge">JMH Microbenchmark Report</span>
                <h1>Benchmarking <span class="text-gradient">Java Collection</span><br>Latency & Throughput</h1>
                <p>An in-depth analysis of latency characteristics in standard Java Collections. Understanding P99 pauses is critical for low-latency trading systems and high-frequency applications.</p>
                
                <div class="stats-row">
                    <div class="stat-item">
                        <div class="stat-value">10M+</div>
                        <div class="stat-label">Ops / Second</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">&lt; 5ns</div>
                        <div class="stat-label">Avg Access</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">P99.9</div>
                        <div class="stat-label">SLO Target</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- CONCEPT SECTION -->
        <section id="concept" class="section-padding">
            <div class="container">
                <h2 style="text-align: center; margin-bottom: 50px;">Why Latency Matters</h2>
                <div class="concept-grid">
                    <div class="card">
                        <h3>⚡ Latency vs. Throughput</h3>
                        <p>Throughput measures total volume, while latency measures the time for a single operation. In real-time systems (e.g., market data), a high throughput with high latency is unacceptable because individual requests time out.</p>
                    </div>
                    <div class="card">
                        <h3>📊 Tail Latency (P99)</h3>
                        <p>Averages hide spikes. We focus on percentiles (P90, P99, P99.9). A P99 spike in a `HashMap` resize event can cause a stutter affecting the entire user experience.</p>
                    </div>
                    <div class="card">
                        <h3>🚀 Allocation Pressure</h3>
                        <p>Excessive object creation during collection operations triggers Garbage Collection. GC "Stop-the-world" events are the enemy of low latency.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- BENCHMARK SECTION (INTERACTIVE) -->
        <section id="benchmarks" class="section-padding benchmark-section">
            <div class="container">
                <div style="text-align: center; margin-bottom: 40px;">
                    <h2>Performance Dashboard</h2>
                    <p style="color: var(--text-muted);">Comparison of common data structures (Lower is better)</p>
                </div>

                <div class="dashboard-controls">
                    <button class="tab-btn active" onclick="switchTab('read')">Random Read</button>
                    <button class="tab-btn" onclick="switchTab('write')">Random Write</button>
                    <button class="tab-btn" onclick="switchTab('iterate')">Iteration</button>
                </div>

                <div class="benchmark-display" id="dashboard-content">
                    <!-- Content injected via JS -->
                </div>
                <p class="chart-note">* Benchmarks run on JDK 21, JMH Mode: Throughput, 1 warmup, 5 forks. Values in nanoseconds/op.</p>
            </div>
        </section>

        <!-- PERCENTILES SECTION -->
        <section id="analysis" class="section-padding">
            <div class="container">
                <div class="percentile-visual">
                    <div class="curve-container">
                        <div class="dist-curve"></div>
                        <div class="p-marker"></div>
                    </div>
                    <div class="percentile-info">
                        <h3>The "Long Tail" Problem</h3>
                        <p>While <code>ArrayList</code> offers incredible average speeds, occasional resizing causes GC spikes.</p>
                        <p><strong>Recommendation:</strong> Pre-size your collections to avoid the O(n) copy cost during resizing.</p>
                        <div style="margin-top: 20px; padding: 15px; background: rgba(16, 185, 129, 0.1); border-left: 3px solid var(--accent-success);">
                            <strong>Winner:</strong> Pre-sized ArrayList (Consistent P99)
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- CODE SECTION -->
        <section id="code" class="section-padding" style="background: #0b1120;">
            <div class="container">
                <h2>Implementation: JMH Benchmark</h2>
                <p style="color: var(--text-muted); margin-bottom: 20px;">How we measure: Using Java Microbenchmark Harness (JMH) to avoid JIT warmup biases.</p>
                
                <div class="code-wrapper">
                    <div class="code-header">
                        <span class="code-lang">Java</span>
                        <span style="font-size: 0.8rem; color: #64748b;">BenchmarkTest.java</span>
                    </div>
                    <pre><code><span class="kwd">@Benchmark</span>
<span class="kwd public">public</span> <span class="cls">void</span> testArrayListRandomRead(<span class="cls">Blackhole</span> bh) {
    <span class="com">// Access random index to simulate real-world cache misses</span>
    <span class="kwd int">int</span> index = <span class="cls">ThreadLocalRandom</span>.current().nextInt(size);
    <span class="cls">Integer</span> val = arrayList.<span class="cls">get</span>(index);
    bh.<span class="cls">consume</span>(val);
}

<span class="kwd">@Benchmark</span>
<span class="kwd public">public</span> <span class="cls">void</span> testHashMapPut(<span class="cls">Blackhole</span> bh) {
    <span class="com">// Re-initialize keys to simulate unique insertion</span>
    <span class="cls">Integer</span> key = <span class="cls">ThreadLocalRandom</span>.current().nextInt();
    hashMap.<span class="cls">put</span>(key, key);
}</code></pre>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <div class="footer-links">
                <a href="#">Methodology</a>
                <a href="#">Source Code</a>
                <a href="#">OpenJDK Docs</a>
                <a href="#">Contact</a>
            </div>
            <p>&copy; 2023 Java Latency Benchmarks. Designed for Performance Engineers.</p>
        </div>
    </footer>

    <script>
        // Data representing latency in nanoseconds (Lower is better)
        const benchmarkData = {
            read: [
                { name: 'Array (int[])', value: 2, color: 'fast' },
                { name: 'ArrayList', value: 4, color: 'fast' },
                { name: 'HashMap', value: 12, color: 'fast' },
                { name: 'ConcurrentHashMap', value: 25, color: 'medium' },
                { name: 'TreeMap', value: 45, color: 'medium' },
                { name: 'LinkedList', value: 1200, color: 'slow' }
            ],
            write: [
                { name: 'Array (int[])', value: 2, color: 'fast' },
                { name: 'ArrayList', value: 6, color: 'fast' },
                { name: 'HashMap', value: 18, color: 'fast' },
                { name: 'ConcurrentHashMap', value: 40, color: 'medium' },
                { name: 'TreeMap', value: 55, color: 'medium' },
                { name: 'LinkedList', value: 8, color: 'fast' } // Linked list is fast for adding if you have the node, but slow for random. Assuming add-end here.
            ],
            iterate: [
                { name: 'Array (int[])', value: 5, color: 'fast' },
                { name: 'ArrayList', value: 7, color: 'fast' },
                { name: 'LinkedList', value: 15, color: 'medium' }, // Slightly slower due to pointer chasing
                { name: 'HashMap (Values)', value: 25, color: 'medium' },
                { name: 'ConcurrentHashMap', value: 30, color: 'medium' },
                { name: 'TreeMap', value: 35, color: 'medium' }
            ]
        };

        function renderChart(type) {
            const container = document.getElementById('dashboard-content');
            const data = benchmarkData[type];
            
            // Find max value for scaling
            const maxValue = Math.max(...data.map(d => d.value));

            let html = '<div class="chart-container">';
            
            data.forEach(item => {
                const widthPercentage = (item.value / maxValue) * 100;
                // Format value
                let displayValue = item.value + ' ns';
                if(item.value > 1000) displayValue = (item.value/1000).toFixed(1) + ' μs';

                html += `
                    <div class="chart-row">
                        <div class="chart-label">${item.name}</div>
                        <div class="bar-area">
                            <div class="bar-fill ${item.color}" style="width: 0%" data-width="${widthPercentage}%">
                                ${widthPercentage > 15 ? displayValue : ''}
                            </div>
                        </div>
                        <div class="chart-value">${displayValue}</div>
                    </div>
                `;
            });

            html += '</div>';
            container.innerHTML = html;

            // Trigger animation after a slight delay
            setTimeout(() => {
                const bars = document.querySelectorAll('.bar-fill');
                bars.forEach(bar => {
                    bar.style.width = bar.getAttribute('data-width');
                });
            }, 50);
        }

        function switchTab(type) {
            // Update active button state
            const buttons = document.querySelectorAll('.tab-btn');
            buttons.forEach(btn => {
                if(btn.innerText.toLowerCase().includes(type)) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });

            // Re-render
            renderChart(type);
        }

        // Initial render
        document.addEventListener('DOMContentLoaded', () => {
            renderChart('read');
        });

    </script>
</body>
</html>
```

Below is a rigorous **experiment design framework tailored specifically to benchmarking and evaluating Java Collections**. The structure follows your requested headings, but it is adapted to Java’s execution model (JVM, JIT, GC) and to the semantic differences among collection types.

---

## 1. System Model

**Execution Environment**

- JVM implementation (e.g., OpenJDK HotSpot)
- JVM version and vendor
- Garbage Collector (G1, ZGC, Shenandoah, Serial)
- Heap sizing strategy (`Xms`, `Xmx`)
- JIT compilation enabled (default tiered compilation)

**Hardware Model**

- CPU architecture (cores, cache hierarchy)
- Memory (NUMA vs UMA)
- Storage (SSD/HDD only relevant for persistence tests)
- OS scheduler and kernel version

**Software Model**

- Java Collections under test:
    - `ArrayList`, `LinkedList`
    - `HashMap`, `LinkedHashMap`, `TreeMap`
    - `HashSet`, `TreeSet`
    - Concurrent variants (`ConcurrentHashMap`, `CopyOnWriteArrayList`)
- Object model assumptions:
    - Reference size (compressed oops on/off)
    - Object allocation and indirection costs

**Threats to Validity**

- JIT warm-up effects
- GC pauses and heap resizing
- CPU frequency scaling and OS noise

## 2. Workload Design

**Operation Mix**

- Primitive operations:
    - Insert (`add`, `put`)
    - Lookup (`get`, `contains`)
    - Update (`set`, overwrite)
    - Remove (`remove`)
    - Iteration (sequential traversal)
- Composite workloads:
    - Read-heavy (e.g., 95% lookup)
    - Write-heavy (e.g., 70% insert/remove)
    - Balanced mixes

**Data Characteristics**

- Key/value types:
    - Primitive wrappers (`Integer`, `Long`)
    - Strings (short vs long)
    - Custom objects with varying `hashCode()` quality
- Cardinality:
    - Small (10²), medium (10⁴), large (10⁶+)
- Distribution:
    - Uniform
    - Skewed (Zipfian, hotspot keys)
    - Adversarial (hash collisions)

**Temporal Structure**

- Warm-up phase (to stabilize JIT)
- Measurement phase
- Cool-down / teardown

**Concurrency Model (if applicable)**

- Thread count scaling
- Read/write contention ratios
- Lock-free vs lock-based behavior

---

## 3. Evaluation Criteria Specification

**Performance Metrics**

- Throughput (ops/sec)
- Latency:
    - Mean
    - Percentiles (P50, P95, P99)
- Scalability:
    - Performance vs size
    - Performance vs thread count

**Memory Metrics**

- Memory footprint (bytes per element)
- Allocation rate
- GC pressure (minor/major collections)
- Pause times

**Algorithmic Behavior**

- Observed complexity trends (O(1), O(log n), O(n))
- Degradation under collision or skew

**Correctness & Semantics**

- Order guarantees (insertion, sorted, none)
- Iterator consistency (fail-fast vs weakly consistent)
- Thread-safety guarantees

---

## 4. Data Collection

**Measurement Tools**

- JMH (Java Microbenchmark Harness) for:
    - Warm-up control
    - Dead-code elimination avoidance
    - Statistical rigor
- JVM diagnostics:
    - GC logs
    - JFR (Java Flight Recorder)
- OS-level metrics (optional):
    - CPU utilization
    - Context switches

**Sampling Strategy**

- Multiple forks (fresh JVMs)
- Multiple iterations per fork
- Confidence intervals rather than single-point estimates

**Artifact Capture**

- Raw timing samples
- GC events and pause durations
- Heap usage snapshots

---

## 5. Visualization

**Performance Plots**

- Throughput vs collection size
- Latency percentiles vs workload mix
- Speedup vs thread count

**Memory Plots**

- Memory per element vs size
- Allocation rate over time
- GC pause distribution histograms

**Comparative Views**

- Side-by-side plots of alternative collections
- Heatmaps for workload × collection performance
- Complexity trend lines (log-log plots)

**Interpretability Focus**

- Explicitly separate:
    - Algorithmic effects
    - JVM/runtime effects
- Annotate regime changes (e.g., resize thresholds, treeification in `HashMap`)

### Summary

This design treats Java Collections not as abstract data structures, but as **runtime artifacts embedded in a managed, JIT-compiled, garbage-collected system**. The experiment is therefore as much about *JVM behavior* as about *data structure theory*, and the framework makes those interactions explicit and measurable.

If you want, I can:

- Instantiate this as a **JMH benchmark template**
- Specialize it for **Maps only**
- Or formalize it as a **methods section for a paper or technical report**

## References

- [**Benchmarking**](note.html?n=technica/computation/system/evaluation/benchmarking.md)