# Configuration Management

- [Secret Management](note.html?n=technica/computation/system/operation/operation-conceptual-model/secret-management.md)

> The “**Configuration Management**” is a framework that outlines the processes and practices for systematically handling, controlling, and updating configurations within a system or organization.
> 

> **Configuration management** involves tracking and controlling changes to a system's configurations, such as software versions, hardware settings, or network configurations, to ensure consistency, reliability, and efficiency throughout a system or environment.
> 

> **Secret management models** are frameworks and practices used to securely store, manage, and access sensitive information such as passwords, API keys, and encryption keys.
> 

> **Metadata management** refers to the process of managing data about other data, which includes organizing, storing, and maintaining metadata to ensure that data is discoverable, usable, and accessible. This can include file formats, data structures, source information, relationships, and much more.
> 

## Models

| **Model** | **Description** | **Examples/Tools** |
| --- | --- | --- |
| **Centralized Secret Management** | A single, centralized system or service is used to store and manage all secrets, providing a unified access control mechanism. | HashiCorp Vault, AWS Secrets Manager, Azure Key Vault |
| **Distributed Secret Management** | Secrets are distributed across multiple systems or services, often with decentralized control and management. | Kubernetes Secrets, Consul |
| **Hardware Security Modules (HSM)** | Dedicated physical devices that store and manage cryptographic keys and perform encryption operations securely. | AWS CloudHSM, Azure Dedicated HSM |
| **Cloud-Native Secret Management** | Built-in secret management features provided by cloud service providers, integrated with their services. | AWS Secrets Manager, Azure Key Vault, Google Cloud Secret Manager |
| **Environment Variable Management** | Secrets are stored in environment variables, which are accessed by applications at runtime. | Docker Secrets, Kubernetes ConfigMaps |
| **Encrypted Configuration Files** | Secrets are stored in configuration files that are encrypted to protect their contents. | Encrypted YAML/JSON files, Ansible Vault |
| **Access Control and Auditing** | Management of secrets includes robust access control policies and auditing mechanisms to monitor access and changes. | IAM (Identity and Access Management), Audit logs |
| **Secret Rotation and Lifecycle Management** | Practices for regularly rotating and managing the lifecycle of secrets to enhance security. | Automated rotation in HashiCorp Vault, AWS Secrets Manager |
| **Configuration Files** | Storing configuration settings in separate files (e.g., YAML, JSON, XML) that are read by the application during runtime. |  |
| **Databases** | … | Dolt, sqllite, … |

## …

## References

- https://en.wikipedia.org/wiki/Software_configuration_management
- https://en.wikipedia.org/wiki/Configuration_management
- https://www.vaultproject.io/
- https://www.consul.io/
- https://www.dolthub.com/blog/2023-05-15-your-config-file-should-be-a-database/
- https://www.atlassian.com/microservices/microservices-architecture/configuration-management
- https://www.puppet.com/
- https://atlas.apache.org/#/
- https://datahubproject.io/