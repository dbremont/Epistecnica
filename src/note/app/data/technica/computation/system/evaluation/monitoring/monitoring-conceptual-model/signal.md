---
tags: [ipc]
---

# Signal


> In these notes, we will explore the concept of a ***Monitoring Signal*** as an umbrella concept for all forms of monitoring data produced by software systems.
> 

## Formulation

### **What is a Monitoring Signal?**

A **monitoring signal** is any **observable, time-indexed emission** produced by a software system, its execution environment, or its control plane that **encodes information about the system’s internal state, behavior, performance, or interactions**, and that can be **consumed by monitoring, diagnostic, or control processes**.

### Which are the properties of a  Monitoring Signal?

| **Property** | **Description** |
| --- | --- |
| **Observable** | The signal is externally accessible to an observer, collector, or instrumentation system without requiring semantic reconstruction of internal system state. |
| **Time-indexed** | The signal is situated in time, either explicitly (timestamped) or implicitly (ordered within a temporal context), enabling temporal correlation and analysis. |
| **Emitted** | The signal is produced as a direct consequence of system execution or control activity, rather than inferred post-hoc from secondary artifacts. |
| **Informational** | The signal carries interpretable information about system state, behavior, or change, as opposed to undifferentiated noise. |
| **Consumable** | The signal is produced for downstream use—inspection, transformation, aggregation, inference, or actuation—by humans or automated systems. |
| **Attributable** | The signal can be associated with a producing entity, component, or scope (e.g., host, service, operation, resource). |
| **Contextualizable** | The signal may be enriched or correlated with contextual metadata (environment, version, tenant, trace context). |
| **Finite in Form** | Each emitted signal instance has a bounded representation, even if the signal stream is unbounded over time. |
| **Transportable** | The signal can be conveyed across process, host, or network boundaries to a monitoring system. |
| **Processable** | The signal admits mechanical processing (filtering, aggregation, correlation) without requiring human interpretation at ingestion time. |

### How to characterized it?

| **Dimension** | **Variable Name** | **Value(s)** |
| --- | --- | --- |
| **Origin** | Execution layer | OS; runtime; kernel |
|  | Application layer | Business logic; domain events |
|  | Infrastructure layer | Network; storage; orchestration |
|  | Control plane | Configuration; deployment state; scaling state |
| **Representation** | Metric | Counters; gauges; histograms; summaries |
|  | Log | Textual logs; structured logs; audit logs |
|  | Span | Operation span; RPC span; database span |
|  | Event | Domain event; lifecycle event; control event |
|  | Profile | CPU profile; memory profile; lock profile |
|  | Topology | Service graph; dependency graph; resource graph |
|  | Alert | Threshold alert; anomaly alert; composite alert |
| Temporal Structure | Continuous | Time-series measurement; streaming measurement |
| Temporal Structure | Discrete | Instantaneous event; logged occurrence |
| Temporal Structure | Episodic | Bounded interval; causally scoped interval |
| Semantic Density | Low-level | Syscalls; GC pauses; scheduler activity |
| Semantic Density | Mid-level | Request latency; error rate; queue depth |
| Semantic Density | High-level | Domain event; business failure; SLA breach |
| Degree of Processing | Raw | Direct emission; unaggregated sample |
| Degree of Processing | Transformed | Aggregated; sampled; filtered |
| Degree of Processing | Derived | Rates; percentiles; SLO indicators; anomaly scores |
| **Intended Use** | Observation & inspection | Visibility; trend analysis |
|  | Diagnosis & debugging | Root cause analysis; forensic analysis |
|  | Alerting & incident detection | Threshold alerts; anomaly detection |
|  | Control & feedback loops | Autoscaling; circuit breaking; adaptive configuration |

### Why can this be used as an umbrella term?

The term **monitoring signal** functions as an effective umbrella because it is:

1. **Format-agnostic:** It does not assume metrics, logs, traces, or events, and therefore does not bias system design toward a specific representation.
2. **Semantically inclusive:** It encompasses both numeric and symbolic emissions, structured and unstructured data, raw and derived artifacts.
3. **Aligned with systems and control theory:** In these disciplines, a *signal* is any observable manifestation of system state used for estimation, diagnosis, or control—precisely the role monitoring data plays.
4. **Compatible with processing pipelines:** Monitoring systems can be modeled as signal-processing pipelines: emission → collection → transformation → interpretation → action.
5. **Stable under technological change:** Unlike vendor- or paradigm-specific terms, “signal” remains valid as instrumentation techniques evolve.

