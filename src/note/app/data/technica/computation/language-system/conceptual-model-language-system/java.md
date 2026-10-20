---
tags: [java, language]
---

# Java

- [Java HotSpot Virtual Machine](note.html?n=technica/computation/language-system/conceptual-model-language-system/java-hotspot-virtual-machine.md)

> **Java** is a high-level, object-oriented programming language designed to be platform-independent, enabling developers to write code that can run on any device with a compatible **Java Virtual Machine (JVM)**.
> 

> **(Dubitatio Praecipua)** To truly master a programming language, one must understand its semantics (highly useful) and ideally have a deeper understanding of the execution machine (less likely). Given this **epistemic uncertainty**, how would you approach describing computations?
> 

QA:

- How are implementation-defined behaviors documented (e.g., file paths, system calls, or hardware dependencies)?
- How does the specification handle backward-incompatible changes (e.g., Python’s `2.x` → `3.x` transition)?
- (Java) What is finally block?
- (Java) What is exception propagation?
- (Java) What is the semantics of the keyword final?
- (Java) When does a final block fail to execute?
- (Java) What is the purpose of the finalize() method?
- How the Java **`Agent premain`**  system works?
- What naming format is used for classes in source code? What naming format is used for classes in bytecode?
- What naming conventions are typically used for classes in:  source code (,java)  and Bytecode  (.class) files)?"
- How does Java's type erasure mechanism impact method overloading and polymorphism in generic classes? Can you give a legal-looking program that fails due to erasure?
- What does it mean to "capture a wildcard" in Java generics? How is this used in methods that accept List<?> as input?
- Why are arrays covariant and generics invariant in Java? What are the risks or justifications from the JLS perspective?
- How does the compiler infer types in chained generic method calls like map().filter().collect()? What are the limitations of this inference?
- Under what circumstances does Java allow variable shadowing? How does the JLS differentiate between shadowing, hiding, and overriding?
- How does the compiler resolve ambiguous names in the presence of static imports and inner classes?
- How are scopes and lifetimes defined for variables captured by local classes? What about anonymous classes?
- What are the "happens-before" relationships defined in the JMM? Give a case where lack of synchronization causes visibility problems between threads.
- Why are final fields treated specially in the JMM? What guarantees do they provide even without synchronization?
- What are the semantic differences between a volatile field and a synchronized block? What happens to instruction reordering in each case?
- What is the JLS rule for definite assignment, and how does it affect variable usage in try-finally blocks?
- What does the JLS say about unreachable code? Give an example where the compiler accepts code that is logically unreachable.
- Why can't a method declare it throws a more general exception than one actually thrown in the implementation?
- How does the JVM determine the order of static initializer execution across a class hierarchy?
- What causes a ClassCircularityError, and how does the JVM detect it according to the JLS?
- What are the exact rules the JLS gives for binary compatibility when replacing one version of a class with another?
- What does the strictfp modifier do? In what cases is floating-point behavior affected?
- How to reason about DB Connection, DB  Connection Pools, etc.? https://github.com/dbremont/data-system-labs

Todo:

