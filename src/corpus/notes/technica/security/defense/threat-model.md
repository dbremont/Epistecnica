---
tags: [note, security, defense, threat]
---

# Threat Model


> A **threat model is a structured representation** of potential threats to a system or application. It is a cybersecurity and information security tool to identify, assess, and mitigate security risks. Threat modeling is a systematic approach to understanding and documenting the various threats and vulnerabilities affecting a system’s security.

[https://pbs.twimg.com/media/GLrfNTEWgAAjxSd?format=jpg](https://pbs.twimg.com/media/GLrfNTEWgAAjxSd?format=jpg)

## Goals

The primary goals of **threat modeling** are to:

1. **Identify Threats:** Determine the potential threats and vulnerabilities that could compromise the security of a system. These threats include malicious activities, software vulnerabilities, human errors, and more.
2. **Assess Risks:** Evaluate the impact and likelihood of each identified threat. Determine the potential consequences of a successful attack or security breach, such as data breaches, service disruptions, or financial losses.
3. **Prioritize Mitigations:** Once threats and risks are identified and assessed, prioritize them based on severity and potential impact. Focus on addressing the most critical threats first.
4. **Guide Security Controls:** Use the threat model to inform the selection and implementation of security controls and countermeasures. These controls include firewalls, encryption, access controls, intrusion detection systems, and more.
5. **Iterate and Improve:** Threat modeling is an iterative process. As the system evolves or new threats emerge, threat models should be updated and refined to reflect changes in the threat landscape.

## Modelling Workflow

> Standard methodologies and tools are available for conducting threat modeling, such as STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege), DREAD (Damage, Reproducibility, Exploitability, Affected users, Discoverability), and various threat modeling software applications.

> Effective threat modeling helps organizations proactively address security concerns and make informed decisions about where to allocate resources to protect their systems and data from potential threats and attacks.

Threat modeling can take various forms, but it often involves the following steps:

1. **Asset Identification:** Identify the assets within the system that need protection, such as data, hardware, software, and network components.
2. **Threat Identification:** Identify potential threats and attackers who may target the system. This includes considering various attack vectors and scenarios.
3. **Vulnerability Assessment:** Identify vulnerabilities or weaknesses in the system that attackers could exploit.
4. **Risk Assessment:** Evaluate the likelihood and impact of each threat, and assign risk scores or rankings to prioritize them.
5. **Countermeasure Selection:** Determine the security controls and countermeasures that can mitigate or reduce the identified risks.
6. **Documentation:** Document the threat model, including the identified threats, vulnerabilities, risks, and recommended countermeasures.

## Thread

> A **threat** is **any potential danger that can exploit a vulnerability to cause harm or damage to a computer system, network, or data**. It represents an action or event that can compromise the confidentiality, integrity, or availability of information or systems.

| **Category** | **Dimension** | **Description** | **Case Study** |
| --- | --- | --- | --- |
| **Threat Actor** | Source/Origin | The entity or individual behind the threat. | Nation-states, cybercriminal groups, insiders, hacktivists, script kiddies |
| **Motivation** | Purpose/Intent | The reason or goal driving the threat actor to launch the attack. | Financial gain, espionage, disruption, ideological reasons, revenge |
| **Attack Vector** | Method of Delivery | The technique or path used to carry out the attack or breach. | Phishing emails, malware, exploit kits, brute force, insider access |
| **Target** | Victim or Asset | The system, organization, or data that is targeted or affected. | Corporate networks, critical infrastructure, personal devices, cloud services |
| **Vulnerability**  | Weakness Exploited | A flaw or gap in the system that the threat exploits. | Unpatched software, weak passwords, misconfigured servers, zero-day exploits |
| **Impact** | Consequence | The damage or effect caused by the threat if successful. | Data theft, service disruption, financial loss, reputational damage |
| **Capability** | Sophistication Level | The skill level, resources, and tools the attacker uses. | Script kiddies with off-the-shelf tools, advanced persistent threats (APTs) |
| **Frequency** | Occurrence Rate | How often the threat or similar attacks are observed. | Rare targeted attacks, common phishing campaigns |
| **Detection** | Identifiability | How easily the threat or attack can be detected. | Known malware signatures, anomalous network behavior, zero-day stealth attacks |
| **Mitigation** | Defense Measures | Techniques or controls to prevent, detect, or respond to the threat. | Firewalls, intrusion detection systems (IDS), employee training, patch management |

