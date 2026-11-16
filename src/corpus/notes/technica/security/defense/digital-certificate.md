---
tags: [note, security, defense, cryptographic]
---

# Digital Certificate

> Related: [Cryptography System](/view.html?p=notes/technica/security/defense/cryptography-system.md), [Public Key Infrastructure (PKI)](/view.html?p=notes/technica/security/defense/public-key-infrastructure-pki.md), [Cryptographic Data](/view.html?p=notes/technica/security/defense/cryptographic-data.md)

> A **Digital Certificate** is a **digital document** used to prove the **ownership of a public key**. It is issued by a **Certificate Authority (CA)** and serves as a critical component of **Public Key Infrastructure (PKI)**.

## Taxonomy

| **Certificate Type** | **Description** | **Key Features** | **Common Use Cases** |
| --- | --- | --- | --- |
| **X.509 Certificate** | The most widely used digital certificate standard for public key infrastructure (PKI). | Public key, subject identity, issuer, validity period, digital signature from CA | SSL/TLS for websites, email encryption, code signing |
| **SSL/TLS Certificate** | Digital certificate that enables SSL/TLS encryption on websites and servers. | Contains domain name, public key, issued by trusted CA, expiration date | HTTPS secure websites, server authentication |
| **Code Signing Certificate** | Used by software developers to digitally sign executables and scripts to verify authenticity. | Binds software publisher identity to the signed code, prevents tampering | Software distribution, driver signing |
| **Client Certificate** | Used to authenticate a client/user to a server in mutual TLS or secure systems. | Contains user identity and public key, issued by CA or internal authority | VPN authentication, enterprise systems access |
| **Email Certificate (S/MIME)** | Enables secure email through encryption and digital signing of email messages. | Contains user identity, public key, CA signature, used with email clients supporting S/MIME | Email confidentiality and authenticity |
| **Wildcard Certificate** | SSL/TLS certificate that secures a domain and all its subdomains with a single certificate. | Uses wildcard character (*) in domain name, same security features as regular SSL certs | Securing multiple subdomains efficiently |
| **Self-Signed Certificate** | A certificate signed by the entity creating it rather than a trusted CA. | Provides encryption but not trusted by browsers by default, useful for internal or testing | Development, internal networks, testing environments |

## References

- https://en.wikipedia.org/wiki/Public_key_certificate
- [X.509](/view.html?p=notes/technica/security/defense/x509.md)
- A Guide to Implementing a Let’s Encrypt Certificate
