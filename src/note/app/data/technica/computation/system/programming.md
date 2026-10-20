# Programming

> **In this note**, we will explore the **technical domain of programming**, characterized by the goal of designing and implementing a program, and structured through a set of `building blocks`, `techniques`, `processes`,  `guiding principles`,  and the more abstract and encompassing  **programming models (paradigms)**.  Programming can be capture fundamentally by <Building Block,  Principle, Technique → Program>.
> 

> A **program** is a **finite sequence of instructions** that a computer or (**computing substrate**) can execute to perform a specific task or set of tasks, it’s basically a **theory of a process**.
> 

> **System** → A broader, interacting set of programs, components, or hardware designed to accomplish one or more tasks.
> 

> **Note:** The distinction between **Program** and **System** is somewhat arbitrary; it is made primarily for **cognitive convenience**.
> 

> **Programming** is the art of fitting computable entities together to meet a specific purpose and generate a computational process.
> 

- [ ]  Should We Need to Add a Note on Programming Problems Space → In order to incorporate let’s say `API Gateway`.
- [ ]  How to think the genericity of a computation description? Generic Data, Operating on Functions, etc.

Classify This:

1. **CAP Theorem & Consistency Models**
Trade-offs between consistency, availability, and partition tolerance; includes strong, eventual, and causal consistency.
2. **Scalability**
Vertical and horizontal scaling strategies.
3. **Fault Tolerance & Failover Mechanisms**
Maintaining availability during hardware/software failures.
4. **Data Replication**
Replica synchronization for availability and durability.
5. **Data Sharding & Partitioning**
Horizontal data distribution for scalability and performance.
6. **Consistent Hashing**
Load/data distribution strategy for dynamic clusters.
7. **Distributed Transactions**
2PC, Saga, Outbox patterns.
8. **Consensus Algorithms**
Paxos, Raft.
9. **Distributed Locks**
Coordination via ZooKeeper/Redis.
10. **Distributed System Architectures**
Monolith, microservices, event-driven systems.
11. **Microservices Architecture**
12. **Event-Driven Architecture**
Event Sourcing, CQRS.
13. **Service Discovery**
Consul, Eureka, Kubernetes DNS.
14. **API Gateway**
NGINX, Kong, Spring Cloud Gateway.
15. **Inter-service Communication**
REST, gRPC, GraphQL, async messaging.
16. **Remote Procedure Call (RPC)**
gRPC, Thrift.
17. **RESTful API Design**
18. **WebSockets**
19. **Socket Programming (TCP/IP, UDP)**
20. **Message Queues & Streaming Platforms**
Kafka, RabbitMQ, JMS.
21. **Kafka Deep Dive**
Partitions, consumer groups, exactly-once semantics.
22. **Distributed Databases**
Cassandra, MongoDB, HBase.
23. **Caching Mechanisms & Patterns**
Redis, Memcached, Cache-Aside, Write-Behind.
24. **In-memory Data Grids**
Hazelcast, Infinispan.
25. **Database Indexing**
26. **CDN (Content Delivery Networks)**
27. **Load Balancing**
NGINX, Kubernetes, client-side LB.
28. **Circuit Breakers & Retry Patterns**
Resilience4j.
29. **Rate Limiting & Throttling**
30. **Monitoring & Metrics**
Prometheus, Grafana, Micrometer.
31. **Logging & Distributed Tracing**
OpenTelemetry, Jaeger, Zipkin.
32. **Alerting & Observability Practices**
33. **Authentication & Authorization**
OAuth2, JWT, OIDC.
34. **Encryption & Secure Communication**
SSL/TLS, mTLS.
35. **Distributed Coordination Systems**
ZooKeeper, etcd.
36. **Cluster Management**
Kubernetes.
37. **Cloud-Native Development**
12-factor apps, sidecars, service mesh.
38. **Serverless Computing**
AWS Lambda concepts.
39. **Java Concurrency**
ExecutorService, CompletableFuture, ForkJoinPool.
40. **Thread Safety & Synchronization**
41. **Java Memory Model**
42. **JVM Tuning for Distributed Systems**
43. **Distributed Data Processing**
Apache Spark, Apache Flink.
44. **API Schema & Contract Evolution**
OpenAPI, backward compatibility strategies.

## Formulation

> 

### Domain Problem

> 

### Programming Doctrine

> **aka** Programming Paradigms → Models of Computation.
> 

