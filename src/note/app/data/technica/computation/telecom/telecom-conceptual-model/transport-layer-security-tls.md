---
tags: [computer-network, protocol]
---

# Transport Layer Security (TLS)

- [SSH](note.html?n=technica/computation/telecom/telecom-conceptual-model/ssh.md)

> In this note, we will explore a key feature of internetworking: TLS, a cryptographic security protocol.
> 

> **Transport Layer Security (TLS)** is a **cryptographic protocol** that operates above the transport layer (typically TCP) to provide **confidentiality, integrity, and authentication** of application-layer data in network communications. It establishes a **secure session** through a **handshake process** that negotiates cryptographic parameters, performs **asymmetric key exchange** (e.g., RSA, ECDHE), derives **symmetric session keys**, and optionally authenticates endpoints using **X.509 digital certificates**. TLS ensures that transmitted data is **encrypted, tamper-evident, and origin-authenticated**, while supporting forward secrecy and modern cryptographic primitives (e.g., AES-GCM, ChaCha20-Poly1305, SHA-2/3).
> 

## Formulation

> What exactly does the TLS protocol do, and how does it work?
> 

### **Handshake Phase (Connection Setup):**

- The client and server **negotiate protocol version, cipher suites, and cryptographic parameters**.
- **Key exchange** is performed using asymmetric cryptography (e.g., RSA, ECDHE) to securely establish shared session keys.
- The server (and optionally the client) presents **X.509 digital certificates** to authenticate identities.
- The handshake may also support **forward secrecy**, ensuring past sessions remain secure even if long-term keys are compromised.

### **Record Phase (Data Transmission):**

- Application data is **encrypted using symmetric encryption** (AES, ChaCha20, etc.) derived from the session keys.
- Each message is **integrity-checked using MACs or AEAD schemes** to prevent tampering.
- The protocol allows **fragmentation, compression (optional), and secure multiplexing** of application data.

## Capability

> Which are the functions supported by the Protocol?
> 

| **TLS Capability** | **Description** |
| --- | --- |
| **Confidentiality** | Provides encryption of data in transit using symmetric algorithms (AES, ChaCha20, 3DES, etc.) |
| **Integrity** | Ensures data has not been altered using MACs (HMAC-SHA256, HMAC-SHA384) or AEAD schemes (AES-GCM, ChaCha20-Poly1305) |
| **Authentication** | Verifies identities using X.509 digital certificates and public key cryptography (RSA, ECDSA) |
| **Key Exchange** | Establishes session keys securely using asymmetric cryptography (RSA, Diffie-Hellman, ECDHE) |
| **Forward Secrecy** | Protects past sessions by using ephemeral key exchanges (DHE, ECDHE) |
| **Protocol Negotiation** | Negotiates TLS version, cipher suite, and optional extensions during the handshake |
| **Fragmentation / Multiplexing** | Breaks application data into secure records via the TLS Record Protocol |
| **Session Resumption** | Reduces handshake overhead for reconnecting clients using Session IDs or Session Tickets |

## History

> What is the history of TSL?
> 

| **Year** | **Event** | **Description** | **Version** |
| --- | --- | --- | --- |
| Early 1990s | SSL 1.0 (internal) | Developed by Netscape but **never released** due to severe flaws | SSL 1.0 |
| 1994 | SSL 2.0 released | First publicly released SSL version by Netscape; had serious security flaws | SSL 2.0 |
| 1995 | SSL 3.0 released | Redesigned protocol with stronger security and more robust handshake; became basis for TLS | SSL 3.0 |
| 1999 | TLS 1.0 standardized | Upgrade of SSL 3.0 by IETF; minor changes but more secure; RFC 2246 | TLS 1.0 |
| 2006 | TLS 1.1 standardized | Added protection against CBC attacks; improved security | TLS 1.1 |
| 2008 | TLS 1.2 standardized | Support for stronger hash functions (SHA-256), AEAD cipher suites, and improved flexibility | TLS 1.2 |
| 2018 | TLS 1.3 standardized | Reduced handshake round-trips, removed insecure algorithms, mandatory forward secrecy | TLS 1.3 |

## Related

> Which are others related protocols?
> 

| **Protocol** | **Purpose / Relation to TLS** |
| --- | --- |
| **SSL (Secure Sockets Layer)** | Predecessor to TLS; TLS is backward-compatible with SSL 3.0 in design (but SSL is now obsolete) |
| **HTTPS (HTTP over TLS)** | Application-layer protocol (HTTP) secured by TLS; encrypts web traffic |
| **DTLS (Datagram TLS)** | TLS variant for unreliable transport (UDP); used in VoIP, streaming, VPNs |
| **IPSec (Internet Protocol Security)** | Network-layer encryption and authentication; protects all IP traffic, unlike TLS which secures individual connections |
| **SSH (Secure Shell)** | Provides secure remote login and command execution; uses its own key exchange and encryption separate from TLS |
| **STARTTLS** | Mechanism to upgrade plain-text protocols (SMTP, IMAP, POP3) to use TLS for encryption |
| **QUIC / HTTP/3** | Modern transport protocol built on UDP with integrated TLS 1.3 encryption for web traffic |

## Alternative

> Which are the alternatives to TLS?
> 

| **Alternative** | **Description** | **Network Layer** |
| --- | --- | --- |
| **IPSec** | Encrypts and authenticates all IP traffic; secures communication between hosts or networks independently of applications | Network / Internet Layer |
| **SSH (Secure Shell)** | Provides secure remote login, command execution, and port forwarding using its own encryption | Application / Session Layer |
| **Kerberos** | Network authentication protocol; issues session keys for secure communication | Application / Session Layer |
| **VPN protocols (WireGuard, OpenVPN, etc.)** | Creates encrypted tunnels over insecure networks; may use pre-shared keys or independent cryptography | Network / Transport Layer |
| **S/MIME / PGP** | Encrypts and signs messages directly at the application layer; end-to-end security | Application Layer |
| **DTLS** | Datagram TLS; provides TLS-like security for unreliable transports like UDP | Transport Layer (UDP) |

## QA

### How HTTPS is implemented?

> A Guide to Implementing a Let’s Encrypt Certificate
> 

## References

- [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)
- [Fetch Itself, Byte by Byte, Over TLS](https://subtls.pages.dev/)
- https://datatracker.ietf.org/doc/html/rfc8446
- https://eprint.iacr.org/2021/467
- [TLS 1.3 -Stanford](https://web.stanford.edu/class/ee380/Abstracts/151118-slides.pdf)