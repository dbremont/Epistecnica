---
tags: [unit-of-computation]
---

# Schedule


> A **schedule** refers to the sequence of operations or transactions that are executed by the system. These operations may be performed by multiple nodes or processes, and the order in which they are executed can have a significant impact on the correctness and consistency of the system.
> 

> A **schedule** is said to be serializable if it produces the same result as a serial execution of the transactions, where each transaction is executed one after the other in some predetermined order. In other words, a serializable **schedule** ensures that the system behaves as if only one transaction is executing at any given time, even though multiple transactions may be executing concurrently.
> 

> Ensuring serializability in a distributed system can be challenging due to the potential for conflicts and inconsistencies that can arise when multiple nodes or processes are accessing shared resources or data. To achieve serializability, distributed systems typically use some form of concurrency control, such as locking or timestamp-based protocols, to ensure that transactions are executed in a consistent and correct order.
> 

## References

- …