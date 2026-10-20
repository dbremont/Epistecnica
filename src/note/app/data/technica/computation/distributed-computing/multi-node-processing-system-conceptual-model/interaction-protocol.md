---
tags: [protocol]
---

# Interaction Protocol


> **Interaction Protocol (API Technology)** refers to the structured set of rules and conventions governing data exchange and communication between software entities, typically defining request-response patterns, message formats, transport mechanisms, and error-handling semantics to facilitate interoperability across distributed systems.
> 

- [ ]  Aka. Application Level Protocol in the OSI Model.
- [ ]  Why having this entry?  Why not in telecom?
- [ ]  In the Communication Stack  In Which Layer does these protocols belongs to?

QA:

- What file formats are commonly used for APIs, and why is Excel not suitable? How much time and resources does serialization/deserialization take for each format?
- …

## **API’S Technology**

| **API Technology** | **Protocol** | **Description** | **Common Use Cases** | **Data Format** |
| --- | --- | --- | --- | --- |
| **REST** | HTTP/HTTPS | Stateless client-server architecture using standard HTTP methods (GET, POST, etc.). | Web services, mobile apps, cloud APIs | JSON, XML |
| **GraphQL** | HTTP/HTTPS | Query-based API that allows clients to request specific data structures. | Flexible APIs for web and mobile apps | JSON |
| **gRPC** | HTTP/2 | High-performance RPC framework using Protocol Buffers (protobuf). | Microservices, real-time communication | Protobuf |
| **SOAP** | HTTP, SMTP, etc. | XML-based protocol for structured messaging and web services. | Enterprise applications, banking, legacy systems | XML |
| **WebSockets** | WS/WSS | Full-duplex communication for real-time data transfer. | Chat applications, live notifications, gaming | JSON, Binary |
| **MQTT** | TCP/IP | Lightweight messaging protocol for IoT devices. | IoT, real-time monitoring | Binary, JSON |
| **AMQP** | TCP/IP | Message queuing protocol for distributed systems. | Messaging brokers (RabbitMQ, Kafka) | Binary |
| **CoAP** | UDP | Lightweight RESTful API optimized for constrained devices. | IoT, low-power networks | JSON, CBOR |
| **WebRTC** | UDP/TCP | Peer-to-peer communication for real-time media streaming. | Video calls, VoIP, live-streaming | Binary |
| **XMPP** | TCP/IP | Extensible messaging protocol for real-time communication. | Instant messaging, IoT, presence tracking | XML |

## Intercrop File Format

> 

| **File Format** | **Why Used?** | **Serialization Speed** | **Deserialization Speed** | **Size Efficiency** | **Human Readable?** |
| --- | --- | --- | --- | --- | --- |
| **JSON** | Lightweight, human-readable, widely used in REST & GraphQL APIs. | Medium | Medium | Moderate | ✅ Yes |
| **XML** | Structured, supports schemas (XSD), used in SOAP APIs. | Slow | Slow | Large | ✅ Yes |
| **Protocol Buffers (Protobuf)** | Compact, efficient binary format, ideal for gRPC. | Fast | Fast | Small | ❌ No |
| **MessagePack** | Binary, smaller than JSON, fast serialization. | Fast | Fast | Small | ❌ No |
| **CBOR** | Efficient binary format for IoT (e.g., CoAP). | Fast | Fast | Small | ✅ Optional |
| **Avro** | Optimized for big data (Apache Kafka, Hadoop). | Fast | Fast | Small | ❌ No |
| **YAML** | Human-readable, used in API configs (OpenAPI, Kubernetes). | Slow | Slow | Large | ✅ Yes |

## Pagination

> 

![image.png](data/technica/computation/distributed-computing/multi-node-processing-system-conceptual-model/assets/interaction-protocol/image.png)

## References

- [Telecom](note.html?n=technica/computation/telecom.md)
- [ ]  https://blog.bytebytego.com/p/api-protocols-101-a-guide-to-choose?utm_source=substack&utm_medium=email
- [ ]  https://github.com/dbremont/system-design-labs
- [ ]  https://github.com/csiglab/networking-labs
- [ ]  [Representation](https://app.notion.com/p/Representation-4afbffa763ec46eeb10d8c87c248edf1?pvs=21)
- https://github.com/csiglab/performance-labs
- [MessagePack](note.html?n=technica/computation/representation/conceptual-model-computational-representation/messagepack.md)