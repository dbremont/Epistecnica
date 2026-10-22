---
tags: [language]
---

# Python

- [CPython](note.html?n=technica/computation/language-system/conceptual-model-language-system/cpython.md)

> **Python** is a high-level, dynamically typed, garbage-collected, multi-paradigm programming language whose reference implementation executes bytecode on a stack-based virtual machine, combining late binding, pervasive object orientation, introspection, and a large runtime/library ecosystem optimized for developer productivity and extensibility over raw execution speed.
> 

> **Python Enhancement Proposals (PEPs)** are design documents that provide information to the Python community, describe new features, processes, or improvements for Python, and serve as the primary mechanism for proposing, discussing, and standardizing major changes to the language and its ecosystem.
> 

![Untitled](../assets/note/technica/computation/language-system/conceptual-model-language-system/python/untitled.png)

QA:

- Do Python files Cause Conflicts with the Import System? Yes.

## Intro

## 🏗️ Models of Computation

> What are the models of computation that  the language supports? See more in [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md).
> 

> Computational paradigms largely fall into two broad categories: **Reactive and Proactive**. **Reactive models** are event-driven and respond to external stimuli, emphasizing adaptability and responsiveness. **Proactive models**, by contrast, execute predefined computations based on structured logic, prioritizing control and determinism. Many modern systems blend both paradigms to optimize performance and adaptability.
> 

## 📜 Language Specification

> The Language Specification precisely defines the rules for **Lexical Grammar** (token formation and character sets), **Syntactic Grammar** (structure, ambiguities, operator precedence), **binding** (associating names with values and constructs), **Scoping Rules** (name visibility and lifetime), and **Semantics** (the meaning of expressions, statements, and program behavior), establishing the formal foundation for how programs are written, interpreted, and executed.
> 

Python: 📜 Language Specification

## **🏷️**Type System

> The Type System defines how a language classifies, checks, and enforces types—covering static vs. dynamic typing, polymorphism, type inference, subtyping models, type safety, advanced features like union or dependent types, and runtime behaviors such as type erasure or reflection—establishing the formal rules for how values and operations are typed and validated throughout program execution.
> 

- [Python: Type System]

## 📚 The Standard Library

> The **Standard Library** provides a comprehensive collection of pre-built modules, functions, and data structures that offer essential utilities and abstractions—such as collections, I/O, concurrency, and networking—serving as a foundational toolkit that enables developers to efficiently build robust and portable applications without reinventing common functionality.
> 

- [Python: The Standard Library]

## **🔀** Representation

> This note delves into the multifaceted concept of **representation** within language systems, covering critical aspects such as **code representation**, **data structures**, **memory layout**, **execution state**, **resource handles**, and related runtime elements. Understanding how these components are represented and managed at various stages—from high-level source constructs down to low-level machine artifacts—provides deep insights into the design, capabilities, and constraints of a programming language and its execution environment.
> 

> By examining representation along a continuum from **higher-level abstractions** (e.g., source code and data models) to **lower-level concrete implementations** (e.g., memory organization and processor state), we conceptually reduce dimensionality and complexity. This stratified approach facilitates clearer reasoning and more effective analysis of a language’s expressive power, runtime efficiency, safety guarantees, and extensibility.
> 

> Studying representation in this layered fashion is a powerful method for dissecting language systems because it highlights the interplay between language semantics and system architecture, illuminating both strengths and potential limitations inherent in the language’s design and implementation.
> 

**Python:  🔀** Representation

## **🧩** Modularization

> **Code organizational mechanisms** refer to strategies and structures used to manage, modularize, and maintain code in a way that promotes clarity, efficiency, and scalability throughout the software development process.
> 

- [Python: Modularization]

## **🔄 Program  Execution Model**

> This note explores the concurrency model, parallelism, error handling, and control flow mechanisms of the language system.
> 

> A **concurrency model** specifies how multiple **instruction streams** (or threads of execution) interact, overlap, and affect shared state over time, often nondeterministically. It defines the rules governing the execution, synchronization, visibility, and ordering of instructions when multiple agents (threads, processes, actors) are active concurrently.
> 

Python: **🔄** Concurrency Model

## **✨**Metaprogramming

> This note explore the  metaprogramming mechanisms provided by this language.
> 

> ¿Can we compute over the **description of computation**? ¿Can code be treated like data?
> 

- [Python: Metaprogramming]

## ⚙️ Execution System

> A **Language Execution System (LES)** is the set of tools, algorithms, and runtime mechanisms that **execute a program** represented by a given **encoding scheme** (e.g., source code, bytecode, machine code). It defines how a program's **semantics** are realized on a computational substrate (hardware, VM, or interpreter) through a series of **transformations** and **runtime behaviors**.
> 

> Related: [**🔀** Representation](note.html?n=technica/computation/language-system/conceptual-model-language-system/python.md).
> 

- [Python: Execution System]

## **🔗 Interoperability**

