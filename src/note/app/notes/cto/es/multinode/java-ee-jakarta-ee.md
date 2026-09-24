# Java EE (Jakarta EE)

> ...

## Formulation

### What technical element type does this technical instance belong to?

**Jakarta EE belongs to the `Technical Standard` technical element type — a set of specs.**

More specifically:

```text
Technical Standard
└── Jakarta EE (umbrella standard — set of member specs)
```

Jakarta EE is a standard because it is a normative specification governing form, function, interoperability, and behavior of enterprise Java artifacts. It is itself a set: member specs (Servlet, JPA, CDI, …) are nested standards grouped in families (Web Tier, Persistence, …). An implementation (e.g. Weld, Hibernate) *implements* a spec; a compatible server (e.g. WildFly, Payara, Tomcat with extensions) *realizes* the set. As a coherent body of standards + objects + techniques + institutions it can also be read as a `Technical Element Set`; the Standard typing is kept primary here.

### What is this technical instance?

> Jakarta EE is a specification-driven, enterprise-grade Java platform instance defining a set of standardized APIs, runtime environments, and container-managed services for building distributed, scalable, and transactional applications — implemented by providers (Hibernate, Weld, RESTEasy, Mojarra, …) and realized by compatible application/web servers (WildFly, Payara, GlassFish, Open Liberty, Tomcat with EE extensions).

### What is the recursive instance decomposition of this technical instance?

> Boundary: this table decomposes the Jakarta EE standard set — member specs under Specification (spec documents, API surfaces, standard-enabled practices), plus conformance control, governance, and realizing servers; vendor implementations are documented in the Implementation matrix below, not here. Deployment-specific values appear only in rows marked exemplar.
>
> Stopping rule: a row is terminal when it names a concrete spec document version, a `jakarta.*` API package, a TCK result, a config file, or a named server distribution.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a compatible server *realizes* the standard set.

