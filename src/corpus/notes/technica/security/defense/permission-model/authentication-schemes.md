---
tags: [note, security, defense]
---

# Authentication Schemes

In .NET Core, authentication schemes refer to different methods or mechanisms used to authenticate users and secure applications. Here are some common authentication schemes in .NET Core:

1. **Cookie Authentication:** Uses browser cookies to maintain user sessions and authentication state.
2. **JWT (JSON Web Token) Authentication:** Utilizes JWTs to provide stateless authentication and authorization for API endpoints.
3. **OAuth 2.0:** Implements OAuth 2.0 authorization flows for third-party authentication and access to user data.
4. **OpenID Connect:** Extends OAuth 2.0 to provide identity verification and single sign-on capabilities.
5. **Windows Authentication:** Uses the user’s Windows credentials for authentication in intranet scenarios.
6. **API Key Authentication:** Validates API keys provided by clients for accessing API resources.
7. **Token Exchange:** Allows exchanging one token (e.g., OAuth access token) for another token with different permissions.
8. **External Authentication Providers:** Integrates with external identity providers like Google, Facebook, Microsoft, etc., for single sign-on.
9. **Certificate Authentication:** Authenticates clients using digital certificates.
10. **Bearer Token Authentication:** Similar to JWT authentication, but not necessarily using JSON Web Tokens.
11. **Custom Authentication Schemes:** Developers can create custom authentication schemes tailored to their application’s requirements.
12. **One-Time Password (OTP)**: Is a temporary and unique authentication code, typically valid for a single login session or transaction, providing an additional layer of security beyond traditional static passwords.

These authentication schemes provide flexibility for securing various types of applications, such as web applications, APIs, and microservices, by allowing developers to choose the most suitable method based on their security needs and application architecture.

## References

[One-Time Password (OTP)](/view.html?p=notes/technica/security/defense/permission-model/authentication-schemes/one-time-password-otp.md)
