# Secret Management

- [Certificate Management](note.html?n=technica/computation/system/operation/operation-conceptual-model/certificate-management.md), [Configuration Management](note.html?n=technica/computation/system/operation/operation-conceptual-model/configuration-management.md)

> In this **note we will** explore **`Secret Management`.**
> 

## Formulation

> What is **secret management** in computational systems operations? **Secret management** is the set of mechanisms and operational practices used to **control the lifecycle of sensitive values used by computational systems**—including their creation, storage, access, delivery, use, rotation, revocation, and destruction.
> 

### What technical problems it solves?

| Problem | Technical concern | Typical solution |
| --- | --- | --- |
| **Secret storage** | Where can sensitive values be kept safely? | Vaults, KMS, encrypted stores |
| **Secret distribution** | How does a process obtain a secret? | Secret injection, APIs, secret volumes |
| **Access control** | Who/what is allowed to access it? | IAM, ACLs, policies, capabilities |
| **Identity** | How is the requesting workload identified? | Workload identity, service accounts, certificates |
| **Exposure** | How can secret lifetime and visibility be minimized? | Ephemeral/dynamic credentials |
| **Credential compromise** | What happens if a secret is exposed? | Rotation, revocation, short-lived credentials |
| **Key protection** | How are cryptographic keys protected? | KMS, HSM, TPM |
| **Secret leakage** | How do we prevent secrets appearing in logs/processes/files? | Redaction, isolation, secure injection |
| **Multi-environment management** | How are development, staging, and production credentials separated? | Namespaces, policies, separate stores |
| **Availability** | What happens if the secret store is unavailable? | Replication, caching, redundancy |
| **Change management** | How are changes to secrets controlled? | Versioning, controlled updates |
| **Accountability** | Who accessed which secret and when? | Audit logs, access records |
| **Automation** | How can machines manage secrets without humans handling them? | APIs, workload identity, automated rotation |
| **Isolation** | How do we prevent one workload from obtaining another's secrets? | Sandboxing, namespaces, least privilege |
| Certificate Management | How are certificates and their associated keys issued, distributed, renewed, and revoked? | PKI, certificate authorities, automated issuance, renewal, and revocation |

### Which are the related `technical practices`?

| Technical Area | Description |
| --- | --- |
| **Secret Storage** | Secure storage and protection of passwords, tokens, API keys, and other sensitive values. |
| **Secret Distribution** | Secure delivery of secrets to applications, workloads, and users when needed. |
| **Credential Management** | Lifecycle management of credentials used to authenticate entities and services. |
| **Identity Management** | Establishing and managing the identities of users, services, workloads, and machines. |
| **Access Management** | Controlling which identities can access which secrets and under what conditions. |
| **Key Management** | Generation, storage, distribution, use, rotation, and destruction of cryptographic keys. |
| **Certificate Management** | Issuance, distribution, validation, renewal, and revocation of digital certificates. |
| **PKI Management** | Management of certificate authorities, trust chains, certificates, and public-key infrastructure. |
| **Hardware-Backed Key Protection** | Protection of cryptographic keys using HSMs, TPMs, secure enclaves, or similar hardware-backed mechanisms. |
| **Workload Identity** | Providing machine and workload identities that can be used to obtain credentials without embedding static secrets. |
| **Credential Lifecycle Management** | Provisioning, activation, rotation, expiration, revocation, recovery, and destruction of credentials. |
| **Secret Injection** | Making secrets available to a workload at runtime without embedding them into source code or images. |
| **Secrets Discovery & Detection** | Identifying secrets accidentally present in source code, repositories, files, logs, or other artifacts. |
| **Secret Leakage Prevention** | Preventing sensitive values from being exposed through logs, processes, files, telemetry, or other channels. |
| **Privileged Access Management** | Controlling and monitoring access to highly privileged credentials and administrative capabilities. |
| **Cryptographic Operations** | Performing encryption, decryption, signing, verification, and related operations using protected cryptographic material. |
| **Audit & Secret Access Monitoring** | Recording and monitoring access to secrets, credentials, keys, and certificates. |
| **Trust & Attestation** | Establishing whether a workload or execution environment is trusted before granting access to sensitive material. |
| **Secure Configuration Management** | Managing sensitive configuration separately from application code and ordinary configuration. |
| **Environment & Credential Isolation** | Separating credentials and sensitive material between workloads, tenants, environments, and execution contexts. |

