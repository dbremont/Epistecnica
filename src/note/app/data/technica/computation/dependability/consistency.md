# Consistency

> In this note we will explore the **notion of consistency - in Computer Science Technical Domain.**
> 

> **Consistency** is the **abstract property** of a **well-defined set of objects** remaining in accordance with a specified **criterion of validity**. By *abstract*, we mean that consistency, by itself, is not a concrete property but a **property template**. The concrete elements of this property—the **objects** to which it applies and the **criterion of validity** against which they are evaluated—are specified by the **domain that concretizes the property**, such as a database, memory system, file system, distributed system, or programming language.
> 

> Etymology: **Consistency** derives from the Latin *consistentia* ("standing together," "agreement," or "coherence"), from *consistere* ("to stand together, remain firm"), reflecting the idea that the parts of a system remain in agreement without contradiction.
> 

> **Note:** The consistency specification is part of the broader **correctness (**[Correctness](note.html?n=technica/computation/dependability/verification/conceptual-model-verification/correctness.md)**) specification** of the software system.
> 

## Formulation

### Which are the instances of the abstract consistency property?

![image.png](../assets/note/technica/computation/dependability/consistency/image.png)

| Category | Domain | **Concrete Consistency Property** | Description | **Formulation — Object Set** | **Formulation — Criteria Set** | **Consistency Model (If Any)** | **Computer System Instance Set** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Order-based** | Distributed systems | **Linearizability** | Each operation appears to take effect atomically at a point between invocation and response, respecting real-time order. | Concurrent operation histories on shared objects | A linearization exists that preserves real-time precedence | Strong consistency | **etcd; ZooKeeper; Consul** |
| **Order-based** | Concurrency / shared memory | **Sequential Consistency** | Execution appears equivalent to a sequential execution consistent with each process's program order. | Memory-operation histories | A total order exists that preserves program order | Memory consistency model | **Java Memory Model; C/C++ implementations under SC atomics; OpenMP** |
| **Order-based** | Databases | **Serializability** | A concurrent transaction history is equivalent to some serial transaction execution. | Transaction histories | Equivalence to a serial history | Transaction isolation model | **PostgreSQL; Oracle Database; MySQL/InnoDB; SQL Server** |
| **Order-based** | Databases | **Strict Serializability** | Serializability additionally constrained by real-time ordering. | Transaction histories | Serial equivalence + real-time order | Strong consistency / transaction isolation model | **Google Cloud Spanner** |
| **Order-based** | Distributed systems | **Causal Consistency** | Causally related operations are observed in causal order. | Distributed operation histories | Causal order is preserved by all observers | Causal consistency model | **COPS; GentleRain; AntidoteDB** |
| **Order-based** | Distributed systems | **PRAM / FIFO Consistency** | Writes issued by one process are observed in that process's order. | Distributed writes and read observations | Per-process write order is preserved | PRAM consistency model | **Distributed shared-memory / replicated-storage implementations** |
| **Order-based** | Distributed systems | **Processor Consistency** | Writes from each processor are observed in processor order without requiring one global order. | Processor memory operations | Per-processor ordering constraints | Memory consistency model | **Historical multiprocessor / DSM systems** |
| **Synchronization-based** | Distributed shared memory | **Weak Consistency** | Consistency is guaranteed at specified synchronization points. | Shared-memory operations + synchronization events | Required ordering/visibility at synchronization points | Weak consistency model | **Classical DSM systems** |
| **Synchronization-based** | Distributed shared memory | **Release Consistency** | Ordering is enforced around acquire/release synchronization. | Memory + synchronization operations | Acquire/release ordering constraints | Weak consistency model | **Distributed shared-memory systems; release-style memory models** |
| **Synchronization-based** | Distributed shared memory | **Entry Consistency** | Synchronization establishes consistency only for associated data. | Data + synchronization objects | Synchronization-specific visibility constraints | Weak consistency model | **Classical DSM research systems** |
| **State-based** | Replicated / distributed systems | **Eventual Consistency** | Replicas converge when updates cease. | Replica states | Quiescence implies eventual convergence | Eventual consistency model | **Amazon Dynamo-style systems; Riak; Cassandra** |
| **State-based** | CRDT / replicated systems | **Strong Eventual Consistency** | Replicas receiving the same updates converge to the same state. | Replica states + delivered operations | Same update set ⇒ same state + eventual convergence | Eventual consistency model | **Automerge; Yjs; Riak DT** |
| **State/order-based** | Distributed systems | **Causal+ Consistency** | Causal consistency combined with convergent conflict resolution. | Distributed histories + replica states | Causal ordering + convergence criterion | Causal consistency model | **GentleRain; COPS-style systems** |
| **Client-centric** | Distributed storage | **Read-Your-Writes** | A client observes its own completed writes. | Client read/write histories | Own writes are visible to subsequent reads | Client-centric consistency model | **Azure Cosmos DB Session; Amazon S3** |
| **Client-centric** | Distributed storage | **Monotonic Reads** | Subsequent reads never return an older state than one previously observed. | Client read histories | Observed states are monotonically ordered | Client-centric consistency model | **Azure Cosmos DB Session** |
| **Client-centric** | Distributed storage | **Monotonic Writes** | A client's writes are observed/applied in issuance order. | Client write histories | Client write order is preserved | Client-centric consistency model | **Azure Cosmos DB Session** |
| **Client-centric** | Distributed storage | **Writes-Follow-Reads** | A write preserves dependencies established by a preceding read. | Client read/write histories | Read-before-write dependency is preserved | Client-centric consistency model | **Azure Cosmos DB Session** |
| **Quantitative** | Distributed storage | **Bounded Staleness** | A read may be stale but only within a specified temporal/version bound. | Replica states + read results | Staleness ≤ specified bound | Bounded-staleness model | **Azure Cosmos DB** |
| **Quantitative** | Distributed storage | **K-Atomicity** | A read may return one of a bounded number of recent writes. | Read/write histories | Returned value belongs to latest K writes | Quantitative consistency model | **Research / specialized distributed-storage systems** |
| **State-based** | Distributed / replicated systems | **Delta Consistency** | Replica divergence is constrained by a specified bound. | Replica states | State/version divergence ≤ specified delta | Quantitative consistency model | **Research geo-replicated systems** |
| **History-based** | Concurrent objects | **Quiescent Consistency** | When concurrency is absent, execution satisfies the required sequential relation. | Operation histories | Required sequential relation during quiescence | History-based consistency model | **Concurrent-object implementations / research systems** |
| **Failure-aware** | Secure distributed storage | **Fork Consistency** | Divergent client views are allowed but must be detectable. | Client-visible histories / views | Divergence forms a detectable fork | Fork consistency model | **SUNDR** |
| **Failure-aware** | Distributed storage | **Fork-Linearizability** | Client histories are linearizable while views remain non-forked; divergence is detectable. | Operation histories + client views | Linearizability + detectable fork | Fork consistency model | **SUNDR / fork-linearizable storage research systems** |
| **Failure-aware** | Byzantine distributed systems | **Byzantine Consistency** | Consistency is maintained under a specified Byzantine fault model. | Distributed states / operation histories | Consistency criteria hold despite allowed Byzantine behavior | Byzantine consistency model | **PBFT; Hyperledger Fabric ordering/consensus components** |
| **Transaction-state** | Databases / STM | **Snapshot Isolation** | Transactions read from a consistent snapshot while concurrent writes are constrained at commit. | Transaction histories + snapshots | Snapshot consistency + write-conflict criterion | Transaction isolation model | **PostgreSQL; Oracle Database; MySQL/InnoDB** |
| **Transaction-state** | Databases / STM | **Opacity** | Transactions, including aborted transactions, cannot observe invalid intermediate states. | Transactional histories + observations | Every observation corresponds to a valid transactional state | Transactional consistency model | **TL2; SwissTM; NOrec** |
| **History-based** | Databases | **Conflict Serializability** | A history is equivalent to a serial history under conflict-preserving reordering. | Transaction histories | Conflict graph is acyclic | Serializability model | **PostgreSQL Serializable; 2PL-based DBMS implementations** |
| **History-based** | Databases | **View Serializability** | A history is equivalent to a serial history with respect to reads-from and final writes. | Transaction histories | Same reads-from relationships and final writes | Serializability model | **Primarily a theoretical/database-theory formulation** |

