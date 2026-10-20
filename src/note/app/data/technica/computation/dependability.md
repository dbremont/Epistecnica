# Dependability

> **Specification** — *A specification is a precise, verifiable description of the required properties, behaviors, interfaces, constraints, and service obligations that a computational system is expected to satisfy.*
> 

> **Computational System** — *A computational system is an organized collection of computational components that process information through computation and interaction to realize specified behaviors and s*e*rvices.*
> 

> **Dependability** — *Dependability is the property of a computational system that justifies confidence that it will deliver its specified services correctly, reliably, safely, securely, and continuously under stated operating conditions.*
> 

## **Dependability**

> What are the components of **dependability** as a **technical requirement**?
> 

> **Dependability** is a composite technical requirement concerned with ensuring that a computational system delivers trustworthy service throughout its operational lifetime.
> 

### **Dependability Requirement Space**

> **Note:** These requirements are not orthogonal. **Durability, fault tolerance, and recoverability can be formulated in terms of continuity and coherence.**
> 

> What are the practical names of the **dependability requirements in the literature**?
> 

| Category | Requirement | Abstract Requirement | Meaning | Note |
| --- | --- | --- | --- | --- |
| **Behavioral Correctness** | **Correctness** | Correctness | The system behaves in accordance with its specification. | Fundamental requirement against which other requirements are defined. |
|  | **Consistency** | Consistency | System observations and state transitions satisfy a specified consistency model. | Includes stronger and weaker consistency models. |
|  | └─ Linearizability | Consistency | Operations appear to occur atomically in real-time order. | Strong distributed consistency model. |
|  | └─ Sequential Consistency | Consistency | Operations appear in an order consistent with each process's program order. | Common in memory and distributed systems. |
|  | └─ Serializability | Consistency | Concurrent transactions are equivalent to some serial execution. | Transactional consistency property. |
|  | └─ Snapshot Isolation | Consistency | Transactions operate against a consistent snapshot. | Transaction isolation/consistency model. |
|  | └─ Eventual Consistency | Consistency | Replicas eventually converge toward a common state. | Weak replicated-state guarantee. |
|  | └─ Read-Your-Writes | Session Consistency | A client observes its own completed writes. | Session-level consistency guarantee. |
|  | └─ Monotonic Reads | Session Consistency | A client does not observe an older state after observing a newer one. | Session-level consistency guarantee. |
|  | **Atomicity** | Atomicity | An operation or transaction takes effect indivisibly. | All-or-nothing state transition. |
|  | **Isolation** | Isolation | Concurrent operations are protected from prohibited interference. | Primarily a transactional requirement. |
| **Persistence & Temporal Dependability** | **Durability** | Persistence | Committed state survives subsequent failures. | Can be understood as preservation of state across discontinuity. |
|  | **Recoverability** | Restoration | Correct service/state can be restored after failure. | Depends on preserving sufficient state and execution information. |
|  | **Continuity** | Temporal Persistence | Computation, state, identity, and obligations remain connected across interruptions or discontinuities (in computer, or after crash) . | Central temporal requirement in this framework. |
|  | **Coherence** | Global Compatibility | Related states, actions, and representations remain mutually compatible across time and components. | Provides the relational constraint necessary for meaningful continuation. |
| **Failure Dependability** | **Reliability** | Failure-Free Operation | The system performs its required function for a specified period under specified conditions. | Concerned with probability/rate of failure. |
|  | **Availability** | Service Accessibility | The system is operational and accessible when required. | Usually characterized by uptime or probability of service being available. |
|  | **Fault Tolerance** | Fault Accommodation | The system continues providing specified service despite faults. | Typically achieved through redundancy, replication, isolation, masking, or failover. |
|  | **Resilience** | Disruption Adaptation | The system withstands, adapts to, and recovers from dis |  |

### **Dependability Thread Space**

> What can break the ‘**Fully Dependable’ State?**
> 

