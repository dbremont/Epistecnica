# Concurrency

> In this note, we will explore in depth the concept of concurrency, the technical problems it introduces, and the mechanisms used to mitigate them.
> 

> **Concurrency** is the property of a computational system in which multiple **sequences of operations execute** in overlapping time intervals, potentially interacting through shared resources, and requiring coordination to ensure correctness under nondeterministic interleaving.
> 

> Note: In this note, the term *coordination* refers specifically to the coordination of concurrent execution, not semantic forms of coordination such as task coordination or plan coordination.
> 

Guiding questions:

- Which are the types  computation units  that can be executed concurrently?
- Which are the **coordination mechanisms**? How it is implemented? Which are the underlying enablers? Which are the tradeoffs of different coordination mechanisms? Which built-in **language semantics automatically govern how multiple concurrent computations** share resources, even without explicit programmer intervention?
- …
- What is a concurrency model? Is this concept even useful?
- Which are the other **related ideas**?
- Which pathologies does concurrent execution introduce?

## Formulation

> Execution Environment, Overlap Execution (Unit of Computation) → Computation Behavior Drift, Coordination.
> 

> How to think about **concurrency**? What type of concept is **concurrency**? What does concurrency denotes?  **Concurrency is a feature, condition that** denotes the overlapping execution and progression of multiple computational processes within a system.
> 

> Concurrent execution introduces a deeply fundamental **technical problem**: how to the  preserve the correctness of each computation, as if each were executing in isolation.  How to make sure that execution overlap (which implies substrate interaction overlap) does not cause - **computation behavior drift**?
> 

> Which are the elements in the **execution substrate**? …
> 

> What is the organizing concept - that drives the solution of the  (**computation behavior drift**)? Coordination.
> 

> Which are the types of coordinations? What is goal coordination?   How is a given **coordination evaluated**? What is the conception of correctness that coordination guarantees? Is the idea of **coordination too abstract**?  Should we talk about a very concrete model of coordination - with a very concrete meaning of correctness?
> 

> **Coordinar**: Verbo del latín tardio coordinare (ordenar algo ajustandolo con otra cosa, ajustar uniendo o combinando), que se usa ampliamente en latin medieval.
> 

### Definition Set

> Coordination: **Coordination**  is the systematic regulation of interaction, ordering, visibility,  resource access, and progress among overlapping units of computation to  revent behavior drift and preserve the correctness and progress  properties each computation would exhibit if executed in isolation.
> 

> **Coordination Model**: A coordination model is a formal semantic framework defining how concurrent computations interact, synchronize, observe, communicate, and preserve correctness under overlapping execution.
> 

> **Coordination Mechanism**: A coordination mechanism is a structure that constrains and regulates the interaction of overlapping computations over shared time, state, resources, or communication channels in order to preserve specified correctness and progress properties. A coordination mechanism is a concrete operational structure, protocol, primitive, or runtime facility that enforces, realizes, or approximates the semantics defined by a **coordination model**.
> 

> **Implicit Coordination Mechanism**: An implicit coordination mechanism is a concurrency-regulating semantic embedded within a language, runtime, or **execution substrate** that automatically governs computational interaction without explicit programmer invocation.
> 

> **Concurrency Paradigm**: A concurrency paradigm is a high-level conceptual worldview that determines how concurrent computation is structured, expressed, coordinated, and reasoned about within a computational system.
> 

> **Concurrency Model**: A concurrency model is an operational and semantic specification describing how concurrent computations are represented, executed, scheduled, coordinated, and observed within a computational environment.
> 

> **Concurrency Pathology**: A concurrency pathology is an emergent failure mode arising from overlapping execution, shared-resource interaction, visibility anomalies, ordering violations, or coordination breakdowns among concurrent computations.
> 

> **Unit of Computation**: A unit of computation is an independently progressing execution entity capable of carrying state, performing operations, interacting with other computations, and participating in coordinated execution within a computational system.
> 

## Coordination

> What is it coordination? **Coordination**  is the systematic regulation of interaction, ordering, visibility,  resource access, and progress among overlapping units of computation to  revent behavior drift and preserve the correctness and progress  properties each computation would exhibit if executed in isolation.
> 

> **Concurrency Control Policy**:  Configuration governing concurrent execution. Read Committed, Serializable.
> 

### Type

> Which are the **types of coordination**?
> 

| Coordination Type | Description |
| --- | --- |
| Synchronization Coordination | Coordinates ordering and mutual interaction between concurrent executions |
| Atomic Coordination | Coordinates indivisible state transitions |
| Memory Coordination | Coordinates memory ordering, coherence, and consistency |
| Visibility Coordination | Coordinates observability of state changes |
| Communication Coordination | Coordinates information transfer between concurrent computations |
| Isolation Coordination | Coordinates interference boundaries between computations |
| Transactional Coordination | Coordinates grouped state transitions under consistency constraints |
| Distributed Coordination | Coordinates interaction across networked concurrent nodes |
| Failure Coordination | Coordinates behavior under partial or total execution failure |
| Progress Coordination | Coordinates liveness and forward progress guarantees |
| Temporal Coordination | Coordinates execution relative to time constraints |
| Reactive Coordination | Coordinates execution through asynchronous propagation and dependency triggering |
| Arbitration Coordination | Coordinates contention over shared resources |
| Flow Coordination | Coordinates throughput, backpressure, and transfer pressure between computations |
| Deterministic Coordination | Coordinates execution to constrain nondeterminism |
| Speculative Coordination | Coordinates optimistic execution with rollback/reconciliation |
| Persistence Coordination | Coordinates durable concurrent state transitions |
| Causality Coordination | Coordinates preservation and propagation of causal relationships |

### Locus of Coordination

> The **Locus of Coordination** in a concurrency system  refers to the specific point or mechanism (e.g., locks, message queues,  or shared memory) where concurrent tasks or processes synchronize their  actions, and it also captures whether the coordination mechanism is  centralized, distributed, or decentralized in nature.
> 

> **Critical Region (Section)**:  A **`critical section`** is a segment of code in a concurrent program where shared resources are accessed or modified, requiring mutual exclusion to prevent race conditions and ensure data consistency.
> 

**Centralized Systems**:

- Single point of control or coordination.
- Examples: Single-machine multithreading, centralized schedulers.

**Distributed Systems**:

- Multiple nodes coordinate over a network.
- Examples: Distributed databases, cloud computing systems.

**Decentralized Systems**:

- No single point of control; peers coordinate directly.
- Examples: Blockchain, peer-to-peer networks.

### Problem Space

> Which problems are induced by concurrent execution?
> 

| **Category** | **Challenge** | **Technical Description** | **Implications** |
| --- | --- | --- | --- |
| Correctness | **Race Conditions** | Unintended behavior due to unsynchronized access to shared resources, where outcome depends on timing/interleaving. | Non-determinism, hard-to-reproduce bugs, data corruption. |
|  | **Atomicity Violations** | Compound operations on shared state not executed atomically, breaking invariants. | Silent data corruption or logic errors. |
| Liveness | **Deadlock** | A cyclic dependency between threads/processes waiting on each other indefinitely for resources or conditions. | System hangs, full halt in progress. |
|  | **Livelock** | Active threads continue to change state in response to each other but make no progress. | High CPU usage, zero useful work. |
|  | **Starvation** | A thread/process is perpetually denied access to a needed resource due to scheduling bias. | Long wait times, degraded system fairness. |
| Scheduling/Real-Time | **Priority Inversion** | A lower-priority task holds a resource needed by a higher-priority one, causing the latter to be blocked indefinitely. | Violation of real-time guarantees, system instability. |
| Debugging/Testability | **Non-Determinism** | Same inputs can lead to different outcomes due to variable execution order. | Difficult debugging, need for extensive testing. |
| Debugging | **Heisenbugs** | Bugs that vanish or alter behavior when one attempts to study them (e.g., adding a log changes timing). | Makes traditional debugging tools unreliable. |
| Memory Consistency | **Data Races** | Concurrent access to shared variable without proper synchronization where at least one is a write. | Undefined behavior, often leads to memory corruption or crashes. |
| Portability/Correctness | **Memory Model Ambiguity** | Different architectures (e.g., x86 vs ARM) have different memory consistency models. | Code that works on one system may fail on another. |
| Performance | **False Sharing** | Threads on different cores write to different variables on the same cache line, causing unnecessary cache coherence traffic. | Severe performance degradation. |
| Performance | **Context Switching Overhead** | Switching between threads or processes incurs cost (CPU time, cache invalidation). | Diminished performance in fine-grained concurrency. |
| Performance/Architecture | **Scalability Bottlenecks** | Limited parallelism due to shared resources or coordination overhead (Amdahl’s law). | Poor multicore utilization. |
| Performance/Design | **Granularity Tuning** | Balancing task size: too fine-grained → overhead; too coarse → underutilization. | Suboptimal throughput or latency. |
| Design/Abstraction | **Composability of Concurrent Constructs** | Combining individually correct concurrent modules can result in incorrect global behavior. | Inhibits modularity and reuse. |
| Synchronization/Latency | **Coordination Overhead** | Costs incurred due to locking, signaling, or consensus protocols among threads/processes. | Reduced parallel efficiency. |
| Fault Tolerance | **Fault Propagation** | Errors in one thread/process may cascade or corrupt shared state accessed by others. | Requires robust isolation or supervision models (e.g. actor model). |
| Timing | **Temporal Nondeterminism** | Execution speed and interleaving vary across runs due to scheduling, hardware, or load. | Makes timing-sensitive designs and testing complex. |
| Performance/Fairness | **Resource Contention** | Competing access to CPU, memory, I/O, or locks reduces performance or leads to unfairness. | Performance anomalies, starvation, degraded QoS. |

### Mechanism Structure

> How to decomposed a coordination mechanism?
> 
- **Enforcement Modality or**  Coordination explicitness denotes the degree to which concurrency regulation requires deliberate programmer invocation versus being automatically enforced by embedded language, runtime, or substrate semantics.
- **Category**: General coordination class to which the mechanism belongs.
- **Mechanism**: Specific coordination structure or primitive.
- **Purpose**: Which coordination problem it solves.
- **Description**: Conceptual explanation of the mechanism.
- **Underlying Principle**: Fundamental operational idea enabling the mechanism.
- **Execution Context**: Environment in which it operates (threading, distributed systems, async runtime, kernel, hardware, etc.).
- **Coordination Domain**: Which aspect of interaction it regulates (ordering, visibility, exclusion, communication, lifecycle, causality, etc.).
- **Interaction Model**: How computations interact through the mechanism.
- **Resource Model**: Which resources are regulated.
- **State Model**: Whether coordination occurs over shared state, replicated state, immutable state, message streams, etc.
- **Communication Semantics**: Shared memory, message passing, event propagation, transactional interaction, etc.
- **Visibility Semantics**: How and when state changes become observable.
- **Ordering Semantics**: Which ordering constraints are preserved or imposed.
- **Atomicity Guarantees**: Which operations are indivisible.
- **Consistency Guarantees**: Which correctness guarantees are enforced.
- **Isolation Semantics**: Whether and how interference is constrained.
- **Progress Guarantees**: Deadlock-freedom, lock-freedom, wait-freedom, fairness, etc.
- **Failure Semantics**: How faults affect coordinated computations.
- **Temporal Semantics**: Relationship to time, scheduling, deadlines, or causality.
- **Determinism Properties**: Whether execution behavior is deterministic or nondeterministic.
- **Scope**: Local thread, process, runtime, node, distributed cluster, global system, etc.
- **Granularity**: Fine-grained vs coarse-grained coordination.
- **Scalability Characteristics**: Behavior under increasing concurrency/load.
- **Performance Costs**: Latency, contention, cache coherence traffic, context switching, synchronization overhead.
- **Contention Behavior**: How performance degrades under competition.
- **Implementation Strategy**: Algorithmic or structural implementation technique.
- **How It Is Implemented**: Concrete runtime/hardware/compiler realization.
- **Hardware Dependencies**: Required CPU or architectural guarantees.
- **Language Dependencies**: Required language/runtime semantics.
- **Verification Complexity**: Difficulty of proving correctness.
- **Debugging Complexity**: Difficulty of diagnosing failures/pathologies.
- **Common Pathologies**: Typical failure modes introduced by the mechanism.
- **Limits**: Fundamental or practical limitations.
- **Trade-offs**: What properties are gained vs sacrificed.
- **Usage**: Typical applications and design scenarios.
- **Abstraction Level**: Hardware, runtime, language, middleware, distributed protocol, etc.
- **Composability**: Whether the mechanism composes safely with others.
- **Variation Set: Which are the variants, and specialization of this mechanism?**

### Mechanism Space

> **Synchronization** is to coordinate and control the access to shared resources or data in order to ensure consistency and prevent conflicts in concurrent executions.
> 

> **Blocking Synchronization**: Processes/threads wait for resources or events.
> 

> **Non-Blocking Synchronization**: Processes/threads make progress without waiting.
> 

> Lock-Free Synchronization: : When emphasizing that the synchronization mechanism avoids traditional locks (e.g., mutexes).
> 

> Wait-Free Synchronization:  When emphasizing that all threads make progress without waiting (a stronger guarantee than lock-free).
> 

