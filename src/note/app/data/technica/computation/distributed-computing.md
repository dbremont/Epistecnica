# Distributed Computing

> Distributed System
> 

> A little bit of multi-process !!!
> 

> **Distributed**: A  systems compose of several proceses on the same or multiple computers.
> 

> Distributed systems are a type of computer system that consists of multiple autonomous computers, connected via a communication network, that work together to achieve a common goal.
> 

> **Goals:** Availability, scalability, performance, reliable.
> 

> **Problems:** concurrency, faults, unbounded latency.
> 

> **Tools:** Replication abstraction, broadcast, consensus.
> 

> “. . . a system in which the failure of a computer you didn’t even know existed can render your own computer unusable.” — Leslie Lamport
> 

> **Multicomputation** refers to the simultaneous execution of multiple computational tasks or processes across a system or network to enhance efficiency and performance.
> 

> **Fault tolerance**: Fault tolerance is the ability of a distributed system to continue operating in the presence of failures, such as node or network failures. Fault tolerance can be achieved through redundancy, replication, and recovery mechanisms.
> 

Why make a system distributed?

- **It’s inherently distributed,** e.g., sending a message from your mobile phone to your friend’s phone.
- **For better reliability,** even if one node fails, the system as a whole keeps functioning
- Get data from a nearby node rather than one halfway around the world for better performance.
- **To solve more significant problems,** e.g., vast amounts of data can’t fit on one machine.

QA:

- How to think about state in distributed computation?

## Breviarium

| **Topic** | **Explanation** | **Emoji** |
| --- | --- | --- |
| Network Communication | Global scope and data transmission | 🌐📡 |
| Consensus Protocols | Agreement among nodes (e.g., Paxos, Raft) | 🤝🗳️ |
| Fault Tolerance | Retry logic and resilience to failure | 🔁🛡️ |
| Replication | Copying data across nodes | 📄📄 |
| Partitioning (Sharding) | Dividing data into slices | 🍰🔪 |
| Leader Election | Choosing a master node | 👑🔍 |
| CAP Theorem | Trade-offs: Consistency, Availability, Partition Tolerance | ⚖️🧩 |
| Eventual Consistency | Updates propagate over time | 🕰️✔️ |
| Distributed Databases | Global data storage systems | 🗃️🌍 |
| Time Synchronization | Ensuring consistent clocks (e.g., NTP, Lamport) | ⏱️🔗 |
| Vector Clocks | Causality tracking | 📈🧭 |
| Gossip Protocol | Info spread like a rumor | 🗣️🤫 |
| Load Balancing | Distributing workload evenly | ⚖️🌐 |
| Service Discovery | Locating services in a network | 🔍📘 |
| Microservices Architecture | Modular, independently deployable components | 🧩🏗️ |
| Kubernetes | Container orchestration system | 🚢📦 |
| Distributed File Systems | E.g., HDFS, Ceph | 📁📤 |
| Message Queues | Async communication (e.g., Kafka, RabbitMQ) | 📬📨 |
| Remote Procedure Calls (RPC) | Calling functions across machines | ☎️📞 |
| Data Consistency Models | Linearizability, eventual consistency, etc. | 🧠📏 |
| Monitoring & Observability | Visibility into system health | 👁️📊 |
| Scalability | Handling growth in traffic or data | 📈🌱 |
| Distributed Tracing | Tracking requests across components | 🧵🔍 |
| Choreography vs Orchestration | Decentralized vs centralized coordination | 💃🧑‍✈️ |

## System Taxonomy

| **System Type** | **Example Technologies** |
| --- | --- |
| **Big Data Processing** | Apache Hadoop, Spark Batch, AWS EMR |
| **ETL Pipelines** | Apache NiFi, Talend, Airflow |
| **Mainframe Batch** | IBM z/OS, JCL (Job Control Language) |
| **Data Warehousing** | Google BigQuery, Snowflake |
| **Financial Transactions** | ACH Processing, End-of-Day Bank Reconciliation |
| **Log Processing** | Logstash, Fluentd |

