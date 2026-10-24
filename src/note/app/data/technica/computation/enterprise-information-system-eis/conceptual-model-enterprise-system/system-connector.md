---
tags: [integration]
---

# System Connector


> In this note  we will explore the notion of a ‘**System Connector**’.
> 

> What kind of technical element establishes access to and communication with another system, without performing the integration itself? A **System Connector.**
> 

## Formulation

### What type of technical element is a `System Connector`?

> A **System Connector** is a technical element that establishes the access and communication channel between a system and another system. It provides the technical means through which communication can occur—such as connection, authentication, authorization, and protocol handling—without performing the higher-level integration itself.
> 

### What is the recursive technical-element decomposition of a `System Connector`?

> **Type:** a connector is typed here as a `Technical Element Set` — configuration, interface, control, security, feedback, and specification parts cooperating to establish the channel — readable as a `Technical Interface`, since the element's function *is* the established access boundary. Concrete connectors (Stripe, Kafka, LDAP) appear as cases below, not as decomposition rows.
>
> **Boundary:** this table decomposes one vendor-neutral connector; deployment values (timeouts, hosts, keys) live in the case sections.
>
> **Stopping rule:** a row is terminal when it names a configuration attribute, a parameter, a protocol, a mechanism, or an interface surface.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element Set` → System Connector | Connector ensemble: the access-and-communication element assembled from configuration, interface, control, and specification parts. |
| `Technical Element Set` → System Connector → `Technical Configuration` | Grouping: technical configuration elements of the connector. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration | Configuration defining how the connector establishes and maintains communication. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Parameter` | Grouping: technical parameter elements of Connector Configuration. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Parameter` → Connection Parameters | Parameters governing establishment and behavior of the connection. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Parameter` → Connection Parameters → `Technical Parameter` | Grouping: technical parameter elements of Connection Parameters. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Parameter` → Connection Parameters → `Technical Parameter` → Connection Timeout | Parameter defining the maximum waiting period for a connection operation. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Parameter` → Connection Parameters → `Technical Parameter` → Retry Parameter | Parameter defining how failed connection operations are retried. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Parameter` → Connection Parameters → `Technical Parameter` → Keepalive Parameter | Parameter defining how connection liveness is maintained or detected. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Configuration` | Grouping: technical configuration elements of Connector Configuration. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Configuration` → Endpoint Configuration | Configuration identifying the remote system endpoint to which communication is established. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Configuration` → Endpoint Configuration → `Technical Parameter` | Grouping: technical parameter elements of Endpoint Configuration. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Configuration` → Endpoint Configuration → `Technical Parameter` → Endpoint Address | Address identifying the remote communication endpoint. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Configuration` → Endpoint Configuration → `Technical Parameter` → Endpoint Port | Port identifying the network service used by the endpoint. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Configuration` → Protocol Configuration | Configuration specifying the communication protocol and its operational parameters. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Configuration` → Protocol Configuration → `Technical Parameter` | Grouping: technical parameter elements of Protocol Configuration. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Configuration` → Protocol Configuration → `Technical Parameter` → Protocol Version | Configuration specifying the version of the communication protocol or protocol implementation. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Configuration` → Protocol Configuration → `Technical Configuration` | Grouping: technical configuration elements of Protocol Configuration. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Configuration` → Protocol Configuration → `Technical Configuration` → Message Format Configuration | Configuration specifying the representation used for exchanged messages. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Configuration` → Authentication Configuration | Configuration specifying how the connector establishes the identity of the connecting party. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Connector Configuration → `Technical Configuration` → Authorization Configuration | Configuration specifying what the connector is permitted to access or perform. |
| `Technical Element Set` → System Connector → `Technical Interface` | Grouping: technical interface elements of the connector. |
| `Technical Element Set` → System Connector → `Technical Interface` → Connection Interface | Boundary through which the connector establishes communication with the external system. |
| `Technical Element Set` → System Connector → `Technical Interface` → Connection Interface → `Technical Interface` | Grouping: technical interface elements of Connection Interface. |
| `Technical Element Set` → System Connector → `Technical Interface` → Connection Interface → `Technical Interface` → Local Endpoint | Interface endpoint exposed by the local system for the connector. |
| `Technical Element Set` → System Connector → `Technical Interface` → Connection Interface → `Technical Interface` → Remote Endpoint | Interface endpoint exposed by the external system to receive communication. |
| `Technical Element Set` → System Connector → `Technical Interface` → Connection Interface → `Technical Interface` → Communication Channel | Technical path through which information is transmitted between the endpoints. |
| `Technical Element Set` → System Connector → `Technical Interface` → Connection Interface → `Technical Interface` → Communication Channel → `Technical Mechanism` | Grouping: technical mechanism elements of Communication Channel. |
| `Technical Element Set` → System Connector → `Technical Interface` → Connection Interface → `Technical Interface` → Communication Channel → `Technical Mechanism` → Transport Mechanism | Mechanism responsible for transporting information across the communication channel. |
| `Technical Element Set` → System Connector → `Technical Interface` → Connection Interface → `Technical Interface` → Communication Channel → `Technical Standard` | Grouping: technical standard elements of Communication Channel. |
| `Technical Element Set` → System Connector → `Technical Interface` → Connection Interface → `Technical Interface` → Communication Channel → `Technical Standard` → Communication Protocol | Rules governing the exchange of information across the channel. |
| `Technical Element Set` → System Connector → `Technical Interface` → Connection Interface → `Technical Interface` → Communication Channel → `Technical Configuration` | Grouping: technical configuration elements of Communication Channel. |
| `Technical Element Set` → System Connector → `Technical Interface` → Connection Interface → `Technical Interface` → Communication Channel → `Technical Configuration` → Channel Configuration | Configuration defining operational characteristics of the communication channel. |
| `Technical Element Set` → System Connector → `Technical Security` | Grouping: technical security elements of the connector. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control | Technical means by which access to the external system is established and constrained. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` | Grouping: technical security elements of Access Control. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authentication Mechanism | Mechanism establishing the identity of the connecting system, agent, or process. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authentication Mechanism → `Technical Mechanism` | Grouping: technical mechanism elements of Authentication Mechanism. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authentication Mechanism → `Technical Mechanism` → Credential | Technical information used to establish identity. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authentication Mechanism → `Technical Mechanism` → Credential → `Technical Configuration` | Grouping: technical configuration elements of Credential. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authentication Mechanism → `Technical Mechanism` → Credential → `Technical Configuration` → Credential Configuration | Configuration defining how credentials are supplied or referenced. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authentication Mechanism → `Technical Standard` | Grouping: technical standard elements of Authentication Mechanism. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authentication Mechanism → `Technical Standard` → Authentication Protocol | Protocol governing the exchange used to establish identity. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authentication Mechanism → `Technical Mechanism` → Authentication Method | Concrete method by which the connector supplies authentication information. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authorization Mechanism | Mechanism determining which resources or operations the authenticated connector may access. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authorization Mechanism → `Technical Specification` | Grouping: technical specification elements of Authorization Mechanism. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authorization Mechanism → `Technical Specification` → Access Policy | Rules defining permitted and prohibited accesses or operations. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authorization Mechanism → `Technical Requirement` | Grouping: technical requirement elements of Authorization Mechanism. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authorization Mechanism → `Technical Requirement` → Permission | Specific permitted operation or resource access granted to the connector. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authorization Mechanism → `Technical Evaluation` | Grouping: technical evaluation elements of Authorization Mechanism. |
| `Technical Element Set` → System Connector → `Technical Security` → Access Control → `Technical Security` → Authorization Mechanism → `Technical Evaluation` → Access Decision | Decision determining whether a requested access or operation is permitted. |
| `Technical Element Set` → System Connector → `Technical Mechanism` | Grouping: technical mechanism elements of the connector. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Protocol Handler | Technical element responsible for implementing the communication protocol at the connector boundary. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Protocol Handler → `Technical Mechanism` | Grouping: technical mechanism elements of Protocol Handler. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Protocol Handler → `Technical Mechanism` → Protocol Implementation | Operative implementation of the communication protocol. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Protocol Handler → `Technical Mechanism` → Protocol Implementation → `Technical Mechanism` | Grouping: technical mechanism elements of Protocol Implementation. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Protocol Handler → `Technical Mechanism` → Protocol Implementation → `Technical Mechanism` → Message Encoder | Converts structured information into the representation required by the protocol. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Protocol Handler → `Technical Mechanism` → Protocol Implementation → `Technical Mechanism` → Message Decoder | Converts received protocol representations into usable structured information. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Protocol Handler → `Technical Mechanism` → Protocol Implementation → `Technical Standard` | Grouping: technical standard elements of Protocol Implementation. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Protocol Handler → `Technical Mechanism` → Protocol Implementation → `Technical Standard` → Message Format | Formal representation governing the structure of exchanged messages. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Protocol Handler → `Technical Mechanism` → Protocol Implementation → `Technical Mechanism` → Request Handler | Technical element responsible for constructing and processing outgoing protocol requests. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Protocol Handler → `Technical Mechanism` → Protocol Implementation → `Technical Mechanism` → Response Handler | Technical element responsible for receiving and processing protocol responses. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connection Manager | Technical element responsible for establishing, maintaining, and terminating the communication connection. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connection Manager → `Technical Act` | Grouping: technical act elements of Connection Manager. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connection Manager → `Technical Act` → Connection Establishment | Operation that creates the communication connection. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connection Manager → `Technical Maintenance` | Grouping: technical maintenance elements of Connection Manager. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connection Manager → `Technical Maintenance` → Connection Maintenance | Operation that preserves an established connection during its operational lifetime. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connection Manager → `Technical Act` → Connection Termination | Operation that deliberately closes the communication connection. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connection Manager → `Technical Act` → Connection Retry | Operation that attempts to re-establish communication after a recoverable failure. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connection Manager → `Technical Act` → Connection Timeout Handling | Operation for handling failure to establish or maintain communication within the configured period. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Session Manager | Technical element responsible for maintaining the logical communication session where the protocol requires one. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Session Manager → `Technical Configuration` | Grouping: technical configuration elements of Session Manager. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Session Manager → `Technical Configuration` → Session State | Technical state representing the current logical communication session. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Session Manager → `Technical Mechanism` | Grouping: technical mechanism elements of Session Manager. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Session Manager → `Technical Mechanism` → Session Identifier | Identifier used to associate communication with a particular session. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Session Manager → `Technical Lifecycle` | Grouping: technical lifecycle elements of Session Manager. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Session Manager → `Technical Lifecycle` → Session Lifecycle Control | Control governing creation, continuation, expiration, and termination of a logical session. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Communication State | Operational state describing the current condition of the connector's communication relationship. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Communication State → `Technical Property` | Grouping: technical property elements of Communication State. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Communication State → `Technical Property` → Connection State | State of the underlying communication connection. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Communication State → `Technical Property` → Authentication State | State indicating the current result or condition of authentication. |
| `Technical Element Set` → System Connector → `Technical Configuration` → Communication State → `Technical Property` → Authorization State | State indicating the access permissions currently applicable to the connector. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connector Control | Technical control logic governing connector operation. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connector Control → `Technical Mechanism` | Grouping: technical mechanism elements of Connector Control. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connector Control → `Technical Mechanism` → Connection Control Logic | Logic governing connection establishment, maintenance, retry, and termination. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connector Control → `Technical Mechanism` → Access Control Logic | Logic applying authentication and authorization decisions. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connector Control → `Technical Mechanism` → Protocol Control Logic | Logic governing protocol-compliant communication. |
| `Technical Element Set` → System Connector → `Technical Mechanism` → Connector Control → `Technical Mechanism` → Error Handling Logic | Logic governing detection, classification, and handling of connector errors. |
| `Technical Element Set` → System Connector → `Technical Security` → Connector Security | Security mechanisms protecting the connector and its communication relationship. |
| `Technical Element Set` → System Connector → `Technical Security` → Connector Security → `Technical Security` | Grouping: technical security elements of Connector Security. |
| `Technical Element Set` → System Connector → `Technical Security` → Connector Security → `Technical Security` → Credential Protection | Protection of credentials used for authentication. |
| `Technical Element Set` → System Connector → `Technical Security` → Connector Security → `Technical Security` → Channel Protection | Protection of information transmitted through the communication channel. |
| `Technical Element Set` → System Connector → `Technical Security` → Connector Security → `Technical Security` → Channel Protection → `Technical Mechanism` | Grouping: technical mechanism elements of Channel Protection. |
| `Technical Element Set` → System Connector → `Technical Security` → Connector Security → `Technical Security` → Channel Protection → `Technical Mechanism` → Encryption Mechanism | Mechanism that transforms information to protect it from unauthorized disclosure. |
| `Technical Element Set` → System Connector → `Technical Security` → Connector Security → `Technical Security` → Channel Protection → `Technical Mechanism` → Integrity Mechanism | Mechanism that enables detection or prevention of unauthorized modification of transmitted information. |
| `Technical Element Set` → System Connector → `Technical Feedback` | Grouping: technical feedback elements of the connector. |
| `Technical Element Set` → System Connector → `Technical Feedback` → Connector Monitoring | Technical means for obtaining information about connector operation and state. |
| `Technical Element Set` → System Connector → `Technical Feedback` → Connector Monitoring → `Technical Feedback` | Grouping: technical feedback elements of Connector Monitoring. |
| `Technical Element Set` → System Connector → `Technical Feedback` → Connector Monitoring → `Technical Feedback` → Connection Status | Information representing the current connection condition. |
| `Technical Element Set` → System Connector → `Technical Feedback` → Connector Monitoring → `Technical Feedback` → Authentication Result | Feedback indicating the outcome of authentication. |
| `Technical Element Set` → System Connector → `Technical Feedback` → Connector Monitoring → `Technical Feedback` → Authorization Result | Feedback indicating the outcome of an authorization decision. |
| `Technical Element Set` → System Connector → `Technical Feedback` → Connector Monitoring → `Technical Failure` | Grouping: technical failure elements of Connector Monitoring. |
| `Technical Element Set` → System Connector → `Technical Feedback` → Connector Monitoring → `Technical Failure` → Communication Error | Feedback representing a failure occurring during communication. |
| `Technical Element Set` → System Connector → `Technical Feedback` → Connector Monitoring → `Technical Feedback` → Connection Metrics | Measurements representing quantitative characteristics of connector operation. |
| `Technical Element Set` → System Connector → `Technical Specification` | Grouping: technical specification elements of the connector. |
| `Technical Element Set` → System Connector → `Technical Specification` → Connector Interface Specification | Formal specification defining the conditions under which the connector can communicate with the external system. |
| `Technical Element Set` → System Connector → `Technical Specification` → Connector Interface Specification → `Technical Specification` | Grouping: technical specification elements of Connector Interface Specification. |
| `Technical Element Set` → System Connector → `Technical Specification` → Connector Interface Specification → `Technical Specification` → Endpoint Specification | Specification of the communication endpoints. |
| `Technical Element Set` → System Connector → `Technical Specification` → Connector Interface Specification → `Technical Specification` → Protocol Specification | Specification of the communication rules and message exchange. |
| `Technical Element Set` → System Connector → `Technical Specification` → Connector Interface Specification → `Technical Specification` → Security Specification | Specification of authentication, authorization, and communication-security requirements. |

## How to Characterize a `System Connector`?

> Let’s take the **`Stripe API Connector`** as grounding for this de-construction.
> 

```bash
System Connector
├── Connector Configuration
├── Connection Interface
│   └── Connector Interface Specification
├── Access Control
│   └── Authentication Mechanism
├── Protocol Handler
├── Connection Manager
├── Session Manager
├── Communication State
├── Connector Control
├── Connector Security
└── Connector Monitoring
```

| **Characteristic Dimension** | **Description** | **Value Set** | **Case** |
| --- | --- | --- | --- |
| **Connector Configuration** | Configuration that specifies how the connector establishes and operates a connection, including endpoint, credentials, protocol, timeouts, and connection parameters. |  | **Stripe API Connector Configuration** |
| **Connection Interface** | The technical interface through which the connector exposes or obtains access to the connected system. |  | **Stripe REST API Interface** |
| **Access Control** | Technical mechanisms that determine whether the connector is permitted to establish and use the connection. |  | **Stripe API Access Control** |
| **Protocol Handler** | Technical element that implements the communication protocol used to exchange messages with the connected system. |  | **HTTPS/HTTP Protocol Handler** |
| **Connection Manager** | Technical element responsible for establishing, maintaining, reusing, and terminating connections to the connected system. |  | **HTTP Connection Manager** |
| **Session Manager** | Technical element responsible for creating, maintaining, renewing, and terminating communication sessions when the connection model is session-oriented. |  | **Stripe API Session Management** |
| **Communication State** | The current state and relevant state information of the communication relationship, such as connected, disconnected, authenticated, or failed. |  | **Stripe Connector Connection State** |
| **Connector Control** | Technical control mechanisms that govern connector operation, including retries, timeouts, rate limiting, failure handling, and connection termination. |  | **Stripe API Retry and Rate-Limit Control** |
| **Connector Security** | Technical mechanisms that protect the connector and its communication from unauthorized access, disclosure, alteration, or misuse. |  | **TLS-secured Stripe API Communication** |
| **Connector Monitoring** | Technical mechanisms that observe connector operation and record relevant communication events, failures, latency, availability, and usage. |  | **Stripe API Request Monitoring** |
| **Connector Interface Specification** | Formal specification defining how the connector accesses and communicates with the connected system, including endpoints, operations, message structures, and communication rules. |  | **Stripe API Specification** |

## System Connector Type Space

| System Connector Type | Type Characterization | Description | Instance(s) |
| --- | --- | --- | --- |
| **Database Connector** | Connector → Database System | Establishes and manages communication with a database system for querying, reading, writing, and transaction operations. | PostgreSQL Connector; MySQL Connector; Oracle Connector |
| **API Connector** | Connector → API | Establishes communication with a software system through an exposed programmatic interface. | Stripe API Connector; Salesforce API Connector |
| **Web Service Connector** | Connector → Web Service | Establishes communication with a remotely exposed software service through a defined service interface. | SOAP Web Service Connector |
| **HTTP Connector** | Connector → HTTP Interface | Communicates with a system through HTTP/HTTPS request-response interactions. | REST HTTP Connector |
| **Message Queue Connector** | Connector → Message Queue | Connects a system to a message queue for producing and/or consuming messages. | RabbitMQ Connector; Amazon SQS Connector |
| **Message Broker Connector** | Connector → Message Broker | Connects to a message broker for publishing, consuming, routing, or mediating messages. | Kafka Connector; RabbitMQ Connector |
| **Event Stream Connector** | Connector → Event Stream | Establishes communication with a continuous event or data stream. | Kafka Stream Connector |
| **File Transfer Connector** | Connector → File Transfer System | Transfers files between systems using a file-transfer protocol or service. | SFTP Connector; FTP Connector |
| **File System Connector** | Connector → File System | Provides access to files and directories maintained by another filesystem or storage system. | Network File System Connector |
| **Object Storage Connector** | Connector → Object Storage System | Communicates with an object-storage system for storing and retrieving objects. | Amazon S3 Connector |
| **Cloud Storage Connector** | Connector → Cloud Storage System | Connects to a remotely hosted cloud storage service. | Google Cloud Storage Connector |
| **Directory Service Connector** | Connector → Directory Service | Connects to a directory system for retrieving and managing identities, groups, and organizational information. | LDAP Connector; Active Directory Connector |
| **Identity Provider Connector** | Connector → Identity Provider | Connects a system to an external identity and authentication provider. | OAuth Connector; OpenID Connect Connector |
| **Email Connector** | Connector → Email System | Connects to an email system for sending, receiving, or managing email messages. | SMTP Connector; IMAP Connector |
| **Payment System Connector** | Connector → Payment System | Connects a system to an external payment-processing system. | Stripe Payment Connector |
| **ERP Connector** | Connector → ERP System | Connects a system with an enterprise resource planning system. | SAP Connector; Oracle ERP Connector |
| **CRM Connector** | Connector → CRM System | Connects a system with a customer relationship management system. | Salesforce Connector; HubSpot Connector |
| **Accounting System Connector** | Connector → Accounting System | Connects a system with an accounting or financial-management system. | QuickBooks Connector; Xero Connector |
| **MCP Connector** | Connector → MCP Server | Establishes communication with an MCP server to discover and invoke exposed tools, access resources, and interact with the server according to the Model Context Protocol. | MCP Client Connector; MCP Server Connector |
| **RPC Connector** | Connector → RPC Interface | Communicates with a remote system through remote-procedure-call semantics. | gRPC Connector; XML-RPC Connector |
| **GraphQL Connector** | Connector → GraphQL Interface | Communicates with a system through a GraphQL interface. | GraphQL API Connector |
| **WebSocket Connector** | Connector → WebSocket Interface | Establishes and maintains a bidirectional communication channel with a remote system. | WebSocket Connector |
| **Remote Shell Connector** | Connector → Remote Shell Interface | Establishes a remote command-execution channel to another system. | SSH Connector |
| **IoT Connector** | Connector → IoT System | Connects to an IoT platform, gateway, or device network for exchanging device data and commands. | MQTT Connector |
| **Device Connector** | Connector → Device | Establishes communication with a physical technical device. | USB Connector; Serial Connector |
| **Legacy System Connector** | Connector → Legacy System | Provides communication with a legacy system through its available technical interface or protocol. | Mainframe Connector |
| **Integration Platform Connector** | Connector → Integration Platform | Connects a system to an intermediary platform that mediates or orchestrates communication with other systems. | MuleSoft Connector; Boomi Connector |

## System Connector Manager

> A **technical element that manages the configuration, lifecycle, credentials, and availability of System Connectors**, enabling their creation, authentication, authorization, activation, deactivation, and maintenance.
> 

## System Connector Case Study

| System Connector | Description |
| --- | --- |
| **Google Drive Connector** | Establishes authenticated and authorized access to Google Drive, providing the communication channel through which another system can access its files and operations. |
| **Slack Connector** | Establishes authenticated and authorized communication with Slack, providing access to its messaging resources and operations. |
| **Salesforce Connector** | Establishes authenticated and authorized access to Salesforce, enabling another system to communicate with its data and services. |
| **GitHub Connector** | Establishes authenticated and authorized access to GitHub, providing the communication channel for interacting with repositories, issues, and other available resources. |
| **Database Connector** | Establishes a connection to a database through its communication protocol and credentials, allowing another system to communicate with the database. |
| **API Connector** | Establishes the endpoint, authentication, authorization, and protocol mechanisms required for communication with an external API. |

## System Connector Manager Case Study

| System Connector Manager | Description |
| --- | --- |
| **Zapier Connections** | Manages the configuration and authentication of connections to external systems, making them available for use by integrations. |
| **n8n Credentials** | Manages credentials and connection configurations used by workflows to communicate with external systems and services. |
| **MuleSoft Anypoint Connectivity** | Manages connectors and connection configurations used to establish communication with external systems. |
| **Microsoft Power Platform Connections** | Manages authenticated connections to external services that can be reused across applications and workflows. |
| **AWS Secrets Manager** | Manages credentials and secrets required by system connectors to establish authenticated access to external systems. |

## QA

### What is the difference between a `System Connector` and a `System Integration`?

> A **System Connector** establishes the technical means by which systems can communicate. A **System Integration** uses that communication capability to coordinate data, operations, or processes between the systems.
> 

### What does a `System Connector` actually integrate?

> Strictly speaking, the connector does not perform the integration. It establishes the **access and communication conditions** that make integration possible.
> 

### What is the role of authentication and authorization in a `System Connector`?

> They regulate access to the communication channel: authentication establishes **who or what is connecting**, while authorization determines **what that connector is permitted to access or perform**.
> 

## References

- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md) — the schema and decomposition contract this table follows.
- [Model Context Protocol](note.html?n=technica/ais/application/model-context-protocol-mcp.md) — a connector specification for tool and resource access.
- [Zapier integrations](https://zapier.com/apps/google-drive/integrations) and the [Zapier repository](https://github.com/zapier) — connector-manager case material.
- [n8n integrations](https://n8n.io/integrations/) — connector catalogue and credential manager.
- [MCP server registry](https://mcpservers.org/) — concrete connector instances.
