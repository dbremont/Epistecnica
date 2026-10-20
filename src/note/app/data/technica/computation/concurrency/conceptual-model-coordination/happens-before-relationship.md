---
tags: [formal-model]
---

# Happens-before Relationship


> A tool to specify operations ordering semantics.
> 

> In formal terms, the happens-before relationship is a **partial order**, meaning it establishes a hierarchy of events where some events must logically happen before others, while not all events need to be related to one another. The happens-before relation is typically defined in the context of memory models, such as those in programming languages like Java and C++, to define how operations (e.g., reads and writes) on shared variables are ordered across multiple threads.
> 

The **happens-before** relation is a type of **partial order** that establishes constraints on how events should be ordered. In multithreaded programs, this relation helps ensure that operations on shared resources are performed in a predictable and safe manner.

- For example, if thread A writes to a shared variable, and thread B reads from the same variable, the happens-before relationship ensures that the write-in thread A occurs before the read in thread B. This helps avoid scenarios where thread B might read an outdated or inconsistent value.

## Uses

- **Memory Visibility in Multi-threaded Programs**: The happens-before relationship ensures that changes made by one thread are visible to other threads. For example, if thread A writes to a shared variable and thread B reads from it, the happens-before rule guarantees that the write-in thread A happens before the read in thread B.
- **Synchronization Primitives (Locks, Barriers, Semaphores):** Synchronization primitives such as **locks**, **semaphores**, **mutexes**, **barriers**, and **condition variables** use the happens-before relationship to establish order between thread actions.
- **Atomic Operations:**  Certain **atomic operations** in concurrent programming (like atomic variables or memory fences) rely on the happens-before relationship to guarantee that memory updates are propagated in a specific order across threads.
- **Ordering Events in Distributed Systems (Causal Consistency):** In **distributed systems**, happens-before relationships are used to establish causal ordering between events (such as message sends and receives). This helps ensure that causally related events are processed in the correct order across multiple machines or processes.
- **Implementing Sequential Consistency in Systems:** The happens-before relationship is used to define **sequential consistency**, ensuring that the results of a concurrent system are as if the operations were executed in some sequential order, respecting the happens-before order.
- …

## Who Guarantees Happens-Before?

- **The programming language's memory model** (e.g., Java Memory Model, C++ Memory Model).
- **Synchronization primitives** provided by the language or runtime environment (e.g., mutexes, atomic operations, condition variables).
- **The hardware memory model** of the CPU, which enforces memory ordering via techniques like memory barriers.
- **The operating system** that schedules threads and enforces synchronization.

## References

- https://en.wikipedia.org/wiki/Happened-before
- https://stackoverflow.com/questions/63472450/why-is-happens-before-relationship-called-like-that