## Node Taxonomy

| **Category** | **Purpose** | **Examples** |
| --- | --- | --- |
| **Input Nodes** | Receive data from external sources | Sensors (IoT), User Interfaces (UI), API Gateways |
| **Processing Nodes** | Perform computations and data processing | CPUs, GPUs, Worker Nodes (Hadoop, Kubernetes) |
| **Memory Nodes** | Temporarily store data for fast access | RAM, Redis, Memcached |
| **Output Nodes** | Send processed data to external systems or users | Display Nodes, API Responses, Printers |
| **Communication Nodes** | Manage data transmission and synchronization | Network Routers, Message Queues (Kafka, RabbitMQ) |
| **Control Nodes** | Oversee and coordinate system operations | Kubernetes Scheduler, Hadoop Master Nodes |
| **Storage Nodes** | Store large volumes of data persistently | MongoDB, Cassandra, HDFS Data Nodes, S3 |
| **Replica Nodes** | Ensure redundancy and fault tolerance | Database Replicas (MySQL, PostgreSQL), File System Replicas |
| **Monitoring Nodes** | Track system health and performance | Prometheus, Nagios, AWS CloudWatch |
| **Security Nodes** | Handle authentication, encryption, and access control | OAuth Authentication Servers, Firewalls, SSL/TLS Terminators |
| **Load Balancer Nodes** | Distribute traffic for balanced system performance | HAProxy, AWS ELB, NGINX Load Balancer |
| **Failure Recovery Nodes** | Ensure system recovery and failover | Kubernetes Cluster Manager, PostgreSQL Failover |
| **Blockchain Nodes** | Validate transactions and maintain decentralized ledgers | Bitcoin Nodes, Ethereum Nodes, Proof-of-Stake Validators |

## Processing Model

> 

| **Processing Model** | **When to Use** | **Example Use Cases** |
| --- | --- | --- |
| **Batch Processing** | Large data sets, non-time-sensitive | Payroll, Log Analysis, Data Aggregation |
| **Real-Time Processing** | Low-latency, instant response required | Fraud Detection, Stock Trading |
| **Stream Processing** | Continuous, event-driven workloads | IoT Data, Web Analytics |

## Taxonomy of  Models In Distributed Systems

> Here's a table outlining different types of models in distributed systems:
> 

> These models provide foundational concepts and techniques for designing, implementing, and managing distributed systems, addressing various aspects such as consensus, transactions, synchronization, communication, replication, failure handling, and security.
> 

