---
tags: [data-collection]
---

# Profiling


> Profiling is the instrumentation-based or sampling-based acquisition of runtime behavioral metrics for the purpose of performance characterization, bottleneck identification, resource attribution, and optimization guidance.
> 

> **Note:** Profiling should not be understood as a fixed collection of techniques or analyses, but as a **goal-directed activity**. As new questions about program execution arise, new measurement and analysis methods must be designed to address them.
> 

> **Old Goal**: Measure and rank.
> 

> **New Goal**: A richer description of the underlying system.
> 

> Profiling is not model building (i.e., constructing a representation with dynamics); rather, it is the observation of a system, followed by data capture and the derivation of fundamental truths through inference.
> 

Guiding Questions

- What is profiling?
- Does we model build in profiling?
- Which kinds  of question does profiling answers?
- What is the nature of the inferences derived from profiling data? Fundamentally, profiling inferences are **statements about program behavior** expressed as **patterns, properties, relationships, anomalies, or statistical summaries**. They can be **qualitative (behavioral descriptors) or quantitative (metrics, distributions)**, and often multiple forms are combined to derive actionable insights.
- What data does it capture?
- How does it capture the data?
- How it’s the data visualization?
- Which are the subjects of programming?
- At which abstraction layer is profiling occurring?
- What type of analysis are done in the data?
    - Which  kinds of modelling?
    - Do we we need causal modelling?
    - Which  kinds of traditional analysis are done?
    - Which  kinds of statistical analysis should be done?
- Which are the epistemic limits?
    - What is unobservable?
    - What is approximated?
    - What is sampled vs instrumented?
    - What bias does sampling introduce?
    - What resolution limits exist?
    - What temporal aliasing occurs?
    - What perturbation does instrumentation introduce?
- What is the space of techniques that guides profiling?
    - How do we design profiling experiments?
    - How do we control noise?
    - How many runs are required?
    - What is the warm-up strategy (JIT systems)?
    - How do we detect measurement bias?
    - What is the observer effect magnitude?
    - How do we isolate variables?
    - What is the reproducibility protocol?
    - What is the execution model being assumed?
    - In which  storage  format  store the data?
    - What is the impact of program execution model - on profiling strategy?
- What is the space of **production technical objects** used to profile systems?
- How doe this connect with the larger set of activities of program analysis?
- Meta
    - What questions are missing? What are the things I should be thinking about?

## Formulation

> **Profiling** is the empirical measurement and characterization of a system’s dynamic behavior during execution.
> 

It is:

- Dynamic (execution-time)
- Observational (non-functional focus)
- Quantitative (metric-driven)
- Diagnostic (optimization-oriented)

It is not static analysis; it is behavioral measurement.

### What is the deep nature of profiling?

> A profiler provides a description of the underlying system that generates the observed data; it conveys patterns, properties, and resource usage, but it does not construct a model of the system’s internal dynamics that would enable simulation, prediction, or extrapolation beyond the observed behavior.
> 

> **Descriptive, not generative:** Profiling data allows you to **describe how the system behaves**, but it doesn’t automatically provide a model that can **predict future behavior under all conditions**.
> 

> Profiling lets you **reason about performance, bottlenecks, and resource usage** by buildinga **description of the system’s operational characteristics**, but it does **not give you the underlying dynamics or causal model**. If you want a dynamical model, you need to **abstract and formalize these descriptions** into a **state-transition or functional model** that generalizes beyond observed runs.
> 

### Which kinds  of question does profiling answers?

| **Type** | **Question** | **Description** |
| --- | --- | --- |
| **Performance Attribution** | Where is execution time spent? | Identifies hotspots via cost attribution (inclusive/exclusive time). |
| **Latency Analysis** | Why is this request slow? | Decomposes end-to-end latency into internal components and critical paths. |
| **Throughput Analysis** | What limits system throughput? | Determines bottlenecks restricting work per unit time. |
| **Resource Utilization** | How are CPU, memory, I/O, and network resources being used? | Maps execution behavior to resource consumption patterns. |
| **Memory Behavior** | Why is memory growing or fragmenting? | Analyzes allocation rate, retention, leaks, fragmentation, GC behavior. |
| **Concurrency Behavior** | Where are threads blocking or contending? | Detects lock contention, deadlocks, scheduling inefficiencies. |
| **Scalability** | How does behavior change under load? | Examines scaling curves and identifies nonlinear degradation. |
| **Phase Behavior** | Does the program exhibit execution phases? | Detects shifts in workload or computational regime over time. |
| **Microarchitectural Efficiency** | Why is CPI high or cache-miss rate elevated? | Maps software structure to hardware-level performance counters. |
| **I/O Behavior** | Where are I/O stalls occurring? | Analyzes syscall latency, disk wait, network delay. |
| **Structural Execution** | Which call paths dominate execution? | Examines call graph topology and cost propagation. |
| **Critical Path Analysis** | What is the longest latency-contributing chain? | Identifies dependency chains limiting completion time. |
| **Behavioral Deviation** | Is execution deviating from expected patterns? | Detects abnormal execution relative to baseline models. |
| **Regression Detection** | Did performance degrade after a change? | Compares runs across versions or configurations. |
| **Configuration Sensitivity** | How does configuration affect runtime behavior? | Evaluates impact of compiler flags, thread counts, memory limits, etc. |
| **Energy Efficiency** | How much energy does execution consume? | Profiles energy per instruction or workload. |
| **Distributed Causality** | How do services interact across boundaries? | Reconstructs trace-level causality in distributed systems. |
| **Input Sensitivity** | How does input structure affect runtime? | Correlates input characteristics with execution patterns. |
| **Fairness & Isolation** | Is one component starving others? | Evaluates scheduler fairness and resource isolation. |
| **Stability** | Is behavior statistically stable over time? | Detects drift, oscillation, or performance jitter. |

## QA

> 

## References

- [Profiler](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/profiler.md)
- [Statistics](https://app.notion.com/p/Statistics-c9d6a53f36a8494eae934a1a14f969da?pvs=21)
- [Modelado](https://app.notion.com/p/Modelado-a6727ea210124fb9a00ff6bb5bcf7cd5?pvs=21)
- [Probability](https://app.notion.com/p/Probability-4210c322839242cd8cc944b9b1e7c27f?pvs=21)
- [Epistemic Artifact](https://app.notion.com/p/Epistemic-Artifact-30ec0f5171ec80909e69c302fff36f78?pvs=21)
- Prinz, Andreas, et al. "Models, systems, and descriptions: A cross-disciplinary reflection on models." Frontiers in Computer Science 5 (2023): 1031807.
- Sowa, John F. "Worlds, models and descriptions." Studia Logica 84.2 (2006): 323-360.
- [‣](https://app.notion.com/p/1be598edb790802687b9d1c4b8bff0a1?pvs=21)