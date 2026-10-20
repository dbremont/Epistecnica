---
tags: [coordination, intrinsic-technical-problem]
---

# Consensus


> Note: This is a very **abstract concept** .
> 

> Consensus is the process of getting all the nodes (or computers) in a distributed system to **agree on a single value** or decision, even if some nodes fail or the network is unreliable.
> 

> **Consensus enables coordination** when agreement on a decision is needed before proceeding (e.g., electing a leader in a distributed system).
> 

> In a multi-node computation system there is some agreement that must be reach. Note there work agreement here is super general.
> 

> Consensus is a  Intrinsic Technical Problem introduced - by the technical system - it’s not part of the ‘problem domain’ - let say business systems, etc.
> 

Consensus is a technical problem that refers - on how to **agree on state evolution** -  when multiple systems have a **local view of the state**.

…

- Which type systems induced this types of problems? Which are the domain problems that induced this types of systems?
- …

How does it emerges?

| Technical Condition | Why Consensus Appears |
| --- | --- |
| Replication | Multiple copies may diverge |
| Distribution | No shared memory |
| Concurrency | Simultaneous operations conflict |
| Failures | Nodes may disagree after crashes |
| Network delays | Different visibility of events |
| Independent execution | No global clock/order |

Imagine a group of friends trying to decide where to eat:

- Each friend suggests a restaurant (this is their "initial value").
- They need to agree on **one restaurant** (this is the "consensus").
- Even if some friends don’t respond or disagree, the group must still find a way to decide.

QA:

- How I Understand Consensus? [How I Understand Consensus?](note.html?n=technica/computation/concurrency/conceptual-model-coordination/consensus.md)
- What is the consensus problem in distributed systems?
- What are the three key properties of consensus?
- What is the difference between synchronous and asynchronous systems in the context of consensus?
- What is the FLP impossibility result, and why is it significant?
- What is the difference between crash failures and Byzantine failures?
- Explain how the Paxos algorithm works. What are its key components?
- How does Raft simplify Paxos? What are the main roles in Raft (e.g., leader, follower)?
- What is Practical Byzantine Fault Tolerance (PBFT), and how does it handle malicious nodes?
- What is the role of a quorum in consensus algorithms?
- What is the **Two Generals' Problem**, and how does it illustrate the challenges of consensus?
- What is the **Byzantine Generals' Problem**, and how does it differ from the Two Generals' Problem?
- How do consensus algorithms handle **network partitions**?
- What is the **CAP theorem**, and how does it relate to consensus?
- Why is **leader election** important in consensus protocols like Paxos and Raft?
- What is Two-Phase Commit (2PC), and how does it ensure atomicity in distributed transactions?
- What are the limitations of 2PC, and how does Three-Phase Commit (3PC) address them?
- How do Paxos Commit and Raft Commit integrate consensus with commit protocols?
- How is consensus used in distributed databases (e.g., Spanner, Cassandra)?
- What role does consensus play in blockchain systems like Bitcoin and Ethereum?
- How does Apache ZooKeeper use consensus to provide coordination services?
- What is the role of consensus in distributed file systems like Google File System (GFS)?
- How do **microservices architectures** use consensus for state management?
- What is **randomized consensus**, and how does it circumvent the FLP impossibility result?
- How does **Tendermint** combine Byzantine fault tolerance with proof-of-stake?
- What is **gossip protocol**, and how does it achieve eventual consistency?
- How do **consensus protocols** handle dynamic membership changes (e.g., nodes joining or leaving)?
- What are the trade-offs between **performance** and **fault tolerance** in consensus algorithms?
- In a system with 5 nodes, how many nodes must agree to tolerate 1 Byzantine failure? Why?
- Describe a scenario where **2PC** might block indefinitely. How would you resolve this?
- How would you design a consensus protocol for a system with high network latency?
- How does **Bitcoin** achieve consensus without a central authority?
- What consensus mechanism does **Ethereum 2.0** use, and why was it chosen?
- How does **Google Spanner** use consensus to provide globally consistent distributed transactions?
- What are the trade-offs between **decentralized** and **leader-based** consensus protocols?
- How does **consensus** differ from **replication** in distributed systems?

## The Three Key Properties of Consensus

For consensus to work, it must satisfy three properties:

1. **Agreement**: All nodes must decide on the **same value**.
2. **Validity**: The agreed-upon value must be one of the values proposed by the nodes.
3. **Termination**: Every node must eventually make a decision (it can’t stay stuck forever).

## Protocols

> 

| **Category** | **Protocol** | **Description** | **Use Cases** |
| --- | --- | --- | --- |
| **Leader-Based** | **Paxos** | A leader-based consensus algorithm that ensures strong consistency and fault tolerance. | Distributed databases, coordination services. |
|  | **Raft** | A simplified leader-based consensus algorithm designed for understandability and practical use. | Distributed systems (e.g., etcd, Consul). |
|  | **Zab** | A leader-based atomic broadcast protocol used in Apache ZooKeeper for coordination. | Coordination services (e.g., Apache ZooKeeper). |
| **Decentralized** | **Gossip** | A decentralized protocol that uses epidemic-style communication to propagate information. | Distributed databases, peer-to-peer networks. |
|  | **Proof-of-Work (PoW)** | A decentralized protocol where nodes solve computational puzzles to propose blocks. | Blockchain systems (e.g., Bitcoin). |
|  | **Proof-of-Stake (PoS)** | A decentralized protocol where nodes are chosen to propose blocks based on their stake (ownership). | Blockchain systems (e.g., Ethereum 2.0, Cardano). |
| **Byzantine Fault-Tolerant** | **PBFT (Practical Byzantine Fault Tolerance)** | A protocol that tolerates malicious nodes and ensures consensus in Byzantine environments. | High-security systems, blockchain (e.g., Hyperledger). |
|  | **Tendermint** | A Byzantine fault-tolerant consensus protocol combined with a proof-of-stake mechanism. | Blockchain systems (e.g., Cosmos). |
| **Commit Protocols** | **Two-Phase Commit (2PC)** | A protocol that ensures atomicity in distributed transactions but can block if the coordinator fails. | Distributed databases, distributed transaction systems. |
|  | **Three-Phase Commit (3PC)** | A non-blocking version of 2PC that adds a pre-commit phase to avoid blocking. | Distributed databases, distributed transaction systems. |
|  | **Paxos Commit** | A commit protocol that integrates Paxos consensus to ensure atomicity and consistency. | Distributed databases, distributed transaction systems. |
|  | **Raft Commit** | A commit protocol that integrates Raft consensus to ensure atomicity and consistency. | Distributed databases, distributed transaction systems. |

## How I Understand Consensus?

- Pre-formal view: In a multicomputation environment, in order to proceed, one needs to make sure that others are on board. What is the agreement problem that were are trying to solve here? How/ Where/When does  decition problems arises?
- Semi formal view: …
- Formal view: …

## References

- [Raft](https://www.wikiwand.com/en/Raft_(algorithm))
- [Paxos](https://www.wikiwand.com/en/Paxos_(computer_science))
- https://en.wikipedia.org/wiki/Consensus_(computer_science)
- [Ask HN: How does Booking.com guarantee consistency of reservations on scale?](https://news.ycombinator.com/item?id=37444740)