### Which are the mechanism used to guaranteed the property in Computer Systems?

| Mechanism | Description | Usage |
| --- | --- | --- |
| **Locks** | Prevent concurrent access to a shared resource according to a locking protocol. | Mutual exclusion, serializability, shared-state consistency |
| **Mutexes** | Mutual-exclusion synchronization primitive allowing only one thread to enter a critical section. | Thread synchronization, shared-memory consistency |
| **Read–Write Locks** | Allow concurrent readers while excluding conflicting writers. | Shared-memory and data-structure synchronization |
| **Semaphores** | Synchronization primitives controlling access to a resource through permits/counts. | Resource coordination, synchronization |
| **Monitors** | Encapsulate shared state together with mutually exclusive operations and condition synchronization. | Concurrent object consistency |
| **Condition Variables** | Allow threads to wait until a specified state predicate becomes true. | Coordination around shared-state invariants |
| **Atomic Operations** | Hardware-supported indivisible read-modify-write operations such as CAS, swap, and fetch-and-add. | Lock-free synchronization and atomic state transitions |
| **Compare-and-Swap (CAS)** | Atomically changes a value only if it still equals an expected value. | Lock-free data structures, optimistic synchronization |
| **Memory Barriers / Fences** | Constrain compiler/CPU reordering and establish visibility/order between memory operations. | Memory consistency and synchronization |
| **Transactional Memory** | Groups memory operations into transactions that commit atomically or abort. | Atomicity and concurrent-state consistency |
| **Database Transactions** | Groups database operations into an atomic unit governed by transaction semantics. | ACID properties, invariant preservation |
| **Two-Phase Locking (2PL)** | Controls transaction access through a growing and shrinking locking phase. | Conflict serializability |
| **MVCC** | Maintains multiple versions of data so readers can access consistent snapshots while writers proceed concurrently. | Snapshot isolation, transaction isolation |
| **Optimistic Concurrency Control (OCC)** | Allows concurrent execution and validates conflicts before commit. | Transaction consistency without extensive locking |
| **Compare-and-Swap Loops** | Repeatedly perform atomic updates until the desired state transition succeeds. | Lock-free concurrent algorithms |
| **Quorum Reads/Writes** | Requires operations to contact a sufficient subset of replicas. | Replica consistency and fault tolerance |
| **Replication** | Maintains multiple copies of data or state. | Availability, durability, fault tolerance, consistency protocols |
| **Synchronous Replication** | An update is acknowledged only after required replicas have applied it. | Stronger replica consistency |
| **Asynchronous Replication** | Updates propagate to replicas after the initiating operation completes. | Availability and eventual consistency |
| **Primary/Leader Replication** | A designated primary orders or coordinates updates before replication. | Ordered replication, consistency |
| **Consensus Protocols** | Enable distributed participants to agree on a value or ordered sequence despite failures. | Replicated state machines, distributed coordination |
| **Paxos** | Consensus protocol for agreeing on values despite crash failures. | Distributed consensus and replicated state |
| **Raft** | Leader-based consensus protocol using replicated logs. | Replicated state machines, distributed coordination |
| **Viewstamped Replication** | Replication protocol using views and a primary/backup structure. | Fault-tolerant replicated services |
| **Zab** | Atomic broadcast/coordination protocol used by ZooKeeper. | Ordered replicated state and coordination |
| **Atomic Broadcast / Total Order Broadcast** | Ensures messages are delivered to participants in a common order. | Replicated-state consistency |
| **Distributed Transactions** | Coordinate transactional operations spanning multiple resources/nodes. | Cross-node atomicity and consistency |
| **Two-Phase Commit (2PC)** | Coordinates participants so a distributed transaction commits or aborts as one unit. | Distributed transaction atomicity |
| **Three-Phase Commit (3PC)** | Adds an intermediate phase to reduce certain blocking scenarios of 2PC. | Distributed transaction coordination |
| **Write-Ahead Logging (WAL)** | Records changes in a durable log before applying them to persistent state. | Atomicity, durability, crash recovery |
| **Journaling** | Records intended filesystem/state changes in a journal before or alongside applying them. | Filesystem consistency and crash recovery |
| **Checksums / Hashes** | Detect accidental corruption by verifying data against a stored digest. | Data integrity |
| **Merkle Trees** | Hierarchical cryptographic hashes allow efficient verification of replicated data. | Data integrity, authenticated replication |
| **CRDTs** | Data structures designed so independently applied operations/states converge under defined conditions. | Strong eventual consistency |
| **Anti-Entropy** | Replicas periodically exchange and reconcile state. | Eventual convergence |
| **Gossip Protocols** | Nodes probabilistically disseminate state or updates among peers. | Replication, membership, eventual convergence |
| **Conflict-Free Merge Functions** | Deterministically combine concurrent state changes. | Replicated-state convergence |
| **Version Vectors** | Track causal/version relationships between replicas. | Causal consistency and conflict detection |
| **Lamport Clocks** | Provide a logical ordering of distributed events. | Ordering and causal reasoning |
| **Vector Clocks** | Track partial causal ordering among distributed events. | Causality detection and conflict resolution |
| **Leases** | Grant temporary exclusive authority over a resource for a bounded period. | Distributed coordination and cache consistency |
| **Fencing Tokens** | Give successive resource owners monotonically increasing tokens so stale owners can be rejected. | Distributed locks and stale-writer prevention |
| **Distributed Locks** | Coordinate exclusive access to a resource across machines. | Distributed mutual exclusion |
| **Leader Election** | Select a single coordinator among distributed participants. | Replication, coordination, distributed services |
| **Barriers** | Prevent participants from proceeding until all required participants reach a synchronization point. | Parallel computation and synchronization |
| **Sequence Numbers** | Assign monotonically ordered identifiers to operations or messages. | Ordering, duplicate detection, replication |
| **Idempotency Keys** | Associate repeated requests with the same logical operation. | Preventing duplicate effects in distributed systems |
| **Deduplication** | Detects and suppresses repeated operations or messages. | Reliable distributed processing |
| **Transactional Message Queues** | Couple message processing with transactional state changes. | Exactly-once-like processing semantics |
| **Atomic Commit Protocols** | Coordinate multiple participants so a distributed operation commits consistently. | Distributed transactions |
| **Replication Logs** | Maintain an ordered durable sequence of state-changing operations. | Replicated state machines |
| **State-Machine Replication** | Replicates deterministic state machines by applying the same ordered commands. | Fault-tolerant consistent services |

