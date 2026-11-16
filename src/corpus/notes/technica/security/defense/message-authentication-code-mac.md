---
tags: [note, security, defense, cryptographic]
---

# Message Authentication Code (MAC)

> Related: [Cryptography System](/view.html?p=notes/technica/security/defense/cryptography-system.md), [JSON Web Token (JWT)](/view.html?p=notes/technica/security/defense/json-web-token-jwt.md)

> A **Message Authentication Code (MAC)** is a **cryptographic primitive** used to verify the **integrity and authenticity** of a message. It ensures that the message has not been altered and that it comes from a legitimate sender who shares a secret key.

> A **Message Authentication Code (MAC)** is a **short, fixed-size cryptographic value** generated from a **message and a secret key**.

> This is a core cryptographic primitive; it does not include **key management** or any **key exchange** protocols.

## Formulation

A **Message Authentication Code (MAC)** is a **short, fixed-size cryptographic value** generated from a **message and a secret key**. It is used to:

1. **Verify integrity** – ensuring the message has not been altered during transmission.
2. **Authenticate the sender** – confirming that the message comes from someone who knows the shared secret key.

## Property

- **Keyed**: Requires a secret key shared between sender and receiver.
- **Deterministic**: The same message and key always produce the same MAC.
- **Collision-resistant**: It is computationally infeasible to find two different messages with the same MAC.

## Workflow

- Sender computes `MAC = MAC_function(secret_key, message)`
- Sender sends the message along with the MAC
- Receiver computes `MAC' = MAC_function(secret_key, message)` and checks if `MAC' == MAC`
    - If yes → message is authentic and unaltered
    - If no → message has been tampered with or key is incorrec

## Algorithm

> Which are the mac functions?

| **Algorithm** | **Type** | **Description** | **Notes** |
| --- | --- | --- | --- |
| **HMAC** | Hash-based MAC | Uses a cryptographic hash function (e.g., SHA-256) combined with a secret key to produce a MAC | Widely used, strong security, simple |
| **CMAC** | Block cipher MAC | Uses a block cipher (e.g., AES) to generate a MAC | Recommended when a block cipher is preferred |
| **PMAC** | Parallel MAC | Parallelizable MAC based on block ciphers | Efficient on parallel hardware |
| **UMAC** | Universal MAC | Uses universal hashing and a cryptographic hash | Designed for very high performance |
| **VMAC** | Universal MAC | Similar to UMAC, optimized for 64-bit platforms | High speed with strong security |
| **GMAC** | Galois MAC | Uses Galois field multiplication, based on AES-GCM | Used in authenticated encryption |

## History

> Which is the History of the idea of MAC?

| **Year** | **Event** | **Description** |
| --- | --- | --- |
| 1979 | **Carter-Wegman MAC** | First formal MAC construction proposed using universal hashing for message authentication. |
| 1980s | **Early symmetric MACs** | Researchers explored block cipher-based MACs (e.g., using DES as a building block). |
| 1988 | **HMAC introduced** | Keyed-Hash MAC (HMAC) concept developed; uses a cryptographic hash (MD5, SHA-1) with a secret key; later standardized in RFC 2104 (1997). |
| 1990s | **CBC-MAC** | MACs based on block cipher chaining modes (like CBC) widely analyzed and applied; used in early TLS/SSL versions. |
| 2001 | **HMAC-SHA1 standardized** | HMAC construction with SHA-1 hash becomes standard for secure communications (RFC 2104, updated for SHA-1/SHA-256). |
| 2004–2010 | **AEAD MACs** | Authenticated Encryption with Associated Data (AEAD) schemes like AES-GCM introduced; combine encryption and MAC for efficiency and security. |
| 2018 | **Modern TLS 1.3** | AEAD constructions (AES-GCM, ChaCha20-Poly1305) replace traditional MAC+encryption combination for better security and performance. |

## References

- [HMAC](https://en.wikipedia.org/wiki/HMAC)
- [MAC](https://en.wikipedia.org/wiki/Message_authentication_code)