- StringBuilder:  This both a time and space optimization vs (+ operator); this understanding the internals.
- How string are represented?
- Update Template.
- ServiceLoader → [https://docs.oracle.com/javase/8/docs/api/java/util/ServiceLoader.html](https://docs.oracle.com/javase/8/docs/api/java/util/ServiceLoader.html)
- Java Keytool:  keytool -list -v -keystore /home/dvictoriano/.sdkman/candidates/java/current/lib/security/cacerts -storepass changeit
- Jav Public Key - Tooling:  `keytool -list -v -keystore /home/dvictoriano/.sdkman/candidates/java/current/lib/security/cacerts -storepass changeit`.
- https://keystore-explorer.org/index.html
- ….

## 🏗️ Model of Computation

> What are the models of computation that  the language supports? See more in [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md).
> 

| **Programming Model** | **Description** |
| --- | --- |
| **Imperative Programming Model** | Java supports traditional procedural programming with variables, control structures, and methods. |
| **Object-Oriented Programming (OOP) Model** | Java emphasizes using objects and classes to represent data and behavior, supporting encapsulation, inheritance, and polymorphism. |
| **Functional Programming Model** | Java incorporates functional programming concepts such as lambda expressions and streams for a declarative style. |
| **Event-Driven Programming Model** | Java supports event-driven programming for GUIs and event listeners, enabling responsive user interactions. |
| **Parallel Programming Model** | Java facilitates parallel programming through its support for threads and concurrency. |
| **Distributed Programming Model** | Java supports distributed programming with remote method invocation (RMI) and networking APIs. |

## 📜 Language Specification

> The Language Specification precisely defines the rules for **Lexical Grammar** (token formation and character sets), **Syntactic Grammar** (structure, ambiguities, operator precedence), **binding** (associating names with values and constructs), **Scoping Rules** (name visibility and lifetime), and **Semantics** (the meaning of expressions, statements, and program behavior), establishing the formal foundation for how programs are written, interpreted, and executed.
> 

Java: 📜 Language Specification

## **🏷️**Type System

> The Language Specification precisely defines the rules for **Lexical Grammar** (token formation and character sets), **Syntactic Grammar** (structure, ambiguities, operator precedence), **binding** (associating names with values and constructs), **Scoping Rules** (name visibility and lifetime), and **Semantics** (the meaning of expressions, statements, and program behavior), establishing the formal foundation for how programs are written, interpreted, and executed.
> 

Java: **🏷️** Type System

## 📚 The Standard Library

> ¿Which are the basic functionality provided?
> 

> The Standard Library provides a comprehensive collection of pre-built modules, functions, and data structures that offer essential utilities and abstractions—such as collections, I/O, concurrency, and networking—serving as a foundational toolkit that enables developers to efficiently build robust and portable applications without reinventing common functionality.
> 

Java: 📚 Standard Library

## **🔀** Representation

> This note delves into the multifaceted concept of **representation** within language systems, covering critical aspects such as **code representation**, **data structures**, **memory layout**, **execution state**, **resource handles**, and related runtime elements. Understanding how these components are represented and managed at various stages—from high-level source constructs down to low-level machine artifacts—provides deep insights into the design, capabilities, and constraints of a programming language and its execution environment.
> 

> By examining representation along a continuum from **higher-level abstractions** (e.g., source code and data models) to **lower-level concrete implementations** (e.g., memory organization and processor state), we conceptually reduce dimensionality and complexity. This stratified approach facilitates clearer reasoning and more effective analysis of a language’s expressive power, runtime efficiency, safety guarantees, and extensibility.
> 

> Studying representation in this layered fashion is a powerful method for dissecting language systems because it highlights the interplay between language semantics and system architecture, illuminating both strengths and potential limitations inherent in the language’s design and implementation.
> 

**Java:  🔀** Representation

## **🧩** Modularization

> What are the **primitives of modularization**?
> 

> Code organizational mechanisms refer to strategies and structures used to manage, modularize, and maintain code in a way that promotes clarity, efficiency, and scalability throughout the software development process.
> 

Java: **🧩** Modularization

## **🔄 Computation Flow Primitive**

> See more in [Concurrency](note.html?n=technica/computation/concurrency.md) and [Notion of Change](note.html?n=technica/computation/language-system/conceptual-model-language-system/notion-of-change.md).
> 

> Instruction Stream:   What is the execution path?
> 

> Conditionals, pattern matching, loops, exception handling, continuations, parallelism, concurrency, event system?
> 

> A concurrency **model** is a structured stream of instructions that encode and regulate the creation, transfer, transformation, and termination of units of value within a system. Each unit of currency carries, implicitly or explicitly, a sequence of operations that affect economic state.
> 

Java: **🔄 Computation Flow Primitive**

## **✨**Metaprogramming

> ¿Can we compute over the **description of computation**? ¿Can code be treated like data?
> 

Java: **✨** Metaprogramming

## ⚙️ Execution System

> A **Language Execution System (LES)** is the set of tools, algorithms, and runtime mechanisms that **execute a program** represented by a given **encoding scheme** (e.g., source code, bytecode, machine code). It defines how a program's **semantics** are realized on a computational substrate (hardware, VM, or interpreter) through a series of **transformations** and **runtime behaviors**.
> 

Java: 🚀 Execution System

## **🔗 Interoperability**

> Which type of **Interoperability  Mechanisms  does this Language Supports?**
> 

Java: **🔗Interoperability**

## 💻 Language System Interface

> The **Language System Interface** encompasses the collection of mechanisms, APIs, and tooling hooks that enable interaction with both the **compile-time** and **runtime** aspects of a programming language system. These interfaces serve as critical access points for developers, compilers, debuggers, profilers, and other tools to analyze, transform, observe, or extend the behavior of programs.
> 

> By exposing internal structures—such as syntax trees, type information, bytecode, runtime metadata, and execution state—the language system interface facilitates tasks ranging from static analysis and metaprogramming to runtime instrumentation and debugging. Studying these interfaces reveals how a language system supports extensibility, introspection, tooling integration, and control over program behavior, making them essential for advanced language engineering and systems programming.
> 

Java: 💻 Language System Interface

## ⚡Performance

> How does the **computational model's** implementation impact performance?
> 

> What are the key factors in programming language **`X`** that influence the execution speed and overall efficiency of programs?
> 

> How does the language's mapping to **`hardware`** (e.g., CPU, memory, I/O) affect application performance?
> 

> What performance impact do the language's built-in data structures have on memory usage and **`execution time`**?
> 

Java: ⚡Performance

## 🛠️ Tooling & Ecosystem

> What tools does the language provide?
> 

> List of implementations of the language.
> 

Java: 🛠️ Tooling & Ecosystem

## `🎭` Miscellanea

> Language Security,  Special Features, Portability, Documentation,  Debugging Support (Interoperability, Ecosystem),  Metadata (Compiler, …),  Intrinsics, …
> 

Java: `🎭` Miscelanea

## 🔗 References

- [**Process**](note.html?n=technica/computation/language-system/conceptual-model-language-system/process.md)
- [Concurrency](note.html?n=technica/computation/concurrency.md)
- [Language System](note.html?n=technica/computation/language-system.md)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- Library & Non Components:
    - https://github.com/dbremont/system-design-labs
    - https://github.com/dbremont/language-system-labs
- https://github.com/dbremont/distributed-system-lab/tree/main
- https://github.com/dbremont/java-analyst-labs
    - https://visualvm.github.io/download.html
- [JDK 21](https://openjdk.org/projects/jdk/21/)
- [Java 21: what’s new?](https://www.loicmathieu.fr/wordpress/en/informatique/java-21-quoi-de-neuf/)
- https://github.com/deephacks/awesome-jvm
- Bloch, J. (2005). Java puzzlers : traps, pitfalls, and corner cases. Addison-Wesley.
- Gosling, J. (2005). The Java language specification. Addison-Wesley.
- Bloch, J. (2018). Effective Java. Addison-Wesley.
- Goetz, B. (2006). Java concurrency in practice. Addison-Wesley.
- Lea, D. (2000). Concurrent programming in Java : design principles and patterns. Addison-Wesley.
- Evans, B. (2018). Optimizing Java : practical techniques for improving JVM application performance. O’Reilly.
- Evans, B. J., Gough, J., Newland, C. (2018). Optimizing Java. O’Reilly Media.
- [Java Almanac](https://javaalmanac.io/bytecode/versions/)
- [Java Versions](https://en.wikipedia.org/wiki/Java_version_history)
- [Java Best Practices](http://java.jonathangiles.net/)
- [SEI CERT Oracle Coding Standard for Java](https://wiki.sei.cmu.edu/confluence/display/java/SEI+CERT+Oracle+Coding+Standard+for+Java)
- https://jenkov.com/tutorials/java-concurrency/java-memory-model.html
- https://en.wikipedia.org/wiki/Java_(programming_language)
- [A Guide to Study Programming Language](https://app.notion.com/p/A-Guide-to-Study-Programming-Language-5a6ed523a0a94f619061f4051dcca041?pvs=21)
- https://javaalmanac.io/