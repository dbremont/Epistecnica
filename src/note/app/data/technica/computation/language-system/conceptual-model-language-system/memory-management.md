---
tags: [language-system]
---

# Memory  Management

- [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md), [Interpreter System](note.html?n=technica/computation/language-system/conceptual-model-language-system/interpreter-system.md), [Type System](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-system.md), [Resource Lifetime](note.html?n=technica/computation/language-system/conceptual-model-language-system/resource-lifetime.md), [Resource Management](note.html?n=technica/computation/language-system/conceptual-model-language-system/resource-management.md)

> A  **memory model** is an abstraction that defines how **memory operations** (such as reads and writes) interact with each other in a **concurrent or multi-threaded system**.
> 

> The memory model specifies the **rules and guarantees for the visibility of memory changes** made by one thread to other threads.
> 

> **Memory Ordering**: Determines the order in which memory operations are executed, ensuring consistent results across threads. [Rules]
> 

> Atomicity:  Ensures that a memory operation (read/write) is indivisible, meaning it happens in a single, uninterrupted step. [Guarantees]
> 

> Memory Fences: Enforces specific ordering constraints on memory operations, preventing reordering across different memory locations. [Implementation]
> 

> Synchronization Mechanisms: Methods for coordinating memory accesses between threads to prevent race conditions and ensure correct ordering of operations.. [Mechanism]
> 

> Release/Acquire Semantics:  Specifies how one thread's actions can influence the memory operations of other threads, ensuring data is visible at the right time. [Mechanism]
> 

## Structure

| **Category** | **Aspect** | **Description** |
| --- | --- | --- |
| **Memory Allocation and Deallocation** | Stack memory | Automatic allocation for function calls, local variables, and activation records; typically LIFO-managed. |
|  | Heap memory | Dynamic allocation for objects, data structures, and closures; managed manually or via garbage collection. |
|  | Static/Global memory | Memory reserved for global/static variables, usually for the program lifetime. |
| **Memory Access** | Addressable locations | Pointers/references to memory locations. |
|  | Safety mechanisms | Bounds checking or memory safety enforcement. |
|  | Performance considerations | Cache alignment, memory locality, and access optimization. |
| **Lifetime and Scope** | Stack-based | Local variables exist only during function execution. |
|  | Heap-based | Objects persist until explicitly freed or garbage collected. |
|  | Static/global | Exist for the entire program duration. |
| **Garbage Collection / Resource Management** | Automatic reclamation | Reference counting, tracing (mark-and-sweep, generational GC). |
|  | Deterministic cleanup | Destructors or finalizers. |
| **Concurrency Considerations** | Thread-local vs shared | Memory accessible only to a thread vs shared among threads. |
|  | Synchronization | Locks, mutexes, atomic operations to prevent race conditions. |
|  | Visibility guarantees | Rules for when changes made by one thread become visible to others. |
|  | Ordering guarantees | Rules for the order in which memory operations are seen by threads (memory consistency). |
| **Optimization Techniques** | Allocation strategies | Pool allocation, copy-on-write, stack allocation for short-lived objects. |
|  | Analysis | Escape analysis to determine if heap allocation is necessary. |
|  |  |  |

## Happens-Before Relationship

> Establishes a causal relationship between memory operations, specifying that one operation (e.g., a write) must happen before another (e.g., a read). [Rule]
> 

> What is the used? The **Happens-Before (HB) relationship** is **used by the language memory model and synchronization mechanisms** to **guarantee visibility and ordering of memory operations** between threads. In a formal fill-in-the-blanks style:
> 

## Case Study(s)

