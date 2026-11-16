---
tags: [note, security, defense]
---

# Defense

> A Note on **cybersecurity** - from the **defense site.**

> **Cyber Defense** is the **technical domain** dedicated to **maintaining** and **restoring** the **conformance of interactions within**—and **with—**a technical ecosystem to its **interaction policy** whether explicit or implicit.

![image.png](../assets/note/technica/security/defense/image.png)

## QA

- Method Space
    - Category; Method; Goal
- What tool to used for **Local Certificate Authority**?
- Problem Space
    - How to ‘secret’ data, like password, api keys, private keys, etc? Which are the type of hows?
        - Store Directly in the Source Code.
        - Environment Variable (.env file, etc)
        - External Manager (Secret Manager):  HashiCorp Vault, AWS Secrets Manager, Google Secret Manager, Azure Key Vault.
        - Encrypt secrets at rest
        - Use OS-level secret stores (local development): GNOME Keyring, …
        - Secrets should be rotated periodically.
        - Restrict access (principle of least privilege)
        - Scan repositories for leaks
        - Secrete Lifecycle: Generation, Storage, Access Control, Usage, Rotation, and Revocation.
        - …
- …

## Formulation

> A **security model** is a protective framework outlining rules and mechanisms to safeguard systems, networks, or apps. It establishes controls, encryption, and access management to ensure data’s integrity, confidentiality, and availability. Covering authentication, authorization, auditing, and more, it guides systematic security implementation for diverse environments and threats.

> A **threat model** is a structured approach used to identify, assess, and prioritize potential security threats to a system, application, or network. It involves understanding how an adversary might attack, what assets are at risk, and the possible impact, which helps in designing appropriate security measures to mitigate those threats.

### Terminology

| **Concept** | **Description** |
| --- | --- |
| **Identity Model** | Defines identities (users, devices, services) and their attributes. |
| Authentication | Verifies identity (passwords, MFA, biometrics, etc.). |
| Authorization | Determines access rights (RBAC, ABAC, PBAC, etc.). |
| **Permission Model** | Grants/denies specific operations on resources (ACLs, capabilities). |
| Federation | Identity sharing across domains (e.g., SAML, OIDC). |
| **Identity Governance** | Lifecycle and compliance of digital identities. |
| Data Classification | Categorizing data by sensitivity (e.g., public, confidential). |
| Encryption | Securing data via cryptography (at rest, in transit, in use). |
| Tokenization | Replacing sensitive data with non-sensitive equivalents. |
| Masking | Hiding parts of data to protect privacy (e.g., showing only last 4 digits of a card). |
| Data Loss Prevention (DLP) | Preventing unauthorized data transfer or leakage. |
| Input Validation | Preventing injection attacks by sanitizing user inputs. |
| Secure Coding Practices | Techniques to avoid vulnerabilities during software development. |
| Code Signing | Ensuring code authenticity and integrity. |
| Dependency Management | Checking third-party libraries for vulnerabilities. |
| API Security | Protecting APIs using rate limiting, tokens, schema validation, etc. |
| Network Segmentation | Isolating systems/networks to contain breaches. |
| Firewalls | Filtering traffic based on rules (perimeter & application level). |
| Intrusion Detection/Prevention (IDS/IPS) | Monitoring or blocking suspicious activity. |
| Endpoint Detection & Response (EDR) | Monitoring, detecting, and responding on end devices. |
| Patch Management | Keeping systems up-to-date to close known vulnerabilities. |
| Symmetric Encryption | One key for both encryption/decryption (e.g., AES). |
| Asymmetric Encryption | Key pair system (e.g., RSA, ECC). |
| Hashing | One-way functions for data integrity (e.g., SHA-256). |
| Digital Signatures | Ensuring authenticity and integrity of messages. |
| Public Key Infrastructure (PKI) | Managing digital certificates and key pairs. |
| Logging & Auditing | Keeping records of system activity and changes. |
| Security Information and Event Management (SIEM) | Centralized log analysis and alerting. |
| Threat Detection | Identifying malicious activity (e.g., behavioral analytics). |
| Incident Response | Processes for handling security breaches or alerts. |
| Forensics | Analyzing breaches to determine scope, actors, and causes. |
| Policies & Standards | Organizational rules and best practices (e.g., ISO 27001, NIST). |
| Risk Management | Identifying and mitigating potential threats and impacts. |
| Security Awareness Training | Educating users to avoid social engineering and risky behaviors. |
| Compliance | Adherence to laws and regulations (e.g., GDPR, HIPAA, PCI DSS). |
| Access Control Systems | Restricting physical access to sensitive areas. |
| Surveillance & Monitoring | Cameras, sensors, intrusion alarms. |
| Environmental Controls | Fire suppression, temperature, and humidity management. |
| Zero Trust Architecture | “Never trust, always verify” — assumes breach and verifies every request. |
| Security by Design | Integrating security throughout the system lifecycle. |
| Threat Modeling | Identifying possible attack vectors during system design. |
| Red Teaming | Simulating attacks to test defenses. |
| Blue Teaming | Defending against simulated or real attacks. |
| Supply Chain Security | Ensuring security of software, hardware, and services you depend on. |
| Privacy Engineering | Embedding privacy into system architecture (e.g., data minimization, differential privacy). |