## Secret Management System

> Which are the set of **`strategies`** or **`models`** used to create **`secret management solutions`**?
> 

### Structure

```jsx
Secret Management
│
├── Storage
│   ├── Centralized Repository
│   └── Distributed Storage
│
├── Generation
│   ├── Static
│   └── Dynamic
│
├── Protection
│   ├── Encryption
│   └── Client-Protected
│
├── Authorization
│   ├── Policy-Based
│   └── Identity-Bound
│
├── Delivery
│   ├── On-Demand Retrieval
│   └── Workload-Provided
│       ├── File
│       ├── Process Environment
│       └── Memory
│
├── Lifecycle
│   ├── Rotation
│   ├── Revocation
│   ├── Expiration
│   └── Versioning
│
├── Availability
│   ├── Replication
│   └── Recovery
│
└── Governance
    ├── Auditing
    └── Policy Governance
```

| Category | Model | Description |
| --- | --- | --- |
| **Secret Storage** | **Centralized Secret Repository Model** | Secrets are maintained in a logically centralized protected repository and accessed by authorized consumers. |
| **Secret Storage** | **Distributed Secret Storage Model** | Secrets are maintained across multiple storage locations or nodes while preserving security and consistency requirements. |
| **Secret Generation** | **Static Secret Model** | Long-lived credentials or secret values are created and maintained explicitly. |
| **Secret Generation** | **Dynamic Secret Model** | Credentials or secret values are generated on demand, typically with a limited lifetime or scope. |
| **Secret Protection** | **Encrypted Secret Model** | Secret values are cryptographically protected while stored or transmitted. |
| **Secret Protection** | **Client-Protected Secret Model** | Protection is performed by the consuming or originating component before the secret leaves its trust boundary. |
| **Authorization** | **Policy-Based Access Model** | Access to secrets is determined by explicit policies relating identities, resources, actions, and conditions. |
| **Authorization** | **Identity-Bound Access Model** | Secret access is associated with authenticated identities, workloads, services, or execution contexts. |
| **Secret Delivery** | **On-Demand Retrieval Model** | A consuming workload explicitly requests and retrieves a secret when it needs it. |
| **Secret Delivery** | **Workload-Provided Secret Model** | Secrets are made available to a workload through its execution environment rather than being explicitly retrieved by application logic. |
| **Secret Delivery** | **File-Based Delivery Model** | Secrets are exposed to the workload through protected files or filesystem-like resources. |
| **Secret Delivery** | **Process-Environment Delivery Model** | Secrets are exposed through the execution environment of a process. |
| **Secret Delivery** | **Memory-Based Delivery Model** | Secrets are provided directly in process memory or another transient runtime representation. |
| **Secret Lifecycle** | **Rotation Model** | Secret values are replaced according to time, events, policy, or security conditions. |
| **Secret Lifecycle** | **Revocation Model** | Previously valid credentials or secret values are explicitly invalidated. |
| **Secret Lifecycle** | **Expiration Model** | Secret validity automatically terminates after a defined condition or lifetime. |
| **Secret Lifecycle** | **Versioned Secret Model** | Multiple versions of a secret are maintained to support transition, rollback, or historical consistency. |
| **Availability** | **Replicated Secret Model** | Secret-management state is replicated across locations or nodes to improve availability and resilience. |
| **Availability** | **Recovery Model** | Secret state can be restored following loss, corruption, failure, or disaster. |
| **Governance** | **Auditable Secret Model** | Secret-management events, accesses, changes, and administrative operations are recorded for accountability and analysis. |
| **Governance** | **Policy-Governed Secret Model** | Secret creation, access, modification, retention, and disposal are constrained by organizational policies. |

