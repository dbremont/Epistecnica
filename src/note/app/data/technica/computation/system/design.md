# Design

> **Software Implementation Process**: The **Software Implementation Process** involves defining system requirements, designing the architecture and components, implementing the code, verifying functionality, evaluating performance and usability, deploying the system, and maintaining it through ongoing updates and adaptations.
> 

> **Five Big Stages**:  **Problem Analysis** → Problem Specification → System Design → System Implementation → **System Analysis → Operationalization.**
> 

> **System Specification**: Architectural Specification, Data Architecture Specification, Interface Design Specification, Component-Level Design Specification, Non-Functional Design Specification (Security, Performance),  Functional Specification.
> 

> **System Requirements**: **System requirements** refer to the set of specifications that define the necessary conditions, functions, and constraints a system must fulfill to meet the needs of users, stakeholders, and the environment in which it operates.
> 

> **Software Architecture**:  Software architecture is the high-level, formalized structure of a software system, defined by a set of **architectural components** $C$, their interactions $I$, constraints $\Phi$, and configuration $\Sigma$, where $C = \{c_1, c_2, ..., c_n\}$ represents computational elements, $I: C \times C \to M$ defines communication mappings over message space $M$, $\Phi$ encodes invariants such as consistency and security policies, and $\Sigma$ specifies deployment topology and runtime constraints.
> 

> **Software design** is the systematic specification of a software system's structural and behavioral organization, defined as a tuple $D = (C, I, M, P, \Phi)$, where $C$ is the set of **computational elements**, $I: C \times C \to \mathcal{F}$ defines inter-component interactions over a function space $\mathcal{F}$,  $M = (S, B, A)$ represents modular decomposition with subsystems $S$, boundaries $B$, and abstraction mechanisms $A$, $P$ encodes design patterns and architectural styles, and $\Phi$ defines constraints governing cohesion, coupling, concurrency, and non-functional requirements.
> 

> **Software Implementation**: **Software implementation** refers to the process of translating a software design or specification into a functional program by writing code, configuring systems, and integrating components.
> 

> **Computational System Analysis** refers to the systematic evaluation of the performance, behavior, and resource utilization of a computational system through mathematical modeling, algorithmic analysis, and empirical measurement, aimed at understanding and optimizing the efficiency, scalability, and reliability of the system under various operational conditions.
> 

> **Note**: System analysis focuses on evaluating the given system itself, not the problem analysis process. However, understanding the problem is essential at this stage, as it forms a crucial part of the overall system analysis.
> 

> **Principle:** A fundamental, abstract guideline that defines desirable properties or constraints in the design or implementation of a system, ensuring correctness, maintainability, and efficiency (e.g., modularity, encapsulation, separation of concerns).
> 

> **Technique:** A concrete, systematic method or approach applied to achieve a specific goal within a system’s design or implementation, often derived from principles and optimized for practical use (e.g., caching, indexing, load balancing).
> 

> Note: Must improve principles in software design  `Adaptability Structures`,   Compositionality, Reflection**,**  Lazy Evaluation (On-Demand Computation),  Constraint Propagation (Declarative Systems),  Interpretation,  Decomposition , Abstraction, Polymorphism,  Concurrency, Reactivity,   etc.
> 

> **Software design techniques** are systematic approaches and methods used to create and structure software systems, aiming to ensure efficiency, maintainability, scalability, and alignment with user requirements and technical constraints.
> 

> An **abstraction** is informally defined as a tool that solves a specific problem—either within a model of computation or related to the process being represented itself.
> 

> Note: For System  Space  -see in Miscellanea.
> 

![image.png](data/technica/computation/system/assets/design/image.png)

![image.png](data/technica/computation/system/assets/design/image-1.png)

QA:

- What is the difference between Software Architecture and Software Design? Architecture deals with higher-level design components called architectural components, while design deals with the computational elements per se.
- What are the **architectural components** of the System Architecture? How are this components model and represented?
- What are the **computational elements** involved in System Design? - Catalog of Computational Elements.
- What is a Software Specification?  What is a Model of a Software System?
- What is the relation between a **System Specification** and a **System Model**?
- What is the relation between real times systems vs online systems (algorithms, computations etc.)?
- How can cross-cutting concerns be effectively managed? (Aspectos Transversales)
- What are the limits of software adaptation?
- What are the criteria for evaluating a computational system design?

## Breviarium

> This is a comprehensive and integrative set of notes by nature, but we will focus only on **Design, Implementation,  System Analysis & Operationalization.**
> 

> *Computers are not mathematical abstractions—they’re physical systems with chaos.*
> 

> **Note: In these notes, we will not use the term "Design Pattern". Instead, we will use the more specific and technically and more general  term: "Programming Technique".**
> 

> Note: **Design techniques** and **implementation techniques** are deeply interconnected. Many language-agnostic techniques lean toward design, but some also apply at the implementation level. Rather than enforcing a rigid boundary, it's more practical to view them as a continuum.
> 

> See [Program](note.html?n=technica/computation/language-system/conceptual-model-language-system/program.md) and [Programming](note.html?n=technica/computation/system/programming.md).
> 

| **Concept** | **Definition** | **Scope/Level** | **Purpose/Role** | **Characteristics** | **Examples** |
| --- | --- | --- | --- | --- | --- |
| **Design Pattern (Design Idiom)** | A reusable, formalized solution template addressing a recurring design problem | Mid-level design structure | Provides a general blueprint for solving problems | Documented problem-solution structure, reusable | Singleton, Observer, Circuit Breaker |
| **Programming Idiom** | A conventional, language- or context-specific way to express or implement a design idea | Language/framework specific | Facilitates idiomatic, natural expression of solutions | Informal, pragmatic, culturally shared conventions | RAII in C++, Pythonic list comprehensions |
| **Technique** | A specific method or procedure applied to accomplish a particular task | Implementation level | Practical approach or procedure to implement a solution | Concrete, procedural, often low-level or tactical | Recursion, Memoization, Loop unrolling |
| **Architectural Style** | A high-level structural organization principle for entire systems | System or application-wide | Defines global system organization and interaction patterns | Broad scope, influences multiple components | Client-Server, Microservices, Event-Driven |
| **Algorithm** | A precise, finite sequence of well-defined instructions for solving a computational problem | Computational logic level | Provides step-by-step solution to a computational problem | Deterministic, mathematically defined, executable | Quicksort, Dijkstra’s algorithm |
| **Framework** | A reusable, semi-complete software environment providing generic functionality | Software platform | Supports development by providing common structure and components | Large-scale, extensible, often includes APIs | React.js, Spring Boot |
| **Design Principle** | Fundamental guideline or rule to guide system or software design decisions | Conceptual/Philosophical | Ensures good design qualities like maintainability or scalability | Abstract, normative, high-level | SOLID principles, DRY (Don’t Repeat Yourself) |
| **Pattern Language** | A structured collection of interrelated design patterns or idioms | Multi-level design | Provides comprehensive guidance for solving complex problems | Organized, hierarchical, systemic | Christopher Alexander’s Pattern Language |
| **Best Practice** | Established, proven technique or method accepted by a community or industry | Practical/Professional | Helps achieve quality and efficiency in design or implementation | Empirical, evolving, consensus-based | Code reviews, Continuous Integration |

## System Implementation Steps

> Note: There is not a particular order.
> 

> **System Implementation Note**: Market research and design are phases within Product Development, not System Implementation.
> 

> **Five Big Stages**:  **Problem** Analysis → Problem Specification → System Design → System Implementation → **System** Analysis & Evaluation → **Operationalization.**
> 

> Like a language that evolves with usage, adapting to new contexts and needs rather than being a static set of predefined rules.
> 

