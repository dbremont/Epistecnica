---
tags: [note, security, defense, cryptographic]
---

# Digital Signature

> Related: [Cryptography System](/view.html?p=notes/technica/security/defense/cryptography-system.md), [Public Key Infrastructure (PKI)](/view.html?p=notes/technica/security/defense/public-key-infrastructure-pki.md)

> A **digital signature** is a cryptographic **mechanism (scheme)** that allows a party holding a private key to generate a unique piece of data, called a **signature**, that is mathematically bound to a specific message.
> Anyone possessing the corresponding public key can verify this signature, ensuring three properties:
> - **Authenticity** – the message truly originated from the holder of the private key.
> - **Integrity** – the message has not been altered since it was signed.
> - **Non-repudiation** – the signer cannot later deny having produced the signature.

![](https://i.stack.imgur.com/vpO8V.png)

## Scheme Working

> How the digital signature scheme works?

Digital signatures use **asymmetric-key cryptography**, involving:

- A **private key** (kept secret by the signer)
- A **public key** (shared with everyone)

- **Key Generation** produces a pair of keys: a private signing key and a public verification key.
- **Signing Process:**
    1. The sender creates a **hash** (digest) of the message.
    2. The hash is **encrypted with the sender’s private key** — this is the **digital signature**.
    3. The original message + signature are sent to the receiver.
- **Verification Process:**
    1. The receiver computes a **hash of the received message**.
    2. The receiver uses the **sender’s public key** to **decrypt the signature** and obtain the original hash.
    3. If the two hashes match:
        - The message is **authentic** and **untampered**.
        - The signature is **valid**.

## 🔐 **Use**

- **SSL/TLS certificates** (HTTPS)
- **Code signing** (software distribution)
- **Blockchain and cryptocurrencies** (e.g., Bitcoin)
- **PDF document signing**
- **Email signing** (e.g., S/MIME, PGP)

## References

- [Signature verification vs decryption?](https://crypto.stackexchange.com/questions/71355/signature-verification-vs-decryption)
- [Digital Signature Algorithm](https://en.wikipedia.org/wiki/Digital_Signature_Algorithm)
- [RSA vs. DSA for SSH Authentication Keys](https://security.stackexchange.com/questions/5096/rsa-vs-dsa-for-ssh-authentication-keys)
- https://blog.cryptographyengineering.com/euf-cma-and-suf-cma/
- https://en.wikipedia.org/wiki/Digital_signature_forgery