### Technical Categorical Decomposition

| **Category** | **Cybersecurity Defense Specialization** |
| --- | --- |
| Technical Domain | Cyber Defense |
| Technical Problem | Unauthorized or unintended interactions with a technical ecosystem |
| Technical Purpose | Preserve or restore the intended secure operational state of a technical ecosystem |
| Technical Object | Information systems, networks, endpoints, identities, applications, OT/ICS, cloud infrastructure |
| Technical Agent | SOC analyst, defender, EDR, firewall, IDS, SIEM, IAM, automated response system |
| Technical Practice | Threat detection, incident response, vulnerability management, hardening, security monitoring |
| Technical Activity | Monitor, investigate, contain, eradicate, recover, validate |
| Technical Task | Analyze alert, deploy patch, revoke credentials, isolate host |
| Technical Act | Block connection, terminate process, modify ACL, update firewall rule |
| Technique | Signature detection, behavioral analysis, sandboxing, memory forensics, least privilege enforcement |
| Technical Mechanism | Authentication, authorization, encryption, sandboxing, logging, packet filtering |
| Technical Principle | Defense in depth, least privilege, complete mediation, fail secure, zero trust |
| Technical Standard | NIST CSF, CIS Controls, ISO 27001, MITRE ATT&CK mappings |
| Technical Feedback | Alerts, telemetry, logs, EDR events, threat intelligence, integrity checks |
| Technical Constraint | Performance, usability, compatibility, legal requirements, incomplete visibility |
| Technical Failure | Successful compromise, unauthorized access, privilege escalation, persistence, service disruption |
| Maintenance | Patch management, certificate rotation, rule tuning, key rotation, backup validation |

### Technical Purpose

| **Goal** | **Definition** | **What It Protects Against** | **Common Mechanisms** |
| --- | --- | --- | --- |
| **Confidentiality** | Ensures that information is **accessible only to authorized parties**. | Eavesdropping, information leakage | Encryption, Access Control, VPNs, Data Masking |
| **Integrity** | Ensures that data is **accurate and has not been altered** in an unauthorized way. | Tampering, forgery, unauthorized modification | Hashing, Digital Signatures, Checksums, Version Control |
| **Availability** | Ensures that systems and data are **accessible and usable** when needed. | Denial-of-Service (DoS), outages | Redundancy, Load Balancing, Failover, DDoS Mitigation |
| **Authentication** | Ensures the **identity of users, devices, or systems** is verified. | Identity spoofing, impersonation | Passwords, Biometrics, Multi-Factor Authentication (MFA) |
| **Authorization** | Determines **what actions or resources** a verified user can access. | Privilege escalation, over-permissioned users | Access Control Lists (ACLs), RBAC, ABAC |
| **Non-repudiation** | Prevents entities from **denying their actions** or communications. | False denials, repudiation | Digital Signatures, Logging, Audit Trails |
| **Accountability** | Ensures **actions can be traced** to responsible entities. | Misuse without traceability | Auditing, Logging, Traceability Systems |
| **Privacy** | Ensures **personal and sensitive data** is protected and handled properly. | Profiling, surveillance, data misuse | Data Minimization, Consent Mechanisms, Anonymization |
| **Resilience** | Ensures systems can **recover from attacks or failures** and continue operating. | System crashes, security breaches | Backups, Incident Response, Fault-Tolerant Architecture |

## Problem Space

> Which are the set of problems that a cyber defense agent needs to solved?