| **Model Type** | **Description** | **Examples** |
| --- | --- | --- |
| **Consensus Models** | Algorithms and protocols for achieving agreement among distributed processes or nodes on a single value, ensuring fault tolerance, consistency, and reliability. | Paxos, Raft, Zab, Viewstamped Replication, Byzantine Fault Tolerance (BFT) |
| **Transaction Guarantee Models** | Techniques for managing concurrent operations and ensuring transactions' atomicity, consistency, isolation, and durability (ACID) properties in distributed databases and systems. | Two-Phase Commit (2PC), Three-Phase Commit (3PC), Optimistic Concurrency Control, Serializable Snapshot Isolation (SSI), Multiversion Concurrency Control (MVCC) |
| **Synchronization (Coordination) Models** | Mechanisms for coordinating access to shared resources and managing concurrency in distributed systems, ensuring operations' consistency, correctness, and efficiency. | Locking mechanisms, semaphores, barriers, distributed transactions, message queues, distributed locks |
| **Communication Models** | Protocols and patterns for communication between distributed processes or nodes, enabling reliable message exchange, event notification, and data synchronization across the network. | Message Passing Interface (MPI), Remote Procedure Call (RPC), Publish-Subscribe (Pub/Sub), RESTful APIs, WebSocket, gRPC |
| **Replication Models** | Techniques for replicating data and state across distributed nodes or data centers, ensuring fault tolerance, scalability, and availability of services and data. | Master-slave replication, master-master replication, leader-based replication, passive replication, active-active replication |
| **Failure Handling Models** | Strategies and mechanisms for detecting, mitigating, and recovering from failures in distributed systems, ensuring system resilience and reliability in the face of faults and errors. | Heartbeat monitoring, failure detection algorithms, quorum-based techniques, fault-tolerant consensus algorithms, graceful degradation, circuit breakers |
| **Security Models** | Policies, protocols, and mechanisms for ensuring data confidentiality, integrity, and availability in distributed systems, protecting against unauthorized access, attacks, and data breaches. | Access control lists (ACLs), Role-based access control (RBAC), Public-key infrastructure (PKI), Encryption, Authentication protocols |
| **Consistency Models** | Specifies the consistency a distributed system guarantees regarding how updates are propagated and observed by different nodes or processes. | Eventual Consistency, Strong Consistency, Read Your Writes Consistency, Causal Consistency, Linearizability |
| **Service Discovery Models** | "Service Discovery Models" encompass various approaches for dynamically locating and managing services within distributed systems, ranging from centralized registries to decentralized protocols. | Service discovery models facilitate the dynamic identification and communication with services in distributed systems, such as Kubernetes DNS-based discovery or HashiCorp Consul's decentralized approach. |
| **Naming Models** | Naming models provide systematic approaches for identifying and addressing resources, services, or entities within distributed systems through unique and meaningful identifiers. | Hierarchical Naming,  Flat Naming, … |
| **Architectural Models** | … | … |

## Guaranteed Models in Distributed Systems

Here’s a table summarizing the guaranteed models in distributed systems:

| **Model** | **Description** |
| --- | --- |
| **At-Most-Once** | Ensures that a message or operation will be delivered or executed at most once, preventing duplicates but possibly missing messages. |
| **At-Least-Once** | Guarantees that a message or operation will be delivered or executed at least once, which may lead to duplicates if retries occur. |
| **Exactly-Once** | Guarantees that a message or operation will be delivered or executed exactly once, avoiding duplicates even with retries. |
| **Strong Consistency** | Ensures that all operations are seen by all nodes in the same order, providing a consistent view of the data across all nodes. |
| **Eventual Consistency** | Guarantees that all replicas will converge to the same state given enough time, allowing temporary inconsistencies but achieving consistency eventually. |
| **Durability** | Guarantees that once a transaction is committed, it will remain committed and survive subsequent failures or crashes. |
| **Fault Tolerance** | Ensures the system can continue operating and maintain its guarantees despite hardware or software failures. |
| **Isolation** | Ensures that transactions are executed in isolation from each other, with the outcome of one transaction not visible to others until it is committed. |

## **Communication Models**

> 
- **Shared Memory**:
    - Processes/threads communicate by reading/writing to shared memory.
    - Examples: Multithreaded programs, GPU programming.
- **Message Passing**:
    - Processes/threads communicate by sending and receiving messages.
    - Examples: MPI (Message Passing Interface), actor models (e.g., Akka, Erlang).
- **Hybrid Models**:
    - Combines shared memory and message passing.
    - Examples: Distributed shared memory (DSM), partitioned global address space (PGAS).

## Conceptual Model

> 

Multi-Node Processing System: Conceptual Model

## References

