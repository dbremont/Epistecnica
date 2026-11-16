---
tags: [note, security, defense, permission]
---

# OAuth

> Related: [Permission Model](/view.html?p=notes/technica/security/defense/permission-model.md), [OpenID](/view.html?p=notes/technica/security/defense/openid.md), [Identity Model](/view.html?p=notes/technica/security/defense/identity-model.md)

> OAuth 2.0 is an **authorization framework** that enables a user to grant limited access to their resources on one service to another service **without sharing credentials**.

> Identity + Permision.

![](https://upload.wikimedia.org/wikipedia/commons/7/72/Abstract-flow.png)

![image.png](../assets/note/technica/security/defense/oauth/image.png)

Abstract Flow

## 🔁 **OAuth Roles**

| **Role** | **Description** |
| --- | --- |
| **Resource Owner** | The user who authorizes access to a resource. |
| **Client** | The app requesting access on behalf of the user. |
| **Resource Server** | The API server hosting the protected resources. |
| **Authorization Server** | Issues tokens to the client after authenticating the user. |

## 📦 **Token Types**

| **Token** | **Purpose** |
| --- | --- |
| **Access Token** | Allows access to protected resources. Short-lived. |
| **Refresh Token** | Used to obtain new access tokens without user interaction. |
| **ID Token** (OIDC) | Contains user identity info (used only in OpenID Connect). |

## 🔁 **Common OAuth 2.0 Flows**

| **Flow** | **Used For** | **Notes** |
| --- | --- | --- |
| **Authorization Code** | Web & mobile apps (with backend) | Most secure; uses code exchange with client authentication. |
| **Authorization Code with PKCE** | SPAs & mobile (public clients) | Adds security for public clients; replaces implicit flow. |
| **Client Credentials** | Server-to-server auth | No user involved; uses client ID and secret only. |
| **Resource Owner Password Credentials (ROPC)** | Trusted apps only | Deprecated; app asks directly for user’s credentials (insecure). |
| **Implicit (Deprecated)** | Browser-based apps | No longer recommended due to security weaknesses. |

## 🌐 **Core HTTP Endpoints**

| **Endpoint** | **Method** | **Description** |
| --- | --- | --- |
| `/authorize` | `GET` | Used by the client to obtain authorization grant (code or token). |
| `/token` | `POST` | Used by the client to exchange code for tokens. |
| `/revoke` | `POST` | Optional. Revoke access/refresh tokens. |
| `/introspect` | `POST` | Optional. Validate a token’s active status and metadata. |

## Scopes

> OAuth 2.0, scopes are used to specify the level of access and permissions that a client application is requesting from a resource owner (user) when accessing protected resources. Scopes define what actions or data the client is allowed to access. They help ensure that clients only request the permissions they need and that users have control over the data they share.

## 🔁 **OAuth vs OpenID Connect**

| **OAuth 2.0** | **OpenID Connect (OIDC)** |
| --- | --- |
| Authorization framework | Authentication protocol (built on OAuth 2.0) |
| Provides access tokens for APIs | Adds ID token for user identity |
| No standard user info mechanism | Standardized user info (`sub`, `email`, `name`, etc.) |
| Used for API access | Used for Single Sign-On (SSO) |

## References

- [The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/rfc/rfc6749)
- [Libraries](https://oauth.net/code/)
- [OAuth 2 Explained In Simple Terms](https://www.youtube.com/watch?v=ZV5yTm4pT8g)
- [OAuth 2.0 and OpenID Connect (in plain English)](https://www.youtube.com/watch?v=996OiexHze0)
- [OAuth 2.0 Debugger](https://oauthdebugger.com/)
- [An Introduction to OAuth 2](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2)
- [Why is OAuth still hard in 2023?](https://www.nango.dev/blog/why-is-oauth-still-hard)
- Complementary Specs:
    - [RFC 7636: Proof Key for Code Exchange (PKCE)](https://oauth.net/2/pkce/)
    - [OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens](https://datatracker.ietf.org/doc/html/rfc8705)
    - [OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693.html)
    - [OAuth 2.0 Authorization Server Metadata](https://datatracker.ietf.org/doc/html/rfc8414)
    - [The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750)
    - [JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://datatracker.ietf.org/doc/html/rfc7523)
    - [Proof Key for Code Exchange by OAuth Public Clients (PKCE)](https://datatracker.ietf.org/doc/html/rfc7636)
    - [OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens](https://datatracker.ietf.org/doc/html/rfc8705)
    - [RFC 7009: Token Revocation](https://oauth.net/2/token-revocation/)
    - [More](https://oauth.net/specs/)
    - [OAuth Working Group Specifications](https://oauth.net/specs/)
- …
