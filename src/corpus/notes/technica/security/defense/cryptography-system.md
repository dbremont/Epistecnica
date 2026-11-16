---
tags: [note, security, defense, cryptographic]
---

# Cryptography System

> Related: [Public Key Infrastructure (PKI)](/view.html?p=notes/technica/security/defense/public-key-infrastructure-pki.md), [Digital Signature](/view.html?p=notes/technica/security/defense/digital-signature.md), [Cryptography Hash Function](/view.html?p=notes/technica/security/defense/cryptography-hash-function.md), [Message Authentication Code (MAC)](/view.html?p=notes/technica/security/defense/message-authentication-code-mac.md), [Digital Certificate](/view.html?p=notes/technica/security/defense/digital-certificate.md), [Cryptography](/view.html?p=notes/technica/security/defense/cryptography.md)

> A **cryptography system** is the practical implementation of cryptographic techniques to secure information and communication.

> Cryptography involves securing communication and data through the use of mathematical techniques and algorithms.

## 🛡️ **Goals of a Cryptosystem**

- **Confidentiality**: Prevent unauthorized access to information.
- **Integrity**: Ensure data is not altered.
- **Authentication**: Verify the identity of sender/receiver.
- **Non-repudiation**: Ensure that actions or messages cannot be denied later.

| **System / Technique** | **Confidentiality** | **Integrity** | **Authentication** | **Non-repudiation** | **Notes** |
| --- | --- | --- | --- | --- | --- |
| Symmetric Encryption (AES, etc.) | ✅ | Limited* | Limited* | ❌ | Protects data confidentiality; integrity/auth usually via MAC or other means. |
| Asymmetric Encryption (RSA, ECC) | ✅ | Limited* | Yes (key-based) | Limited* | Provides confidentiality and authentication via key pairs. |
| Hash Functions (SHA-256, etc.) | ❌ | ✅ | ❌ | ❌ | Provide data integrity verification only. |
| Message Authentication Codes (MACs) | ❌ | ✅ | ✅ (shared key) | ❌ | Verify integrity and authentication in symmetric key systems. |
| Digital Signatures (RSA, ECDSA) | ❌ | ✅ | ✅ | ✅ | Provide authentication, integrity, and non-repudiation. |
| Public Key Infrastructure (PKI) | ❌ | ❌ | ✅ | ✅ | Supports authentication and non-repudiation by managing certificates. |
| Transport Layer Security (TLS/SSL) | ✅ | ✅ | ✅ | Limited* | Provides confidentiality, integrity, and authentication for network comms. |
| Zero-Knowledge Proofs | ❌ | ❌ | ✅ | Limited* | Proves knowledge without revealing it; authentication/privacy-focused. |
| Secret Sharing Schemes | ❌ | ✅ (if designed) | ❌ | ❌ | Securely splits secrets; supports confidentiality and integrity of secrets. |
| Timestamping Services | ❌ | ✅ | Limited* | ✅ | Proves existence and integrity at a time; supports non-repudiation. |

## Characterization

> A cryptographic model can be characterized by several key attributes that define its functionality, security, and usage.

> Cryptographic algorithms, keys, and protocols.
- **Purpose**: A cryptographic system is designed to achieve specific security goals, such as confidentiality, integrity, authenticity, and non-repudiation. The purpose of the system determines the cryptographic algorithms, keys, and protocols used to meet those goals.
- **Key Management**: Cryptographic systems require secure key management to generate, store, distribute, and revoke cryptographic keys. Proper key management is crucial for maintaining the security of the system.
- **Key Exchange Protocols**: In asymmetric cryptography, the system requires secure protocols for key exchange and management, such as Diffie-Hellman key exchange or RSA key generation.
- **Certification**: The cryptographic system’s security may depend on the trustworthiness of cryptographic modules and algorithms used. Certifications and compliance with industry standards can enhance trust in the system.

## 📦 **Components of a Cryptography System**

