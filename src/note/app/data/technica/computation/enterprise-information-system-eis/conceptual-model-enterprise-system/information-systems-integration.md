---
tags: [integration]
---

# Information Systems Integration


> **Enterprise Systems Integration Models** encompass the methodologies and frameworks used to connect disparate systems, applications, and data sources within an organization to facilitate seamless communication and data exchange.
> 

![image.png](data/technica/computation/enterprise-information-system-eis/conceptual-model-enterprise-system/assets/information-systems-integration/image.png)

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
- [Distributed Computing](note.html?n=technica/computation/distributed-computing.md)
- [Integration platform as a service (iPaaS)](https://en.wikipedia.org/wiki/Cloud-based_integration)