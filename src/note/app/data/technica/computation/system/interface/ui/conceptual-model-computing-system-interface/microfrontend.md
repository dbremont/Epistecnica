# Microfrontend


> 

Guiding questions:

- What is the nature of the idea of a micro-froneend? Is this a technique?
- /
- What is the nature of the problem solved this strategy?
- Which are the implementation techniques?
- How should the microfront ends communicate?
- How to design an observabilty layers - that allows us to make sense of the interactions?

## Interaction Model(s)

| **Strategy** | **Mechanism** | **Coupling** | **Sync Model** | **Topology** | **State Ownership** | **Primary Use Cases** | **Strengths** | **Weaknesses / Failure Modes** | **Governance Requirements** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Event-Driven (DOM Events / CustomEvent)** | `window.dispatchEvent`, `addEventListener` | Low | Asynchronous | Broadcast (1→N) | Distributed | Cross-cutting events (cart, auth, notifications) | Decoupled, scalable, framework-agnostic | Hard to trace, no type safety, silent no-op if no listeners | Event schema registry, naming conventions, instrumentation |
| **Message Bus (Pub/Sub Abstraction)** | Central bus (`publish/subscribe`) | Low | Asynchronous | Mediated (via broker) | Distributed | Large-scale MFE ecosystems, orchestration | Observability, replay, central control | Added complexity, infra overhead | Typed contracts, event versioning, monitoring |
| **Shared State (Client Store)** | Redux, Zustand, RxJS | Medium | Reactive (push-based) | Centralized | Shared | Auth, session, feature flags | Single source of truth, predictable updates | Hidden coupling, global state sprawl | Ownership rules, schema control, strict boundaries |
| **Direct API Calls (Imperative)** | `window.api.method()` | High | Synchronous | Point-to-point (1→1) | Caller/Owner defined | Performance-critical paths, tightly bound MFEs | Explicit, simple, low latency | Tight coupling, versioning breakage | Versioned interfaces, strict contracts (TS/IDL) |
| **URL / Routing-Based** | Query params, path state | Low | Stateless (request-driven) | Indirect (via router) | Externalized (URL) | Navigation flows, deep linking | Transparent, browser-native, bookmarkable | Limited payload, encoding complexity | URL schema design, backward compatibility |
| **Web Components / DOM Props** | Custom elements + attributes/events | Medium | Mixed (props + events) | Hierarchical (DOM tree) | Component-local | Design systems, framework interoperability | Encapsulation, standard interface | Prop drilling, limited global coordination | Component contracts, attribute/event schema |
| **Backend-Mediated (BFF/API)** | HTTP / GraphQL APIs | Low (frontend) | Async (network) | Centralized (server) | Backend-owned | Critical data flows, consistency, multi-device sync | Strong consistency, decoupled frontends | Latency, backend dependency | API versioning, SLA, schema governance |

## References

- https://en.wikipedia.org/wiki/Micro_frontend
- https://micro-frontends.org/