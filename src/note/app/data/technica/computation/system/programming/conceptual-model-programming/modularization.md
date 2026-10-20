---
tags: [task]
---

# Modularization


> In this note we will explore one of the principal activities in program design and implementation: modularization.
> 

> Abstraction is indeed the key of any modularization, and without modularization every hope of being able to guarantee reliability and correctness vanishes.
> 

## What is the nature of ‘program modularization’? It’s a Technique?  A Set of techniques? A Problem?

> **Program modularization** is the design process of partitioning a program into discrete computational units (modules) with well-defined responsibilities and interfaces.
> 

> It’s not a technique itself - but a type of process - that is a task.
> 

## What is a modular program? What is a un-modular program?

> A Modular Program is a program with structure ( see [‣](https://app.notion.com/p/15f598edb7908187a28bea3fc54ad64e?pvs=21) ) in which - the set of entities composing the program - are organized (decomposed) (structural organization) in a hierchical way (**hierchicy induced  by aggregation**)  - following simple interaction patterns - in different sub-pieces of sub-structures (large units).
> 

> A **modular program** is a program with **structure** (see [‣](https://app.notion.com/p/15f598edb7908187a28bea3fc54ad64e?pvs=21)). That is, the set of entities composing the program is **organized through hierarchical decomposition**, where the hierarchy is **induced by aggregation**. Another important element is the **pattern of interaction between computational units**, which should be **as minimal as possible**.
> 

> A un-modular program is a program is little structure - small units - not clear level - based form.
> 

> Note: This definition are basically for structure of the symbolic representation - not for the structure of the dynamics (computational process) that they generate.
> 

## What is the ‘value’ of modularization? Why make programs modular?

| **Engineering Objective** | **Property Induced by Modularization** | **Result** |
| --- | --- | --- |
| **Cognitive Tractability (Intelligibility)** | Decomposition of a large program into **bounded modules with coherent responsibilities**. | Developers can reason about the system **module-by-module**, dramatically reducing cognitive load when understanding or navigating the codebase. |
| **Local Reasoning** | **Encapsulation and information hiding** restrict access to internal implementation details. | Correctness and behavior can be analyzed by inspecting **a module and its interface**, without examining the entire program. |
| **Evolvability** | **Stable interfaces + replaceable implementations** allow internal changes without affecting dependents. | Systems can **adapt to new requirements** by modifying or replacing modules while preserving external contracts. |
| **Parallel Development** | Explicit **interface boundaries** partition the system into independently developable units. | Multiple teams or developers can **develop and test modules concurrently** with minimal coordination overhead. |
| **Change Facilitation (Change Isolation)** | **Dependency control and information hiding** limit the propagation of modifications. | Changes remain **localized**, reducing ripple effects across the codebase. |
| **Reuse** | Modules encapsulate **generalized functionality with well-defined interfaces**. | Functionality can be **reused across programs or systems**, reducing duplication and development time. |
| **Reliability** | Modules create **fault containment boundaries** and enable **independent testing**. | Errors can be **detected, isolated, and corrected** within individual modules, improving overall system robustness. |

## Which are the techniques used to make a program modular?

| **Category** | **Technique** | **Description** |
| --- | --- | --- |
| **Functional Decomposition** | **Procedural Decomposition** | Divide the program into procedures or functions, each responsible for a specific computational task. |
| **Responsibility Organization** | **Separation of Concerns** | Partition the program so that each module addresses a distinct concern or responsibility within the system. |
| **Encapsulation** | **Information Hiding** | Conceal internal implementation details of a module and expose only the necessary interface. |
| **Data Abstraction** | **Abstract Data Types (ADT)** | Organize modules around data structures and define operations that manipulate those structures. |
| **Interface Design** | **Interface Definition** | Define explicit module interfaces that specify the operations and data that other modules can access. |
| **Architectural Structuring** | **Layered Architecture** | Arrange modules in hierarchical layers where higher layers depend only on lower layers. |
| **Dependency Management** | **Dependency Inversion** | Depend on abstractions rather than concrete implementations, reducing tight coupling between modules. |
| **Object-Oriented Structuring** | **Encapsulation via Classes** | Use classes to bundle state and behavior into modular units with controlled access. |
| **Code Organization** | **Packages / Namespaces** | Group related modules into higher-level organizational units to manage complexity. |
| **Component Structuring** | **Componentization** | Construct modules as independently deployable or replaceable components with explicit interfaces. |

## How to evaluate different modular re-formulations of programs?

> Basically, we evaluate structural properties of the symbolic program, along with properties related to its evolution, modification dynamics, and dependency structure.
> 

| **Category** | **Metric** | **Description** |
| --- | --- | --- |
| **Internal Quality** | **Cohesion** | Measures how strongly the elements within a module belong together. High cohesion means the module implements a **single, well-defined responsibility**. |
| **Inter-Module Dependency** | **Coupling** | Measures the degree of dependency between modules. Lower coupling indicates that modules interact through **minimal and well-defined interfaces**. |
| **Interface Design** | **Interface Complexity** | Evaluates the size and complexity of a module’s public interface (number of functions, parameters, exposed types). Simpler interfaces are generally preferable. |
| **Dependency Structure** | **Dependency Directionality** | Evaluates whether dependencies follow a **clear architectural direction** (e.g., layered structure) rather than forming arbitrary links. |
| **Dependency Structure** | **Cyclic Dependencies** | Measures whether modules depend on each other in cycles. Good modular designs **avoid cycles**, enabling easier reasoning and independent evolution. |
| **Change Dynamics** | **Change Propagation** | Estimates how widely a modification in one module spreads to others. Better modularizations **limit ripple effects**. |
| **Comprehensibility** | **Module Size and Scope** | Evaluates whether modules are **small enough to understand**, but large enough to represent meaningful functionality. |
| **Reuse Potential** | **Reusability** | Measures whether modules are sufficiently **generic and decoupled** to be reused in other systems. |
| **Testability** | **Independent Testability** | Evaluates whether a module can be **tested in isolation**, using mocks or stubs for dependencies. |
| **System Robustness** | **Fault Isolation** | Measures the extent to which errors remain **contained within modules** rather than propagating throughout the system. |

## Which are the related tasks (objectives) (activities)?

| **Category** | **Task - Activity** | **Description** |
| --- | --- | --- |
| **Program Analysis** | **Responsibility Identification** | Determine the major responsibilities or functional concerns within the program. |
| **Program Analysis** | **Dependency Analysis** | Identify relationships between functions, data structures, and subsystems. |
| **Program Decomposition** | **Module Identification** | Partition the program into candidate modules that group related functionality. |
| **Program Decomposition** | **Responsibility Assignment** | Assign clear responsibilities to each module so that each unit performs a coherent role. |
| **Interface Design** | **Interface Definition** | Define the public operations and data exposed by each module. |
| **Interface Design** | **Information Hiding** | Decide which implementation details remain internal to the module. |
| **Dependency Control** | **Dependency Structuring** | Organize dependencies between modules (e.g., layering, hierarchical relations). |
| **Implementation** | **Module Construction** | Implement modules according to their defined responsibilities and interfaces. |
| **Verification** | **Interface Validation** | Verify that module interfaces are correct, minimal, and coherent. |
| **Verification** | **Independent Module Testing** | Test modules in isolation to verify correctness and robustness. |
| **Refinement** | **Modular Refactoring** | Improve the modular structure as the system evolves or requirements change. |
| **Maintenance** | **Impact Analysis** | Evaluate how modifications affect modules and their dependencies. |

## References

- https://news.ycombinator.com/item?id=39536437
- https://en.wikipedia.org/wiki/Modular_programming
- Bayer, Rudolf. "On program volume and program modularization." (1973).
- Parnas, David Lorge. "On the criteria to be used in decomposing systems into modules." *Communications of the ACM* 15.12 (1972): 1053-1058.
- Parnas, David Lorge, Paul C. Clements, and David M. Weiss. "The modular structure of complex systems." *IEEE Transactions on software Engineering* 3 (2006): 259-266.
- Sullivan, Kevin J., et al. "The structure and value of modularity in software design." *ACM SIGSOFT Software Engineering Notes* 26.5 (2001): 99-108.
- [Program](note.html?n=technica/computation/language-system/conceptual-model-language-system/program.md)
- [Abstraction](note.html?n=technica/computation/system/programming/conceptual-model-programming/abstraction.md)
- [Problem](https://app.notion.com/p/Problem-1e8c0f5171ec80e59848c3449661c09f?pvs=21)
- [Cohesion](note.html?n=technica/computation/system/programming/conceptual-model-programming/cohesion.md)
- [Coupling](note.html?n=technica/computation/system/programming/conceptual-model-programming/coupling.md)
- https://sidhion.com/blog/oberon_notes/
- [‣](https://app.notion.com/p/15f598edb7908187a28bea3fc54ad64e?pvs=21)