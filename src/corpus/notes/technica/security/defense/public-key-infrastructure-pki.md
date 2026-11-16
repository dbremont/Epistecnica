---
tags: [note, security, defense, cryptographic]
---

# Public Key Infrastructure (PKI)

> Related: [Cryptography System](/view.html?p=notes/technica/security/defense/cryptography-system.md), [Digital Signature](/view.html?p=notes/technica/security/defense/digital-signature.md), [Digital Certificate](/view.html?p=notes/technica/security/defense/digital-certificate.md)

> PKI is a **hierarchical framework** of roles, policies, and procedures that enables secure communication through **public-key cryptography**, particularly for **authentication**, **integrity**, and **encryption**.

> **Public Key Infrastructure (PKI):**  Manages creating, distributing, and revoking digital certificates to secure communication.

> **Key Exchange Protocols:** Facilitates the secure exchange of cryptographic keys between parties.

## Role

| **Function** | **Description** |
| --- | --- |
| **Authentication** | It is ensuring that a message, transaction, or other data exchange is truly from the sender (not an imposter). |
| **Confidentiality** | It is ensuring that only the intended recipient(s) can access the contents of the data transmitted. |
| **Data Integrity** | It is ensuring that the data has not been altered from its original form during transmission or storage. |
| **Non-Repudiation** | Providing proof of the origin and integrity of data, which can be verified by a third party to prove that a sender cannot deny the authenticity of their signature on a message. |

## 🔐 Structure

> Which are the components of the security system?

| **Component** | **Role** |
| --- | --- |
| **Certificate Authority (CA)** | The trusted entity that issues and digitally signs **digital certificates**. |
| **Registration Authority (RA)** | Verifies the identity of users or entities **before** certificates are issued. |
| **Digital Certificate** | A data file that binds a public key to an identity (person, server, etc.) using the CA’s digital signature. |
| **Public & Private Keys** | A **key pair**: the public key is distributed via **certificates**, and the private key is kept secret. |
| **Certificate Revocation List (CRL)** | A published list of certificates that are no longer valid before their expiration. |
| **Online Certificate Status Protocol (OCSP)** | A real-time protocol for checking if a certificate is still valid. |
| **Certificate Repository** | A server or database where certificates and CRLs are stored and made available. |
| **End Entities** | The users, servers, or devices that request, receive, and use digital certificates. |

## 🏗 Model

```bash
          Root CA
             |
         Intermediate CA(s)
             |
     ------------------------
     |                      |
   Server A            Server B
   User X              User Y
```

## **📋 Workflow**

> Which are the workflow - that the PKI System handles?

| **Process** | **Description** |
| --- | --- |
| **Certificate Enrollment** | Requesting and verifying identity for issuing a certificate. |
| **Key Generation** | Creation of public/private key pairs (often by the end entity). |
| **Certificate Issuance** | CA signs the certificate after RA approval. |
| **Certificate Revocation** | Revoking a certificate before it expires due to compromise, etc. |
| **Validation** | Ensuring the certificate is authentic and hasn’t been revoked. |

### **Validation**

> How a Certificate is validated?

