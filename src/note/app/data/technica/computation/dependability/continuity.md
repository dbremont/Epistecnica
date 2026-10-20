# Continuity

> In this note, we will treat a particularly important topic in computer science: **how to make computational systems capable of self-continuation and Joint-Continuation.**
> 

> **Note:** Self-Continuation is not only about failures, recovery, etc. It is also about **joint computation**. What happens when I send a task to another system and do not receive an update about what happened?
> 

## Formulation

> What do we mean by **Self Continuation capabilty?**
> 

> **Self-continuation capability** is the ability of a computational system to **maintain, recover, and continue its own ongoing computational process across time, interruptions, or failures**.
> 

> **Note:** In the broad sense, **Self-Continuation** can be understood as a kind of awareness of its own computation, together with the persistence of that awareness, in order to **maintain and continue its ongoing computational process across time and interruptions**.
> 

More concretely, the system can:

- **Maintain** a representation of its ongoing computational state.
- **Persist** that state across interruptions.
- **Recover** its prior state after stopping or failure.
- **Recognize** what computation it was performing.
- **Resume** the computation from an appropriate point.
- **Preserve coherence** between the previous and resumed computation.

### What is Continuity?

> **Continuity** is the property of a process by which its state, identity, and progression are maintained across time, allowing what happens later to remain connected to what happened before.
> 

> **Computational continuity** is the preservation of sufficient state and context for an ongoing computation to remain connected and able to proceed across time, interruptions, or changes in execution.
> 

> Note: Continuity is not only about crash recovery—it can also fail during continuous computation. For example, a system may send a task for execution, fail to receive or retain the result, and then lose track of the task entirely. The computation continues, but the system's logical continuity has been broken.
> 

### What is Self-Continuity?

> **Self-continuity** is the capacity of a computational system to maintain the continuity of **its own ongoing computation** across time, including after interruptions, by preserving and recovering a representation of its state, context, and progress.
> 

The key idea is:

**“What I am doing now remains connected to what I was doing before.”**

### What is Joint Continuity?

> **Joint continuity** is the capacity to maintain the continuity of an **ongoing computation distributed across multiple interacting systems**, by maintaining the connections between their states, actions, dependencies, and results over time.
> 

### **What types of failures can introduce discontinuity and incoherence?** Why does a system need to be made “continuous”?

| Failure Type | Description | Instance Set |
| --- | --- | --- |
| Node Failure | Occurs when a node in the distributed system becomes unresponsive or crashes, leading to a loss of availability for services hosted on that node. | Hardware failure, software crash |
| Network Partition | A situation where communication between nodes in the distributed system is disrupted, leading to the isolation of subsets of nodes from each other, potentially causing inconsistency. | Split-brain scenario, network congestion |
| Message Loss/Delay | Due to network issues, messages exchanged between nodes may be lost, delayed, or delivered out of order, leading to potential inconsistency or incorrect behavior in the system. | Packet loss, network congestion, message queue overflow |
| Byzantine Failure | This occurs when a node in the distributed system behaves maliciously or arbitrarily, sending incorrect or misleading information to other nodes and potentially compromising system integrity. | Malware infection, compromised node |
| Performance Degradation | The overall performance of the distributed system may degrade due to factors such as increased load, inefficient resource utilization, or bottlenecks in the system architecture. | CPU saturation, disk I/O bottleneck, inefficient algorithms |
| Data Corruption/Inconsistency | Data stored in the distributed system may become corrupted or inconsistent due to software bugs, hardware faults, or improper handling of concurrent updates. | Data loss, stale data, inconsistent state |

### Which types of technical guarantees must a continuity-capable system provide?