| Instance Tree Path | Description | Technical Category | Technical Element Type Tree Path |
|---|---|---|---|
| **Jakarta EE** | Umbrella standard: set of enterprise Java specs + their API surfaces and realizing servers (vendor implementations live in the Implementation matrix below, not in this decomposition). | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification | The member-specification set: all Jakarta EE member specs grouped by family. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Coherence (portable application architecture) | Organizing structure: portable enterprise applications via standard APIs + container-managed services (DI, transactions, security, concurrency). | System Structure | `(root) > Technical Architecture` |
| Jakarta EE > Realized capability | Capability realized: distributed, scalable, transactional component-based applications on compatible servers. | Mechanism & Capability | `(root) > Technical Capability` |
| Jakarta EE > Governance (Eclipse Foundation stewardship) | Eclipse Foundation stewardship of the spec set; JCP heritage; compatibility/TCK process. | Knowledge & Methodology | `(root) > Technical Element Set > Knowledge & Methodology > Technical Institution` |
| Jakarta EE > Specification > Web Tier | Nested standard group for HTTP/web presentation. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Web Tier > Jakarta Servlet | Core HTTP request/response programming model and lifecycle. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Web Tier > Jakarta Servlet > `jakarta.servlet` API | Defined boundary through which web components exchange requests/responses. | System Structure | `(root) > Technical Interface` |
| Jakarta EE > Specification > Web Tier > Jakarta Faces (JSF) | Component-based UI framework for server-rendered interfaces (skeleton row; see Faces section below). | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Web Services | Nested standard group for REST/SOAP/JSON interop. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Web Services > Jakarta REST (JAX-RS) | Standard API for RESTful HTTP services. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Web Services > Jakarta REST (JAX-RS) > `jakarta.ws.rs` API | Interface boundary for resources, providers, filters. | System Structure | `(root) > Technical Interface` |
| Jakarta EE > Specification > Persistence | Nested standard group for data access. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Persistence > Jakarta Persistence (JPA) | Standard ORM API for entity-based relational mapping. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Persistence > Jakarta Persistence (JPA) > `jakarta.persistence` API | Interface boundary (entities, `EntityManager`, JPQL). | System Structure | `(root) > Technical Interface` |
| Jakarta EE > Specification > Enterprise Integration | Nested standard group for messaging/batch/mail/concurrency. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Enterprise Integration > Jakarta Messaging (JMS) | Messaging standard for async, reliable, decoupled communication. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Enterprise Integration > Jakarta Messaging (JMS) > `jakarta.jms` API | Interface boundary for queues, topics, listeners. | System Structure | `(root) > Technical Interface` |
| Jakarta EE > Specification > Business Logic | Nested standard group for transactional components and injection. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Business Logic > Jakarta Enterprise Beans (EJB) | Component model for transactional, secure, distributed logic. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Business Logic > Jakarta Enterprise Beans (EJB) > `jakarta.ejb` API | Interface boundary (session/message-driven beans, timers). | System Structure | `(root) > Technical Interface` |
| Jakarta EE > Specification > Business Logic > Jakarta CDI | Context-aware dependency injection with scopes, lifecycle, events. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Business Logic > Jakarta CDI > `jakarta.enterprise` + `jakarta.inject` API | Interface boundary for beans, scopes, events, interceptors. | System Structure | `(root) > Technical Interface` |
| Jakarta EE > Specification > Business Logic > Dependency injection practice | Repeatable pattern: constructor/field injection, scopes, producers applied by agents across projects. | Technique | `(root) > Technical Practice` |
| Jakarta EE > Specification > Security | Nested standard group for authN/authZ and identity integration. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Security > Jakarta Security | Standardized authentication, authorization, identity-store integration. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Security > Declarative security practice | Repeatable pattern: annotations + roles + identity stores enforced by the container. | Technique | `(root) > Technical Practice` |
| Jakarta EE > Specification > Transaction Management | Nested standard group for distributed transaction coordination. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Transaction Management > Jakarta Transactions (JTA) | Standard for demarcating and coordinating distributed transactions. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Transaction Management > Jakarta Transactions (JTA) > `jakarta.transaction` API | Interface boundary (`UserTransaction`, XA enlistment). | System Structure | `(root) > Technical Interface` |
| Jakarta EE > Specification > Transaction Management > Transaction coordination mechanism | Arrangement through which atomic commit/rollback across resources is produced. | Mechanism & Capability | `(root) > Technical Mechanism` |
| Jakarta EE > Specification > Configuration & Naming | Nested standard group for metadata, injection contracts, lookup. | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Specification > Validation & MVC | Nested standard group: Bean Validation (constraints) + MVC (optional action-based framework). | Requirements & Definition | `(root) > Technical Standard` |
| Jakarta EE > Compatibility (TCK) | Conformance evaluation deciding whether an implementation/server may claim compatibility. | Technical Control | `(root) > Verification Type` |
| Jakarta EE > Compatibility (TCK) > Technology Compatibility Kit (TCK) | The executable test suite, harness, and documentation artifacts against which implementations and servers are certified; passing it licenses a compatibility claim. | System Structure | `(root) > Constitutive Technical Object` |
| Jakarta EE > Evolution javax-to-jakarta | Historical rename `javax.*` → `jakarta.*` (EE 8 → 9) after the 2017 Eclipse transfer; platform versions 8/9/10/11. | Lifecycle & Continuity | `(root) > Technical Evolution` |
| Jakarta EE > Realizing servers | Compatible servers realizing the standard set (links only; decomposed in their own notes). | System Structure | `(root) > Production Technical System` |
| Jakarta EE > Realizing servers > WildFly | Full-profile production system realizing EJB/JMS/JCA and the core set. | System Structure | `(root) > Production Technical System` |
| Jakarta EE > Realizing servers > Payara/GlassFish/Open Liberty | Compatible production systems realizing the set (profiles vary). | System Structure | `(root) > Production Technical System` |
| Jakarta EE > Realizing servers > Tomcat (+ EE extensions) | Servlet-container production object realizing the web subset; full EE only with added impls (Mojarra, Weld, Hibernate Validator). | System Structure | `(root) > Production Technical Object` |

## Specification Set

