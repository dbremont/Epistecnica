---
tags: [language]
---

# Erlang


> Erlang is a concurrent, functional programming language designed for building scalable and fault-tolerant systems, often used in telecommunications and distributed computing.
> 

> **Language characterization** is the process of analyzing and  describing a programming language's key features—like its syntax rules,  how code executes, type checking behavior, memory management, and  supported programming styles—to understand its strengths, limitations,  and best use cases.
> 

## 🧮 Model of Computation

> What are the models of computation that  the language supports? See more in [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md).
> 

## 📜 Language Specification

> The Language Specification precisely defines the rules for **Lexical Grammar** (token formation and character sets), **Syntactic Grammar** (structure, ambiguities, operator precedence), **binding** (associating names with values and constructs), **Scoping Rules** (name visibility and lifetime), and **Semantics** (the meaning of expressions, statements, and program behavior), establishing the formal foundation for how programs are written, interpreted, and executed.
> 

Erlang: 📜 Language Specification

## **🏷️**Type System

> The Type System defines how a language classifies, checks, and enforces types—covering static vs. dynamic typing, polymorphism, type inference, subtyping models, type safety, advanced features like union or dependent types, and runtime behaviors such as type erasure or reflection—establishing the formal rules for how values and operations are typed and validated throughout program execution.
> 

Erlang: **🏷️** Type System

## 📚 The Standard Library

> The **Standard Library** provides a comprehensive collection of pre-built modules, functions, and data structures that offer essential utilities and abstractions—such as collections, I/O, concurrency, and networking—serving as a foundational toolkit that enables developers to efficiently build robust and portable applications without reinventing common functionality.
> 

Erlang: 📚 Standard Library

## **🔀** Representation

> This note delves into the multifaceted concept of **representation** within language systems, covering critical aspects such as **code representation**, **data structures**, **memory layout**, **execution state**, **resource handles**, and related runtime elements. Understanding how these components are represented and managed at various stages—from high-level source constructs down to low-level machine artifacts—provides deep insights into the design, capabilities, and constraints of a programming language and its execution environment.
> 

> By examining representation along a continuum from **higher-level abstractions** (e.g., source code and data models) to **lower-level concrete implementations** (e.g., memory organization and processor state), we conceptually reduce dimensionality and complexity. This stratified approach facilitates clearer reasoning and more effective analysis of a language’s expressive power, runtime efficiency, safety guarantees, and extensibility.
> 

> Studying representation in this layered fashion is a powerful method for dissecting language systems because it highlights the interplay between language semantics and system architecture, illuminating both strengths and potential limitations inherent in the language’s design and implementation.
> 

Erlang**:  🔀** Representation

## **🧩** Modularization

> **Code organizational mechanisms** refer to strategies and structures used to manage, modularize, and maintain code in a way that promotes clarity, efficiency, and scalability throughout the software development process.
> 

Erlang: **🧩**Modularization

## **🔄 Computation Flow Primitive**

> This note explores the concurrency model, parallelism, error handling, and control flow mechanisms of the language system.
> 

> A **concurrency model** specifies how multiple **instruction streams** (or threads of execution) interact, overlap, and affect shared state over time, often nondeterministically. It defines the rules governing the execution, synchronization, visibility, and ordering of instructions when multiple agents (threads, processes, actors) are active concurrently.
> 

Erlang: **🔄 Computation Flow Primitive**

## **✨**Metaprogramming

> This note explore the  metaprogramming mechanisms provided by this language.
> 

> ¿Can we compute over the **description of computation**? ¿Can code be treated like data?
> 

Erlang**: ✨**Metaprogramming

## ⚙️ Execution System

> A **Language Execution System (LES)** is the set of tools, algorithms, and runtime mechanisms that **execute a program** represented by a given **encoding scheme** (e.g., source code, bytecode, machine code). It defines how a program's **semantics** are realized on a computational substrate (hardware, VM, or interpreter) through a series of **transformations** and **runtime behaviors**.
> 

