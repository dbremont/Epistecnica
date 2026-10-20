# Java: 🔄 Computation Flow Primitive

> **In this note,** we will explore Java mechanisms for managing the path of execution (ordering, branching, sequencing) and the **units of execution** (threads, tasks, processes, coroutines, actors) in order to describe complex computations.
> 

> **Path-of-execution mechanisms** are abstract levers that shape, constrain, and make intelligible the unfolding of computation in time, enabling non-linear progressions that enable iteration (repetition), conditional execution, and other dynamic control flows, thereby transforming computation from a rigid sequence into a flexible, adaptive process capable of expressing complex **computational processes**.
> 

## Concurrency Model

### Unit

| **Unit** | **Description** | **Level of Abstraction** | **Lifecycle Control** | **Notes** |
| --- | --- | --- | --- | --- |
| **Thread** | Basic unit of execution mapped (usually) to an OS thread. Each has its own call stack, program counter, and local variables. | Low | Explicit start/stop via `Thread` API | Can be expensive to create/manage in large numbers. |
| **Runnable** | Task abstraction representing a block of code to run (`run()` method). Does not return a value. | Low–Mid | Submitted to a thread or executor | Separates *what to run* from *where to run*. |
| **Callable<T>** | Like `Runnable` but returns a value or throws checked exceptions. | Mid | Submitted to `ExecutorService` → produces `Future<T>` | Integrates with task-based concurrency. |
| **Future / CompletableFuture** | A handle to an asynchronous result of a task. `CompletableFuture` extends this with fluent async composition. | Mid–High | Controlled via callbacks, chaining, cancellation | Key for async programming; enables declarative pipelines. |
| **Executor / ExecutorService** | Framework abstraction to manage task execution (thread pooling, scheduling, lifecycle). | High | Submit tasks, shut down pools | Decouples task submission from execution strategy. |
| **ForkJoinTask / ForkJoinPool** | Work-stealing framework for fine-grained parallelism (divide-and-conquer tasks). | High | Pool manages scheduling automatically | Underpins Java’s parallel streams. |
| **Parallel Stream** | Declarative data-parallel operations on collections/streams, internally backed by ForkJoinPool. | Very High | Implicit (developer specifies `.parallel()`) | Great for data pipelines, less control over tuning. |
| **Virtual Thread** *(Java 19+ / Project Loom)* | Lightweight threads managed by the JVM, not OS. Designed for massive concurrency with simple programming model. | Low (but cheap) | Same as `Thread` API but scaled | Enables millions of concurrent tasks with blocking code style. |
| **Actor (Akka / external libs)** | Message-passing concurrency model (not in core JDK, but widely used in Java ecosystem). | Very High | Managed by runtime/actor system | Avoids shared mutable state; more scalable. |
| **Coroutine (via Loom or Kotlin)** | Cooperative concurrency unit, lighter than threads. Kotlin integrates natively; Loom provides similar in Java. | Very High | Suspended/resumed transparently | Makes async code look synchronous. |

### Property

| **Property** | **Description** | **Notes** |
| --- | --- | --- |
| **Safety** | Guarantees that concurrent execution does not produce incorrect or inconsistent state. Often involves preventing data races. | Using `synchronized`, `ReentrantLock`, or atomic variables in Java. |
| **Liveness** | Ensures that the system makes progress; threads/tasks don’t get stuck indefinitely. | Avoiding deadlocks or livelocks. |
| **Atomicity** | Operations appear indivisible; intermediate states are not visible to other units. | `AtomicInteger.incrementAndGet()`, or critical sections in OS. |
| **Isolation** | The execution of a unit is insulated from interference by others. | Transactional memory or properly synchronized blocks. |
| **Durability (Persistence)** | Changes made by a unit are reliably reflected after completion (mainly in transactional systems). | Less relevant to plain threads, more to database transactions. |
| **Fairness** | Ensures that units get scheduled or executed without starvation. | Java `ReentrantLock(true)` uses fair locking. |
| **Determinism** | Execution produces predictable outcomes under the same inputs. | Hard to guarantee with threads due to scheduler nondeterminism. |
| **Composability** | Units can be safely combined without introducing new concurrency hazards. | Building larger concurrent algorithms from safe primitives. |
| **Scalability** | Performance improves (or at least remains acceptable) when increasing the number of units. | ForkJoinPool scales better than manually managing threads. |
| **Interruptibility (Cancelability)** | Ability to stop, pause, or preempt execution safely. | `Thread.interrupt()`, `Future.cancel()`. |
| **Recoverability (Exception Safety)** | Unit can handle exceptions without leaving shared state inconsistent. | Using try-finally or transactional rollback mechanisms. |

### Control Mechanism

