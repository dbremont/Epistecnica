---
tags: [model-of-computation]
---

# Model of Computation

- [Effect System](note.html?n=technica/computation/language-system/conceptual-model-language-system/effect-system.md), [Time](note.html?n=technica/computation/language-system/conceptual-model-language-system/time.md), [Computation  (Computational Process)](note.html?n=technica/computation/language-system/conceptual-model-language-system/computation-computational-process.md)

> In this note we **will explore —** one one the most relevant ideas in **Computer Science —  *Model of Computation —** abstract **computing machine model** or **computation schema**.*
> 

> A **model of computation** (also called a *computation model* or *computational formalism*) is a formal system that defines how computations (processes) are **represented** and **executed**. It specifies:
> 
> - **What a description looks like** — its structural form.
> - **How a computation is represented** — the syntax or state space.
> - **What kinds of computations that representation can generate** — the expressive power of the model.
> - **What the description means** — the semantics it induces, i.e., *what processes it generates*.

> **Note.** From the *ars* (practical) dimension, a Model of Computation can be understood as a **toolbox**, **constructive paradigm**, or **operational language** modelling and describing processes.
> 

> Note: **Different models** expose different regions of the process landscape. A **Turing machine** foregrounds sequential symbolic transformation over discrete tape state; the **Lambda calculus** foregrounds functional abstraction and substitution; **Petri net** foregrounds oncurrency, synchronization, and resource flow; dynamical systems formulations foreground continuous evolution through state space. Thus, selecting a model of computation is not neutral. It is an act of **abstraction design**: choosing the representational machinery through which a class of processes becomes intelligible.
> 

Guide:

- **Note:** *“Computation” and “Program” are like yin and yang—any concept formulated in terms of computation can also be formulated in terms of a program, and vice versa.*
- A *Model of Computation* functions as a **cognitive tool** — a conceptual *middle layer* between **processes** (natural or synthetic) and the **raw, highly elemental machinery** that ultimately executes them. It allows us to reason about how a process can be represented, transformed, and enacted on a machine without being overwhelmed by the machine’s physical details.
- Key Questions:
    - Why do we need several models of computation?
    - (Problem - Process → Model of Computation) In which model of computation is this process most naturally or easily expressed?
    - (Model of Computation → Process) What kinds of processes can be naturally represented in this computational model?
    - Which programming paradigms does this model of computation enable?
    - What is the relation between a Model of Computation and a Model of a Computer?
    - What characterizes a *Model of Computation*? What is the *structure of the space of all models of computation*?