> Java EE (Jakarta EE) is a specification-driven, enterprise-grade Java platform that defines a set of standardized APIs, runtime environments, and container-managed services for building distributed, scalable, and transactional applications, leveraging a component-based architecture with servlets, JSP, JSF, CDI, EJB, JPA, JMS, JTA, and web services (REST and SOAP) while enforcing dependency injection, declarative security, and multi-threaded request processing within managed execution environments such as application servers (e.g., WildFly, Payara, or **Tomcat with EE extensions**).


| **Category**               | **Specification**                                   | **Description**                                                                                         | **Implementation Set**             |
| -------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **Web Tier**               | **Jakarta Servlet**                                 | Defines the core HTTP request/response programming model and lifecycle for web applications.            | Apache Tomcat / Jetty              |
|                            | **Jakarta Server Pages (JSP)**                      | Provides a server-side view technology for generating dynamic HTML using Java and tag libraries.        | Jasper                             |
|                            | **Jakarta Faces (JSF)**                             | Component-based UI framework for building server-rendered web user interfaces.                          | Mojarra / MyFaces                  |
|                            | **Jakarta Expression Language (EL)**                | Unified expression language for accessing and manipulating application data in web views and templates. | Eclipse EL                         |
| **Web Services**           | **Jakarta RESTful Web Services (JAX-RS)**           | Defines a standard API for building RESTful HTTP-based services.                                        | RESTEasy / Jersey / CXF            |
|                            | **Jakarta XML Web Services (JAX-WS)**               | Defines APIs and annotations for SOAP-based web services.                                               | Metro / CXF                        |
|                            | **Jakarta JSON Processing (JSON-P)**                | Low-level streaming and object-model APIs for parsing and generating JSON.                              | Eclipse JSON-P                     |
|                            | **Jakarta JSON Binding (JSON-B)**                   | High-level API for mapping Java objects to and from JSON representations.                               | Eclipse Yasson                     |
| **Persistence**            | **Jakarta Persistence (JPA)**                       | Standard ORM API for managing relational data using entity-based object mapping.                        | Hibernate / EclipseLink            |
|                            | **Jakarta Data**                                    | Repository-style abstraction for simplified and declarative data access (1.0, Jakarta EE 11).                | Eclipse JNoSQL 1.1.4 / Hibernate 6.6   |
| **Enterprise Integration** | **Jakarta Messaging (JMS)**                         | Messaging API for asynchronous, reliable, and decoupled communication between components.               | Apache ActiveMQ / Artemis          |
|                            | **Jakarta Batch**                                   | Defines a job-oriented model for offline, bulk, and long-running batch processing.                      | Eclipse Batch                      |
|                            | **Jakarta Mail**                                    | APIs for composing, sending, and receiving email messages.                                              | Eclipse Angus                      |
|                            | **Jakarta Concurrency**                             | Managed concurrency utilities for executing asynchronous and scheduled tasks in containers.             | Eclipse Concurrency                |
| **Business Logic**         | **Jakarta Enterprise Beans (EJB)**                  | Component model for transactional, secure, and distributed business logic.                              | OpenEJB / WildFly EJB              |
|                            | **Jakarta CDI (Contexts and Dependency Injection)** | Context-aware dependency injection framework with scopes, lifecycle management, and events.             | Weld / OpenWebBeans                |
|                            | **Jakarta Interceptors**                            | Mechanism for implementing cross-cutting concerns (logging, security, metrics) via interception.        | Provided by CDI implementation     |
| **Security**               | **Jakarta Security**                                | Standardized APIs for authentication, authorization, and identity management integration.               | Soteria                            |
| **Transaction Management** | **Jakarta Transactions (JTA)**                      | Defines APIs for demarcating and coordinating distributed transactions.                                 | Narayana / Geronimo                |
|                            | **Jakarta Connectors (JCA)**                        | Architecture for integrating Jakarta EE applications with external enterprise information systems.      | IronJacamar                        |
| **Configuration & Naming** | **Jakarta Annotations**                             | Common annotations used across Jakarta EE for declarative configuration and metadata.                   | Eclipse Annotations                |
|                            | **Jakarta Dependency Injection (DI)**               | Base dependency injection contract defining injection points and resolution semantics.                  | Integrated with CDI                |
|                            | **Jakarta Naming (JNDI)**                           | Naming and directory API for binding and looking up resources in a hierarchical namespace.              | Container-provided                 |
|                            | **Jakarta Config**                                  | Externalized configuration API for applications and runtimes.                                           | SmallRye Config                    |
| **Web & MVC (Optional)**   | **Jakarta MVC**                                     | Action-based MVC framework layered on top of JAX-RS for server-side web applications.                   | Ozark                              |
| **Validation**             | **Jakarta Bean Validation**                         | Declarative validation framework using constraints and annotations to enforce data integrity.           | Hibernate Validator                |