- [Consistency in Distributed Systems](https://mwhittaker.github.io/consistency_in_distributed_systems/)
- [Distributed Computing](https://en.wikipedia.org/wiki/Distributed_computing)
- [Distributed systems algorithms](https://en.wikipedia.org/wiki/List_of_algorithms)
- [Notes on Theory of Distributed Systems](http://www.cs.yale.edu/homes/aspnes/classes/465/notes.pdf)
- [Patterns of Distributed Systems](https://martinfowler.com/articles/patterns-of-distributed-systems/)
- [Two Generals and Time Machines](https://mwhittaker.github.io/blog/two_generals_and_time_machines/)
- [The Semantics of a Simple Language for Parallel Programming](http://www1.cs.columbia.edu/~sedwards/papers/kahn1974semantics.pdf)
- [Common Gateway Interface](https://www.wikiwand.com/en/Common_Gateway_Interface)
- [Understanding Raft - Part 2 (Raft leaders, logs, and safety)](https://www.micahlerner.com/2020/05/09/understanding-raft-consensus-part-2.html)
- https://github.com/dbremont/Epistecnica/tree/main/src/tecnica/documentorum/cto/platform
- [Distributed Systems Safety Research (jepsen)](https://jepsen.io/)
- Tango: Distributed Data Structures over a Shared Log, Mahesh Balakrishnan, Dahlia Malkhi, Ted Wobber, Ming Wu, Vijayan Prabhakaran, Michael Wei, John D. Davis, Sriram Rao, Tao Zou, Aviad Zuckk. SOSP 2013.
- Distributed Snapshots: Determining Global States of a Distributed System. K. Mani Chandy Leslie Lamport, ACM Transactions on Computer Systems, 1985.
- Virtual Time and Global States of Distributed Systems. Mattern, F. 1988.
- Practical uses of synchronized clocks in distributed systems. B. Liskov, 1991.
- The Drinking Philosophers Problem, K. M. Chandy, J. Misra, ACM TOPLAS 1984
- The Arrow Distributed Directory Protocol, Michael J. Demmer, M. Herlihy, DISC 1998.
- Hints for computer system design, Butler Lampson, 1983
- The role of distributed state, John Ousterhout, 1990
- SEDA: An Architecture for Well-Conditioned, Scalable Internet Services. Matt Welsh, David Culler, and Eric Brewer, SOSP 2001
- Crash only software, George Candea, Armando Fox, HotOS 2003
- On designing and deploying Internet scale services, James Hamilton, LISA 2007
- Life beyond Distributed Transactions: an Apostate’s Opinion, Pat Helland, CIDR 2007.
- Above the Clouds: A Berkeley View of Cloud Computing. Michael Armbrust, Armando Fox, Rean Griffith, Anthony D. Joseph, Randy H. Katz, Andrew Konwinski, Gunho Lee, David A. Patterson, Ariel Rabkin, Ion Stoica, Matei Zaharia, 2009.
- Cloud Programming Simplified: A Berkeley View on Serverless Computing, 2019.
- Ongaro, D., & Ousterhout, J. (n.d.). In Search of an Understandable Consensus Algorithm. 305.
- Reed, B., & Junqueira, F. P. (2008). A Simple Totally Ordered Broadcast Protocol. 1–6.
- Chandra, T., Griesemer, R., & Redstone, J. (2007). Paxos Made Live-An Engineering Perspective.
- Burrows, M. (2006). The Chubby Lock Service for Loosely-Coupled Distributed Systems.
- Lamport, L. (2001). Paxos Made Simple.
- Fischer, M. J., Lynch, N. A., & Paterson, M. S. (1985). Impossibility of Distributed Consensus With One Faulty Process. 32(2), 374–382.
- Lamport, L., Shostak, R., & Pease, M. (1982). The Byzantine Generals Problem.
- Castro, M., & Liskov, B. (1999, February). Practical Byzantine Fault Tolerance.
- Bailis, P., Davidson, A., Fekete, A., Ghodsi, A., & Hellerstein, J. M. (2013). Highly Available Transactions: Virtues and Limitations.
- Abadi, D. (2012). Consistency Tradeoffs in Modern Distributed Database System Design: CAP is Only Part of the Story. 45(2), 37–42.
- Kleppmann, M. (2015). A Critique of the CAP Theorem.
- Brewer, E. (2012). CAP Twelve Years Later: How the “Rules” Have Changed.
- Thomson, A., Diamond, T., Weng, S. C., Ren, K., Shao, P., & Abadi, D. J. (2012). Calvin: Fast Distributed Transactions for Partitioned Database Systems. 1–12.
- Thomson, A., Diamond, T., Weng, S. C., Ren, K., Shao, P., & Abadi, D. J. (2012). Calvin: Fast Distributed Transactions for Partitioned Database Systems. 1–12.
- Saito, Y., & Shapiro, M. (2005). Optimistic Replication. 37(1), 42–81.
- Fox, A., & Brewer, E. A. (1999). Harvest, Yield, and Scalable Tolerant Systems.
- Herlihy, Maurice P., and Jeannette M. Wing. “Linearizability: A Correctness Condition for Concurrent Objects.” ACM Transactions on Programming Languages and Systems (TOPLAS) 12.3 (1990): 463-492.
- Lamport, L. (1978). Time, Clocks, and the Ordering of Events in a Distributed System.
- Shapiro, M., Preguiça, N. M., Baquero, C., & Zawirski, M. (2011). A Comprehensive Study of Convergent and Commutative Replicated Data Types.
- Preguiça, N., Marquès, J. M., Shapiro, M., & Leţia, M. (2009). A Commutative Replicated Data Type for Cooperative Editing. 395–403.
- Letia, M., Preguiça, N., & Shapiro, M. (2009). CRDTs: Consistency Without Concurrency Control.
- Conway, N., Marczak, W. R., Alvaro, P., Hellerstein, J. M., & Maier, D. (2012). Logic and Lattices for Distributed Programming.
- Alvaro, P., Marczak, W. R., Conway, N., Hellerstein, J. M., Maier, D., & Sears, R. (2010). Dedalus: Datalog in Time and Space. 6702 LNCS, 262–281.
- Dean, J., & Ghemawat, S. (2008). MapReduce: Simplified Data Processing on Large Clusters. 51(1), 107–113.
- Abouzeid, A., Bajda-Pawlikowski, K., Abadi, D., Silberschatz, A., & Rasin, A. (2009). HadoopDB: an Architectural Hybrid of MapReduce and DBMS Technologies for Analytical Workloads. 2(1), 922–933.
- Waldo, J., Wyant, G., Wollrath, A., & Kendall, S. (1994). A Note on Distributed Computing.
- Corbett, J. C., Dean, J., Epstein, M., Fikes, A., Frost, C., Furman, J. J., Ghemawat, S., Gubarev, A., Heiser, C., Hochschild, P., Hsieh, W., Kanthak, S., Kogan, E., Li, H., Lloyd, A., Melnik, S., Mwaura, D., Nagle, D., Quinlan, S., … Woodford, D. (n.d.). Spanner: Google’s Globally-Distributed Database. 12, 251.
- Hunt, P., Konar, M., Grid, Y. !, Junqueira, F. P., Reed, B., & Research, Y. ! (n.d.). ZooKeeper: Wait-Free Coordination For Internet-Scale Systems.
- Birman, Ken. “A history of the virtual synchrony replication model.” Replication: Theory and Practice (2010): 91-120.
- Lakshman, A., & Malik, P. (2010). Cassandra - A Decentralized Structured Storage System. 44(2), 35–40. https://doi.org/10.1145/1773912.1773922
- DeCandia, G., Hastorun, D., Jampani, M., Kakulapati, G., Lakshman, A., Pilchin, A., Sivasubramanian, S., Vosshall, P., & Vogels, W. (2007). Dynamo: Amazon’s Highly Available Key-Value Store. 205–220.
- Sears, R. C. (2010). Stasis: Flexible Transactional Storage.
- Ghemawat, S., Gobioff, H., & Leung Google, S.-T. (2003). The Google File System.
- Brewer, E. A. (2001). Lessons from Giant-Scale Services. 5(4), 46–55.
- Brewer, Eric A. “Towards robust distributed systems.” PODC. Vol. 7. No. 10.1145. 2000.
- Fox, Armando, et al. “Cluster-Based Scalable Network Services.” Proceedings of the sixteenth ACM Symposium on Operating systems principles. 1997.
- Birman, Kenneth P. “The Process Group Approach to Reliable Distributed Computing.” Communications of the ACM 36.12 (1993): 37-53.
- Maxgio. (n.d.). A journey into the Linux scheduler. Retrieved July 12, 2022, from https://blog.maxgio.me/posts/linux-scheduler-journey/
- Bacon, J. (1992). Concurrent systems. Addison Wesley.
- Tanenbaum, A. S., van Steen, M. (2001). Distributed systems. Pearson.
- Kleppmann, M. (2021). Distributed Systems. https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/dist-sys-notes.pdf
- Whittaker, M. (n.d.). Consistency in Distributed Systems. Retrieved July 19, 2022, from https://mwhittaker.github.io/consistency_in_distributed_systems/
- Bernstein, P. A., Newcomer, E. (2009). Principles of Transaction Processing. In Principles of Transaction Processing (pp. 99–119). Elsevier.
- Bacon, J. (1992). Concurrent systems. Addison Wesley.
- Tanenbaum, A. S., van Steen, M. (2001). Distributed systems. Pearson.
- Kaashoek, M. Frans, and Jerome H. Saltzer. Principles of Computer System Design: An Introduction. Elsevier Science, 2009.
- “Java Concurrency in Practice”, Brian Goetz
- “Designing Data-Intensive Applications”, Martin Kleppmann
- Escriva, Robert, and Emin Gün Sirer. “The design and implementation of the warp transactional filesystem.” 13th {USENIX} Symposium on Networked Systems Design and Implementation ({NSDI} 16). 2016.
- [Distributed Systems](https://dl.acm.org/doi/pdf/10.1145/4547.4552)
- [Distributed transaction patterns for microservices compared](https://developers.redhat.com/articles/2021/09/21/distributed-transaction-patterns-microservices-compared)
- Learning about distributed systems: where to start? / [http://muratbuffalo.blogspot.com/2020/06/learning-about-distributed-systems.html](http://muratbuffalo.blogspot.com/2020/06/learning-about-distributed-systems.html) / [https://news.ycombinator.com/item?id=40037324](https://news.ycombinator.com/item?id=40037324) / [https://fly.io/dist-sys/](https://fly.io/dist-sys/)
- [UC Berkeley launches SkyPilot to help navigate soaring cloud costs](https://news.ycombinator.com/item?id=33964285)
- [Synchronization in Distributed Programs](https://dl.acm.org/doi/pdf/10.1145/357162.357163)
- [Consistency Models](https://jepsen.io/consistency)
- [The many faces of consistency](http://sites.computer.org/debull/A16mar/p3.pdf)
- [Awesome Distributed Systems](https://github.com/theanalyst/awesome-distributed-systems)
- [Distributed Systems Reading List](https://people.cs.rutgers.edu/~pxk/417/readinglist.html)
- [Firefox](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/firefox.md)
- [Data Streaming](note.html?n=technica/computation/telecom/data-streaming.md)
- https://dancres.github.io/Pages/
- https://ferd.ca/a-distributed-systems-reading-list.html
- [Operating System](note.html?n=technica/computation/operating-system.md)
- [Telecom](note.html?n=technica/computation/telecom.md)
- [‣](https://app.notion.com/p/57a6a0bb4bec4f7590dd95f4076ecdf2?pvs=21)
- [Concurrency](note.html?n=technica/computation/concurrency.md)
- https://github.com/dbremont/documentorum/tree/main/component/multinode
- https://geocar.sdf1.org/fast-servers.html