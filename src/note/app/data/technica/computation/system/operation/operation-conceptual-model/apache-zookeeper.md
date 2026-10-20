---
tags: [tool]
---

# Apache Zookeeper

- [Etcd](note.html?n=technica/computation/system/operation/operation-conceptual-model/etcd.md)

> An **Apache** project that provides centralized service for maintaining configuration information, naming, and providing distributed synchronization.
> 

> **Apache ZooKeeper** is a **distributed coordination service** designed to manage configuration information, naming, synchronization, and group services across a distributed system. It provides a reliable, high-performance platform for building distributed applications that need to coordinate across multiple nodes, ensuring consistency and fault tolerance.
> 

## Use Cases

- **Configuration Management**: Centralized storage of configuration parameters used by distributed systems, enabling consistency and real-time updates.
- **Service Discovery**: Discover and maintain dynamic configuration of services in large-scale distributed environments.
- **Leader Election**: Ensure that a single instance of a service is designated as the leader in systems requiring coordination, such as in distributed databases or task coordination systems.
- **Distributed Locks**: ZooKeeper can be used to create and manage distributed locks, preventing race conditions in distributed systems.
- **Queue Management**: Distributed queueing systems where coordination and ordering of operations are necessary.

## Anatomy of  Apache Zookeeper

### **ZNode**:

- A **ZNode** is the fundamental data structure in ZooKeeper, which is similar to a file system node. Each ZNode can store data and has an associated **version number**, which is incremented whenever the ZNode's data or structure changes.
- ZNodes are organized in a hierarchical structure, forming a tree-like namespace. ZNodes are either **persistent** or **ephemeral**.
    - **Persistent ZNodes**: Exist until explicitly deleted.
    - **Ephemeral ZNodes**: Automatically deleted when the session that created them ends.

### **Zookeeper Ensemble**

- A **ZooKeeper ensemble** is a group of ZooKeeper servers working together to provide a fault-tolerant service. The ensemble ensures **data consistency** by employing the **Zab (Zookeeper Atomic Broadcast)** protocol to manage write operations and provide a consistent view of the system.
- A ZooKeeper ensemble typically consists of an odd number of nodes (3, 5, etc.) to ensure **quorum-based majority** voting, which ensures high availability and fault tolerance.
1. **Leader Election**:
    - ZooKeeper uses the **Zab protocol** to achieve **leader election** and ensure a single leader manages write operations within the ensemble. Only the leader can handle write requests, ensuring consistency, while followers replicate the leader's changes.
    - The leader election mechanism is designed to tolerate failure of a subset of servers while maintaining the correct operation of the ensemble.
2. **Watches**:
    - ZooKeeper allows clients to set **watches** on nodes (ZNodes). A watch is a mechanism that enables the system to notify clients when data or state changes occur at a particular ZNode. This allows for real-time notifications of changes, which is critical for synchronization across distributed systems.
3. **Quorum and Consistency**:
    - ZooKeeper guarantees **strong consistency** using a **majority quorum** approach. When a client performs a write operation, it is first proposed to the **leader**, which then broadcasts the change to followers. Once the majority of nodes in the ensemble acknowledge the change, the write is considered committed.
    - Read requests can be served by any node, but to ensure consistency, reads may be slightly stale if the system is recovering from a failure.
4. **Atomicity and Durability**:
    - ZooKeeper ensures **atomicity** in operations like updates and deletion. It guarantees that these operations either fully succeed or fully fail, ensuring **data durability** across the ensemble.

## **Zab Protocol**

> **Zab Protocol (Zookeeper Atomic Broadcast)**: Ensures **total ordering** of updates in the system by enforcing a linearizable write protocol. Every update request is assigned a **transaction ID (zxid)**, which is used to order transactions across the ensemble. The Zab protocol ensures that writes are durable and consistent across all nodes.
> 

## **Session Management**

> **Session Management**: ZooKeeper clients maintain **sessions** with the ensemble. Each session is identified by a session ID and has a **timeout** associated with it. If the client loses connection to the ensemble, ZooKeeper will attempt to reconnect. If a session expires, all ephemeral nodes associated with that session are deleted.
> 

## Fault Tolerance

- **Replication**: ZooKeeper employs **replication** of data across nodes in the ensemble. Changes to ZNodes are replicated to ensure consistency and availability, even in the case of server failures.
- **ZooKeeper's fault tolerance** ensures that the system continues to function as long as a majority (quorum) of servers are available, allowing for **toleration of node crashes** and network partitions.

## Performance

- **Write Performance**: Writes in ZooKeeper require synchronization across a majority of nodes, which can introduce latency, especially in large ensembles.
- **Read Performance**: Reads are more scalable, as they can be served by any available node, reducing the load on the leader and enabling faster response times for clients.

## **Consul vs. etcd vs. Zookeeper**

> This is a comparison of three prominent distributed systems used for configuration management and service discovery (etcd, Consul, and ZooKeeper).
> 

> **Use Cases:** The comparison helps determine the best tool for your architecture based on scalability, consistency, and use case-specific requirements.
> 
- **Consul** focuses more on service discovery and provides built-in support for service mesh.
- **etcd** is primarily used for **consistent configuration storage** and is deeply integrated with Kubernetes.
- **ZooKeeper** provides strong consistency and coordination primitives, but is less focused on configuration management specifically.

## References

- [Apache Zookeeper](https://zookeeper.apache.org/)
- https://nats.io/