---
tags: [note, integration, api-gateway, gateway, kong]
---

# Kong Gateway

> **Kong Gateway** is an open-source API gateway and lifecycle layer: it sits between clients and the services behind it, terminates the request, applies a policy — authenticate, rate-limit, transform, log — and forwards it to the right upstream. It is built on NGINX and OpenResty, so the data plane is the proxy that already runs at the edge of most of the internet.

> The design choice that defines it is the **plugin**: routing, authentication, throttling, transformation and observability are plugins in a chain, not features compiled into the gateway. A route declares which plugins run; the gateway becomes a policy engine rather than a fixed reverse proxy.

## Formulation

### What technical element type does this technical instance belong to?

**Kong Gateway belongs to the `Production Technical System` technical element type — an organized set of services and objects realizing the API-boundary capability.**

It is a system because several components co-operate: the data plane that proxies, the control plane that configures it, the plugin runtime, and the datastore (or the declarative file) that holds configuration. Readable as a `Constitutive Technical Object` when a deployment is read as one component of an enterprise integration architecture, and as a `Technical Element Set` when the plugins and policies are read as the set.

The boundary against **Apache APISIX** is the same function with a different core (APISIX is built on NGINX and etcd, Kong on NGINX/OpenResty with Postgres or a declarative file); against **APIGEE** it is deployment model — Kong is self-hosted software, Apigee a managed cloud service.

### What is this technical instance?

> A proxy process (or a cluster of them) in front of upstream services: routes map paths and hosts to upstreams, services define the upstream, plugins attach behaviour to routes, consumers and credentials identify callers, and the admin API or a declarative file configures the whole graph. In DB-less mode the configuration is a single YAML document loaded at start; in the traditional mode it lives in Postgres and is edited through the admin API.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one gateway deployment, decomposed at shallow depth — the routing objects, the plugins, the configuration plane and the parameters. The upstream services and the clients are outside the instance.
>
> Stopping rule: a row is terminal when it names a concrete object, plugin, plane, parameter or evaluation.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.
>
> Verbs: the route *maps*; the service *targets*; the plugin *enforces*; the control plane *configures*.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical System` → Kong Gateway | The API gateway deployment: routes, services, plugins, configuration and data plane. |
| `Production Technical System` → Kong Gateway → `Production Technical Object` | Grouping: the routing and targeting objects. |
| `Production Technical System` → Kong Gateway → `Production Technical Object` → Route | The rule that matches a request by host, path, method or header. |
| `Production Technical System` → Kong Gateway → `Production Technical Object` → Service | The upstream definition a route forwards to — scheme, host, port, path, timeouts. |
| `Production Technical System` → Kong Gateway → `Production Technical Object` → Consumer | The identity a request is authenticated as, with its credentials and groups. |
| `Production Technical System` → Kong Gateway → `Production Technical Object` → Plugin Chain | The ordered set of plugins a route or service enforces. |
| `Production Technical System` → Kong Gateway → `Technical Mechanism` | Grouping: how the gateway does its work. |
| `Production Technical System` → Kong Gateway → `Technical Mechanism` → Request Routing | Match, rewrite and proxy the request to the upstream. |
| `Production Technical System` → Kong Gateway → `Technical Mechanism` → Authentication and Authorization | Key, JWT, OAuth2, OIDC or mTLS enforcement before the upstream is reached. |
| `Production Technical System` → Kong Gateway → `Technical Mechanism` → Rate Limiting | Local or Redis-backed counters that throttle by consumer, IP or service. |
| `Production Technical System` → Kong Gateway → `Technical Mechanism` → Request and Response Transformation | Header, body and path rewriting at the boundary. |
| `Production Technical System` → Kong Gateway → `Technical Mechanism` → Observability | Access logs, metrics, tracing and the plugin hooks that emit them. |
| `Production Technical System` → Kong Gateway → `Technical Parameter` | Grouping: the variables that fix the deployment. |
| `Production Technical System` → Kong Gateway → `Technical Parameter` → Configuration Mode | Traditional (Postgres-backed) or DB-less (declarative YAML). |
| `Production Technical System` → Kong Gateway → `Technical Parameter` → Upstream Timeouts and Retries | Per-service connection, read and write limits. |
| `Production Technical System` → Kong Gateway → `Technical Parameter` → Worker Processes and Connections | The NGINX worker model the data plane runs on. |
| `Production Technical System` → Kong Gateway → `Technical Constraint` | Grouping: the bounds the deployment works inside. |
| `Production Technical System` → Kong Gateway → `Technical Constraint` → Configuration Propagation | How fast a change reaches every data-plane node. |
| `Production Technical System` → Kong Gateway → `Technical Constraint` → Plugin Compatibility | The dependency and runtime limits a plugin imposes. |
| `Production Technical System` → Kong Gateway → `Technical Evaluation` | Grouping: how the deployment is judged. |
| `Production Technical System` → Kong Gateway → `Technical Evaluation` → `Verification` | Grouping: conformance of the routing and policy configuration. |
| `Production Technical System` → Kong Gateway → `Technical Evaluation` → `Verification` → Route and Policy Test | A request reaches the intended upstream with the intended policy applied. |
| `Production Technical System` → Kong Gateway → `Technical Evaluation` → `Validation` | Grouping: fitness in the integration architecture. |
| `Production Technical System` → Kong Gateway → `Technical Evaluation` → `Validation` → Latency and Throughput Measurement | The gateway's added latency and its capacity under load. |

## The Objects

| Object | What it is | Why it exists |
| --- | --- | --- |
| **Service** | The upstream definition | Separates *where* the API is from *how* it is exposed |
| **Route** | The match rule | One service can be exposed under several paths or hosts |
| **Consumer** | The API caller's identity | Credentials and rate limits attach to the caller, not the route |
| **Plugin** | A policy attached to a route, service, consumer or globally | The behaviour of the gateway is composed, not fixed |
| **Upstream** | A load-balanced set of targets | Health checks and balancing live here |

## The Planes

> Kong separates the **data plane** — the NGINX workers that proxy traffic — from the **control plane**, which holds and distributes configuration. In the traditional mode the control plane is the admin API over Postgres; in **DB-less** mode a declarative YAML file is the whole configuration, which makes the gateway a read-only artefact that can be versioned and deployed like code; and in **Kong Konnect** the control plane is a managed service that pushes configuration to data planes across clusters.

> That split is what makes the gateway operable at scale: the data plane holds no state that must be replicated, and a configuration change is a distribution problem, not a database transaction.

## In the integration architecture

> The gateway is the boundary object of an API-based integration: it is where the contract in an [OpenAPI](/view.html?p=notes/technica/general/openapi.md) document becomes runtime behaviour, where [information-systems integration](/view.html?p=notes/technica/computation/enterprise-information-system-eis/information-systems-integration.md) publishes and governs its APIs, and where the non-functional requirements — authentication, quota, observability — are applied once for every consumer instead of once per service.

## References

- [Kong](https://github.com/Kong/kong) — the gateway repository
- [Kong documentation](https://docs.konghq.com/)
- [Apache APISIX](/view.html?p=notes/technica/computation/enterprise-information-system-eis/apache-apisix.md) — the other open-source gateway on this shelf
- [Apigee](/view.html?p=notes/technica/computation/enterprise-information-system-eis/apigee.md) — the managed-cloud counterpart
- [Information Systems Integration](/view.html?p=notes/technica/computation/enterprise-information-system-eis/information-systems-integration.md) — the architecture the gateway serves
- [OpenAPI](/view.html?p=notes/technica/general/openapi.md) — the interface contract the gateway enforces
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) — the schema and the permitted link forms
