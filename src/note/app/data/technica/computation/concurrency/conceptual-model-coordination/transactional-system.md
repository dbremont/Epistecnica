# Transactional System


> It’s a tools to bundle several operations into one atomic.
> 

> **Transaction**: A transaction in to a sequence of one or more operations that are executed as a single unit, ensuring data integrity and consistency, and typically adhering to the ACID properties (Atomicity, Consistency, Isolation, Durability).
> 

> **Chained Transaction Model**: Allows for the chaining of transactions, where the success or failure of one transaction determines the start of another.
> 

> **Distributed Transaction Model**: Manages transactions that involve multiple distributed databases or services, often using protocols like XA (eXtended Architecture).
> 

> **Flat Transaction Model**: Simple transactions that either fully succeed or fully fail without considering concurrency control or isolation.
> 

> A Database Transaction is a mechanism for combining a set of statements into a single, indivisible unit of work, ensuring that either all operations are completed successfully or none of them are applied, thereby maintaining data integrity.
> 

> A Transactional System is a computerized system or application that ensures the reliable and consistent processing of multiple related operations as a single, indivisible unit of work, typically providing features like atomicity, consistency, isolation, and durability (ACID properties) to maintain data integrity.
> 

> Atomicity:  …
> 

> Durability:  …
> 

## ….

> Transactional guarantee models refer to the different levels of guarantees provided by transactional systems regarding the properties of transactions. Here's an exploration of some common transactional guarantee models presented in a table:
> 

|  | Description | Example |
| --- | --- | --- |
| ACID (Atomicity, Consistency, Isolation, Durability) | The traditional set of transactional guarantees ensures that transactions are Atomic (all or nothing), Consistent (the database remains in a consistent state), Isolated (transactions are isolated from each other), and Durable (committed transactions persist even in the event of system failures). | Relational databases (e.g., Oracle, MySQL) enforce ACID properties to ensure data integrity and consistency. |
| BASE (Basically Available, Soft State, Eventually Consistent) | A relaxed set of transactional guarantees emphasizing availability over consistency, Soft state over strict consistency, and eventual consistency over immediate consistency. BASE systems prioritize system availability and responsiveness, allowing for temporary inconsistency resolved over time. | NoSQL databases (e.g., Cassandra, MongoDB) prioritize availability and partition tolerance over strict consistency, enabling scalable and highly available distributed systems. |
| Strong Consistency | A transactional guarantee ensures that all operations appear to execute atomically and in isolation, providing a linearizable view of the system where all clients see the same consistent state despite concurrent updates. This ensures strong consistency and eliminates inconsistencies. | Google Spanner uses a globally distributed architecture and TrueTime API to guarantee consistency across geographically distributed datacenters. |
| Eventual Consistency | A transactional guarantee allows temporary inconsistencies among replicas that eventually converge to a consistent state, ensuring eventual convergence of replicas despite concurrent updates, network partitions, and failures, providing high availability and partition tolerance. | Amazon DynamoDB employs eventual consistency to provide low-latency, highly available access to data, allowing for flexible scaling and distributed access patterns. |

## Models

> Here's a comparison of different transaction processing models commonly used in computing, presented in a table:
> 

| **Transaction Processing Model** | **Description** | **Examples** |
| --- | --- | --- |
| Two-Phase Commit (2PC) | A distributed transaction processing model that ensures atomicity and consistency across multiple participating nodes by coordinating a two-phase commit protocol, involving a coordinator and multiple participants, to decide whether to commit or abort the transaction. | Distributed databases (Oracle, MySQL), XA transactions |
| Saga Pattern | A distributed transaction model for long-lived, complex transactions that decomposes the transaction into a sequence of smaller, independent steps called "saga steps," where each step is associated with its compensating action to handle partial failures and ensure eventual consistency. | Microservices architecture, distributed systems |
| Optimistic Concurrency Control | A transaction processing model that assumes conflicts between transactions are rare, allowing transactions to proceed without locking resources and detecting conflicts only during commit time. If conflicts are detected, the model potentially rolls back transactions. | NoSQL databases (MongoDB), Conflict-free Replicated Data Types (CRDTs) |
| Pessimistic Concurrency Control | A transaction processing model that uses locks to ensure exclusive access to resources during a transaction, preventing concurrent conflicting access and guaranteeing serializability but potentially leading to increased contention and reduced concurrency. | Relational databases (Oracle, PostgreSQL), Java Transaction API (JTA) |
| Event Sourcing | A transaction processing model where all changes to application state are captured as a sequence of immutable events allows the system's state to be reconstructed by replaying events, provides auditability, and enables temporal queries and analysis. | Event-driven architectures, CQRS (Command Query Responsibility Segregation) |
| Distributed Locking | A transaction processing model that coordinates access to shared resources across distributed nodes using distributed locks, ensuring exclusive access and preventing conflicting updates, but potentially leading to deadlock and scalability issues. | Apache ZooKeeper, Consul, Redis distributed locks |

## Nested Transaction

> Here's a comparison of different nested transaction mechanisms, including savepoints, presented in a table:
> 

| **Nested Transaction Mechanism** | **Description** | **Example** |
| --- | --- | --- |
| Savepoints | Allows transactions to be divided into smaller work units, with the ability to set savepoints within a transaction and roll back to a specific savepoint without affecting the entire transaction. | In a banking application, a transaction may involve multiple database operations such as deposit, withdrawal, and transfer, with savepoints set before each operation to roll back in case of errors. |
| Nested Transactions | Allows transactions to be nested within other transactions, where inner transactions are treated as part of the outer transaction but can commit or rollback independently without affecting the state of the outer transaction. | In a distributed system, a transaction may include multiple sub-tasks, each encapsulated within nested transactions, ensuring that each sub-task can be committed or rolled back independently within the scope of the larger transaction. |

## References

- [Shadow paging](https://en.wikipedia.org/wiki/Shadow_paging)
- [Transaction Processing](https://en.wikipedia.org/wiki/Transaction_processing)
- [The end of a myth: Distributed transactions can scale](https://news.ycombinator.com/item?id=35520044)
- Elmagarmid, Ahmed K. [“Transaction models for advanced database applications.”](https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1870&context=cstech) (1991).
- Gray, J., & Reuter, A. (1992). Transaction Processing: Concepts and Techniques. Elsevier.
- OASIS Business Transaction Protocol https://flylib.com/books/en/2.87.1.69/1/
- Distributed Transaction Management with REST and Try Confirm/Cancel Pattern https://zhenyanghua.github.io/2019/04/distributed-transaction-management-with-rest-and-try-confirm-cancel-pattern/
- An In-Depth Analysis of Distributed Transaction Solutions https://www.alibabacloud.com/blog/an-in-depth-analysis-of-distributed-transaction-solutions_597232
- [Transaction Processing in PostgreSQL](https://www.postgresql.org/files/developer/transactions.pdf)
- [Demystifying Database Transactions](https://dineshgowda.com/posts/demystifying-database-transcations/)
- https://en.wikipedia.org/wiki/Transaction_processing_system