### Which are the related terms?

| **Term** | **Description** |
| --- | --- |
| **Observability Data** | The collected and stored body of monitoring signals, typically organized, indexed, and enriched to support querying, correlation, and analysis of system behavior and state. |
| **Indicator** | A derived, evaluative construct computed from one or more monitoring signals, intended to summarize system condition relative to goals, thresholds, or expectations (e.g., SLI, KPI). |
| **Telemetry** | The automated emission and transmission of monitoring signals from a system to a remote collection or analysis endpoint, emphasizing transport and instrumentation rather than interpretation. |

## Signal Space

> *What happened?*
> 

> Note: This is not a representation (format) concept.
> 

| **Category** | **Signal Type** | **Description** | **Instance(s)** | **Generation Mechanism** | **Representation Mechanism** |
| --- | --- | --- | --- | --- | --- |
| **Execution** | Behavioral Signal | Observable runtime behavior produced by executing code paths in response to inputs or schedules. | Request handled, job executed, function invoked | Program execution, scheduler dispatch, request routing | Metrics, logs, spans, profiles |
| **Execution** | Performance Signal | Evidence of efficiency and timing characteristics of execution. | Latency, throughput, execution time | Timing instrumentation, counters, sampling | Metrics, spans, profiles |
| **Execution** | Fault Signal | Evidence of incorrect or failed execution relative to expected behavior. | Exception thrown, timeout, failed retry | Error handling paths, assertion failures, fault detectors | Logs, metrics, spans, events |
| **State** | State Signal | Snapshot or transition of internal or external system state. | Cache miss, state transition, flag value | State mutation in memory, storage, or config | Metrics, logs, events |
| **State** | Capacity Signal | Evidence of available, consumed, or exhausted system resources. | Disk full, memory pressure, CPU saturation | Resource allocation, quota enforcement | Metrics, profiles |
| **Structure** | Dependency Signal | Evidence of interaction or coupling between components or services. | Service call, DB query, API dependency | IPC, RPC, network communication | Spans, topology, logs |
| **Structure** | Topological Signal | Evidence of structural relationships and system composition. | Service graph, pod–node mapping | Service discovery, orchestration control plane | Topology, logs |
| **Change** | Change Signal | Evidence that the system or its environment has been modified. | Deployment, config update, scaling event | CI/CD actions, control-plane mutation | Events, logs, topology |
| **Control** | Health Signal | Evidence of system self-assessment or supervisory status. | Heartbeat, readiness probe result | Health checks, watchdogs | Metrics, events |
| **Control** | Alerting Signal | Evaluated condition indicating abnormal or noteworthy state. | High latency alert, error budget burn | Rule evaluation, anomaly detection | Alerts |
| **Security** | Security Signal | Evidence of access, identity, or policy-related activity. | Login attempt, auth failure, policy violation | AuthN/AuthZ evaluation, audit hooks | Logs, events, metrics |
| **Domain** | Domain Signal | Evidence of domain-level or user-meaningful occurrences. | Order placed, payment failed, user signup | Business logic execution | Events, logs, metrics |

## Signal Encoding Space

> *How is it encoded?* (Signal Representation)
> 

| **Signal Representation** | **Description** | **Representation Capacity** | **Instance(s)** |
| --- | --- | --- | --- |
| **Metric** | Aggregated, time-indexed numeric representation of system behavior, optimized for statistical analysis and trend detection; encodes behavior via counters, gauges, and distributions rather than individual occurrences. | Low semantic richness per data point; high temporal continuity; high statistical compressibility; no per-entity causality or payload detail. | CPU usage %, request rate (RPS), error ratio, latency histogram (p50/p95/p99), queue depth |
| **Log** | Discrete, append-only record representation of individual events or messages, expressed as textual or structured entries; prioritizes completeness and forensic detail over aggregation efficiency. | High semantic richness; unbounded payload; low structural constraint; weak native temporal aggregation; no intrinsic causality model. | Application log line, error stack trace, audit record, HTTP access log |
| **Span** | Temporal and causal representation of an operation, encoded as a bounded time interval enriched with contextual metadata and explicit parent–child relationships forming traces. | Medium–high semantic richness; explicit causality; bounded duration; structured metadata; moderate aggregation potential via trace analysis. | HTTP request span, database query span, RPC call span, trace segment |
| **Event** | Lightweight discrete representation of a single occurrence without enforced duration or causal structure; commonly used for domain-level or lifecycle signaling. | Medium semantic richness; point-in-time only; minimal structural guarantees; flexible payload; weak temporal continuity. | Deployment event, feature flag change, user signup event, job completion signal |
| **Profile** | Statistical, sampling-based representation of execution behavior (e.g., CPU, memory, call stacks) aggregated over time windows rather than per-request. | Low semantic richness per sample; high behavioral density; probabilistic accuracy; captures systemic hotspots but not individual executions. | CPU flame graph, heap allocation profile, lock contention profile |
| **Topology** | Graph-oriented representation capturing structural relationships and dependencies among system components. | High structural expressiveness; low temporal resolution; encodes relationships rather than behavior; supports impact and dependency analysis. | Service dependency graph, network map, Kubernetes pod–service graph |
| **Alert** | Evaluative representation derived from other signals, encoding detected conditions, anomalies, or threshold violations rather than raw observations. | Very low raw information content; high decision salience; binary or categorical state; derivative and lossy by design. | High latency alert, error budget burn alert, host down notification |

