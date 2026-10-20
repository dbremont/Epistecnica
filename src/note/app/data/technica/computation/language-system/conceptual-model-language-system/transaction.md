---
tags: [unit-of-computation]
---

# Transaction


> A **transaction** is a unit of work that must be executed as a single, indivisible operation. A **transaction** typically involves a sequence of database operations, such as reading or updating data in one or more database tables. The main purpose of a **transaction** is to ensure that all database operations are completed successfully or not at all.
> 

> A **transaction** in databases follows the **ACID properties**, which stands for **Atomicity**, **Consistency**, **Isolation**, and **Durability**. Atomicity ensures that a **transaction** is treated as a single unit of work and is either fully completed or fully rolled back if an error occurs. Consistency ensures that a **transaction** brings the database from one consistent state to another consistent state. Isolation ensures that concurrent transactions do not interfere with each other. Durability ensures that once a **transaction** is committed, its changes are permanent and cannot be undone.
> 

## References

- https://en.wikipedia.org/wiki/Atomic_commit
- https://en.wikipedia.org/wiki/Commit_(data_management)