> **Minimal Viable Programs**: A [minimal viable program](https://joearms.github.io/#2014-06-25%20Minimal%20Viable%20Programs) is the smallest program that solves a particular problem. It is small and beautiful. It has no additional features.
> 

```
Problem Evolution:   P1 → P2 → P3 → P4 → P5 → ...
                              ↘     ↗     ↘     
System Evolution:    S1 → S2 → S3 → S4 → S5 → ...
```

- **System Requirements** → Define the high-level goals, functionalities, and constraints the software must meet.
- **Architectural Design** → Establish the system’s structure, components, and their interactions at a high level.
- **Detailed Design** → Specify the internal details of each component, including algorithms, data structures, and interfaces.
- **Implementation** → Write the code, integrate components, and build the system as per the design specifications.
- **Verification** → Conduct testing to ensure the system meets functional and non-functional requirements.
- **Performance Evaluation** → Assess the system’s performance, scalability, and resource efficiency under realistic conditions.
- **Usability Evaluation** → Measure the user experience, including interface design, ease of use, and accessibility.
- **Deployment** → Deploy the system into the production environment for end-user access.
- **Maintenance & Adaptation** → Continuously update, improve, and adapt the system based on user feedback and evolving requirements.
- **Operationalization: …**

## Design: System Architecture Specification

## Design: System Design (What)

> A **design technique** is a systematic method or approach used to create and develop solutions, structures, or artifacts by applying specific principles, tools, or processes to achieve desired objectives or solve particular problems.
> 

> A **design pattern** is a reusable solution to a common software design problem, providing a template for solving specific issues in a way that can be adapted to different scenarios.
> 

> **Programming Paradigms** = Models of Computation + Techniques !!!
> 

> **Fundamental Technique**:  Decomposition: Mix and Match Parts; Communication Trough clear Interfaces.
> 

> *The right decomposition reduces cognitive load and isolates failures.*
> 

> A **software design principle** is a fundamental guideline or rule that governs the organization, structure, and behavior of software components to ensure maintainability, scalability, flexibility, and performance, typically rooted in concepts such as modularity, abstraction, separation of concerns, and reusability.
> 

Fundamental Ideas:

| **Idea** | **What is it?** | **What problem does it solve?** | **Techniques used** |
| --- | --- | --- | --- |
| **Decomposition** | Dividing a complex system into smaller, manageable, and loosely coupled components. | Separation of Concerns,  | **Modular design**, **Microservices**, **Separation of layers** (e.g., UI, business logic, data access) |
| **Compositionality** | Building systems from smaller, reusable components that can be combined to form more complex systems. | Interaction | **Object-oriented programming (OOP)**, **Functional programming**, **Design patterns** (e.g., Adapter, Composite, Proxy) |
| **Adaptability (Flexibility)** | The ability of a system to adjust to changes, whether in requirements or environmental conditions. | Solves the problem of **change**—systems need to evolve with minimal impact on existing functionality. | **Configuration management**, **Plug-in architectures**, **Dependency injection**, **Design for extensibility** |
| **Abstraction** | Hiding the complex internal workings of a system while exposing only necessary interfaces or functionality. | Solves the problem of **complexity** by reducing the need for users or components to understand low-level details. | **Abstract data types (ADT)**, **Interfaces**, **API design**, **Encapsulation** |
| **Fault Tolerance & Robustness** | Designing systems to continue functioning correctly even in the face of component failure. | Solves the problem of **reliability**—ensuring systems remain operational despite failures. | **Replication**, **Error detection and correction**, **Failover**, **Redundant hardware** (RAID), **Idempotency, Redundancy** |
| **Scalability** | The ability of a system to handle increased load by adding resources without major changes to its architecture. | Solves the problem of **resource exhaustion**—as the demand increases, systems must be able to scale to meet the need without performance degradation. | **Load balancing**, **Sharding**, **Distributed databases**, **Horizontal scaling**, **Elastic cloud resources** |
| **Consistency** | Ensuring that all components of a system reflect the same state, especially in distributed settings. | Solves the problem of **data inconsistency**, where different parts of the system may have conflicting data. | **CAP theorem** (Consistency, Availability, Partition tolerance), **Quorum-based voting**, **Two-Phase Commit**, **Eventual consistency**, **Distributed transactions** |
| **Coordination** | Managing the communication and synchronization between distributed components to ensure that they work together coherently. | Solves the problem of **synchronization**—ensuring that actions in different parts of the system occur in a well-defined order. | **Locking** (distributed locks), **Paxos**, **Raft**, **Vector clocks**, **Consensus algorithms** |
| **Security** | Ensuring that the system is protected from unauthorized access, data breaches, and other malicious activities. | Solves the problem of **data integrity** and **privacy**—ensuring the system is resilient to attacks, and data is kept secure. | **Encryption** (AES, RSA), **Authentication** (OAuth, SSO), **Access control** (RBAC, ACLs), **TLS/SSL**, **Firewalls**, **Intrusion detection systems (IDS)** |

## System Implementation (How)

> A **computer program** is a description of a computation—a model of a real or mental process. It is represented as a discrete collection of symbols that evolve as our understanding improves, until it reaches a metastable state within another model: **satisfaction**. — Alan Perlis
> 

> Since large programs grow from smaller ones, we must develop an arsenal of standard **program structures (idioms)** - and **organizational techniques** to combine them into larger structures. - Alan Perlis
> 

> The work of a great **programmer** is to develop a working vocabulary to describe computations. - Guy L. Steele Jr.
> 

> **Pair programming** is a collaborative software development technique where two programmers work together at one workstation, with one writing code (the driver) while the other reviews each line of code as it is written (the observer or navigator).
> 

## Analysis: Evaluation Model

> 

## Analysis: System Analysis

> Monitoring, …
> 

## Documentation

> 

## **Operationalization**

> 

## Theory of Computational Systems

- Classical Computation
- Concurrency Theory
- Category Theory & Compositionality
- Control Theory (Cybernetics)
- Mechanism Design
- Formal Verification
- Type Theory
- Formal Methods

## Computational System Building Block

> 

| **📦 Category** | **🔧 Building Block** | **📝 Description** |
| --- | --- | --- |
| **♻️ Code Reuse** | 📚 **Libraries** | Reusable code modules offering specific functionality (e.g., NumPy, Lodash). |
|  | 🏗 **Frameworks** | Structured codebases that enforce architectural patterns (e.g., Django, React). |
| **🌐 External Integration** | 🔌 **External Services** | Third-party services accessed via APIs (e.g., Stripe, Firebase, AWS). |
| **⚙️ Execution Platform** | 🚀 **Runtime Environments** | Systems in which code executes (e.g., JVM, Python Interpreter, Node.js). |
| **🚢 Deployment Layer** | 📦 **Containers** | Isolated environments for packaging applications (e.g., Docker). |
|  | 🖥 **Virtual Machines** | Emulated hardware environments for system-level isolation. |
| **📡 Coordination** | 🧭 **Orchestration Tools** | Manage deployment, scaling, and automation (e.g., Kubernetes, Nomad). |
| **🔗 Communication** | 🌐 **Protocols & APIs** | Standards and interfaces for system interaction (e.g., HTTP, gRPC, REST). |
| **🗄 Persistence** | 🧮 **Databases** | Structured data storage and retrieval systems (e.g., PostgreSQL, MongoDB). |
|  | ⚡ **Caches** | Temporary, high-speed data stores (e.g., Redis, Memcached). |
| **📊 Observability** | 📈 **Logging & Monitoring** | Tools for tracking behavior and performance (e.g., Prometheus, ELK Stack). |
| **🔐 Security** | 🧑‍💼 **Identity & Access Control** | Auth systems and permissions (e.g., OAuth, JWT, Keycloak). |
| **⚙️ Configuration** | 🧾 **Environment Management** | Tools and conventions for system settings (e.g., dotenv, ConfigMaps). |

## Computational System Space

> See https://www.bremontix.xyz/lab/pro/Catalog/Good/Software/
> 

## Evaluation: Necessary & Sufficient Principle

> A small as possible; but not smaller.
> 

> Picard’s Principle:  "Make it possible to express what’s necessary, but impossible to express what’s incorrect.”.
> 

> Worse is better: Simplicity > Completeness. Incomplete but minimal solutions win.
> 

> Orthogonality: Ad-hoc methods that violate minimal orthogonality.
> 

> YAGNI (You Aren’t Gonna Need It): Avoid adding functionality until it’s absolutely necessary.
> 

> Occam’s Razor: Among competing hypotheses, the simplest one is most likely correct.
> 

> "Simplicity is the ultimate sophistication." — Leonardo da Vinci
> 

> "The best way to accomplish something is to subtract." — Rich Hickey (Clojure)
> 

> "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away." — Antoine de Saint-Exupéry
> 

> **"Minimum but complete"** - Captures the essence of necessary and sufficient
> 

> **"Just enough"** - No more, no less than what's required
> 

> **"Barely sufficient"** - The threshold of adequacy
> 

> **"Essential complexity only"** - Eliminating all accidental complexity
> 

> **"Nothing superfluous"** - Strict exclusion of non-essentials
> 

> **"Thin interface, deep implementation"** - Minimal surface area with robust internals
> 

> **"Zero feature creep"** - Aggressive resistance to unnecessary additions
> 

> **"Skeleton implementation"** - Just enough structure to be functional
> 

> **"Vanishing design"** - The system disappears into its purpose
> 

> **"Transparent abstraction"** - Minimal cognitive overhead
> 

**Practical Exercises to Achieve Minimalism**

1. **The 80/20 Rule**: Identify the 20% of features that deliver 80% of the value.
2. **Scratch Refactoring**: Rebuild a system from scratch using only what you *actually* need.
3. **Dependency Audit**: For each dependency, ask: *Could we build this ourselves in a day?*
4. **Feature Sunsetting**: Periodically remove features and see if anyone complains.

## Cohesion

> 

## Coupling

> 

## Modularity

> The art of decomposing a system into a set of sub-systems.
> 

> The art of decomposing a system into a set of modules.
> 

> High Cohesion and Low Coupling.
> 

> **Module**: In software engineering, the term "module" is often overused. It originates from the Latin *modulus*, meaning a "small measure" or "standard unit." Traditionally, it refers to a distinct, standardized part that can also be used for measurement. In software engineering, it typically refers to a collection of programming constructs designed to perform specific tasks or functions within a larger system.
> 

> Component: …
> 

> See [What is intelligibility?](https://app.notion.com/p/What-is-intelligibility-284c0f5171ec80ca98c0d8ad7df5c847?pvs=21).
> 

> Modularity is the art of transforming  a …
> 

## Extension / Adaptation Technique

> A **meta-pattern** where a **general computational or data structure** is defined with **intentionally incomplete (partial)  (**un-reifined**) parts**, allowing users to **extend or adapt (reified)**  it by providing concrete implementations. This generates a **finalized, executable (reified) structure** tailored to specific needs.
> 

> Partial Definition: The core structure is **partially abstract**, with "gaps" (hooks, placeholders, or abstract methods) that must be filled.
> 

> Reification: The adapted structure becomes fully computable after refinement.
> 

> Note: This is an extremely powerful general concept, alongside:;  along side with Compositionality, Reflection**,**  Lazy Evaluation (On-Demand Computation),  Constraint Propagation (Declarative Systems),  Interpretation,  Decomposition , Abstraction, Polymorphism,  Concurrency, Reactivity,   etc.
> 

> See more in
> 

Types:

- Basic Adaptation : Parameters / Declarative
- Behavior, …

Uses:

- Template Method,
- Strategy,
- Factory Method,
- Abstract Factory,
- Partial Evaluation,
- Decorator**,**
- Dependency Injection / Late Binding

Computer System Design: Conceptual Model

## References

- [Operating System](note.html?n=technica/computation/operating-system.md)
- [Design](note.html?n=technica/computation/system/design.md)
- [Operation](note.html?n=technica/computation/system/operation.md)
- [Telecom](note.html?n=technica/computation/telecom.md)
- [‣](https://app.notion.com/p/57a6a0bb4bec4f7590dd95f4076ecdf2?pvs=21)
- [Verification](note.html?n=technica/computation/dependability/verification.md)
- [Data System](note.html?n=technica/computation/data-system.md)
- [Concurrency](note.html?n=technica/computation/concurrency.md)
- [Security](https://app.notion.com/p/Security-abe7b617157f43099a19bee382dd5996?pvs=21)
- [Representation](note.html?n=technica/computation/representation.md)
- [Agentic System](https://app.notion.com/p/Agentic-System-1b5c0f5171ec802db3b2f70081ecaf6a?pvs=21)
- [Language System](note.html?n=technica/computation/language-system.md)
- [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md)
- https://plato.stanford.edu/entries/mereology/
- [UI](note.html?n=technica/computation/system/interface/ui.md)
- [Cloud Computing System](note.html?n=technica/computation/platform/cloud-computing-system.md)
- [Distributed Computing](note.html?n=technica/computation/distributed-computing.md)
- [**A Guide to Improving Computational Systems in a Principled Way**](https://app.notion.com/p/A-Guide-to-Improving-Computational-Systems-in-a-Principled-Way-1bec0f5171ec808fb56ffd094de27a12?pvs=21)
- [‣](https://app.notion.com/p/10e598edb790812486ddf8943b946a96?pvs=21)
- [‣](https://app.notion.com/p/10e598edb790814f9020d6a74a0829c7?pvs=21)
- https://github.com/dbremont/system-design-labs
- [Decision Table Patterns (2020)](https://news.ycombinator.com/item?id=38822319) ([hillelwayne.com](http://hillelwayne.com/))
- [system-design](https://github.com/karanpratapsingh/system-design)
    - [System Design Primer](https://github.com/donnemartin/system-design-primer)
    - [ByteByteGo Newsletter](https://blog.bytebytego.com/)
    - [The Twelve-Factor App](https://12factor.net/es/)
    - [The mythical 10x programmer](http://antirez.com/news/112)
    - [System Design The Big Archive](https://drive.google.com/file/d/1AmdZZI7GNdb_a5itXqULjGPa1p33CIoC/view?usp=drive_link)
    - [From design patterns to category theory](https://blog.ploeh.dk/2017/10/04/from-design-patterns-to-category-theory/)
    - [System Design Blueprint: The Ultimate Guide](https://drive.google.com/file/d/1oF9VEJ-DRCAHDwzrijxQMLv7xJbC8Tx-/view?usp=drive_link)
    - [What we talk about when we talk about System Design](https://maheshba.bitbucket.io/blog/2023/07/12/Design.html)
    - Notes on Structured Programming (1970) [pdf] ([utexas.edu](http://utexas.edu/))
    - Estimating Software Projects: So you messed up. Now what?
    [https://news.ycombinator.com/item?id=39678057](https://news.ycombinator.com/item?id=39678057)
-     - [Three Laws of Software Complexity (or: [why software engineers are always grumpy)]](https://maheshba.bitbucket.io/blog/2024/05/08/2024-ThreeLaws.html)
    - …
- [Hints and Principles for Computer System Design](https://www.microsoft.com/en-us/research/uploads/prod/2019/09/Hints-and-Principles-v1-full.pdf)
- [Programming Principles](https://github.com/webpro/programming-principles)
- https://www.turing.com/blog/principles-of-software-development-guide
- https://maheshba.bitbucket.io/blog/2024/05/08/2024-ThreeLaws.html
- https://en.wikipedia.org/wiki/Software_metric
- https://github.com/karanpratapsingh/system-design
- https://github.com/yzr95924/storage_paper_list
- https://www.cs.otago.ac.nz/cosc345/resources/nasa-10-rules.htm
- https://news.ycombinator.com/item?id=43267095
- https://newsletter.systemdesignclassroom.com/
- https://github.com/dbremont/system-design-labs
- [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md)
- https://www.seangoedecke.com/good-system-design/
- https://github.com/rrweb-io/rrweb