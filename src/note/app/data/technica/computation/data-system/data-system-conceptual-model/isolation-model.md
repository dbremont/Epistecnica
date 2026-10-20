---
tags: [specification]
---

# Isolation Model

- [Concurrency Control](note.html?n=technica/computation/data-system/data-system-conceptual-model/concurrency-control.md)

> In this note we will explore  a central idea in data system - Isolation Model - and Isolation Level.
> 

> An **isolation model  (level)** is essentially the concrete consistency guarantee that a data system provides for a transaction.
> 

## Isolation Level Set

| **Isolation Level** | **Description** | **How it is Implemented?** |
| --- | --- | --- |
| **Read Uncommitted** | A transaction may read changes made by other transactions before those changes are committed. Dirty reads, non-repeatable reads, and phantom reads are possible. | Typically by **allowing reads to ignore write locks** / not enforcing sufficient read-write synchronization. |
| **Read Committed** | A transaction only reads data that has been committed. Dirty reads are prevented, but the same query may return different results if another transaction commits changes between executions. | Usually through **short-lived shared/read locks** or **MVCC**, where each statement reads the latest committed version available when the statement starts. |
| **Repeatable Read** | Once a transaction has read a row, subsequent reads of that row return the same value. Dirty and non-repeatable reads are prevented. Phantom behavior depends on the database implementation. | Through **longer-lived read locks**, **MVCC snapshots**, or equivalent mechanisms that preserve the transaction's view of previously read data. |
| **Snapshot Isolation** | Each transaction reads from a **consistent snapshot** of the database rather than seeing changes committed after its snapshot was established. Dirty and non-repeatable reads are prevented. Some concurrent transactions can still commit changes that produce anomalies such as **write skew**. | Through **MVCC/versioned data**, maintaining multiple versions of rows and assigning each transaction a consistent snapshot. |
| **Serializable** | Transactions produce results equivalent to some **serial execution order**. It prevents the concurrency anomalies permitted by weaker isolation levels. | Through **strict locking**, **predicate/key-range locking**, **serializable MVCC**, **serialization validation**, or combinations of these techniques. |

## References

- https://en.wikipedia.org/wiki/Isolation_(database_systems)
- https://www.bailis.org/blog/understanding-weak-isolation-is-a-serious-problem/
- https://bytebytego.com/guides/what-are-database-isolation-levels/