## Vulnerability  Space


| **Category** | **Type** | **Description** |
| --- | --- | --- |
| **Software Vulnerabilities** | Buffer Overflow | Overrunning memory bounds leading to arbitrary code execution |
|  | SQL Injection | Malicious SQL code injection through input fields |
|  | Cross-Site Scripting (XSS) | Injection of malicious scripts into web pages |
|  | Race Conditions | Timing issues causing unexpected behavior |
|  | Privilege Escalation | Bugs allowing elevation of user permissions |
|  | Unpatched Software | Known flaws not fixed by updates |
| **Configuration Vulnerabilities** | Default Credentials | Using out-of-the-box passwords or settings |
|  | Open Ports | Network ports unnecessarily exposed |
|  | Misconfigured Firewalls | Weak or incorrect firewall rules |
|  | Insecure Permissions | Excessive access rights on files or services |
|  | Disabled Security Features | Features like SELinux or antivirus turned off |
| **Human Vulnerabilities** | Social Engineering Susceptibility | Phishing, pretexting, baiting targeting users |
|  | Poor Password Practices | Weak or reused passwords |
|  | Lack of Security Awareness | Ignorance about cyber hygiene |
| **Hardware Vulnerabilities** | Side-Channel Attacks | Leaking info via timing, power, or electromagnetic channels |
|  | Firmware Bugs | Vulnerabilities in device firmware |
|  | Physical Access Weaknesses | Poor physical security allowing tampering |
| **Network Vulnerabilities** | Insecure Protocols | Use of outdated/unencrypted protocols (e.g., Telnet, FTP) |
|  | Man-in-the-Middle (MITM) Weaknesses | Lack of proper encryption or authentication |
|  | DNS Spoofing | Manipulating DNS responses to redirect traffic |
| **Zero-day Vulnerabilities** | Unknown Flaws | Previously undisclosed bugs with no available patches |

## Defense Space


## Cybersecurity Framework

> A **cybersecurity framework** is a **structured set of guidelines, best practices, standards, and processes** designed to help organizations **identify, manage, reduce, and respond to cybersecurity risks**.

| **Framework** | **Publisher** | **Use Case** |
| --- | --- | --- |
| **NIST CSF** | NIST (US) | Broad, risk-based approach for public and private sectors |
| **ISO/IEC 27001** | ISO | International standard for Information Security Management Systems (ISMS) |
| **CIS Controls** | Center for Internet Security | Prioritized set of cybersecurity best practices |
| **COBIT** | ISACA | Governance and management of enterprise IT |
| **MITRE ATT&CK** | MITRE | Threat modeling and defense based on real-world adversary behavior |
| **NIST SP 800-53** | NIST | Detailed control catalog for U.S. federal systems |

## References

- [Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- https://github.com/sbilly/awesome-security
- https://owasp.org/www-community/attacks/
- https://en.wikipedia.org/wiki/List_of_cyberattacks
- https://owasp.org/www-project-top-ten/
- [Unicode characters to Bypass Security Checks](https://sim4n6.beehiiv.com/p/unicode-characters-bypass-security-checks)
- [An Alternative Way of Using MITRE ATT&CK® for Threat Hunting and Detection](https://posts.bluraven.io/an-alternative-way-of-using-mitre-att-ck-for-threat-hunting-and-detection-be55739dc7aa)
