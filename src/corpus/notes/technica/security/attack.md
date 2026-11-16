---
tags: [note, security, attack]
---

# Attack

> A **Note on Cybersecurity Attacks** — From the Perspective of a Law-Abiding Citizen - with the goal of defense.

## Attack Surface

> Which are the points of interaction through which an external or internal entity can influence, observe, or gain access to a technical ecosystem?
> The **Attack Surface** is the set of all interfaces, resources, services, identities, and trust relationships that are reachable by an attacker and therefore constitute potential entry points or targets for unauthorized interactions.

| **Category** | **Attack Surface** | **Description** |
| --- | --- | --- |
| Network | Open Ports | Listening network ports exposed to other systems. |
| Network | Network Services | Services such as SSH, HTTP, HTTPS, DNS, SMTP, FTP, etc. |
| Network | Wireless Networks | Wi-Fi, Bluetooth, NFC, Zigbee, and other wireless interfaces. |
| Web | Web Applications | Browser-accessible applications and websites. |
| Web | APIs | REST, GraphQL, gRPC, SOAP, and other service interfaces. |
| Identity | User Accounts | Human identities capable of authenticating to the system. |
| Identity | Service Accounts | Non-human identities used by applications and infrastructure. |
| Identity | Authentication Endpoints | Login pages, OAuth providers, SSO portals, VPN gateways. |
| Software | Executables | Applications installed on endpoints or servers. |
| Software | Libraries & Dependencies | Third-party software that may introduce vulnerabilities. |
| Data | Databases | Structured data stores accessible over the network or locally. |
| Data | File Systems | Shared folders, cloud storage, removable media. |
| Cloud | Cloud Services | Public cloud resources, storage, serverless functions, SaaS platforms. |
| Infrastructure | Virtual Machines | Compute instances hosting workloads. |
| Infrastructure | Containers | Docker containers, Kubernetes workloads, container registries. |
| Infrastructure | Hypervisors | Virtualization platforms. |
| Hardware | Endpoints | Laptops, desktops, mobile devices, IoT devices. |
| Hardware | Peripherals | USB devices, printers, smart cards, removable storage. |
| Physical | Facilities | Data centers, server rooms, network closets. |
| Supply Chain | Software Supply Chain | Package repositories, CI/CD pipelines, update mechanisms. |
| Trust | Certificates | Trusted certificates and certificate authorities. |
| Trust | Third-Party Integrations | External services connected to the ecosystem. |
| Human | Users | Employees, administrators, contractors, customers. |
| Human | Administrative Interfaces | Management consoles and operational dashboards. |

## Vulnerability Space

> Which weaknesses within a technical ecosystem can enable unauthorized or unintended interactions?
> The **Vulnerability Space** is the set of weaknesses in the design, implementation, configuration, operation, or governance of a technical ecosystem that may allow an attacker to violate the intended interaction policy.

| **Category** | **Vulnerability** | **Description** |
| --- | --- | --- |
| Authentication | Weak Authentication | Authentication mechanisms can be bypassed or easily compromised. |
| Authentication | Default Credentials | Factory or well-known credentials remain enabled. |
| Authentication | Missing MFA | Multi-factor authentication is not enforced where appropriate. |
| Authorization | Broken Access Control | Authorization checks are missing or incorrectly implemented. |
| Authorization | Excessive Privileges | Identities possess more permissions than required. |
| Authorization | Privilege Escalation | Weaknesses allow unauthorized acquisition of elevated privileges. |
| Input Validation | Injection | Untrusted input is interpreted as commands or queries (e.g., SQL, OS, LDAP). |
| Input Validation | Buffer Overflow | Input exceeds memory bounds, enabling arbitrary behavior. |
| Input Validation | Cross-Site Scripting (XSS) | Untrusted input executes within another user's browser. |
| Cryptography | Weak Cryptography | Insecure algorithms, protocols, or parameters are used. |
| Cryptography | Improper Key Management | Keys are poorly generated, stored, rotated, or protected. |
| Secrets | Hardcoded Secrets | Passwords, API keys, or tokens are embedded in source code or binaries. |
| Configuration | Misconfiguration | Insecure default or operational configuration. |
| Configuration | Unnecessary Services | Unused services increase the attack surface. |
| Configuration | Open Network Exposure | Services are unnecessarily reachable from untrusted networks. |
| Software | Unpatched Software | Known vulnerabilities remain unremediated. |
| Software | Vulnerable Dependency | Third-party components contain known weaknesses. |
| Software | Memory Safety Errors | Use-after-free, race conditions, or similar implementation flaws. |
| Data Protection | Sensitive Data Exposure | Confidential information is insufficiently protected. |
| Data Protection | Insecure Storage | Sensitive data is stored without adequate protection. |
| Logging | Insufficient Logging | Security-relevant events are not adequately recorded. |
| Monitoring | Insufficient Monitoring | Malicious activity cannot be detected in a timely manner. |
| Trust | Trust Misconfiguration | Certificates, trust anchors, or identity relationships are improperly configured. |
| Supply Chain | Compromised Dependency | Trusted software or hardware introduces malicious functionality. |
| Physical | Physical Exposure | Attackers can physically access protected assets. |
| Human | Social Engineering Susceptibility | Users can be manipulated into violating security policies. |

## Technique

> Which reusable technical techniques are used to execute attack tasks?