| Threat | Description | Instance(s) |
| --- | --- | --- |
| Infrastructure Failure | Failure of underlying computing resources. | Server crash, disk failure, network outage. |
| Communication Failure | Messages cannot be delivered correctly. | Packet loss, timeout, duplicated message. |
| Service Failure | A component does not provide its expected service. | Payment service unavailable. |
| Incorrect Execution | A component executes incorrectly. | Payment charged twice. |
| State Inconsistency | Different parts of the system disagree about state. | Database replicas diverge. |
| Concurrency Conflict | Concurrent operations interfere incorrectly. | Lost update, race condition. |
| Data Corruption | Stored or transmitted data becomes invalid. | Corrupted transaction record. |
| Configuration Error | System configuration causes incorrect behavior. | Wrong database isolation level. |
| Resource Exhaustion | System lacks required resources. | Memory exhaustion, thread exhaustion. |
| Security Violation | Unauthorized behavior affects system correctness. | Unauthorized transaction. |
| Integration Failure | Interacting systems violate assumptions. | External API changes response format. |
| Human/Operational Error | Operational actions introduce incorrect states. | Wrong deployment, bad migration. |

### **Dependability Mechanism Space**

> How to prevent break the ‘**Fully Dependable’ State?**
> 

| **Mechanism** | **Description** | **Instance(s)** |
| --- | --- | --- |
| Redundancy | Multiple components provide the same function. | Replicated services, RAID. |
| Retry Control | Handles transient failures safely. | Exponential backoff, retry limits. |
| Idempotency Control | Prevents duplicate effects. | Payment request IDs. |
| Transaction Control | Ensures atomic state changes. | Database transactions. |
| Concurrency Control | Prevents incorrect concurrent execution. | Locks, MVCC, serializability. |
| Consistency Protocols | Keeps distributed state aligned. | Consensus, replication protocols. |
| Failure Detection | Identifies failed components. | Heartbeats, health checks. |
| Recovery Mechanism | Restores valid operation. | Rollback, checkpointing. |
| Validation Mechanism | Prevents invalid states. | Schema validation, invariants. |
| Monitoring and Observability | Detects violations early. | Metrics, tracing, alerts. |
| Isolation Mechanism | Prevents unwanted interference. | Containers, database isolation levels. |
| Access Control | Prevents unauthorized operations. | Authentication, authorization. |
| Transaction Policy |  |  |

## Dependability State

> What are the **possible states related** to the dependability properties that a given system can be in?
> 

![image.png](data/technica/computation/assets/dependability/image.png)

| State | Meaning |
| --- | --- |
| **Correct** | The delivered service complies with the specification. |
| **Incorrect** | The delivered service deviates from the specification. |
| **Operational** | The system is providing service. |
| **Failed** | The delivered service no longer satisfies the specification. |
| **Degraded** | Service is still provided but below the desired level (performance, availability, etc.). |
| **Fully Dependable** | Every specified dependability requirement is satisfied. |
| **Partially Dependable** | Some requirements are satisfied, while others are violated. |
| **Undependable** | The system fails to satisfy its required dependability objectives to an unacceptable degree. |

## References

[**Continuity**](note.html?n=technica/computation/dependability/continuity.md)

[Verification](note.html?n=technica/computation/dependability/verification.md)

[Consistency](note.html?n=technica/computation/dependability/consistency.md)

[Formal Verification](note.html?n=technica/computation/dependability/formal-verification.md)

- [System](note.html?n=technica/computation/system.md)
- [Verification](note.html?n=technica/computation/dependability/verification.md)
- [Consistency](note.html?n=technica/computation/dependability/consistency.md)
- [Transaction](note.html?n=technica/computation/language-system/conceptual-model-language-system/transaction.md)
- [**Transactional System**](note.html?n=technica/computation/concurrency/conceptual-model-coordination/transactional-system.md)
- Laprie, Jean-Claude, and Brian Randell. "Fundamental concepts of dependability." *Report N01145, LAAS-CNRS* (2001).