| **Problem** | **Description** |
| --- | --- |
| **Unauthorized Access** | An entity gains access to a resource without possessing the required authorization. |
| **Unauthorized Disclosure** | Information is observed, copied, or transmitted to entities not permitted to receive it. |
| **Unauthorized Modification** | Data, software, configurations, or system state are altered in violation of the interaction policy. |
| **Unauthorized Execution** | Software, commands, or workflows execute without being permitted by the intended operational rules. |
| **Unauthorized Resource Consumption** | Computing, storage, memory, network bandwidth, or other resources are consumed beyond authorized limits, degrading availability. |
| **Unauthorized Communication** | Information flows occur between entities that should not communicate according to policy. |
| **Unauthorized Identity Use** | An identity is impersonated, forged, stolen, or otherwise used by an entity not entitled to act as that identity. |
| **Unauthorized Privilege Acquisition** | An entity obtains permissions or capabilities beyond those intended by the system. |
| **Policy Violation** | A permitted actor performs an action that violates organizational, operational, or security policy, whether intentionally or accidentally. |
| **Integrity Violation** | The correctness, consistency, or authenticity of information or system state can no longer be trusted. |
| **Availability Violation** | A service or resource cannot be accessed or operated according to its intended availability requirements. |
| **Trust Violation** | The authenticity or provenance of software, hardware, identities, communications, or data can no longer be established or relied upon. |
| **Persistence of Unauthorized State** | An unauthorized system state remains present despite intended mechanisms for detection, recovery, or removal. |
| **Uncontrolled External Interaction** | Interactions entering or leaving the ecosystem occur outside the intended trust boundaries or established interaction policy. |

## Task Space

> Which are tasks that a `cyber defense`  agent can attack?

> The Task Space defines the discrete units of work that a Cyber Defense agent can perform to detect, analyze, prevent, contain, recover from, or remediate interaction-policy violations.

| **Task** | **Description** |
| --- | --- |
| Monitor System | Observe system behavior, events, and interactions for deviations from the intended interaction policy. |
| Collect Telemetry | Gather logs, metrics, traces, packets, and endpoint data for analysis. |
| Detect Threats | Identify unauthorized or suspicious interactions. |
| Generate Alerts | Notify operators or automated systems when policy violations are detected. |
| Investigate Incident | Analyze evidence to determine the nature, scope, and cause of a security event. |
| Assess Risk | Evaluate the likelihood and impact of observed vulnerabilities or threats. |
| Validate Identity | Verify the identity of users, devices, services, or processes. |
| Authorize Access | Determine whether a requested interaction complies with the interaction policy. |
| Enforce Access Control | Apply permissions, ACLs, RBAC, ABAC, or other authorization mechanisms. |
| Inspect Traffic | Analyze network communications for malicious or unauthorized behavior. |
| Scan for Vulnerabilities | Identify weaknesses that could enable policy violations. |
| Harden Systems | Configure systems to reduce the attack surface and enforce security policy. |
| Apply Patches | Correct known vulnerabilities through software or firmware updates. |
| Protect Secrets | Secure credentials, keys, certificates, and other sensitive material. |
| Verify Integrity | Confirm that software, data, and configurations have not been improperly modified. |
| Isolate Assets | Prevent compromised components from interacting with the rest of the ecosystem. |
| Block Interaction | Prevent unauthorized communications, executions, or resource access. |
| Remove Threat | Eliminate malware, unauthorized software, accounts, or persistence mechanisms. |
| Recover System | Restore systems and services to an intended secure operational state. |
| Restore Data | Recover information from trusted backups or other recovery mechanisms. |
| Rotate Credentials | Replace passwords, keys, certificates, or tokens that may be compromised. |
| Audit Compliance | Verify that systems and interactions satisfy security policies and standards. |
| Produce Evidence | Record logs, artifacts, and forensic evidence for accountability or investigation. |
| Update Security Policy | Modify rules or configurations in response to new requirements or threats. |

## Product Space

> What are the products of Cyber Defense? How is the conceptual scaffold of the Cyber Defense domain manifested in practice?

> The Product Space defines the outputs produced by Cyber Defense. These outputs operationalize security principles into deployable artifacts, operational capabilities, and supporting documentation that collectively preserve the secure operational state of a technical ecosystem.

> **Note:** A **product** is **not** a **tool**. A tool is an instrument used to produce or operate on a product; a product is the artifact or capability resulting from Cyber Defense activities.

