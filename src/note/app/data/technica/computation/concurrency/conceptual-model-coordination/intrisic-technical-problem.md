---
tags: [intrinsic-technical-problem]
---

# Intrisic Technical Problem


> Which are the technical problems introduced by concurrent execution, and which concurrency coordination techniques can be introduced to address them?
> 

## Problem Space

> Concurrency Coordination Technique Induced Problem ←→ Emergent Pathology.
> 

| Type | Name | Description | Note |
| --- | --- | --- | --- |
| Concurrent Execution Induced Problem | Race Condition | Execution outcome depends on uncontrolled timing/interleaving. | Canonical concurrency hazard. |
| Concurrent Execution Induced Problem | Lost Update | Concurrent writes overwrite each other. | Common in databases/counters. |
| Concurrent Execution Induced Problem | Visibility Problem | Updates are not observed consistently across threads/cores. | Memory-model issue. |
| Concurrent Execution Induced Problem | Atomicity Violation | Compound operation becomes interleaved. | Violates logical indivisibility. |
| Concurrent Execution Induced Problem | Data Inconsistency | Observers read partially updated state. | Consistency failure. |
| Concurrent Execution Induced Problem | Non-Determinism | Multiple executions produce different outcomes. | Makes debugging difficult. |
| Concurrent Execution Induced Problem | Deadlock | Actors wait indefinitely on cyclic dependencies. | Progress failure. |
| Concurrent Execution Induced Problem | Livelock | Actors react indefinitely without useful progress. | Active but ineffective. |
| Concurrent Execution Induced Problem | Starvation | Some actors never receive resources/execution. | Fairness failure. |
| Concurrent Execution Induced Problem | Priority Inversion | High-priority execution blocked by lower-priority holder. | Real-time systems issue. |
| Concurrent Execution Induced Problem | False Sharing | Independent variables interfere through cache coherence. | Hardware-induced slowdown. |
| Concurrent Execution Induced Problem | Message Reordering | Messages arrive out of causal/program order. | Coordination challenge. |
| Concurrent Execution Induced Problem | Duplicate Delivery | Same message/event processed multiple times. | Requires idempotency. |
| Concurrent Execution Induced Problem | Network Partition | Nodes lose communication consistency. | CAP-related issue. |
| Concurrent Execution Induced Problem | Thundering Herd | Many waiters awaken and contend simultaneously. | Load spike pathology. |
| Concurrent Execution Induced Problem | Oversubscription | Excessive runnable tasks overload scheduling resources. | Scheduling overhead. |
| Concurrent Execution Induced Problem | Load Imbalance | Work distribution across workers is uneven. | Reduces parallel efficiency. |
| Concurrent Execution Induced Problem | Barrier Synchronization Failure | Some workers fail to reach synchronization barrier. | Common in HPC. |
| Concurrent Execution Induced Problem | Cancellation Race | Completion and cancellation overlap inconsistently. | Async coordination hazard. |
| Concurrency Coordination Technique Induced Problem | ABA Problem | CAS-based synchronization mistakes A→B→A as unchanged state. | Lock-free algorithm pathology. |
| Concurrency Coordination Technique Induced Problem | Lock Contention | Excessive waiting on synchronization primitives. | Scalability bottleneck. |
| Concurrency Coordination Technique Induced Problem | Lock Convoying | Threads serialize behind a heavily contended lock. | Throughput degradation. |
| Concurrency Coordination Technique Induced Problem | Deadlock | Coordination primitives create cyclic waiting dependencies. | Coordination-induced progress failure. |
| Concurrency Coordination Technique Induced Problem | Livelock | Coordination logic causes endless reactive retries. | Non-blocking progress failure. |
| Concurrency Coordination Technique Induced Problem | Starvation | Coordination policy unfairly favors some actors. | Resource exclusion pathology. |
| Concurrency Coordination Technique Induced Problem | Priority Inversion | Synchronization causes high-priority tasks to block indirectly. | Coordination-scheduling interaction. |
| Concurrency Coordination Technique Induced Problem | Missed Signal / Lost Wakeup | Notification protocol fails due to timing/order mismatch. | Coordination bug. |
| Concurrency Coordination Technique Induced Problem | Contention Collapse | Synchronization overhead dominates useful work. | Scalability collapse. |
| Concurrency Coordination Technique Induced Problem | Retry Storm | Concurrent retries amplify contention/failure. | Distributed systems issue. |
| Concurrency Coordination Technique Induced Problem | CAS Spin Failure | Threads waste CPU repeatedly retrying atomic operations. | Busy-wait pathology. |
| Concurrency Coordination Technique Induced Problem | Synchronization Bottleneck | Central coordination primitive limits scalability. | Serialization point. |
| Concurrency Coordination Technique Induced Problem | Coordination Overhead Explosion | Coordination costs exceed computational work. | Parallel inefficiency. |
| Concurrency Coordination Technique Induced Problem | Barrier Stall | Faster workers wait excessively for slower workers. | Reduces throughput. |
| Concurrency Coordination Technique Induced Problem | Cascading Backpressure | Flow-control propagation stalls upstream systems. | Throughput collapse risk. |
| Concurrency Coordination Technique Induced Problem | Distributed Consensus Stall | Consensus cannot progress due to failures/quorum loss. | Availability tradeoff. |
| Concurrency Coordination Technique Induced Problem | Split-Brain Recovery Conflict | Recovery coordination creates conflicting authorities. | Cluster consistency issue. |
| Concurrency Coordination Technique Induced Problem | Memory Reclamation Hazard | Coordination for safe reclamation becomes inconsistent. | Lock-free memory safety issue. |
| Concurrency Coordination Technique Induced Problem | Coordination State Explosion | Synchronization states/interactions become unmanageable. | Verification complexity. |
| Concurrency Coordination Technique Induced Problem | Heisenbug | Instrumentation/debugging perturbs synchronization behavior. | Difficult reproduction. |

## References

- https://en.wikipedia.org/wiki/ABA_problem