> See the models  of computation in [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md) and Paradigms Here [ Programming Paradigm](note.html?n=technica/computation/language-system/conceptual-model-language-system/programming-paradigm.md).
> 

> **Programming Paradigm:** A programming paradigm is a fundamental style or approach to programming that shapes how problems are conceptualized and how solutions are expressed. It defines the structure, patterns, and techniques used in writing and organizing code.
> 

> **Programming Paradigm =   Style and Mechanisms to Write Programs in a Given Model of Computation.**
> 

### Design

> The process of defining **what a program should do** and **how it should do it**.
> 

> **Program design** is the disciplined, formal process of constructing the internal structure and behavior of a software artifact such that it satisfies a given specification, under resource constraints, by selecting and organizing computational abstractions (e.g., data types, control structures, and interfaces) into coherent, composable units (e.g., functions, classes, modules) that collectively realize a correct, maintainable, and efficient program.
> 

> **Level of Abstraction:**  Design decisions depend on the **level of abstraction**, ranging from low-level (hardware-near) to high-level (conceptual or domain-specific).
> 

### Programming Problem

> **Programming Problem:** Not a domain problem, nor an algorithm, but rather **how to describe a given computation for a specific substrate.**
> 

### Program

> A **program** is a finite, well-defined sequence of instructions that a computer can execute to perform specific tasks. It can also be viewed as a **formal specification or theory of a computation**.
> 

| **Aspect** | **Description** |
| --- | --- |
| **Definition** | A finite sequence of instructions a computer can execute; also a specification or theory of computation. |
| **Inputs and Outputs** | Processes input data and produces outputs, which can be displayed, stored, or sent to other systems. |
| **State** | Maintains internal state that evolves during execution; can be implicit (variables) or explicit (state machines). |
| **Behavior** | Describes how inputs are transformed into outputs, including control flow, data flow, and side effects. |
| **Environment** | Executes within hardware and software context (OS, libraries, networks, peripherals). |
| **Correctness and Specification** | Degree to which program conforms to its specification; can be formally or informally defined. |
| **Complexity** | Time complexity (execution duration) and space complexity (memory usage). |
| **Modularity and Composition** | Composed of reusable functions, classes, or components; supports reuse and combination. |
| **Executability** | Can be executed directly by hardware (compiled) or via interpreter/virtual machine. |
| **Maintainability and Evolution** | Can be modified, extended, or optimized over time. |
| **Representation** | Exists in multiple forms: source code, intermediate code, machine code, or formal models. |

### Computation

> The process of **executing instructions** to transform inputs into outputs.
> 

### Computational Entity

> 

### Language Construct

> See more in [Building Block](note.html?n=technica/computation/system/programming/conceptual-model-programming/building-block.md).
> 

> Building blocks provided by a programming language, such as **variables, functions, classes, types**, and **control structures**.
> 

- Algorithm (Library)
- Type

### Physical **Substrate**

> The Computing **Physical Substrate** refers to the **material foundation** that enables the representation, transformation, and transmission of information in a computing system.
> 

> It consists of the **actual physical entities**—matter, energy, and their dynamic interactions—that instantiate the abstract structures and operations of computation.
> 

> The **physical substrate** defines the **laws**, **constraints**, and **capacities** under which computation occurs. These include limits of energy, speed, precision, noise, and reliability. Every higher-level computational abstraction ultimately reduces to patterns of **state transitions** in this substrate.
> 

### Computer or (C**omputing Substrate**)

> A computer—or more generally, a **computing substrate**—is any physical system capable of performing computation through the manipulation of information-bearing states according to well-defined rules.
> 

> In short, a **computer** is an *instance* of a **computing substrate** designed to execute symbolic or algorithmic transformations, while the **substrate** itself defines the *material and dynamical preconditions* that make computation possible.
> 

> The **substrate** provides the **material basis** and **dynamical laws** from which the abstract process of computation emerges.
> 

> **Actuator:** …
> 

In classical contexts, this refers to **electronic digital systems** (e.g., CPUs, GPUs, microcontrollers) that implement symbolic operations on discrete states. However, the notion extends to **any physical medium** that can reliably support information processing, including:

- **Analog substrates** (e.g., electronic circuits, mechanical or hydraulic systems)
- **Quantum substrates** (e.g., qubits, quantum gates, measurement systems)
- **Biological substrates** (e.g., neural tissue, DNA computing, cellular automata in biological media)
- **Optical and photonic substrates** (e.g., light-based logic or communication systems)
    
    