| **Product** | **Description** |
| --- | --- |
| Security Policy | Specification of the interaction rules governing the ecosystem. |
| Access Control Policy | Rules defining which identities may perform which interactions. |
| Firewall Rule Set | Network filtering rules enforcing communication policy. |
| IAM Configuration | Identity and access management configuration defining authentication and authorization behavior. |
| Cryptographic Keys | Keys generated to support encryption, signatures, and authentication. |
| Digital Certificates | Credentials binding identities to cryptographic keys. |
| Public Key Infrastructure (PKI) | Certificate hierarchy supporting trust establishment. |
| Secrets | Passwords, API keys, tokens, and other protected credentials. |
| Security Configuration (Baseline) | Hardened configuration of operating systems, applications, or infrastructure. |
| Detection Rules | Signatures, behavioral rules, or analytics used to detect policy violations. |
| Threat Intelligence | Structured knowledge describing adversaries, indicators, tactics, and vulnerabilities. |
| Security Alerts | Notifications indicating suspected interaction-policy violations. |
| Audit Logs | Persistent records of security-relevant interactions. |
| Incident Report | Structured documentation of a security incident, its impact, and resolution. |
| Forensic Evidence | Collected artifacts supporting investigation and attribution. |
| Vulnerability Assessment | Report describing discovered weaknesses and associated risks. |
| Risk Assessment | Analysis of security risks and recommended mitigations. |
| Security Architecture | Structural design specifying security controls and trust boundaries. |
| Secure Software | Software produced according to secure development practices. |
| Hardened System Image | Preconfigured secure operating system or application image. |
| Backup | Trusted copy of system state or data for recovery purposes. |
| Recovery Plan | Procedures for restoring secure operations following disruption. |
| Monitoring Dashboard | Operational view of security telemetry and system health. |
| Compliance Report | Evidence demonstrating conformance to standards or regulations. |

## Technique

> How to operational defense?

### Technique Space

> Which are techniques in executing cyber defense tasks?

| **Category** | **Technique** | **Description** |
| --- | --- | --- |
| Authentication | Password Authentication | Authenticates users using a shared secret. |
| Authentication | Multi-Factor Authentication (MFA) | Combines multiple authentication factors. |
| Authentication | Certificate-Based Authentication | Uses digital certificates for identity verification. |
| Authentication | FIDO2/WebAuthn | Passwordless authentication using cryptographic authenticators. |
| Authorization | Role-Based Access Control (RBAC) | Grants permissions according to organizational roles. |
| Authorization | Attribute-Based Access Control (ABAC) | Makes authorization decisions using attributes. |
| Authorization | Capability-Based Access Control | Grants permissions through capabilities or tokens. |
| Encryption | Symmetric Encryption | Uses a shared key for confidentiality. |
| Encryption | Asymmetric Encryption | Uses public/private key pairs. |
| Encryption | Envelope Encryption | Combines symmetric and asymmetric cryptography for scalable key management. |
| Integrity | Digital Signatures | Verifies authenticity and integrity of data. |
| Integrity | Hash-Based Integrity Verification | Detects unauthorized modification using cryptographic hashes. |
| Detection | Signature-Based Detection | Detects known malicious patterns. |
| Detection | Behavioral Analysis | Detects deviations from expected behavior. |
| Detection | Anomaly Detection | Detects statistically unusual activity. |
| Detection | Heuristic Analysis | Detects suspicious behavior using expert-defined rules. |
| Detection | Threat Intelligence Matching | Matches telemetry against known indicators of compromise. |
| Network Protection | Packet Filtering | Filters traffic according to predefined rules. |
| Network Protection | Stateful Inspection | Tracks connection state during filtering. |
| Network Protection | Deep Packet Inspection | Examines packet payloads for policy enforcement. |
| Network Protection | Microsegmentation | Enforces fine-grained communication restrictions. |
| Malware Defense | Sandboxing | Executes software within an isolated environment. |
| Malware Defense | Application Whitelisting | Allows execution only of approved applications. |
| Malware Defense | Behavior Blocking | Prevents malicious runtime behavior. |
| Vulnerability Assessment | Static Analysis (SAST) | Examines source code without execution. |
| Vulnerability Assessment | Dynamic Analysis (DAST) | Evaluates software during execution. |
| Vulnerability Assessment | Fuzz Testing | Generates malformed inputs to discover vulnerabilities. |
| Vulnerability Assessment | Dependency Analysis (SCA) | Identifies vulnerabilities in third-party components. |
| Monitoring | Log Correlation | Combines multiple events into higher-level incidents. |
| Monitoring | Continuous Monitoring | Continuously evaluates security posture. |
| Monitoring | User and Entity Behavior Analytics (UEBA) | Models behavior to identify anomalies. |
| Incident Response | Host Isolation | Disconnects compromised endpoints. |
| Incident Response | Credential Rotation | Replaces compromised credentials. |
| Incident Response | Snapshot Restoration | Restores trusted system state from backups. |

