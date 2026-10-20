---
tags: [problem]
---

# Fault-Tolerant Design


> **Fault-tolerant** refers to a system's ability to continue operating correctly, possibly with reduced performance, in the presence of faults or partial failures in its components.
> 

 **Key Topics:**

- Consensus algorithms (Raft, Paxos, Byzantine Fault Tolerance)
- Design patterns for **resilient microservices**
- Event sourcing and CQRS
- Cloud-native software design

**Research Questions:**

- What are the limits of **strong consistency vs. eventual consistency**?
- How can we optimize **replication strategies in large-scale databases**?
- Can we improve **stateful services in Kubernetes**?

**Good starting points:**

- Read about **Raft vs. Paxos** (raft.github.io).
- Study **Netflix's chaos engineering practices**.

**Replication**:

- Data or computation is duplicated across nodes.
- Examples: Primary-backup replication, quorum systems.

**Checkpointing and Recovery**:

- System state is periodically saved and restored after failures.
- Examples: Rollback recovery, log-based recovery.

**Consensus Protocols**:

- Ensures agreement among nodes despite failures.
- Examples: Paxos, Raft, Byzantine fault tolerance (BFT).

## References

- https://en.wikipedia.org/wiki/Fault_tolerance
- https://news.ycombinator.com/item?id=47977645