# Java Security Model

> The Java security model is a comprehensive framework designed to provide security features and mechanisms for Java applications running within the Java Virtual Machine (JVM). It encompasses various layers of security controls to protect against malicious code and unauthorized actions.
> 

| **Component** | **Description** | **Examples** |
| --- | --- | --- |
| **Security Manager** | Controls access to system resources and enforces security policies. | Custom security policies and permissions. |
| **ClassLoader Restrictions** | Prevents classes from different class loaders from interacting unless explicitly allowed. | Isolation of classes loaded by different class loaders. |
| **Java Cryptography Architecture (JCA)** | Provides a framework and implementation for encryption, decryption, and secure communication. | `Cipher`, `KeyGenerator`, `Signature`. |
| **Java Authentication and Authorization Service (JAAS)** | Framework for user authentication and access control. | Authentication modules and access control policies. |

### PKI

> 
> 

- **Key generation & storage**
    - `KeyPairGenerator` → generate RSA, EC key pairs.
    - `KeyStore` → secure container for keys and certificates.
- **Certificates**
    - `java.security.cert.X509Certificate` → representation of X.509 certificates.
    - `CertificateFactory` → load and parse certificates (PEM, DER).
- **Digital signatures**
    - `Signature` → sign and verify data using private/public keys.
- **Trust management**
    - `TrustManager` & `KeyManager` → used in SSL/TLS contexts.
    - `KeyStore` can act as trust store (CA roots).
- **Crypto providers**
    - Built-in: SunJCE, SunJSSE.
    - External: BouncyCastle (common for advanced PKI and certificate generation).