> A **control mechanism** is a construct or tool that regulates the interaction between multiple units of execution (threads or processes) to **ensure correct, predictable, and safe access to shared resources**. It manages **mutual exclusion**, **coordination**, **ordering**, and **visibility** of operations to prevent race conditions, deadlocks, and inconsistent states.
> 

> Note: We need a specification of what it means to be correct, predictable, and safe when dealing with shared resources, along with a specification of the shared resources themselves.
> 

**Key aspects:**

1. **Mutual Exclusion** – Ensures that only one thread accesses a critical section at a time.
2. **Coordination / Synchronization** – Enables threads to wait for or signal each other to maintain correct sequencing.
3. **Visibility** – Guarantees that changes made by one thread are observable by others in a consistent manner.
4. **Atomicity** – Provides indivisible operations that cannot be interrupted mid-execution.

| Category | Mechanism | Description | JVM Implementation |
| --- | --- | --- | --- |
| **Intrinsic Lock (Monitor)** | `synchronized` | Built-in locking for methods or blocks, ensures mutual exclusion. | Each object has a monitor; JVM acquires/releases it and uses thin/fat locks depending on contention. |
|  | `wait()` / `notify()` / `notifyAll()` | Used with synchronized blocks for classic monitor coordination. | Threads are placed in a monitor wait set; `wait()` releases the monitor, `notify()` wakes a thread. |
| **Explicit Lock** | `ReentrantLock` | Explicit mutual exclusion lock with advanced features (tryLock, timed lock). | Built on AbstractQueuedSynchronizer (AQS) with a FIFO queue and owner tracking. |
|  | `ReentrantReadWriteLock` | Separate read and write locks to improve concurrency for read-heavy workloads. | Uses AQS with separate counters for read and write locks; readers may proceed concurrently. |
|  | `StampedLock` | Optimized read/write lock with support for optimistic reads. | Tracks a version stamp for optimistic reads; falls back to blocking if conflicts detected. |
|  | `LockSupport` | Low-level park/unpark mechanism for building custom synchronizers. | Parks threads in JVM using OS-level primitives (e.g., futex) and resumes via unpark. |
| **Synchronizer** | `Semaphore` | Controls concurrent access to a resource with permits. | Uses AQS; decrements permits atomically and parks threads if none are available. |
|  | `CountDownLatch` | Wait for a fixed number of events before proceeding. | Maintains a counter and parks waiting threads until it reaches zero. |
|  | `CyclicBarrier` | Allows a group of threads to wait for each other at a barrier point; reusable. | Uses AQS to block threads until all participants arrive, then releases them. |
|  | `Phaser` | Advanced version of CyclicBarrier with dynamic participants and phases. | Maintains phase counters and dynamically tracks registered parties using AQS queues. |
|  | `Exchanger` | Allows two threads to exchange objects at a synchronization point. | Uses internal nodes and AQS queues to match and exchange objects between two threads. |
| **Lock-Free Primitive** | `AtomicInteger`, `AtomicLong`, `AtomicReference`, etc. | Provides lock-free, thread-safe operations on single variables. | Uses CPU atomic instructions (CAS) via `Unsafe` for lock-free updates. |
|  | `AtomicIntegerArray`, `AtomicLongArray`, `AtomicReferenceArray`, `AtomicMarkableReference`, `AtomicStampedReference` | Lock-free operations on arrays or with metadata (mark/stamp). | Built on CAS loops using `Unsafe` for atomic updates. |
|  | `VarHandle` | Low-level, flexible atomic operations on fields, array elements, and memory locations. | JVM maps `VarHandle` to CPU atomic instructions; can implement compareAndSet, getAndSet, etc. |
| **Thread Coordination** | `Thread.join()` | Waits for a thread to terminate. | Blocks the calling thread until the target thread completes execution. |
|  | `Future` / `CompletableFuture` | Asynchronous result container; supports waiting, timeout, chaining, and combining tasks. | Encapsulates tasks and blocks or schedules threads as needed; completion updates state atomically. |
|  | `ExecutorService.invokeAll()` / `invokeAny()` | Executes multiple tasks with built-in coordination and optional timeout. | Submits tasks to a thread pool; uses internal queues and blocking for coordination. |
|  | `ForkJoinPool` / `RecursiveTask` / `RecursiveAction` | Framework for parallel divide-and-conquer tasks; supports work-stealing. | Uses lightweight worker threads; manages task queues and steals tasks from other workers. |
| **Visibility Control** | `volatile` | Guarantees visibility of changes to a variable across threads; prevents instruction reordering for that variable. | Inserts memory barriers to enforce read/write visibility and prevent instruction reordering. |
|  | `final` fields | Guarantees safe publication of immutable objects. | JVM ensures initialization safety; readers see fully initialized values. |
| **Thread-Local Storage** | `ThreadLocal<T>` | Provides each thread with its own independent value. | Stores values in a per-thread map inside the Thread object, avoiding shared access. |
| **Concurrent Collections** | `ConcurrentHashMap`, `ConcurrentLinkedQueue`, `ConcurrentSkipListMap`, `LinkedTransferQueue` | Thread-safe collections and queues for coordination without explicit locks. | Uses internal fine-grained locks, CAS, and other non-blocking algorithms. |
| **Other / Advanced** | `PhantomReference` / `WeakReference` | Can be used in advanced scenarios for memory-sensitive thread coordination. | JVM tracks references and enqueues them in reference queues when garbage collected. |

