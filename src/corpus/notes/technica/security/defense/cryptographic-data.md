---
tags: [note, security, defense, representation]
---

# Cryptographic Data

> Related: [JSON Web Token (JWT)](/view.html?p=notes/technica/security/defense/json-web-token-jwt.md), [JSON Web Key (JWK)](/view.html?p=notes/technica/security/defense/json-web-key-jwk.md), [X.509](/view.html?p=notes/technica/security/defense/x509.md), [Digital Certificate](/view.html?p=notes/technica/security/defense/digital-certificate.md)

> **Domain**: "Cryptographic data" refers to information that has been encoded using cryptographic algorithms to ensure its confidentiality, integrity, and authenticity.

## Digital Certificate

> Which are the formats? Which are the different encodings - of such formats?

> A **digital certificate** is a **cryptographically signed data structure** that binds a **public key** to an **entity’s identity or attributes**. It serves as a digital credential, allowing others to verify that a given public key legitimately belongs to the claimed subject.

| **Certificate Format** | **Description** | **Use** | **Encoding(s)** |
| --- | --- | --- | --- |
| **X.509** | Standard for public key certificates defined by ITU-T. Uses ASN.1 structure with extensions (v3). Relies on hierarchical Certificate Authorities. | TLS/SSL (HTTPS), VPNs, email (S/MIME), code signing, PKI systems. | DER (binary), PEM (Base64+headers), PKCS#12 (.pfx/.p12 for cert+key), PKCS#7 (.p7b for chains). |
| **OpenPGP** | Certificates bind user IDs (e.g., name/email) to public keys. Trust model is a decentralized “Web of Trust.” | Email encryption/signing, file/package signing (e.g., Debian, Git), secure messaging. | ASCII-armored text (`-----BEGIN PGP PUBLIC KEY BLOCK-----`), binary packet format. |
| **SPKI (Simple Public Key Infrastructure)** | Experimental MIT format focusing on authorization rather than identity. Allows delegation of rights directly. | Academic/research, some distributed authorization systems. Rare in production. | ASN.1/DER, S-expressions. |
| **WebAuthn (FIDO2)** | Modern authentication credential format. Stores public keys and attestation data in authenticators (hardware or platform). | Passwordless login, 2FA, hardware security keys (YubiKey, Titan). | CBOR (binary JSON-like encoding), sometimes JSON for APIs. |
| **SSH Keys / SSH Certificates** | Keys and optional short-lived certificates binding principals to keys. Signed by an SSH CA, independent of X.509. | Secure shell login, machine-to-machine authentication. | OpenSSH text format (`ssh-rsa AAAAB3...`), proprietary binary (RFC 4253), OpenSSH certs (`ssh-rsa-cert-v01@openssh.com`). |
| **JWK (JSON Web Key)** | JSON-based representation of cryptographic keys. Used for web APIs, token signing, and federated identity. | OAuth2, OpenID Connect, API authentication, JWT signing. | JSON (plain), JWK Sets (JWKS via HTTPS endpoints). |
| **JWT (JSON Web Token)** | A compact, URL-safe token format containing claims about a subject. Can be signed (JWS) or encrypted (JWE). Often carries or references keys (via JWK). | Authentication and authorization in APIs, OAuth2, OpenID Connect (ID tokens, access tokens). | Base64URL-encoded JSON (`header.payload.signature`). |
| **SAML** | XML-based standard for exchanging authentication and authorization assertions between an Identity Provider (IdP) and a Service Provider (SP). Uses digital signatures (often X.509 certs) to ensure integrity. | Enterprise Single Sign-On (SSO), identity federation, B2B authentication. | XML (over HTTP POST, Redirect, SOAP bindings). |

## Digital Signature

> A **digital signature** is a **cryptographic value** that allows one to **verify the authenticity and integrity** of digital data. It ensures that a message, document, or file was **created by a known sender** and **has not been altered** since it was signed.

| **Format** | **Description** | **Commonly Used In** |
| --- | --- | --- |
| **PDF Signature (PAdES)** | Signatures embedded in PDF documents, with visible or invisible fields. | Legal documents, contracts |
| **XML Digital Signature (XMLDSig)** | W3C standard using `<Signature>` tags to sign portions of XML. | SOAP, SAML, secure XML applications |
| **JSON Web Signature (JWS)** | Component of JWT (JSON Web Token); uses Base64-URL encoded JSON for header, payload, and signature. | OAuth, OpenID Connect, API auth |
| **Signed Email (S/MIME)** | Signature embedded in MIME format using X.509 certs and PKCS#7. | Secure email (Outlook, Thunderbird) |

## References

- https://en.wikipedia.org/wiki/X.509
- https://serverfault.com/questions/9708/what-is-a-pem-file-and-how-does-it-differ-from-other-openssl-generated-key-file
- SSH