### Technical Principle Space

> Which are the set of technical principles that guides cyber defense?

| **Technical Principle** | **Description** |
| --- | --- |
| Least Privilege | Grant only the minimum permissions required to perform an authorized task. |
| Defense in Depth | Employ multiple, independent layers of defense to reduce the likelihood of compromise. |
| Zero Trust | Continuously verify every interaction regardless of origin; trust is never assumed. |
| Complete Mediation | Evaluate every access request against the applicable security policy. |
| Fail Secure (Fail Closed) | Upon failure, default to the most secure operational state. |
| Separation of Privilege | Require multiple independent conditions or authorities before granting sensitive operations. |
| Separation of Duties | Divide critical responsibilities among multiple agents to reduce abuse and error. |
| Least Common Mechanism | Minimize shared mechanisms to reduce unintended interaction and attack surfaces. |
| Economy of Mechanism | Prefer simple designs that are easier to understand, verify, and secure. |
| Minimize Attack Surface | Reduce exposed interfaces, services, software, and privileges to limit opportunities for attack. |
| Secure by Default | Configure systems to operate securely without requiring additional user action. |
| Secure by Design | Integrate security considerations throughout the entire system lifecycle. |
| Explicit Trust Boundaries | Clearly define and enforce boundaries between trusted and untrusted entities. |
| Principle of Isolation | Segregate components, workloads, or users to limit the propagation of failures or attacks. |
| Compartmentalization | Partition systems and information so that compromise is contained within defined boundaries. |
| Least Functionality | Enable only the functionality required for the intended operation. |
| Assume Breach | Design and operate under the assumption that compromise is possible or already exists. |
| Continuous Verification | Continuously validate identities, devices, configurations, and system integrity. |
| Accountability | Ensure that actions are attributable to identifiable entities through logging and auditing. |
| Traceability | Maintain sufficient evidence to reconstruct security-relevant events. |
| Tamper Evident | Design artifacts and systems so unauthorized modifications are detectable. |
| Resilience | Maintain or rapidly restore secure operation despite failures or attacks. |
| Recoverability | Ensure that systems can be restored to a trusted operational state after compromise. |
| Security Automation | Automate repetitive defensive activities to improve consistency, speed, and reliability. |
| Continuous Monitoring | Continuously observe system state and interactions to detect policy violations. |
| Defense Proportionality | Select controls that are appropriate to the value of protected assets and assessed risk. |
| Risk-Based Security | Prioritize defensive measures according to the likelihood and impact of threats. |
| Principle of Least Exposure | Minimize disclosure of information, metadata, and system interfaces. |
| Cryptographic Protection | Protect confidentiality, integrity, authenticity, and non-repudiation using sound cryptographic methods. |
| Secure Configuration | Maintain systems in a hardened and policy-compliant configuration throughout their lifecycle. |

### Technical Mechanism Space

> Which technical mechanisms are used to enforce, preserve, detect, verify, or restore the intended interaction policy of a technical ecosystem?

**Mechanism - vs  Technical Production Object vs  Technique:** 

- Mechanism:  How does this works?
- Technique: How to implement a mechanism?
- Production Technical Object:  With what concrete object is the technique executed?