## Implementation

### Which servers realize the specifications?

> Support Levels reflect this note's sourced rows — not official certification (certification lives with the TCK process and the jakarta.ee compatibility listings). `*` marks levels limited by unsourced rows rather than proven absence: an empty pivot cell means unsourced, never incapable.

| Java EE Implementor (Server) | Description | Support Level |
|---|---|---|
| WildFly | Modular full-profile application server; decomposed in the WildFly note. | Full Platform |
| JBoss EAP | Hardened, commercially supported WildFly derivative. | Full Platform |
| Payara Server | Full-platform server from the GlassFish lineage. | Full Platform |
| GlassFish | Eclipse reference implementation server. | Full Platform |
| Open Liberty | Feature-based runtime; profiles composed per deployment. | Web Profile* |
| TomEE | Tomcat base with OpenEJB/OpenWebBeans/ActiveMQ additions. | Web Profile* |
| Apache Tomcat | Servlet container with JSP/EL support. | Servlet Container |
| Jetty | Servlet container. | Servlet Container |

### Which implementations realize each specification on each server?

> Pivot of the Implementation Sets in the Specification Set above, with the WildFly column refined from the WildFly note's subsystem table (hence Undertow/EJB3/Elytron instead of the shared defaults). Empty cell = unsupported on that server or not yet sourced — never a claim. Server columns are ordered most-complete-first. Open Liberty and GlassFish are omitted from this pivot (see the server table for their support levels); their sourced cells matched the shared defaults. Server profiles vary (see WildFly/Tomcat notes).

| Category | Specification | WildFly | JBoss EAP | Payara | TomEE | Tomcat | Jetty |
|---|---|---|---|---|---|---|---|
| **Web Tier** | Jakarta Servlet | Undertow | Undertow |  | Tomcat (native) | Tomcat (native) | Jetty (native) |
|  | Jakarta Server Pages (JSP) | Undertow JSP | Undertow JSP |  | Jasper | Jasper | Jasper |
|  | Jakarta Faces (JSF) | Mojarra | Mojarra |  | MyFaces |  |  |
|  | Jakarta Expression Language (EL) | Eclipse EL | Eclipse EL | Eclipse EL | Eclipse EL | Eclipse EL |  |
| **Web Services** | Jakarta REST (JAX-RS) | RESTEasy | RESTEasy |  |  |  |  |
|  | Jakarta XML Web Services (JAX-WS) | CXF | CXF |  |  |  |  |
|  | Jakarta JSON Processing (JSON-P) | RESTEasy JSON-P Provider | RESTEasy JSON-P Provider | Eclipse JSON-P |  |  |  |
|  | Jakarta JSON Binding (JSON-B) | RESTEasy JSON-B Provider | RESTEasy JSON-B Provider | Yasson |  |  |  |
| **Persistence** | Jakarta Persistence (JPA) | Hibernate | Hibernate |  |  |  |  |
|  | Jakarta Data |  |  |  |  |  |  |
| **Enterprise Integration** | Jakarta Messaging (JMS) | Artemis | Artemis |  | ActiveMQ |  |  |
|  | Jakarta Batch | JBeret | JBeret |  |  |  |  |
|  | Jakarta Mail | Mail Session | Mail Session | Angus |  |  |  |
|  | Jakarta Concurrency | Managed Executor | Managed Executor | Eclipse Concurrency |  |  |  |
| **Business Logic** | Jakarta Enterprise Beans (EJB) | EJB3 | EJB3 |  | OpenEJB |  |  |
|  | Jakarta CDI | Weld | Weld |  | OpenWebBeans |  |  |
|  | Jakarta Dependency Injection | Weld | Weld |  | OpenWebBeans |  |  |
|  | Jakarta Interceptors | Weld / EJB3 | Weld / EJB3 |  |  |  |  |
| **Security** | Jakarta Security | Soteria via Elytron | Soteria via Elytron | Soteria |  |  |  |
| **Transaction Management** | Jakarta Transactions (JTA) | Narayana | Narayana |  |  |  |  |
|  | Jakarta Connectors (JCA) | IronJacamar | IronJacamar |  |  |  |  |
| **Configuration & Naming** | Jakarta Annotations | Eclipse Annotations | Eclipse Annotations | Eclipse Annotations |  | Eclipse Annotations |  |
|  | Jakarta Naming (JNDI) | JNDI Namespace | JNDI Namespace | Container-provided |  | Container-provided |  |
|  | Jakarta Config | SmallRye Config | SmallRye Config | SmallRye Config |  |  |  |
| **Web & MVC** | Jakarta MVC | Ozark |  | Ozark |  |  |  |
| **Validation** | Jakarta Bean Validation | Hibernate Validator | Hibernate Validator | Hibernate Validator |  | Hibernate Validator |  |