## Principle Space

> Which principles should guide Signal Selection, Capture Representation, etc?
> 

| **Principle** | **Description** | **Implications** |
| --- | --- | --- |
| **Relevance** | Only capture signals that are necessary and sufficient to explain, predict, or control system behavior under relevant failure modes. | Guides **signal selection**; prevents data overload and irrelevant instrumentation. |
| **Minimal Intrusiveness** | Instrumentation should minimize performance and behavioral impact on the system. | Guides **capture mechanisms**; favors lightweight, non-blocking, or out-of-band techniques. |
| **Causal Traceability** | Signals should enable reconstruction of causal chains in system operations. | Guides **representation design**, e.g., traces, structured logs, and correlation IDs. |
| **Observability Completeness** | Capture sufficient signals to detect and diagnose all anticipated failure modes. | Ensures **coverage in instrumentation planning**; informs which metrics, logs, or traces are necessary. |
| **Aggregation & Abstraction** | Raw signals should be encoded in forms suitable for analysis, alerting, and decision-making. | Guides **representation techniques**; supports metrics, dashboards, SLIs, and derived indicators. |
| **Correlation & Context** | Signals should carry context (e.g., IDs, timestamps, system/environment info) for linking events and operations. | Improves **cross-service or cross-machine analysis**; enables end-to-end observability. |
| **Adaptivity** | Observability strategies should support dynamic adjustment based on system load, incidents, or evolving requirements. | Guides **dynamic instrumentation and sampling**; reduces overhead while maintaining coverage. |
| **Consistency & Standardization** | Signal formats, naming, and units should be uniform across the system. | Facilitates **aggregation, parsing, and automated analysis**; reduces interpretation errors. |
| **Security & Privacy** | Signals should avoid leaking sensitive information unless strictly necessary and compliant. | Guides **logging and representation policies**; critical for compliance in production environments. |
| **Actionability** | Captured signals should support operational decisions, alerting, or control loops. | Ensures that observability investments translate into **practical system improvements**. |

## Technical Space

> Which types of techniques are used in signal generation?
> 

### Dimension

| Technique Dimension | Description | Instance(s) |
| --- | --- | --- |
| **Signal Selection Technique** | How the system produces an observable phenomenon as a consequence of execution or state change | Native emission, explicit code instrumentation, implicit instrumentation (eBPF, bytecode weaving), event-triggered emission, sampling |
| **Signal Capture Technique** | How generated signals are intercepted and collected | In-process SDKs, agents, sidecars, kernel probes, network interception, scraping |
| **Signal Representation Technique** | How captured signals are encoded into a consumable form | Metrics (counters, gauges, histograms), logs (textual, structured), spans/traces, events |
| **Signal Correlation Technique** | How related signals are linked at or near the source | Trace context propagation, request IDs, causal metadata injection |
| **Signal Aggregation-at-Source Technique** | How signals are reduced or summarized before export | Local counters, sliding windows, histograms, pre-aggregation |
| **Signal Sampling Technique** | How signal volume is reduced at generation or capture time | Head-based sampling, probabilistic sampling, rate limiting |
| **Signal Enrichment Technique** | How contextual metadata is attached to signals at emission | Service tags, environment labels, topology metadata |
| **Signal Emission Control Technique** | How signal production is gated or regulated | Log levels, dynamic instrumentation flags, feature gates |
| **Signal Fidelity Management Technique** | How precision and overhead are balanced | Precision scaling, adaptive sampling, resolution tuning |

