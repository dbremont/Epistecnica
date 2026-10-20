---
tags: [technical-object]
---

# Hash Function


> A **hash function is a mechanism to perform a deterministic** many-to-one transformation from arbitrary-length input data into a fixed-size digest, enabling (efficient comparison, content identification, integrity verification, data indexing, and distribution).
> 

> A **`hash value`** **content derived tag - or content derived token**.
> 

> Note: A hash function does not compress, encode, or represent the input data; it is a non-bijective transformation that produces a fixed-length derived value used for identification, verification, or comparison, not for reconstructing the original input.
> 

> It’s a technical constitutive object.
> 

## Formulation

> A **hash function** is a mathematical or algorithmic function that converts input data of arbitrary size into a fixed-size output, called a **hash value**, **digest**, or **hash code**. Hash functions are used in data structures (e.g., hash tables), cryptography (e.g., message integrity, password storage), checksums, digital signatures, and content-addressable storage. They are designed to distribute inputs uniformly across the output space, be efficient to compute, and—when cryptographic—resist preimage, second-preimage, and collision attacks.
> 

> A hash function can be represented formally as: $h: {0,1}^* \rightarrow {0,1}^n$ where $({0,1}^*)$ is an input of arbitrary length and $({0,1}^n)$ is an n-bit fixed-size output.
> 

### Property

Properties of a good hash function:

- **Deterministic**: Same input → same hash.
- **Uniform distribution**: Hashes are evenly spread over the output space.
- **Efficient**: Computable in minimal time and resources.
- **Collision resistance (cryptographic)**: Hard to find two inputs with the same hash.
- **Preimage resistance (cryptographic)**: Hard to recover input from hash.

## Hash Function Space

| **Hash Function** | **Description** | **Digest Size** | **Performance** | **Security** | **Year** | **Tags** |
| --- | --- | --- | --- | --- | --- | --- |
| **MD5** | Cryptographic hash function widely used for checksums. | 128 bits | Very Fast (≈300 MB/s on modern CPUs) | **Broken** (Collision attacks practical) | 1992 | Legacy, checksums, collisions |
| **SHA-1** | NIST standard cryptographic hash function. | 160 bits | Fast (≈150 MB/s) | **Broken** (Collision attacks practical) | 1995 | Deprecated, TLS, certificates |
| **SHA-256** | Part of the SHA-2 family; industry standard for security. | 256 bits | Fast (≈100 MB/s) | **Strong** (No practical attacks) | 2001 | Cryptographic, blockchain, TLS |
| **SHA-3** | Keccak-based hash function; NIST standard post-SHA-2. | 224–512 bits | Moderate (≈50–100 MB/s) | **Strong** (Design differs from SHA-2) | 2015 | Cryptographic, versatile, SHA-2 alternative |
| **BLAKE2** | Optimized version of BLAKE; fast and secure. | 128–512 bits | **Very Fast** (≈1 GB/s) | **Strong** (No known practical attacks) | 2012 | Cryptographic, high-speed, versatile |
| **BLAKE3** | Latest evolution of BLAKE; parallelizable and extremely fast. | 256 bits (extendable) | **Extremely Fast** (≈5 GB/s) | **Strong** (Modern design, no attacks) | 2020 | Cryptographic, parallel, post-quantum resistant |
| **RIPEMD-160** | European-designed cryptographic hash function. | 160 bits | Moderate (≈50 MB/s) | **Strong** (No practical attacks) | 1996 | Cryptographic, Bitcoin addresses |
| **Whirlpool** | Designed for security and performance. | 512 bits | Moderate (≈40 MB/s) | **Strong** (No practical attacks) | 2000 | Cryptographic, high entropy |
| **xxHash** | Non-cryptographic hash for high-speed hashing. | 64/128 bits | **Extremely Fast** (≈10 GB/s) | Non-cryptographic | 2012 | Checksums, databases, speed |
| **MurmurHash** | Non-cryptographic hash with good distribution. | 32/128 bits | **Very Fast** (≈5 GB/s) | Non-cryptographic | 2008 | Hash tables, non-crypto, fast |
| **SipHash** | Cryptographic hash optimized for hash tables. | 64/128 bits | Fast (≈100 MB/s) | **Strong** (Resists hash-flooding) | 2012 | Cryptographic, hash tables, DoS-resistant |

## Technical Usage

> How is the hash function use?
> 