| Technical Guarantee | Description | How continuity enables it? |
| --- | --- | --- |
| **Exactly-once delivery** | A message/event is delivered to its logical recipient exactly once. | The system must retain delivery identity/history across interruptions to recognize what has already been delivered. |
| **Exactly-once processing** | A logical operation is processed exactly once. | The system must preserve processing state so a restarted execution does not duplicate a completed operation. |
| **Exactly-once effects** | An external effect occurs exactly once. | The system must durably record whether the effect occurred, or use a mechanism that makes repeated execution equivalent to one effect. |
| **At-most-once processing** | An operation is processed no more than once. | The system must preserve enough state to distinguish an already-attempted operation after restart. |
| **At-least-once processing** | An unfinished operation is eventually retried. | The system must retain unfinished work and resume/retry it after interruption. |
| **Idempotent continuation** | Re-executing a continuation does not produce an incorrect duplicate effect. | The system must identify the logical operation/continuation across executions and preserve its relevant state. |
| **Deduplication** | Repeated representations of the same logical operation are recognized and collapsed. | The system must preserve stable identity and sufficient history across executions. |
| **Checkpoint / resume** | Computation can continue from a previously preserved execution point. | Continuity provides persistent execution state from which computation can resume. |
| **Transactional continuity** | An interrupted transaction retains its logical state until it can be committed, aborted, or recovered. | Transaction state must survive process/node interruption independently of the transient execution. |
| **Durable workflow state** | A workflow retains its state across process failures and restarts. | Workflow state persists independently of the currently executing process. |
| **Causal ordering** | Events that have a causal relationship retain the required ordering. | Relevant causal history must persist across interruptions and execution boundaries. |
| **Monotonic state progression** | State does not incorrectly regress when computation resumes. | The system retains prior state/version information and can reject or reconcile stale state. |
| **Exactly-once state transition** | A logical state transition occurs once, rather than being lost or applied repeatedly. | The transition's identity and completion state must survive interruption and recovery. |
| **Execution identity continuity** | A resumed execution can be recognized as the continuation of the same logical execution. | Persistent execution identity links pre-interruption and post-interruption activity. |
| **Progress continuity** | Previously achieved computational progress is not unnecessarily lost after interruption. | Intermediate progress/state is durably retained and recoverable. |
| **Session continuity** | A computational session retains its relevant state across process or connection interruptions. | Session state exists independently of the transient process/connection. |
| **State-machine continuity** | A stateful computation resumes from the correct logical state. | Current state and transition history/version are preserved across interruptions. |
| **Workflo** |  |  |

### What are the consequences of a system that allows discontinuities?

- Partial failure
- Atomicity failure
- Dual-write problem
- Distributed transaction problems
- Lost state
- Lost messages
- Duplicate execution
- Inconsistent state
- Orphaned tasks
- Lost progress
- Broken causal continuity
- Context loss
- Coordination failure

## Implementation

> How to make computational systems maintain computational continuity and coherence?
> 

### What types of technical problems need to be solved for **Self-Continuation**?

| **Type of Problem** | **Description** |
| --- | --- |
| **State Persistence** | How to preserve the system's relevant computational state across time. |
| **State Recovery** | How to reconstruct the computational state after interruption or failure. |
| **Process Continuation** | How to resume an ongoing computation from its previous state. |
| **Identity Continuity** | How the system maintains a persistent representation of the computation as *its own ongoing process*. |
| **Temporal Coherence** | How to maintain consistency between past, present, and future computational states. |
| **Context Persistence** | How to preserve the context necessary to continue the computation coherently. |
| **Failure Recovery** | How to continue computation after crashes, faults, or unexpected termination. |
| **Checkpointing** | How and when to capture recoverable snapshots of computational state. |
| **Consistency** | How to prevent state from becoming inconsistent during interruption and recovery. |
| **Distributed State Management** | How to preserve and reconstruct state when computation spans multiple machines or processes. |
| **Resource Reacquisition** | How to recover the computational resources, connections, files, services, or tools required for continuation. |
| **Progress Tracking** | How to determine what has already been completed and what remains to be done. |
| **Self-State Representation** | How the system represents its own current computational condition and history. |
| **Continuation Decision** | How the system determines what computation should happen next after resumption. |
| **Long-Term Continuity** | How to maintain computational continuity over extended periods and multiple interruptions. |
| **Joint Coherence** | How to maintain a coherent computational process when parts of the computation are performed by other systems. |
| **Joint Continuity** | How to maintain continuity of a computation across multiple collaborating systems, including tracking delegated work, receiving updates, and incorporating external results into the ongoing process. |
| **Joint State** | How to maintain a representation of the state of a computation that is distributed across multiple interacting systems. |

### How to address does problems?