### **Signal Capture Technique**

> When should they be captured? By what mechanisms should they be captured? How much should I Used Logging in an Application?  Which are the implications?
> 

| **Category** | **Technique** | **Description** |
| --- | --- | --- |
| **Static Instrumentation** | Compile-Time Logging / Hardcoded Metrics | Signals are embedded in code at development time. High predictability and low runtime complexity, but requires redeploy to change. |
| **Dynamic Instrumentation** | Runtime Log Levels / Feature Flags / Sampling | Signals captured are modulated at runtime via configuration. Enables selective observability and controlled performance impact. |
| **Live / On-Demand Instrumentation** | eBPF Probes, Runtime Trace Injection, Debug Hooks | Captures signals without redeploying. Allows deep investigation of incidents but increases operational risk. |
| **External Observation** | Sidecar Agents, Network Taps, System Metrics (CPU, I/O) | Observes system behavior without modifying application code. Provides coarse-grained or low-semantic signals. |
| **Derived Capture** | Aggregation, Metrics Computation, Anomaly Detection | Signals are synthesized from other signals (e.g., rate of failed requests). Useful for monitoring trends, alerts, or dashboards but may lose fine-grained causal detail. |

### **Signal Representation Technique**

| **Category** | **Description** | **Technique(s)** |
| --- | --- | --- |
| **Metric-Based Representation** | Aggregates raw signal into numeric form, often time-indexed. Optimized for trend detection, anomaly detection, and statistical analysis. | Counters, Gauges, Histograms, Distributions |
| **Log-Based Representation** | Captures individual events with rich context. Prioritizes forensic detail and completeness over aggregation efficiency. | Structured Logs, Append-Only Event Records |
| **Trace-Based Representation** | Represents causally connected sequences of operations, usually for request-level analysis or performance profiling. | Spans, Trace Trees, Context Propagation |
| **Composite / Derived Representation** | Synthesizes multiple signals into higher-level indicators. Facilitates decision-making but may obscure underlying events. | Dashboards, SLIs, Alert Metrics |
| **Sampling / Probabilistic Representation** | Represents a subset of signals to reduce volume and overhead while retaining statistical fidelity. Useful for high-throughput systems. | Event Sampling, Reservoir Sampling |

### Log Data Representation

> **Log metadata** refers to the structured, auxiliary fields attached to a log entry—such as timestamps, severity levels, execution context identifiers (e.g., trace ID, span ID, process/thread ID), and source attributes—that enable machine-parsable indexing, correlation, filtering, and analytical processing of event logs within distributed and observable systems.
> 
- ¿What’s information is usually included?
- Logging is for events with identity; metrics are for events without identity. They are not the same thing.

| **Metadata Field** | **Description** |
| --- | --- |
| **Timestamp** | The precise time the log event occurred (typically in ISO 8601 or epoch format), often with millisecond or nanosecond precision. |
| **Log Level / Severity** | Indicates the importance or criticality of the log entry (e.g., DEBUG, INFO, WARN, ERROR, FATAL, TRACE). |
| **Message** | The main descriptive content of the log, often a human-readable summary of the event. |
| **Application / Service Name** | Identifies which application, microservice, or component produced the log. |
| **Environment** | Runtime environment (e.g., `dev`, `staging`, `prod`) to distinguish logs across deployments. |
| **Host / Instance ID** | The physical or virtual machine, container, or pod identifier where the log was generated. |
| **Thread / Process ID** | Identifier for the OS thread or process that emitted the log message. |
| **Logger Name / Class** | The name of the logging class, module, or library (e.g., `com.example.MyClass`). |
| **Trace ID** | Unique ID that connects logs across services for distributed tracing (used in correlation). |
| **Span ID** | Subdivision of a trace representing a single unit of work (part of distributed tracing). |
| **Request ID / Correlation ID** | Identifier used to group all logs associated with a single user request or transaction. |
| **User ID / Session ID** | ID of the authenticated user or session responsible for the action. |
| **HTTP Metadata** | Includes request method, path, status code, user-agent, IP address, latency, etc. |
| **Custom Tags** | Application-defined labels for filtering, such as `region=us-east-1`, `feature=beta-access`. |
| **Log Source** | The mechanism or agent that collected the log (e.g., syslog, Fluent Bit, Logstash). |
| **Log Format Version** | Schema version identifier if logs are structured (e.g., JSON format versioning). |
| **Exception / Stack Trace** | Captures stack information for errors or exceptions, if applicable. |
| **Event Type / Category** | Classification such as `AUTH_EVENT`, `DB_QUERY`, `SECURITY_ALERT`. |