## Evolution

> Java EE (1999, Sun) → Java EE 5–8 under JCP → 2017 transfer to Eclipse Foundation → Jakarta EE 8 (same as Java EE 8) → Jakarta EE 9 (namespace rename `javax.*` → `jakarta.*`) → 9.1/10/11 (profiles: Platform, Web, Core). Each step keeps the spec → implementation → realization chain: specs versioned, implementations re-certified via TCK, servers re-released per profile.

## **Jakarta Faces**

> aka. Java Server Faces.
> 

QA:

- How events are handle?
- How data binding works?
- How partial updates works?
- What is the execution model?
- How `DemuxCompositeELResolver` works?
- What is the different between `Jakarta EE Server` vs `Application Server`?

Phases:

- com.sun.faces.lifecycle.RestoreViewPhase@4793eed2
- com.sun.faces.lifecycle.ApplyRequestValuesPhase@4f2666db
- com.sun.faces.lifecycle.ProcessValidationsPhase@382e51f1
- com.sun.faces.lifecycle.UpdateModelValuesPhase@26a93b9b
- com.sun.faces.lifecycle.InvokeApplicationPhase@7e14a4e2 -> Use dr.gov.esigef.pds.presentacion.nucleo.evento.EventoEjecutadoCambioValor@42185d63
- com.sun.faces.lifecycle.RenderResponsePhase@2f80545

Expression Language (EL):

- Unified EL resolves `#{bean.prop}` against CDI-managed beans via the container EL resolver chain (see `DemuxCompositeELResolver` question above); values set during Update-Model-Values, rendered during Render-Response.

## QA

- How does WildFly determine which **JSP** file to serve for a given **URL**, and where must the **JSP** be located inside the **WAR**?

## References

- [weld/core](https://github.com/weld/core)
- [Jakarta EE (Wikipedia)](https://en.wikipedia.org/wiki/Jakarta_EE)
- [Jakarta Faces 3.0 jsdoc — jsf.ajax](https://jakarta.ee/specifications/faces/3.0/jsdoc/jsf.ajax.html)
- [What exactly is Java EE? (Stack Overflow)](https://stackoverflow.com/questions/7295096/what-exactly-is-java-ee)
- [Jakarta EE Specifications](https://jakarta.ee/specifications/)
- [Jakarta Data 1.0](https://jakarta.ee/specifications/data/1.0/)
- [CDI TCK](https://jakartaee.github.io/cdi-tck/)
- [distributed-system-lab](https://github.com/dbremont/distributed-system-lab)
- [Java: Modularization](https://righteous-guardian-68f.notion.site/Java-Modularization-210c0f5171ec809b8108ee6acba4db9c?source=copy_link)
- [What is the difference between application server and web server?](https://stackoverflow.com/questions/936197/what-is-the-difference-between-application-server-and-web-server?rq=3)

- [Apache Tomcat](note.html?n=cto/es/multinode/apache-tomcat.md)
- [Wildfly](note.html?n=cto/es/multinode/wildfly.md)