> Which type of **Interoperability  Mechanisms  does this Language Supports?**
> 

Python: **🔗Interoperability**

## 💻 Language System Interface

> The **Language System Interface** encompasses the collection of mechanisms, APIs, and tooling hooks that enable interaction with both the **compile-time** and **runtime** aspects of a programming language system. These interfaces serve as critical access points for developers, compilers, debuggers, profilers, and other tools to analyze, transform, observe, or extend the behavior of programs.
> 

> By exposing internal structures—such as syntax trees, type information, bytecode, runtime metadata, and execution state—the language system interface facilitates tasks ranging from static analysis and metaprogramming to runtime instrumentation and debugging. Studying these interfaces reveals how a language system supports extensibility, introspection, tooling integration, and control over program behavior, making them essential for advanced language engineering and systems programming.
> 

💻🔧 Python: Language System Interface

## ⚡Performance

> How does the **computational model's** implementation impact performance?
> 

> What are the key factors in programming language **`X`** that influence the execution speed and overall efficiency of programs?
> 

> How does the language's mapping to **`hardware`** (e.g., CPU, memory, I/O) affect application performance?
> 

> What performance impact do the language's built-in data structures have on memory usage and **`execution time`**?
> 

- [Python: Performance]

## 🛠️ Tooling & Ecosystem

🛠️ Python: Tooling & Ecosystem

## `🎭` Miscellanea

### Python Language Governance

> **Python Language Governance** refers to the structured decision-making process led by the **Python Steering Council** and supported by the **Python Core Developers**, guided by the **Python Enhancement Proposal (PEP)** process, to ensure the language's evolution, maintenance, and community-driven development.
> 

- https://peps.python.org/pep-0000/

## 🔗 References

- [Ultimate Python study guide for newcomers and professionals alike](https://github.com/huangsam/ultimate-python)
- [Speeding up function calls with just one line in Python](https://hackeregg.github.io/2020/06/03/Speeding-up-function-calls-with-just-one-line-in-Python.html)
- [Using os.walk() to recursively traverse directories in Python](https://stackoverflow.com/questions/16953842/using-os-walk-to-recursively-traverse-directories-in-python)
- [Python Configuration Right](https://whalesalad.com/blog/doing-python-configuration-right)
- [Overview of python dependency management tools](https://modelpredict.com/python-dependency-management-tools)
- [Costs of running a Python webapp for 55k monthly users](https://keepthescore.co/blog/posts/costs-of-running-webapp/)
- [Optimized I/O operations in Python](https://towardsdatascience.com/optimized-i-o-operations-in-python-194f856210e0)
- [Containerized Python Development](https://matteoguadrini.github.io/posts/containerized-python-development/)
- [Anyscale - Parallelizing Python Code](https://www.anyscale.com/blog/parallelizing-python-code)
- [The Python Language Reference — Python 3.10.0 documentation](https://docs.python.org/3/reference/)
- [Python behind the scenes #11: how the Python import system works](https://tenthousandmeters.com/blog/python-behind-the-scenes-11-how-the-python-import-system-works/)
- [Python Concurrency: The Tricky Bits](https://python.hamel.dev/concurrency/)
- [Pattern Matching in Python](https://github.com/gvanrossum/patma/blob/master/README.md#tutorial)
- [Profiling and Analyzing Performance of Python Programs](https://martinheinz.dev/blog/64)
- [PyInstrument](https://github.com/joerick/pyinstrument)
- [Numba](https://numba.pydata.org/)
- [Python Developer’s Guide](https://devguide.python.org/)
- [How CPython Implements and Uses Bloom Filters for String Processing](https://codeconfessions.substack.com/p/cpython-bloom-filter-usage)
- Pydantic
[https://docs.pydantic.dev/dev/](https://docs.pydantic.dev/dev/)
- PEP 491 – The Wheel Binary Package Format 1.9 / [https://peps.python.org/pep-0491/](https://peps.python.org/pep-0491/)
- https://peps.python.org/
- https://docs.python.org/3/library/index.html
- https://diveintopython3.net/index.html
- ‣[https://github.com/gaogaotiantian/viztracer](https://github.com/gaogaotiantian/viztracer)
- [https://www.notion.so/A-Guide-to-Study-Programming-Language-5a6ed523a0a94f619061f4051dcca041?source=copy_link](https://www.notion.so/A-Guide-to-Study-Programming-Language-5a6ed523a0a94f619061f4051dcca041?source=copy_link)‣
- [Concurrency](note.html?n=technica/computation/concurrency.md)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [Language System](note.html?n=technica/computation/language-system.md)
- https://github.com/csiglab/language-system-labs
- https://docs.pydantic.dev/latest/
- Ruff: Formatter + Linter
- uv: Environment management
- Pytest: Testing
- Click: Typer
- https://gvanrossum.github.io/index.html
- https://blog.changs.co.uk/python-315-features-that-didnt-make-the-headlines.html