# Specification

> Spec Driven Software Production  - Power by AI.
> 

> Why not include this in the Systems notes? Because many topics—such as correctness, consistency, and related properties—depend on the system's specification. Therefore, this note is cross-cutting set of notes.
> 

## Structure

> How a Specification is structure?
> 

| Layer | Definition | Instances(s) |
| --- | --- | --- |
| Technical Requirement | A property the system is required to satisfy. | **Dependability  (Quality)**(Correctness, Isolation, Consistency, Availability, Durability, Security), Functionality |
| Technical Guarantee (Contract) | A formally specified behavioral guarantee that precisely defines what level of the requirement is provided. It is the contract between the system and its users. |  |
| **Operational Policy (Configuration)** | A selected behavioral contract or operating mode that determines how the system will attempt to satisfy the requirement under given conditions. It is typically configurable. | Serializable, Snapshot Isolation, FIFO scheduling, LRU cache replacement, Retry with exponential backoff |
| **Mechanism (Implementation)** | The algorithms, protocols, and data structures that enforce the selected policy. | Strict Two-Phase Locking (2PL), MVCC, Timestamp Ordering, Red-Black Tree scheduler, Raft, Paxos |

## (Quality Specification) Dependability

> **Dependability** is the degree to which a **computational system** can justifiably be relied upon to deliver its specified services under stated conditions.
> 

> See more in [Dependability](note.html?n=technica/computation/dependability.md).
> 

## Technical Requirement Type Set

> What are the types of technical requirements that appear in Computational Systems Engineering?
> 

### Category

| **Category** | **Requirement Types** |
| --- | --- |
| **Behavioral** | Functional |
| **Quality Attributes (Non-Functional)** | Performance, Scalability, Availability, Reliability, Dependability, Maintainability, Modifiability, Portability, Usability, Accessibility, Extensibility, Testability, Configurability |
| **Cyber Defense & Trustworthiness** | Security, Confidentiality, Integrity, Privacy, Auditability, Safety |
| **Operational** | Recoverability, Fault Tolerance, Deployment, Operational, Observability |
| **Interoperability** | Compatibility, Interoperability |
| **Data** | Data Requirements |
| **Governance** | Compliance |
| **Resource Constraints** | Resource Requirements |

### Type Set

