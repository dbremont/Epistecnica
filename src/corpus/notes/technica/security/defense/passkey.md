---
tags: [note, security, defense, identity]
---

# Passkey


> A **passkey** is a **cryptographic authentication credential** that replaces passwords. It is based on **public-key cryptography** and is designed to resist phishing, credential theft, and password reuse.

> A **passkey** is a credential consisting of a cryptographic key pair, where the **private key** remains securely stored on the user's device and the **public key** is registered with the relying party (the service). Authentication is performed by proving possession of the private key without revealing it.

## How does it works?

```jsx
Registration
────────────

User Device
 ┌────────────────────┐
 │ Generate Key Pair  │
 │                    │
 │ Private Key ◄──────┐
 │ Public Key ────────┼────────► Service
 └────────────────────┘         (stores public key)

Authentication
──────────────

Service
   │
   │ Challenge (random nonce)
   ▼
User Device
   │
   │ Sign challenge with Private Key
   ▼
Signed Challenge
   │
   ▼
Service
   │
Verify signature using stored Public Key
   │
   ▼
Authenticated
```

## References

- https://fidoalliance.org/passkeys/
- https://passkeys.directory/