A **computing substrate** can be characterized by:

| **Dimension** | **Description** |
| --- | --- |
| **Information Carrier** | The physical form that encodes bits, qubits, or continuous values (e.g., voltage levels, photon polarization, molecular states). |
| **State Space** | The set of distinguishable configurations that the substrate can occupy. |
| **Transformation Rules** | The physical dynamics or transition functions that determine how states evolve (e.g., logic gates, quantum operations). |
| **Energy Model** | How computation consumes or dissipates energy; constraints from thermodynamics. |
| **Error Model** | Types and rates of state corruption; tolerance and correction mechanisms. |
| **Scalability** | How computational power scales with physical size, complexity, or parallelism. |

## Principle Set

> Which Principles Should Guide Programming?
> 

> See more in [Programming Principle](note.html?n=technica/computation/system/programming/conceptual-model-programming/programming-principle.md).
> 

## Technique  Space Structure

> Which are the fundamental categories on which every technique falls?
> 

> Note: One technique can spans across many categories.
> 

> Specific **methods, patterns, or practices** used to implement, optimize, or reason about programs.
> 

> A **programming technique** is a method, strategy, or approach used by programmers to design, implement, or optimize code in order to solve a problem efficiently, clearly, and correctly.
> 

> **Note:** The hierarchy represents levels of abstraction, where **5** corresponds to highly abstract, conceptual technique classes, and **1** corresponds to concrete, application-level techniques. This classification is primarily for organizing knowledge and should not be interpreted rigidly.
> 

> Which is the structure of the technique space of  programming?
> 

| **Technique Type** | **Description** | **Hierarchy (Level)** | **Parent (Higher-Level Class)** | **Instance(s)** |
| --- | --- | --- | --- | --- |
| **Organization (Design)** | Techniques for structuring code and systems to improve clarity, maintainability, and reuse before implementation. | 5 (Top-Level) | *None* | Object-oriented design, design patterns (Observer, Factory), modularization, domain-driven design (DDD), test-driven development (TDD). |
| **Organization (Architecture)** | Methods for arranging large-scale components, responsibilities, and system interactions. | 5 (Top-Level) | *None* | Layered architecture, n-tier design, service-oriented architecture (SOA), microservices, dependency injection, inversion of control. |
| **System Interaction** | Techniques that manage the actual communication between distributed components or processes. | 4 (Sub-Level) | Organization | Message queues, RPC, REST/gRPC APIs, shared memory, publish-subscribe, IPC, WebSockets. |
| **Representational** | Techniques for modeling, storing, transforming, and accessing data efficiently. | 5 (Top-Level) | *None* | Data modeling (relational, graph, vector), normalization/denormalization, indexing strategies, caching, serialization, ETL pipelines. |
| **Algorithmic** | Mathematical strategies and methods for solving discrete computational problems. | 5 (Top-Level) | *None* | Divide and conquer, dynamic programming, greedy algorithms, backtracking, graph algorithms (BFS, Dijkstra), sorting/searching. |
| **Control Flow** | Techniques managing execution paths, branching, and decision-making logic in a program. | 5 (Top-Level) | *None* | Structured programming, recursion, event-driven programming, exception handling, state machines. |
| **Concurrency** | Techniques enabling multiple computations to occur simultaneously or asynchronously. | 4 (Sub-Level) | Control Flow | Multi-threading, multi-processing, async/await, actor model, message passing, GPU/SIMD programming, locks, semaphores. |
| **Execution Organization** | Techniques for structuring runtime behavior and the underlying scheduling of computations. | 4 (Sub-Level) | Control Flow | Task queues, event loops, reactive streams, work stealing, fibers, coroutines, continuation-passing style. |
| **Performance** | Techniques focused on improving execution efficiency, reducing latency, or optimizing resource use. | 5 (Top-Level) | *None* | Profiling, loop unrolling, lazy evaluation, memory pooling, vectorization, algorithmic optimization, JIT compilation. |
| **Security** | Techniques ensuring correctness, confidentiality, integrity, and robustness against malicious attacks. | 5 (Top-Level) | *None* | Input validation, sandboxing, privilege separation, cryptography, secure coding practices, access control, SQL injection prevention. |
| **Metaprogramming** | Techniques that allow programs to treat other programs (or themselves) as their data to inspect or modify dynamically. | 5 (Top-Level) | *None* | Reflection, macros, code generation, templates, dynamic typing, aspect-oriented programming (AOP). |
| **Verification** | Techniques to ensure the correctness, reliability, and expected behavior of software pre-deployment. | 5 (Top-Level) | *None* | Unit tests, integration tests, property-based testing, fuzzing, formal verification, static analysis, mutation testing. |
| **Instrumentation** | Techniques to monitor, debug, measure, and observe software behavior at runtime post-deployment. | 5 (Top-Level) | *None* | Logging frameworks, distributed tracing (OpenTelemetry), metrics collection, profiling hooks, health checks. |
| Resiliency & Fault Tolerance | Techniques for ensuring system reliability and availability under failures or unexpected conditions. | 4 (Sub-Level) | Organization (Architecture) | Circuit breakers, retries with exponential backoff, graceful degradation, redundancy/replication, leader election, consensus algorithms (Raft, Paxos). |
| Presentation & UI | Techniques for designing, structuring, and rendering user interfaces and interactions. | 5 (Top-Level) | None | MVC/MVVM, component-based UI frameworks (React, Angular), accessibility patterns, responsive design, rendering optimization |
| Resource Management | Techniques for efficiently allocating, tracking, and releasing computational and system resources. | 5 (Top-Level) | None | Memory management, object pooling, file handles, thread pools, garbage collection tuning, connection pooling |
| Data Processing | Techniques for organizing, transforming, and analyzing large-scale data efficiently. | 4 (Sub-Level) | Representational | Batch processing, stream processing, map-reduce, ETL pipelines, windowing, in-memory computation (Spark, Flink) |