| **Component** | **Description** |
| --- | --- |
| **Plaintext (P)** | The original, readable message or data. |
| **Ciphertext (C)** | The encrypted, unreadable form of the plaintext. |
| **Encryption Algorithm (E)** | The algorithm that transforms plaintext into ciphertext using a key. |
| **Decryption Algorithm (D)** | The algorithm that transforms ciphertext back into plaintext using a key. |
| **Key(s) (K)** | The secret(s) used by the algorithms — may be the same (symmetric) or different (asymmetric). |
| **Key Generation Algorithm** | Procedure to produce cryptographic keys securely. |
| **Protocol (optional)** | Rules governing how the system is used (e.g., key exchange, digital signatures). |

## Case Study

| **Cryptosystem** | **Type** | **Purpose** |
| --- | --- | --- |
| **AES** (Advanced Encryption Standard) | Symmetric | Fast, secure encryption of data. |
| **RSA** | Asymmetric | Public-key encryption and signatures. |
| **ECC** (Elliptic Curve Cryptography) | Asymmetric | Encryption, key exchange, signatures. |
| **PGP** (Pretty Good Privacy) | Hybrid | Email encryption and authentication. |
| One-time Pad (OTP) | … | … |
| Threshold Cryptography |  |  |

## Cryptography Design Primitives

| **Category** | **Primitive** | **Description** | **Used To Construct** |
| --- | --- | --- | --- |
| **One-Way Functions** | One-Way Function (OWF) | Easy to compute, hard to invert. | Hash functions, commitments |
|  | Trapdoor One-Way Function | A OWF with a secret “trapdoor” enabling inversion. | Public-key encryption, digital signatures |
| **Randomness & Entropy** | Entropy Source / RNG | Provides randomness, ideally from physical noise or a secure PRNG. | Key generation, nonces, IVs |
|  | Pseudorandom Generator (PRG) | Expands short seed into long pseudorandom output. | Stream ciphers, key material |
|  | Pseudorandom Function (PRF) | Keyed function indistinguishable from random. | MACs, encryption schemes, KDFs |
|  | Pseudorandom Permutation (PRP) | A bijective PRF (e.g., AES). | Block ciphers |
| **Hashing & Compression** | Collision-Resistant Hash Function | Hash where it is hard to find two inputs with the same output. | Digital signatures, integrity, commitment schemes |
|  | Keyed Hash Function | Hash that uses a key (e.g., HMAC construction). | MACs, PRFs |
|  | Salting Function | Adds random data to input before hashing to prevent precomputation. | Secure password storage |
|  | Padding Scheme | Adds structured bits to data to match algorithm block size or encoding requirements. | Block ciphers, RSA |
| **Key & Session Derivation** | Key Derivation Function (KDF) | Derives one or more cryptographic keys from input (e.g., shared secret). | Session key generation, password hashing |
|  | Initialization Vector Generator | Ensures uniqueness/randomness for block cipher encryption. | CBC/CTR encryption modes |
| **Algebraic Structures** | Homomorphic Mapping | Preserves operations (e.g., addition, multiplication) over encrypted values. | Homomorphic encryption |
| **Knowledge Proofs** | Zero-Knowledge Proof Primitive | Allows a prover to prove knowledge of a secret without revealing the secret. | Authentication, privacy-preserving computation |
| **Secret Distribution** | Secret Sharing Scheme | Splits a secret into multiple shares, reconstructable with a threshold. | Threshold cryptography, backup schemes |
| **Idealized Models** | Random Oracle (idealized) | A theoretical black-box function behaving like a true random function. | Used in provable security and heuristic constructions |
| **Hardness Assumptions** | Hard Problem Assumption | Underlying assumption of computational hardness (e.g., factoring, elliptic curve discrete log). | RSA, DH, ECC, lattice-based crypto |

## References

- [Cryptosystem](https://en.wikipedia.org/wiki/Cryptosystem)
- [List of cryptosystems](https://en.wikipedia.org/wiki/List_of_cryptosystems)
- [Cryptographic primitive](https://en.wikipedia.org/wiki/Cryptographic_primitive)
- [Zero-knowledge Proof](https://en.wikipedia.org/wiki/Zero-knowledge_proof)
- [Cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
- [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [AES vs RSA - Which is stronger given two scenarios?](https://crypto.stackexchange.com/questions/47991/aes-vs-rsa-which-is-stronger-given-two-scenarios)