| **Category** | **Technical Mechanism** | **Description** |
| --- | --- | --- |
| Identity | Authentication | Verifies the identity of a user, device, service, or process before interaction is permitted. |
| Identity | Multi-Factor Authentication (MFA) | Combines multiple independent authentication factors. |
| Identity | Federation | Shares identity across administrative domains. |
| Authorization | Authorization | Determines whether an authenticated identity is permitted to perform an operation. |
| Authorization | Role-Based Access Control (RBAC) | Grants permissions according to organizational roles. |
| Authorization | Attribute-Based Access Control (ABAC) | Makes authorization decisions based on attributes. |
| Authorization | Capability-Based Access Control | Grants access through transferable capabilities or tokens. |
| Authorization | Policy Decision Point (PDP) | Evaluates access requests against security policies. |
| Cryptography | Symmetric Encryption | Protects confidentiality using a shared secret key. |
| Cryptography | Asymmetric Encryption | Uses public/private key pairs for confidentiality and authentication. |
| Cryptography | Hashing | Produces fixed-length integrity digests. |
| Cryptography | Digital Signature | Verifies authenticity and integrity of digital objects. |
| Cryptography | Key Exchange | Securely establishes shared cryptographic keys. |
| Cryptography | Key Derivation | Derives cryptographic keys from shared secrets or passwords. |
| Trust | Public Key Infrastructure (PKI) | Establishes trust through certificates and certificate authorities. |
| Trust | Certificate Validation | Verifies certificate authenticity and validity. |
| Trust | Certificate Revocation | Invalidates compromised or expired certificates. |
| Trust | Code Signing | Verifies software origin and integrity. |
| Network Protection | Packet Filtering | Permits or denies packets according to policy. |
| Network Protection | Stateful Inspection | Tracks connection state while enforcing policies. |
| Network Protection | Deep Packet Inspection (DPI) | Examines packet payloads for policy enforcement. |
| Network Protection | Network Segmentation | Isolates network zones to limit interaction. |
| Network Protection | Microsegmentation | Enforces fine-grained communication policies between workloads. |
| Detection | Signature Detection | Detects known malicious patterns. |
| Detection | Behavioral Analysis | Detects deviations from expected behavior. |
| Detection | Anomaly Detection | Identifies statistically abnormal activity. |
| Detection | Threat Correlation | Correlates multiple security events into incidents. |
| Detection | Threat Intelligence Matching | Matches telemetry against known indicators of compromise. |
| Endpoint Protection | Process Isolation | Prevents processes from interfering with one another. |
| Endpoint Protection | Sandboxing | Executes code within an isolated environment. |
| Endpoint Protection | Application Whitelisting | Allows execution only of approved software. |
| Endpoint Protection | Memory Protection | Prevents exploitation through memory safety mechanisms. |
| Data Protection | Data Encryption at Rest | Protects stored information. |
| Data Protection | Data Encryption in Transit | Protects communications between systems. |
| Data Protection | Tokenization | Replaces sensitive values with non-sensitive tokens. |
| Data Protection | Data Masking | Conceals sensitive information while preserving usability. |
| Data Protection | Data Loss Prevention (DLP) | Prevents unauthorized disclosure of sensitive information. |
| Integrity | Integrity Verification | Detects unauthorized modification of software or data. |
| Integrity | File Integrity Monitoring | Continuously monitors protected files for changes. |
| Integrity | Secure Boot | Verifies software during system startup. |
| Monitoring | Logging | Records security-relevant events. |
| Monitoring | Auditing | Evaluates actions against policy and compliance requirements. |
| Monitoring | Telemetry Collection | Collects operational security data. |
| Monitoring | Continuous Monitoring | Continuously evaluates system security posture. |
| Response | Automated Response | Executes predefined remediation actions automatically. |
| Response | Host Isolation | Disconnects compromised systems from the network. |
| Response | Credential Revocation | Invalidates compromised credentials. |
| Response | Backup Restoration | Restores trusted system state following compromise. |
| Resilience | Redundancy | Provides alternate components to maintain availability. |
| Resilience | Failover | Transfers operation to standby systems after failure. |
| Resilience | Disaster Recovery | Restores services following major disruption. |
| Secure Development | Input Validation | Ensures inputs conform to expected formats and constraints. |
| Secure Development | Output Encoding | Prevents injection attacks by safely encoding outputs. |
| Secure Development | Dependency Verification | Validates third-party software integrity. |
| Secure Development | Static Analysis | Identifies vulnerabilities without executing software. |
| Secure Development | Dynamic Analysis | Detects vulnerabilities during software execution. |

### Technical Production Object Space

