---
tags: [note, security, defense, identity]
---

# OpenID

> Related: [Identity Model](/view.html?p=notes/technica/security/defense/identity-model.md), [OAuth](/view.html?p=notes/technica/security/defense/oauth.md)

> **OpenID** is an **open and decentralized authentication protocol** that allows users to log into multiple websites using a **single identity** provided by a trusted third party (an **OpenID Provider**).

| **Term** | **Definition** |
| --- | --- |
| **User (End-User)** | The person trying to log into a website. |
| **Relying Party (RP)** | The website or application that accepts OpenID login (e.g., a blog or SaaS app). |
| **OpenID Provider (OP)** | The identity provider (e.g., Google, Yahoo) that authenticates the user. |

## 📜 **How It Works (Simplified Flow)**

1. **User visits** a website (the *Relying Party*).
2. They choose to log in with an OpenID Provider (e.g., `google.com`).
3. The Relying Party redirects the user to the OpenID Provider.
4. The user logs in and **authenticates with the Provider**.
5. The Provider **sends back a signed assertion** to the Relying Party.
6. The Relying Party **verifies the assertion**, and logs the user in.

## 📚 **Variants and Evolution**

| **Protocol** | **Description** |
| --- | --- |
| **OpenID 1.0 / 2.0** | Original protocol for federated identity. Focused only on authentication. |
| **OpenID Connect (OIDC)** | Modern version built on top of OAuth 2.0. Supports **identity**, **authentication**, and **user info sharing** in a secure and extensible way. |

## OpenID Connect HTTP Spec

| Endpoint | Purpose | Typical URL Path |
| --- | --- | --- |
| **Authorization Endpoint** | Where client redirects user to authenticate and authorize | `/authorize` |
| **Token Endpoint** | Exchange authorization code for tokens (ID token, access token) | `/token` |
| **UserInfo Endpoint** | Retrieve user profile information with access token | `/userinfo` |
| **JWKS URI** | Retrieve JSON Web Key Set (public keys for JWT verification) | `/.well-known/jwks.json` |
| **Discovery Endpoint** | Fetch OpenID Provider configuration metadata | `/.well-known/openid-configuration` |

### Endpoints

| Endpoint | Purpose | Typical URL Path |
| --- | --- | --- |
| **Authorization Endpoint** | Where client redirects user to authenticate and authorize | `/authorize` |
| **Token Endpoint** | Exchange authorization code for tokens (ID token, access token) | `/token` |
| **UserInfo Endpoint** | Retrieve user profile information with access token | `/userinfo` |
| **JWKS URI** | Retrieve JSON Web Key Set (public keys for JWT verification) | `/.well-known/jwks.json` |
| **Discovery Endpoint** | Fetch OpenID Provider configuration metadata | `/.well-known/openid-configuration` |

### **Authorization Request (HTTP GET)**

```bash
GET /authorize?response_type=code
 &client_id=CLIENT_ID
 &redirect_uri=https%3A%2F%2Fclient.example.com%2Fcallback
 &scope=openid%20profile%20email
 &state=xyzABC123
 &nonce=randomNonce123 HTTP/1.1
Host: accounts.exampleop.com
```

### **Token Request (HTTP POST)**

```bash
grant_type=authorization_code
&code=AUTH_CODE_RECEIVED
&redirect_uri=https%3A%2F%2Fclient.example.com%2Fcallback
&client_id=CLIENT_ID
&client_secret=CLIENT_SECRET
```

### UserInfo Request

```bash
Authorization: Bearer ACCESS_TOKEN
```

### JWT Validation

```bash
GET /.well-known/jwks.json HTTP/1.1
Host: accounts.exampleop.com
```

### **Discovery Document**

```bash
GET /.well-known/openid-configuration HTTP/1.1
Host: accounts.exampleop.com
```

## **OpenID Provider (OP)**

| **Provider Name** | **Description** | **Type** | **Notable Features** | **Typical Use Cases** |
| --- | --- | --- | --- | --- |
| Google Identity | Google’s OIDC provider supporting millions of users. | Public / Global | Easy integration, wide adoption, free tier. | Consumer apps, websites, mobile apps. |
| Microsoft Entra ID (Azure AD) | Microsoft’s enterprise-grade identity platform. | Enterprise / Cloud | Enterprise SSO, MFA, conditional access. | Corporate apps, internal portals. |
| Auth0 | Cloud identity platform supporting OIDC and many protocols. | SaaS / Multi-tenant | Highly customizable, social login, rules. | SaaS, startups, custom identity flows. |
| Okta | Enterprise identity management & SSO platform. | Enterprise / Cloud | Lifecycle management, MFA, API access mgmt. | Enterprise apps, B2B, workforce identity. |
| Amazon Cognito | AWS service for user sign-up, sign-in, and access control. | Cloud / AWS | Tight AWS integration, social identity links. | AWS-powered apps, mobile/web apps. |
| Ping Identity | Enterprise identity federation and SSO solution. | Enterprise | Robust federation, API security, hybrid cloud. | Large enterprises, complex environments. |
| Keycloak | Open-source identity and access management server. | Self-hosted / Open Source | Full OIDC and SAML support, extensible. | On-premises, private clouds, dev/test. |
| Apple ID | Apple’s OIDC provider for iOS/macOS ecosystem users. | Public / Global | Privacy-focused, native device integration. | iOS/macOS apps, consumer-facing apps. |
| GitHub | GitHub’s OAuth2/OIDC for developer identity. | Public / Developer | Popular for developer tools and integrations. | Developer portals, DevOps tools. |
| Salesforce | Cloud CRM with identity services supporting OIDC. | Enterprise / SaaS | CRM integration, customer identity mgmt. | Sales apps, customer portals. |

## Case Study


### Library

| Platform | Popular Libraries | Notes |
| --- | --- | --- |
| **JavaScript** | `oidc-client`, `openid-client`, `next-auth` | Client-side and server-side implementations |
| **Python** | `python-oauthlib`, `Authlib`, `mozilla-django-oidc` | For Flask, Django, FastAPI |
| **Java** | `spring-security-oauth2-client` | Integration with Spring Security |
| **.NET** | `Microsoft.Identity.Web`, `OpenIdConnect` | ASP.NET Core middleware |
| **Go** | `coreos/go-oidc` | OpenID Connect verification library |
| **Ruby** | `omniauth-openid-connect` | OmniAuth strategy for OIDC |

## References

- [OpenID](https://www.wikiwand.com/en/OpenID_Connect)
- https://github.com/dbremont/security-labs/tree/main/server