### Log Data Representation Evolution

> 

> **Log Schema Evolution** refers to the **gradual change in the structure, format, or fields** of log records over time due to evolving application logic, infrastructure updates, instrumentation enhancements, or versioning. Logging systems must **gracefully accommodate schema changes** without breaking parsing, indexing, or querying functionality. Schema inference, version tagging, and backward compatibility handling are critical to support robust log analytics in dynamic environments.
> 

🔁 **Causes of Schema Evolution**

| **Source** | **Example** |
| --- | --- |
| **Application Updates** | New fields added to logs (e.g., `request_id`, `user_agent`) |
| **Instrumentation Changes** | Refactored logging format, renaming fields, or changing nesting |
| **Microservice Versioning** | Different services or service versions emitting different log shapes |
| **Observability Enhancements** | Adding structured context, new error codes, or business metadata |
| **Pipeline Rewrites** | Log shippers transforming or flattening schemas differently over time |

🧠 **Challenges**

| **Challenge** | **Impact** |
| --- | --- |
| **Parser Breakage** | Rigid log parsers may fail on unknown fields or structures |
| **Index Drift** | Schemaless backends (e.g., Elasticsearch) may suffer from index fragmentation or field-type conflicts |
| **Query Inconsistency** | Saved queries and dashboards may become invalid or misleading |
| **Backfill Difficulty** | Historical logs may not match new schema expectations |
| **Debugging Errors** | Missing or misaligned fields complicate root cause analysis |

🛠️ **Best Practices for Managing Schema Evolution**

| **Practice** | **Description** |
| --- | --- |
| **Schema Version Tagging** | Add a `schema_version` field to each log event to support conditional parsing or queries |
| **Optional Field Design** | Design log formats with optional fields that can safely be missing |
| **Schema Registry or Contract** | Define log schemas explicitly using JSON Schema, OpenTelemetry Logs, or Avro |
| **Schema Inference Tools** | Use dynamic field extractors (e.g., in Fluent Bit, Loki, or BigQuery) to infer and adapt to schema variations |
| **Field Type Governance** | Ensure consistent types for semantically identical fields (`status_code: string` vs `status_code: int`) |
| **Backward-Compatible Parsers** | Write parsers resilient to new fields or changes in field order |
| **Monitoring for Schema Drift** | Automatically detect and alert on field set anomalies or schema divergence using schema diffing or observability metrics |

### Representations System

| **Format** | **Description** | **Advantages** | **Disadvantages** | **Typical Use Cases** |
| --- | --- | --- | --- | --- |
| **Plain Text** | Free-form human-readable strings, unstructured logs | Easy to read manually; simple to implement | Difficult to parse programmatically; inconsistent | Small applications, quick debugging, legacy systems |
| **JSON** | JavaScript Object Notation, structured key-value pairs | Machine-readable; widely supported; flexible schema | Larger size than plain text; needs parsing | Cloud-native apps, microservices, observability pipelines |
| **XML** | Extensible Markup Language with nested tags | Strongly typed, schema validation possible | Verbose, larger size; slower parsing | Enterprise systems, legacy integration, configurations |
| **LTSV** | Labeled Tab-Separated Values, key:value tabular format | Simple, human-readable; easier parsing than plain text | Less popular, limited tool support | Lightweight logging, command-line tools |
| **CSV** | Comma-separated values, flat tabular format | Easy to parse and export to spreadsheets | Poor for nested or complex data structures | Simple logs, exports, batch processing |
| **Syslog** | Standardized text format used by syslog protocol | Standard for UNIX/Linux systems; widely supported | Limited structure; difficult complex queries | System logs, network devices |
| **Protobuf** | Protocol Buffers, binary serialization by Google | Compact size; fast serialization/deserialization | Requires schema; less human-readable | High-performance distributed systems, gRPC |
| **Avro** | Apache Avro, compact binary serialization with schema | Schema evolution support; compact | Requires tooling; binary format not human-readable | Big data pipelines, Hadoop ecosystem |
| **CEF** | Common Event Format, semi-structured plain text | Standardized for security events; extensible | Vendor-specific nuances; text-based | Security Information and Event Management (SIEM) |
| **GELF** | Graylog Extended Log Format, JSON-based extended format | Supports large messages, structured data | Graylog-specific; some complexity | Centralized logging with Graylog |

