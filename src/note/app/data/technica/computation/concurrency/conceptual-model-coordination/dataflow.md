---
tags: [concurrency-model]
---

# Dataflow


> The **Dataflow concurrency model** is a model of computation where **execution is driven by the availability of data** rather than by a pre-defined sequence of instructions. In this model, **operations (nodes)** are only triggered (i.e., become *eligible to execute*) when **all of their input data is available**—hence modeling computation as a directed graph of dependencies.
> 

### 📚 Terminology

- **Dataflow programming** (a paradigm where control flow is driven by the availability of data)
- **Dataflow architectures** (hardware or virtual machines designed around data availability rather than instruction order)
- **Dataflow analysis** (a compiler technique for tracking how data moves through a program)
- **Data pipelines** (as in ETL systems)

## 📌 Formalism

- **Core Abstraction**: A **Dataflow graph**, where:
    - **Nodes** represent operations or instructions.
    - **Edges** represent data dependencies (tokens flowing along edges).
- **Execution Rule**: A node *fires* (executes) as soon as all its input edges carry data (are "ready").
- **Concurrency Semantics**: Since multiple nodes may become ready independently, they can be executed **in parallel** without explicit synchronization.

## Expressive Power

> (**Model of Computation → Process**) What kinds of processes can be naturally represented in this computational model?
> 

| **Computation Type** | **Why Dataflow Works Well** | **Example** |
| --- | --- | --- |
| **Incremental/Reactive Updates** | Values propagate automatically once inputs are available | UI frameworks: auto-updating a UI when data changes |
| **Streaming Computations** | Results are computed as data arrives, not after it's complete | Real-time video/audio processing, sensor pipelines |
| **Pipeline Processing** | Each step waits for and operates on its input as soon as it's ready | Image filters, data cleaning pipelines |
| **Constraint Solving** | Variables are resolved as their dependencies become satisfiable | Spreadsheet cells, constraint-based animation |
| **Parallel Functional Computation** | Independent expressions evaluate in parallel as soon as data is ready | Functional dataflow graphs, e.g., in Lucid or TensorFlow |
| **Reactive Systems** | Events trigger computations that react once dependencies are resolved | Functional Reactive Programming (FRP), signals in hardware |
| **Distributed Data Pipelines** | Nodes perform operations asynchronously, triggered by data availability | Apache Beam, Flink, NiFi |
| **Circuit Simulation** | Gates update outputs once inputs stabilize | Digital logic simulation, VHDL-level modeling |

## Tools

| **Library / Framework** | **Language(s)** | **Description** | **Key Features** | **Typical Use Cases** | **License** |
| --- | --- | --- | --- | --- | --- |
| **Apache Beam** | Java, Python, Go | Unified API for batch and streaming data pipelines | Portable runners (Flink, Spark, Dataflow), scalable | Large-scale ETL, real-time & batch processing | Apache 2.0 |
| **Apache Flink** | Java, Scala | Distributed stream processing framework with dataflow model | Stateful streams, event-time, fault-tolerance | Real-time analytics, event-driven applications | Apache 2.0 |
| **Apache NiFi** | Java | Visual dataflow automation and routing | Drag-and-drop UI, backpressure, extensible processors | Data ingestion, IoT dataflows | Apache 2.0 |
| **RxJava / ReactiveX** | Java, JS, Python, .NET, etc. | Reactive functional dataflow programming | Observables, composability, async streams | UI event handling, reactive systems | Apache 2.0 / MIT |
| **Akka Streams** | Java, Scala | Reactive stream processing on top of Akka Actor system | Backpressure, DSL, async and fault-tolerant | Event-driven systems, reactive microservices | Apache 2.0 |
| **Google Cloud Dataflow** | Java, Python | Managed dataflow service on Google Cloud | Autoscaling, batch & streaming, integrated with GCP | Cloud ETL, real-time analytics | Proprietary (GCP) |
| **TensorFlow Dataflow Graph** | Python, C++ | Computation graph for ML workflows | Optimized graph execution, automatic differentiation | Machine learning pipelines | Apache 2.0 |
| **Dask** | Python | Parallel computing and dynamic task scheduling | Dynamic task graphs, distributed computing | Big data processing in Python | BSD |
| **Sodium** | C++, Java, JavaScript, .NET | Functional reactive programming library | Continuous/discrete streams, memory safe | GUIs, robotics, event-driven systems | MIT |
| **Bacon.js** | JavaScript | Functional reactive programming for JS | Event streams, properties | Web UI, reactive front-end apps | MIT |
| **LabVIEW** | Visual (Graphical) | Visual dataflow programming language | Real-time data acquisition, graphical node-based flows | Engineering, control systems | Proprietary |
| **Quartz Composer** | macOS (Visual) | Visual node-based dataflow programming | Multimedia, interactive visual programming | Multimedia installations, interactive art | Proprietary |
| **Spring Cloud Data Flow** | Java | Microservice orchestration with dataflow pipelines | Integration with Spring Boot, supports batch/streaming | Enterprise microservices and data pipelines | Apache 2.0 |
| **Hazelcast Jet** | Java | Distributed stream and batch processing | Event-time, fault tolerance, scalable | Real-time analytics, streaming | Apache 2.0 |
| **Esper** | Java, .NET | Complex event processing with dataflow concepts | Temporal event patterns, low latency | Fraud detection, monitoring systems | GPL |
| **Streamlit** | Python | Reactive dataflow-driven UI apps | Easy UI building, rapid prototyping | Data apps, dashboards | Apache 2.0 |
|  |  |  |  |  |  |

