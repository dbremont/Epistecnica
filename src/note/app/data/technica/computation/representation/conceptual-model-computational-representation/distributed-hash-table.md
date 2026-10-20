---
tags: [data-structure]
---

# Distributed Hash Table


> A Distributed Hash Table (DHT) is a decentralized distributed system that provides a scalable and efficient way to locate and retrieve data in a peer-to-peer (P2P) network. DHTs are often used in P2P file-sharing systems, content delivery networks (CDNs), and other decentralized applications.
> 

## Formulation

Here’s an overview of the key concepts and how a DHT works:

1. **Key-Value Storage:** DHTs are designed to store and retrieve key-value pairs. Each piece of data is associated with a unique key, and the DHT allows you to store data with a given key and retrieve data using that key.
2. **Decentralization:** Unlike traditional client-server architectures, DHTs are decentralized. There is no central server that stores all the data or manages the lookup process. Instead, data and control are distributed across the participating nodes (peers) in the network.
3. **Hashing:** DHTs use a distributed hashing algorithm to map keys to nodes in the network. This ensures that data is distributed evenly across nodes and that each node is responsible for a subset of the keyspace. Popular hashing algorithms like SHA-1 or SHA-256 are often used for this purpose.
4. **Routing Table:** Each node in the DHT maintains a routing table that helps it locate other nodes responsible for specific keys. This routing table typically contains information about nearby nodes in the keyspace, making it possible to route requests efficiently.
5. **Key Lookup:** When a node wants to retrieve data associated with a specific key, it queries the DHT network to find the node responsible for that key. This process involves iterative lookups using the routing table until the responsible node is found.
6. **Data Replication:** To ensure fault tolerance and availability, data in a DHT is often replicated across multiple nodes. This means that multiple nodes are responsible for the same data, and if one node goes offline, another can serve the data.
7. **Bootstrap Nodes:** To join a DHT network, a new node typically needs to contact one or more bootstrap nodes initially. These bootstrap nodes can provide information about the current state of the network and help the new node join the network.
8. **Security and Trust:** DHTs can implement security mechanisms to ensure the integrity and authenticity of data. Cryptographic techniques like digital signatures and certificates may be used to establish trust among nodes.
9. **Application Layer:** DHTs serve as a foundation for building various distributed applications. Developers can build applications on top of DHTs to create decentralized file storage systems, messaging platforms, or content distribution networks.

## Implementation

| **Implementation** | **Description** |
| --- | --- |
| **Kademlia** | One of the most well-known DHTs, widely used in peer-to-peer networks for decentralized key-value storage and efficient node lookup. |
| **Chord** | Simplifies distributed key-value storage using consistent hashing and a ring-based overlay network for scalable and fault-tolerant lookups. |
| **CAN (Content Addressable Network)** | DHT algorithm designed for distributed content addressing using a multi-dimensional coordinate space to map keys. |
| **Pastry** | DHT-based overlay network that provides decentralized routing and scalable object location in distributed systems. |
| **Tapestry** | DHT designed for distributed systems and content-addressable networks, supporting efficient routing and object location. |
| **OpenDHT** | Open-source DHT implementation used by the BitTorrent network, enabling distributed key-value storage and retrieval. |
| **NTLDHT (NAT Traversal Library and DHT)** | Lightweight DHT library with built-in NAT traversal support for easy integration into decentralized applications. |
| **Koorde** | DHT designed for efficient routing in large-scale networks, combining Chord’s ring structure with De Bruijn graph routing. |

## Use

> Which problems does DHT Solve?
> 

| **Problem** | **How DHT Solves It** |
| --- | --- |
| Distributed key-value storage | Uses a distributed hash function to map keys to nodes, enabling decentralized storage and retrieval. |
| Efficient lookup | Structured routing tables allow locating data in $O (log N)$ hops, even in large networks. |
| Load balancing | Uniform key distribution ensures that storage and query load is spread evenly across nodes. |
| Fault tolerance & node churn | Replicates keys and dynamically updates routing tables to maintain data availability despite node failures. |
| Decentralization | Eliminates central servers by allowing nodes to store and retrieve data independently. |
| Scalability | Logarithmic lookup cost with network size enables support for millions of nodes. |
| NAT traversal & peer discovery (some implementations) | Built-in NAT traversal and routing allow peers behind firewalls to join and communicate in the network. |

## References

- https://en.wikipedia.org/wiki/Distributed_hash_table
- https://stackoverflow.com/questions/144360/simple-basic-explanation-of-a-distributed-hash-table-dht
- https://arxiv.org/abs/2508.14239