| **Type of Problem** | **Solution Space** |
| --- | --- |
| **State Persistence** | Persistent storage, databases, durable state stores |
| **State Recovery** | State reconstruction, snapshots, recovery protocols |
| **Process Continuation** | Checkpoint–restart, resumable execution, continuation mechanisms |
| **Identity Continuity** | Persistent process identity, execution IDs, durable identity |
| **Temporal Coherence** | Event logs, versioning, temporal state models |
| **Context Persistence** | Persistent context stores, session state, event histories |
| **Failure Recovery** | Fault tolerance, retries, replication, recovery mechanisms |
| **Checkpointing** | Periodic checkpoints, incremental checkpoints, state snapshots |
| **Consistency** | Transactions, synchronization, consensus, consistency protocols |
| **Distributed State Management** | Distributed databases, replicated state, consensus systems |
| **Resource Reacquisition** | Resource managers, service discovery, connection recovery |
| **Progress Tracking** | Execution logs, task state, workflow state machines |
| **Self-State Representation** | Internal state models, execution metadata, system state representations |
| **Continuation Decision** | Workflow engines, planners, schedulers, policy/state machines |
| **Long-Term Continuity** | Durable execution, persistent workflows, event sourcing |

### What are the underlying techniques behind solutions to **Self-Continuation** problems?

> Persistence → State Representation → State Capture → State Recovery → Context Reconstruction → Continuation → Coherent Progress.
> 

> **Note:** Some of these techniques are **mitigations applied during computation**; others are **mechanisms for recovery, reconstruction, or continuation after a disruption.**
> 