### Space

> Which are the set of Secret Management System and solutions?
> 

| Solution | Description | Role | Implementation |
| --- | --- | --- | --- |
| **HashiCorp Vault** | Centralized system for storing, controlling, generating, and delivering secrets and credentials. | General-purpose secret management | Centralized repository; policy-based authorization; dynamic credential generation; API-based and workload-oriented delivery |
| **OpenBao** | Open-source system for centralized management of secrets and sensitive credentials. | General-purpose secret management | Centralized repository; policy-based access; dynamic secrets; API-based retrieval |
| **AWS Secrets Manager** | Managed service for storing, retrieving, rotating, and controlling access to application and infrastructure secrets. | Cloud secret management | Managed centralized repository; identity-based authorization; API-based retrieval; automated rotation |
| **Azure Key Vault** | Managed service for protecting and managing secrets, cryptographic keys, and certificates. | Cloud secret and key management | Managed repository; identity/policy-based access; API-based retrieval; lifecycle management |
| **Google Cloud Secret Manager** | Managed service for storing, versioning, accessing, and auditing application secrets. | Cloud secret management | Managed centralized repository; identity-based authorization; versioned secrets; API-based retrieval |
| **OCI Vault** | Managed service for protecting cryptographic keys and application secrets. | Cloud key and secret management | Managed repository; identity-based authorization; encryption-backed protection; API-based retrieval |
| **CyberArk Secrets Management** | Enterprise platform for securing credentials used by applications, machines, services, and workloads. | Enterprise credential and secret management | Centralized repository; identity/policy-based access; automated rotation; workload-oriented delivery |
| **Delinea Secret Server** | System for securely storing, controlling, rotating, and auditing credentials and privileged secrets. | Privileged credential management | Centralized repository; role/policy-based authorization; credential rotation; audited retrieval |
| **BeyondTrust Password Safe** | Platform for managing privileged credentials and controlling their use. | Privileged access and credential management | Centralized credential repository; policy-based access; automated credential rotation; audited access |
| **Akeyless** | Secret-management platform for applications, workloads, credentials, keys, and certificates. | General-purpose secret management | Centralized logical management; policy-based authorization; dynamic credentials; API/workload delivery |
| **Infisical** | Secret-management platform for development, applications, infrastructure, and deployment environments. | Developer and application secret management | Centralized repository; environment-based organization; identity/policy access; API/agent-based delivery |
| **Doppler** | Centralized platform for managing and distributing application configuration and secrets across environments. | Application configuration and secret management | Centralized repository; environment-based organization; API/CLI/runtime delivery |
| **1Password Secrets Automation** | Programmatic interface for retrieving secrets stored in 1Password for applications and infrastructure. | Application/workload secret delivery | Centralized repository; identity-based authorization; API-based retrieval; runtime delivery |
| **Kubernetes Secrets** | Kubernetes resource for representing sensitive configuration data consumed by workloads. | Workload secret representation and delivery | Cluster-managed storage; workload-oriented delivery; environment/file/volume-based consumption |
| **External Secrets Operator** | Kubernetes controller that retrieves secrets from external secret-management systems and represents them as Kubernetes resources. | Secret synchronization and workload delivery | External repository; synchronization; declarative workload integration |
| **SOPS** | Tool for encrypting sensitive configuration files while retaining them in files or source repositories. | Encrypted configuration management | Client-side/file encryption; decentralized storage; key-based decryption |
| **Sealed Secrets** | Kubernetes-oriented mechanism for storing encrypted secrets in source-control systems and decrypting them inside the cluster. | Kubernetes secret protection | Client-side encryption; encrypted repository representation; cluster-side decryption |
| **EJBCA** | PKI platform for issuing, managing, and revoking digital certificates and associated cryptographic material. | Certificate and PKI management | Certificate authority; lifecycle management; policy-based issuance and revocation |
| **cert-manager** | Kubernetes-native system for automating certificate issuance and renewal. | Certificate lifecycle management | Automated issuance; workload integration; renewal and expiration management |

