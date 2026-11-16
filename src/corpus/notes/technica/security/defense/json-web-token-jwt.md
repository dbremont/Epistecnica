---
tags: [note, security, defense, representation]
---

# JSON Web Token (JWT)

> Related: [Cryptographic Data](/view.html?p=notes/technica/security/defense/cryptographic-data.md), [Message Authentication Code (MAC)](/view.html?p=notes/technica/security/defense/message-authentication-code-mac.md), [JSON Web Signature (JWS)](/view.html?p=notes/technica/security/defense/json-web-signature-jws.md)

> A **JWT** is a **base64url-encoded string** that encodes a set of **claims** as a **JSON object**, optionally signed and/or encrypted for integrity and confidentiality.

> **JSON Web Token (JWT)** is a compact, URL-safe means of representing claims to be transferred between two parties.  The claims in a JWT are encoded as a JSON object that is used as the payload of a **JSON Web Signature (JWS)** structure or as the plaintext of a JSON **Web Encryption (JWE)** structure, enabling the claims to be digitally signed or integrity protected with a **Message Authentication Code (MAC)** and/or encrypted.

> Note: This mechanism supports asymmetric cryptography, where a private key is used to sign the token and a public key is used to verify its signature.

![image.png](../assets/note/technica/security/defense/json-web-token-jwt/image.png)

OAuth 2.0 Encoding:

- HS256 (JSON Web Signature (**JWS**))
- RS256 (**JWK** Public Key Info)

## 🧱 Structure

> A JWT is composed of **three parts**, separated by `.`:  `<Header>.<Payload>.<Signature>`

Each component is base64url-encoded:

1. **Header**:
    - A JSON object describing metadata about the token, particularly:
        - `alg`: the signing algorithm (e.g., `HS256`, `RS256`)
        - `typ`: token type, usually `"JWT"`
    - Example:
        
        ```json
        {
          "alg": "RS256",
          "typ": "JWT"
        }
        
        ```
        
2. **Payload (Claims Set)**:
    - A JSON object containing **claims**, which are statements about an entity (typically the user) and additional data.
    - Claims may be:
        - **Registered** (e.g., `iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`)
        - **Public** (defined by standards or agreed-upon schema)
        - **Private** (custom-defined between parties)
3. **Signature**:
    - Computed as:
        
        ```
        HMACSHA256(
          base64urlEncode(header) + "." + base64urlEncode(payload),
          secret
        )
        
        ```
        
        - or using asymmetric algorithms like RSA/ECDSA:
        
        ```
        RSASHA256(privateKey, base64urlEncode(header) + "." + base64urlEncode(payload))
        
        ```
        
    - Used for **integrity** and **authentication** of the token's issuer.

## ⚙️ Technical Characteristics

- **Encoding**: Uses Base64url encoding (no padding).
- **Transport**: Designed to be URL-safe; suitable for HTTP headers (e.g., `Authorization: Bearer <token>`), query strings, or request bodies.
- **Cryptographic Security**:
    - Supports **JWS (JSON Web Signature)** for signing.
    - May support **JWE (JSON Web Encryption)** for confidentiality (not common in typical JWT usage).
- **Statelessness**: The token is **self-contained**; no need for server-side session storage.
- **Expiration & Revocation**:
    - JWTs are typically **immutable** and have an `exp` claim.
    - Revocation must be handled via external mechanisms (e.g., revocation lists, token blacklists).

## 🛠️ Implementation Considerations

- Token validation requires:
    - Verifying the **signature** using the shared secret or public key.
    - Validating the **claims** (e.g., expiration, issuer, audience).
- JWTs should **not be stored in local storage** in browsers due to XSS risks.
- When used improperly, JWTs can be a **security liability** (e.g., algorithm confusion attacks).

## 🔄 Use Cases

- **Authentication**: Carrying user identity across stateless systems.
- **Authorization**: Embedded roles/permissions claims.
- **Federation**: SSO via OpenID Connect (OIDC).
- **Inter-service communication**: Auth between microservices.

## 🔐 Security Flow with JWT

### **Authentication (Login Phase)**

The client authenticates with credentials to the **Authorization Server** (or identity provider).

Flow:

1. **Client → Auth Server**: Sends credentials (e.g., `username`, `password`) over HTTPS.
2. **Auth Server**:
    - Verifies credentials.
    - Generates a JWT containing user identity and claims.
    - Signs it using a secret (`HS256`) or private key (`RS256`).
3. **Auth Server → Client**: Returns the signed JWT.
    - Example: `Authorization: Bearer <JWT>`

JWT Payload Example:

```json
{
  "sub": "user123",
  "name": "Alice",
  "iat": 1716938400,
  "exp": 1716942000,
  "role": "admin"
}

```

---

### **Resource Access (Authorization Phase)**

The client sends the JWT with each request to the **Resource Server**.

Flow:

1. **Client → Resource Server**: Sends request with JWT in the `Authorization` header:
    
    ```
    Authorization: Bearer <JWT>
    
    ```
    
2. **Resource Server**:
    - Extracts and decodes the JWT.
    - **Validates**:
        - Signature (via HMAC key or RSA public key)
        - Expiration (`exp`), not-before (`nbf`), issued-at (`iat`)
        - Audience (`aud`) and issuer (`iss`) if applicable
    - Grants or denies access based on claims (e.g., `role`, `scope`)

### **Token Expiration & Renewal**

JWTs often have **short TTLs** (e.g., 15 mins) and are refreshed using **refresh tokens**.

Refresh Flow (optional):

1. **Client → Auth Server**: Sends a refresh token (securely stored).
2. **Auth Server**: Validates the refresh token and issues a new JWT.
3. **Client → Resource Server**: Uses the new JWT for further access.

### **Revocation (Caveat)**

Because JWTs are stateless and self-contained, **revocation is non-trivial**.

- **Mitigation options**:
    - Use **short-lived access tokens** + **long-lived refresh tokens**.
    - Maintain a **token blacklist** (e.g., in Redis).
    - Rotate signing keys and/or change secrets.

## ⚠️ Common Pitfalls

- **Not validating tokens**: Always verify signature + expiration.
- **Storing in localStorage**: Vulnerable to XSS.
- **Long-lived JWTs**: Risky without revocation mechanisms.
- **Misuse of algorithms**: e.g., allowing `"alg": "none"`.

## References

- [jwt.io](https://jwt.io/)
- [Self-Encoded Access Tokens](https://www.oauth.com/oauth2-servers/access-tokens/self-encoded-access-tokens/)
- [JSON Web Tokens](https://auth0.com/docs/secure/tokens/json-web-tokens)
- [Validate JSON Web Tokens](https://auth0.com/docs/secure/tokens/json-web-tokens/validate-json-web-tokens)
- [JSON Web Signature (JWS)](https://datatracker.ietf.org/doc/html/rfc7515#section-4.1.4)
- https://datatracker.ietf.org/doc/html/rfc7519
- https://news.ycombinator.com/item?id=44092102