| **Technique** | **Technique Tree Path** | **Description** | **Role** |
| --- | --- | --- | --- |
| **Persistence** | State → Persistence | Store computational state beyond the lifetime of a running process. | Preserve state across time |
| **Checkpointing** | State → Persistence → Checkpointing | Periodically save a recoverable execution state. | Enable restart |
| **Snapshotting** | State → Persistence → Snapshotting | Capture a point-in-time representation of system state. | Provide recovery points |
| **Event Sourcing** | State → Persistence → Event Sourcing | Persist state-changing events from which state can be reconstructed. | Reconstruct state |
| **Write-Ahead Logging** | State → Persistence → Logging → WAL | Record changes before applying them to durable state. | Support recovery |
| **Execution Journaling** | State → Persistence → Logging → Execution Journal | Record computational actions and their outcomes. | Reconstruct execution history |
| **Versioning** | State → Persistence → Versioning | Maintain successive versions of state or artifacts. | Support temporal reconstruction |
| **State Representation** | State → Representation | Explicitly represent the state relevant to continuing computation. | Make continuation state identifiable |
| **State Machines** | State → Representation → State Machine | Represent computation as states and transitions. | Make progress and transitions explicit |
| **Self-State Modeling** | State → Representation → Self-State | Represent the system's own computational condition, progress, and context. | Support self-continuation |
| **Context Persistence** | State → Representation → Context | Preserve the contextual information required to continue computation. | Preserve computational coherence |
| **Progress Tracking** | State → Representation → Progress | Track completed, pending, and active computational work. | Determine continuation point |
| **Consistency** | State → Consistency | Ensure that related state remains mutually compatible. | Prevent incoherent recovery |
| **Transactions** | State → Consistency → Transactions | Group state changes into atomic units. | Preserve state integrity |
| **Concurrency Control** | State → Consistency → Concurrency | Coordinate concurrent state modifications. | Prevent conflicting updates |
| **Distributed Consensus** | State → Consistency → Distributed Agreement | Coordinate agreement about shared state across nodes. | Maintain distributed consistency |
| **Replication** | State → Redundancy → Replication | Maintain multiple copies of state or computation. | Protect against state loss |
| **Redundancy** | State → Redundancy | Duplicate critical computational components or resources. | Maintain availability |
| **Failure Detection** | Recovery → Detection | Detect failures, anomalies, or unavailable components. | Trigger recovery |
| **Health Checking** | Recovery → Detection → Health Checks | Periodically verify component availability and health. | Detect failed components |
| **Heartbeats** | Recovery → Detection → Heartbeats | Exchange periodic liveness signals. | Detect process failure |
| **Timeouts** | Recovery → Detection → Timeouts | Bound the time allowed for an operation to complete. | Detect stalled computation |
| **Recovery** | Recovery → State Recovery | Restore a computational process from preserved state. | Re-establish continuity |
| **Checkpoint–Restart** | Recovery → State Recovery → Checkpoint–Restart | Restore a computation from a previously saved checkpoint. | Resume interrupted computation |
| **Rollback** | Recovery → State Recovery → Rollback | Return computation to a previous valid state. | Recover from inconsistent state |
| **Failover** | Recovery → Execution Recovery → Failover | Transfer computation to an alternative component or node. | Continue after failure |
| **Process Migration** | Recovery → Execution Recovery → Migration | Move computation to another execution environment. | Preserve execution despite infrastructure change |
| **Resource Rebinding** | Recovery → Execution Recovery → Resource Rebinding | Reconnect recovered computation to required resources. | Restore execution environment |
| **Retry** | Recovery → Operation Recovery → Retry | Re-execute an operation that failed. | Recover transient failures |
| **Retry Policy** | Recovery → Operation Recovery → Retry → Policy | Define when and how failed operations are retried. | Control repeated execution |
| **Idempotency** | Recovery → Operation Recovery → Idempotency | Make repeated execution produce an equivalent valid result. | Make retries safe |
| **Circuit Breaking** | Recovery → Operation Recovery → Circuit Breaker | Temporarily stop calls to an failing dependency. | Contain cascading failure |
| **Graceful Degradation** | Recovery → Service Continuity → Degradation | Reduce functionality while preserving essential operation. | Maintain partial continuity |
| **Durable Queuing** | Continuation → Work Persistence → Durable Queue | Persist pending work until it is successfully processed. | Prevent loss of unfinished work |
| **Workflow Persistence** | Continuation → Workflow → Persistence | Persist workflow state and execution history. | Enable long-running continuation |
| **Workflow Recovery** | Continuation → Workflow → Recovery | Restore a workflow to an appropriate execution point. | Resume multi-step computation |
| **Continuation Management** | Continuation → Control | Determine what computation should occur next. | Drive resumed execution |
| **Scheduling** | Continuation → Control → Scheduling | Determine when and where pending computation executes. | Continue computational progress |
| **Leasing** | Coordination → Liveness → Leasing | Temporarily assign ownership of computational work or resources. | Enable reassignment after failure |
| **Leader Election** | Coordination → Liveness → Leader Election | Select an active coordinator among distributed processes. | Restore coordination |
| **Distributed Coordination** | Coordination → Distributed Coordination | Coordinate state and actions among participating systems. | Maintain joint computation |
| **Joint State Management** | Joint Continuity → State | Maintain state spanning multiple computational participants. | Preserve shared computational state |
| **Joint Progress Tracking** | Joint Continuity → Progress | Track progress of delegated or distributed computation. | Know what other systems have completed |
| **Result Propagation** | Joint Continuity → Communication → Results | Communicate intermediate and final computational results between systems. | Connect distributed computation |
| **Acknowledgment** | Joint Continuity → Communication → Acknowledgment | Confirm receipt or completion of a computational action. | Establish continuity across interactions |
| **Distributed Workflow Coordination** | Joint Continuity → Coordination → Workflow | Coordinate a computation whose steps execute across different systems. | Maintain joint continuity |

### What is a practical - and minimal architecture for any system with self-continuity capacity?

```bash
COMPUTE
   ↓
UPDATE STATE
   ↓
PERSIST STATE
   ↓
     [INTERRUPTION]
   ↓
RECOVER STATE
   ↓
RECONSTRUCT CONTEXT
   ↓
CONTINUE
   ↓
COMPUTE ...
```

## Case Study

### How certain types of computational systems handle  discontinuity?

