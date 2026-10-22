# Computacion

> Problems → Technologies.
> 

> **Computer Science** is the study of **computers** and **computational systems**, focusing on algorithms, data structures, software design, and the theoretical and practical aspects of processing information and solving problems through computational means.
> 

> **Computation** is the process of performing mathematical, logical, or data-processing operations using algorithms and hardware to solve problems or perform tasks.
> 

> **Programming** is the process of **reifying** a **mental model of a computational process** into a symbolic expression within a given programming language.
> 

> **Software Engineering** is the discipline of **constructing large computational systems** through the composition and organization of smaller computational descriptions, with complexity management as its central concern.
> 

> **ML** deals with **intractable computational problems** by developing models that learn patterns from data and make predictions or decisions without explicit programming.
> 

> **Programming**: A General human activity, to mean the act of extending or chancing a systems’s functionality.`
> 

> Note: The terms ***computation*** and ***description of computation*** are not synonymous. However, the term “computation” is often used to refer both to the process itself and to its descriptive representation (i.e., the formal system or language used to specify it). This ambiguity should be handled carefully, as it can create unnecessary linguistic confusion or misleading conceptual impressions even when the underlying distinction is clear. Take the case principle to organize computation - we don’t organize a computation (most of the time - except in computation interaction - let’s say in multi node  - process system, scheduler, etc) - we organize it’s description.
> 

> How to integrate ML Driven Computation with Symbolic Driven Computations?
> 

![**Computation** is the **evolution** of states under a governing **dynamic law**.](../assets/note/technica/computation/computacion/image.png)

**Computation** is the **evolution** of states under a governing **dynamic law**.

![Programming: Computational Mental Model ↔ Concrete Reification in a Given Language System. ](../assets/note/technica/computation/computacion/image-1.png)

Programming: Computational Mental Model ↔ Concrete Reification in a Given Language System. 

## Guide

> Note: Since the breadth and depth of these notes are vast, it is useful to develop a set of guides as an entry point.
> 
- [ ]  Systems,  Libraries and  Tools will  be **preferably** analyzed in  https://github.com/dbremont/system-design-labs,  https://github.com/dbremont/language-system-labs and https://github.com/dbremont/tecno-miscellanea-labs.

### Cross-Cutting Concerns

> Regardless of domain, any study of **computational systems** must account for concerns that cut across abstraction layers and architectural boundaries. These are ***non-functional*** requirements that influence design, implementation, and evaluation.
> 

- [ ]  **Security** – How can we ensure that systems are robust against unauthorized access, tampering, and exploitation across their lifecycle?
- [ ]  **Performance** – How efficiently does the system utilize available computational resources (e.g., CPU, memory, I/O) under real workloads?
- [ ]  **Correctness** – Does the system behave as intended under all expected (and unexpected) inputs? How can this be specified, verified, and validated?
- [ ]  **Scalability** – Can the system maintain its functionality and performance as demands (e.g., users, data size, distributed nodes) increase?
- [ ]  **Maintainability** – How easily can the system be understood, adapted, debugged, or extended over time?
- [ ]  **Usability** – How effectively can human users interact with the system? Are feedback, error handling, and affordances adequate?
- [ ]  **Observability** – Can internal system behavior be inspected via logs, metrics, and traces to support debugging and understanding?
- [ ]  **Resilience** – How does the system respond to faults, unexpected inputs, partial failures, or degraded environments?
- [ ]  **Portability** – Can the system operate across different environments (e.g., OSes, hardware, cloud platforms) with minimal changes?

### Study Guide

> As you study computer science, don’t limit yourself to just the mathematical foundations—concepts like computability, decidability, and asymptotic complexity are intellectually stimulating, but they only tell part of the story. Make sure to also invest deeply in the physical realities of computing: energy costs of computation, data locality, parallelism, and computer architecture. These are the domains where real power and performance are unlocked. Balance theory with systems—one sharpens the mind, the other builds capability.
> 

## A Reflection on Hardware-Software

> Explore the fundamental relationship between hardware and software. How much of a robotic system is hardware versus software? What defines a hardware problem versus a software problem? Which issues are a mix of both, and how can they be identified?
> 

## A Reflection on the Processes → Mental Model ↔ Problem Relationship

> These questions capture **key aspects of efficient thinking and problem-solving** in computer science and mathematics.
> 
- How easy is it to translate a **mental model** of a process **into a program** within a given model of computation?
- How easy is it to translate a **program** in a given model of computation into a **mental model** of a process?
- How easy is it to capture a given process as a mental model?

## Central Dogma

> The central dogma of computer science is **“Model of Computation | Representation + Computation = Information Processing.”** This means that information processing is achieved through representing information in a structured way and performing computations on those representations.
> 

> Representation refers to how information is encoded or structured in a computer system, such as in binary form or other formats. Computation manipulates that information through various algorithms, data structures, and logical operations.
> 

## A New Kind of System

> **Note:** **Computational systems** may be better understood by analogy to cognitive systems, which function as adaptive, embodied software architectures. Both involve symbolic encoding, internal dynamics, and interaction with an environment, though they differ in implementation (formal vs. biological) and flexibility (programmed vs. emergent).
> 

> A **computational system** consists of a programmable control architecture (*logical core*) and a mechanical or digital substrate (*actuator layer*) that executes its directives. This decoupling of control and structure marks a departure from earlier systems—biological or mechanical—where control and execution were co-located and structurally indivisible, leading to limited adaptability.
> 

> This is somewhat analogous to **Cartesian Dualism**—a philosophical view in which the **mind** (*res cogitans*) and the **body** (*res extensa*) are fundamentally distinct substances: the former non-material and mental, the latter material and physical.
> 

> **Note**: Cartesian Dualism oversimplifies biological systems. In living organisms, the 'software' (e.g., behavior, cognition, control mechanisms) is shaped by and embedded within the 'hardware' (e.g., neural tissue, body morphology), and the two are tightly intertwined and co-evolving. There is no strict separation—structure and function mutually influence one another at all levels.
> 

## Fundamental Notion

> See [Computation](https://app.notion.com/p/Computation-1c8c0f5171ec8074a6fbe931c2102aec?pvs=21).
> 

## Topics

[System](note.html?n=technica/computation/system.md)

[Platform](note.html?n=technica/computation/platform.md)

[Telecom](note.html?n=technica/computation/telecom.md)

[Algorithm](note.html?n=technica/computation/algorithm.md)

Miscelanea

[Concurrency](note.html?n=technica/computation/concurrency.md)

[Data System](note.html?n=technica/computation/data-system.md)

[Specification](note.html?n=technica/computation/specification.md)

[Dependability](note.html?n=technica/computation/dependability.md)

[Representation](note.html?n=technica/computation/representation.md)

[Problem Space](note.html?n=technica/computation/problem-space.md)

[Operating System](note.html?n=technica/computation/operating-system.md)

[Language System](note.html?n=technica/computation/language-system.md)

[Data Visualization](note.html?n=technica/computation/data-visualization.md)

[Product Development](note.html?n=technica/computation/product-development.md)

[Distributed Computing](note.html?n=technica/computation/distributed-computing.md)

[Quantum Computation](note.html?n=technica/computation/quantum-computation.md)

[**Computational Complexity Theory**](note.html?n=technica/computation/computational-complexity-theory.md)

[**Enterprise Information System (EIS)**](note.html?n=technica/computation/enterprise-information-system-eis.md)

## References

- [Dev Docs](https://devdocs.io/)
- https://github.com/dbremont/configs
- [Compiler Explorer](https://godbolt.org/)
- https://github.com/oxnr/awesome-bigdata
- [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)
- [Open-source alternatives](https://opensource.builders/)
- https://github.com/madd86/awesome-system-design
- [IT Tools - Handy tools for developers](https://it-tools.tech/)
- https://www.bremontix.xyz/lab/pro/Production/Industry/Software/
- Exploring Object File Formats ([maskray.me](http://maskray.me/))
[https://news.ycombinator.com/item?id=3899891](https://news.ycombinator.com/item?id=38998914)
- AI Infrastructure Landscape (ai-infra.fun)
[https://news.ycombinator.com/item?id=39508950](https://news.ycombinator.com/item?id=39508950)
- [Restack - Run Your Favorite Open Source Products](https://www.restack.io/)
- TinyML: Ultra-low power Machine Learning ([ikkaro.net](http://ikkaro.net/))
[https://news.ycombinator.com/item?id=39014866](https://news.ycombinator.com/item?id=39014866)
- https://www.cs.utexas.edu/~EWD/transcriptions/EWD08xx/EWD854.html
- https://www.thoughtworks.com/radar
- https://www.uxdesigninstitute.com/blog/the-top-8-ai-tools-for-ux/
- [‣](https://app.notion.com/p/a193a8e1f23548b3a9181177c3079296?pvs=21)
- [A Guide on the Use of Algebra in Computer Science](https://app.notion.com/p/A-Guide-on-the-Use-of-Algebra-in-Computer-Science-1b9c0f5171ec809c9ea7d0424b462960?pvs=21)
- https://holdenlee.github.io/What%20I%20learned%20from%20Patrick%20Winston.html
- [A General Set of Programming Tips](https://app.notion.com/p/A-General-Set-of-Programming-Tips-1c2c0f5171ec80e89de7d94c23e143b3?pvs=21)
- [A Guide to Thinking Deeply About Software Systems — Especially Complex Ones](https://app.notion.com/p/A-Guide-to-Thinking-Deeply-About-Software-Systems-Especially-Complex-Ones-203c0f5171ec800ea048e41bf35179f3?pvs=21)

[Graphical, Heterogeneous, High-Performance Computing System](note.html?n=technica/computation/graphical-heterogeneous-high-performance-computing-system.md)