## **Thread**

> A **thread** is a lightweight unit of execution within a process. Java threads are **mapped to native OS threads** (usually) through the Java Virtual Machine (JVM). Threads allow concurrent execution within a single process.
> 

### Lifecycle

| State | Description |
| --- | --- |
| `NEW` | Created but not started (`start()` not called) |
| `RUNNABLE` | Ready to run, waiting for CPU time |
| `BLOCKED` | Waiting for a monitor lock |
| `WAITING` | Waiting indefinitely for another thread (via `Object.wait()`) |
| `TIMED_WAITING` | Waiting for a specified time (`sleep`, `join`) |
| `TERMINATED` | Finished execution |

### **Scheduling**

- Java relies on **OS thread scheduler**.
- Thread **priority** (`Thread.MIN_PRIORITY` to `Thread.MAX_PRIORITY`) is a **hint**, not a guarantee.
- Preemptive scheduling is OS-dependent.
- Threads can be:
    - **Cooperative**: voluntarily yield (`Thread.yield()`)
    - **Preemptive**: OS interrupts and switches threads automatically.

### Execution Environment

> What happens when several processes (units of execution) operate on the same resources?
> 

1. Java’s **Memory Model (JMM)** defines visibility rules for threads:
    - **Volatile variables**: ensure visibility across threads.
    - **Synchronized blocks/methods**: ensure atomic access and visibility.
2. **Stack & Heap**
    - Each thread has **private stack memory** (local variables).
    - Threads share **heap memory** (object fields, arrays).
3. **Context Switching**
    - Switching threads involves saving/restoring **CPU registers** and stack pointer.
    - Expensive compared to sequential execution, but lightweight compared to processes.
4. **Atomic Units of Execution**
    - Instructions like reading/writing a `long` or `double` may not be atomic on all platforms.
    - Use `synchronized` or `Atomic*` classes for safe operations.

## **Path-of-execution Mechanism**

> 

| **Mechanism** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Sequential Execution** | The default control flow where statements are executed one after another in the order they appear. | `int a = 5; int b = a + 2;` |
| **Conditional Statements** | Control flow changes based on conditions, allowing branches in code execution. | `if (x > 10) { ... } else { ... }` |
| **Switch Statement** | Provides a way to execute different parts of code based on the value of a variable or expression. | `switch (day) { case MONDAY: ... break; }` |
| **Loops** | Repeat a block of code multiple times based on a condition or a counter. | `for (int i = 0; i < 10; i++) { ... }`<br>`while (condition) { ... }`<br>`do { ... } while (condition);` |
| **Break Statement** | Exits from the nearest enclosing loop or switch statement, terminating its execution. | `break;` |
| **Continue Statement** | Skips the current iteration of the nearest enclosing loop and proceeds to the next iteration. | `continue;` |
| **Return Statement** | Exits from the current method and optionally returns a value to the caller. | `return value;` |
| **Exception Handling** | Manages errors and exceptional conditions using `try`, `catch`, `finally`, and `throw` keywords. | `try { ... } catch (Exception e) { ... } finally { ... }` |
| **Threads** | Allow concurrent execution of code by running multiple threads in parallel, each with its own stack and execution path. | `Thread t = new Thread(() -> { ... }); t.start();` |
| **Virtual Threads** | Lightweight threads introduced in Java 19 that are designed for high-throughput concurrent applications, offering better scalability and reduced resource overhead compared to traditional threads. | `var vt = Thread.ofVirtual().start(() -> { ... });` |
| **Labeled Statements** | Provides labels to blocks of code, which can be used with `break` and `continue` to control flow in nested loops. | `outer: for (...) { ... } inner: for (...) { break outer; }` |
| **Exception Propagation** | Exceptions can be thrown from methods and propagated up the call stack to be handled by calling methods. | `throw new IllegalArgumentException("Invalid input");` |

## **❌** Error Handling

> How the language manages runtime errors?
> 

> In Java, error handling is the mechanism of detecting, propagating, and managing exceptional conditions using **`try-catch-finally` blocks**, **`throw` statements**, and **checked/unchecked exceptions** to maintain program stability and control flow.
> 

## Performance

> See more in Java: ⚡Performance.
> 

