---
tags: [coordination]
---

# Conflict-free Replicated Data Type (CRDT)


A **Conflict-Free Replicated Data Type (CRDT)** is a type of data structure that is designed to support distributed systems that replicate data across multiple nodes or replicas. The key feature of a CRDT is that it is designed to maintain consistency and convergence of data across replicas, even in the face of network partitions and failures.

**CRDTs** achieve this by using a set of rules or algorithms to ensure that updates to the data structure are commutative and associative. This means that updates to the data structure can be applied in any order, and the end result will be the same across all replicas. Additionally, **CRDTs** are designed to be conflict-free, meaning that updates can be applied independently on different replicas without the need for coordination or consensus.

There are two main types of **CRDTs**: operation-based and state-based. Operation-based **CRDTs** define a set of operations that can be applied to the data structure, and ensure that updates are commutative and associative with respect to these operations. State-based **CRDTs**, on the other hand, maintain a copy of the entire data structure at each replica, and use a set of merging rules to ensure that replicas converge to the same state.

**CRDTs** are used in a variety of distributed systems, including databases, collaboration tools, and real-time applications. By providing a consistent and reliable way to replicate and manage data across multiple nodes, **CRDTs** help to ensure that distributed systems remain available and responsive, even in the face of network failures and other disruptions.

## References

[CRDT.tech](https://crdt.tech/)

[Conflict-free Replicated Data Type](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type)

[You might not need a CRDT](https://news.ycombinator.com/item?id=33865672)

[5000x faster CRDTs: An Adventure in Optimization](https://josephg.com/blog/crdts-go-brrr/)