## Constitutive Technical Object(s)

> 

## Evaluation

> 

### Criteria Set

> 

### Trade-offs

> 

## Conceptual Model

Conceptual Model: Programming

## QA

- How to detect over-abstraction?
- What makes a good abstraction?
- Does peer-review improve programs?
- What makes a program hard to debug?
- What is the role of naming in code clarity?
- What is the cost of premature optimization?
- What makes a program hard to understand?
- What is the role of documentation in program comprehension? Can the meaning of a program be derived solely from its code? Similarly, can the meaning of a mathematical model be fully understood only from its symbolic representation?

### What is the relationship between program design and system design?

| Aspect | **System Design** | **Program Design** |
| --- | --- | --- |
| **Level of Abstraction** | High-level (architectural) | Low-level (implementation) |
| **Scope** | Entire system or application comprising multiple components | Single program/module/component |
| **Focus** | Interaction, integration, and coordination of components | Internal structure and behavior of a component |
| **Goal** | Define architecture, interfaces, communication, scalability, reliability | Create correct, maintainable, efficient code within design constraints |
| **Output** | Architectural diagrams, module boundaries, protocols, system topology | Class diagrams, algorithms, data structures, code structure |
| **Concerns** | Scalability, fault tolerance, distributed computing, data flow, deployment | Algorithm design, modularity, encapsulation, coding style |
| **Typical Questions** | How do modules communicate? How is data stored and replicated? How to ensure availability and security? | How to implement this algorithm? Which design pattern fits? How to keep code maintainable? |
| **Methods & Tools** | UML component diagrams, system modeling, API definitions, infrastructure planning | Pseudocode, flowcharts, design patterns, refactoring techniques |
| **Time Horizon** | Long-term system lifecycle, including deployment and operation | Coding, testing, debugging phases during development |

## References

- https://en.wikipedia.org/wiki/Computer_program
- [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md)
- [Algorithm](note.html?n=technica/computation/algorithm.md)
- [Trade-Off](https://app.notion.com/p/Trade-Off-2edd6d82fe1d488ebdff70cab3dc4f7b?pvs=21)
- [Design](note.html?n=technica/computation/system/design.md)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081b3a2e7c6c2f92d2317?pvs=21)
- [‣](https://app.notion.com/p/220598edb79080e9a9b9e10713fc4690?pvs=21)
- https://en.wikipedia.org/wiki/Computer_programming
- https://www.bremontix.xyz/lab/pro/Production/Industry/Software/Production/Program/
- https://www.bremontix.xyz/lab/pro/Production/Industry/Software/Production/Constitutive/
- [Program](note.html?n=technica/computation/language-system/conceptual-model-language-system/program.md)
- https://apenwarr.ca/log/20101213
- https://news.ycombinator.com/item?id=47099401
-