| **Category** | **Technique** | **Description** |
| --- | --- | --- |
| Initial Access | Phishing | Trick users into executing malicious actions. |
| Initial Access | Exploit Public-Facing Application | Exploit vulnerabilities exposed to external users. |
| Credential Access | Credential Dumping | Extract stored credentials from a compromised system. |
| Credential Access | Keylogging | Capture user keystrokes. |
| Execution | Command Injection | Execute arbitrary commands through vulnerable software. |
| Execution | SQL Injection | Execute database commands through unsanitized input. |
| Execution | DLL Injection | Inject malicious code into another process. |
| Persistence | Scheduled Tasks | Maintain recurring execution. |
| Persistence | Registry Modification | Achieve persistence through system configuration changes. |
| Defense Evasion | Obfuscation | Conceal malicious code or behavior. |
| Defense Evasion | Process Injection | Execute within another trusted process. |
| Discovery | Network Scanning | Discover hosts and services. |
| Discovery | Service Enumeration | Identify running services and configurations. |
| Lateral Movement | Pass-the-Hash | Reuse password hashes for authentication. |
| Collection | Screen Capture | Capture sensitive visual information. |
| Exfiltration | Data Compression | Reduce data size before transfer. |
| Exfiltration | Encrypted Channel | Hide stolen data within encrypted communications. |

### Attack Technique Space

> Which reusable technical techniques are used to execute attack tasks?

| **Category** | **Technique** | **Description** |
| --- | --- | --- |
| Initial Access | Phishing | Trick users into executing malicious actions. |
| Initial Access | Exploit Public-Facing Application | Exploit vulnerabilities exposed to external users. |
| Credential Access | Credential Dumping | Extract stored credentials from a compromised system. |
| Credential Access | Keylogging | Capture user keystrokes. |
| Execution | Command Injection | Execute arbitrary commands through vulnerable software. |
| Execution | SQL Injection | Execute database commands through unsanitized input. |
| Execution | DLL Injection | Inject malicious code into another process. |
| Persistence | Scheduled Tasks | Maintain recurring execution. |
| Persistence | Registry Modification | Achieve persistence through system configuration changes. |
| Defense Evasion | Obfuscation | Conceal malicious code or behavior. |
| Defense Evasion | Process Injection | Execute within another trusted process. |
| Discovery | Network Scanning | Discover hosts and services. |
| Discovery | Service Enumeration | Identify running services and configurations. |
| Lateral Movement | Pass-the-Hash | Reuse password hashes for authentication. |
| Collection | Screen Capture | Capture sensitive visual information. |
| Exfiltration | Data Compression | Reduce data size before transfer. |
| Exfiltration | Encrypted Channel | Hide stolen data within encrypted communications. |

### Attack Tool Space

> Which concrete technical objects are used to implement attack techniques?

| **Category** | **Attack Tool** | **Description** |
| --- | --- | --- |
| Reconnaissance | Nmap | Host discovery and port scanning. |
| Reconnaissance | Masscan | High-speed Internet-scale scanner. |
| Web Exploitation | Burp Suite | Web application interception and testing. |
| Web Exploitation | sqlmap | Automated SQL injection exploitation. |
| Exploitation Framework | Metasploit Framework | Exploit development and execution platform. |
| Credential Access | Mimikatz | Credential extraction from Windows systems. |
| Password Auditing | Hashcat | Password cracking and auditing. |
| Password Auditing | John the Ripper | Password auditing tool. |
| Remote Access | Cobalt Strike | Post-exploitation and command-and-control framework. |
| Remote Access | Sliver | Open-source adversary emulation framework. |
| Malware Development | msfvenom | Payload generation utility. |
| Malware Analysis | Ghidra | Reverse engineering platform. |
| Network Manipulation | Bettercap | Network interception and manipulation. |
| Wireless | Aircrack-ng | Wireless network assessment suite. |
| Command & Control | Mythic | Command-and-control platform. |
| Container | Peirates | Kubernetes and container exploitation tool. |

### **Strategy**

> Which are the high-level plans used by an adversary to achieve an attack objective?

| **Strategy** | **Description** |
| --- | --- |
| Phishing Campaign | Gain credentials or malware execution through social engineering. |
| Supply Chain Compromise | Attack a trusted supplier to reach downstream victims. |
| Watering Hole Attack | Compromise websites frequently visited by the target. |
| Insider Attack | Abuse legitimate access to achieve malicious objectives. |
| Ransomware Operation | Encrypt or exfiltrate data to extort the victim. |
| Living off the Land | Abuse legitimate system tools to avoid detection. |
| Credential Theft Campaign | Collect credentials for later unauthorized access. |
| Persistence Campaign | Establish long-term unauthorized access. |
| Denial-of-Service Campaign | Degrade or deny system availability. |
| Data Exfiltration Campaign | Steal sensitive information from the ecosystem. |

### **Method**

> Which operational procedures are followed to execute an attack strategy?

| **Method** | **Description** |
| --- | --- |
| Phishing Email | Deliver a malicious message to induce user interaction. |
| Spear Phishing | Target a specific individual with personalized content. |
| Drive-by Download | Deliver malware through a compromised website. |
| Password Spraying | Attempt common passwords across many accounts. |
| Credential Stuffing | Reuse leaked credentials against another service. |
| Brute Force | Systematically guess authentication secrets. |
| Exploit Delivery | Deliver an exploit to trigger a vulnerability. |
| Lateral Movement | Move between systems after initial compromise. |
| Privilege Escalation Workflow | Gain higher privileges after initial access. |
| Data Exfiltration Workflow | Transfer stolen information outside the ecosystem. |

## References

Conceptual Model: Cyber Attack

- https://www.cve.org/
- https://vuldb.com/
- https://www.exploit-db.com/
- https://github.com/berabuddies/redis-poc