| Category | Mechanism | Description | How It Is Implemented | Usage | Enforcement Modality | Variation Set |
| --- | --- | --- | --- | --- | --- | --- |
| Execution Coordination | Scheduler | Allocates execution time among concurrent computations | OS scheduler, runtime scheduler, work‑stealing queues | Thread/task progression | Implicit | Work‑stealing, FIFO, Round‑robin, Priority, O(1) scheduler, CFS, Real‑time (FIFO/RR), Gang scheduler, Co‑scheduler |
| Execution Coordination | Event Loop | Centralized execution dispatcher for asynchronous tasks/events | Queue polling + callback/task dispatch | Async runtimes, GUI systems | Implicit | Single‑threaded (JS, Python asyncio), Multi‑threaded (libuv), Epoll/kqueue/IOCP backends, Proactor/Reactor |
| Execution Coordination | Structured Concurrency Scope | Constrains lifetime relationships between spawned computations | Parent‑child task trees + scoped cancellation/joining | Safe async composition | Hybrid | Trio nurseries, Kotlin coroutineScope, Python `TaskGroup`, Java StructuredTaskScope, C++20 `std::jthread` with stop token |
| Synchronization | Mutex | Enforces exclusive access to shared state | Atomic instructions + wait queues/futexes | Critical sections | Explicit | Reentrant, Timed, Robust, Priority Inheritance, Priority Ceiling, Seqlock, Phased Lock, Recursive, Non‑recursive |
| Synchronization | Spinlock | Busy‑wait mutual exclusion primitive | Atomic CAS/TAS loops | Very short critical sections | Explicit | Unfair, Ticket lock, MCS lock, CLH lock, Backoff lock, Peterson’s (2‑thread), Dekker’s, Lamport’s Bakery, Test‑and‑set |
| Synchronization | Read–Write Lock | Allows concurrent readers and exclusive writers | Reader counters + writer exclusion logic | Read‑heavy workloads | Explicit | Upgradable, Pthread rwlock, FIFO reader/writer, Writer‑preference, Reader‑preference |
| Synchronization | Semaphore | Coordinates bounded concurrent access through counters | Atomic decrement/increment + blocking queues | Resource pools | Explicit | Counting, Binary, Timed, Named (system‑wide), Permit‑based (Java Semaphore) |
| Synchronization | Monitor | Encapsulated synchronization combining lock + condition state | Language/runtime‑managed mutex + wait sets | Object synchronization | Hybrid | Mesa monitor (signal‑and‑continue), Hoare monitor (signal‑and‑wait), Java `synchronized`, C# `lock` |
| Synchronization | Barrier | Forces computations to synchronize at a common point | Arrival counters + release synchronization | Parallel phases | Explicit | Reusable (CyclicBarrier), Non‑reusable, Combining barrier, Phaser (dynamic), Barrier with timeout |
| Synchronization | Latch | One‑time synchronization gate | Countdown counter + wait queue | Startup/shutdown coordination | Explicit | CountDownLatch, One‑shot, Binary latch (count=1) |
| Synchronization | Condition Variable | Suspends execution until predicate changes | Wait queues + mutex integration | Producer‑consumer | Explicit | Timed condition variable, Condition with predicate, Spurious wakeup‑aware |
| Synchronization | Futex | Hybrid userspace/kernel synchronization primitive | Atomic userspace fast‑path + kernel wait fallback | High‑performance locks | Hybrid | Robust futex (owner death), PI futex (priority inheritance), Private/shared futex |
| Atomic Coordination | Atomic Variable | Indivisible memory operations | CPU atomic instructions | Shared counters/flags | Explicit | AtomicInteger, AtomicLong, AtomicBoolean, AtomicReference, AtomicFieldUpdater, AtomicArray, AtomicMarkableReference, AtomicStampedReference, AtomicDouble (float) via bit‑cast |
| Atomic Coordination | Compare‑And‑Swap (CAS) | Conditionally updates memory atomically | Hardware CAS instruction | Lock‑free structures | Explicit | Double‑CAS (DCAS), CAS with weak/strong (C++), CAS on pointer (ABA handling via versioning), LL/SC (separate but related) |
| Atomic Coordination | Fetch‑And‑Add | Atomic arithmetic update primitive | Atomic ALU instructions | Counters/work distribution | Explicit | Fetch‑And‑Or, Fetch‑And‑And, Fetch‑And‑Xor, Atomic Min/Max, Atomic Floating‑Point Add (limited) |
| Atomic Coordination | LL/SC | Atomic update pair based on reservation | Hardware reservation tracking | Lock‑free algorithms | Explicit | LDREX/STREX (ARM), lwarx/stwcx (PowerPC), lr/sc (MIPS), SC failure retry semantics |
| Memory Coordination | Memory Model | Visibility/ordering semantics of shared memory | Compiler + CPU ordering constraints | All shared‑memory concurrency | Implicit | SC, TSO, PSO, RMO, Weak/Relaxed, Release Consistency, Lazy Release, Scope Consistency, Causal Consistency, Processor Consistency, C++11 memory model, Java MM |
| Memory Coordination | Memory Barrier/Fence | Prevents illegal memory operation reordering | CPU fence instructions | Synchronization ordering | Explicit | LoadLoad, StoreStore, LoadStore, StoreLoad, Full fence, Acquire/Release, Compiler barrier, C++ `atomic_thread_fence`, `asm volatile` |
| Memory Coordination | Cache Coherence Protocol | Consistency among processor caches | Hardware cache‑state protocols | Multicore memory coherence | Implicit | MESI, MOESI, MESIF, Dragon, Firefly, Synapse, Berkeley, Directory‑based, Snooping, Token Coherence |
| Memory Coordination | Happens‑Before Relation | Causal ordering between operations | Synchronization semantics + memory rules | Correctness reasoning | Implicit | Synchronizes‑with, Dependency‑ordered before, Sequentially consistent HB, Data‑race‑free HB |
| Visibility Coordination | Volatile Variable | Constrained visibility/reordering semantics | Compiler/runtime memory barriers | Shared flags/publication | Explicit | Java volatile (full fence), C++ volatile (no threading), C# volatile, `volatile` reads/writes, `Volatile.Read`/`Write` |
| Visibility Coordination | Safe Publication | Guarantees correct visibility after init | Synchronization + memory ordering | Immutable/shared objects | Hybrid | Final fields (Java), Immutable object publication, Static initializer safety, Double‑checked locking (fixed with volatile), `std::atomic` shared_ptr |
| Communication Coordination | Channel | Structured communication conduit | Queues + synchronization semantics | CSP/message‑passing | Explicit | Synchronous (rendezvous), Buffered, Unbuffered, Broadcast, Priority, Scheduled/Delayed, Dead Letter, Select/Alt over channels, Join pattern |
| Communication Coordination | Mailbox | Asynchronous message reception queue | Runtime‑managed queues | Actor systems | Implicit | Unbounded, Bounded (backpressure), Priority, Mailbox with stash (temporary deferral), Multi‑reader/multi‑writer |
| Communication Coordination | Pipe | Byte‑stream communication abstraction | Kernel‑managed buffers | IPC/stream composition | Explicit | Named pipe (FIFO), Anonymous pipe, Bidirectional pipe, Byte pipe, Message pipe (datagram) |
| Communication Coordination | Queue | Ordered concurrent work/data structure | Locking or lock‑free algorithms | Producer‑consumer | Hybrid | Blocking, Non‑blocking, Linked, Array, Priority, Transfer, Work‑stealing, Draining, Synchronous (zero‑capacity) |
| Communication Coordination | Publish–Subscribe | Event dissemination | Broker/event‑routing systems | Reactive/distributed | Hybrid | Topic‑based, Content‑based, Broker‑based, Brokerless (distributed), Event bus, Persisted pub/sub |
| Communication Coordination | RPC | Remote procedure invocation | Serialization + networking + blocking/futures | Distributed systems | Explicit | Synchronous, Asynchronous (future), One‑way, Streaming (gRPC), Bidirectional, JSON‑RPC, XML‑RPC, Thrift, Avro |
| Isolation Coordination | Process Isolation | Prevents unsafe shared‑memory interaction | Virtual memory/address‑space separation | Fault containment | Implicit | UNIX fork, Sandboxing (seccomp‑bpfs, Capsicum), VM isolation (KVM), Container (namespaces + cgroups), Enclave (SGX), SFI (Wasm, NaCl) |
| Isolation Coordination | Actor Isolation | Encapsulates mutable state per actor | Mailbox/message semantics | Fault‑tolerant concurrency | Implicit | Erlang/OTP actor, Akka (typed/untyped), Orleans grain, Virtual actor, Actor with become/unbecome |
| Isolation Coordination | Ownership System | Restricts aliasing and mutation rights | Type‑system enforcement | Race prevention | Implicit | Linear types, Affine types (Rust), Uniqueness types (Clean), Reference capabilities (Pony), Capabilities (Capsicum) |
| Isolation Coordination | Borrowing System | Temporary delegated access rights | Compiler lifetime analysis | Safe shared access | Implicit | Shared borrow (&T), Mutable borrow (&mut T), Lifetimes (explicit, elision), Temporary borrow, Reborrowing |
| Isolation Coordination | Immutability | Eliminates mutable shared‑state interference | Language/runtime restrictions | Functional/reactive | Implicit | Shallow, Deep (persistent data structures), Freeze/thaw, Immutable views, Read‑only references |
| Transactional Coordination | Transaction | Grouped operations executed atomically | Logging/versioning/conflict detection | Databases/STM | Explicit | ACID, Nested, Distributed (2PC, 3PC, Paxos Commit, Calvin), Saga, TCC, Transactional Messaging (Outbox) |
| Transactional Coordination | STM | Optimistic shared‑memory coordination | Read/write sets + rollback | Concurrent data structures | Hybrid | Lock‑based, Lock‑free, Word‑based, Object‑based, Deferred update, Direct update, Haskell STM, Clojure STM, Multi‑version (MVCC) |
| Transactional Coordination | MVCC | Coordinates reads/writes via versioning | Multi‑version storage + timestamps | Databases | Implicit | Snapshot isolation, Serializable snapshot, Optimistic MVCC, Pessimistic MVCC, Timestamp‑based (OCC, T/O) |
| Transactional Coordination | Optimistic Concurrency Control | Detects conflicts at commit time | Validation phases + rollback | Low contention | Hybrid | Backward validation, Forward validation, Certify locks, Read‑then‑write set, Dynamic validation |
| Transactional Coordination | Pessimistic Locking | Prevents conflicts before execution | Explicit lock acquisition | High contention | Explicit | Table‑level, Row‑level, Page‑level, Gap lock (MySQL), Predicate lock, Intention locks, Range lock |
| Distributed Coordination | Consensus Protocol | Distributed agreement under failures | Quorum algorithms + replication | Distributed DBs | Explicit | Paxos (basic, multi, fast), Raft, Zab, Viewstamped Replication, PBFT, Tendermint, HotStuff, Nakamoto (PoW), PoS (Casper, Ouroboros) |
| Distributed Coordination | Distributed Lock | Exclusivity across nodes | Consensus/lease systems | Cluster coordination | Explicit | Lease‑based, Fencing token, Redis Redlock, ZooKeeper lock, etcd lock, DB advisory lock |
| Distributed Coordination | Logical Clock | Orders events causally | Counter propagation | Event ordering | Implicit | Lamport timestamp, Scalar clock, Matrix clock, Version vector (subset) |
| Distributed Coordination | Vector Clock | Tracks partial causal relationships | Per‑node logical clocks | Distributed causality | Implicit | Version vector, Dotted version vector, Interval tree clock |
| Distributed Coordination | Leader Election | Selects coordinating authority | Voting/consensus protocols | Cluster management | Hybrid | Bully, Ring, Raft election, Paxos leader, ZooKeeper leader (temporary sequential nodes), Kubernetes lease‑based |
| Failure Coordination | Supervisor | Detects and manages computation failures | Monitoring + restart strategies | Actor systems | Implicit | One‑for‑one, One‑for‑all, Rest‑for‑one, All‑for‑one, Supervision tree, Escalation |
| Failure Coordination | Cancellation Token | Cooperative termination | Shared cancellation state | Structured concurrency | Explicit | Polling token, Callback‑based, Thread interruption, Cooperative with timeout, Scoped cancellation |
| Failure Coordination | Retry Mechanism | Transient failure recovery | Backoff/retry policies | Distributed systems | Hybrid | Immediate, Exponential backoff, Linear, Constant, Jitter, Retry with circuit breaker, Retry budget |
| Progress Coordination | Lock‑Free Algorithm | System‑wide progress without blocking | Atomic retry loops | High‑concurrency | Explicit | Lock‑free stack/queue/list/map, CAS‑based, Hazard pointer‑protected, EBR‑based, Double‑word CAS |
| Progress Coordination | Wait‑Free Algorithm | Per‑thread bounded progress | Advanced atomic algorithms | Real‑time | Explicit | Bounded wait‑free, Population‑oblivious, Array‑based non‑commutative, Helping protocols |
| Progress Coordination | Obstruction‑Free Algorithm | Progress in isolation | Optimistic retry semantics | Experimental | Explicit | Optimistic retry, Version‑based, All‑or‑nothing, Interruptible obstruction‑free |
| Temporal Coordination | Timeout | Bounds waiting duration | Timers + scheduler interrupts | Failure detection | Explicit | Absolute, Relative, Hard (fatal), Soft (advisory), Operation, Idle, Connection, Read/write, Retry |
| Temporal Coordination | Deadline Scheduling | Execution relative to temporal constraints | Priority/deadline schedulers | Real‑time | Implicit | EDF, Deadline monotonic, Constant bandwidth server, Sporadic server, Deferrable server, SCHED_DEADLINE, RM, RR with deadlines |
| Temporal Coordination | Rate Limiter | Regulates resource consumption rate | Token bucket, leaky bucket | Throughput control | Explicit | Token bucket, Leaky bucket, Sliding window log, Sliding window counter, Fixed window (GCRA), Concurrency limiter, Distributed (centralized) |
| Reactive Coordination | Future/Promise | Deferred computation dependency | State machines + continuations | Async composition | Hybrid | CompletableFuture, ListenableFuture, Shared future, Settable future, Thenable, Combinators (thenApply, thenCompose) |
| Reactive Coordination | Signal/Event | Reactive propagation | Event dispatch systems | GUIs/reactive | Hybrid | Plain signal, Typed event, Weakly referenced handler, Event aggregator, Event bus with dispatch rules |
| Reactive Coordination | Stream | Asynchronous dataflow | Buffered propagation pipelines | Reactive/dataflow | Hybrid | Cold (per‑subscriber), Hot (shared), Broadcast, Subject, Backpressured (Reactive Streams), Coroutine flow, Async sequence |
| Lang‑Level Implicit | Evaluation Order Semantics | Implicitly constrains operation ordering | Compiler/language spec | Expression semantics | Implicit | Strict (applicative), Non‑strict (normal), Call‑by‑name, Call‑by‑need (lazy), Call‑by‑value, Call‑by‑reference, Call‑by‑sharing, Parallel `par` |
| Lang‑Level Implicit | Garbage Collection | Safe memory reclamation | Reachability + stop‑the‑world/concurrent | Managed runtimes | Implicit | Tracing (mark‑sweep, mark‑compact, copying), Ref‑counting, Generational, Concurrent, Parallel, Incremental, Real‑time, Region‑based, Tri‑color marking |
| Lang‑Level Implicit | Async Suspension Semantics | Resumable execution | State‑machine transformation | Async runtimes | Implicit | `await`/`async` (C#, Python, JS), State‑machine (Rust), Promise‑based (JS), Task (C#), Deferred (Python), Coroutine with yield, Generator |
| Lang‑Level Implicit | Exception Propagation | Failure transfer between computations | Stack unwinding / runtime propagation | Async/task systems | Implicit | Stack unwinding (C++), Exception object (Java), Checked/unchecked, Future aggregation, Structured concurrency propagation, Failure as value (Result), Panic/recover (Go) |
| Hardware Coordination | Interrupts | Async hardware/software interaction | CPU interrupt handling | OS/device | Implicit | HW interrupt, SW exception/trap, MSI, MSI‑X, Virtual IRQ, Coalescing, Nested, NMI, Task‑Priority Register (TPR) |
| Hardware Coordination | DMA Coordination | Device‑memory access | Hardware memory arbitration | High‑speed I/O | Implicit | Single‑transfer, Scatter‑gather, Double‑buffered, Circular buffer, RDMA (InfiniBand, RoCE, iWARP), NVMe DMA, P2P DMA, IOMMU‑protected |
| Hardware Coordination | NUMA Policies | Memory locality across processors | NUMA‑aware allocators/schedulers | Multisocket | Implicit | First‑touch, Round‑robin, Interleaved, Preferred node, Local allocation, Bind‑to‑node, Migrate‑on‑fault, Page replication, MPOL_BIND, MPOL_PREFERRED, MPOL_INTERLEAVE |
| Synchronization | Reentrant Mutex | Lock that can be re‑acquired by the same thread without deadlock | Owner thread ID + recursion counter | Recursive critical sections (e.g., GUI callbacks) | Explicit | Same‑thread reentrant, Non‑reentrant (standard), Reentrant with unlock count |
| Synchronization | Timed Mutex | Mutex with try‑lock timeout | Kernel timer + wait queue | Upper‑bound waiting, deadlock avoidance | Explicit | Relative timeout, Absolute timeout, Try_lock_for, Try_lock_until |
| Synchronization | Ticket Lock | Fair spinlock using two counters (next ticket, now serving) | Atomic fetch‑and‑add on `next`, load on `now` | Fair, low‑contention spin | Explicit | 64‑bit ticket, 32‑bit wrap, Backoff variant |
| Synchronization | MCS Lock | Scalable queue‑based lock (per‑node linked list) | CAS on tail, spinning on local flag | Many cores, reduce cache coherence traffic | Explicit | MCS, K42 lock, NUMA‑aware variant |
| Synchronization | CLH Lock | Queue‑based lock with spinning on predecessor’s flag | CAS on tail, spinning on a local boolean | Similar to MCS but different memory footprint | Explicit | CLH, CLH with padding, Adaptive CLH |
| Synchronization | Backoff Lock | Spinlock with exponential/linear backoff | Delay loop (pause, yield, exponential delay) | High contention, hyper‑threaded systems | Explicit | Exponential backoff, Linear backoff, Random backoff, Adaptive (based on collision count) |
| Synchronization | Peterson’s Algorithm | Software mutual exclusion for two threads | Two flag variables + turn variable | Embedded/education (no atomics needed) | Explicit | Peterson, Filter lock (N‑thread generalisation) |
| Synchronization | Dekker’s Algorithm | Early mutual exclusion for two threads | Flags + turn with explicit race resolution | Historical, education | Explicit | Original Dekker, Variant with stronger memory ordering |
| Synchronization | Lamport’s Bakery | N‑thread mutual exclusion using ticket numbers | Fetch‑and‑increment, array of flags | Proof of possibility, educational | Explicit | Bakery with memory barriers, Bakery with atomic increment |
| Synchronization | Seqlock (Sequence Lock) | Optimistic lock, readers don’t block writers | Sequence counter (even = unlocked, odd = locked) | Low‑contention reads, infrequent writes | Explicit | Plain seqlock, Writer‑preference seqlock, RCU‑based seqlock |
| Synchronization | Phaser | Dynamic barrier with tiering and on‑the‑fly registration | Arrival counters + phase objects | Parallel simulations, iterative algorithms | Explicit | Java Phaser, Phaser with parties, Tiered phaser (tree) |
| Synchronization | Transfer Queue | Hybrid queue, producer may wait for consumer | Atomic pointers + CAS with condition | Data transfer with optional rendezvous | Hybrid | Synchronous (always wait), Partially buffered, TransferQueue (Java) |
| Atomic Coordination | Double CAS (DCAS) | Atomically compare and update two distinct memory locations | Hardware support (very rare) or software emulation (with locks) | Linked data structures (e.g., BST rotations) | Explicit | Word‑pair DCAS, Extended DCAS (n locations) |
| Atomic Coordination | Hardware Transactional Memory (HTM) | Group memory ops as atomic isolated transaction | CPU transactional cache / buffer (Intel TSX, ARM TME) | Lock elision, optimistic concurrency | Hybrid | RTM (Intel), HLE (Intel), TME (ARM), IBM HTM, RISC‑V TME |
| Memory Coordination | Memory Consistency Models (specific) | Formalised ordering rules beyond “Memory Model” | ISA specification + compiler mapping | Formal verification, portability | Implicit | SC, TSO, PSO, RMO, Weak, Release Consistency, LRC, Scope, Causal, Processor |
| Memory Coordination | Cache Flush Instructions | Explicitly write back and/or invalidate cache lines | CPU `clflush`, `clwb`, `dc cvac`, `dcbf` | Non‑volatile memory, cache coherency management | Explicit | `clflush` (x86), `clflushopt`, `clwb`, `dc cvac` (ARM), `dcbf` (Power), `cflush` (RISC‑V) |
| Memory Coordination | Non‑temporal Stores | Stores that bypass cache (write‑combining) | Streaming stores (x86 `movnti`, `movntdq`) | Large sequential writes, avoid cache pollution | Explicit | Streaming store for integers, for double quadwords, for SIMD registers |
| Memory Coordination | Compiler Barrier | Prevents compiler reordering, not hardware | `asm volatile("" ::: "memory")`, `_ReadWriteBarrier` | Low‑level code, memory‑mapped I/O | Explicit | GCC/Clang `asm` barrier, MSVC `_ReadWriteBarrier`, `atomic_signal_fence` (C++) |
| Memory Coordination | Memory Ordering Annotations | Language‑level ordering constraints (weaker than barriers) | `memory_order_consume`, `acquire`, `release`, `acq_rel`, `seq_cst` (C++), `Ordering` enum (Rust) | High‑performance concurrent data structures | Explicit | consume (address dependency), acquire, release, relaxed, seq_cst |
| Visibility Coordination | Synchronizes‑With | Formal relation establishing happens‑before | Lock acquire/release, atomic operations, thread start/join | Formal correctness proofs | Implicit | Lock‑based, Atomic‑based, Thread‑based, Signal‑based (std::condition_variable) |
| Visibility Coordination | Data Race Freedom | Language guarantee of no data races | Type system (Rust), memory model (Java, C++ with proper atomics) | Safe concurrency by construction | Implicit | Rust ownership + borrow checker, Java `volatile` + final + locks, C++ data‑race‑free programs |
| Visibility Coordination | Final Field Publication | Safe publication via final fields (Java) | JMM rule: freezes final field at construction | Immutable objects, safe publication | Implicit | Final fields, `@Immutable` annotation, `record` (Java 14+) |
| Visibility Coordination | Thread‑local Handshake | Visibility via thread‑local storage | `thread_local` (C++), `ThreadLocal` (Java), `threading.local` (Python) | Per‑thread state without sharing | Implicit | Static thread‑local, Dynamic thread‑local (e.g., `ThreadLocal<T>`), Fast TLS (register‑based) |
| Communication Coordination | Rendezvous Channel | Zero‑capacity, synchronous channel | Dual‑queue with CAS; sender blocks until receiver ready | Tight handoff, no buffering | Explicit | Single‑rendezvous, Multi‑rendezvous, Channel with rendezvous + fallback buffer |
| Communication Coordination | Select / Alt | Multiplex over multiple channels | Runtime polling, epoll/kqueue/wait‑on‑multiple‑futures | CSP, actor systems | Explicit | Go `select`, Occam `ALT`, Rust `select!`, Async select (tokio) |
| Communication Coordination | Join Pattern | Match messages on multiple channels simultaneously | Join calculus runtime, pattern matcher | Synchronisation without explicit locks | Explicit | π‑calculus join, Cω chords, Join Java, Orc |
| Communication Coordination | Tuple Space | Associative shared memory via tuples | Linda, JavaSpaces, TSpaces | Coordination in distributed agents | Explicit | Generative, Read‑only, Take (destructive), TupleSpace with transactions |
| Communication Coordination | Blackboard | Centralised repository, agents read/write data | Shared memory + access control | AI, expert systems, multi‑agent | Explicit | Centralised blackboard, Distributed blackboard, Hierarchical |
| Communication Coordination | Work Queue (Job Queue) | Producer‑consumer with work stealing | Concurrent queue + worker threads (stealing) | Parallel task processing | Hybrid | FIFO work queue, LIFO work queue, Work stealing, Work sharing |
| Communication Coordination | Draining Queue | Bulk removal (drain_to) | Lock‑free or lock‑based with bulk transfer | Batch processing, migration | Hybrid | `drain_to` (C++ `concurrent_queue`), `drain_all`, timed drain |
| Communication Coordination | Broadcast Channel | One message to multiple receivers | Copy‑to‑each‑queue, or single message with reference count | Event notification, metrics | Explicit | Single‑producer, Multi‑producer, Persistent broadcast (history) |
| Communication Coordination | Fan‑out / Fan‑in | Parallel distribution and aggregation | Splitter queue + merger queue | MapReduce, scatter‑gather | Explicit | Dynamic fan‑out, Static fan‑out, Fan‑in with ordering |
| Isolation Coordination | Capability Isolation | Rights delegation via unforgeable tokens | Capsicum (cap_enter, cap_new), UNIX capabilities | Secure compartmentalisation | Implicit | POSIX capabilities, Capsicum, seccomp‑bpf + capabilities, Okta/oauth (distributed) |
| Isolation Coordination | Namespace Isolation | Linux kernel namespaces | `unshare`, `clone`, `setns` (mount, net, pid, user, uts, ipc, cgroup) | Container isolation (Docker, LXC) | Implicit | User namespace (UID remap), Network namespace (veth), PID namespace, Mount namespace |
| Isolation Coordination | Security Contexts | Mandatory access control | SELinux (type enforcement), AppArmor (path‑based), Smack, Tomoyo | Hardening multi‑tenant systems | Implicit | SELinux: targeted, strict; AppArmor: complain, enforce; Smack (simplified) |
| Isolation Coordination | Sandboxing | Restricted execution environment | Firejail, Bubblewrap (bwrap), Landlock, seccomp‑bpf | Running untrusted code | Implicit | System call filtering (seccomp), Path restriction (Landlock), Namespace + seccomp |
| Isolation Coordination | Virtual Machine Isolation | Hypervisor‑based separation | KVM, Xen, ESXi, Hyper‑V, VT‑x/AMD‑V | Strong isolation, cloud workloads | Implicit | Full virtualisation, Para‑virtualisation (virtio), Hardware‑assisted (VT‑x) |
| Isolation Coordination | Enclave Isolation | Hardware protected memory regions | Intel SGX, AMD SEV, Arm TrustZone | Confidential computing | Implicit | SGX: enclave, attestation; SEV: encrypted VMs; TrustZone: normal vs secure world |
| Isolation Coordination | SFI (Software Fault Isolation) | In‑process sandboxing | WebAssembly (linear memory), NaCl (segment mapping) | Browser, plugin safety | Implicit | Wasm (structured stack), NaCl (x86 with masking), SFI for RISC‑V |
| Isolation Coordination | Compartmentalisation | Fine‑grained privilege separation | CHERI (capability hardware), Morello prototype | Memory safety at C level | Implicit | CHERI pure‑capability, CHERI hybrid, Morello (ARM + CHERI) |
| Isolation Coordination | Resource Isolation (cgroups) | Limit CPU, memory, I/O, devices | Linux control groups v2 | Container resource control | Implicit | cpu.cfs, memory.low/min, io.max, pids.max, devices.allow, cpuset |
| Isolation Coordination | Container Isolation | User‑space isolation (namespaces + cgroups) | Docker, rkt, containerd, podman | Application packaging | Implicit | OCI runtime (runc), Kata (VM container), gVisor (user‑space kernel) |
| Isolation Coordination | Cryptographic Isolation | Encryption key per process / container | MKTME (Intel), SEV (AMD), encrypted filesystems (fscrypt) | Data secrecy even from hypervisor | Implicit | TME‑MK (key per VM), MKTME (key per enclave), fscrypt (per‑directory) |
| Transactional Coordination | Two‑Phase Commit (2PC) | Distributed transaction commit protocol | Coordinator + participants, prepare/commit log | Distributed DBs, XA transactions | Explicit | Classic 2PC, Presumed‑abort, Presumed‑commit, Linearisable 2PC |
| Transactional Coordination | Three‑Phase Commit (3PC) | Non‑blocking variant of 2PC | Additional pre‑commit phase | Fault‑tolerant commit (no network partitions) | Explicit | Basic 3PC, 3PC with timeouts, Paxos‑based 3PC |
| Transactional Coordination | Paxos Commit | Consensus‑based transaction commit | Uses Paxos for decision log | Spanner, Google Percolator | Explicit | Paxos Commit, Fast Paxos Commit |
| Transactional Coordination | Calvin | Deterministic ordering of transactions | Pre‑order transactions using sequencing layer | High‑throughput distributed DBs | Explicit | Calvin (no coordination during execution), Calvin with replication |
| Transactional Coordination | TrueTime | External consistency using GPS + atomic clocks | Hardware clock + uncertainty interval | Spanner globally distributed DB | Implicit | TrueTime (Google), Amazon TimeSync, Microsoft Time Service |
| Transactional Coordination | Percolator | Distributed transaction with timestamp oracle | 2PC + timestamp oracle + write‑locks | Bigtable‑based systems (TiDB) | Explicit | Original Percolator (Google), Parallel Percolator (TiDB) |
| Transactional Coordination | Saga | Compensating transactions | Sequence of local transactions + compensation logic | Long‑running workflows, microservices | Explicit | Orchestrated Saga, Choreographed Saga, Saga with backward recovery |
| Transactional Coordination | TCC (Try‑Confirm/Cancel) | Application‑level distributed transaction | Try (reserve), Confirm, Cancel | High‑performance payments, inventory | Explicit | TCC with idempotency, TCC with timeout, Hierarchical TCC |
| Transactional Coordination | Transactional Messaging | Exactly‑once delivery + DB update together | JTA/XA (resource manager), Outbox pattern + polling | Reliable message bus | Explicit | XA (2PC), Outbox with Kafka, Transaction log tailing (Debezium) |
| Transactional Coordination | Savepoint | Nested transaction checkpoint | LSN (log sequence number) | Partial rollback in large transactions | Explicit | Named savepoints, Nested transactions (real), Subtransactions |
| Transactional Coordination | Compensation Scope | Defines compensating actions for sub‑transactions | Workflow language (e.g., Temporal, Cadence) | Long‑running sagas | Explicit | Sync compensation, Async compensation, Retryable compensation |
| Transactional Coordination | Outbox Pattern | Ensures DB write + message send atomically | Transactional outbox table + message relay | Reliable event publishing | Explicit | Outbox with polling publisher, Outbox with CDC (Debezium), Outbox with transaction log |
| Distributed Coordination | Gossip Protocol | Epidemic dissemination | Random peer selection + periodic exchange | Membership, failure detection, data propagation | Implicit | Push gossip, Pull gossip, Push‑pull, SWIM, Plumbar |
| Distributed Coordination | SWIM | Scalable Weakly‑consistent Infection‑style Process Group Membership | Direct ping + indirect ping (k‑random) + suspicion | Cassandra, Consul, Akka cluster | Implicit | SWIM with suspicion, SWIM with round‑trip, Lifeguard (SWIM++), HyParView |
| Distributed Coordination | Phi Accrual Failure Detector | Adaptive failure detection using historical heuristics | Sliding window of heartbeat inter‑arrival times, phi distribution | Cassandra, Akka | Implicit | Single‑threshold, Multi‑threshold, Adaptive window |
| Distributed Coordination | Lease | Time‑bound grant of authority | Timestamp + renewal (TTL), revocation on expiry | Distributed lock cache, leader lease | Explicit | Single‑use lease, Renewable lease, Non‑renewable, Leases with fencing |
| Distributed Coordination | Fencing Token | Prevents split‑brain by monotonic tokens | Monotonic counter (epoch number) attached to each request | ZooKeeper, Kafka, Raft | Explicit | ZooKeeper `zxid`, Kafka controller epoch, Raft term, Google Chubby sequencer |
| Distributed Coordination | Distributed Semaphore | Cross‑node bounded concurrency | Distributed counter (etcd, ZooKeeper, Redis) | Throttling distributed tasks | Explicit | Counting semaphore, Fair semaphore (queue‑based), Timed semaphore |
| Distributed Coordination | Consistent Hashing | Distributed hash with minimal rehashing | Hash ring (MD5, SHA), virtual nodes | Dynamo, Cassandra, memcached | Implicit | Basic ring, Virtual nodes (weight), Rendezvous hashing (HRW), Jump consistent hash |
| Distributed Coordination | Quorum System | Read/write quorum (NWR) | Pairwise intersection (W + R > N) | Replicated databases, Dynamo | Explicit | Sloppy quorum, Hierarchical quorum, Grid quorum |
| Distributed Coordination | Replication Protocols | Maintain consistent copies | See variants | Fault tolerance, scalability | Explicit | Primary‑backup, Chain replication, State machine replication, Viewstamped, Multi‑Paxos, Raft |
| Distributed Coordination | Virtual Synchrony | Group communication with ordered views | ISIS, Spread, JGroups, ZooKeeper (atomic broadcast) | Group membership + multicast | Hybrid | Extended virtual synchrony, Weak virtual synchrony, Reliable virtual synchrony |
| Distributed Coordination | Byzantine Fault Tolerance (BFT) | Consensus despite malicious failures | PBFT, Tendermint, HotStuff, HoneyBadgerBFT | Blockchain, high‑assurance systems | Explicit | PBFT (3f+1), LibraBFT, MirBFT, SBFT |
| Distributed Coordination | Nakamoto Consensus | PoW longest chain | Proof‑of‑work, dynamic difficulty adjustment | Bitcoin, Ethereum (pre‑PoS) | Implicit | Nakamoto, GHOST, Conflux, Ouroboros (PoS variant) |
| Distributed Coordination | Proof‑of‑Stake (PoS) | Stake‑based voting | Casper FFG, Ouroboros, Tendermint | Energy‑efficient blockchain | Hybrid | Casper (validator list), Ouroboros (slot leader election), Tendermint (round‑robin proposer) |
| Distributed Coordination | Hybrid Logical Clocks (HLC) | Physical + logical clock for causality | Physical time + logical counter (mixing true time) | CockroachDB, Yugabyte | Implicit | HLC, Hybrid Time (Spanner true time + logical), Timestamp Oracle (Percolator) |
| Distributed Coordination | CRDTs (Conflict‑free Replicated Data Types) | Convergent replicated state | State‑based (CvRDT), Operation‑based (CmRDT), Delta‑CRDT | Offline‑first, collaborative editing | Implicit | G‑Counter, PN‑Counter, G‑Set, OR‑Set, LWW‑Set, MV‑Register, RGA (Sequence) |
| Distributed Coordination | Operational Transformation (OT) | Collaborative editing coordination | Transformation functions (dOPT, adOPTed, GOT, COT) | Google Docs, Wave | Hybrid | Centralised OT, Decentralised OT (WOOT), AST (Address Space Transformation) |
| Distributed Coordination | Anti‑entropy / Read Repair / Hinted Handoff | Eventually consistent replica sync | Merkle trees, timestamp comparison, hinted handoff log | Dynamo, Cassandra | Implicit | Read repair (blocking, async), Hinted handoff, Active anti‑entropy (Merkle) |
| Distributed Coordination | Service Discovery | Locate services dynamically | etcd, Consul, ZooKeeper, Eureka, DNS SRV | Microservices, cloud | Hybrid | Client‑side discovery, Server‑side discovery (load balancer), Service mesh (Pilot) |
| Distributed Coordination | Configuration Coordination | Distributed key‑value for config | etcd, Consul KV, ZooKeeper (Znode) | Feature flags, cluster config | Explicit | Watch‑based, Polling, Versioned config |
| Distributed Coordination | Distributed Circuit Breaker | Prevents cascading failures | Hystrix, Resilience4j, Sentinel | Microservice resiliency | Explicit | Client‑side, Proxy‑side, Circuit breaker with fallback |
| Distributed Coordination | Bulkhead Pattern | Resource isolation (thread pools, semaphores) | Per‑service thread pool / connection pool | Limiting failure blast radius | Explicit | Thread pool bulkhead, Semaphore bulkhead, Connection bulkhead |
| Distributed Coordination | Hedged Request | Race multiple replicas, take first reply | Send request to N replicas, cancel/ignore others | Low‑latency tail tolerance | Explicit | Hedged with backup request (after delay), Full hedging (parallel) |
| Distributed Coordination | Load Balancing Policies | Distribute requests among backends | Round‑robin, least connections, consistent hash, power of two choices, adaptive | Reverse proxies, gRPC, Kubernetes | Hybrid | Round‑robin, Weighted RR, Least loaded, Consistent hash, P2C (Power of Two Choices), Adaptive (load‑aware) |
| Distributed Coordination | Distributed Throttling | Rate limiting across nodes | Token bucket in Redis, etcd, or sliding window with coordination | API gateways, cloud resources | Explicit | Centralised (Redis), Distributed (etcd lease + quota), Edge‑based with consensus |
| Distributed Coordination | Shard Rebalancing | Automatic data migration | Raft snapshot transfer, consistent hash ring adjustment, automatic tablet splitting | Dynamo, Cassandra, ClickHouse | Hybrid | Automatic (Dynamo), Manual (Redis Cluster), Rebalancer with quorum |
| Distributed Coordination | Distributed Deadlock Detection | Detect cycles in wait‑for graph across nodes | Centralised waiter graph, edge chasing (path pushing), diffusion computation | Distributed DBs, lock managers | Explicit | Centralised detector, Hierarchical detector, Distributed (Chandy‑Misra‑Haas) |
| Distributed Coordination | Distributed Mutual Exclusion | Cross‑node exclusive access | Ricart‑Agrawala, Maekawa, Suzuki‑Kasami, Raymond’s tree | Distributed systems without leader | Explicit | Token‑based (Raymond), Quorum‑based (Maekawa), Timestamp‑based (Ricart‑Agrawala) |
| Distributed Coordination | Fencing (STONITH) | Node‑level power/reset fencing | SCSI‑3 persistent reservations, IPMI, network switch API | High availability clusters | Explicit | STONITH (Shoot The Other Node In The Head), External fencing (Pacemaker), Watchdog fencing |
| Distributed Coordination | Split‑brain Avoidance | Prevent simultaneous active leadership | Quorum, dynamic quorum, tie‑breaking (arbitrator, witness disk) | Clustered filesystems, DB clusters | Explicit | Quorum (majority), Dynamic quorum (adjustable), Arbiter node, Witness disk |
| Distributed Coordination | Kubernetes Controller Coordination | Informers, workqueues, leader election | Client‑go informer (reflector, indexer), workqueue (rate limiting), Lease election | K8s operators, custom controllers | Hybrid | SharedInformers, DeltaFIFO, RateLimitingQueue, LeaderElection with lease |
| Failure Coordination | Circuit Breaker | Trip on failure threshold | Closed -> Open -> Half‑Open state, timeout | Resilient microservices | Explicit | Count‑based, Time‑based, Slow call detector, Adaptive circuit breaker |
| Failure Coordination | Exponential Backoff & Jitter | Retry with increasing delay + randomness | Sleep( base * 2^retry + jitter ) | Cloud APIs, network calls | Explicit | Full jitter (random uniform), Equal jitter, Decorrelated jitter |
| Failure Coordination | Retry Budget | Limit total retry volume | Token bucket for retries | Prevent retry storms | Hybrid | Per‑method budget, Global budget, Dynamic budget (adaptive) |
| Failure Coordination | Health Checks | Liveness, readiness, startup probes | HTTP endpoint, TCP connection, exec command | Kubernetes, load balancers | Explicit | Liveness (restart), Readiness (traffic cut), Startup (slow start), gRPC health protocol |
| Failure Coordination | Watchdog Timer | Hardware/software timer triggering reset | Hardware watchdog (WDT), software timer + kernel thread | Embedded, safety‑critical | Implicit | External hardware watchdog, Internal CPU watchdog, Software watchdog (monitoring daemon) |
| Failure Coordination | Crash‑Only Software | No graceful shutdown, only crash + restart | Idempotent operations, transaction logs, reboot | High‑availability embedded, some cloud | Implicit | Crash‑only with journal, Crash‑only with recovery script |
| Failure Coordination | Redundancy Styles | Active‑passive, active‑active, N+M | Keepalived, HAProxy, LVS | Service HA | Explicit | Active‑passive (failover), Active‑active (load‑sharing), N+M (N active, M spare), 2N, 2N+1 |
| Failure Coordination | Failover / Failback | Transition to/from backup | Heartbeat + takeover (e.g., Pacemaker, Corosync) | High availability clusters | Explicit | Manual failover, Automatic failover, Failback with resync |
| Failure Coordination | Coordinated Checkpointing | Distributed snapshot | Chandy‑Lamport algorithm (marker) | Stateful distributed systems (Flink) | Explicit | Coordinated (blocking), Non‑blocking with markers |
| Failure Coordination | Uncoordinated Checkpointing | Each process checkpoints independently | Periodic local snapshots, domino effect risk | Research, low‑frequency checkpoints | Explicit | Basic uncoordinated, Periodic with logging |
| Failure Coordination | Message Logging | Recover messages after failure | Pessimistic (log before send), Optimistic, Causal, Sender‑/receiver‑based | Reliable message queues, actors | Explicit | Pessimistic (blocking), Optimistic (no block, rollback), Causal logging (minimal domino) |
| Failure Coordination | Deterministic Replay | Record and replay execution | Hardware tracing (Intel PT), software logging (rr) | Debugging concurrency bugs | Explicit | Record‑replay (rr, UndoDB), Hardware‑assisted (Intel PT, Arm ETM) |
| Failure Coordination | Power Fail Recovery | Recover after sudden power loss | Journaling (ext4, XFS), Write‑Ahead Log (WAL), Copy‑on‑Write (ZFS, Btrfs), Shadow paging | Filesystems, databases | Implicit | Full journal, Ordered journal, Write‑ahead log (WAL) with checkpoint, Copy‑on‑write (ZFS) |
| Failure Coordination | Backup Coordination | Full, incremental, differential, hot/cold | rsync, snapshot (LVM, EBS), backup agents | Disaster recovery | Explicit | Full backup, Incremental (changed since last), Differential (changed since full), Online hot backup (consistent via lock) |
| Failure Coordination | State Machine Snapshot | Capture state of replicated log | Raft snapshot (replace log), transfer snapshot as file | Distributed systems (Raft) | Explicit | Raft snapshot, Log compaction, Snapshot transfer |
| Failure Coordination | Graceful Shutdown | Quiesce, drain, then terminate | PreStop hooks (K8s), SIGTERM handler, connection draining | Microservices, daemons | Explicit | Shutdown with timeout, Shutdown with inflight request draining, Rolling shutdown |
| Progress Coordination | Read‑Copy‑Update (RCU) | Deferred memory reclamation with grace periods | Grace period detection (quiescent state), `synchronize_rcu` | Linux kernel, read‑most data structures | Hybrid | Classic RCU (quiescent states), Sleepable RCU (SRCU), Tasks RCU, Preemptible RCU |
| Progress Coordination | Hazard Pointers | Safe memory reclamation for lock‑free structures | Per‑thread hazard pointer list, retire list with scan | Lock‑free linked lists, maps | Explicit | Hazard pointers (HP), Hazard eras, Hazard pointers with epoch |
| Progress Coordination | Epoch‑Based Reclamation (EBR) | Reclaim based on global epoch | Global epoch counter, per‑thread active flag, retire to local list | Lock‑free queues, memory management | Explicit | EBR, EBR with local garbage list, EBR with global epoch |
| Progress Coordination | Quiescent State‑Based Reclamation (QSBR) | RCU‑like, threads announce quiescent states | `rcu_quiescent_state`, global grace period | User‑space RCU (liburcu) | Explicit | QSBR (thread‑specific), QSBR with batch, QSBR with signal |
| Progress Coordination | Flat Combining | One thread collects and executes operations for others | Combine array + combiner thread | High‑contention data structures | Explicit | Classic Flat Combining, Flat Combining with wait‑free publishing |
| Progress Coordination | Combining Tree | Hierarchical aggregation of operations | Tree of combining nodes, bottom‑up aggregation | Distributed data structures, multi‑core | Explicit | Binary combining tree, K‑ary tree, Combining with elimination |
| Progress Coordination | Elimination Backoff | Pairwise cancellation of matching operations | Exchanger (stack elimination array) | Elimination stack, queue | Explicit | Stack elimination, Queue elimination, Elimination array with backoff |
| Progress Coordination | Helpful Algorithms (Helping) | Threads help complete pending operations | Pass operation descriptors, CAS on status | Wait‑free implementations | Explicit | Helping via descriptors (e.g., wait‑free queue), Pass‑the‑buck helping |
| Temporal Coordination | High‑Resolution Timers (hrtimers) | Nanosecond‑precision kernel timers | Red‑black tree of timers, hardware timer (TSC, HPET) | Real‑time, precise scheduling | Implicit | hrtimer (Linux), POSIX `clock_nanosleep`, `timerfd` |
| Temporal Coordination | Timer Slack Coalescing | Group close timers to reduce wakeups | Adjust expiry by slack (e.g., 100 µs) | Power‑efficient systems, Android | Implicit | Timer slack (Linux `prctl`), Coalescing timer wheel, Adaptive coalescing |
| Temporal Coordination | Tickless Kernel (NOHZ) | No periodic timer interrupt when idle | Dynamic tick, stop idle tick | Low‑power systems, real‑time | Implicit | NO_HZ_IDLE, NO_HZ_FULL (full dynticks), RCU dyntick |
| Temporal Coordination | Rate Monotonic Scheduling (RMS) | Fixed priority based on period | Priority = shorter period → higher priority | Real‑time systems (periodic tasks) | Implicit | Basic RMS, RMS with resource protocols (PIP, PCP), HRT (hard real‑time) |
| Temporal Coordination | Sporadic / Deferrable / Constant Bandwidth Server | Resource reservation for aperiodic tasks | Server budget (C) and period (T) | Real‑time mixed workload | Implicit | Polling server, Sporadic server, Deferrable server, Constant Bandwidth Server (CBS) |
| Temporal Coordination | Admission Control | Accept/reject tasks based on utilisation | Utilisation bound test (e.g., RMS: n*(2^(1/n)-1)), EDF (sum <= 1) | Real‑time guarantee | Hybrid | Offline admission test, Online admission (QoS, dynamic) |
| Temporal Coordination | Stack Resource Policy (SRP) | Real‑time sync + deadlock avoidance | Priority ceiling via stack resources | Real‑time OS (e.g., OSEK, FreeRTOS) | Hybrid | SRP, SRP with multi‑unit resources, SRP for nested locking |
| Temporal Coordination | Robust Mutex / Robust Futex | Recover when owner dies | Kernel marks mutex as inconsistent, FUTEX_OWNER_DIED | Reliable lock recovery | Explicit | Robust mutex (pthread), Robust futex, Owned mutex with state |
| Language | Linear / Affine / Uniqueness Types | Enforce single ownership | Type system (linear: use exactly once; affine: at most once) | Memory safety, resource management | Implicit | Linear types (Idris, ATS), Affine types (Rust), Uniqueness (Clean), Reference capabilities (Pony) |
| Language | Session Types | Protocol conformance across channels | Typed channels (binary session types, multiparty) | Verifying communication protocols | Implicit | Binary session types (SCC), Multiparty session types (MPST), Scribble |
| Language | Typestate | State‑aware types (finite‑state machines) | Typestate checking (Plaid, Rust state machines via typestate pattern) | Object lifecycle, protocol validation | Implicit | Linear typestate, Ownership‑based typestate (Rust), Verona |
| Language | Effect Systems | Track side effects (concurrency, IO, async) | Effect rows / algebraic effects (Koka, Eff, OCaml) | Pure/impure separation, async inference | Implicit | IO effect, Async effect, Concurrency effect, Rows vs labelled effects |
| Language | Region‑Based Memory Management | Automatic region inference | Region inference engine + type system (ML Kit, Cyclone) | Real‑time GC alternative | Implicit | Lexical regions (Cyclone), Dynamic regions, LIFO regions, Reference count regions |
| Language | Drop (RAII) | Deterministic resource release | Destructors called when variable goes out of scope | C++, Rust, resource cleanup | Implicit | Rust `Drop` trait, C++ destructor, Swift `deinit`, Python `__del__` (less deterministic) |
| Language | Defer / Finally / Try‑with‑resources | Scoped cleanup | Go `defer`, Java `finally`, C# `using`, Python `with`, Kotlin `use` | Resource management (files, locks) | Explicit | Stacked defer (LIFO), Panic‑safe defer, Try‑with‑resources (auto‑close) |
| Language | Thread‑Local Storage (TLS) | Per‑thread static data | `__thread` (GCC), `thread_local` (C++11), `ThreadLocal` (Java) | Thread‑specific state, random seeds | Implicit | Static TLS (fixed offset), Dynamic TLS (allocation at runtime), `_Thread_local` (C11) |
| Language | Async‑Local Storage | Propagates context across async calls | `contextvars` (Python), `AsyncLocal` (C#), `Context` (Go) | Request tracing, dependency injection | Implicit | Copy‑on‑write context, Immutable context, Context with cancel/timeout |
| Language | Coroutine / Generator | Suspendable functions | `yield`, `await`, `async`/`await` (state machine) | Stream processing, async I/O | Hybrid | Symmetric coroutine (call/cc), Asymmetric coroutine (yield), Generator (yield return), C++20 coroutines (`co_yield`, `co_await`) |
| Language | Continuations (delimited) | Capture remaining computation | `shift`/`reset`, `call/cc` (Racket, Scheme, OCaml) | Control inversion, early exit, async | Explicit | Undelimited (call/cc), Delimited (shift/reset, prompt), Composable continuations |
| Language | Atomic Blocks (language level) | Language‑provided atomicity | `synchronized` (Java), `lock` (C#), `@atomic` (Swift), `atomic` (C++ – not a block) | Critical sections with convenience | Explicit | Object monitor, Reentrant lock syntactic sugar, Atomic region (OpenMP) |
| Language | Parallel / Task Regions | OpenMP‑style parallelism | `#pragma omp parallel`, `task`, `taskwait`, `taskgroup` | Shared‑memory HPC | Explicit | Parallel for, Sections, Task (single/multiple), Taskloop, Taskgroup, Depends |
| Language | PGAS (Partitioned Global Address Space) | Shared memory with affinity | UPC, Coarray Fortran, Chapel (global view) | HPC, large‑scale data sharing | Implicit | UPC (shared/private pointers), Coarrays (Fortran 2008), OpenSHMEM |
| Language | X10 / Chapel / Habanero Java | Async‑finish, phasers, clocks | Async/finish constructs, phasers (X10), forall (Chapel) | Productivity parallel programming | Hybrid | async, finish, phaser (X10); forall, sync (Chapel); Habanero Java (HJ) |
| Hardware | Transactional Lock Elision (TLE) | Elide locks using HTM | RTM/HLE transparently executes lock elision | Improving lock scalability | Implicit (transparent) | XACQUIRE/XRELEASE (Intel HLE), TLE with fallback |
| Hardware | Memory Controller Scheduling | Reorder DRAM commands | FR‑FCFS, ATLAS, BLISS, per‑bank queues, write draining | DDR4/5, HBM | Implicit | FR‑FCFS (First‑Ready First‑Come‑First‑Served), ATLAS (adaptive), BLISS, TCM (thread cluster) |
| Hardware | DRAM Refresh Coordination | Manage refresh to reduce impact | Auto‑refresh, self‑refresh, per‑bank refresh, refresh postponement | Low‑power, real‑time | Implicit | Per‑bank (fine‑grained), All‑bank (coarse), Refresh‑free (long idle), PASR (partial array) |
| Hardware | Cache Replacement Policies | Decide which cache line to evict | LRU, PLRU, FIFO, NMRU, RRIP, SRRIP, DRRIP, SHiP, Hawkeye | CPU caches (L1, L2, LLC) | Implicit | LRU, Pseudo‑LRU (tree‑PLRU), BIP (bimodal), RRIP (re‑reference interval prediction), SRRIP, DRRIP, Hawkeye (machine learning) |
| Hardware | Hardware Prefetching | Fetch data into cache before demand | Stream, stride, adjacency, software prefetch, prefetch distance throttling | Hiding memory latency | Implicit | Next‑line, Stride (fixed), Stream (detect streams), Spatial prefetcher, Delta‑correlation, PIF (prefetch‑in‑flight) |
| Hardware | Cache Bypassing / Locking | Selectively bypass or lock lines | Non‑temporal stores (bypass), cache lockdown registers (ARM), Intel CAT (lock cache ways) | Real‑time, streaming data | Explicit | Write‑combining bypass, Read‑only cache locking, Way locking, MSR‑based locking |
| Hardware | QoS (Cache/Memory) | Intel RDT (CAT, MBA, CDP), ARM MPAM | CAT (cache allocation), MBA (memory bandwidth), CDP (code/data prioritisation) | Multi‑tenant clouds | Implicit | Intel RDT, ARM MPAM, AMD QoS (via CCC), PQOS (Linux resctrl) |
| Hardware | PCIe Transaction Ordering | Relaxed / ID‑based ordering | Relaxed Ordering (RO), ID‑Based Ordering (IDO), No Snoop (NS), Traffic Class / Virtual Channel | High‑performance NICs, GPUs | Explicit | Relaxed Ordering (RO), IDO (ID‑based), Strong ordering (default), VC/TC priorities |
| Hardware | PCIe Atomic Operations | Hardware atomic ops over PCIe | Atomic Fetch‑and‑add, CAS, swap, bit test‑and‑set | RDMA, GPU‑initiated atomics | Explicit | PCIe 3.0+ atomic operations, CXL atomic, NVLink atomic |
| Hardware | CXL Coordination | Cache coherent interconnect | CXL.cache (coherency), CXL.mem (memory pooling), fabric manager | Disaggregated memory, accelerators | Implicit | CXL 1.1, 2.0, 3.0; CXL.cache (H2D, D2H); CXL.mem (type 1/2/3 devices); Global persistent flush |
| Hardware | NVLink / NVSwitch | High‑bandwidth GPU interconnect | NVLink 1.0/2.0/3.0, NVSwitch (all‑to‑all GPU communication) | Multi‑GPU training, inference | Implicit | NVLink (point‑to‑point), NVSwitch (full crossbar), SHARP (in‑network reduction) |
| Hardware | InfiniBand / RoCE | RDMA with congestion control | InfiniBand (IBTA), RoCE (RDMA over Converged Ethernet) | HPC, storage (NVMe‑oF) | Implicit | InfiniBand (reliable, unreliable), RoCEv2 (UDP), iWARP, DCQCN (congestion control) |
| Hardware | IOMMU / VT‑d | DMA remapping and protection | DMA remapping, interrupt remapping, ATS, PASID | Virtualisation, device isolation | Implicit | VT‑d (Intel), AMD‑Vi, ARM SMMU, IOMMU with ATS (Address Translation Services) |
| Hardware | Performance Monitoring (PMU) | Hardware counters for profiling | Fixed counters, programmable counters, PEBS, LBR, Intel PT | Profiling, optimisation | Implicit | x86 PMU (fixed: inst_retired, cycles), ARM PMU (events), LBR (last branch record), Intel PT (tracing) |
| Hardware | Thermal Throttling | Reduce frequency on overheat | Clock modulation (proportional), frequency reduction (P‑state throttling), task migration | Laptop, server cooling | Implicit | Clock modulation (skipping cycles), DVFS (lower P‑state), TCC offset (Intel), Hysteresis control |
| Hardware | Power Management (DVFS, C‑states) | Dynamic voltage/frequency scaling + idle states | P‑states (performance), C‑states (idle), power gating, clock gating | Energy efficiency | Implicit | ACPI P‑states (performance), C‑states (C1, C1E, C2, C3, C6, …), S‑states (suspend), T‑states (throttling) |
| Hardware | Virtualisation Hardware | CPU support for VMs | VMCS (Intel), VMCB (AMD), EPT/NPT, VPID, tagged TLBs, ASID | Hypervisors (KVM, Xen, ESXi) | Implicit | Intel VT‑x (VMX), AMD‑V (SVM), EPT/NPT (nested paging), VPID (tagged TLB), ASID (ARM) |
| Hardware | SR‑IOV / MR‑IOV | Single‑/Multi‑Root I/O Virtualisation | PCIe SR‑IOV (physical function (PF) + virtual functions (VF)) | High‑performance VMs, network/storage devices | Implicit | SR‑IOV (single root), MR‑IOV (multi‑root sharing), Scalable IOV (Intel) |
| Hardware | VirtIO & vhost | Para‑virtualisation for I/O | Virtqueues (split/packed), event index, vhost‑user, vDPA | QEMU/KVM, container networking | Implicit | VirtIO 1.0, 1.1 (packed virtqueue); vhost‑net, vhost‑user (DPDK), vDPA (virtio datapath acceleration) |
| Hardware | Network on Chip (NoC) | Router pipeline, VC allocation, deadlock‑free routing | Router pipeline (route, VC allocation, switch allocation), turn models | Manycore (TILE64, Epiphany), GPUs | Implicit | Mesh, Torus, Ring, Tree; VC (virtual channel), Escape VC (deadlock avoidance); XY, up*/down*, turn model (West‑First, North‑Last, Negative‑First) |
| Hardware | Hardware Barrier / Reduction | Dedicated sync / reduction network | Global barrier wire, reduction tree (adder, min, max) | SIMD, GPU warp sync, Cray shmem | Implicit | Hardware barrier (barrier instruction), Reduction tree (parallel sum), All‑to‑all barrier |
| Hardware | Hardware Mailbox / Queue | Low‑level inter‑core FIFO | Dedicated memory + hardware handshake (ARM Mailbox, Intel MCS) | Firmware, inter‑core communication | Explicit | MS‑queue (hardware), RING with doorbell, Mailbox with interrupt |
| Arbitration Coordination | Resource Arbiter | Resolves contention over scarce shared resources | Arbitration algorithms, token assignment, queue ordering | CPU, memory, I/O, bus allocation | Hybrid | Centralized arbiter, Distributed arbiter, Fair arbiter, Weighted arbiter |
| Arbitration Coordination | Resource Reservation | Guarantees future resource availability | Reservation tables, quotas, admission control | Real-time systems, networking, cloud scheduling | Explicit | Hard reservation, Soft reservation, Time-slot reservation |
| Arbitration Coordination | Quota System | Enforces bounded resource consumption | Counters, token accounting, cgroups | Multi-tenant systems, APIs | Explicit | Fixed quota, Elastic quota, Hierarchical quota |
| Arbitration Coordination | Fair Queuing | Shares resources proportionally across consumers | Virtual finish times, weighted queues | Networking, storage schedulers | Implicit | WFQ, DRR, SFQ, Hierarchical fair queuing |
| Arbitration Coordination | Credit-Based Flow Control | Limits producers through transferable credits | Credit counters + acknowledgements | Interconnects, distributed messaging | Explicit | Static credits, Dynamic credits, Window credits |
| Arbitration Coordination | Priority Inheritance Protocol | Prevents unbounded priority inversion | Temporary priority boosting | Real-time locking | Implicit | Basic PIP, Nested PIP, Distributed PIP |
| Arbitration Coordination | Priority Ceiling Protocol | Prevents deadlock and priority inversion | Static resource priority ceilings | Hard real-time systems | Implicit | Original PCP, Immediate ceiling PCP |
| Dependency Coordination | Dependency Graph | Explicitly models execution dependencies | DAG structures + topological scheduling | Build systems, workflow engines | Explicit | Static DAG, Dynamic DAG, Cyclic dependency graph |
| Dependency Coordination | Dataflow Graph | Executes computations when inputs become available | Data dependency edges + firing rules | Stream processing, reactive runtimes | Implicit | Static dataflow, Dynamic dataflow, Synchronous dataflow |
| Dependency Coordination | Incremental Recomputation | Recomputes only invalidated subgraphs | Dependency tracking + invalidation propagation | IDEs, spreadsheets, caches | Hybrid | Pull-based, Push-based, Self-adjusting computation |
| Dependency Coordination | Constraint Propagation | Coordinates through constraint satisfaction | Solver propagation engines | Scheduling, optimization, reactive UI | Implicit | SAT propagation, CSP propagation, SMT propagation |
| Dependency Coordination | Workflow DAG Engine | Coordinates multi-stage task execution | Persistent DAG runtime + orchestration | ETL, ML pipelines, workflows | Explicit | Airflow-style, Temporal-style, Serverless DAG |
| Flow Coordination | Backpressure | Regulates producers according to consumer capacity | Demand propagation, bounded queues | Reactive streams, messaging | Hybrid | Push backpressure, Pull backpressure, Adaptive backpressure |
| Flow Coordination | Window-Based Flow Control | Bounds in-flight operations/messages | Sliding windows + acknowledgements | TCP, RPC streaming | Explicit | Fixed window, Sliding window, Dynamic window |
| Flow Coordination | Congestion Control | Adapts throughput to system/network load | RTT estimation, packet loss heuristics | Networks, distributed systems | Implicit | Reno, Cubic, BBR, Vegas |
| Flow Coordination | Demand Signaling | Consumers explicitly request production volume | Request counters/messages | Reactive Streams, async pipelines | Explicit | Pull-based, Credit-based, Batched demand |
| Flow Coordination | Watermark Coordination | Tracks progress through event-time streams | Monotonic timestamps + coordination barriers | Stream processing | Implicit | Event-time watermark, Processing-time watermark, Idle watermark |
| Flow Coordination | Batching Coordination | Groups operations into coordinated batches | Batch queues + flush policies | Storage, messaging, stream systems | Hybrid | Fixed batch, Adaptive batch, Time-window batch |
| Deterministic Coordination | Deterministic Scheduler | Produces reproducible execution ordering | Controlled scheduling + replay logs | Testing, simulation | Explicit | Record/replay scheduler, Seeded scheduler |
| Deterministic Coordination | Deterministic Parallelism | Guarantees deterministic parallel execution | Ordered commit + deterministic reduction | HPC, scientific computing | Implicit | Kahn process network, Deterministic STM |
| Deterministic Coordination | Epoch Determinism | Partitions execution into deterministic epochs | Epoch barriers + ordered commits | Simulation, distributed runtimes | Hybrid | Fixed epoch, Adaptive epoch |
| Speculative Coordination | Speculative Execution Coordination | Executes before correctness certainty | Prediction + rollback | CPUs, databases | Implicit | Branch speculation, Transaction speculation |
| Speculative Coordination | Rollback Coordination | Restores previous consistent state | Undo logs, snapshots | Transactions, distributed recovery | Explicit | Full rollback, Partial rollback, Cascading rollback |
| Speculative Coordination | Shadow Copy Coordination | Applies updates to isolated replicas | Copy-on-write, shadow paging | Filesystems, STM | Hybrid | Full shadow copy, Delta shadowing |
| Speculative Coordination | Undo Logging | Enables reversible operations | Write-ahead undo records | Databases, recovery systems | Explicit | Physical undo log, Logical undo log |
| Persistence Coordination | Journaling | Coordinates crash-safe persistent updates | Append-only journals | Filesystems | Implicit | Metadata journal, Full data journal |
| Persistence Coordination | Write-Ahead Logging | Persists intent before commit | Sequential durable logging | Databases | Explicit | ARIES WAL, Logical WAL, Physical WAL |
| Persistence Coordination | File Locking | Coordinates concurrent file access | Kernel lock tables | IPC, storage systems | Explicit | Advisory lock, Mandatory lock, Byte-range lock |
| Persistence Coordination | Snapshot Isolation Engine | Coordinates consistent storage snapshots | MVCC + snapshot timestamps | Databases | Implicit | Snapshot isolation, Serializable snapshot |
| Persistence Coordination | Copy-on-Write Coordination | Creates isolated writable replicas | Page/block remapping | Filesystems, VMs | Implicit | Block COW, Page COW, Tree-based COW |
| Dataflow Coordination | Stream Processor | Coordinates continuous event processing | Stateful operators + streaming runtime | Analytics, telemetry | Hybrid | Stateless, Stateful, Windowed |
| Dataflow Coordination | Stateful Stream Coordination | Coordinates distributed operator state | Checkpoint barriers + state backends | Flink, Beam | Hybrid | Keyed state, Operator state |
| Dataflow Coordination | Shuffle Coordination | Redistributes partitioned data | Partition exchanges + routing | MapReduce, Spark | Explicit | Hash shuffle, Range shuffle, Broadcast shuffle |
| Dataflow Coordination | Exactly-Once Stream Coordination | Prevents duplicate or lost stream effects | Checkpointing + transactional sinks | Streaming systems | Explicit | Barrier-based, Idempotent sink, Transactional sink |
| Knowledge Coordination | Membership Coordination | Maintains shared view of cluster participants | Heartbeats + dissemination | Distributed clusters | Implicit | Static membership, Dynamic membership |
| Knowledge Coordination | Failure Detector | Infers failed nodes/processes | Heartbeat timeout heuristics | Distributed systems | Implicit | Push heartbeat, Pull heartbeat, Phi accrual |
| Knowledge Coordination | View Synchrony | Coordinates membership and message delivery | Ordered view transitions | Group communication | Hybrid | Virtual synchrony, Extended virtual synchrony |
| Knowledge Coordination | Topology Dissemination | Propagates routing/topology knowledge | Gossip or routing propagation | Cluster networking | Implicit | Flooding, Gossip, Hierarchical |
| Knowledge Coordination | State Dissemination Protocol | Propagates replicated system state | Gossip + anti-entropy | Distributed caches | Hybrid | Epidemic dissemination, Tree dissemination |
| Orchestration Coordination | Orchestrator | Coordinates lifecycle of distributed tasks/services | Centralized control plane | Kubernetes, Nomad | Explicit | Centralized orchestrator, Federated orchestrator |
| Orchestration Coordination | Placement Coordinator | Assigns workloads to execution locations | Constraint scheduling + scoring | Cluster schedulers | Explicit | Bin packing, Spread, Affinity-based |
| Orchestration Coordination | Autoscaling Coordinator | Dynamically adjusts capacity | Feedback controllers + metrics | Cloud infrastructure | Hybrid | Reactive scaling, Predictive scaling |
| Orchestration Coordination | Deployment Coordinator | Coordinates rolling system changes | Health checks + staged rollout | CI/CD, microservices | Explicit | Rolling deploy, Blue-green, Canary |
| Causality Coordination | Atomic Broadcast | Delivers messages in identical total order | Consensus + ordered logs | Replicated state machines | Explicit | Total order broadcast, Uniform atomic broadcast |
| Causality Coordination | Reliable Broadcast | Guarantees message dissemination | Retransmission + acknowledgements | Distributed messaging | Explicit | Best-effort, Uniform reliable, FIFO reliable |
| Causality Coordination | Causal Broadcast | Preserves causal message ordering | Vector clocks + buffering | Collaborative systems | Implicit | FIFO causal, Uniform causal |
| Causality Coordination | Global Snapshot | Captures consistent distributed state | Marker protocols | Distributed checkpointing | Explicit | Chandy-Lamport, Lai-Yang |
| Causality Coordination | Stable Time Computation | Determines globally safe progress frontier | Watermark aggregation | Distributed databases | Implicit | Low watermark, Frontier-based |
| Observability Coordination | Race Detection | Detects conflicting unsynchronized accesses | Happens-before analysis | Concurrency debugging | Explicit | Dynamic race detection, Static analysis |
| Observability Coordination | Deadlock Detection | Detects wait dependency cycles | Wait-for graph analysis | Databases, runtimes | Explicit | Centralized detection, Distributed detection |
| Observability Coordination | Happens-Before Tracing | Records causal execution relationships | Event tracing + vector clocks | Debugging, replay | Explicit | Vector-clock tracing, Epoch tracing |
| Observability Coordination | Contention Monitoring | Measures synchronization contention | Runtime counters + profiling | Performance engineering | Implicit | Lock contention, Cache contention |
| Observability Coordination | Causal Profiling | Measures effect of latency reductions | Perturbation analysis | Systems optimization | Explicit | Sampling causal profiling, Deterministic profiling |
| Adaptive Coordination | Adaptive Scheduler | Dynamically adjusts scheduling policy | Runtime telemetry feedback loops | OS/runtime schedulers | Implicit | Load-aware, Latency-aware, Energy-aware |
| Adaptive Coordination | Adaptive Backoff | Adjusts retry delay under contention | Exponential/randomized backoff tuning | Spinlocks, distributed retries | Implicit | Linear, Exponential, Jittered |
| Adaptive Coordination | Dynamic Load Shedding | Drops work during overload | Queue pressure heuristics | Distributed services | Explicit | Probabilistic shedding, Priority shedding |
| Adaptive Coordination | Elastic Coordination | Dynamically resizes coordination topology | Auto-partitioning + scaling | Cloud systems | Hybrid | Horizontal scaling, Vertical scaling |
| Adaptive Coordination | Coordination Feedback Control | Uses closed-loop regulation for coordination | PID/control-theoretic loops | Datacenters, schedulers | Implicit | PID, MPC, Reinforcement-based |
| Accelerator Coordination | Warp Synchronization | Synchronizes GPU SIMD execution lanes | Warp barriers/instructions | CUDA/OpenCL kernels | Implicit | Warp barrier, Warp vote, Warp shuffle |
| Accelerator Coordination | CUDA Stream Coordination | Orders asynchronous GPU operations | GPU command queues | GPU compute pipelines | Explicit | Default stream, Priority stream |
| Accelerator Coordination | SIMT Divergence Coordination | Coordinates branch divergence recovery | Masked execution + reconvergence | GPUs | Implicit | Immediate reconvergence, Stack-based reconvergence |
| Accelerator Coordination | Cooperative Groups | Structured GPU collective coordination | Group synchronization primitives | CUDA cooperative kernels | Explicit | Thread block, Warp group, Grid group |
| Protocol Coordination | Session Protocol Coordination | Enforces communication protocol correctness | Session type checking | Distributed communication | Implicit | Binary session types, Multiparty session types |
| Protocol Coordination | Capability-Based Coordination | Governs interactions through authority tokens | Capability references + access checks | Secure systems | Implicit | Object capabilities, OS capabilities |
| Protocol Coordination | Ownership Transfer Coordination | Transfers mutation/control authority safely | Move semantics + ownership rules | Rust-style systems | Implicit | Linear ownership, Affine ownership |
| Topology Coordination | Dissemination Tree | Coordinates hierarchical propagation | Tree routing structures | Broadcast, aggregation | Implicit | Binomial tree, Spanning tree |
| Topology Coordination | Partition Coordination | Coordinates isolated execution regions | Partition maps + routing | Distributed databases | Hybrid | Static partitioning, Dynamic partitioning |
| Topology Coordination | Rebalancing Coordination | Redistributes ownership/workload | Migration protocols | Sharded systems | Explicit | Incremental rebalance, Full rebalance |

### Hardware Substrate

> See [Hardware Substrate](note.html?n=technica/computation/concurrency/conceptual-model-coordination/hardware-substrate.md).
> 

### **Implicit Coordination Mechanism**

> See more in [Implicit Coordination Mechanism](note.html?n=technica/computation/concurrency/conceptual-model-coordination/implicit-coordination-mechanism.md).
> 

## Intrisic Technical Problem

> Which are the technical problems introduced by concurrent execution, and which concurrency coordination techniques can be introduced to address them?
> 

> See more in [Intrisic Technical Problem](note.html?n=technica/computation/concurrency/conceptual-model-coordination/intrisic-technical-problem.md).
> 

## Concurrency Paradigm(s)

| **Paradigm** | **Description** | **Formulation** | **Instance(s)** |
| --- | --- | --- | --- |
| **Shared-Memory Concurrency** | Concurrent entities interact by reading and writing shared state | Threads + memory model + synchronization | POSIX threads (C), Java threads, C++ threads |
| **Message-Passing Concurrency** | Interaction occurs via explicit message exchange between isolated entities | Processes/actors + channels/mailboxes | CSP (Occam, Go channels), Actor Model (Erlang, Akka) |
| **Event-Driven Concurrency** | Computation advances in response to events via handlers or callbacks | Event loop + non-blocking I/O | Node.js, libuv, GUI event systems |
| **Async/Await (Structured Asynchrony)** | Asynchronous tasks composed with structured control flow | Futures/Promises + suspension points | Python `asyncio`, C# `async/await`, JavaScript |
| **Dataflow Concurrency** | Execution driven by data availability rather than control flow | Data dependency graph | TensorFlow graphs, Kahn process networks |
| **Transactional Concurrency** | Concurrent operations composed as atomic transactions | Transactions + conflict detection | Software Transactional Memory (Haskell STM, Clojure STM) |
| **Pipeline / Stream Concurrency** | Computation organized as staged data transformations | Linear or DAG pipelines | Unix pipelines, reactive streams |
| **Reactive Concurrency** | Systems react continuously to streams of events | Observable streams + propagation rules | Rx, ReactiveX, FRP systems |
| **Distributed Concurrency** | Concurrency across address spaces and machines | Message passing + failure model | MPI, microservices, distributed actors |
| Structured Concurrency |  |  |  |

## Concurrency Model Set

> Concurrency for us is multiple multiple in one process.
> 

> **Concurrency**: Many things are making progress at a time.
> 

> Concurrency is the composition of independently executing computations.
> 

> A unit of computation refers to the smallest independent and executable task performed by a computer or computing system.
> 

> A unit of computation refers to the smallest independent and executable task performed by a computer or computing system.
> 

> An **execution unit** is a concurrent entity that carries out tasks independently or cooperatively, such as a thread, process, or coroutine, enabling parallel or asynchronous execution within a program.
> 

> **Execution units** in computer programming are the fundamental entities responsible for carrying out tasks and operations.
> 

> A **concurrency model** is a set of principles that govern how multiple tasks or processes can be executed simultaneously and interact with each other within a software system.
> 

> **Concurrency models** provide a systematic approach or paradigm for handling and coordinating multiple tasks or processes that can execute simultaneously, ensuring efficient and synchronized execution in software systems.
> 

> **Reactive Programming**: It deals with asynchronous data streams and provides a way to react to changes or events as they occur.
> 

### Characterization

| **Aspect** | **Description** | **Case(s)** |
| --- | --- | --- |
| **Paradigm** | Conceptual worldview that frames how concurrency is expressed and reasoned about | Shared-memory (Threads), Message-passing (CSP, Actors), Event-driven (Async/Await), Transactional (STM) |
| **Units of Computation** | Fundamental concurrently executing entities | Threads, Processes, Actors, Goroutines, Tasks |
| **Composition & Structure** | Rules for assembling concurrent entities into larger systems | Thread pools; process networks (CSP); actor hierarchies; structured concurrency scopes |
| **Execution Model** | Scheduling, progress, and execution semantics | Preemptive (threads); cooperative (async); run-to-completion (actors); transactional retries (STM) |
| **Core Abstraction** | Central construct exposed by the model | Thread; Channel; Actor; Future/Promise; Transaction |
| **Interaction & Communication** | How information flows between concurrent entities | Shared variables; synchronous channels; asynchronous messages; event callbacks |
| **Coordination & Synchronization Primitives** | Mechanisms to control ordering, mutual exclusion, or dependency | Locks, semaphores, barriers; rendezvous; message ordering; `await` |
| **Memory Model** | Visibility, consistency, and ordering guarantees | Sequential consistency; weak/relaxed (C++/Java); isolation via immutability (Actors); transactional consistency (STM) |
| **Fault Isolation** | Scope and containment of failures | Process isolation; actor-level isolation with supervision; shared-state failure propagation |
| **Correctness Criteria** | Formal and informal properties defining correct behavior | Data-race freedom; deadlock freedom; linearizability; eventual progress; protocol conformance |

### **Units of Computation**

> See more in [Unit of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/unit-of-computation.md).
> 

| **Unit** | **Description** | **Type** | **Use Case** |
| --- | --- | --- | --- |
| **Thread** |  | OS-level execution unit | Lightweight, shares process memory, suitable for parallel tasks within a process |
| **Process** |  | Independent OS execution context | Heavyweight, isolated address space, suitable for strong fault isolation |
| **Actor** |  | Logical concurrent entity (Actor Model) | Encapsulates state, communicates via asynchronous messages, fault-tolerant via supervision |
| **Goroutine** |  | Lightweight thread (Go runtime) | Extremely lightweight, multiplexed onto OS threads, efficient for large numbers of concurrent tasks |
| **Task** |  | Abstract concurrent unit | General unit for async execution (e.g., futures/promises), often used in structured concurrency |

### Space

| **Model** | **Paradigm** | **Core Abstraction** | **Execution Model** | **Coordination** | **Memory Model** | **Fault Isolation** | **Use Cases / Languages** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Threads + Locks** | Concurrency | Threads + mutexes | Preemptive | Shared state, explicit synchronization | Shared memory | Weak | C, C++, Java, POSIX, OS Kernels |
| **Message Passing (MP)** | Concurrency / Distributed | Isolated processes | Explicit coordination | Send/receive primitives | No shared state | Strong | MPI, ZeroMQ, OpenMPI |
| **Actor Model** | Distributed / Asynchronous | Actors with mailboxes | Event-driven | Asynchronous messages | Encapsulated state | Strong | Erlang, Akka, Elixir |
| **Communicating Sequential Processes (CSP)** | Concurrency | Processes + channels | Blocking I/O | Rendezvous / synchronous channels | No shared memory | Medium | Go, Occam, Rust (crossbeam) |
| **π-Calculus / Join Calculus** | Theoretical Concurrency | Mobile processes / joins | Algebraic transitions | Name-passing, join patterns | No shared state | Strong | JoCaml, Nomadic Pict |
| **Fork/Join Model** | Parallelism | Forkable tasks + join barriers | Task-based / Fork-Join | Implicit join | Shared memory | Weak | Java ForkJoin, .NET TPL, OpenMP |
| **Software Transactional Memory (STM)** | Concurrency (Functional) | Memory transactions | Optimistic concurrency | Rollback, commit/abort | Shared memory with rollback | Weak | Haskell STM, Clojure |
| **Dataflow Model** | Parallelism / Declarative | Data dependency graph | Token-based firing on data availability | Implicit synchronization | Stateless or SSA-like | Strong | TensorFlow, LabVIEW, Faust |
| **Reactive / Event-Driven** | UI / Functional | Events, loops, handlers | Callback-based | Futures, Promises, Signals | Global or scoped state | Medium | JavaScript, Elm, RxJS, React |
| **Green Threads / Coroutines** | Cooperative Concurrency | Lightweight coroutines | Manual yield/resume | Cooperative queues or shared memory | Shared or isolated stacks | Weak | Lua, Python (asyncio), Kotlin |
| **Structured Concurrency** | Deterministic Concurrency | Scoped concurrency blocks | Fork-Join with lifetime management | Scoped joins | Structured shared memory | Stronger | Kotlin, Rust (async-scoped), Java Loom |
| **Petri Nets** | Graph-Theoretic / Formal | Places + transitions + tokens | Token transitions | Graph-based rules | Implicit state | Strong | CPN Tools, TINA |
| **Reo Model** | Channel-based Coordination | Connectors + constraints | Connector-driven | Constraint-based, context-sensitive | Encoded semantics | Strong | Coordination tools, Reo |
| **Tuple Spaces (Linda)** | Associative Memory | Shared space of tuples | Pattern-driven | Out/in, pattern matching | Shared blackboard memory | Medium | JavaSpaces, TSpaces |
| **Kahn Process Networks (KPN)** | Functional / Streaming | Deterministic processes + FIFO | Blocking reads, non-blocking writes | Dataflow blocking | No global state | Strong | StreamIt, Lucid |
| **Statecharts / Sync Reactive** | Reactive / Model-based | Hierarchical states + transitions | Step-wise synchronous | Events + transitions | Internal variables | Medium | Simulink, SCXML, Esterel |
| **Bigraphs (Milner)** | Graphical / Topological | Nodes + connectivity | Graph rewrite systems | Structural transitions | No memory model | Strong | Formal modeling tools |
| **Event-B** | Refinement / Formal | Events on state machines | Guarded transitions | Event atomicity | Abstract state | Strong | B-Method tools, Atelier-B |
| **Cellular Automata** | Grid / Formal Systems | Local cell states + update rules | Synchronous grid update | None (local rules) | Local neighborhood memory | Strong | Game of Life, CA simulators |
| **CHAM (Chemical Abstract Machine)** | Rewriting Systems | Molecules + reaction rules | Rule-based multiset rewriting | Chemical-style reaction rules | Abstract global memory | Strong | Gamma Language, theoretical models |
| **MapReduce / BSP** | Parallelism | Map/reduce + supersteps | Bulk synchronous processing | Implicit shuffle / barrier | Shared-nothing memory | Strong | Hadoop, Spark, Dryad |
| **CRDTs / Event Sourcing** | Eventual Consistency | Logs or mergeable replicated data types | Eventually consistent updates | Conflict-free merging | Append-only logs or CRDTs | Strong | Riak, Akka Persistence, Lasp |
| **TTA (Time-Triggered Architecture)** | Real-Time / Embedded | Periodic time slots | Globally synchronized steps | Pre-scheduled messages | Isolated memory per component | Strong | Avionics, TTP |
| **Deterministic Concurrency / Race-Free** | Safe-by-Design Concurrency | Language-enforced safe interleaving | Static scheduling or async | Ownership, structured concurrency | Strong type + ownership model | Strong | Rust (Send/Sync), Pony |
| **SIMD (Single Instruction, Multiple Data)** | Instruction-Level Parallelism | Vector operations | Parallel vector execution | Implicit via hardware registers | Local registers | Strong | CUDA, AVX, SSE |
| **MIMD (Multiple Instruction, Multiple Data)** | Hardware Parallelism | Independent cores / instruction streams | Hardware multi-threading | Mixed (sync primitives or async) | Shared or distributed | Strong | CPUs, GPUs, multicore processors |
| **Task Graph / DAG Scheduling** | Parallelism / Workflow | DAG of tasks | Scheduler-driven | Dependency-aware | Shared memory or distributed | Medium | Dask, TensorFlow, LLVM |
| **Transactional DAGs** | Parallelism | DAGs + rollback zones | Parallel execution + compensation | Atomic task groups | Shared or isolated memory | Medium | Ray, Prefect, Airflow |

## Correctness & Validation

> How to Reason About Correctness in Concurrent  Systems? How to specify the meaning of correctness in a given Concurrency System? How to validate a concurrency system?
> 

> Correctness in a concurrency system is typically defined by the following properties:
> 

> See [Consistency](note.html?n=technica/computation/dependability/consistency.md).
> 

### Specification

| **Strategy** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Property-Based Specification** | Correctness is defined as a set of explicit properties that executions must satisfy (safety, liveness, ordering, visibility, etc.). | Mutual exclusion, deadlock freedom, linearizability, causal consistency |
| **Invariant-Based Specification** | Correctness is expressed as state predicates that must hold in all reachable system states, independent of interleaving. | Resource conservation, protocol state invariants, balance constraints |
| **State-Machine Specification** | System behavior is defined as a transition system; correctness means all executions conform to the allowed transitions. | Automata models, protocol specifications, Promela/Spin |
| **History-Based Specification** | Correctness is defined over execution histories (invocation/response traces), not internal states. | Linearizability, sequential consistency |
| **Refinement-Based Specification** | A concrete concurrent implementation is correct if it refines an abstract specification. | Lock-free data structures refining atomic specs |
| **Contract-Based Specification** | Components expose correctness via preconditions, postconditions, and guarantees under concurrency assumptions. | Concurrent ADTs, API-level correctness |
| **Temporal Logic Specification** | Correctness properties are expressed over time using modal operators. | LTL/CTL safety and liveness formulas |
| **Equivalence-Based Specification** | A system is correct if its observable behavior is equivalent to a reference model. | Observational equivalence, bisimulation |
| **Consistency-Model Specification** | Correctness is defined by visibility and ordering guarantees across concurrent observers. | Sequential consistency, causal consistency, eventual consistency |
| **Failure-Aware Specification** | Correctness is defined relative to failure models and recovery semantics. | Crash consistency, exactly-once processing |

### Verification

> Concurrency theory also involves techniques for verifying the correctness of concurrent systems:
> 
1. **Model Checking**: Exhaustively explores all possible states of a system to verify properties like
safety (e.g., no deadlocks) and liveness (e.g., eventual progress).
2. **Theorem Proving**: Uses formal logic to prove that a system satisfies certain properties.
3. **Static Analysis**: Analyzes code without executing it to detect potential concurrency issues like data races.
4. **Testing**: Techniques like stress testing and randomized scheduling to uncover concurrency bugs.

## Performance & Scalability

> How does concurrent execution affect computational latency and other performance metrics?
> 

## Concurrency Theory

> See more in [Concurrency Theory](note.html?n=technica/computation/concurrency/conceptual-model-coordination/concurrency-theory.md).
> 

## **Practice**

> ….
> 

Design Principles

- Simplicity and structure
- Avoidance of shared state
- Failure containment
- Explicit coordination

### **Fault Tolerance**

> See more in [‣](https://app.notion.com/p/57a6a0bb4bec4f7590dd95f4076ecdf2?pvs=21) and [Fault-Tolerant Design](note.html?n=technica/computation/system/design/computer-system-design-conceptual-model/fault-tolerant-design.md)
> 
- Checkpointing
- Consensus Protocols

Pathologies and Failure Modes

- Race conditions
- Deadlocks and livelocks
- Memory visibility bugs
- Performance collapse

Practical Heuristics

- Common patterns
- Anti-patterns (“Don’ts”)
- Debugging strategies
- Performance considerations

## System Case Study

| **Industry** | **Use Case** | **Type of Concurrent System** | **Examples** |
| --- | --- | --- | --- |
| **Web and Cloud Services** | Scalable web applications | Distributed systems, microservices | Amazon Web Services (AWS), Google Cloud, Kubernetes |
|  | Real-time data processing | Stream processing frameworks | Apache Kafka, Apache Flink, Apache Storm |
|  | Database management | Distributed databases | Cassandra, MongoDB, CockroachDB |
| **Finance** | High-frequency trading | Low-latency distributed systems | Custom trading platforms, FPGA-based systems |
|  | Fraud detection | Real-time stream processing | Apache Spark, Apache Flink |
|  | Blockchain and cryptocurrency | Decentralized consensus protocols | Bitcoin, Ethereum, Hyperledger |
| **Healthcare** | Medical imaging and analysis | Parallel processing (GPU/CPU) | MRI reconstruction, AI-based diagnostics |
|  | Patient monitoring systems | Real-time event processing | IoT-based health monitors, wearable devices |
|  | Drug discovery and genomics | High-performance computing (HPC) | Distributed simulations, DNA sequencing pipelines |
| **Telecommunications** | Network packet processing | Real-time stream processing | 5G networks, SDN (Software-Defined Networking) |
|  | Call routing and management | Distributed systems | VoIP systems, SIP servers |
|  | IoT device communication | Message-passing systems | MQTT, CoAP |
| **Manufacturing** | Industrial automation | Real-time control systems | PLCs (Programmable Logic Controllers), robotics |
|  | Supply chain optimization | Distributed optimization algorithms | SAP ERP systems, warehouse management systems |
|  | Predictive maintenance | Real-time data analytics | IoT sensors, edge computing |
| **Gaming** | Multiplayer online games | Distributed real-time systems | Game servers (e.g., Unity, Unreal Engine) |
|  | Physics simulations | Parallel processing (GPU/CPU) | NVIDIA PhysX, Havok |
|  | Rendering and graphics | GPU-based parallelism | DirectX, Vulkan |
| **Transportation** | Autonomous vehicles | Real-time sensor data processing | Tesla Autopilot, Waymo |
|  | Traffic management systems | Distributed control systems | Smart traffic lights, GPS routing systems |
|  | Ride-sharing platforms | Distributed matching algorithms | Uber, Lyft |
| **Energy** | Smart grid management | Distributed control systems | IoT-based energy monitoring, demand-response systems |
|  | Oil and gas exploration | High-performance computing (HPC) | Seismic data processing, reservoir simulations |
|  | Renewable energy optimization | Real-time data analytics | Wind farm management, solar panel optimization |
| **Retail** | Inventory management | Distributed databases | Walmart, Amazon inventory systems |
|  | Recommendation systems | Real-time data processing | Netflix, Amazon recommendations |
|  | Checkout and payment systems | High-availability distributed systems | Point-of-sale (POS) systems, payment gateways |
| **Entertainment** | Video streaming | Distributed content delivery networks (CDNs) | Netflix, YouTube, Twitch |
|  | Real-time video processing | GPU-based parallelism | Video editing software, live streaming |
|  | Virtual reality (VR) and augmented reality (AR) | Real-time rendering and interaction | Oculus Rift, Microsoft HoloLens |
| **Aerospace** | Flight control systems | Real-time embedded systems | Avionics systems, autopilot software |
|  | Satellite communication | Distributed systems | GPS systems, satellite data processing |
|  | Aircraft design and simulation | High-performance computing (HPC) | Computational fluid dynamics (CFD), finite element analysis (FEA) |
| **Defense** | Surveillance and reconnaissance | Real-time image and video processing | Drone systems, satellite imagery |
|  | Command and control systems | Distributed real-time systems | Military communication networks |
|  | Cybersecurity | Real-time threat detection | Intrusion detection systems (IDS), firewalls |

## QA

- What is the more succinct formulation of the multi-stream instruction coordination problem?
- Why Create Concurrent Systems in the First Place?
- What to Verify About Concurrent Systems?  How to verify Concurrent Systems?
- Explain the concept of atomicity in concurrent systems and how it is achieved in hardware and software.
- What are the trade-offs between fine-grained and coarse-grained locking in concurrent systems?
- How does the memory consistency model of a system affect the behavior of concurrent programs?
- What are the differences between mutexes, semaphores, and condition variables, and when would you use each?
- What is the thundering herd problem, and how can it be avoided in concurrent systems?
- What is the CAP theorem, and how does it influence the design of distributed systems?
- How does the Paxos algorithm achieve consensus in distributed systems, and what are its limitations?
- What is the two-phase commit (2PC) protocol, and why is it considered a blocking protocol?
- How does multi-version concurrency control (MVCC) work, and why is it widely used in modern databases?
- How does the serializable isolation level ensure strict consistency, and what are its performance implications?
- What are the differences between pessimistic and optimistic concurrency control, and when would you choose one over the other?
- What is a race condition, and how can it be detected and prevented in concurrent systems?
- How do software transactional memory (STM) systems simplify concurrent programming, and what are their limitations?
- What is deadlock, and what are the four necessary conditions for it to occur? How can each condition be prevented?
- How does event-driven architecture handle concurrency, and what are its advantages and disadvantages?
- What is vector clocks, and how are they used to track causality in distributed systems?
- How does Amdahl’s Law limit the scalability of concurrent systems, and how can it be mitigated?
- What is false sharing in concurrent programming, and how does it impact performance?
- What is the actor model, and how does it handle concurrency compared to traditional threading models?
- How does the Paxos algorithm achieve consensus in distributed systems, and what are its limitations?
- Compare and contrast Raft and Paxos in terms of ease of understanding, implementation, and performance.
- Explain the concept of wait-free and lock-free algorithms. Can you provide an example of each?

## References

Conceptual Model: Coordination

- [Concurrency](https://en.wikipedia.org/wiki/Concurrency_(computer_science))
- [Tree-Structured Concurrency (yoshuawuyts.com)](https://news.ycombinator.com/item?id=36559030)
- Milne, George, and Robin Milner. "Concurrent processes and their syntax." *Journal of the ACM (JACM)* 26.2 (1979): 302-321.
- [Models for Concurrency](https://www.cl.cam.ac.uk/~gw104/winskel-nielsen-models-for-concurrency.pdf)
- [Goroutines: the concurrency model we wanted all along](https://jayconrod.com/posts/128/goroutines-the-concurrency-model-we-wanted-all-along)
- [A proposal of new concurrency model for Ruby 3](http://www.atdot.net/~ko1/activities/2016_rubykaigi.pdf)
- [The event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop)
- [Tasks, microtasks, queues and schedules](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/)
- [A concurrency C library 10x faster than Golang.](https://github.com/shiyanhui/libcsp)
- [The C11 and C++11 Concurrency Model](https://www.cs.kent.ac.uk/people/staff/mjb211/docs/toc.pdf)
- [Modeling for Concurrency](https://tapoueh.org/blog/2018/07/modeling-for-concurrency/)
- [List of Concurrency Models](https://stackoverflow.com/questions/4153118/list-of-concurrency-models)
- Sassone, Vladimiro, Mogens Nielsen, and Glynn Winskel. “Models for concurrency: Towards a classification.” Theoretical Computer Science 170.1-2 (1996): 297-348.
- Winskel, Glynn, and Mogens Nielsen. “Models for concurrency.” DAIMI Report Series 463 (1993).
- Sassone, Vladimiro, Mogens Nielsen, and Glynn Winskel. “Models for concurrency: Towards a classification.” Theoretical Computer Science 170.1-2 (1996): 297-348.
- Phillips, Iain, and Irek Ulidowski. “Reversibility and models for concurrency.” Electronic Notes in Theoretical Computer Science 192.1 (2007): 93-108.
- [Fiber (computer science)](https://en.wikipedia.org/wiki/Fiber_(computer_science))
- [Protothread](https://en.wikipedia.org/wiki/Protothread)
- [Java Virtual Threads](https://blog.devgenius.io/java-virtual-threads-715c162c6c39)
- [Virtual Threads: New Foundations for High-Scale Java Applications](https://www.infoq.com/articles/java-virtual-threads/)
- [Coroutine](https://en.wikipedia.org/wiki/Coroutine)
- [Futures and promises](https://en.wikipedia.org/wiki/Futures_and_promises)
- [Communicating Sequential Processes](http://www.usingcsp.com/cspbook.pdf)
- The best multicore-parallelization refactoring you’ve never heard of∗ / [https://www.andrew.cmu.edu/user/mrainey/papers/pardefunc.pdf](https://www.andrew.cmu.edu/user/mrainey/papers/pardefunc.pdf)
- Note: Virtual Threads from the conceptual point of view are equal to green threads; the different is in the implementation.
- [What is the difference between green threads and virtual threads?](https://stackoverflow.com/questions/74639116/what-is-the-difference-between-green-threads-and-virtual-threads)
- [Is there a difference between fibers, coroutines and green threads and if that is so what is it?](https://softwareengineering.stackexchange.com/questions/254140/is-there-a-difference-between-fibers-coroutines-and-green-threads-and-if-that-i)
- LMAX’s Disruptor Pattern: The "LMAX's Disruptor Pattern" is a high-performance concurrent event processing pattern that utilizes a ring buffer and careful thread coordination to achieve low-latency, high-throughput data processing.
- Channels:  Data structures communicate and synchronize concurrent processes or coroutines, typically supporting operations like sending and receiving messages.
- https://news.ycombinator.com/item?id=42450227
- https://news.ycombinator.com/item?id=36465085
- https://news.ycombinator.com/item?id=38863339
- https://news.ycombinator.com/item?id=43397640
- https://www.alibabacloud.com/blog/paxos-raft-epaxos-how-has-distributed-consensus-technology-evolved_597127
- https://mwhittaker.github.io/blog/lamports_logical_clocks/
- https://news.ycombinator.com/item?id=35684232
- https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html
- https://en.wikipedia.org/wiki/Multiversion_concurrency_control
- [x86](note.html?n=technica/computation/operating-system/x86.md)
- [‣](https://app.notion.com/p/fe6e9732f0ce4104b49c95bc3e106a70?pvs=21)
- [Instruction Set Architecture (ISA)](note.html?n=technica/computation/language-system/conceptual-model-language-system/instruction-set-architecture-isa.md)
- [Reduced Instruction Set Computer (RISC-V)](note.html?n=technica/computation/language-system/conceptual-model-language-system/reduced-instruction-set-computer-risc-v.md)
- [‣](https://app.notion.com/p/57a6a0bb4bec4f7590dd95f4076ecdf2?pvs=21)
- [Distributed Computing](note.html?n=technica/computation/distributed-computing.md)
- [Real-Time Computing](note.html?n=technica/computation/miscelanea/real-time-computing.md)
- [Language System](note.html?n=technica/computation/language-system.md)
- [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md)
- [Distributed Computing](note.html?n=technica/computation/distributed-computing.md)
- [**Message Delivery Guarantee**](note.html?n=technica/computation/distributed-computing/multi-node-processing-system-conceptual-model/message-delivery-guarantee.md)
- https://en.wikipedia.org/wiki/Cache_coherence
- https://stackoverflow.com/questions/10989403/how-is-x86-instruction-cache-synchronized
- https://stackoverflow.com/questions/2368164/how-is-thread-synchronization-implemented-at-the-assembly-language-level
- https://variantsystems.io/blog/beam-otp-process-concurrency
- [ ]  [‣](https://app.notion.com/p/1c0598edb79080da9c22cde3239e401e?pvs=21)
- [ ]  [‣](https://app.notion.com/p/10e598edb79081faa034f225f0f1e4f2?pvs=21)
- [ ]  [‣](https://app.notion.com/p/1c0598edb79080218e2ee5719e731592?pvs=21)
- [ ]  https://github.com/ailidani/paxi
- [ ]  [](https://app.notion.com/p/1c0c0f5171ec80c7a63ed72734e9fac5?pvs=21)
- [ ]  Hansen, Per Brinch. "Concurrent programming concepts." *ACM Computing Surveys (CSUR)* 5.4 (1973): 223-245.
- [ ]  Hansen, Per Brinch, ed. The origin of concurrent programming: from semaphores to remote procedure calls. Springer Science & Business Media, 2013.
- [ ]  https://en.wikipedia.org/wiki/Parallel_computing