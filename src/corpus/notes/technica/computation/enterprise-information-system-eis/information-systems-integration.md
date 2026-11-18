---
tags: [note, integration]
---

# Information Systems Integration


> **Enterprise Systems Integration Models** encompass the methodologies and frameworks used to connect disparate systems, applications, and data sources within an organization to facilitate seamless communication and data exchange.
> 

![image.png](/assets/note/technica/computation/enterprise-information-system-eis/information-systems-integration/image.png)

## Interaction Styles

> Integration patterns describe *how a message is processed*; interaction styles describe *how two systems talk at all*. The style fixes the coupling — temporal, spatial and semantic — and therefore the failure modes, the latency and the operational cost of the link.

| Style | How it works | Coupling it creates | Where it fits |
| --- | --- | --- | --- |
| **Request-response** | The caller sends a request and blocks for the reply | Temporal and semantic: both sides must be up and agree on the contract | Synchronous APIs, user-facing reads, CRUD |
| **Event-driven** | A producer emits an event; consumers react when they can | Loose in time, tighter in schema: the event contract is the coupling | Notifications, state propagation, decoupled workflows |
| **Publish-subscribe** | A broker fans a message out to all subscribers | Spatial decoupling: the publisher does not know the subscribers | Many consumers of one fact, integration buses |
| **Streaming** | A continuous flow of records is consumed as it arrives | Ordering and offset semantics become the contract | Telemetry, logs, market data, change data capture |
| **Batch** | Files or record sets are exchanged on a schedule | Loose in time: the run window is the contract | Bulk settlement, reporting, legacy mainframe feeds |
| **File-based** | A shared filesystem or transfer drops a file for the other side | The path, the name and the format are the contract | Legacy interchange, partner drops, EDI over files |
| **Shared database** | Two systems read and write the same schema | The tightest coupling: the schema is the interface | Legacy integration, reporting replicas — and a known anti-pattern for services |
| **Remote procedure call** | A typed call to a remote function, as if it were local | The interface definition and its versioning | Internal service-to-service calls, gRPC, RPC-style APIs |

> The choice is usually made once and paid for repeatedly: a synchronous request-response link between two services turns every downstream outage into an upstream outage, while an event link buys availability at the price of eventual consistency. The message patterns in the next section are the internal mechanics of these styles.

## Integration Patterns

> 

| EIP | Description |
| --- | --- |
| Message Channel | A channel is a way to exchange messages between components or systems. Channels can be synchronous or asynchronous and use various communication protocols, such as JMS, AMQP, or HTTP. |
| Message Router | A component that directs incoming messages to one or more destinations based on predefined criteria, such as message content, headers, or routing rules. |
| Message Filter | A component that evaluates incoming messages against specified criteria and selectively passes or discards them based on the evaluation result. |
| Message Translator | A component that converts messages from one data format or protocol to another to facilitate communication between systems with different interfaces or data representations. |
| Message Endpoint | Endpoints represent the origin or destination of a message within an integration flow. They can be connectors to external systems, service invocations, or event listeners and use various transport protocols and APIs. |
| Message Splitter | A component that breaks down a single message into multiple smaller messages, each containing a subset of the original message's data. It helps process large messages or split data for parallel processing. |
| Message Aggregator | Aggregation is a component that combines multiple related messages into a single message to simplify downstream processing. Aggregation strategies can include collecting, grouping, or merging messages based on common attributes or identifiers. |
| Content-Based Router | A component that routes messages to different destinations based on message content or attributes. Routing decisions are made dynamically at runtime based on content-based rules or expressions. |
| Message Store | Message stores are storage mechanisms that temporarily store messages during integration processing. They provide persistence, queuing, and retrieval features to ensure reliable message delivery and processing. |
| Event-Driven Consumer | A component that consumes messages or events from an external system or message channel and triggers downstream processing or actions in response to received events. Event-driven consumers enable asynchronous and event-based integration. |
| Transactional Client | A component that participates in distributed transactions and ensures that message processing is atomic and consistent across multiple systems. Transactional clients coordinate transactional behavior between messaging systems and business logic. |
| Scatter-Gather | A component that sends a single request message to multiple recipients in parallel and aggregates the responses into a single response message. Useful for fan-out and fan-in scenarios where multiple systems need to be queried or invoked concurrently. |
| Dead Letter Channel | A mechanism for handling messages that cannot be processed successfully and need to be routed to an alternative destination or logged for analysis. Dead letter channels help manage error handling and ensure handling of failed messages properly. |
| Message Broker | Message brokers are middleware components that facilitate communication and message exchange between distributed applications or services. They often provide features such as routing, message queuing, publish-subscribe messaging, and message transformation. |

## Toolset

| Integration Model | Example Tools/Frameworks |
| --- | --- |
| ETL (Extract, Transform, Load) | [Apache NiFi](https://nifi.apache.org/),  … |
| Change Data Capture (CDC) | [Apache Kafka Connect](https://docs.confluent.io/platform/current/connect/index.html),  [Debezium](https://debezium.io/),  … |
| API-Based Integration | [MuleSoft Anypoint Platform](https://www.mulesoft.com/), [Dell Boomi](https://boomi.com/), [Airbyte](https://airbyte.com/), [IBM App Connect](https://www.ibm.com/products/app-connect),  … |
| Messaging Systems | Apache Kafka - RabbitMQ - Apache ActiveMQ - AWS SQS (Simple Queue Service) - Google Cloud Pub/Sub |
| Database Replication | MySQL Replication - PostgreSQL Replication - SQL Server Replication - Oracle GoldenGate - Dbvisit Replicate |
| File-Based Integration | WinSCP - FileZilla - AWS DataSync |
| Custom Integration | - Spring Integration - Apache Beam - Apache Flink - Apache Storm - Apache Spark, - Apache Camel - Apache Airflow |
| … | … |

## References

- [Airbyte](https://airbyte.com/)
- [Camunda](https://camunda.com/)
- [Boomi, LP](https://en.wikipedia.org/wiki/Boomi,_LP)
- [Apache NiFi](https://nifi.apache.org/documentation/v2/)
- [System Integration](https://en.wikipedia.org/wiki/System_integration)
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/)
- [Distributed Computing](/view.html?p=notes/technica/computation/distributed-computing.md)
- [Integration platform as a service (iPaaS)](https://en.wikipedia.org/wiki/Cloud-based_integration)