| **Requirement Type** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Functional Requirement** | Defines what the system must do; the services, behaviors, or functions it must provide. | Authenticate users, process payments, calculate routes, store files. |
| **Performance Requirement** | Specifies quantitative limits on speed, throughput, capacity, or efficiency. | ≤100 ms latency, 10,000 requests/sec, 95% CPU utilization maximum. |
| **Scalability Requirement** | Defines the ability to maintain acceptable performance as workload or system size grows. | Support 10× traffic growth, horizontal scaling, partitioning. |
| **Availability Requirement** | Specifies how continuously the system must remain operational. | 99.99% uptime, no more than 5 minutes downtime/month. |
| **Reliability Requirement** | Defines the probability that the system performs correctly without failure over time. | MTBF > 1 year, transaction success rate >99.999%. |
| **Dependability Requirement** | Specifies the overall trustworthiness of the system, including reliability, availability, maintainability, integrity, and safety. | Fault-tolerant architecture, graceful degradation. |
| **Fault Tolerance Requirement** | Specifies the ability to continue operating despite component failures. | Automatic failover, replicated databases, redundant services. |
| **Recoverability Requirement** | Defines how the system restores correct operation after failure. | RTO < 15 minutes, RPO < 1 minute, disaster recovery. |
| **Maintainability Requirement** | Specifies how easily the system can be modified, repaired, or upgraded. | Modular architecture, automated testing, low coupling. |
| **Modifiability Requirement** | Specifies how easily new features or changes can be introduced. | Plugin architecture, configuration-driven behavior. |
| **Interoperability Requirement** | Defines the ability to exchange and use information with other systems. | REST APIs, OAuth, OpenID Connect, MQTT. |
| **Compatibility Requirement** | Specifies supported environments or coexistence with other systems. | Windows/Linux support, PostgreSQL compatibility. |
| **Portability Requirement** | Defines how easily the system can operate in different environments. | Docker deployment, cloud portability, ARM/x86 support. |
| **Usability Requirement** | Specifies how effectively intended users can use the system. | Accessible UI, intuitive workflow, WCAG compliance. |
| **Accessibility Requirement** | Defines support for users with disabilities. | Screen reader support, keyboard navigation, color contrast. |
| **Security Requirement** | Specifies protection against unauthorized access or misuse. | Authentication, authorization, encryption, auditing. |
| **Privacy Requirement** | Specifies protection of personal or sensitive information. | Data minimization, consent management, anonymization. |
| **Safety Requirement** | Specifies prevention of harm to people, property, or the environment. | Emergency shutdown, fail-safe control, hazard mitigation. |
| **Integrity Requirement** | Ensures data and system state remain correct and unaltered except by authorized actions. | Checksums, digital signatures, ACID transactions. |
| **Confidentiality Requirement** | Prevents unauthorized disclosure of information. | AES encryption, TLS, access control lists. |
| **Auditability Requirement** | Specifies the ability to reconstruct and verify system activities. | Immutable logs, audit trails, event sourcing. |
| **Observability Requirement** | Specifies the ability to understand internal system state from outputs. | Metrics, tracing, structured logging. |
| **Compliance Requirement** | Specifies conformance with standards, regulations, or policies. | ISO 27001, PCI DSS, GDPR, HIPAA. |
| **Resource Requirement** | Defines limits on consumption of computational resources. | ≤2 GB RAM, ≤4 CPU cores, ≤50 W power. |
| **Deployment Requirement** | Specifies how the system must be installed, configured, and operated. | Kubernetes deployment, blue-green deployment, IaC. |
| **Operational Requirement** | Defines constraints during production operation. | 24/7 monitoring, automated backups, on-call alerts. |
| **Testability Requirement** | Specifies how easily the system can be verified and validated. | Unit-test coverage >90%, dependency injection, simulation support. |
| **Extensibility Requirement** | Defines the ability to add new capabilities without redesign. | Plugin framework, extension APIs. |
| **Configurability Requirement** | Specifies what aspects of system behavior can be changed without modifying code. | Runtime configuration, feature flags, policy engine. |
| **Data Requirement** | Specifies constraints on data representation, storage, quality, or lifecycle. | Retain logs for 7 years, JSON schema validation, data lineage. |

## System Interface Description Format

| **Interface Description Format** | **File Format** | **Typical File** | **Description** |
| --- | --- | --- | --- |
| **OpenAPI** | YAML / JSON | `openapi.yaml` | Describes HTTP APIs, typically REST APIs |
| **AsyncAPI** | YAML / JSON | `asyncapi.yaml` | Describes asynchronous, event-driven APIs |
| **GraphQL SDL** | SDL | `schema.graphql` | Defines the schema and operations of a GraphQL API |
| **gRPC / Protocol Buffers** | Protobuf | `service.proto` | Defines RPC services, methods, and message types |
| **WSDL** | XML | `service.wsdl` | Describes SOAP web services |
| **RAML** | YAML | `api.raml` | Describes HTTP/REST APIs |
| **API Blueprint** | Markdown-like | `api.apib` | Describes HTTP APIs using a human-readable syntax |
| **Smithy** | Smithy IDL | `model.smithy` | Models services, operations, resources, and data structures |

## References

- [Documentation](note.html?n=technica/computation/system/documentation.md)
- [Fault-Tolerant Design](note.html?n=technica/computation/system/design/computer-system-design-conceptual-model/fault-tolerant-design.md)
- https://www.bremontix.xyz/lab/pro/Catalog/Production/Regime/Technoetism/
- https://githubnext.com/projects/speclang/
- [A Guide on AI-Assisted Programming](https://app.notion.com/p/A-Guide-on-AI-Assisted-Programming-2c1c0f5171ec802f8be1d2b1d6d6c92c?pvs=21)
- https://github.com/dbremont/Epistecnica/blob/main/src/note/app/notes/cto/es/multinode/openapi.md