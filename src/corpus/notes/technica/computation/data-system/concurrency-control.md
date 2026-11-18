---
tags: [note]
---

# Concurrency Control

- [Isolation Model](/view.html?p=notes/technica/computation/data-system/isolation-model.md)

> **Concurrency control** is the set of **mechanisms and protocols that a data system uses to coordinate concurrent operations on shared data**, so that their execution satisfies the system's specified **correctness and isolation guarantees**.
> 

## What is Concurrency Control in a Data  System?

> **Concurrency control** is the set of mechanisms used by a data system to coordinate **concurrent operations** on shared data so that their execution satisfies the system's specified correctness and isolation guarantees.
> 

## What is the map of data systems concurrency control technical elements?

> See the full table — https://github.com/dbremont/Epistecnica/blob/main/src/notes/app/notes/general/data-system-concurrency-control.md
> 

## What are the types of locks?

| Lock Type | Description |
| --- | --- |
| Shared Lock (S) | Permits a transaction to read a resource while allowing other compatible shared locks. |
| Exclusive Lock (X) | Permits a transaction to read and modify a resource while preventing conflicting locks. |
| Update Lock (U) | Indicates that a transaction may update a resource and helps prevent certain conversion deadlocks between shared and exclusive locks. |
| Intention Shared Lock (IS) | Indicates that a transaction intends to acquire shared locks on finer-grained resources below the locked resource. |
| Intention Exclusive Lock (IX) | Indicates that a transaction intends to acquire exclusive locks on finer-grained resources below the locked resource. |
| Shared Intention Exclusive Lock (SIX) | Combines a shared lock on the current resource with an intention to acquire exclusive locks on finer-grained resources. |
| Key-Range Lock | Locks a range of index keys to control concurrent access to records that fall within the range. |
| Gap Lock | Locks the gap between index records to prevent concurrent insertion into that range. |
| Next-Key Lock | Combines a record lock with a gap lock to protect an index record and the gap preceding it. |
| Predicate Lock | Locks all records satisfying a logical predicate, including records that may subsequently satisfy the predicate. |
| Record Lock | Locks an individual index record or row. |
| Page Lock | Locks a storage page containing multiple records. |
| Table Lock | Locks an entire table. |
| Database Lock | Locks an entire database. |
| Metadata Lock | Prevents conflicting schema or metadata operations while a transaction uses the affected database object. |

## Which are the set of **Locking Behavior** Options - that data systems support?

| Locking Behavior Option (Mechanism) | Description | Supported By |
| --- | --- | --- |
| **WAIT** | Wait for the conflicting lock to be released before proceeding. This is typically the default locking behavior. | Oracle, PostgreSQL, MySQL/InnoDB, SQL Server |
| **NOWAIT** | Attempt to acquire the lock; if it is already held by another transaction, immediately return an error rather than waiting. | Oracle, PostgreSQL, MySQL/InnoDB, SQL Server |
| **SKIP LOCKED** | If a requested row is already locked, skip that row and continue processing other eligible rows instead of waiting. | Oracle, PostgreSQL, MySQL/InnoDB, SQL Server |
| **LOCK WAIT TIMEOUT** | Wait for a specified maximum period for the lock; if the lock is not obtained within that period, fail the operation. | Oracle, PostgreSQL, MySQL/InnoDB, SQL Server |
| **DEADLOCK DETECTION / ABORT** | Detect a cycle of transactions waiting for one another and abort one transaction to break the cycle. | Oracle, PostgreSQL, MySQL/InnoDB, SQL Server |

## What is the relation with Isolation Level?

> An **isolation level** specifies the **concurrency guarantees** that a data system provides to a transaction, while **concurrency control** is the set of mechanisms used to enforce those guarantees during concurrent execution.
> 

> The relation is best read as a **permission table**. An isolation level names the anomalies that must not occur; the concurrency-control mechanism decides how to prevent them. The matrix below is therefore a specification of what each level permits, not a description of any particular implementation.

| Level | Dirty read | Non-repeatable read | Phantom read | Lost update | Write skew |
| --- | --- | --- | --- | --- | --- |
| **Read Uncommitted** | possible | possible | possible | possible | possible |
| **Read Committed** | prevented | possible | possible | possible | possible |
| **Repeatable Read** | prevented | prevented | possible (implementation-dependent) | possible | possible |
| **Snapshot Isolation** | prevented | prevented | prevented | prevented | **possible** |
| **Serializable** | prevented | prevented | prevented | prevented | prevented |

> Snapshot isolation is the row that shows why the levels are not a ladder. It prevents phantoms — the anomaly the standard's ladder treats as the last step before serialisability — and still permits **write skew**, two transactions reading disjoint state and writing on the strength of what the other read. A system can therefore be stronger than Repeatable Read on one axis and weaker than Serializable on another, which is why an isolation level should be chosen per workload and verified by its anomalies rather than by its name.

## Can the selected isolation level and concurrency-control mechanism conflict with each other?

> The selected isolation level and concurrency-control mechanism can be semantically incompatible when the mechanism permits concurrent executions whose observable effects violate the execution histories or visibility guarantees required by that isolation level.
> 

> Executions permitted by the concurrency-control mechanism ⊆ executions permitted by the isolation-level specification.
> 

## References

- [Concurrency](/view.html?p=notes/technica/computation/concurrency/concurrency.md)
- https://shopify.engineering/scaling-inventory-reservations
- [What are Database Isolation Levels? — ByteByteGo](https://bytebytego.com/guides/what-are-database-isolation-levels/) — the compact statement of the level ladder this note maps onto concurrency-control mechanisms