| System | Description | How does it handle discontinuity? |
| --- | --- | --- |
| **Task Execution System** | Submits tasks to workers and tracks their execution and results. | Detects lost communication or execution state and uses durable task identity, state, retries, and reconciliation to continue the task. |
| **Message Queue** | Transfers messages between producers and consumers. | Persists messages and delivery state so an interrupted consumer can resume without losing the logical message history. |
| **Workflow Engine** | Coordinates a sequence of dependent tasks over time. | Persists workflow state and resumes from the last known logical state after interruption or lost execution context. |
| **Database Transaction System** | Maintains consistent state across multiple operations. | Uses durable transaction state, logging, commit protocols, and recovery to resolve interrupted transactions. |
| **Distributed Job Scheduler** | Assigns and monitors jobs across computational resources. | Maintains durable job identity and execution state, detects lost workers, and reassigns or reconciles work. |
| **Agent System** | Performs multi-step actions using tools and external systems. | Maintains task/context state and records actions and results so it does not silently forget an unfinished operation. |
| **Stream Processing System** | Continuously processes an ordered stream of events. | Uses offsets, checkpoints, state stores, and recovery mechanisms to preserve processing position and state. |
| **File Transfer System** | Transfers data between endpoints, potentially over unreliable connections. | Tracks transfer progress and resumes incomplete transfers rather than treating the interrupted transfer as none |

### How do particular systems handle discontinuity?

| System | Description | How does it handle discontinuity? |
| --- | --- | --- |
| **Apache Kafka** | Distributed event-streaming platform. | Persists events and consumer offsets so consumers can resume from a known position after interruption or loss of connection. |
| **PostgreSQL** | Relational database management system. | Uses WAL and transactional recovery to preserve database state across crashes and interrupted transactions. |
| **Apache Airflow** | Workflow orchestration platform. | Persists DAG/task state and can retry or resume tasks whose execution was interrupted or failed. |
| **Temporal** | Durable workflow execution platform. | Records workflow history durably and reconstructs workflow state after workers disappear or executions are interrupted. |
| **Kubernetes** | Container orchestration platform. | Continuously reconciles desired state with observed state and recreates failed workloads. |
| **Slurm** | HPC workload manager. | Maintains job state and can requeue/recover jobs when execution resources or nodes fail. |
| **Apache Flink** | Stateful stream-processing system. | Uses checkpoints/savepoints to preserve computation state and resume processing after failure. |
| **Spark** | Distributed data-processing engine. | Reconstructs lost computation through lineage and can persist intermediate state/checkpoints. |
| **Redis** | In-memory data store with persistence and replication mechanisms. | Can preserve state beyond a process lifetime through persistence and recover it after restart. |
| **Git** | Distributed version-control system. | Preserves the history and identity of changes, allowing work to continue across disconnected executions and machines. |
| **Amazon S3** | Durable object-storage service. | Objects persist independently of the process that created them, allowing later computation to recover previously produced data. |
| **SQLite** | Embedded transactional database. | Uses journaling/WAL to recover a consistent database state after interruption. |

## QA

### Which are the related topics in Computer Science to ‘**Self Continuation’?**

- **Fault-Tolerant Systems**
- **Fault Recovery**
- **Checkpointing and Restart**
- **State Persistence**
- **Process Recovery**
- **Resumable Computation**
- **Durable Execution**
- **Self-Healing Systems**
- **Fault-Tolerant Distributed Systems**
- **Process Migration**
- **Workflow Recovery**
- **Long-Running Computation**
- **Persistent Processes**
- **Temporal State Management**
- **Continuation-Passing Style (CPS)**

## References

- [Agency](https://app.notion.com/p/Agency-eebe9b5a15d84a3db7a1a1273fc29a2c?pvs=21)
- https://github.com/checkpoint-restore/criu
- https://www.geeksforgeeks.org/failure-models-in-system-design/
- https://www.geeksforgeeks.org/failure-models-in-distributed-system/
- https://en.wikipedia.org/wiki/Fault_tolerance
- [Consensus](note.html?n=technica/computation/concurrency/conceptual-model-coordination/consensus.md)
- [Consistency](note.html?n=technica/computation/dependability/consistency.md)
- [Concurrency](note.html?n=technica/computation/concurrency.md)
- [Fault-Tolerant Design](note.html?n=technica/computation/system/design/computer-system-design-conceptual-model/fault-tolerant-design.md)
- [**Transactional System**](note.html?n=technica/computation/concurrency/conceptual-model-coordination/transactional-system.md)
- https://en.wikipedia.org/wiki/Reliability_engineering
- [**Message Delivery Guarantee**](note.html?n=technica/computation/distributed-computing/multi-node-processing-system-conceptual-model/message-delivery-guarantee.md)
- [Distributed Computing](note.html?n=technica/computation/distributed-computing.md)
- https://arxiv.org/abs/2402.05244