| **Category** | **Production Technical Object** | **Description** |
| --- | --- | --- |
| Cryptography | OpenSSL | Cryptographic toolkit for encryption, hashing, digital signatures, TLS, and PKI. |
| Cryptography | GnuPG (GPG) | OpenPGP encryption and digital signature toolkit. |
| Cryptography | age | Modern file encryption utility. |
| Public Key Infrastructure (PKI) | mkcert | Local certificate authority and certificate generation. |
| Public Key Infrastructure (PKI) | CFSSL | PKI toolkit and certificate authority. |
| Public Key Infrastructure (PKI) | Smallstep CA | Automated certificate authority platform. |
| Secret Management | HashiCorp Vault | Enterprise secret management platform. |
| Secret Management | Infisical | Secret management platform. |
| Secret Management | AWS Secrets Manager | Cloud secret management service. |
| Secret Management | Azure Key Vault | Cloud key and secret management platform. |
| Secret Management | Google Secret Manager | Managed cloud secret storage. |
| Identity & Access Management (IAM) | Keycloak | Identity provider implementing OAuth2, OIDC, and SAML. |
| Identity & Access Management (IAM) | Microsoft Entra ID | Enterprise identity management platform. |
| Identity & Access Management (IAM) | FreeIPA | Linux identity and policy management. |
| Identity & Access Management (IAM) | Authentik | Self-hosted identity provider. |
| Multi-Factor Authentication (MFA) | Duo Security | Multi-factor authentication platform. |
| Privileged Access Management (PAM) | CyberArk | Privileged credential management platform. |
| Network Discovery | Nmap | Network discovery and security auditing. |
| Network Discovery | Masscan | High-speed Internet-scale port scanner. |
| Network Analysis | Wireshark | Packet capture and protocol analysis. |
| Network Analysis | tcpdump | Command-line packet analyzer. |
| Firewall | pfSense | Open-source firewall and router platform. |
| Firewall | OPNsense | Open-source firewall platform. |
| Firewall | Palo Alto NGFW | Next-generation firewall platform. |
| Web Application Firewall (WAF) | ModSecurity | Open-source web application firewall. |
| Web Application Firewall (WAF) | Cloudflare WAF | Managed web application firewall. |
| Intrusion Detection & Prevention (IDS/IPS) | Snort | Signature-based IDS/IPS. |
| Intrusion Detection & Prevention (IDS/IPS) | Suricata | High-performance IDS/IPS. |
| Intrusion Detection & Prevention (IDS/IPS) | Zeek | Network security monitoring framework. |
| Endpoint Protection | Microsoft Defender Antivirus | Endpoint malware protection. |
| Endpoint Protection | ClamAV | Open-source antivirus engine. |
| Endpoint Detection & Response (EDR/XDR) | Microsoft Defender for Endpoint | Endpoint detection and response. |
| Endpoint Detection & Response (EDR/XDR) | CrowdStrike Falcon | Cloud-native EDR platform. |
| Endpoint Detection & Response (EDR/XDR) | SentinelOne | Autonomous endpoint protection. |
| Endpoint Detection & Response (EDR/XDR) | Wazuh | Open-source XDR platform. |
| Vulnerability Assessment | Nessus | Enterprise vulnerability scanner. |
| Vulnerability Assessment | OpenVAS | Open-source vulnerability scanner. |
| Vulnerability Assessment | Qualys VM | Cloud vulnerability management. |
| Configuration Compliance | OpenSCAP | Security configuration assessment framework. |
| Configuration Compliance | Lynis | Security auditing tool. |
| Security Information & Event Management (SIEM) | Splunk Enterprise Security | Enterprise SIEM platform. |
| Security Information & Event Management (SIEM) | Microsoft Sentinel | Cloud-native SIEM/SOAR. |
| Security Information & Event Management (SIEM) | Elastic Security | SIEM and analytics platform. |
| Security Information & Event Management (SIEM) | IBM QRadar | Enterprise SIEM. |
| Security Orchestration, Automation & Response (SOAR) | Cortex XSOAR | Security automation platform. |
| Security Orchestration, Automation & Response (SOAR) | Splunk SOAR | Automated incident response. |
| Threat Intelligence | MISP | Threat intelligence sharing platform. |
| Threat Intelligence | OpenCTI | Threat intelligence management platform. |
| Digital Forensics | Autopsy | Digital forensic investigation platform. |
| Digital Forensics | FTK | Enterprise forensic toolkit. |
| Memory Forensics | Volatility | Memory analysis framework. |
| Malware Analysis | Ghidra | Reverse engineering platform. |
| Malware Analysis | IDA Pro | Interactive disassembler. |
| Malware Analysis | Cuckoo Sandbox | Automated malware analysis sandbox. |
| Web Application Security | Burp Suite | Web application penetration testing suite. |
| Web Application Security | OWASP ZAP | Open-source web security testing platform. |
| API Security | Postman Security | API testing and security validation. |
| Container Security | Trivy | Container and dependency vulnerability scanner. |
| Container Security | Falco | Runtime container threat detection. |
| Kubernetes Security | Kubescape | Kubernetes security scanner. |
| Kubernetes Security | kube-bench | Kubernetes CIS benchmark assessment. |
| Cloud Security | Wiz | Cloud security posture management. |
| Cloud Security | Prisma Cloud | Cloud-native application protection platform. |
| Cloud Security | Prowler | AWS/Azure/GCP security assessment tool. |
| Data Loss Prevention (DLP) | Microsoft Purview DLP | Enterprise data loss prevention. |
| Database Security | Oracle Database Vault | Database security and access control. |
| Backup & Recovery | Veeam Backup & Replication | Enterprise backup platform. |
| Backup & Recovery | Restic | Encrypted backup utility. |
| Backup & Recovery | BorgBackup | Deduplicating backup tool. |
| Supply Chain Security | Sigstore | Software artifact signing infrastructure. |
| Supply Chain Security | Cosign | Container image signing utility. |
| Supply Chain Security | Syft | Software Bill of Materials (SBOM) generator. |
| Supply Chain Security | Grype | SBOM-based vulnerability scanner. |
| Static Application Security Testing (SAST) | Semgrep | Static code security analysis. |
| Static Application Security Testing (SAST) | SonarQube | Code quality and security analysis. |
| Software Composition Analysis (SCA) | Dependency-Check | Dependency vulnerability analysis. |
| Software Composition Analysis (SCA) | Snyk | Dependency and container security platform. |
| Infrastructure Automation | Terraform | Infrastructure-as-Code provisioning. |
| Infrastructure Automation | Ansible | Configuration management and automation. |
| Infrastructure Automation | Puppet | Infrastructure configuration management. |
| Infrastructure Automation | Chef | Infrastructure automation framework. |
| Certificate Transparency | Trillian | Certificate transparency log server. |
| Password Auditing | Hashcat | Password auditing and recovery. |
| Password Auditing | John the Ripper | Password auditing tool. |

