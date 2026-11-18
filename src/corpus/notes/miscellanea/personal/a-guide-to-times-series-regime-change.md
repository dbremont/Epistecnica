---
tags: [note, guia]
---

# A Guide to Times Series Regime Change


> …
> 

Guiding questions:

- How to detect the **performance** (latency) regime in a software system?
- How to **compute the performance** of the system at time $T$? The issue with this - is that we need also to characterize the workload (that is - what is being used?)
    - What is the expected latency for a random route $X$?
    - …
- How to compute the **performance** of a route a time $T$?
- How to decomposed the latency?  How to explain the dynamics?
- How to analyze the latency and workload? How to find the latency no-explain by workload?
- How can data be smoothed to reduce noise while preserving trends? How can data be resampled or aggregated to different time resolutions?  How can a series of $n$ observations be mapped or aggregated into $m$ observations when n>m
n>m?
- How to smooth data? How to map data to other time resolutions? How to create time intervals view of data points? How to take n observations an map to m observations, when n > m?
- Should I even be thinking on smoothing - and not a new time series (of let say deviations) based on the raw data? Which should be properties of the new times series? **How to**  create a derivative time series for one resolution (let say 5 minutes)as used as based for others?
    - How to evaluate this new times series?
        - **Sensitivity to spikes** – if a single request is extreme, it should reflect a high deviation.
        - **Sensitivity to persistent drift** – if latency gradually increases, the metric should rise.
        - **Robustness to noise** – normal small jitter shouldn’t trigger alerts.
        - **Composability** – can be used in dashboards, smoothing, or downstream analytics.
        - Interpretability …
- How to compute on previous data (at the head of the time series)? (The Chicken and Egg Problem): …
- How to model the latency of a system?   (System State, Current Workload) —>  Latency.
    - How can we use the historical model to identify and track the events responsible for portions of the observed latency?
    - If you used correlation between the task - how to used some structural simulation like component analysis - to reduced the data dimensions? …
    - Our system - latency are non markovian (they have memory)?
    - How to model and system with memory?
- How to **simulate workload**?
- What kind of statistics can be computed at the system level latency?
    - Latency Deviation (Using the Underlying Task Deviation) Per Time Window
    - % of Deviation per Time Window
    - Max Latency Over The Window
    - 

## Formulation

We need to answer the following questions:

- (System) What is the **expected latency** for a random route at time $T$? $L_\text{system}(T) = \frac{\sum_{r \in R}  L_r(T)} {|R|}$  where $f_r(T)$ = fraction of requests for route $r$ at time $T$, $L_r(T)$ = latency of that route.
    - Trick: If we does not have an observation for a route at time - used the take an average of the nearest one - before - and fill with that.
    - **Note:** This approach reconstructs an **imperfect system state** due to imputation with past data (e.g., forward-fill). As a result, it may **fail to reflect instantaneous or unobserved systemic degradation**. However, the **change signal (derivative)** remains informative, since updates from active routes still propagate directional shifts.
    - **Note:** We assume that **every route invocation is logged**. If requests are missing or not recorded, then both the **state reconstruction** and the **change detection** become unreliable, potentially leading to incorrect inferences.
    - We are also assuming that each request has equal probability (useful for the derivative) but inadequate for the expected latency at time $t$.
- (Routed) What is the latency of route $x$ at time $T$? It’s provided by the data.

Our data is of the form 

- Time: …
- Route: …
- Duration: …

## How to think about latency modelling?

> …
> 

## Task Set

> …
> 

## Technical Mechanism Set

> How to do near nearest-neighbor search(at time t, x)?
> 

### Which are type of aggregation (metrics) that can be done over a bucket (slide)  over latency data?

These are derived time-series metrics computed over a latency bucket or sliding window.