> Related: [**🔀** Representation](https://app.notion.com/p/Representation-3722a849ef3140db9df1b0a6654d29b2?pvs=21).
> 

Erlang: ⚙️ Execution System

## **🔗 Interoperability**

> Which type of **Interoperability  Mechanisms  does this Language Supports?**
> 

Erlang: **🔗Interoperability**

## 💻 Language System Interface

> The **Language System Interface** encompasses the collection of mechanisms, APIs, and tooling hooks that enable interaction with both the **compile-time** and **runtime** aspects of a programming language system. These interfaces serve as critical access points for developers, compilers, debuggers, profilers, and other tools to analyze, transform, observe, or extend the behavior of programs.
> 

> By exposing internal structures—such as syntax trees, type information, bytecode, runtime metadata, and execution state—the language system interface facilitates tasks ranging from static analysis and metaprogramming to runtime instrumentation and debugging. Studying these interfaces reveals how a language system supports extensibility, introspection, tooling integration, and control over program behavior, making them essential for advanced language engineering and systems programming.
> 

Erlang: 💻 Language System Interface

## ⚡Performance

> How does the **computational model's** implementation impact performance?
> 

> What are the key factors in programming language **`X`** that influence the execution speed and overall efficiency of programs?
> 

> How does the language's mapping to **`hardware`** (e.g., CPU, memory, I/O) affect application performance?
> 

> What performance impact do the language's built-in data structures have on memory usage and **`execution time`**?
> 

Erlang: ⚡Performance

## 🛠️ Tooling & Ecosystem

> What tools does the language provide?
> 

> List of implementations of the language.
> 

Erlang: 🛠️ Tooling & Ecosystem

## `🎭` Miscellanea

> Language Security,  Special Features, Portability, Documentation,  Debugging Support (Interoperability, Ecosystem),  Metadata (Compiler, …),  Intrinsic, …
> 

## 🔗 References

- [Erlang (programming language)](https://en.wikipedia.org/wiki/Erlang_(programming_language))
- [Learn You Some Erlang](https://learnyousomeerlang.com/content)
- [My favorite Erlang Program](https://joearms.github.io/published/2013-11-21-My-favorite-erlang-program.html)
- [Erlang/OTP 25.3](https://www.erlang.org/doc/index.html)
- [The Erlang BEAM Virtual Machine Specification](http://www.cs-lab.org/historical_beam_instruction_set.html)
- [Why I program in Erlang (2012) (evanmiller.org)](https://news.ycombinator.com/item?id=33426041)
- [The Erlang Runtime System](https://blog.stenmans.org/theBeamBook/)
- [Robert Virding - Hitchhiker’s Tour of the BEAM](https://www.youtube.com/watch?v=_Pwlvy3zz9M)
- [Everything you need to know to start contributing to Erlang today!](https://medium.com/erlang-battleground/all-you-need-to-know-to-start-contributing-to-erlang-2fcd5748319e)
- [Erlang Engine Tuning: know Your Engine The Beam](https://www.erlang-factory.com/upload/presentations/817/EngineTuningII_Beam.pdf)
- [Type Specifications and Erlang](https://learnyousomeerlang.com/dialyzer)
- [Erlang/OTP](https://github.com/erlang/otp)
- [erlang-is-not-about](https://github.com/stevana/armstrong-distributed-systems/blob/main/docs/erlang-is-not-about.md)
- [Erlang’s not about lightweight processes and message passing (github.com/stevana)](https://news.ycombinator.com/item?id=34545061)
- [A Gentle Introduction to Core Erlang: Part 1](https://baha.github.io/intro-core-erlang-1/)
- [Erlang/OTP: Garbage Collector (medium.com/erlang-battleground](https://news.ycombinator.com/item?id=35385952)
- [More Optimizations in the Compiler and JIT](https://www.erlang.org/blog/more-optimizations/) - [Comments](https://news.ycombinator.com/item?id=35625656)
- Armstrong, Joe. "A history of Erlang." Proceedings of the third ACM SIGPLAN conference on History of programming languages. 2007.
- Armstrong, Joe. "Erlang—a Survey of the Language and its Industrial Applications." Proc. INAP. Vol. 96. 1996.
- Armstrong, Joe. "A history of Erlang." Proceedings of the third ACM SIGPLAN conference on History of programming languages. 2007.
- [BEAM File Format](https://beam-wisdoms.clau.se/indepth-beam-file.html)
- [The BEAM Book](https://blog.stenmans.org/theBeamBook/#BEAM_files)
- https://github.com/drobakowski/awesome-erlang
- [A Guide to Study Programming Language](https://app.notion.com/p/A-Guide-to-Study-Programming-Language-5a6ed523a0a94f619061f4051dcca041?pvs=21)
- [Concurrency](note.html?n=technica/computation/concurrency.md)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [Language System](note.html?n=technica/computation/language-system.md)
- https://github.com/csiglab/language-system-labs