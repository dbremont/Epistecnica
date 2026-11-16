---
tags: [note, security, defense, cryptographic]
---

# Cryptography Hash Function

> Related: [Cryptography System](/view.html?p=notes/technica/security/defense/cryptography-system.md)

> A **cryptographic hash function** is a **mathematical algorithm** that takes an input (or "message") and returns a **fixed-size string of bytes**, typically a **digest** that appears random.

QA:

- How can I determine the most suitable cryptographic hash function for my use case?

## Property

| **Property** | **Description** |
| --- | --- |
| **Deterministic** | The same input always produces the same output. |
| **Fast Computation** | The hash can be computed quickly for any given input. |
| **Pre-image Resistance** | Given a hash value *h*, it is infeasible to find any input *x* such that `hash(x) = h`. |
| **Second Pre-image Resistance** | Given input *x₁*, it is infeasible to find *x₂ ≠ x₁* such that `hash(x₁) = hash(x₂)`. |
| **Collision Resistance** | It is infeasible to find two different inputs *x₁* and *x₂* such that `hash(x₁) = hash(x₂)`. |
| **Avalanche Effect** | A small change in input causes a drastic change in output. |

## Use Cases

| **Use Case** | **Purpose** |
| --- | --- |
| **Password Hashing** | Store hashed passwords instead of plaintext. |
| **Data Integrity Checks** | Verify that data has not been altered (e.g., checksums). |
| **Digital Signatures** | Generate message digests to sign with private keys. |
| **Blockchain** | Link blocks securely using hash values. |
| **File Deduplication** | Detect identical files based on hashes. |

## Case Studies

| **Name** | **Digest Size** | **Speed** | **Security Status** | **Structure** | **Use Cases** | **Designer** |
| --- | --- | --- | --- | --- | --- | --- |
| **MD4** | 128 bits | Very fast | ❌ Broken | Merkle–Damgård | Predecessor to MD5, obsolete | Ron Rivest (1990) |
| **MD5** | 128 bits | Very fast | ❌ Broken | Merkle–Damgård | Widely deprecated, still seen in legacy systems | Ron Rivest (1991) |
| **SHA-0** | 160 bits | Fast | ❌ Broken | Merkle–Damgård | Withdrawn quickly due to flaws | NSA (1993) |
| **SHA-1** | 160 bits | Fast | ❌ Collisions found | Merkle–Damgård | Deprecated, once widely used | NSA (1995) |
| **SHA-224** | 224 bits | Medium | ✅ Secure | Merkle–Damgård | Truncated SHA-256 | NSA (SHA-2, 2001) |
| **SHA-256** | 256 bits | Medium | ✅ Secure | Merkle–Damgård | Common for blockchain, file integrity | NSA (SHA-2, 2001) |
| **SHA-384** | 384 bits | Medium | ✅ Secure | Merkle–Damgård | Uses SHA-512 internally | NSA (SHA-2, 2001) |
| **SHA-512** | 512 bits | Slower (more secure) | ✅ Secure | Merkle–Damgård | High-security applications | NSA (SHA-2, 2001) |
| **SHA-3 (Keccak)** | 224–512 bits | Moderate | ✅ Secure | Sponge construction | NIST SHA-3 winner, good for post-quantum prep | Guido Bertoni et al. (2015) |
| **BLAKE** | 224/256/384/512 bits | Fast | ✅ Secure | HAIFA | Finalist in SHA-3 competition | JP Aumasson et al. (2010) |
| **BLAKE2b** | 512 bits (variable) | ⚡ Very fast | ✅ Secure | HAIFA | Successor to BLAKE, faster than MD5/SHA | JP Aumasson et al. (2012) |
| **BLAKE2s** | 256 bits | ⚡ Very fast | ✅ Secure | HAIFA | For smaller architectures (mobile, embedded) | Same |
| **BLAKE3** | 256 bits | ⚡⚡ Extremely fast | ✅ Secure | Merkle tree + SIMD | Parallelizable, tree hashing | Jack O'Connor (2020) |
| **RIPEMD-160** | 160 bits | Fast | ⚠️ Weaker than SHA-2 | Merkle–Damgård | Used in some PGP and Bitcoin addresses | COSIC (1996) |
| **RIPEMD-256/320** | 256/320 bits | Slower | ✅ (Limited use) | Merkle–Damgård | Niche usage | COSIC |
| **Whirlpool** | 512 bits | Moderate | ✅ Secure | Miyaguchi–Preneel | ISO/IEC standard | Barreto & Rijmen (2000) |
| **Tiger** | 192 bits | Fast (64-bit CPUs) | ⚠️ Obsolete | Merkle–Damgård | Designed for fast hashing on 64-bit processors | Anderson & Biham (1995) |
| **HAVAL** | 128–256 bits | Fast | ⚠️ Legacy | Merkle–Damgård | Variable rounds and digest length | Zheng et al. (1992) |
| **Fugue** | 224–512 bits | Fast | ✅ Not widely adopted | Wide-pipe construction | SHA-3 competition entrant | IBM (SHA-3 contender) |
| **Grøstl** | 224–512 bits | Slow | ✅ Secure | Wide-pipe Merkle–Damgård | Very strong security margins | SHA-3 Finalist |
| **JH** | 224–512 bits | Fast | ✅ Secure | AES-like S-boxes | Lightweight crypto | Hongjun Wu (SHA-3 Finalist) |
| **Skein** | 256–512 bits | Fast | ✅ Secure | Unique tweakable block cipher | Flexible and configurable | Schneier et al. (SHA-3 finalist) |
| **Streebog (GOST R 34.11-2012)** | 256/512 bits | Moderate | ⚠️ Limited trust | Merkle–Damgård | Russian national hash function | Russian standard |

## References

- https://en.wikipedia.org/wiki/Cryptographic_hash_function
- https://en.wikipedia.org/wiki/Secure_Hash_Algorithms
- https://github.com/BLAKE3-team/BLAKE3