![**Note:** A model of computation formalizes the informal concept of programming paradigms.](https://miro.medium.com/v2/resize:fit:1400/1*wS8DsmEejvsswkQjNA-BoQ.png)

**Note:** A model of computation formalizes the informal concept of programming paradigms.

## Meta

> Evaluation Framework.
> 

> **The understanding of a concept is proportional** to the time invested in deep reflection, deliberate practice, and repeated engagement with its nuances. If a Concept has been learned soft of by osmosis - then is not well understood.
> 

### **✅** Evaluation

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

> See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21) & [](https://app.notion.com/p/250c0f5171ec8010a8d3caa5d0a1266e?pvs=21)
> 

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | ⭐⭐⭐⭐ (Strong). Well-structured, relevant, and insightful, though with minor room for improvement. |
| **Completeness** | Substantially complete covering core concepts, various models, and their relationships. Some areas (like the Taxonomy section) could be expanded for full completeness. |
| **Coherence & Structure** | Excellent logical flow from foundational concepts to complex applications. Hierarchical organization with clear sectioning supports both overview and detailed study. |
| **Epistemic Self-Assessment** | ⭐⭐⭐ (Competent). Adequate understanding; functional in typical contexts; recognizes patterns but may not generalize broadly. |
| **Internalization Self-Assessment** | **⭐⭐⭐ Moderate** – The concept is **understood and occasionally applied**, with **some influence on behavior or reasoning**, but full internalization has not yet occurred. |
| **Should I Reorganize This -in My Content Forest?** |  |
| **What’s my study Strategy? Should I Change It?** | Current strategy of building comprehensive theoretical foundation is effective. Next phase should focus on implementing small projects using different computation models to strengthen practical understanding and identify gaps in theoretical knowledge. |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | A **Model of Computation is a formal lens**. It is a selective abstraction that defines what aspects of a process we choose to represent and how we choose to control its execution, thereby making certain computational patterns natural and others difficult. It
is the bridge between the messy, continuous world of processes and the
discrete, formal world of executable descriptions. |
| **Telos (Intent) 🎯** | **To manage complexity and enable effective praxis.** Its purpose is to provide a cognitive tool for reasoning about
processes without being overwhelmed by implementation details. It offers a vocabulary, a set of structuring principles, and a definition of
correctness. The outcome is the ability to design, analyze, and
implement systems that are correct, efficient, and understandable. |
| **Gnosis (Understanding) 🧠** | The mental representation is a **multi-dimensional space** (as you've begun to chart). To grow it, one must place each new model
(e.g., Prolog's Logic Programming, TensorFlow's Dataflow) within this
space, asking: How does it handle state? Control flow? Time?
Concurrency? The prerequisite structure is a solid grasp of formal
logic, set theory, and the basics of automata theory (FSM, TM). The
representation is fluid if you can easily translate a problem statement
between different models. |
| **Epignosis (Application) 🛠️** | Application is the art of **model selection**. When faced with a problem (e.g., building a reactive UI, a distributed
database, a neural network), the master can identify the dominant
computational patterns and select the model that embodies them (e.g.,
FRP, Actor model, Differentiable programming). Advanced skill involves *composing* models or creating domain-specific models. |
| **Idoneitas (Suitability) 📐** | A model's effectiveness is measured by its **expressive economy** for a given problem domain. Metrics include: code brevity, reasoning
simplicity, runtime performance, scalability, and fault-tolerance
characteristics. The value of the Actor model, for instance, is proven
by the legendary reliability of Erlang systems. |
| **Limites (Limits) ⛔** | Every model is a simplification. The limits of a model are the problems it makes awkward or impossible to express naturally. The Von Neumann model hits the "von Neumann bottleneck." Purely functional programming struggles with stateful I/O. The Turing Machine model abstracts away all concerns of time and physicality. |
| **Critica (Critique) 🔍** | A common critique is the "law of the instrument" - if all you have is a hammer, everything looks like a nail. Over-reliance on a single model (e.g., imperative OOP) can lead to overly complex solutions for problems better suited to other models. The debate between "declarative" and "imperative" styles is a perennial critical thread. |
| **Verbum Usus (Language Use) 🗣️** | The term is used formally in computer science theory, but also loosely in engineering. People often conflate "Model of Computation" with "Programming Paradigm." Your note correctly distinguishes them as the formalization and the style/enabling of that formalization, respectively. The trend is towards using these terms to justify architectural choices, e.g., "We use an event-driven model for scalability.” |

## Computation

> Computation refers to the process of performing a set of well-defined operations or calculations in order to solve a problem or produce a result. Computation can be performed by a computer, a calculator, or even by a human using pen and paper.
> 

> Computation is about state transformation; in a productive or reactive manner. All computation reduces to logic + time.
> 

### **⚙️ Process**

> See more  in [Computation  (Computational Process)](note.html?n=technica/computation/language-system/conceptual-model-language-system/computation-computational-process.md) and [Notion of Change](note.html?n=technica/computation/language-system/conceptual-model-language-system/notion-of-change.md).
> 

> A computation is a directed change process in which successive states are generated according to a formal transformation relation.
> 

> **Note: The underlying concept — or form — of change** is not specified in this definition, although it is fundamental in practice. More concrete notions of change, such as transition semantics, reduction semantics, control transfer, constraint propagation, and related formalisms, provide the operational mechanisms through which computation is modeled, analyzed, and realized.
> 

### **🧠State**

> State refers to a complete and observable configuration of a system at a given point in time, encoding all information necessary to determine its future behavior under defined transition rules. In formal models:
> 
- **State space** $\mathcal{S}$ is the set of all possible configurations.
- Each computation step is a transition $\delta: \mathcal{S} \rightarrow \mathcal{S}$.

State may be partitioned into internal (private, local) and external (shared, global) components, depending on the computational model (e.g., finite state machines, cellular automata, von Neumann machines).

### **🌐 Environment**

> The environment is the external context within which a process or system operates, including all non-deterministic or exogenous inputs, interaction channels, and shared constraints. Formally, it can be defined as an interface  $E: \mathcal{I} \times \mathcal{O} \rightarrow \mathcal{S}_e$, where:
> 
- $\mathcal{I}$: set of inputs the system receives
- $\mathcal{O}$: set of outputs it emits
- $\mathcal{S}_e$: state space of the environment

The environment may be dynamic (evolving independently), adversarial (game-theoretic), or passive (statistical).

### 🔄 Interaction

> Interaction refers to the structured exchange of information between a computational system and its environment (or other systems) during execution, occurring as a sequence of input-output events that influence state transitions. It fundamentally extends the traditional closed-system model of computation (e.g., Turing machine) to **open systems**, where computation is not a one-time function application but an ongoing *dialogue* with an external context.
> 

### **🔋Resources**

> Resources are quantifiable or bounded entities required by a computation to execute, including time, space (memory), energy, bandwidth, and information access rights. In systems modeling, resources are defined by:
> 
- **Type** $T$ (e.g., CPU cycles, RAM, I/O bandwidth)
- **Capacity** $C \in \mathbb{R}^+$
- **Allocation function** $CA: P \rightarrow T \rightarrow C$

Resource constraints shape the complexity, feasibility, and optimality of computations (as in time complexity, space complexity, real-time deadlines, etc.).

### 🪢Computational Elment

> A **computational entity** is a higher-order conceptual unit that captures the fundamental components that make up a program or computational system.
> 

> **Note:** Other alternative terms that capture what is intended by *Abstraction* include *Computational Element*, *Computational Entity*, *Conceptual Unit*, and related formulations.
> 

> Note: Both source code - and the vivid representation.
> 

> See more in [Program Element](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-element.md).
> 

It encompasses both:

- **Representational elements** — structures that encode state, data, or descriptions.
- **Execution-oriented elements** — mechanisms that transform, manipulate, or evolve those representations over time.

### 🧾Representation

> **Note:** *Representation* can refer both to the **state** and to the **description of the ongoing computation**. In this context, whenever we mention *representation* by itself, we refer **only to the state**.
> 

### ⏱️ Time

> See more in [Time](note.html?n=technica/computation/miscelanea/time.md) & [Time](note.html?n=technica/computation/language-system/conceptual-model-language-system/time.md).
> 

> What is the role of time in computation?
> 

### ⚡ Effect

> The notion of an **effect** in computation is an extremely abstract yet useful one — that denotes **what a computation does beyond producing a value**,  such state change, performing I/O, throwing exceptions,  non-determinism, or control flow (which is the current step, execution pointer, etc)
> 

> Effects capture the  observable side-actions of a program, distinguishing pure computations  (which only return results) from impure ones (which also have an impact  on the world or execution context).
> 

> See more in [Side Effect](note.html?n=technica/computation/language-system/conceptual-model-language-system/effect-system.md).
> 

### 🌍 **Non-Local State Based Computation**

> **Non-Local State Computation** refers to performing computations where required data, intermediate state, or computational agents are **not co-located** but distributed across spatial, temporal, or logical boundaries. It generalizes the traditional assumption that all data is locally accessible in unit time, and instead treats data movement and communication as fundamental computational costs.
> 

> **Which systems can be build to compute** over non local or distributed data?  **How much data** does certain algorithm needs to compute?
> 

## 📘 Description

> A description a space of computations (computation path).
> 

> A description  of a space of computation - where each computation in each space unfolds with time overlap.
> 

> A **program (description)** is a set of interconnected **computational elements** that **animate a computational process**.
> 

> See more in [Program](note.html?n=technica/computation/language-system/conceptual-model-language-system/program.md).
> 

## Unit of Computation

> A **Unit of Computation** is the minimal, semantically meaningful entity of execution or evaluation in a computational system, encompassing structures such as instructions, functions, processes, or tasks, and serving as a foundational building block for specifying, scheduling, and performing computational work.
> 

> **Execution Units**: Core Structures Underlying All **Computational System**.
> 

> Workload: A **Workload** is the total amount of work or processing tasks that are assigned to a system or component over a specific period. It can refer to the volume, complexity, and variety of operations that a system must handle, including tasks, transactions, and other computational activities
> 

![Untitled](../assets/note/technica/computation/language-system/conceptual-model-language-system/model-of-computation/untitled.png)

### 🔍 Characterization

> Characterization of  Execution Units.
> 

> Note: This is basically the same as [Space Structure](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md) but more compress.
> 

| **Aspect** | **Description** |
| --- | --- |
| **Granularity** | Can range from low-level (e.g., a machine instruction) to high-level (e.g., a distributed task). |
| **Independence** | Execution units operate independently, often executing concurrently without relying on a single thread's order. |
| **Concurrency** | Multiple tasks or parts of tasks can be managed and executed simultaneously. |
| **Parallelism** | Multiple tasks are executed at the same time using hardware or distributed systems for increased throughput. |
| **Allocation** | Requires CPU time, memory, I/O; effective resource management ensures fairness and efficiency. |
| **Scheduling** | OS or environment determines when and how long a unit runs, optimizing system goals like throughput and responsiveness. |
| **Communication** | Execution units may exchange data or signals during operation. |
| **Coordination** | Synchronization is often required to manage shared resources and ordering of operations. |
| **Isolation** | Prevents unintended interference; processes have separate memory, threads share within a process. |
| **Context Switching** | Saves and loads execution state to switch between units, enabling multitasking but introducing overhead. |
| **Scheduling Model** | Can be cooperative (yield-based) or preemptive (system-enforced switching). |
| **Scalability** | Units like threads scale well on multicore systems to improve workload performance. |
| **State** | Each unit maintains context (registers, stack, program counter) defining its execution state. |
| **Sincronizity** | Execution may be synchronous (blocking, ordered) or asynchronous (non-blocking, decoupled in time). |
| **Temporality** | Defines how execution relates to time—can be periodic, real-time, event-driven, or time-sliced. |
| **Adaptability** | Ability of the unit to respond to environmental changes—load, faults, resource availability. |
| Persistence (Memory) | Whether execution state survives system shutdown or crash (e.g., persistent actors, workflows). |
| Fault Tolerance | Capacity to recover or continue after errors or failures in the unit or related infrastructure. |
| Energy Profile | Energy consumption patterns relevant in embedded, mobile, or green computing contexts. |
| Instrumentation | How observable or traceable the unit is—logging, metrics, probes, and performance counters. |
| Lifecycle | Phases: creation, initialization, execution, suspension, resumption, termination, cleanup. |
| Security Domain | Defines trust boundaries, capabilities, and access control for execution unit. |

### **🧮** Taxonomy

> 

| **Category** | **Unit of Computation** | **Scope** | **Characteristics** | **Examples** |
| --- | --- | --- | --- | --- |
| **Atomic Execution** | Instruction | CPU Cycle | Smallest unit executed by a processor (e.g., `ADD`, `MOV`). | Assembly instructions |
|  | Operation | Micro-operations | Lower-level CPU operations performed within an instruction. | ALU operations, microcode |
| **Basic Computation** | Function / Procedure | Encapsulated Code Block | Self-contained execution, may have inputs and outputs. | C function, Python method |
|  | Thread | OS / User-space Thread | Lightweight execution unit within a process. | POSIX thread, std::thread |
|  | Process | OS Process | Independent execution with its own memory space. | Linux process, Windows process |
|  | Actor |  | A unit of computation that encapsulates state and behavior, communicating with other actors via asynchronous messages. |  |
| **Transactional** | Transaction | Database / ACID Compliance | Atomic sequence of operations that maintains consistency. | SQL transaction, bank transfer |
|  | Event | Event-Driven System | Discrete unit of processing triggered by an event. | Click event, sensor data |
| **Coordination** | Workflow | Multi-step Execution | Sequence of tasks with dependencies, often spanning multiple systems. | BPMN workflow, CI/CD pipeline |
|  | Task | Parallel Processing | Unit of work within a larger workflow or job. | Thread pool task, MPI task |
|  | Pipeline |  | A sequence of stages where each stage processes data and passes it to the next stage. |  |
|  | Batch |  | A collection of tasks or jobs grouped together for execution as a single unit. |  |
| **Distributed** | Job | Cluster / Grid Computing | A collection of tasks in a distributed system. | Hadoop job, SLURM job |
|  | Session | Stateful Interaction | Continuous interaction between a client and a system. | HTTP session, SSH session |
| **Higher-Level** | Process Group | Distributed Systems | Collection of processes working together. | MPI process group |
|  | Service | Microservices | Self-contained, network-accessible computation. | REST API, gRPC service |
|  | Application | Software System | Large-scale software performing computational tasks. | Web app, ML model deployment |

### **🔗 Interaction & Communication**

> In computational systems, **Interaction & Communication** among units of computation—such as processes, threads, tasks, or distributed nodes—refers to the set of mechanisms, protocols, and patterns enabling these discrete entities to exchange data, synchronize execution, and coordinate behavior, while preserving system correctness and performance.
> 

> See more in [Telecom](note.html?n=technica/computation/telecom.md) and [Distributed Computing](note.html?n=technica/computation/distributed-computing.md).
> 

Formally, it involves:

- **Inter-Unit Data Transfer:** The movement of information across computational boundaries via IPC (Inter-Process Communication) mechanisms such as shared memory segments, message queues, pipes, signals, sockets, or remote procedure calls (RPC), ensuring data integrity and coherence across isolated address spaces or nodes.
- **Synchronization Primitives:** Execution units coordinate their operations through low-level primitives (e.g., mutexes, spinlocks, barriers, condition variables) to enforce mutual exclusion and ordering constraints, preventing race conditions and maintaining consistency on shared resources or communication buffers.
- **Temporal Coordination:** Units use signaling, events, or interrupts to asynchronously notify peers about state changes or resource availability, enabling decoupled control flows and reducing idle waiting.
- **Communication Models:** Defines interaction modalities between units, such as synchronous blocking calls (e.g., RPC), asynchronous messaging (e.g., event queues), or publish-subscribe systems, each with trade-offs in latency, throughput, and complexity.
- **Protocol Semantics:** Units adhere to structured communication protocols specifying message format, sequencing, acknowledgment, error handling, and retransmission to achieve reliable and ordered data exchange, critical in distributed or heterogeneous environments.
- **Resource and Performance Constraints:** Communication between units must be optimized considering overhead from context switches, memory copies, network latency, and bandwidth limitations to minimize performance degradation and maximize concurrency.

## 📈 Scalability

> See more in [Design](note.html?n=technica/computation/system/design.md).
> 

> **Note:** Scalability cannot be reduced to the performance of individual computational units; it also depends on the system's ability to isolate these units from one another—minimizing contention, interference, and coordination overhead—provided sufficient resources are available.
> 

> **Note:** A system is *infinitely scalable* if its workload can be perfectly partitioned across a set of **isolated units of computation**, and **unbounded computational resources** are available. This represents a theoretical ideal, assuming **zero coordination, communication, and contention overhead**.
> 

**Scalability** refers to the capacity of computational units to maintain or improve their performance and efficiency as system resources or workload size increase. In the context of units of computation, scalability is characterized by:

- **Vertical Scalability (Scale-Up):** The ability of a unit to leverage increased resources within a single node, such as more CPU cores, memory bandwidth, or cache sizes, to improve throughput or reduce latency. For example, multithreaded tasks exploiting multicore processors.
- **Horizontal Scalability (Scale-Out):** The capacity for execution units to be replicated or distributed across multiple nodes or machines, enabling workload partitioning and parallel execution with minimal performance degradation or overhead due to communication and synchronization.
- **Load Balancing:** Efficient distribution of work across multiple units to prevent bottlenecks or resource underutilization, often requiring dynamic task scheduling, work stealing, or adaptive partitioning.
- **Concurrency and Parallelism Efficiency:** The degree to which additional units contribute to linear or near-linear performance gains, measured by speedup and efficiency metrics, factoring in synchronization overhead, contention, and communication latency.
- **Resource Contention and Overhead:** Scalability is limited by shared resource contention (e.g., locks, memory bandwidth) and system overhead (context switches, communication costs), which may cause diminishing returns or bottlenecks as unit count grows.
- **Fault Isolation and Recovery:** Scalable units support failure containment and recovery without cascading effects, ensuring that increased scale does not compromise system robustness.
- **Elasticity:** The ability to dynamically instantiate or terminate units in response to workload changes, optimizing resource usage and cost.
- **Scalability Boundaries:** Defined by Amdahl’s Law or Gustafson’s Law, which describe theoretical limits on speedup based on the portion of the workload that can be parallelized or scaled.

### Performace

The performance $P$ is a function:

$P = f(R, W)$

where:

- $R = (r_1, r_2, ..., r_m)$, with $r_i$ representing the ith resource parameter (e.g., CPU cycles/sec, memory bandwidth)
- $W = (w_1, w_2, ..., w_n)$, with $w_j$ describing workload parameters (e.g., task size, parallel fraction, communication demand)
- $P$: Performance metric of the unit of computation (e.g., throughput, latency, execution time, speedup)

### 🔁 System Scalability

> System scalability refers to the ability of a computational system to sustain or improve performance as the **workload** or number of **computational units** increases, without prohibitive degradation due to systemic constraints.
> 

| **Dimension** | **Description** |
| --- | --- |
| **Structural Scalability** | The architecture’s capacity to accommodate more execution units (e.g., threads, processes, nodes) without requiring fundamental redesign. |
| **Performance Scalability** | The extent to which increased computational resources yield proportional performance gains (e.g., linear or sublinear speedup). |
| **Resource Scalability** | Ability of the system to efficiently allocate and manage increased hardware/software resources such as memory, CPU time, network bandwidth. |
| **Coordination Overhead** | As execution units increase, coordination costs (locking, synchronization, scheduling) often grow nonlinearly, impacting scalability. |
| **Communication Overhead** | In distributed or shared-memory systems, the cost of inter-unit communication may dominate and limit scalability beyond a certain threshold. |
| **Isolation Capacity** | The system’s ability to isolate units of computation from one another (e.g., through process separation, cache partitioning) directly affects scalability by minimizing interference. |
| **Scalability Envelope** | The theoretical and practical boundaries within which the system maintains acceptable performance scaling—constrained by hardware, software, and workload properties. |
| 🧠 State Management | The scalability of a system is heavily influenced by how it handles state—whether it is shared, isolated, replicated, or persistent. Shared or global state introduces coordination and contention overhead, while stateless or partitioned-state designs enable higher scalability. |

### 📉 Limitations and Trade-offs

- **Diminishing Returns:** Due to Amdahl’s Law, as non-parallelizable work increases, benefits from adding more units plateau.
- **Contention and Bottlenecks:** Shared resources (e.g., memory buses, I/O channels) can become saturated, limiting effective scaling.
- **Topology Constraints:** In distributed systems, network topology and latency can severely restrict scalability at large node counts.
- **Software Stack Overhead:** Runtime systems, garbage collection, scheduling policies, and locking mechanisms introduce non-negligible overhead that limits scalability.

### Note on State and Scalability

> Let $E$ represent the global/shared state of a system, $U = \{ u_1, u_2, \ldots, u_N \}$ be the set of $N$ units of computation, and $W = \{ w_1, w_2, \ldots, w_M \}$ be the workload composed of MM tasks or operations.
> 

> To what extent can the shared state $E$ be **segregated or partitioned** among $U$ to minimize inter-unit coordination, contention, and maximize parallel efficiency?
> 

## **Elasticity**

> In computing and systems design, **elasticity** refers to the **ability of a system to dynamically adapt its resource usage to changing workload demands**, typically by **scaling up or down** computational resources **automatically or with minimal effort**.
> 

## «Model of Computation**»** Space

> A **model of computation** is a formal system that defines how processes can be represented and executed.
> 

> **Expressiveness**: A computation model is expressive if it can represent a wide range of computations and algorithms. An expressive model can represent many different types of problems, which is important for its practical usefulness.
> 

> **Foundations**: Is there an elegant and concise mathematical description of the model? Is it useful in proving helpful facts about the behavior of the model? Or is the model so complex that its description could be clearer and of more mathematical use?
> 

### Families of Models of Computation

> 🧮 Classical Models:  Classical models of computation—ranging from finite automata to Turing machines and lambda calculus—are formal mathematical abstractions that define computation as state transitions over discrete configurations using deterministic or nondeterministic rules, under assumptions of idealized memory and sequential control, capturing the Church-Turing Thesis in both procedural and functional paradigms.
> 

> ⚛️ Quantum Models: Quantum models of computation generalize classical frameworks by encoding information in quantum states and evolving them via unitary transformations and projective measurements, exploiting superposition, entanglement, and nonlocality to define computation as a reversible, linear-algebraic process governed by the laws of quantum mechanics, and characterized by complexity classes such as BQP that transcend classical limitations.
> 

### Space Structure

> What characterize a model of computation? or What it’s structure of the space?
> 

| **Category** | **Instance** | **Description** |
| --- | --- | --- |
| **State Handling (History Sensitivity)** | *Discrete State* | Fixed or unbounded state transitions. |
|  | *Continuous State* | Smooth, real-valued state evolution. |
|  | *Probabilistic State* | Probabilistic transitions or superpositions of states. |
|  | *Stateless* | No state retention between computations. |
|  | History-Sensitive | Computation depends explicitly on past inputs or previous states (memory of the past matters). |
|  | History-Insensitive | Computation depends only on current input regardless of prior history (memoryless semantics). |
| **Notion of Change** | *Imperative (State Tarnsition Semantics)* | Sequential execution of commands. |
|  | *Functional  (Reduction Semantics)* | Evaluation of mathematical functions without state changes. |
|  | *Declarative (Reduction Semantics)* | Execution driven by rules or constraints rather than explicit control flow. |
| **Concurrency** | *Sequential* | Single-threaded execution, no parallelism. |
|  | *Parallel* | Synchronized execution across multiple processors. |
|  | *Distributed* | Decentralized execution with asynchronous actors or processes. |
| **Abstraction Level** | *Hardware-Level* | Direct manipulation of physical or logical gates. |
|  | *Mid-Level* | Machine-friendly but relatively human-readable. |
|  | *High-Level* | Human-centric abstractions (objects, streams, etc.). |
| **Memory Model** | *Finite Memory* | Limited, predefined memory usage without dynamic allocation. |
|  | *Unbounded Memory* | Theoretical or potential infinite memory. |
|  | *Shared vs. Isolated Memory* | Mechanisms for managing memory access across concurrent processes. |
|  | Isolated Memory | Each process or agent operates over independent memory regions. |
|  | External Memory | Computation operates over bounded internal memory while external persistent storage holds larger datasets; computation is decomposed into staged, partitioned, I/O-efficient subcomputations. |
|  | Streaming Memory | Computation over continuously arriving or sequentially accessed data where memory is highly constrained and often only **summary state can be retaine**d. |
|  | Persistent Memory | State survives process execution and remains durable across sessions. |
| **Determinism** | *Deterministic* | Predictable, reproducible execution. |
|  | *InDeterministic* | Multiple possible outcomes, non-fixed execution paths. |
| **Reactivity** | Reactive | Continuously or repeatedly responds to environmental inputs or state changes. |
|  | Interactive | Responds to external user or system input with a two-way engagement loop. |
|  | Passive | Runs independently; not influenced by runtime inputs once started. |
|  | Proactive | Initiates actions based on internal logic or predictive models rather than input. |
| **Synchronicity** | Synchronous | Execution or communication happens in lockstep or with strict timing/ordering constraints. |
|  | Asynchronous | Execution or communication is decoupled in time; processes proceed independently or via deferred coordination. |
|  | Fire-and-Forget | Sends a task/message without waiting for or expecting a response. |
|  |  |  |
| Data Representation | … | … |

### Space

> **Note:** This space focuses on *practical models of computation*—the models that directly support and guide programming practice.
> 

> **Note:** The category of **Reactive Models** refers to a **multi-agent (multi-instruction stream)** environment in which events are asynchronously received from a source and processed in response. The mechanism governing this response determines the specific model of reactivity.
> 

> Computational paradigms largely fall into two broad categories: **Reactive and Proactive**. **Reactive models** are event-driven and respond to external stimuli, emphasizing adaptability and responsiveness. **Proactive models**, by contrast, execute predefined computations based on structured logic, prioritizing control and determinism. Many modern systems blend both paradigms to optimize performance and adaptability.
> 

> **Note:** Why “**Trigger-Based Models of Computation”?** Trigger-Based Models of Computation encompass a class of execution models—flow-based, reactive, and event-driven—characterized by the activation of computational units in response to external events, data availability, or internal state transitions.
> 

> See [Notion of Change](note.html?n=technica/computation/language-system/conceptual-model-language-system/notion-of-change.md).
> 

| **Category** | **Model** | **Notion of Change** | **Model Characterization (Representation Mechanism + Execution Model)** | **Which classes of process descriptions are simplified by adopting this Model of Computation? (Suitability) (Idoneidad)** | **Case Study** |
| --- | --- | --- | --- | --- | --- |
| **State-Based Model** | Finite State Machine (FSM) | Discrete state transition | Finite states with transitions triggered by inputs. | Systems with a finite number of states and clear transitions between them, especially those where the current state depends only on the previous state and input. | Traffic light control system, vending machine operation, or communication protocol like TCP handshake. |
|  | Pushdown Automaton (PDA) | state transition + stack transformation | FSM extended with a stack (unbounded memory). | Systems that require memory beyond just the current state, particularly those with nested or recursive structures. | Syntax checking for programming languages, XML/HTML tag validation, or arithmetic expression evaluation. |
|  | Turing Machine (TM) | tape-state transition | FSM with an infinite tape (universal computation). | Any algorithmic process that can be computed. As a universal model, it can theoretically simulate any other computational model. | Any general-purpose computation, such as sorting algorithms, mathematical function computation, or simulating other computational models. |
| **Functional Model** | Lambda Calculus | symbolic reduction/substitution | Computation via functions, variables, and binding (Turing-complete). | Mathematical functions, recursive algorithms, and problems that can be expressed through function composition and application. | Implementation of functional programming languages, symbolic computation, or mathematical proofs. |
|  | SKI Combinator Calculus | combinatory reduction | Minimalistic functional model using `S`, `K`, `I` combinators. | Similar to Lambda Calculus but with an even more minimalistic approach. Good for modeling computation without variables. | Implementation of functional programming language cores, optimization of lambda expressions, or theoretical foundations of computation. |
| **Imperative Model** | Imperative Programming | mutable state transformation | Sequential commands modifying program state. | Sequential operations that modify state, algorithms with clear step-by-step procedures, and problems that naturally involve mutable data structures. | Sorting algorithms like quicksort, file processing operations, or database transaction handling. |
| **OOP Model** | Object-Oriented (OOP) | message-induced object-state evolution | Objects (state + methods) interacting via messages. | Systems composed of interacting entities with their own state and behavior, problems involving complex data structures with associated operations. | Banking system with accounts and transactions, graphical user interfaces with interactive components, or simulation of physical systems. |
| **Logic Model** | Logic Programming | inference/constraint satisfaction | Inference over predicates/rules (e.g., Prolog). | Problems involving logical inference, pattern matching, rule-based systems, and those that can be expressed through declarative relationships. | Expert systems, natural language processing, automated theorem proving, or database query processing. |
| **Concurrent Model** | Actor Model | asynchronous message propagation | Independent actors communicating via asynchronous messages. | Distributed systems, concurrent computations with independent entities, and problems involving asynchronous communication and state encapsulation. | Distributed messaging systems, multiplayer online games, or cloud computing architectures. |
|  | Petri Nets | token flow and transition firing | Distributed systems modeled with places and transitions. | Systems with concurrent, parallel, or distributed activities, especially those involving synchronization, resource sharing, and conflict resolution. | Manufacturing workflow systems, communication protocols, or traffic management systems. |
|  | π-Calculus | communication and channel reconfiguration | Algebra for concurrent processes with dynamic communication channels. | Mobile concurrent systems, dynamic communication topologies, and problems involving the creation and destruction of communication channels. | Mobile ad-hoc networks, dynamic web services, or biological process modeling. |
|  | Thread | synchronized shared-state transition | Sequential execution with shared memory and synchronization primitives. | Concurrent execution within a single process, parallel algorithms, and problems that can benefit from shared memory concurrency. | GUI applications with background processing, parallel numerical computations, or server handling multiple clients. |
| **Trigger-Based Models of Computation** | Reactive Functional Programming (FRP) | propagation of time-varying values | Events/data represented as time-varying streams. | Systems that respond to continuous or discrete inputs over time, interactive applications, and problems involving time-varying values. | Real-time animation systems, interactive user interfaces, or robotics control systems. |
|  | Dataflow Models | dependency-triggered data propagation | Nodes execute upon receiving input data/events. | Problems that can be expressed as data transformations, parallel computations with clear data dependencies, and streaming data processing. | Signal processing systems, big data processing pipelines, or scientific computing workflows. |
|  | Event-Driven FSM (EFSM) | event-triggered state transition | FSM extended with event queues and context variables. | Complex stateful systems with event handling, context-dependent behavior, and problems requiring both state management and event processing. | Network protocol implementations, embedded control systems, or user interface state management. |
|  | Imperative Event Driven Model | event-triggered imperative mutation | Sequential execution triggered by events with mutable state. | Systems where actions are triggered by events, interactive applications, and problems requiring non-linear execution flow based on external stimuli. | Graphical user interfaces, web servers handling requests, or video game logic. |
|  | Propagator Model | monotonic information propagation | Computation via propagation of information through networks of cells. | Problems involving constraint satisfaction, distributed knowledge, and systems where information needs to be propagated through a network. | Constraint satisfaction problems, distributed sensor networks, or spreadsheets with dependent cells. |
|  | Reactive Model of Computation | reactive propagation of changes | Focuses on propagating changes and handling events in a data-driven manner, often used in user interfaces and event-driven systems. | Systems that respond to external stimuli, user interfaces, and problems requiring immediate reaction to changes. | Real-time control systems, interactive web applications, or IoT device management. |
|  | Event-Driven | asynchronous event-triggered execution | Computation is driven by the occurrence of events, where actions are triggered in response to events. | Systems with asynchronous behavior, non-deterministic input sequences, and problems where execution is determined by external events. | Node.js web servers, GUI frameworks, or event-driven microservices. |
|  | Timely Data Flow | temporally coordinated data propagation | A dataflow model designed for distributed data processing, emphasizing the flow of data across distributed nodes in a timely manner. | Distributed data processing with time constraints, real-time analytics, and problems requiring coordination across distributed nodes. | Real-time financial data analysis, distributed sensor data processing, or stream processing systems. |
|  | Kahn Process Networks | stream propagation through processes | A model for concurrent computation where processes communicate through unbounded FIFO channels. | Dataflow processing with unbounded communication, concurrent signal processing, and problems involving pipelined computation. | Multimedia processing systems, signal processing applications, or parallel data transformation pipelines. |
|  | Synchronous Data Flow | clocked deterministic data propagation | A dataflow model that follows a fixed schedule, ensuring predictable execution of tasks in real-time systems. | Real-time systems with predictable timing, periodic processing tasks, and problems requiring deterministic execution schedules. | Digital signal processing, embedded control systems, or real-time audio/video processing. |
| **Spatial Models** | Cellular Automata | local-rule spatial state evolution | Grid of cells evolving via local interaction rules. | Systems with spatial organization, local interaction rules, and problems involving emergent behavior from simple rules. | Traffic flow simulation, forest fire propagation, or crystal growth modeling. |
| **Quantum Models** | Quantum Computing Models | unitary state evolution + measurement collapse | Computation using qubits and quantum gates. | Problems involving quantum mechanical phenomena, exponential parallelism, and those that can benefit from quantum superposition and entanglement. | Quantum cryptography, Shor's algorithm for factorization, or quantum simulation of molecular structures. |
| **Differentiable Model** | Neural Networks | weighted activation propagation | Networks of interconnected neurons for learning. | Pattern recognition, function approximation, and problems involving learning from data without explicit programming. | Image recognition, natural language processing, or financial market prediction. |
| **Biological Models** | DNA Computing | biochemical reaction transformation | Information processing using biochemical reactions. | Massive parallelism, problems with high combinatorial complexity, and those that can be mapped to biochemical operations. | Solving the Hamiltonian path problem, molecular pattern recognition, or complex combinatorial optimization. |
|  | Neuromorphic | spike/event propagation | Hardware/software systems inspired by neural architectures; spiking neurons, event-driven, parallel and asynchronous processing. | Systems mimicking neural processing, problems requiring low-power computation, and those benefiting from event-driven, parallel processing. | Brain-inspired computing, sensory processing systems, or adaptive robotics. |
| **Symbolic Models** | Rewriting Systems | symbolic rewrite transformation | Computation via transformation of symbolic expressions. | Symbolic transformation, pattern matching, and problems involving rule-based manipulation of expressions. | Algebraic simplification, term rewriting in programming languages, or automated theorem proving. |
| **Optimization Models** | Simulated Annealing | probabilistic energy-state transition | Probabilistic optimization inspired by metallurgy. | Combinatorial optimization problems, search spaces with many local optima, and problems where finding the global optimum is difficult. | Traveling salesman problem, circuit design optimization, or protein folding prediction. |
|  | Genetic Algorithms (GA) | evolutionary population transformation | Optimization via selection, mutation, and crossover. | Optimization in complex search spaces, problems with many parameters, and those where the fitness landscape is not well understood. | Engineering design optimization, scheduling problems, or evolutionary art generation. |
|  | Ant Colony Optimization (ACO) | stigmergic pheromone propagation | Pathfinding inspired by ant foraging behavior. | Pathfinding problems, network routing, and optimization problems that can be mapped to graph traversal. | Vehicle routing problems, telecommunication network routing, or project scheduling. |
|  | Artificial Immune Systems (AIS) | adaptive recognition and response evolution | Pattern recognition inspired by immune systems. | Pattern recognition, anomaly detection, and problems requiring adaptation to changing environments. | Network intrusion detection, fault diagnosis, or computer security systems. |
|  | Differential Evolution (DE) | vector-space population perturbation | Population-based optimization using differential vectors. | Continuous optimization problems, parameter tuning, and those requiring robust search in multidimensional spaces. | Engineering design optimization, neural network training, or filter design. |
|  | Neuroevolution | evolutionary neural topology transformation | Neural network training via evolutionary algorithms. | Neural network architecture optimization, problems requiring both learning and evolution, and those where gradient-based learning is difficult. | Evolving neural network controllers for robotics, game playing AI, or adaptive systems. |
| **Synchronicity** | Synchronous Model | globally synchronized transition | Computation based on simultaneous execution and global clock. | Systems requiring precise timing coordination, real-time control, and problems involving synchronous operations. | Hardware description languages, synchronous digital circuits, or real-time control systems. |
| … | External Memory Model of Computation | staged externalized state transformation | Computation assumes bounded internal working memory and large external persistent memory. Global computations are transformed into staged, partitioned, I/O-aware execution plans where subsets of data are incrementally loaded, processed, materialized, and recombined. Execution emphasizes block transfer, buffering, locality optimization, and memory hierarchy orchestration. | Systems where datasets exceed internal memory capacity; large-scale data management; persistent-state systems; database query execution; storage engines; big data analytics; scalable scientific computing; workloads where I/O complexity, partitioning, and staged processing dominate performance. Particularly suitable for computations requiring semantic preservation under partial data visibility. | Relational DBMS query execution (external sort, hash join, buffer pool management), B-tree/LSM-tree storage engines, Hadoop/MapReduce, Spark spill-to-disk, external merge sort, distributed ETL pipelines, large-scale graph analytics, filesystem indexing. |

## Evaluation

> How to evaluate models of computation?
> 

> What kinds of computation are easily described by eager evaluation models?
> 

| **Category** | **Criteria** | **Description** |
| --- | --- | --- |
| **Expressive Power** | Computable Class | What functions/processes the model can define; relation to Turing, super-Turing, or interactive computation. |
|  | Control Abstractions | Available control forms: recursion, continuations, nondeterminism, concurrency primitives. |
|  | Data Abstractions | Native representable data: higher-order functions, infinite structures, streams. |
| **Semantic Structure** | Operational Semantics | Precision of transition rules; determinism vs nondeterminism; step granularity. |
|  | Denotational Semantics | Existence of a compositional mathematical interpretation (domains, categories, coalgebras). |
|  | Equational Theory | Strength, minimality, and elegance of induced algebraic laws. |
| **Computational Resources** | Time/Space Cost Models | Whether the model supports canonical resource metrics. |
|  | Granularity | Clarity of atomic operations; coarse/fine granularity of steps. |
|  | Resource Predictability | Stability of resource usage under semantic or syntactic variation. |
| **Execution Dynamics** | Evaluation Strategy | How reduction order or evaluation policy shapes execution (CBV, CBN, CBNd, etc.). |
|  | Concurrency Semantics | Representation of interleaving, true concurrency, or partial-order execution. |
|  | Interaction Model | Ability to model reactive, online, or open-world computation. |
| **Compositionality & Modularity** | Program Composition | Whether programs compose cleanly (composition operators, monoidal structures). |
|  | State Encapsulation | Treatment of local state, scopes, environments, store semantics. |
|  | Equational Reasoning | Ability to reason modularly without global interference. |
| **Observational Behavior** | Observational Equivalence | How observable behavior is discriminated (traces, bisimulation, contextual equivalence). |
|  | Determinacy | Degree of determinism or nondeterminism in observable outcomes. |
|  | Error/Divergence Semantics | Treatment of partiality, failure, exceptions, divergence. |
| **Implementation Feasibility** | Realizability | How naturally maps to real architectures, interpreters, or VMs. |
|  | Optimization Transparency | How semantics tolerate optimization (e.g., through referential transparency). |
|  | Hardware Correspondence | Faithfulness or abstraction distance to physical machines. |
| **Mathematical Robustness** | Closure Properties | Closure under composition, parallel composition, iteration. |
|  | Fixed-Point Semantics | Existence and uniqueness of fixed points for recursion. |
|  | Algebraic Structure | Presence of monads, algebraic effects, domains, categorical models. |
| **Practical Utility** | Ease of Specification | Intuitiveness for describing and structuring computations. |
|  | Analytical Power | Supports proofs of correctness, safety, resource bounds. |
|  | Interoperability | Ability to integrate with other models or serve as semantic substrate. |

## Programming Paradigm

> **Programming Paradigm:** A programming paradigm is a fundamental style or approach to programming that shapes how problems are conceptualized and how solutions are expressed. It defines the structure, patterns, and techniques used in writing and organizing code.
> 

> **Programming Paradigm =   Style and Mechanisms to Write Programs in a Given Model of Computation.**
> 

> See more in [ Programming Paradigm](note.html?n=technica/computation/language-system/conceptual-model-language-system/programming-paradigm.md).
> 

## Case Studies

> Which models of **computation** are used to describe the processes that ***make* these systems**?
> 

| **System** | **Model(s) of Computation** | **Description** |
| --- | --- | --- |
| **Traditional CPU** | Von Neumann Architecture | Sequential execution with stored-program memory; fetches, decodes, executes instructions. |
| **Distributed Databases** | Actor Model + Transactional Models | Nodes communicate asynchronously (actors); ACID transactions ensure consistency. |
| **Web Browsers** | Event-Driven + Imperative | DOM events trigger callbacks (event-driven); JavaScript executes imperative logic. |
| **Erlang/Elixir** | Actor Model | Lightweight processes (actors) communicate via message-passing; fault-tolerant. |
| **TensorFlow/PyTorch** | Dataflow + Functional | Computation graphs (dataflow); operations are stateless, pure functions. |
| **Blockchain (e.g., Ethereum)** | State Machine Replication + Smart Contracts | Nodes replicate state transitions; contracts execute deterministically. |
| **Kafka/Event Streaming** | Reactive/Dataflow | Events processed as streams; decoupled producers/consumers. |
| **Prolog** | Logic Programming | Backtracking over Horn clauses; unification-driven execution. |
| **Hadoop/MapReduce** | Dataflow + Batch Processing | Parallel processing of partitioned data (map → shuffle → reduce). |
| **Neural Networks** | Connectionist Model | Parallel computation across weighted nodes; gradient descent for learning. |
| **Quantum Computers** | Quantum Circuits | Qubits manipulated via gates; superposition/entanglement enable parallelism. |
| **AWS Lambda** | Event-Driven + Stateless Functions | Functions triggered by events; ephemeral execution environments. |
| **Digital Circuits** | Finite State Machines (FSM) | Hardware logic transitions between states based on inputs. |
| **Kubernetes** | Declarative + Control Theory | Desired state declared; controllers reconcile actual vs. desired state. |
| **Game Engines (e.g., Unity)** | Imperative + Event-Driven | Object-oriented logic (imperative); physics/input handled via events. |

## QA

### To what extent must a Model of Computation incorporate an explicit Model of Execution? In other words, is a computational model complete without specifying its execution semantics (e.g., operational rules, scheduling, or evaluation strategy)?

> 

### How do differences in the execution model and the associated evaluation strategy influence the expressive power of a given Model of Computation?

> 

### What is the difference between a language system and a model of computation?

> A Model of Computation is like the unit -of program → computation contract - and a language system can implement several of those.
> 

## References

- [‣](https://app.notion.com/p/1c0598edb790801a91fee15cf27090c1?pvs=21)
- [‣](https://app.notion.com/p/1c0598edb79080088359cee8038d1ec8?pvs=21)
- [‣](https://app.notion.com/p/1c0598edb79080cfa052c8de8cb04535?pvs=21)
- https://gwern.net/turing-complete
- https://en.wikipedia.org/wiki/Array_programming
- [‣](https://app.notion.com/p/1c0598edb7908060a75ce69793e32a2f?pvs=21)
- [‣](https://app.notion.com/p/1c0598edb79080759e3afdcc1d75f33e?pvs=21)
- [Storing Data in Control Flow](https://research.swtch.com/pcdata)
- https://research.swtch.com/pcdata
- Dietrich, Eric. "Computationalism." Thinking computers and virtual persons. Academic Press, 1994. 109-136.
- Davis, Martin. "What is a computation?." Mathematics Today Twelve Informal Essays. New York, NY: Springer New York, 1978. 241-267.
- Akl, Selim G. "What is computation?." International Journal of Parallel, Emergent and Distributed Systems 29.4 (2014): 337-345.
- Denning, Peter J. "What is computation." Ubiquity (2010): 2-11.
- Backus, J. (1978). Can programming be liberated from the von Neumann style? Communications of the ACM, 21(8), 613–641.
- [‣](https://app.notion.com/p/10e598edb790816bb840d76fb2831140?pvs=21)
- [‣](https://app.notion.com/p/10e598edb790814f9020d6a74a0829c7?pvs=21)
- [‣](https://app.notion.com/p/10e598edb7908162af92c422bb1be3e2?pvs=21)
- [***F*-coalgebra**](https://app.notion.com/p/F-coalgebra-1bfc0f5171ec8002b087f2fafcf96d27?pvs=21)
- [Concurrency](note.html?n=technica/computation/concurrency.md)
- [Formal System](https://app.notion.com/p/Formal-System-41d02881d0544314b0e7ad3e6ada608a?pvs=21)
- [Function](https://en.wikipedia.org/wiki/Function_(computer_programming))

Untitled

- [ ]  [Formal Language](https://app.notion.com/p/Formal-Language-195c0f5171ec8012bf0fd0530a135871?pvs=21).
- [ ]  [Language System](note.html?n=technica/computation/language-system.md)
- [ ]  Programming Paradigms
    - [ ]  https://en.wikipedia.org/wiki/Declarative_programming
    - [ ]  https://en.wikipedia.org/wiki/Programming_paradigm
    - [ ]  https://en.wikipedia.org/wiki/Programming_model
- [ ]  **Trigger-Based Models of Computation**
    - [ ]  [Dataflow](https://en.wikipedia.org/wiki/Dataflow)
    - [ ]  [Data Flow Computational Models](https://www.cs.colostate.edu/cameron/dataflow.html)
    - [ ]  [Event-Driven Architecture Overview](http://elementallinks.com/el-reports/EventDrivenArchitectureOverview_ElementalLinks_Feb2011.pdf)
    - [ ]  [Timely Dataflow](https://timelydataflow.github.io/timely-dataflow/introduction.html)
    - [ ]  [Event-Driven FRP](https://link.springer.com/chapter/10.1007/3-540-45587-6_11)
    - [ ]  [How is reactive programming different than event-driven programming?](https://stackoverflow.com/questions/34495117/how-is-reactive-programming-different-than-event-driven-programming)
    - [ ]  [What is the difference between Dataflow programming and Reactive programming?](https://stackoverflow.com/questions/30685707/what-is-the-difference-between-dataflow-programming-and-reactive-programming)
    - [ ]  [First version of a data flow procedure language](https://link.springer.com/chapter/10.1007/3-540-06859-7_145)
    - [ ]  [Precise Dataflow Analysis of Event-Driven Applications](https://arxiv.org/pdf/1910.12935.pdf)
    - [ ]  [Advances in Dataflow Programming Languages](http://www.cs.ucf.edu/~dcm/Teaching/COT4810-Spring2011/Literature/DataFlowProgrammingLanguages.pdf)
    - [ ]  [Thinking in events: from databases to distributed collaboration software](https://dl.acm.org/doi/10.1145/3465480.3467835)
    - [ ]  [Flow-based vs. Reactive programming paradigms](https://cs.stackexchange.com/questions/45560/flow-based-vs-reactive-programming-paradigms)
    - [ ]  [Flow-based Programming](https://en.wikipedia.org/wiki/Flow-based_programming)
    - [ ]  I. Arvind, and Gostelow, K.P. A new interpreter for data flow schemas and its implications for computer architecture. Tech. Rep.
    - [ ]  Dennis, J.B. First version of a data flow procedure language. Tech. Mere. No. 61, Lab. for Comptr. Sci., M.I.T., Cambridge, Mass., May 1973.
    - [ ]  Kosinski, P. A data flow programming language. Rep. RC 4264, IBM T.J. Watson Research Ctr., Yorktown Heights, N.Y., March 1973. 14.
    - [ ]  Dataflow Variable - Van Roy
    - [ ]  he Dataflow Model: A Practical Approach to BalancingCorrectness, Latency, and Cost in Massive-Scale,Unbounded, Out-of-Order Data Processing
    - [ ]  [A Survey of Parametric Dataflow Models of Computation](https://dl.acm.org/doi/abs/10.1145/2999539)
    - [ ]  Akidau, T., Bradshaw, R., Chambers, C., Chernyak, S., Fernández, R. J., Fernández-Moctezuma, F., Lax, R., Mcveety, S., Mills, D., Perry, F., Schmidt, E., & Whittle Google, S. (2150). *The Dataflow Model: A Practical Approach to Balancing Correctness, Latency, and Cost in Massive-Scale, Unbounded, Out-of-Order Data Processing*.
    - [ ]  Murray, D. G., McSherry, F., Isaacs, R., Isard, M., Barham, P., & Abadi, M. (2013). Naiad: A timely dataflow system. *SOSP 2013 - Proceedings of the 24th ACM Symposium on Operating Systems Principles*, 439–455. https://doi.org/10.1145/2517349.2522738
    - [ ]  [The Essence of Dataflow Programming](https://cs.ioc.ee/~tarmo/papers/essence.pdf)
    - [ ]  [The Essence of Dataflow Programming](https://news.ycombinator.com/item?id=35973151)
    - [ ]  [The Art of the Propagator](https://groups.csail.mit.edu/mac/users/gjs/6.945/readings/art.pdf)
- [ ]  Concurrent Model of Computation
    - [ ]  [Multicomputation: A Fourth Paradigm for Theoretical Science](https://writings.stephenwolfram.com/2021/09/multicomputation-a-fourth-paradigm-for-theoretical-science/)
    - Wooldridge, Michael, and Nicholas R. Jennings. "Intelligent agents: Theory and practice." The knowledge engineering review 10.2 (1995): 115-152.
    - Dorri, Ali, Salil S. Kanhere, and Raja Jurdak. "Multi-agent systems: A survey." Ieee Access 6 (2018): 28573-28593.
    - [Multi-Agent System](https://en.wikipedia.org/wiki/Multi-agent_system)
- [ ]  https://github.com/BartoszMilewski/DaoFP/blob/master/DaoFP.pdf
- [ ]  [‣](https://app.notion.com/p/10e598edb7908183ba99f3b404ea8627?pvs=21)
- [Operational Semantics](https://app.notion.com/p/Operational-Semantics-1d1c0f5171ec801db681e3ebfe8d41f7?pvs=21)