## QA

### Does consistency means - they should not be failures?

> Consistency is not the absence of failures; it is the preservation of system invariants despite failures, concurrency, and other forms of execution.
> 

### Why is the term *“Concrete Consistency  Property”* preferred over *“Consistency Model”* as an organizing framework for discussing consistency?

> The term **"Consistency Model"** refers to categories or families of concrete consistency-property formulations, rather than to any single practical, concrete formulation.
> 

### What is the relation of consistency - and isolation level?

> An **isolation level** is a **configuration mechanism provided by a data system** that allows the user to select the **concrete consistency guarantees** that a transaction receives.
> 

## References

- [Isolation Model](note.html?n=technica/computation/data-system/data-system-conceptual-model/isolation-model.md)
- [Visualizing Linearizability](https://mwhittaker.github.io/blog/visualizing_linearizability/)
- [Linearizability versus Serializability](http://www.bailis.org/blog/linearizability-versus-serializability/)
- [Eventual Consistency Today: Limitations, Extensions, and Beyond](https://queue.acm.org/detail.cfm?id=2462076)
- [On Consistency and Durability](http://www.bailis.org/blog/on-consistency-and-durability/)
- [Eventual Business Consistency](https://tidyfirst.substack.com/p/eventual-business-consistency)
- [On Consistency and Durability](http://www.bailis.org/blog/on-consistency-and-durability/)
- [Operational transformation](https://en.wikipedia.org/wiki/Operational_transformation)
- [Memory Consistency Models: A Tutorial](https://news.ycombinator.com/item?id=40350201) ([utexas.edu](http://utexas.edu/))
- https://people.mpi-sws.org/~viktor/wmc/
- https://en.wikipedia.org/wiki/ACID
- https://en.wikipedia.org/wiki/Eventual_consistency
- https://en.wikipedia.org/wiki/Consistency_model
- https://jepsen.io/consistency
- https://jepsen.io/consistency/models