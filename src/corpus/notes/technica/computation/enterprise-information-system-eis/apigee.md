---
tags: [note, integration, api-management, apigee, google-cloud]
---

# Apigee

> **Apigee** is Google Cloud's API management platform: a gateway that proxies API traffic, a management plane that defines the proxies and policies, a developer portal that publishes them, and analytics that record how they are used. It is the managed-cloud answer to the same problem Kong and APISIX answer with self-hosted software.

> The unit of work is the **API proxy**: a facade that accepts the client's request, applies a policy pipeline, and calls the target service. The client sees the proxy's contract, not the backend's, which is what lets the backend change without the consumer noticing.

## Formulation

### What technical element type does this technical instance belong to?

**Apigee belongs to the `Production Technical System` technical element type — an organized set of services and objects realizing API-management capability.**

It is a system because gateway, management plane, portal and analytics are distinct components with distinct jobs. Readable as a `Constitutive Technical Object` inside an enterprise integration architecture, and as a `Technical Element Set` when the policy catalogue is read as the set.

The boundary against **Kong Gateway** and **Apache APISIX** is the deployment model and the policy language: Apigee is managed, policy-driven (XML policy steps) and bundled with a portal and analytics; the open-source gateways are self-hosted and plugin-driven.

### What is this technical instance?

> A set of API proxies, each with a request and response flow built from policy steps — verify API key, OAuth, quota, spike arrest, message transformation, JSON-to-XML, logging — and a target endpoint; an environment (dev, test, prod) that deploys a revision of the proxy; a developer portal where apps register and receive credentials; and analytics that record traffic, latency and errors per proxy, app and developer.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one Apigee organization, decomposed at shallow depth — the proxy, its policy pipeline, the environment and the portal. The backend services are outside the instance.
>
> Stopping rule: a row is terminal when it names a concrete object, policy, environment, parameter or evaluation.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.
>
> Verbs: the proxy *facades*; the policy *enforces*; the environment *deploys*; the portal *publishes*.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical System` → Apigee | The API management platform: proxies, policies, environments, portal and analytics. |
| `Production Technical System` → Apigee → `Production Technical Object` | Grouping: the objects the platform manages. |
| `Production Technical System` → Apigee → `Production Technical Object` → API Proxy | The facade that exposes an API and calls the target. |
| `Production Technical System` → Apigee → `Production Technical Object` → Policy Pipeline | The ordered request and response flow of policy steps. |
| `Production Technical System` → Apigee → `Production Technical Object` → Target Endpoint | The backend the proxy calls, with its own connection settings. |
| `Production Technical System` → Apigee → `Production Technical Object` → Environment | The deployment stage that holds a proxy revision. |
| `Production Technical System` → Apigee → `Production Technical Object` → Developer Portal | The publishing surface where apps register and get credentials. |
| `Production Technical System` → Apigee → `Technical Mechanism` | Grouping: how the platform does its work. |
| `Production Technical System` → Apigee → `Technical Mechanism` → Credential Verification | API key, OAuth 2.0 and JWT validation as a policy step. |
| `Production Technical System` → Apigee → `Technical Mechanism` → Quota and Spike Arrest | Rate and burst control attached to the proxy. |
| `Production Technical System` → Apigee → `Technical Mechanism` → Message Transformation | JSON, XML and SOAP conversion between client and target. |
| `Production Technical System` → Apigee → `Technical Mechanism` → Traffic Analytics | Per-proxy, per-app and per-developer metrics. |
| `Production Technical System` → Apigee → `Technical Parameter` | Grouping: the variables that fix a deployment. |
| `Production Technical System` → Apigee → `Technical Parameter` → Proxy Revision | The versioned configuration deployed to an environment. |
| `Production Technical System` → Apigee → `Technical Parameter` → Quota Interval and Allowance | The rate the policy enforces. |
| `Production Technical System` → Apigee → `Technical Parameter` → Deployment Region | Where the runtime runs, for latency and data residency. |
| `Production Technical System` → Apigee → `Technical Constraint` | Grouping: the bounds the platform works inside. |
| `Production Technical System` → Apigee → `Technical Constraint` → Managed-Service Boundary | The platform's limits — quota, region, policy runtime — which the customer does not control. |
| `Production Technical System` → Apigee → `Technical Constraint` → Migration and Hybrid Mode | The path between the managed service and a customer-operated runtime. |
| `Production Technical System` → Apigee → `Technical Evaluation` | Grouping: how the deployment is judged. |
| `Production Technical System` → Apigee → `Technical Evaluation` → `Verification` | Grouping: conformance of proxy and policies. |
| `Production Technical System` → Apigee → `Technical Evaluation` → `Verification` → Proxy Deployment Test | The revision deployed in a stage accepts and routes the intended requests. |
| `Production Technical System` → Apigee → `Technical Evaluation` → `Validation` | Grouping: fitness in the integration architecture. |
| `Production Technical System` → Apigee → `Technical Evaluation` → `Validation` → Developer Adoption and Traffic | Whether the published API is actually used by the intended consumers. |

## The Platform

| Component | What it is | Where the boundary sits |
| --- | --- | --- |
| **Runtime (gateway)** | The proxy tier that executes the policy pipeline | Customer controls proxies and policies; Google controls the runtime |
| **Management plane** | The API where proxies, products and apps are defined and deployed | Configuration, not traffic |
| **Developer portal** | The public surface for app registration and documentation | The API as a product |
| **Analytics** | Traffic, latency, error and developer metrics | Evidence for the API-programme decision |
| **API products** | The bundle of proxies and quota a developer subscribes to | The unit of monetisation and access |

## The Policy Model

> Apigee's policies are declarative steps in a flow, not code: a `VerifyAPIKey`, an `OAuthV2`, a `Quota`, a `SpikeArrest`, a `JSONToXML`, a `MessageLogging`, attached to `PreFlow`, `PostFlow` or a conditional flow. The model is closer to a mediation pipeline than to a plugin chain — the order is explicit, and the configuration is a document that can be versioned and reviewed.

> The policy model is the platform's real lock-in. Proxies and policies are portable as API definitions, but the specific policy names and the deployment tooling are Apigee's; a migration is a re-implementation of the mediation layer, not a configuration copy.

## In the integration architecture

> Apigee is the managed-cloud pole of the API-based integration pattern: it publishes the [OpenAPI](/view.html?p=notes/technica/general/openapi.md) contract as a product, enforces the non-functional requirements once for every consumer, and records the traffic that tells the organisation whether the API programme works. In an [information-systems integration](/view.html?p=notes/technica/computation/enterprise-information-system-eis/information-systems-integration.md) it is the boundary object between the internal services and the external consumers.

## References

- [Apigee documentation](https://docs.apigee.com/)
- [Apigee](https://cloud.google.com/apigee) — the product page
- [Apache APISIX](/view.html?p=notes/technica/computation/enterprise-information-system-eis/apache-apisix.md) · [Kong Gateway](/view.html?p=notes/technica/computation/enterprise-information-system-eis/kong-gateway.md) — the self-hosted gateways on this shelf
- [Information Systems Integration](/view.html?p=notes/technica/computation/enterprise-information-system-eis/information-systems-integration.md) — the architecture the platform serves
- [OpenAPI](/view.html?p=notes/technica/general/openapi.md) — the contract the proxy publishes
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) — the schema and the permitted link forms