| **Usage** | **Technical Purpose** | **How the Hash Function Is Used** | **Instance** |
| --- | --- | --- | --- |
| **Data Integrity Verification** | Detect whether data has changed | Compute a hash digest of the original data and compare it with a newly computed digest later. A different hash indicates that the content changed. | File downloads publish SHA-256 checksums so users can verify the file was not corrupted. |
| **Content Identification** | Identify data by its content rather than by location or name | The hash value acts as a content-derived identifier. Equal inputs produce the same hash, allowing efficient lookup and deduplication. | Git identifies objects using SHA-1/SHA-256 hashes of their contents. |
| **Digital Signatures** | Provide authenticity and integrity | Instead of signing large data directly, systems hash the data first and sign the fixed-size digest. | A software vendor signs the SHA-256 digest of a release package. |
| **Password Storage** | Store password verifiers without storing plaintext passwords | The system stores a password-derived hash. During authentication, the entered password is hashed and compared with the stored value. | Password databases store Argon2, bcrypt, or PBKDF2 outputs. |
| **Message Authentication (MAC/HMAC)** | Verify integrity and authenticity with a shared secret | A keyed hash combines the message with a secret key to produce an authentication tag. | HMAC-SHA-256 verifies API requests. |
| **Hash Tables** | Efficient data retrieval | A hash function maps keys into positions in a table, enabling fast average-case lookup. | Programming language dictionaries/maps use hash functions internally. |
| **Caching and Memoization** | Quickly identify previously processed data | Hashes provide compact keys for stored results. | A compiler caches results using hashes of source files and build options. |
| **Deduplication** | Detect identical data | Data blocks are hashed; equal hashes suggest identical content, reducing duplicate storage. | Cloud storage systems avoid storing the same file multiple times. |
| **Distributed Systems / Content Addressing** | Locate objects by their content | The hash becomes the object's address rather than a server-specific location. | IPFS uses content identifiers derived from hashes. |
| **Blockchain and Merkle Trees** | Provide tamper-evident data structures | Hashes link blocks and summarize collections of transactions, making unauthorized modification detectable. | Bitcoin uses SHA-256 extensively for block linking and mining. |
| **Randomized Algorithms** | Create deterministic but well-distributed mappings | Hash functions spread inputs uniformly to reduce collisions and improve performance. | Load balancing assigns requests to servers using hashes. |
| **Checksums (Non-Cryptographic Hashes)** | Detect accidental errors | Simple hash functions detect transmission or storage errors. | CRC32 verifies network packets or archived files. |

## QA

### Which are the terminal enable tools in linux to computed hash values on inputs?

| Tool | Hash Algorithms Supported | Input Sources | Typical Usage | Example |
| --- | --- | --- | --- | --- |
| `sha256sum` | SHA-256 | Files, standard input | Compute cryptographic hashes for integrity verification | `sha256sum file.iso` |
| `sha1sum` | SHA-1 | Files, standard input | Legacy SHA-1 digest computation | `sha1sum document.txt` |
| `sha512sum` | SHA-512 | Files, standard input | Compute stronger SHA-2 hashes | `sha512sum archive.tar.gz` |
| `md5sum` | MD5 | Files, standard input | Legacy checksum and compatibility use (not secure for cryptographic purposes) | `md5sum file.zip` |
| `b2sum` | BLAKE2 | Files, standard input | Modern fast cryptographic hashing | `b2sum file.tar` |
| `cksum` | CRC-based checksum | Files, standard input | Detect accidental data corruption (not cryptographic) | `cksum file.bin` |
| `sum` | System-dependent checksum (often BSD/SYSV variants) | Files | Historical file checksum utility | `sum file.txt` |
| `openssl dgst` | SHA family, MD5, BLAKE2, others | Files, standard input | General-purpose cryptographic digest tool | `openssl dgst -sha256 file.txt` |
| `gpg --print-md` | Various message digests | Files, standard input | Compute hashes using GnuPG infrastructure | `gpg --print-md SHA256 file.txt` |
| `hashdeep` | MD5, SHA-1, SHA-256, Tiger, etc. | Files/directories | Recursive hashing and audit comparison | `hashdeep -r directory/` |
| `rhash` | CRC, MD5, SHA, Tiger, AICH, etc. | Files/directories | Multi-algorithm hashing and verification | `rhash --sha256 file.iso` |
| `xxhsum` | XXH32, XXH64, XXH3 | Files, standard input | Very fast non-cryptographic hashing | `xxhsum large_file.dat` |

## References

- https://github.com/Cyan4973/xxHash
- https://en.wikipedia.org/wiki/Hash_function
- [Cryptography Hash Function](https://app.notion.com/p/Cryptography-Hash-Function-231c0f5171ec8005bbf7f49f20895811?pvs=21)
- https://en.wikipedia.org/wiki/List_of_hash_functions