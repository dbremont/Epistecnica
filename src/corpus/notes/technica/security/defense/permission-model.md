---
tags: [note, security, defense, permission]
---

# Permission Model

> Related: [Identity Model](/view.html?p=notes/technica/security/defense/identity-model.md), [OAuth](/view.html?p=notes/technica/security/defense/oauth.md)

> Authorization is the process of determining whether a user, application, or system has the appropriate permissions to access a specific resource, perform an action, or use a service.

## Authorization Models

> Authorization models determine access controls and permissions for authenticated users or entities within a system.

**Role-Based Access Control (RBAC)**: Users are assigned roles, and each role has specific permissions. Access to resources is based on the user’s role.

**Attribute-Based Access Control (ABAC)**: Access decisions are based on attributes or characteristics of users, resources, and the environment, allowing for more flexible and fine-grained access control.

**Discretionary Access Control (DAC)**: Owners of resources have control over who can access them and can grant or revoke permissions as they see fit.

**Mandatory Access Control (MAC)**: Access control is based on a set of predefined rules or policies, and users cannot change or modify the access controls.

**Role-Based Access Control with Hierarchies (RBAC-H)**: An extension of RBAC that includes role hierarchies, allowing roles to inherit permissions from other roles.

**Rule-Based Access Control (RBAC)**: Access decisions are based on a set of rules or policies rather than fixed roles or attributes.

**Policy-Based Access Control (PBAC)**: Access control is determined by a set of policies that define what actions are allowed or denied.

**Claims-Based Access Control**: Access decisions are based on claims (assertions) about the user or entity’s identity and attributes.

**Time-Based Access Control**: Access to resources is granted or restricted based on specific time periods.

**Attribute-Based Access Control with Policy (ABAC-P)**: Combines ABAC with policy-based access control to manage access based on attribute conditions and policies.

**History-Based Access Control**: Access control decisions consider historical data or past actions of the user.

**Context-Based Access Control**: Access decisions are based on the context in which the user is accessing the resource, such as location or device.

**Relationship-Based Access Control (ReBAC)**: Access decisions are influenced by relationships between users and resources.

**Organization-Based Access Control**: Access control is defined based on the user’s organizational role or affiliation.

**Risk-Based Access Control**: Access decisions are made based on risk factors associated with the user, resource, or the environment.

**Hierarchical Access Control**: Access is granted based on a hierarchical structure, such as organization levels or project teams.

**Non-Discretionary Access Control**: Also known as centralized access control, where access decisions are made by a central authority.

**Peer-Based Access Control**: Peers within a network collectively make access decisions based on a consensus mechanism.

**Delegated Access Control**: Users can delegate their access rights to other users, often used in delegation scenarios.

## References

- [Authorization](https://en.wikipedia.org/wiki/Authorization)
- [Why Authorization Is Hard (osohq.com)](https://news.ycombinator.com/item?id=28543457)
- [Zanzibar: Google’s Consistent, Global Authorization System](https://research.google/pubs/pub48190/)
    - [HN 20132520](https://news.ycombinator.com/item?id=20132520)
- [Use Keycloak as Identity Provider in ASP.NET Core 6](https://nikiforovall.github.io/aspnetcore/dotnet/2022/08/24/dotnet-keycloak-auth.html)
- Atluri, Vijayalakshmi, and Wei-Kuang Huang. “An authorization model for workflows.” Computer Security—ESORICS 96: 4th European Symposium on Research in Computer Security Rome, Italy, September 25–27, 1996 Proceedings 4. Springer Berlin Heidelberg, 1996.
- Trnka, M., Abdelfattah, A. S., Shrestha, A., Coffey, M., & Cerny, T. (2022). Systematic Review of Authentication and Authorization Advancements for the Internet of Things. Sensors (Basel, Switzerland), 22(4). https://doi.org/10.3390/s22041361
- Bucko, Ahmet, et al. “Enhancing JWT Authentication and Authorization in Web Applications Based on User Behavior History.” Computers 12.4 (2023): 78.
- [Authorization Modeling By Example](https://www.linkedin.com/pulse/authorization-modeling-example-mike-sparr)
- [Security Models: Authentication and Authorization Explained](https://www.linkedin.com/pulse/security-models-authentication-authorization-explained-mike-sparr/)
- [What’s the Right Authorization Model for My Application?](https://auth0.com/blog/whats-the-right-authorization-model-for-my-application/)
- [Authorization in a Microservices World (alexanderlolis.com)](https://news.ycombinator.com/item?id=30878926)
- [Pundit](https://github.com/varvet/pundit)
- [Distributed Systems Security - Autho](https://people.cs.rutgers.edu/~pxk/417/notes/oauth.html)

[Authentication Schemes](/view.html?p=notes/technica/security/defense/permission-model/authentication-schemes.md)

[Password](/view.html?p=notes/technica/security/defense/permission-model/password.md)
