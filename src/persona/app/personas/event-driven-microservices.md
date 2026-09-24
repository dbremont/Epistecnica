---
type: architecture
tags: [event-driven, microservices]
---

# Event-Driven Microservices

> An architecture entry: a system decomposed into autonomous services that communicate through an event log rather than synchronous calls.

## Formulation

### What is this architecture?

> A set of independently deployable services, each owning its data, coordinated through published domain events carried by a durable log. Services react to events; no service calls another synchronously in the steady state.

### What does it trade off?

> Coupling for latency and complexity: producers never block on consumers, but delivery becomes at-least-once, ordering becomes partial, and debugging requires tracing across the log. Schema evolution of events is the load-bearing discipline.

## References

- [Designing Event-Driven Systems (Ben Stopford, O'Reilly)](https://www.oreilly.com/library/view/designing-event-driven-systems/9781492038252/)
