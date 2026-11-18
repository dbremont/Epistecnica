---
tags: [note, production]
---

# Software Technology

> A minimal, structural vocabulary to reason about how software capabilities are built up from foundational operational procedures.

## Formulation

> **Software Technology** consists of the formal description of processes that a machine executes to drive actuators, manipulate data, or control system behavior. It encompasses the design and integration of operational techniques, technical objects, and constitutive principles into deployable products that achieve specific effects in a controlled environment.

## Terminology

> Note: Technical objects are constructed from combinations of other technical objects and the operational techniques that underpin them.

> Note: A Product is also a Technical Object—one that aggregates multiple technical objects and operational techniques into a deployable, externally oriented system. However, in this document we will use the term Product specifically to refer to the final user–facing object.

| **Term**                       | **Definition**                                                                                                                                                             | **Case(s)**                                                                                                                                                                                                   |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Foundational Research**      | Research aimed at generating new scientific knowledge, theories, or principles without immediate practical application, forming the basis for future technical innovation. | Development of formal models of distributed consensus; research on type systems; mathematical foundations of cryptography.                                                                                    |
| **Technical Research**         | Research focused on transforming foundational knowledge into new technical objects, operational techniques, or methods that can be applied in systems and products.        | Implementing Raft for distributed systems; designing a new compiler optimization; developing a scalable transaction log subsystem.                                                                            |
| **Operational Technique**      | A repeatable, competence-based procedure used to achieve a specific operational effect under constraints.                                                                  | Hashing a key; applying a lock-free increment; scheduling a coroutine; parsing a token; writing an append-only log entry.                                                                                     |
| **Technical Object**           | A structural artifact that embodies operational techniques into a stable, reproducible system with defined interfaces and invariants.                                      | A key–value store (etcd); a scheduler; a compiler frontend; a transaction log subsystem; a virtual machine.                                                                                                   |
| **Constitutive Technique**     | The generative architectural logic that defines how a technical object is constructed, organized, and made operational as a class of objects.                              | Raft (constitutive for etcd); LSM-tree design (constitutive for log-structured storage engines); SSA form (constitutive for modern optimizing compilers); Paxos (constitutive for replicated state machines). |
| **Representational Technique** | The method or format used to encode, model, or depict information, processes, or operational states so that they can be manipulated, stored, or communicated effectively.  | Binary encoding of audio for voice processing; JSON or protobuf for structured data interchange; abstract syntax trees in compilers; graphical models for system architecture.                                |
| **Product(s)**                 | The realized, packaged, deployable system—enabled by operational techniques and technical objects—that exposes a coherent set of capabilities to users and environments.   | YouTube; GitHub; a cloud database service; a container orchestration platform.                                                                                                                                |

## Technical Object Space

> Which technical objects are used to build final products?

| **Category**           | **Technical Object**      | **Description**                                                                                | **Constitutive Technique(s)**                                                                                |
| ---------------------- | ------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Storage & Coordination | **etcd**                  | A distributed key-value store for configuration and service discovery in cloud-native systems. | Consensus algorithms (Raft), key-value storage operations, snapshotting, log compaction.                     |
| Storage & Caching      | **Redis**                 | In-memory data structure store used for caching, messaging, and ephemeral storage.             | Memory management, data eviction policies, pub/sub messaging, persistence techniques (RDB/AOF).              |
| Messaging & Streaming  | **Kafka**                 | Distributed streaming platform for event ingestion and message queuing.                        | Partitioning, replication, log compaction, producer/consumer APIs, message ordering guarantees.              |
| Databases              | **PostgreSQL**            | Relational database system providing ACID-compliant storage and querying.                      | Query parsing/optimization, transaction management, buffer management, indexing, WAL (write-ahead log).      |
| Web & Proxy            | **Nginx**                 | High-performance web server and reverse proxy for HTTP and TCP traffic.                        | Event-driven architecture, asynchronous I/O, connection handling, caching techniques, load balancing.        |
| OS Extensions          | **Linux Kernel Module**   | Loadable module extending kernel functionality (e.g., device drivers, filesystems).            | System calls, interrupt handling, memory management, kernel API integration.                                 |
| Security & Crypto      | **OpenSSL Library**       | Cryptographic library enabling secure communication over networks.                             | Symmetric/asymmetric encryption, hashing, digital signature algorithms, key management.                      |
| Container Orchestration| **Kubernetes API Server** | Control plane component exposing cluster API to manage workloads.                              | REST API handling, resource validation, etcd integration, admission control, authentication/authorization.   |
| RPC & Communication    | **gRPC Framework**        | Remote procedure call system for connecting services in distributed applications.              | Protocol buffers serialization, connection multiplexing, streaming, authentication, retry/backoff logic.     |
| Container Runtime      | **Docker Engine**         | Container runtime for packaging, distributing, and running containerized applications.         | Image layering, container namespaces, cgroups resource management, filesystem overlay, container networking. |

## Actuator Space

> Which peripherals or actuators can a computation control or drive?

| **Category**               | **Actuator / Peripheral**                  | **Description**                                      | **Computing Role**                                                       |
| -------------------------- | ------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------------------ |
| Mechanical                 | Motor / Servo                              | Converts electrical signals into mechanical movement | Control position, speed, or torque in robots, vehicles, or machinery     |
| Electrical                 | Relay / Switch                             | Electrically controls circuits or devices            | Toggle power or signals in automated systems                             |
| Optical                    | LED / Display / Monitor                    | Emits or modulates light signals                     | Visual feedback, user interface, or system monitoring                    |
| Acoustic / Audio           | Speaker / Buzzer / Headphones              | Converts electrical signals into sound               | Alerts, notifications, audio output, or user feedback                    |
| Thermal                    | Heater / Cooler                            | Modulates temperature via electrical input           | Climate control, process regulation, or thermal testing                  |
| Magnetic / Electromagnetic | Solenoid / Electromagnet                   | Generates motion or force using magnetic fields      | Actuate locks, valves, or magnetic mechanisms                            |
| Fluidic / Pneumatic        | Pump / Valve                               | Controls the flow of liquids or gases                | Automated fluid delivery, hydraulics, or pneumatic systems               |
| Network / Communication    | Network Interface / Modem / Router         | Sends signals over wired or wireless channels        | Trigger remote devices, IoT actuators, distributed systems, or messaging |
| Storage / Memory           | Disk / Flash / Tape                        | Reads/writes persistent data                         | Data logging, buffering, or caching outputs                              |
| Haptic / Tactile           | Vibration Motor / Force Feedback           | Provides physical feedback to users                  | Tactile alerts, haptic interfaces, or immersive control systems          |
| Sensors as Actuators       | Camera with motorized lens / Lidar / Radar | Can actively adjust or emit signals                  | Actively scan, illuminate, or emit signals based on computation          |

## References

- [Computing](https://en.wikipedia.org/wiki/Computing)