> See [https://datatracker.ietf.org/wg/pkix/about/](https://datatracker.ietf.org/wg/pkix/about/);

> Certificates are validated through a **chain of trust**, starting from the certificate you want to validate (the end-entity or leaf certificate) up to a trusted root certificate.

> Certificates don’t validate themselves. Every validation step is **performed by the accessing software**, based on the information in the certificate and the software’s trust configuration.

A certificate is a digital document that binds a public key to an entity (person, server, organization). Validation ensures:

- **Check the certificate signature:**
    - Each certificate in the chain is signed by its issuer (the next certificate up).
    - The system verifies the signature using the issuer’s public key.
- **Build the certificate chain:**
    - The validator collects the chain: Leaf → Intermediate(s) → Root.
    - It stops at a **trusted root CA** in the trust store (e.g., `cacerts` in Java).
- **Check issuer validity:**
    - Each certificate must be issued by the next certificate in the chain.
    - The root must be explicitly trusted.

Software: **Validation software** is any program, library, or subsystem that checks whether a digital certificate can be trusted before establishing a secure connection or performing a cryptographic operation.

- openssl verify
- PKI libraries (BouncyCastle, NSS, wolfSSL, etc.)
- Chrome, Firefox, Safari SSL/TLS stack

## Chain of Trust

A **Chain of Trust** is a hierarchical sequence of trusted entities (usually digital certificates or signing authorities) where each entity vouches for the authenticity and integrity of the next. In practice, it ensures that a system, software, or communication component can be trusted because it originates from a source that is ultimately validated by a root authority.

**Key Points:**

1. **Root of Trust:** The starting point, typically a highly secure and trusted certificate or hardware module.
2. **Intermediate Entities:** Optional layers that extend trust from the root to other entities.
3. **Leaf Entity:** The end component being verified (e.g., a website certificate or software binary).
4. **Verification Process:** Each certificate or signature is checked against the one above it in the chain. If any link is invalid or compromised, the chain of trust breaks, and the system does not trust the entity.

## Configuration

## Linux

> How to interact with the PKI System?
- `/etc/ca-certificates.conf`*: A configuration file.
- `/etc/ssl/certs/ca-certificates.crt`: A single-file version of CA certificates. This holds all CA certificates that you activated in /etc/ca-certificates.conf.
- `/usr/share/ca-certificates`: Directory of CA certificates.
- `/usr/local/share/ca-certificates`: Directory of local CA certificates (with .crt extension).

### Java

> How to configure PKI - Java Interaction?

> See more in .

### Utilities

> This structured presentation not only describes the integral parts and functions of PKI but also illustrates how these are utilized or can be managed on Linux systems, leveraging commonly used tools and applications that support PKI operations. This setup exemplifies a robust framework for managing identity and security in various networked and local applications on Linux.

| **Tool/Framework** | **Function** | **Details** |
| --- | --- | --- |
| **OpenSSL** | Toolkit for SSL/TLS protocols and general cryptographic library. | They are used for creating and managing certificates, keys, and more. |
| **EasyRSA** | Command line utility for building and managing a PKI CA. | Simplified wrapper around OpenSSL for managing CA operations. |
| **GnuPG** | Implements the OpenPGP standard for encrypting and signing data and communications. | They are widely used for email encryption and code signing. |
| **Certbot** | Automatically uses Let’s Encrypt to issue and renew certificates and can configure web servers to use these. | Famous in web environments for managing SSL/TLS certificates. |

## Testing

| Category | URL | Note |
| --- | --- | --- |
| 🔴 Invalid/ Broken | [https://expired.badssl.com/](https://expired.badssl.com/) | Certificate is **expired** |
| 🔴 Invalid/ Broken | [https://self-signed.badssl.com/](https://self-signed.badssl.com/) | Certificate is **self-signed** |
| 🔴 Invalid/ Broken | [https://wrong.host.badssl.com/](https://wrong.host.badssl.com/) | Certificate’s **CN/SAN does not match** hostname |
| 🔴 Invalid/ Broken | [https://untrusted-root.badssl.com/](https://untrusted-root.badssl.com/) | Signed by an **untrusted CA** |
| 🟢 Valid | [https://sha256.badssl.com/](https://sha256.badssl.com/) | Uses **SHA-256**, valid cert |
| 🟢 Valid | [https://www.google.com/](https://www.google.com/) | **Normal trusted certificate** |

## QA

### How to check a certificate?

> `openssl s_client -connect [cdn.hacienda.gob.do:443](http://cdn.hacienda.gob.do:443/) -servername [cdn.hacienda.gob.do](http://cdn.hacienda.gob.do/) -showcerts`

### How to check the CA Authority?

> `openssl s_client -connect [cdn.hacienda.gob.do:443](http://cdn.hacienda.gob.do:443/) -servername [cdn.hacienda.gob.do](http://cdn.hacienda.gob.do/) | openssl x509 -noout -issuer -subject`

- [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/)
- [https://crt.sh/](https://crt.sh/)

### How to check if CA Authority is in the Java Trust Store?

> It’s varies for version but for 1.8 is $JAVA_HOME/jre/lib/security/cacerts.

> `keytool -list -keystore $JAVA_HOME/jre/lib/security/cacerts -storepass changeit`, `change it` it’s the default password.

> Note:  Note - Java does not used the OS - for Certificate Validation.

### How to download the CA Authority?

> openssl s_client -showcerts -connect [cdn.hacienda.gob.do](https://cdn.hacienda.gob.do/):443 </dev/null 2>/dev/null | sed -n '/BEGIN CERTIFICATE/,/END CERTIFICATE/p' > chain.pem

### How to add a CA Authority to Java KeyStore?

> Download the certificate (PEM) Form.

> Add to Keystore: `keytool -import -trustcacerts -alias CloudFlare-CA -file CloudFlare.pem -keystore $JAVA_HOME/jre/lib/security/cacerts` `-storepass changeit`

> Verify:  `keytool -import -trustcacerts -alias CloudFlare-CA -file CloudFlare.pem -keystore` $JAVA_HOME/../8.0.372-zulu/jre/lib/security/cacerts `-storepass changeit`

### Where is the TSL/SSL implemented?

TLS/SSL is a **protocol** for secure communication over a network. It is not implemented in one single place; it spans multiple layers:

- **Library level**: Most programming languages use cryptographic libraries that implement TLS/SSL. For example:
    - **OpenSSL** (C/C++)
    - **BoringSSL** / **LibreSSL**
    - **Windows SChannel** (Windows API)
    - **Java’s JSSE** (Java Secure Socket Extension)
- **Application level**: Web servers or clients invoke these libraries:
    - **Apache HTTP Server** uses OpenSSL to handle HTTPS connections.
    - **Browsers** use their own TLS stacks (e.g., Mozilla uses NSS).
- **Operating System level**: Sometimes TLS is offloaded to OS libraries for certificates, encryption, or networking integration.

## References

- https://en.wikipedia.org/wiki/Public_key_infrastructure
- Transport Layer Security (TLS)
- A Guide to Implementing a Let’s Encrypt Certificate
- https://blog.brycekerley.net/2026/03/08/webpki-and-you.html