## How does it integrate with the overall computational system that requires the secrets?

> A secret-management system integrates with a computational system by authenticating the workload or user, authorizing access to specific secrets, retrieving or generating the required secret material, and securely delivering it to the consuming process at the appropriate point in its execution lifecycle.
> 

| Integration Dimension | Description |
| --- | --- |
| **Secret Discovery** | Determines which secret or credential is required, where it is located, and how the consuming workload identifies it. |
| **Workload Authentication** | Establishes the identity of the application, service, workload, machine, or user requesting secret access. |
| **Access Authorization** | Determines whether the authenticated identity is permitted to access a particular secret and under which conditions. |
| **Secret Request** | The consuming process requests a specific secret, credential, key, or other protected material from the secret-management system. |
| **Secret Retrieval** | The secret-management system locates and retrieves the requested secret from its protected storage or generates it dynamically. |
| **Secret Generation** | The system generates ephemeral or dynamic credentials when a static secret is not required. |
| **Secret Delivery** | Transfers the secret from the secret-management system to the authorized consumer through an appropriate secure interface or mechanism. |
| **Secret Injection** | Makes the secret available to the consuming process at runtime, such as through memory, environment variables, mounted files, or an agent. |
| **Secret Consumption** | The application uses the secret to authenticate, authorize, establish connections, perform cryptographic operations, or access another resource. |
| **Secret Renewal** | Obtains a new secret or credential before the existing one expires, allowing continuous operation without embedding long-lived credentials. |
| **Secret Rotation** | Replaces an existing secret with a new value and coordinates the transition between the secret-management system and consuming workloads. |
| **Secret Revocation** | Invalidates a secret or credential so that it can no longer be used to obtain or maintain access. |
| **Revocation Propagation** | Propagates revocation or credential-state changes to the systems, workloads, or services currently relying on the affected secret. |
| **Secret Change Notification** | Notifies consuming systems that a secret has changed, expired, been rotated, or been revoked so they can refresh or terminate their use of it. |
| **Failure & Recovery** | Defines how the consuming system handles unavailable secrets, failed authentication, expired credentials, revoked credentials, or secret-management service failures. |
| **Access Auditing** | Records secret requests, authentication, authorization decisions, |

## Which technical mechanisms do programming languages and runtimes provide for implementing aspects of secret management?

