---
tags: [language-system]
---

# Language System

> In this note, we conduct a comprehensive exploration of models of computation, programming paradigms, meta-linguistic and linguistic abstractions, languages, and language systems—focusing on **representing processes** by a **program** that produce computations and on **designing frameworks** (language systems) that support the expression of those processes.
> 

> **Computation** is the process of performing mathematical, logical, or data-processing operations using algorithms and hardware to solve problems or perform tasks.
> 

> **Meta Linguistic Abstractions: Abstractions that form the foundational layer beneath linguistic abstractions, enabling the construction and structuring of language-level constructs.**
> 

> Programming Paradigm:  **Programming Paradigm:** A programming paradigm is a fundamental style or approach to programming that shapes how problems are conceptualized and how solutions are expressed. It defines the structure, patterns, and techniques used in writing and organizing code.
> 

> Language:  A programming language is a formal system comprising a well-defined syntax and semantics that enables the specification of algorithms and computational processes through symbolic expressions, which are parsed, analyzed, and translated by language processors into executable instructions for a target computational model or machine.
> 

> **Linguistic Abstraction** refers to how a programming language allows developers to express computations at a high level, abstracting away the underlying machine-specific details.
> 

![](https://craftinginterpreters.com/image/a-map-of-the-territory/mountain.png)

Parts of Writing a new Language

![**Eval** bridges the gap between representation (code) and execution, while **Apply** executes that representation within a specific environment.](data/technica/computation/assets/language-system/image.png)

**Eval** bridges the gap between representation (code) and execution, while **Apply** executes that representation within a specific environment.

![**Metacomputation** empowers **computation** by enabling it to reflect upon, manipulate, and evolve itself.](data/technica/computation/assets/language-system/image-1.png)

**Metacomputation** empowers **computation** by enabling it to reflect upon, manipulate, and evolve itself.

![image.png](data/technica/computation/assets/language-system/image-2.png)

![image.png](data/technica/computation/assets/language-system/image-3.png)

## Model of Computation

> Model of Computation: A **model of computation** (computation model) (**or computational formalism)** is a formal system that defines how computations are represented and executed. How is this process represented? And what are the **semantics** of this **representation**?
> 

> See in  [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md).
> 

## Language System

> **Language System**: A comprehensive framework encompassing the formal syntax, semantic rules, runtime environment, toolchain components (such as parsers, compilers, interpreters, and linkers), and associated libraries that collectively define, implement, and support the specification, translation, and execution of programs written in a particular programming language.
> 

> A note on the implementation of **Models of Computation**.
> 

> **Language System**: A comprehensive framework encompassing the formal syntax, semantic rules, runtime environment, toolchain components (such as parsers, compilers, interpreters, and linkers), and associated libraries that collectively define, implement, and support the specification, translation, and execution of programs written in a particular programming language.
> 

> **Data/Code:**  Data is passive, the "yin," while code is active, the "yang," but code *operates* on data, and data *informs* the code.  They are two sides of the same coin.
> 

> **Hardware/Software:** Hardware is the tangible, physical "yin," while software is the intangible, logical "yang."  Software needs hardware to run, and hardware is useless without software.
> 

> **Compilation/Interpretation:** Compilation is the "yin," a preparatory, offline process, while interpretation is the "yang," an immediate, online execution.  Both achieve the same goal but through different means.
> 

### Implementation

> See more in [Compiler System](note.html?n=technica/computation/language-system/conceptual-model-language-system/compiler-system.md), [Bytecode Virtual Machine](note.html?n=technica/computation/language-system/conceptual-model-language-system/bytecode-virtual-machine.md),  [Interpreter System](note.html?n=technica/computation/language-system/conceptual-model-language-system/interpreter-system.md) & [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md).
> 

How to Implement a Description of Computation:

- By translation,
- By simulating a machine,
- By implementing a hardware machine.

| Model | Description |
| --- | --- |
| **Interpreted Languages** | In interpreted languages, an interpreter executes source code line-by-line at runtime. Interpreters translate code into machine instructions or intermediate representations on-the-fly. Examples include Python, JavaScript, and Ruby. |
| **Compiled Languages (**Translating the Model to Another**)** | Compiled languages are translated into machine code or bytecode by a compiler before execution. The compiled code is executed directly by the CPU or a virtual machine. Examples include C, C++, Java, and Rust. |
| **Just-In-Time (JIT) Compilation** | JIT compilation combines aspects of both interpreted and compiled languages. Source code is initially interpreted, and frequently executed parts are dynamically compiled into machine code for improved performance. Examples include Java (HotSpot), JavaScript (V8), and Python (PyPy). |
| **Bytecode Languages** | Bytecode languages compile source code into an intermediate representation (bytecode) that a virtual machine can execute. This approach provides platform independence and facilitates portability. Examples include Java (JVM bytecode), Python (Python bytecode), and C# (CIL). |
| **Meta-Compilation** | Meta-compilation involves generating code or transformations based on high-level descriptions or specifications at compile-time. This approach allows for advanced code generation and optimization techniques. Examples include code generators and domain-specific language compilers. |
| **Transpiled Languages** | Transpiled languages are source-to-source compiled, where source code written in one programming language is translated into equivalent code in another. This enables cross-language compatibility and code reuse. Examples include TypeScript (transpiled to JavaScript), CoffeeScript, and Dart (transpiled to JavaScript). |
| **Reflective Languages** | Reflective languages provide mechanisms for introspecting and modifying their structure and behavior at runtime. This enables dynamic code generation, modification, and adaptation. Examples include Lisp, Smalltalk, and Ruby. |
| **Concurrency-Oriented Languages** | Concurrency-oriented languages are designed with built-in support for concurrent and parallel programming paradigms. They provide language-level constructs for expressing concurrent computations and synchronization. Examples include Go, Erlang, and Clojure. |

### Code Representation

> Code can be represented in various forms, including source code (e.g., Python, C++, Java), intermediate code (e.g., bytecode), and machine code (binary instructions for specific processor architectures).
> 

> **Code representation** refers to the visual or symbolic depiction of a computer program, often in a form that facilitates understanding, analysis, or manipulation by developers or automated tools.
> 

> **Code Representations**: Code can be represented in various forms, including source code (e.g., Python, C++, Java), intermediate code (e.g., bytecode), and machine code (binary instructions for specific processor architectures).
> 

| **Term** | **Description** |
| --- | --- |
| **AST (Abstract Syntax Tree)** | A hierarchical representation of the syntactic structure of source code, where each node represents a code element like statements, expressions, or declarations, used in parsing, type checking, and compiler code generation. |
| **SSA (Static Single Assignment)** | An intermediate code representation where each variable is assigned exactly once, simplifying data flow analysis and enabling specific optimizations, which clarifies variable lifetimes and dependencies. |
| **IR (Intermediate Representation)** | An abstract, machine-independent code representation used in compilers, acting as an intermediary between source and target machine codes, allowing for optimizations and transformations across multiple target architectures. |
| **CFG (Control Flow Graph)** | A graphical representation of a program's control flow, consisting of nodes representing basic blocks (sequences of instructions without branches) and edges representing possible control flow transfers between these blocks. |
| **DAG (Directed Acyclic Graph)** | A graph with directed edges and no cycles efficiently represents computations with shared sub-expressions, allowing for optimizations like eliminating common sub-expressions. |
| **RTL (Register Transfer Language)** | A low-level representation of code that describes how data is moved between registers and memory and the operations performed on them is used in hardware description languages and for low-level compiler optimizations. |
| **HLD (High-Level Dataflow)** | A representation used in high-level synthesis for hardware design, describing the flow of data between operations and enabling the generation of efficient hardware implementations. |
| **CPS (Continuation-Passing Style)** | A style of programming where programs are represented by explicitly passing continuation functions as arguments to function calls, facilitating the implementation of control flow operations like exceptions and coroutines. |
| **S-Expressions** | (Description not provided) |
| **Three-Address Code** | A low-level intermediate representation (IR) is used for code optimization and generation. It breaks down complex expressions into simple operations with at most three operands. |

### Grammar

> See more in [Formal Language](https://app.notion.com/p/Formal-Language-195c0f5171ec8012bf0fd0530a135871?pvs=21).
> 

### Scanning

> aka: Lexing or Lexical Analysis.
> 

> See more in [Scanning](note.html?n=technica/computation/language-system/conceptual-model-language-system/scanning.md).
> 

### Parsing

> aka. Reverse engineering the **Derivation Process (Expansion Process)**,
> 

> **Parsing** is the process of mapping a sentence, given a grammar, to a **parse tree**. Depending on the grammar, a sentence may have one or multiple possible parse trees.
> 

### Static Analysis

> See more in [Program Analysis](note.html?n=technica/computation/miscelanea/program-analysis.md).
> 

### Data Model

> 
- Control Flow Models
- Data Flow Models
- Abstract Memory Models
- Type and Effect Systems
- Program Dependency Graphs (PDG)
- Symbolic Models
- Semantic and Logical Models
- Symbol Table

### Language System Space

> Which are the language systems study in this notes?
> 

> [Clojure](note.html?n=technica/computation/language-system/conceptual-model-language-system/clojure.md), [Erlang](note.html?n=technica/computation/language-system/conceptual-model-language-system/erlang.md),  [Elixir](note.html?n=technica/computation/language-system/conceptual-model-language-system/elixir.md),  [Coq](note.html?n=technica/computation/language-system/conceptual-model-language-system/coq.md),  [Haskell](note.html?n=technica/computation/language-system/conceptual-model-language-system/haskell.md), [Vala](note.html?n=technica/computation/language-system/conceptual-model-language-system/vala.md),   [Standard ML](note.html?n=technica/computation/language-system/conceptual-model-language-system/standard-ml.md),  [R Language](note.html?n=technica/computation/language-system/conceptual-model-language-system/r-language.md),  [Lisp](note.html?n=technica/computation/language-system/conceptual-model-language-system/lisp.md),  [Lua](note.html?n=technica/computation/language-system/conceptual-model-language-system/lua.md),  [Perl](note.html?n=technica/computation/language-system/conceptual-model-language-system/perl.md),  [Python](note.html?n=technica/computation/language-system/conceptual-model-language-system/python.md),  [Rust](note.html?n=technica/computation/language-system/conceptual-model-language-system/rust.md),  [C++](note.html?n=technica/computation/language-system/conceptual-model-language-system/c-2.md),  [OCaml](note.html?n=technica/computation/language-system/conceptual-model-language-system/ocaml.md),  [Racket](note.html?n=technica/computation/language-system/conceptual-model-language-system/racket.md),  [AWK](note.html?n=technica/computation/language-system/conceptual-model-language-system/awk.md),  [Java](note.html?n=technica/computation/language-system/conceptual-model-language-system/java.md),  [Javascript](note.html?n=technica/computation/language-system/conceptual-model-language-system/javascript.md),  [C Language](note.html?n=technica/computation/language-system/conceptual-model-language-system/c-language.md),  [PHP: Hypertext Preprocessor](note.html?n=technica/computation/language-system/conceptual-model-language-system/php-hypertext-preprocessor.md),  [Ruby Language](note.html?n=technica/computation/language-system/conceptual-model-language-system/ruby-language.md),  [C#](note.html?n=technica/computation/language-system/conceptual-model-language-system/c.md), [Go](note.html?n=technica/computation/language-system/conceptual-model-language-system/go.md).
> 

## Optimization

> **Optimization:** Once we understand what the user’s program means, we are free to swap it out
with a different program that has the *same semantics* but implements them more
efficiently—we can **optimize** it.
> 

## Runtime System

> **Runtime:** The collection of services, mechanisms, and infrastructure provided by the execution environment that supports and manages the behavior of a program while it runs.
> 

> See more in [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md).
> 

## Concurrency System

> See More in [Concurrency](note.html?n=technica/computation/concurrency.md).
> 

## Conceptual Model

Conceptual Model: Language System

## References

- [Naming](note.html?n=technica/computation/system/programming/conceptual-model-programming/naming.md)
- [Reification](note.html?n=technica/computation/system/programming/conceptual-model-programming/reification.md)
- [Formal System](https://app.notion.com/p/Formal-System-41d02881d0544314b0e7ad3e6ada608a?pvs=21)
- [Formal Language](https://app.notion.com/p/Formal-Language-195c0f5171ec8012bf0fd0530a135871?pvs=21)
- https://github.com/csiglab/language-system-labs
- [A Guide to Programming Languages](https://app.notion.com/p/A-Guide-to-Programming-Languages-252c0f5171ec8003af50d798f047936a?pvs=21)
- [A Guide to Study Programming Language](https://app.notion.com/p/A-Guide-to-Study-Programming-Language-5a6ed523a0a94f619061f4051dcca041?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081bdaae5c39344d05faf?pvs=21)
- [‣](https://app.notion.com/p/194598edb79080678cacdd3eb1ff91f9?pvs=21)
- [‣](https://app.notion.com/p/10e598edb790814f9020d6a74a0829c7?pvs=21)
- [‣](https://app.notion.com/p/10e598edb790816bb840d76fb2831140?pvs=21)
- [‣](https://app.notion.com/p/10e598edb7908192a80ccd4325c01edf?pvs=21)
- [‣](https://app.notion.com/p/10e598edb7908162af92c422bb1be3e2?pvs=21)
- [Formal Grammar](https://www.wikiwand.com/en/Formal_grammar)
- [Lexical Grammar](https://en.wikipedia.org/wiki/Lexical_grammar)
- [Chomsky Hierarchy](https://www.wikiwand.com/en/Chomsky_hierarchy)
- [Programming language](https://www.cs.mcgill.ca/~rwest/wikispeedia/wpcd/wp/p/Programming_language.htm)
- [Programming languages resources](https://bernsteinbear.com/pl-resources/)
- [Design Criteria for Programming Languages](https://jcsites.juniata.edu/faculty/rhodes/lt/plcriteria.htm)
- https://www.youtube.com/watch?v=_ahvzDzKdB0&list=WL&index=16&t=10s
- [x86](note.html?n=technica/computation/operating-system/x86.md)
- [‣](https://app.notion.com/p/10e598edb79081d2a549ec868ef75bcd?pvs=21)
- [‣](https://app.notion.com/p/1c7598edb79080a99e37e0c313af53bc?pvs=21)
- [‣](https://app.notion.com/p/1c7598edb790808d9ed5e22c6617dfd1?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081d2af7fededaf67de2c?pvs=21)
- https://github.com/dbremont/algorithms/tree/main/csf
- [**Backus-Naur Form (BNF)**](https://app.notion.com/p/Backus-Naur-Form-BNF-5e3c8a0c5b85406ab2aaf8e70eef3b97?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081bdaae5c39344d05faf?pvs=21)
- https://people.csail.mit.edu/rachit/post/why-study-programming-languages/
- https://david.alvarezrosa.com/posts/devirtualization-and-static-polymorphism/