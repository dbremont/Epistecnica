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

> **Note:** One could say that **System Connector** is a **Technical Element Type**. Strictly speaking, it is a type; however, for ease of exposition, it is better to treat this more concrete type as belonging to a separate type tree.
> 

| **Technical Element Instance Tree Path** | **Description** | **Technical Element Type Tree Path** | **Technical Element Category Tree Path** | **Case: Concrete Instance** |
| --- | --- | --- | --- | --- |
| **System Connector** | Technical element that establishes access to and the communication channel between one system and another. | `System Structure → Technical Interface` | `System Structure` | **Stripe API Connector** |
| System Connector → **Connector Configuration** | Configuration defining how the connector establishes and maintains communication. | `System Structure → Technical Configuration` | `System Structure` | **Stripe Connector Configuration** |
| System Connector → Connector Configuration → **Connection Parameters** | Parameters governing establishment and behavior of the connection. | `Requirements & Definition → Technical Parameter` | `Requirements & Definition` | **Stripe Connection Parameter Set** |
| System Connector → Connector Configuration → Connection Parameters → **Connection Timeout** | Parameter defining the maximum waiting period for a connection operation. | `Requirements & Definition → Technical Parameter` | `Requirements & Definition` | **30-second timeout** |
| System Connector → Connector Configuration → Connection Parameters → **Retry Parameter** | Parameter defining how failed connection operations are retried. | `Requirements & Definition → Technical Parameter` | `Requirements & Definition` | **3 retries** |
| System Connector → Connector Configuration → Connection Parameters → **Keepalive Parameter** | Parameter defining how connection liveness is maintained or detected. | `Requirements & Definition → Technical Parameter` | `Requirements & Definition` | **TCP keepalive configuration** |
| System Connector → Connector Configuration → **Endpoint Configuration** | Configuration identifying the remote system endpoint to which communication is established. | `System Structure → Technical Configuration` | `System Structure` | **Stripe API Endpoint Configuration** |
| System Connector → Connector Configuration → Endpoint Configuration → **Endpoint Address** | Address identifying the remote communication endpoint. | `Requirements & Definition → Technical Parameter` | `Requirements & Definition` | **api.stripe.com** |
| System Connector → Connector Configuration → Endpoint Configuration → **Endpoint Port** | Port identifying the network service used by the endpoint. | `Requirements & Definition → Technical Parameter` | `Requirements & Definition` | **TCP port 443** |
| System Connector → Connector Configuration → **Protocol Configuration** | Configuration specifying the communication protocol and its operational parameters. | `System Structure → Technical Configuration` | `System Structure` | **HTTPS/REST Configuration** |
| System Connector → Connector Configuration → Protocol Configuration → **Protocol Version** | Configuration specifying the version of the communication protocol or protocol implementation. | `Requirements & Definition → Technical Parameter` | `Requirements & Definition` | **TLS 1.2+ / current Stripe API version** |
| System Connector → Connector Configuration → Protocol Configuration → **Message Format Configuration** | Configuration specifying the representation used for exchanged messages. | `System Structure → Technical Configuration` | `System Structure` | **JSON configuration** |
| System Connector → Connector Configuration → **Authentication Configuration** | Configuration specifying how the connector establishes the identity of the connecting party. | `System Structure → Technical Configuration` | `System Structure` | **Stripe API-Key Configuration** |
| System Connector → Connector Configuration → **Authorization Configuration** | Configuration specifying what the connector is permitted to access or perform. | `System Structure → Technical Configuration` | `System Structure` | **Stripe API Authorization Configuration** |
| System Connector → **Connection Interface** | Boundary through which the connector establishes communication with the external system. | `System Structure → Technical Interface` | `System Structure` | **Stripe REST API Interface** |
| System Connector → Connection Interface → **Local Endpoint** | Interface endpoint exposed by the local system for the connector. | `System Structure → Technical Interface` | `System Structure` | **Local application API client** |
| System Connector → Connection Interface → **Remote Endpoint** | Interface endpoint exposed by the external system to receive communication. | `System Structure → Technical Interface` | `System Structure` | **Stripe REST API endpoint** |
| System Connector → Connection Interface → **Communication Channel** | Technical path through which information is transmitted between the endpoints. | `System Structure → Technical Interface` | `System Structure` | **HTTPS connection** |
| System Connector → Connection Interface → Communication Channel → **Transport Mechanism** | Mechanism responsible for transporting information across the communication channel. | `Mechanism & Capability → Technical Mechanism` | `Mechanism & Capability` | **TCP/IP** |
| System Connector → Connection Interface → Communication Channel → **Communication Protocol** | Rules governing the exchange of information across the channel. | `Requirements & Definition → Technical Standard` | `Requirements & Definition` | **HTTPS** |
| System Connector → Connection Interface → Communication Channel → **Channel Configuration** | Configuration defining operational characteristics of the communication channel. | `System Structure → Technical Configuration` | `System Structure` | **TLS/HTTPS Client Configuration** |
| System Connector → **Access Control** | Technical means by which access to the external system is established and constrained. | `Technical Control → Technical Security` | `Technical Control` | **Stripe API Access Control** |
| System Connector → Access Control → **Authentication Mechanism** | Mechanism establishing the identity of the connecting system, agent, or process. | `Technical Control → Technical Security` | `Technical Control` | **API-Key Authentication** |
| System Connector → Access Control → Authentication Mechanism → **Credential** | Technical information used to establish identity. | `System Structure → Constitutive Technical Object` | `System Structure` | **Stripe Secret API Key** |
| System Connector → Access Control → Authentication Mechanism → Credential → **Credential Configuration** | Configuration defining how credentials are supplied or referenced. | `System Structure → Technical Configuration` | `System Structure` | **Environment-variable credential configuration** |
| System Connector → Access Control → Authentication Mechanism → **Authentication Protocol** | Protocol governing the exchange used to establish identity. | `Requirements & Definition → Technical Standard` | `Requirements & Definition` | **Stripe API-Key authentication scheme** |
| System Connector → Access Control → Authentication Mechanism → **Authentication Method** | Concrete method by which the connector supplies authentication information. | `Technical Operation → Technical Technique` | `Technical Operation` | **HTTP Authorization header** |
| System Connector → Access Control → **Authorization Mechanism** | Mechanism determining which resources or operations the authenticated connector may access. | `Technical Control → Technical Security` | `Technical Control` | **Stripe authorization mechanism** |
| System Connector → Access Control → Authorization Mechanism → **Access Policy** | Rules defining permitted and prohibited accesses or operations. | `Requirements & Definition → Technical Specification` | `Requirements & Definition` | **Stripe API access policy** |
| System Connector → Access Control → Authorization Mechanism → **Permission** | Specific permitted operation or resource access granted to the connector. | `Requirements & Definition → Technical Requirement` | `Requirements & Definition` | **Permission to retrieve customer records** |
| System Connector → Access Control → Authorization Mechanism → **Access Decision** | Decision determining whether a requested access or operation is permitted. | `Technical Control → Technical Decision` | `Technical Control` | **API request authorized** |
| System Connector → **Protocol Handler** | Technical element responsible for implementing the communication protocol at the connector boundary. | `System Structure → Constitutive Technical Object` | `System Structure` | **Stripe REST Client** |
| System Connector → Protocol Handler → **Protocol Implementation** | Operative implementation of the communication protocol. | `System Structure → Production Virtual Technical Object` | `System Structure` | **Stripe REST API client implementation** |
| System Connector → Protocol Handler → Protocol Implementation → **Message Encoder** | Converts structured information into the representation required by the protocol. | `Technical Operation → Technical Technique` | `Technical Operation` | **JSON serializer** |
| System Connector → Protocol Handler → Protocol Implementation → **Message Decoder** | Converts received protocol representations into usable structured information. | `Technical Operation → Technical Technique` | `Technical Operation` | **JSON deserializer** |
| System Connector → Protocol Handler → Protocol Implementation → **Message Format** | Formal representation governing the structure of exchanged messages. | `Requirements & Definition → Technical Standard` | `Requirements & Definition` | **JSON** |
| System Connector → Protocol Handler → Protocol Implementation → **Request Handler** | Technical element responsible for constructing and processing outgoing protocol requests. | `System Structure → Production Virtual Technical Object` | `System Structure` | **Stripe HTTP request handler** |
| System Connector → Protocol Handler → Protocol Implementation → **Response Handler** | Technical element responsible for receiving and processing protocol responses. | `System Structure → Production Virtual Technical Object` | `System Structure` | **Stripe HTTP response handler** |
| System Connector → **Connection Manager** | Technical element responsible for establishing, maintaining, and terminating the communication connection. | `System Structure → Constitutive Technical Object` | `System Structure` | **HTTP connection manager** |
| System Connector → Connection Manager → **Connection Establishment** | Operation that creates the communication connection. | `Technical Operation → Technical Activity` | `Technical Operation` | **TCP/TLS connection establishment** |
| System Connector → Connection Manager → **Connection Maintenance** | Operation that preserves an established connection during its operational lifetime. | `Lifecycle & Continuity → Technical Maintenance` | `Lifecycle & Continuity` | **HTTP connection reuse / keepalive** |
| System Connector → Connection Manager → **Connection Termination** | Operation that deliberately closes the communication connection. | `Technical Operation → Technical Act` | `Technical Operation` | **HTTP/TCP connection closure** |
| System Connector → Connection Manager → **Connection Retry** | Operation that attempts to re-establish communication after a recoverable failure. | `Technical Operation → Technical Activity` | `Technical Operation` | **Automatic request retry** |
| System Connector → Connection Manager → **Connection Timeout Handling** | Operation for handling failure to establish or maintain communication within the configured period. | `Technical Operation → Technical Activity` | `Technical Operation` | **30-second timeout handler** |
| System Connector → **Session Manager** | Technical element responsible for maintaining the logical communication session where the protocol requires one. | `System Structure → Constitutive Technical Object` | `System Structure` | **HTTP client session manager** |
| System Connector → Session Manager → **Session State** | Technical state representing the current logical communication session. | `System Structure → Technical State` | `System Structure` | **Active HTTP client session state** |
| System Connector → Session Manager → **Session Identifier** | Identifier used to associate communication with a particular session. | `System Structure → Constitutive Technical Object` | `System Structure` | **HTTP session identifier / connection context** |
| System Connector → Session Manager → **Session Lifecycle Control** | Control governing creation, continuation, expiration, and termination of a logical session. | `Technical Control → Technical Lifecycle Control` | `Technical Control` | **HTTP client session lifecycle management** |
| System Connector → **Communication State** | Operational state describing the current condition of the connector's communication relationship. | `System Structure → Technical State` | `System Structure` | **Current Stripe connection state** |
| System Connector → Communication State → **Connection State** | State of the underlying communication connection. | `Mechanism & Capability → Technical Property` | `Mechanism & Capability` | **Connected** |
| System Connector → Communication State → **Authentication State** | State indicating the current result or condition of authentication. | `Mechanism & Capability → Technical Property` | `Mechanism & Capability` | **Authenticated** |
| System Connector → Communication State → **Authorization State** | State indicating the access permissions currently applicable to the connector. | `Mechanism & Capability → Technical Property` | `Mechanism & Capability` | **Authorized** |
| System Connector → **Connector Control** | Technical control logic governing connector operation. | `System Structure → Production Virtual Technical Object` | `System Structure` | **Stripe Connector Control Logic** |
| System Connector → Connector Control → **Connection Control Logic** | Logic governing connection establishment, maintenance, retry, and termination. | `System Structure → Production Virtual Technical Object` | `System Structure` | **HTTP connection-control implementation** |
| System Connector → Connector Control → **Access Control Logic** | Logic applying authentication and authorization decisions. | `System Structure → Production Virtual Technical Object` | `System Structure` | **API credential and permission validation logic** |
| System Connector → Connector Control → **Protocol Control Logic** | Logic governing protocol-compliant communication. | `System Structure → Production Virtual Technical Object` | `System Structure` | **REST/HTTP request-control logic** |
| System Connector → Connector Control → **Error Handling Logic** | Logic governing detection, classification, and handling of connector errors. | `System Structure → Production Virtual Technical Object` | `System Structure` | **HTTP/API error handler** |
| System Connector → **Connector Security** | Security mechanisms protecting the connector and its communication relationship. | `Technical Control → Technical Security` | `Technical Control` | **Stripe Connector Security Controls** |
| System Connector → Connector Security → **Credential Protection** | Protection of credentials used for authentication. | `Technical Control → Technical Security` | `Technical Control` | **Secret-key storage in environment variables** |
| System Connector → Connector Security → **Channel Protection** | Protection of information transmitted through the communication channel. | `Technical Control → Technical Security` | `Technical Control` | **TLS-protected HTTPS channel** |
| System Connector → Connector Security → Channel Protection → **Encryption Mechanism** | Mechanism that transforms information to protect it from unauthorized disclosure. | `Mechanism & Capability → Technical Mechanism` | `Mechanism & Capability` | **TLS encryption** |
| System Connector → Connector Security → Channel Protection → **Integrity Mechanism** | Mechanism that enables detection or prevention of unauthorized modification of transmitted information. | `Mechanism & Capability → Technical Mechanism` | `Mechanism & Capability` | **TLS integrity protection** |
| System Connector → **Connector Monitoring** | Technical means for obtaining information about connector operation and state. | `Technical Control → Technical Feedback` | `Technical Control` | **Stripe connector monitoring subsystem** |
| System Connector → Connector Monitoring → **Connection Status** | Information representing the current connection condition. | `Technical Control → Technical Feedback` | `Technical Control` | **HTTP connection status** |
| System Connector → Connector Monitoring → **Authentication Result** | Feedback indicating the outcome of authentication. | `Technical Control → Technical Feedback` | `Technical Control` | **Stripe authentication success/failure response** |
| System Connector → Connector Monitoring → **Authorization Result** | Feedback indicating the outcome of an authorization decision. | `Technical Control → Technical Feedback` | `Technical Control` | **Stripe authorization response** |
| System Connector → Connector Monitoring → **Communication Error** | Feedback representing a failure occurring during communication. | `Technical Control → Technical Failure` | `Technical Control` | **HTTP 5xx / network error** |
| System Connector → Connector Monitoring → **Connection Metrics** | Measurements representing quantitative characteristics of connector operation. | `Technical Control → Technical Feedback` | `Technical Control` | **Request latency and error-rate metrics** |
| System Connector → **Connector Interface Specification** | Formal specification defining the conditions under which the connector can communicate with the external system. | `Requirements & Definition → Technical Specification` | `Requirements & Definition` | **Stripe API Interface Specification** |
| System Connector → Connector Interface Specification → **Endpoint Specification** | Specification of the communication endpoints. | `Requirements & Definition → Technical Specification` | `Requirements & Definition` | **Stripe API endpoint specification** |
| System Connector → Connector Interface Specification → **Protocol Specification** | Specification of the communication rules and message exchange. | `Requirements & Definition → Technical Specification` | `Requirements & Definition` | **Stripe REST/HTTP API specification** |
| System Connector → Connector Interface Specification → **Security Specification** | Specification of authentication, authorization, and communication-security requirements. | `Requirements & Definition → Technical Specification` | `Requirements & Definition` | **Stripe API security requirements** |

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

- [Identity Model](https://app.notion.com/p/Identity-Model-aa621c3b1f734edf81c65ae31417e89a?pvs=21)
- [Permision Model](https://app.notion.com/p/Permision-Model-17910d56fc6b49a08d2b435aa4600f9b?pvs=21)
- https://zapier.com/apps/google-drive/integrations
- https://github.com/zapier
- https://n8n.io/integrations/
- MCP
- https://mcpservers.org/servers/PaulFidika/gmail-mcp-server