### **Log Optimization Strategy**

> **Log Optimization Strategies** are systematic approaches and techniques applied throughout the logging pipeline to **reduce resource consumption, improve processing efficiency, enhance storage management, and maintain log quality**—all while preserving the diagnostic and operational value of logs for monitoring, troubleshooting, security, and compliance purposes. These strategies address challenges such as excessive log volume, redundant or sensitive data, serialization overhead, and retention costs by employing methods like sampling, filtering, batching, compression, and retention policies to optimize the cost-effectiveness and performance of logging systems.
> 

| **Strategy Type** | **Strategy** | **Description** | **Typical Use Case** |
| --- | --- | --- | --- |
| **Volume Reduction** | **Sampling** | Emit only a subset of log events (e.g., 1%, adaptive, tail-based) to reduce ingestion and storage load. | High-traffic systems, distributed tracing |
|  | **Rate Limiting** | Enforce a maximum log emission rate per component or category. | Prevents log storms or bursts |
|  | **Deduplication** | Detect and suppress repetitive log messages. | Reduces noise during repeated failures |
|  | **Aggregation** | Combine multiple similar events into a summarized log entry. | Batch events over time or count occurrences |
| **Data Minimization** | **Field Filtering** | Exclude unnecessary fields or metadata from structured logs. | Save storage, improve indexing efficiency |
|  | **Redaction** | Mask or remove sensitive fields (e.g., PII, secrets). | Security, compliance, privacy |
|  | **Truncation** | Limit the length of fields or messages. | Prevent unbounded log sizes |
| **Serialization Efficiency** | **Compact Formats** | Use binary or compressed formats like Protobuf, Avro, or Zstd-compressed JSON. | Efficient transmission and storage |
|  | **Asynchronous Logging** | Queue log events in memory for background processing and emission. | Minimizes latency impact on application |
|  | **Batching** | Send logs in grouped batches rather than individually. | Reduces network overhead |
| **Retention Control** | **Rotation & Archival** | Move or delete old logs based on size/time policies. | Disk space management, compliance |
|  | **Tiered Storage** | Use hot/warm/cold storage (e.g., SSD, S3, Glacier) depending on log age/frequency of access. | Cost-efficient long-term storage |
| **Index Optimization** | **Index Tuning** | Index only necessary fields, avoid high-cardinality tags. | Improves query speed and reduces index bloat |
|  | **Log Schema Governance** | Enforce structured logging with controlled schemas. | Ensures consistency and parsing performance |

## Signal Selection

> What signals should be captured? Which are the pitfalls in Signal Selection?
> 

> What information is necessary and sufficient to explain, predict, or control system behavior under relevant failure modes?
> 

### Criteria

| **Criterion** | **Description** |
| --- | --- |
| **Failure Mode Coverage** | Degree to which the signal discriminates between known or plausible failure modes (e.g., CPU saturation vs. lock contention). |
| **Causal Proximity** | How directly the signal reflects the underlying mechanism rather than a downstream symptom. |
| **Information Density** | Amount of explanatory power per unit of signal volume (high signal-to-noise ratio). |
| **Temporal Resolution** | Whether the signal’s sampling or emission frequency is sufficient to capture transient or cascading failures. |
| **Actionability** | Whether the signal can directly inform an operational or automated response. |
| **Cost of Capture** | Runtime overhead, storage cost, cardinality explosion risk, and operational complexity. |
| **Stability Under Change** | Robustness of the signal’s semantics across deployments, refactors, or scaling events. |
| **Composability** | Ability to correlate the signal with others across layers (e.g., request ID, trace context). |
| **Audience Alignment** | Fit with the cognitive needs of operators, SREs, developers, or automated controllers. |

### Format Selection

> Which signal representation format should be used?
> 

| **Format** | **Purpose** | **Strengths** | **Limitations** |
| --- | --- | --- | --- |
| **Metric** | Quantitative state and behavior measurement | Cheap, aggregatable, alert-friendly, trend-oriented | Low semantic detail; poor for root cause analysis |
| **Log (Structured)** | Discrete event and decision explanation | High semantic richness; human-readable; flexible | Expensive; high cardinality; weak aggregation |
| **Trace / Span** | End-to-end execution flow | Causal ordering across boundaries; latency attribution | Sampling required; storage overhead |
| **Event (Domain)** | Durable business fact recording | Replayable; auditable; schema-governed | Not diagnostic by default; requires consumers |
| **Profile** | Resource usage attribution | Low overhead; identifies hotspots | Minimal domain semantics |
| **Snapshot / State Dump** | Point-in-time system state | High forensic value | High cost; risky in production |

