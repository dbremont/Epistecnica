---
tags: [note, security]
order: 0
---

# Security

> Let’s learn how to control interaction - and keep the interaction - in an space of (…) - while inform by the attacker capabilities.
> 

> NOTE: PAY HUGE ATTENTION TO SECURITY; SEEMS THE COMODITIZATION OF ATTACKS, AND DEFENSE - DEFEND THE OPERATIONAL OF COMPUTATIONAL SYSTEMS - MUST TAKE PRIORITY - EVEN OVER CAPABILITY EVOLUTION OF THEM.
> 

## The two sides

Security is the control of interaction in a technical ecosystem: the set of interfaces, identities and trust relations that an attacker can reach, met by the set of mechanisms that keep that reach from becoming a compromise. The shelf is cut along that line.

| Side | What it carries | Note |
| --- | --- | --- |
| **Attack** | The offensive reading: what the attacker can reach (the attack surface), what a reached weakness buys (a buffer overflow, for one), and how the reach is used | [Attack](/view.html?p=notes/technica/security/attack.md) |
| **Defense** | The defensive reading: identity, authorization, cryptography and its systems, the standards built on them (X.509, PKI, JWT, OAuth), and the controls — threat modelling, zero trust, secure multi-party computation | [Defense](/view.html?p=notes/technica/security/defense.md) |

## What is in the shelf

| Note | What it carries |
| --- | --- |
| [Attack](/view.html?p=notes/technica/security/attack.md) | The attack-surface inventory — network, web, identity, software, data, cloud, infrastructure, hardware, physical, supply chain, trust, human — and the attacks that enter through it |
| [Buffer Overflow](/view.html?p=notes/technica/security/attack/buffer-overflow.md) | The classic memory-safety failure and the capabilities it enables, from code execution to sandbox escape |
| [Defense](/view.html?p=notes/technica/security/defense.md) | The defense domain: its problem space, task space, product space and technique space, stated in the technical shell |
| [Identity Model](/view.html?p=notes/technica/security/defense/identity-model.md) · [Permission Model](/view.html?p=notes/technica/security/defense/permission-model.md) | Who the agent is, and what it may do — with authorization schemes, passwords and one-time passwords under the permission model |
| [Cryptography](/view.html?p=notes/technica/security/defense/cryptography.md) · [Cryptography System](/view.html?p=notes/technica/security/defense/cryptography-system.md) · [Cryptographic Data](/view.html?p=notes/technica/security/defense/cryptographic-data.md) | The primitives, the system they compose into, and the data they protect |
| [Cryptography Hash Function](/view.html?p=notes/technica/security/defense/cryptography-hash-function.md) · [Digital Signature](/view.html?p=notes/technica/security/defense/digital-signature.md) · [Message Authentication Code (MAC)](/view.html?p=notes/technica/security/defense/message-authentication-code-mac.md) | Integrity and authenticity, by key or by hash |
| [X.509](/view.html?p=notes/technica/security/defense/x509.md) · [Digital Certificate](/view.html?p=notes/technica/security/defense/digital-certificate.md) · [Public Key Infrastructure (PKI)](/view.html?p=notes/technica/security/defense/public-key-infrastructure-pki.md) | The certificate standard, the certificate, and the machinery that issues and trusts them |
| [JSON Web Key (JWK)](/view.html?p=notes/technica/security/defense/json-web-key-jwk.md) · [JSON Web Signature (JWS)](/view.html?p=notes/technica/security/defense/json-web-signature-jws.md) · [JSON Web Token (JWT)](/view.html?p=notes/technica/security/defense/json-web-token-jwt.md) | The web's own token format and the two notes it is built from |
| [OAuth](/view.html?p=notes/technica/security/defense/oauth.md) · [OpenID](/view.html?p=notes/technica/security/defense/openid.md) · [Passkey](/view.html?p=notes/technica/security/defense/passkey.md) | Delegated authorization, federated identity, and the credential that replaces the password |
| [Threat Model](/view.html?p=notes/technica/security/defense/threat-model.md) · [Zero Trust System](/view.html?p=notes/technica/security/defense/zero-trust-system.md) · [Audit Log Model](/view.html?p=notes/technica/security/defense/audit-log-model.md) | What can go wrong, the architecture that assumes it will, and the record that makes it visible |
| [Malware](/view.html?p=notes/technica/security/defense/malware.md) · [Phishing](/view.html?p=notes/technica/security/defense/phishing.md) | The two attacks that go through the user rather than the interface |
| [Secure Multi-Party Computation](/view.html?p=notes/technica/security/defense/secure-multi-party-computation.md) | Computing on data that no party is allowed to see |

## Neighbours

The security notes that live with the objects they secure, rather than here — a chip, a language, an operating system, a protocol — stay where they are and are reachable from this page:

- [Computational System Security](/view.html?p=notes/technica/computation/system/design/computational-system-security.md) — security as a property of the system under design
- [X86 Security](/view.html?p=notes/technica/computation/language-system/x86-isa/x86-security.md) — the hardware's own boundaries
- [Java Security Model](/view.html?p=notes/technica/computation/language-system/java/java-miscelanea/java-miscelanea/java-security-model.md) — the language runtime's sandbox and its history
- [Linux Security Stack](/view.html?p=notes/technica/computation/operating-system/linux/linux-security-stack.md) — the operating system's layers of enforcement
- [Transport Layer Security (TLS)](/view.html?p=notes/technica/computation/telecom/transport-layer-security-tls.md) — the channel
- [Certificate Management](/view.html?p=notes/technica/computation/system/operation/certificate-management.md) — the operational life of a certificate
- [Git Security](/view.html?p=notes/technica/computation/system/operation/git-global-information-tracker/git-security.md) — the supply chain's own history
- [SSH (Secure Shell)](/view.html?p=notes/technica/general/ssh/ssh-secure-shell.md) — remote access, secured

## References

- https://arxiv.org/abs/2604.20801
- https://github.com/berabuddies/Semia
- [https://huggingface.co/spaces/zai-org/OpenVuln](https://huggingface.co/spaces/zai-org/OpenVuln)
- [GLM-5.3: Frontier Coding with Emergent Cyber Capabilities](https://z.ai/blog/glm-5.3)
- [https://cvd.z.ai/ledger/](https://cvd.z.ai/ledger/)
- [Attack](/view.html?p=notes/technica/security/attack.md) · [Defense](/view.html?p=notes/technica/security/defense.md) — the two sides of this shelf