## Evaluation

> How to evaluate the **defense layer**?

## QA

### Should I have one or many private keys?

> **You should have many private keys**, each with a distinct purpose. A private key represents an identity or cryptographic role, not a person.

| **Purpose** | **Separate Private Key?** | **Reason** |
| --- | --- | --- |
| Root Certificate Authority | Yes | Highest trust; kept offline. |
| Intermediate CA | Yes | Issues certificates without exposing the root key. |
| TLS Server Certificate | Yes (per server or service) | Limits impact if one server is compromised. |
| Code Signing | Yes | Separate trust domain from TLS. |
| Email (S/MIME) | Yes | Separate communications from infrastructure. |
| SSH Authentication | Yes | Authenticate administrators or services. |
| Document Signing | Yes | Digital signatures for documents. |
| Disk Encryption | Yes | Protect stored data independently. |
| VPN Authentication | Yes | Separate remote access credentials. |
| JWT/OAuth Signing | Yes | Sign authentication tokens. |

## References

Conceptual Model: Cyber Defense

- [Sigstore](https://www.sigstore.dev/)
- https://jwt.io/
- [Linux Security Stack](/view.html?p=notes/technica/computation/operating-system/linux/linux-security-stack.md)
- [Computer Security Model](https://en.wikipedia.org/wiki/Computer_security_model)
- [Hashing, Encryption, and Encoding](https://www.integralist.co.uk/posts/hashing-and-encryption/)
- https://github.com/dbremont/system-design-labs/blob/main/tool/OpenSSL.md
- [A Look Back at “Security Problems in the TCP/IP Protocol Suite”](https://css.csail.mit.edu/6.858/2020/readings/lookback-tcpip.pdf)
- https://github.com/dbremont/system-design-labs/blob/main/tool/Pretty%20Good%20Privacy%20(PGP).md
- [Ken Thompson Really Did Launch His “Trusting Trust” Trojan Attack in Real Life](https://lwn.net/SubscriberLink/909469/95386a9171af0b46/)
- [The Quest to Replace Passwords: A Framework for Comparative Evaluation of Web Authentication Schemes](https://ieeexplore.ieee.org/document/6234436)
- Bellovin, S. M. (1989). Security problems in the TCP/IP protocol suite. 19(2), 32–48.
- Burrows, M., Abadi, M., & Needham, R. (1990). A logic of authentication. 8(1), 18–36.
- Shannon, C. E. (1948). A mathematical theory of communication. ACM SIGMOBILE Mobile Computing and Communications Review, 5(1), 3–55.
- https://brootware.github.io/awesome-cyber-security-university/
- https://webauthn.io/
- https://brootware.github.io/awesome-cyber-security-university/
- https://github.com/hashicorp/vault
- https://www.reddit.com/r/cybersecurity/comments/1njw3kn/selfhosted_secrets_management_alternatives_to/
- https://infisical.com/ https://github.com/Infisical/infisical
- https://news.ycombinator.com/item?id=22136699