- **P95 / P99 / Percentiles:** Captures high-latency behavior beyond the mean.
- **Mean / Average:** Standard central tendency of latencies.
- **Median / P50:** Robust measure less sensitive to outliers.
- **Variance / Std Dev:** Quantifies the spread or variability of latencies.
- **Histogram / Distribution:** Provides a full view of latency distribution within the bucket.
- **Rate / Count:** Number of requests or events in the bucket.
- **Tail Latency Contribution:** Measures how extreme latencies influence overall performance.
- **Deviation-Based Metrics:** Measures how individual latency observations deviate from expected behavior (e.g., residuals relative to moving averages, deviations from predicted latency using a model, or anomaly scores).

### How to combine metrics view from routes - to a comprehensive derived metric  of the system?

> This is a derived time series that synthesizes multiple route-level series into a comprehensive system-level metric.
> 

Strategies:

- Max Route-Request Latency From the Set.
- Min  Route-Request Latency From the Set.
- Simple Route - Request Latency Set  Average.
- Simple Route - Request Latency Set  Average Deviation.

### How can we ensure that, for example, the P95 latency over one hour matches the P95 derived from the aggregation of 1‑minute buckets?

> For efficiency, we rely on 1‑minute metrics to avoid recomputing over many GBs of data. How can we maintain **consistency** when supporting multi-resolution aggregation? Specifically, how can we ensure that, for example, the P95 latency over one hour matches the P95 derived from the aggregation of 1‑minute buckets?
> 

> How to derived  Average, P50 Average (Median), P75 Average, Variance of Log-Latency, Max Value - using 1min  - data (statistics) resolution?
> 

Strategies:

- t-digest: …
- …

Evaluation Criteria:

- Compression ratio: the size of the compressed representation compared to the original data.
- Consistency: It's the P95 latency from the orignial data - equal to the P95 latency from the reconstructed data.
- Computational efficiency: the time it takes to compress and decompress the data, as well as the time it takes to compute statistics

## Representation Set

> Which kinds of analytical representations serves to answer the questions?
> 

### **System Latency Deviation Decomposition Representation**

> …
> 

Strategies:

- **Is interference an intrinsic**, stable relationship between routes, or a context-dependent phenomenon that only “activates” under certain workload conditions?
- **Geometric view** of the workload space: identifying regions where interference occurs.
- **Simulation view**: how to learn to simulate latency under different workload patterns.
- **Understanding interference** in workload subsets: considering structure, execution timing, order, and other dependencies that affect latency.
- **Introducing an intermediate** effective abstraction—a latent resource—through which workloads interact; this latent resource is then used to derive latency deviations.
- …

## QA

### Is task-latency correlation any good?

- …

## References

- https://en.wikipedia.org/wiki/Change_detection
- https://en.wikipedia.org/wiki/Interval_tree
- https://en.wikipedia.org/wiki/Segment_tree
- https://en.wikipedia.org/wiki/Moving_average
- https://en.wikipedia.org/wiki/Standard_score
- https://en.wikipedia.org/wiki/Isolation_forest
- https://bactra.org/notebooks/state-space-reconstruction.html
- https://en.wikipedia.org/wiki/Standard_deviation
- https://en.wikipedia.org/wiki/Data_binning
- https://en.wikipedia.org/wiki/Isolation_forest
- https://en.wikipedia.org/wiki/Intensive_and_extensive_properties
- https://en.wikipedia.org/wiki/Hysteresis
- https://en.wikipedia.org/wiki/EWMA_chart
- https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average
- https://en.wikipedia.org/wiki/Infinite_impulse_response
- https://en.wikipedia.org/wiki/Convolution
- https://en.wikipedia.org/wiki/Kernel_smoother
- https://en.wikipedia.org/wiki/Inverse_problem
- https://en.wikipedia.org/wiki/Kaplan%E2%80%93Meier_estimator
- https://en.wikipedia.org/wiki/Identifiability
- https://en.wikipedia.org/wiki/Granger_causality
- https://en.wikipedia.org/wiki/Force_field_(physics)
- [User-System Interaction Event Stream](https://app.notion.com/p/User-System-Interaction-Event-Stream-331c0f5171ec8081aba6da90b6892946?pvs=21)