| **Criterion** | **Guidance** |
| --- | --- |
| **Question Type** | “How many / how fast?” → Metrics; “Why this instance?” → Logs/Traces |
| **Cardinality** | High-cardinality dimensions favor logs or events, not metrics |
| **Temporal Scope** | Continuous trends → Metrics; causal chains → Traces |
| **Audience** | Operators → Metrics; Developers → Logs/Traces; Auditors → Events |
| **Actionability** | Immediate alerts → Metrics; post-mortem → Logs/Traces |
| **Cost Sensitivity** | Tight budgets favor metrics and sampling |
| **Regulatory Needs** | Compliance requires events, not logs |
| **Change Tolerance** | Metrics must be stable; logs can evolve |

### Checklist

> Which are the things that we should log?
> 

| **Check** | **Description** |
| --- | --- |
| **Process Lifecycle Events** | Application start/stop, restart reasons, configuration load/reload, version/build identifiers. |
| **Boundary Crossings** | Entry and exit of external interfaces (HTTP requests, RPC calls, message consumption/production). |
| **State Transitions** | Meaningful internal changes (e.g., cache miss → fill, follower → leader, circuit closed → open). |
| **Decision Points** | Branches where the system chooses among alternatives (routing decisions, feature-flag evaluation, retry vs. fail). |
| **Invariant Violations** | Explicit checks that should “never happen” (contract breaches, impossible states). |
| **Error Conditions** | Failures that require investigation or intervention, with causal context. |
| **Recoverable Anomalies** | Retries, fallbacks, partial failures, degraded modes entered/exited. |
| **External Dependency Outcomes** | Calls to databases, APIs, queues—especially timeouts, errors, and latency outliers. |
| **Security-Relevant Events** | Authentication failures, authorization denials, privilege changes (without sensitive payloads). |
| **Resource Pressure Signals** | Log-worthy thresholds crossed (queue overflow, pool exhaustion), not continuous usage. |
| **Configuration & Feature Flags** | Changes in runtime behavior due to config or flag updates. |
| **Correlation Context** | Request IDs, trace IDs, user/session scope (bounded and sanitized). |
| **Business-Critical Events** | Domain-level events that explain user-visible outcomes (order rejected, transaction rolled back). |
| **Unexpected Input Shapes** | Malformed, truncated, or semantically invalid inputs that pass syntactic checks. |
| **System Self-Protection Actions** | Rate limiting, circuit breaking, load shedding, kill-switch activation. |

### Pitfall(s)

| **Pitfall** | **Description** |
| --- | --- |
| **Symptom-Only Instrumentation** | Capturing downstream effects (e.g., error rates) without upstream causal signals. |
| **Over-Aggregation** | Metrics that collapse heterogeneous behaviors, masking rare but critical failures. |
| **Unbounded Cardinality** | Labels or dimensions that explode combinatorially, rendering signals unusable. |
| **Static World Assumption** | Signals designed for steady-state behavior that fail under scale, load, or topology changes. |
| **Tool-Driven Selection** | Choosing signals because a platform supports them, not because the system requires them. |
| **Excessive Verbosity** | High-volume logs or traces with low marginal informational value. |
| **Lack of Failure Hypotheses** | Instrumentation without an explicit model of how the system can fail. |

### Case Study

| **Case** | **Description** | **Evaluation** |
| --- | --- | --- |
| CPU Usage Only | System monitors average CPU utilization to detect overload. | Insufficient: cannot distinguish busy-waiting, GC pressure, or lock contention. |
| Error Rate Without Context | Alerts fire on HTTP 500 rate spikes without request metadata. | Poor explanatory power; no causal attribution or blast-radius assessment. |
| High-Cardinality User IDs in Metrics | Metrics labeled with user identifiers for per-user analysis. | Operationally dangerous; leads to cardinality explosion and degraded monitoring systems. |
| Latency Percentiles + Traces | p50/p95/p99 latency metrics combined with sampled distributed traces. | Strong balance: detection via metrics, explanation via traces. |
| Queue Depth + Arrival Rate | Monitoring queue length alongside ingress rate. | Predictive: enables early detection of saturation before failure. |
| Business-Level Signals Only | Monitoring only KPIs (orders/min, revenue). | Necessary for impact assessment but insufficient for technical diagnosis. |

