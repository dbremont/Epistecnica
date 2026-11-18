---
tags: [note, production]
---

# Security

> Note:  All the time - even competent Twitter users get hacked.
>

When you can't fully control authentication or post-authentication interactions (e.g., stolen tokens), shift trust to message-level cryptography. Each client request is signed with an asymmetric private key; the server verifies the signature (and optionally checks a nonce/timestamp) via a public-key verification endpoint. Combine this with revocation lists, hardware-backed keys, and short-lived tokens to reduce the impact of compromise.

Quick implementation checklist

- Use asymmetric signatures (ECDSA/ED25519) for client-signed requests.
- Include a nonce/timestamp to prevent replay.
- Provide a server endpoint that verifies signatures and returns validation status.
- Store public keys in a trusted registry and support key rotation.
- Use short-lived authentication tokens plus message signing for high-risk operations.
- Consider hardware-backed keys (TPM, secure enclave, or YubiKey) for private-key protection.
- Log and alert on signature verification failures and unusual patterns.