| **Memory Model** | **Description** | **Consistency Guarantees** | **Visibility Guarantees** | **Ordering Guarantees** | **Synchronization Mechanisms** | **Thread Interaction** |
| --- | --- | --- | --- | --- | --- | --- |
| **C++ Memory Model** | Defines how concurrent operations (e.g., reading and writing to shared variables) behave in multi-threaded programs. | Ensures that threads see consistent data under specific synchronization rules. | Controls visibility of atomic variables and the memory states across threads. | Sequential consistency or relaxed ordering based on `std::atomic` and fences. | Mutexes, atomic operations, memory fences. | Threads communicate through synchronization primitives (locks, condition variables). |
| **Java Memory Model (JMM)** | Provides rules for how threads interact with memory and ensures visibility of shared variables between threads. | Ensures visibility and ordering between synchronized blocks or volatile variables. | Guarantees visibility through `volatile` and synchronization blocks. | Happens-before relationship ensures ordering between synchronized methods. | Synchronized blocks, `volatile` variables, locks. | Threads synchronize explicitly through `synchronized` blocks or volatile variables. |
| **Sequential Consistency** | Requires that all memory operations appear to be executed in a single, consistent order, providing strong guarantees for memory visibility. | Strong consistency with a single order of execution for all threads. | Strong visibility guarantees—everyone sees operations in the same order. | All operations (loads and stores) are strictly ordered in the same sequence. | No additional synchronization mechanisms needed; relies on strict ordering. | All threads see the same execution order without reordering. |
| **Relaxed Consistency** | Allows for more flexibility, letting threads observe memory operations out of order for improved performance, but without compromising on critical synchronization. | Provides weak consistency across threads. | Visibility is not guaranteed across threads unless synchronization occurs. | Relaxed memory ordering, often used with memory fences. | Synchronization mechanisms like locks or memory fences are required to enforce visibility. | Threads can perform operations out of order for performance benefits. |
| **Release Consistency** | A memory model that allows writes to be visible to other threads only after certain synchronization points (like acquiring locks or barriers). | Ensures that writes are visible only after release operations. | Synchronization points (release/acquire) control visibility. | Ordering is guaranteed around synchronization points, but not globally. | Uses acquire-release semantics to enforce consistency at synchronization points. | Threads synchronize via acquire-release operations to ensure proper visibility. |
| **Total Store Order (TSO)** | A memory model in which stores (writes) are guaranteed to be observed in the same order across all threads, but loads (reads) can be reordered. | Guarantees consistency for stores but allows flexibility for loads. | Visibility of store operations is guaranteed in order; loads can be reordered. | Write operations are strictly ordered, but reads can be reordered for performance. | May use memory barriers to enforce store ordering. | Store operations across threads are seen in the same order. |
| **Causal Consistency** | Allows for memory reordering, but ensures that causally related operations (such as dependent reads and writes) are observed in the same order by all threads. | Allows reordering but ensures causally related operations are visible in order. | Operations are visible in a way that respects causal dependencies, but not all operations need to be visible in real time. | Reordering of non-causal operations is allowed; causal ones remain ordered. | Requires additional synchronization to ensure causal consistency is maintained. | Threads interact via causal relationships and need synchronization for causality. |
| **Weak Consistency** | Guarantees memory consistency only at synchronization points. Between these points, operations may be observed in any order, allowing significant flexibility. | Consistency only guaranteed at synchronization points. | Operations are visible across threads only at synchronization points (e.g., barriers, locks). | No global ordering of operations; synchronization points enforce visibility. | Synchronization primitives (locks, barriers) are needed to enforce consistency. | Threads can perform operations out of order, leading to possible inconsistencies. |
| **Eventual Consistency** | Often used in distributed systems, where it is guaranteed that, given enough time, all replicas of data will eventually converge to the same value. | No immediate consistency, but guarantees eventual convergence. | Operations are visible at different times across threads or nodes, but will converge eventually. | No strict ordering, but ensures eventual consistency. | Synchronization is needed across nodes, but consistency is not immediate. | Used in distributed systems where data is eventually synchronized across nodes. |
| **Transactional Memory** | Allows concurrent programs to execute transactions on shared memory without traditional locking, simplifying the development of parallel programs. | Guarantees atomicity, consistency, and isolation (ACID properties). | Provides visibility for transactions as a whole, ensuring consistency across threads. | Guarantees atomicity and isolation, with operations appearing atomic across threads. | Uses transaction management to handle consistency, eliminating the need for traditional locks. | Threads execute as transactions; memory writes are isolated until commit. |

## References

- https://en.wikipedia.org/wiki/Memory_model_(programming)
- https://research.swtch.com/mm
- https://en.wikipedia.org/wiki/X86_memory_models
- https://dl.acm.org/doi/10.1145/1229428.1229469
- [Memory Allocation](https://samwho.dev/memory-allocation/)
- Tofte, Mads, and Jean-Pierre Talpin. "Region-based memory management." Information and computation 132.2 (1997): 109-176.
- Henglein, Fritz, Henning Makholm, and Henning Niss. "Effect types and region-based memory management." Advanced Topics in Types and Programming Languages (2005): 87-135.
- [Happens-before Relationship](note.html?n=technica/computation/concurrency/conceptual-model-coordination/happens-before-relationship.md)