## QA

1. 🧱 **Fundamentals**
    - **What are the primary purposes of logging in a software system?**
    - **What is the difference between structured and unstructured logs?**
    - **Why is timestamping critical in log entries?**
    - **What are common log levels (e.g., `DEBUG`, `INFO`, `ERROR`), and when should each be used?**
    - **How does logging differ from monitoring and tracing?**
2. 🛠️ **Architecture & Design**
    - **What is a logging pipeline, and what are its typical components?**
    - **How does a centralized logging system differ from a decentralized one?**
    - **Explain the role of log shippers (e.g., Fluent Bit, Logstash) in a logging architecture.**
    - **What is log rotation, and why is it important?**
    - **What are some strategies to prevent logs from overwhelming system resources?**
3. ⚙️ **Performance and Optimization**
    - **Define ingestion throughput and write latency in the context of logging.**
    - **How does asynchronous logging improve application performance?**
    - **What are backpressure mechanisms in log pipelines, and how do they help?**
    - **What is log sampling, and when would you use it?**
    - **What are the trade-offs of real-time logging vs. batch logging?**
4. 🔐 **Security and Compliance**
    - **What is log tampering, and how can it be prevented or detected?**
    - **Which compliance frameworks require specific logging practices (e.g., HIPAA, GDPR, PCI-DSS)?**
    - **What is the purpose of audit logging, and how is it secured?**
    - **What does log anonymization or redaction mean, and when is it necessary?**
    - **How can cryptographic techniques be used to ensure log integrity?**
5. 🔍 **Analysis and Observability**
    - **What is log correlation, and why is it essential in distributed systems?**
    - **How would you perform root cause analysis using logs?**
    - **What is schema evolution in logs, and how can you handle it in a logging system?**
    - **Compare different log querying techniques (text search, SQL, label-based).**
    - **What role can machine learning play in log analysis?**
6. 🧠 **Advanced and Conceptual**
    - **What are logging modalities, and how do they help in designing log strategies?**
    - **How does log structure impact storage efficiency and query latency?**
    - **What is the difference between head-based and tail-based sampling?**
    - **Explain how a logging system supports observability in cloud-native environments.**
    - **What are the risks of over-logging, and how can they be mitigated systematically?**

### Should We Log Every Business Process Execution Even If There is Not Failure?

### Should We Used Id’s for Logs?

### How can I track a process that spans multiple computational entities, including across different machines?

## References

- [Serilog](https://serilog.net/)
- [Log Parsing](https://pbs.twimg.com/media/FxCDRkVaYAAhkYQ?format=jpg&name=4096x4096)
- [Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/)
- [Common Log Format](https://en.wikipedia.org/wiki/Common_Log_Format)
- [Tips for analyzing logs](https://news.ycombinator.com/item?id=33971432)
- [Program Modification](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-modification.md)
- [My Logging Best Practices](https://news.ycombinator.com/item?id=28759492)
- https://news.ycombinator.com/item?id=46346796
- https://news.ycombinator.com/item?id=30393683
- [Scuba: Diving into Data at Facebook](https://research.facebook.com/publications/scuba-diving-into-data-at-facebook/)
- https://news.ycombinator.com/item?id=37224651
- [Is it possible to use Serilog with OpenTelemetry?](https://stackoverflow.com/questions/67540739/is-it-possible-to-use-serilog-with-opentelemetry)
- https://news.ycombinator.com/item?id=28759492
- [8 Best Logging Practices to Keep Sensitive Data Out](https://dev.to/pragativerma18/8-best-logging-practices-to-keep-sensitive-data-out-39p9)
- [Tracing: Structured logging, but better](https://news.ycombinator.com/item?id=37562593) ([andydote.co.uk](http://andydote.co.uk/))
- https://news.ycombinator.com/item?id=20818106
- [Fast and Reliable Schema-Agnostic Log Analytics Platform](https://www.uber.com/en-DO/blog/logging/)
- https://news.ycombinator.com/item?id=31945564
- https://news.ycombinator.com/item?id=32800598
- https://news.ycombinator.com/item?id=35643255
- https://news.ycombinator.com/item?id=19497788
- https://news.ycombinator.com/item?id=12272642
- [https://news.ycombinator.com/item?id=8356695](https://news.ycombinator.com/item?id=8356695)
- https://news.ycombinator.com/item?id=20853586
- https://www.reddit.com/r/technology/comments/1q29eyg/tesla_loses_title_as_worlds_biggest_electric/