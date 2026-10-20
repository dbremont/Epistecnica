---
tags: [technique]
---

# Indirection

- [Technique](note.html?n=technica/computation/system/programming/conceptual-model-programming/technique.md), [Abstraction](note.html?n=technica/computation/system/programming/conceptual-model-programming/abstraction.md)

> In computer science, **indirection refers** to the technique of accessing data or resources through an intermediate layer, reference, or identifier rather than directly. It involves using a **"pointer"** or **"reference"** to locate the actual target, creating an indirect path to the desired information. This concept is foundational in programming, data structures, and system design.
> 

> At its core, indirection is about programming against virtual entities—representing concretions; this very simple idea has tremendous consequences.
> 

## Meta

> Evaluation Framework.
> 

### **✅** Evaluation

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

> See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21) & [](https://app.notion.com/p/250c0f5171ec8010a8d3caa5d0a1266e?pvs=21)
> 

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | … |
| **Completeness** | … |
| **Coherence & Structure** | … |
| **Epistemic Self-Assessment** | … |
| **Should I Reorganize This -in My Content Forest?** |  |
| **What’s my study Strategy? Should I Change It?** |  |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | What is the deepest essence? |
| **Evidentia (Evidence) 📊** | What proofs, data, or logical arguments support it? How can its claims or performance be verified? |
| **Telos (Intent) 🎯** | What is it for? Toward what end is it directed? What tools does it offer, if any? What outcomes does it aim to achieve? |
| **Gnosis (Understanding) 🧠** | How to grow a **mental represented** (compress, fluid,  hierarchical (depth, abstraction), meta-awareness, flexibility, minimal sensitivity, well-connected) that capture this topic both its declarative aspects and procedural aspects?  How can we develop an **explicit representation & organization** of this topic that supports the growth of a strong **mental representation**? What **previous structure**  must be in place in order to make the growth of the new representation feasible? |
| **Epignosis (Application) 🛠️** | How is this knowledge applied in practice? What advanced skills or insights emerge from mastery? What real-world problems does it solve? |
| **Relatio (Connections) 🔗** | How does this topic relate to other subjects or fields? What are the interdisciplinary connections? |
| **Idoneitas (Suitability) 📐** | How effectively does it achieve its purpose? What metrics prove its value? |
| **Limites (Limits) ⛔** | What are its boundaries? What constraints define its operation? |
| **Contextus (Context) 🌍** | What is the historical, cultural, or situational context in which this study occurs? |
| **Dynamis (Evolution) 🌱** | How might it transform? What emerging influences could redefine it? |
| **Critica (Critique) 🔍** | What are the common criticisms or challenges associated with this topic? How have these been addressed or debated? |
| **Verbum Usus (Language Use) 🗣️** | How is the word/concept used in language and discourse? What are the typical semantic, pragmatic, and stylistic patterns surrounding its use? How do people’s usage contexts, connotations, and variations influence understanding? What shifts or trends in language use reflect its evolving meaning or social significance? |

### 🧠 Mental Representation

> How should we think about x?
> 

> See more in [How do different **mental representations** of the same RepTarget impact performance?](https://app.notion.com/p/How-do-different-mental-representations-of-the-same-RepTarget-impact-performance-24ac0f5171ec80dbaea5cc0e93f7647e?pvs=21).
> 

## Why Indirection?

| **Core Impact** | **Description** | **Example(s)** |
| --- | --- | --- |
| **Decoupling** | Separates identity from implementation or location, enabling modularity. | Variable name `counter` vs. memory address. |
| **Abstraction** | Hides complexity behind references or interfaces. | APIs, polymorphic objects. |
| **Flexibility** | Allows substituting, extending, or redirecting behavior without breaking clients. | Function pointer tables, dependency injection. |
| **Control** | Inserts governance over access, enabling checks, security, or mediation. | File handles in OS kernels. |
| **Sharing & Reuse** | Allows multiple entities to point to and reuse the same resource. | Symbol tables, shared caches. |
| **Scalability** | Supports hierarchical or layered mappings that grow with system size. | DNS, distributed systems identifiers. |
| **Cognitive Leverage** | Enables humans to think symbolically instead of mechanically. | Using variable names instead of raw memory addresses. |

## How Indirection?

| Category | Technique | Description | Example(s) |
| --- | --- | --- | --- |
| **Memory (Pointers)** | Pointer / Reference | Store the address of a value or object instead of the value itself. | C/C++ pointers, Java references, smart pointers. |
|  | Indirect Memory Access | Access memory through a level of indirection (tables, offsets). | Page tables in virtual memory, segment:offset addressing. |
| **Functions (Behavior)** | Function / Method Tables | Use a table of functions or callbacks to select behavior at runtime. | C++ vtables, function pointer arrays, dispatch tables. |
|  | Higher-Order Function Defunctionalization | Replace higher-order functions with first-order equivalents. | Functional programming transformations. |
|  | Late Binding / Dynamic Linking | Resolve references to functions or modules at runtime. | DLLs, shared libraries, plugin systems. |
| **Abstraction (Interfaces)** | Interface / Abstract Class | Hide concrete implementation behind a reference type. | Java interfaces, C# abstract classes. |
|  | Replace Conditional with Polymorphism | Swap complex conditionals for polymorphic objects. | Strategy pattern, polymorphic dispatch. |
| **Handles (Identifiers)** | Handle / Opaque Reference | Provide symbolic or opaque references instead of direct access. | File handles, database connection IDs, GPU resource handles. |
|  | Names / Symbols | Map symbolic names to actual resources. | DNS (domain names → IPs), symbolic links in file systems. |
|  | Parameter Object | Encapsulate multiple related parameters into an object. | Method calls with complex argument sets. |
| **Data (Mapping)** | Mapping Table / Lookup Table | Use an intermediate mapping from one identifier to another. | Symbol tables in compilers, routing tables, address translation. |
|  | Indirection via Arrays / Hashes | Access data indirectly via indices or keys. | Arrays of pointers, hash maps. |
| **Control (Safety)** | Access Control Layer | Interpose a reference layer to enforce rules or constraints. | File handles, memory protection via OS, capability-based security. |
|  | Proxy / Wrapper | Insert an intermediary to monitor, cache, or modify requests. | Remote proxies, API wrappers, decorators. |
| **Resource Sharing (Reuse)** | Shared Reference / Reference Counting | Multiple clients refer to the same resource through indirection. | Shared pointers, reference-counted objects, caches. |
| **Virtualization (Decoupling)** | Virtual Memory | Decouple logical addresses from physical memory. | Paging, segmentation. |
|  | Virtual Machines / Containers | Decouple software from underlying hardware. | JVM, Docker containers. |
|  | Namespaces | Decouple names from actual entities to allow multiple contexts. | Linux namespaces, package/module systems. |
| **Networking (Distributed Systems)** | Layered Indirection | Use multiple mapping layers to reach the final resource. | DNS (name → IP → route → server), load balancers, distributed hash tables. |
|  | Logical IDs / Indirection Layer | Separate logical identity from physical location. | Node IDs in distributed systems, consistent hashing, Kubernetes services. |
| **Cognitive (Design)** | Symbolic Reference | Allow humans to reason about objects symbolically instead of concretely. | Variable names vs memory addresses, symbolic constants. |
|  | Extract Method / Variable | Refactor code to introduce a layer of indirection for clarity. | Methods extracted from large functions, variables for complex expressions. |
|  | Dependency Injection | Inject references to dependencies instead of concrete instances. | Spring Framework DI, .NET Core DI containers. |

## Trade-off Model

| **Aspect** | **Benefit** | **Cost (Trade-off)** | **Example(s)** |
| --- | --- | --- | --- |
| **Flexibility & Adaptability** | Allows runtime behavior changes, supports dynamic features | Extra lookup steps, potential performance overhead | Function pointers, late binding, plugin systems |
| **Separation of Concerns** | Keeps modules independent, easier to reason about | Adds layers that may obscure flow | APIs, abstract classes, virtual methods |
| **Maintainability & Extensibility** | Simplifies adding or modifying functionality | Can complicate debugging and tracing | Extract method/variable, interface extraction, refactoring |
| **Reduced Coupling** | Components depend on abstractions, not concrete implementations | Indirection layers may introduce slight overhead | Dependency injection, polymorphic dispatch |
| **Polymorphism & Dynamic Behavior** | Supports multiple implementations and late resolution | Performance cost of indirection; harder to follow code path | Object-oriented polymorphism, strategy pattern |
| **Easier Testing / Dependency Injection** | Allows swapping real objects with mocks or stubs | Requires extra setup; adds indirection complexity | DI containers, mock objects, test doubles |
| **Resource Sharing / Reuse** | Centralized resources, avoids duplication | Risk of unintended side-effects | Shared pointers, symbol tables, caches |
| **Scalability** | Layered mappings help manage large systems | Complexity increases with more layers | DNS, virtual memory, distributed system IDs |
| **Cognitive Leverage** | Enables symbolic reasoning and abstraction | Too many layers can confuse | Variable names vs memory addresses, symbolic constants |

## ❓ QA

### Can all forms of abstraction be reduced to indirection?

> Technically yes,  the relationship holds, but in computer science, it's crucial to
distinguish between the two concepts: indirection serves as a specific technique for realizing abstractions, whereas abstraction itself represents a broader, foundational technique & principle.
> 

## References

- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- 
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [](https://app.notion.com/p/245c0f5171ec80749daec722e73b8a81?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- [](https://app.notion.com/p/24ac0f5171ec8020aec7f11bae9eb632?pvs=21)
- https://en.wikipedia.org/wiki/Indirection