## Case Studies

| **System** | **Domain** | **Type** | **Dataflow Model** | **Distinguishing Features** |
| --- | --- | --- | --- | --- |
| **TensorFlow** | Machine Learning / Deep Learning | Software framework | Dynamic + Static Dataflow | Computation modeled as graphs of ops; lazy evaluation; support for control flow ops |
| **Apache Beam** | Distributed Stream + Batch Data | Stream processing model | Unified Dataflow | Abstracts over runners (Flink, Spark); event-time processing; windowing; streaming + batch |
| **NiFi** | Data Ingestion / ETL | GUI-based pipeline engine | Dynamic Dataflow | Real-time flow-based programming; supports backpressure, provenance, routing |
| **Lucid** | Programming Language | Functional Dataflow Language | Deterministic Dataflow | Declarative language where programs are intensional expressions over data streams |
| **LabVIEW** | Embedded / Control Systems | Visual programming IDE | Graph-based Dataflow | Nodes are operations wired with signals; supports parallel hardware interaction |
| **Reactive Extensions (Rx)** | UI / Event-driven Programming | Library (push streams) | Event/Data-Driven Reactive | Uses observable sequences; enables stream transformations and event coordination |
| **Simulink (MATLAB)** | Control Systems / Simulation | Visual modeling tool | Signal/Dataflow Blocks | Block diagrams simulate systems using sample rates; supports hybrid models |
| **KPN (Kahn Process Networks)** | Theoretical Model | Formal concurrency model | Deterministic Asynchronous | Processes read from unbounded FIFOs; preserves determinism in concurrent systems |
| **Arvind’s Tagged-Token Machine** | Hardware Architecture | Dataflow processor design | Tagged-token Dataflow | Tokens carry tags to enable dynamic execution; handles instruction-level parallelism |
| **SDF (e.g., Ptolemy II)** | Signal Processing / Embedded | Modeling framework | Static Synchronous Dataflow | Token rates are fixed; enables compile-time scheduling; used for real-time applications |
| **Microsoft Power Automate (Flow)** | Workflow Automation | GUI Workflow Engine | Event/Data Triggered Flows | Business logic as event/data-driven pipelines |
| **Google Dataflow (Runner)** | Cloud Data Processing | Cloud processing backend | Unified Batch/Stream Model | Execution engine for Apache Beam pipelines |
| **Hume** | Real-Time Programming | Functional + State-based | Stream-Oriented Dataflow | Designed for predictable resource-bounded execution in real-time systems |
| **Verilog / VHDL (at RTL)** | Hardware Design / Simulation | Hardware Description Language | Signal-level Dataflow | Models logic at signal level with dataflow semantics; used in synthesis and simulation |
| **Airflow** |  |  |  |  |
| **Dask** |  |  |  |  |

## QA

### What types of processes are easily represented using the Dataflow Model?

### (Problem - Process → Model of Computation) In which model of computation is this process most naturally or easily expressed?

> 

### (Model of Computation → Process) What kinds of processes can be naturally represented in this computational model?

> 

## References

- https://en.wikipedia.org/wiki/Dataflow
- https://timelydataflow.github.io/timely-dataflow/
- Gilles Kahn (1974). The Semantics of a Simple Language for Parallel Programming.
In: Information Processing 74, North-Holland.
- Jack B. Dennis (1974). First version of the Data Flow Scheme. In: Information Processing 74, North-Holland.
- W. B. Ackerman (1975). Data Flow Languages. In: IEEE Computer, Vol. 15, No. 2.
- Edward A. Lee, David G. Messerschmitt (1987). Synchronous Data Flow. In: Proceedings of the IEEE, 75(9), pp. 1235–1245.
- Lucid (Ashcroft & Wadge, 1977): A dataflow functional language.
- MIT Tagged-Token Dataflow Architecture (Arvind & Thomas, 1980s): Hardware dataflow execution model.
- Tools
    - https://github.com/spotify/luigi?tab=readme-ov-file
    - https://streamlit.io/