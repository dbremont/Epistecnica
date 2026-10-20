---
tags: [computational-entity, unit-of-computation]
---

# Unit of Computation

- [Effect System](note.html?n=technica/computation/language-system/conceptual-model-language-system/effect-system.md), [Program Element](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-element.md), [Notion of Change](note.html?n=technica/computation/language-system/conceptual-model-language-system/notion-of-change.md)

> Execution Units are the foundational elements upon which concurrency models are constructed, representing the tasks or processes that operate concurrently within the system.
> 

> Execution Units.
> 

> Note: We need to distinguish between entities that are execution contexts (entities that represent the flow of computation) (or process units) (carrier … ), such as threads, green threads, etc., and entities that describe computation (such as instructions, basic blocks, functions, etc.).
> 

> For a **more in-depth analysis** of the idea of computation flow, see. - [Notion of Change](note.html?n=technica/computation/language-system/conceptual-model-language-system/notion-of-change.md).
> 

![Untitled](data/technica/computation/language-system/conceptual-model-language-system/assets/unit-of-computation/untitled.png)

# Characterization

> Characterization of  Execution Units.
> 

| **Aspect** | **Description** |
| --- | --- |
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
| **Scalability** | Units like threads scale well on multi-core systems to improve workload performance. |
| **State** | Each unit maintains context (registers, stack, program counter) defining its execution state. |
| **Granularity** | The size or scope of work per unit; fine-grained units allow more concurrency but may increase overhead, coarse-grained units reduce overhead but limit parallelism. |
| **Composition** | Units can be composed hierarchically or functionally; tasks can spawn sub-tasks, threads can be grouped, actors can supervise children. |
| **Dependencies** | Units may have explicit or implicit dependencies on others, affecting execution order, synchronization needs, and possible deadlocks. |

## Taxonomy

| **Category** | **Unit of Computation** | **Scope** | **Characteristics** | Instance Set |
| --- | --- | --- | --- | --- |
| **Atomic Execution** | Instruction | CPU Cycle | Smallest indivisible operation executed by a CPU. Represents a machine-level command like arithmetic, data movement, or control flow. | Assembly instructions (e.g., `ADD`, `MOV`) |
|  | Operation | Micro-operations | Sub-steps inside a CPU instruction, often executed in pipeline stages or microcode. | ALU add, register read/write, microcode step |
| **Basic Computation** | Function / Procedure | Encapsulated Code Block | A named, reusable block of code that executes sequential instructions, may accept parameters and return results. | C function, Python method, Java method |
|  | Lambda / Closure | Anonymous Code Block | First-class function with lexical environment capture; may be passed around and invoked. | JavaScript lambda, Python closure |
| **Threading and Concurrency** | Thread | OS / User-space Thread | Lightweight execution unit within a process. Has its own call stack and program counter; shares memory. | POSIX thread (pthreads), std::thread (C++) |
|  | Green Thread | User-Space Thread | User-managed threads, scheduled by runtime rather than OS. Lightweight and cooperative. | Go goroutine, Erlang process |
|  | Fiber | Stackful Coroutine | Lightweight, manually scheduled unit with own stack. Can yield and resume execution explicitly. | Windows fibers, Ruby fibers |
|  | Coroutine | Stackless / Stackful Coroutine | Generalized subroutine that can suspend and resume execution at certain points, allowing cooperative multitasking. | Python `async def` coroutine, Lua coroutine |
|  | Generator | Stackless Coroutine | Specialized coroutine that can yield multiple times to produce sequence of values lazily. | Python generators (`yield`), JavaScript generators |
|  | Continuation | First-Class Control Flow | Represents “the rest of the computation,” capturing the control state at any point, allowing non-linear control flow and advanced flow manipulations. | Scheme `call/cc`, delimited continuations |
|  | Async Function / Future | Asynchronous Computation | Unit representing an ongoing or future computation, often scheduled by an event loop or thread pool. | JavaScript `async/await`, Java `CompletableFuture` |
|  | Future/Promise |  |  |  |
| **Transactional** | Transaction | Database / ACID Context | A sequence of operations treated as a single atomic unit to ensure consistency, isolation, and durability. | SQL transaction, banking transfer operation |
|  | Event | Event-Driven System | Discrete trigger or occurrence that causes computation, usually handled asynchronously. | UI click event, sensor reading, message receipt |
| **Coordination** | Workflow | Multi-step Execution | Orchestrates multiple tasks or steps with dependencies, potentially across distributed systems. | BPMN workflows, Jenkins pipeline, CI/CD process |
|  | Task | Parallel / Distributed Work | Basic unit of work or computation within a scheduler or distributed system. May be scheduled independently or grouped. | Thread pool task, MPI task |
|  | Pipeline | Streaming / Sequential Data | Ordered sequence of processing stages where each stage transforms data and passes it downstream. | Unix pipe, Apache Beam pipeline |
|  | Batch | Bulk Processing | Group of jobs or tasks collected and executed as one unit, often for throughput optimization. | Hadoop batch job, nightly ETL batch |
| **Distributed** | Job | Cluster / Grid Computing | A set of coordinated tasks or processes running across nodes in a distributed system to accomplish a larger goal. | Hadoop MapReduce job, SLURM job |
|  | Session | Stateful Interaction | Maintains continuity of interaction between client and server over time, tracking state across requests. | HTTP session, SSH connection |
| **Higher-Level** | Process Group | Distributed System Group | Logical grouping of processes that cooperate, often for communication or fault tolerance. | MPI process group, Kubernetes pod |
|  | Service | Microservices Architecture | Network-accessible computational unit exposing an API, independently deployable and scalable. | REST API service, gRPC microservice |
|  | Application | Software System | Complete software system that performs computation, usually composed of multiple processes or services. | Web application, ML model deployment |
| **Deferred / Lazy** | Thunk | Delayed Computation | Encapsulates computation to be performed later (lazy evaluation). May or may not memoize results. | Functional programming thunks, Haskell lazy eval |

## References

- [Function](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Concurrency](note.html?n=technica/computation/concurrency.md)
- [Notion of Change](note.html?n=technica/computation/language-system/conceptual-model-language-system/notion-of-change.md)