| Language / Runtime | Technical Solution / Mechanism | Secret-Management Aspect | Description |
| --- | --- | --- | --- |
| **Java / Jakarta EE** | **JNDI** | Secret lookup / configuration | Provides a standardized naming mechanism through which applications can obtain configured resources and credentials without hard-coding them in application code. |
| **Java / Spring** | **Externalized Configuration** | Secret injection / configuration | Allows credentials and sensitive configuration to be supplied externally rather than embedded in application source. |
| **Java** | **Java KeyStore (JKS/PKCS12)** | Credential / key storage | Provides a protected container for cryptographic keys and certificates used by Java applications. |
| **Java** | **JAAS** | Authentication | Provides mechanisms for application authentication and credential handling. |
| **Python** | **`os.environ` / Environment Variables** | Secret injection | Allows applications to obtain secrets supplied through the process environment. |
| **Python** | **`keyring`** | Secret storage / retrieval | Provides an interface for accessing operating-system or platform credential stores. |
| **Python** | **`.env` / `python-dotenv`** | Local configuration / injection | Loads environment variables from a local configuration file, commonly used for development. |
| **Node.js** | **`process.env`** | Secret injection | Provides access to environment variables supplied to the Node.js process. |
| **Node.js** | **`.env` / built-in dotenv support** | Local configuration / injection | Loads environment-based configuration from `.env` files. |
| **Go** | **`os.Getenv` / `os.LookupEnv`** | Secret injection | Provides access to secrets supplied through environment variables. |
| **Rust** | **`std::env`** | Secret injection | Provides access to environment variables available to the process. |
| **C / C++** | **`getenv()`** | Secret injection | Allows applications to retrieve values supplied through the process environment. |
| **PHP** | **Environment Variables / `getenv()`** | Secret injection | Allows applications to obtain externally supplied credentials and configuration. |
| **Ruby** | **`ENV`** | Secret injection | Provides access to environment variables containing externally supplied configuration and credentials. |
| **.NET** | **Configuration Providers** | Secret injection / configuration | Provides abstractions for loading configuration and secrets from environment variables, files, user secrets, and external providers. |
| **.NET** | **Data Protection API** | Secret/key protection | Provides cryptographic protection for application data and key material. |
| **Shell / Unix** | **Environment Variables** | Secret injection | Supplies credentials to a process without placing them directly in command-line arguments or source code. |
| **Shell / Unix** | **File-based secrets** | Secret injection | Makes secrets available through protected filesystem objects with controlled permissions. |
| **Kubernetes** | **Secrets** | Secret distribution / injection | Provides an abstraction for making sensitive values available to containers through environment variables, volumes, or APIs. |
| **Docker / OCI** | **Build/Runtime Secrets** | Secret injection | Provides mechanisms for supplying secrets during image construction or container execution without permanently embedding them in images. |
| **CI/CD** | **Secret Variables / Secret Stores** | Secret injection | Injects credentials into build and deployment processes at runtime. |
| **Operating System** | **Credential Stores** | Secret storage / retrieval | Provides platform-level mechanisms for applications to retrieve credentials without maintaining their own plaintext secret stores. |

## How does the system establish initial trust and obtain the credentials required for its first authenticated access?

| Bootstrap Model | How Initial Trust Is Established | How First-Access Credentials Are Obtained |
| --- | --- | --- |
| **Pre-Provisioned Credential** | A trusted administrator or provisioning system establishes the initial trust relationship. | Token, password, key, or certificate is provisioned to the system beforehand. |
| **Machine Identity** | The system authenticates using a pre-established machine identity. | Credentials are derived from or issued to the machine identity. |
| **Workload Identity** | The execution environment provides an authenticated workload identity. | The system exchanges that identity for a short-lived access credential. |
| **Certificate-Based Bootstrap** | The system proves possession of a trusted private key and presents a certificate. | A certificate/private-key pair provides the initial authentication material. |
| **Hardware-Backed Identity** | A hardware security component establishes device authenticity. | The system uses hardware-protected keys to authenticate and obtain credentials. |
| **External Identity Provider** | An existing trusted identity system authenticates the system. | The system obtains an access token or temporary credential through an identity exchange. |
| **Operator Bootstrap** | A human administrator explicitly establishes the initial trust relationship. | The administrator provides or authorizes the initial credential. |
| **Out-of-Band Bootstrap** | Trust information is transferred through a separate trusted channel. | An initial token, key, certificate, or other bootstrap secret is securely transferred. |
| **Key-Based Bootstrap** | The system proves possession of a pre-established cryptographic key. | The key is used directly or to authenticate and obtain a subsequent credential. |

## References

- https://github.com/infisical/infisical
- [Hashicorp Vault](https://www.vaultproject.io/)
- https://varlock.dev/
- https://news.ycombinator.com/item?id=28301058
- https://news.ycombinator.com/item?id=16757364
- https://martinfowler.com/articles/session-secret.html
- https://blog.exe.dev/http-proxy-secrets
- https://news.ycombinator.com/item?id=47318528
- https://devenv.sh/
- https://devenv.sh/blog/2025/07/21/announcing-secretspec-declarative-secrets-management/
- https://github.com/tellerops/teller
-