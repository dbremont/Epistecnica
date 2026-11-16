---
tags: [note, security, defense, cryptographic]
---

# JSON Web Signature (JWS)

> Related: [JSON Web Token (JWT)](/view.html?p=notes/technica/security/defense/json-web-token-jwt.md)

> **JWS** is a compact and URL-safe format for representing digitally signed data using **JSON objects**. It is defined in RFC 7515 and is one of the core components of the **JOSE** (JSON Object Signing and Encryption) framework.

## Structure

| **Component** | **Content** | **Purpose** |
| --- | --- | --- |
| **Header** | `{"alg": "RS256", "typ": "JWT"}` | Specifies the signing algorithm and token type |
| **Payload** | `{"sub": "1234567890", "name": "Joe", ...}` | The actual content being signed |
| **Signature** | `Signature = Sign(EncodedHeader + "." + EncodedPayload, PrivateKey)` | Ensures integrity and authenticity |

## Signing Algorithms (`alg`)

| **Algorithm** | **Type** | **Description** |
| --- | --- | --- |
| `HS256` | HMAC with SHA-256 | Symmetric signing |
| `RS256` | RSA SHA-256 | Asymmetric with public/private key |
| `ES256` | ECDSA using P-256 | Compact ECC-based signature |
| `EdDSA` | Edwards-curve Ed25519 | Modern, fast, secure |

## 📑 JWS Serialization Modes

| **Mode** | **Format** | **Use Case** |
| --- | --- | --- |
| **Compact** | Single string with 3 parts | JWT tokens, web APIs |
| **JSON Serialization** | Structured JSON object | Multiple signers, clear separation |
| **Flattened JSON** | JSON with single signature | Simpler to parse in structured data |

## ✅ Use Cases

- **Authentication**: JWS is used inside JWT (JSON Web Token) for identity assertions.
- **API Authorization**: Signed tokens (e.g., OAuth 2.0 bearer tokens).
- **Data Integrity**: Ensures transmitted payloads haven't been tampered with.
- **Decentralized Identity**: Used in DID and Verifiable Credentials systems.

## References

- https://en.wikipedia.org/wiki/JSON_Web_Signature