| **Unit** | **Overhead (Cost)** | **Context Switch** | **Memory Footprint** | **Scalability** | **Typical Use** |
| --- | --- | --- | --- | --- | --- |
| **Thread (`java.lang.Thread`)** | High creation/destruction cost (kernel thread) | High; OS-level context switch | Moderate (~1 MB stack default) | Limited by OS thread count | Long-lived, blocking operations, full concurrency |
| **Runnable / Callable + ExecutorService** | Moderate; pooled threads amortize cost | Moderate; depends on pool | Low per task (uses existing threads) | High; thread pools scale better than raw threads | Short-lived tasks, async processing |
| **ForkJoinTask / ForkJoinPool** | Low to moderate; lightweight task splitting | Low; work-stealing avoids many OS switches | Low; tasks are small | Very high; designed for fine-grained parallelism | Divide-and-conquer, CPU-bound tasks |
| **CompletableFuture / Future** | Low; mostly wrapping tasks | Low; non-blocking chaining avoids context switch | Low | High; async, non-blocking composition | Async workflows, event-driven pipelines |
| **Virtual Thread (Project Loom)** | Very low; user-mode scheduling | Very low; managed by JVM | Very low (~10 KB stack) | Extremely high; millions of virtual threads possible | High-concurrency workloads, I/O-heavy servers |
| **Actor (Akka / Quasar fibers)** | Low to moderate; mailbox overhead | Very low; fiber-scheduled | Low | High; actors scale horizontally | Message-driven concurrency, reactive systems |
| **Coroutines (via Kotlin / Quasar)** | Very low; lightweight stack | Very low; JVM-managed | Low | High; millions of coroutines feasible | Async I/O, fine-grained concurrency |

## Case Study

> See more in https://github.com/dbremont/language-system-labs.
> 

## QA

- What are the **happens-before relationships** in Java Memory Model (JMM)? How do `volatile`, `synchronized`, and `final` relate to it?
- Explain **linearizability** and **sequential consistency**. How do `AtomicInteger` operations ensure linearizability?
- Compare **lock-based vs lock-free** programming. When is each approach preferable?
- How does a **monitor (`synchronized`)** work internally in the JVM? What are **thin locks, inflated locks, and biased locking**?
- How does `ReentrantLock` differ from `synchronized` in **fairness guarantees, reentrancy, and interruptibility**?
- Explain `ReentrantReadWriteLock` and `StampedLock` **optimistic reads**. How does the JVM detect and resolve conflicts?
- Describe the **lifecycle of a `CountDownLatch`** or `CyclicBarrier`. How does the JVM park and unpark threads internally?
- What is the difference between **`LockSupport.park()`** and **`Object.wait()`** at the JVM and OS level?
- How do **`ThreadLocal` variables** work under the hood? How does this impact memory and garbage collection?
- Explain **compare-and-swap (CAS)** and **ABA problem**. How does Java handle ABA issues in `AtomicStampedReference`?
- Describe **false sharing** in lock-free algorithms. How can padding prevent it?
- How does **`ForkJoinPool`** implement **work-stealing**? What are the trade-offs vs thread pools?
- How does **biased locking** improve uncontended performance? When is it revoked?
- What happens in the JVM when a thread calls **`park()` or `unpark()`**? How is it mapped to OS primitives (e.g., futex on Linux)?
- How does **thread scheduling** interact with Java’s `Thread` priorities and **OS thread scheduling**?
- How would you **design a lock-free multi-producer/multi-consumer queue** in Java? What atomic primitives and memory barriers would you use?
- How would you **implement a concurrent LRU cache** in Java ensuring thread-safety and minimal contention?
- How do **false sharing, cache coherence, and NUMA architecture** influence high-performance Java concurrency design?
- How would you **prove correctness** of a Java concurrent algorithm using **happens-before** and **linearizability** reasoning?
- How do you **measure the cost of `synchronized` vs `ReentrantLock`** under high contention? What JVM flags or profilers would you use?
- Design experiments to **stress-test atomic operations** under heavy thread contention. What metrics would you record?
- What **common concurrency bugs** exist in Java? How do you detect and fix them (e.g., using ThreadSanitizer or Java Flight Recorder)?
- What optimizations are applied to control flow?
- How are recursive algorithms optimized?
- What is the cost of context switching (e.g., coroutines vs. threads)?
- How are stack traces generated?
- How are exceptions implemented?

## References

- [Concurrency](note.html?n=technica/computation/concurrency.md)
- [Notion of Change](note.html?n=technica/computation/language-system/conceptual-model-language-system/notion-of-change.md)
- [Unit of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/unit-of-computation.md)
- [Exception Handling System](note.html?n=technica/computation/language-system/conceptual-model-language-system/exception-handling-system.md)
- Memory Model
- https://news.ycombinator.com/item?id=12256220