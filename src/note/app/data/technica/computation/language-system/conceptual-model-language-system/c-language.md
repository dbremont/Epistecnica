---
tags: [language]
---

# C Language


> **C** is a **statically typed**, **imperative**, **procedural**, **low-level systems programming language** defined by a **small core language** with **explicit memory management**, a **weak type system**, and a **flat compilation model** targeting machine-level execution.
> 

> It was formally standardized as **ISO/IEC 9899**, with multiple editions (e.g., C89/C90, C99, C11, C17, C23), and is defined via a **translation process model**, **abstract machine semantics**, and a **conformance-testing framework**.
> 

QA:

- How are implementation-defined behaviors documented (e.g., file paths, system calls, or hardware dependencies)?
- How does the specification handle backward-incompatible changes (e.g., Python’s `2.x` → `3.x` transition)?
- Which are the pre-defined macros in C? `__DATE__, __TIME__` , etc.

## 🧮 Model of Computation

> What are the models of computation that  the language supports? See more in [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md).
> 

## 📜 Language Specification

> The Language Specification precisely defines the rules for **Lexical Grammar** (token formation and character sets), **Syntactic Grammar** (structure, ambiguities, operator precedence), **binding** (associating names with values and constructs), **Scoping Rules** (name visibility and lifetime), and **Semantics** (the meaning of expressions, statements, and program behavior), establishing the formal foundation for how programs are written, interpreted, and executed.
> 

C Language: 📜 Language Specification

## **🏷️**Type System

> The Type System defines how a language classifies, checks, and enforces types—covering static vs. dynamic typing, polymorphism, type inference, subtyping models, type safety, advanced features like union or dependent types, and runtime behaviors such as type erasure or reflection—establishing the formal rules for how values and operations are typed and validated throughout program execution.
> 

C Language: **🏷️** Type System

## 📚 The Standard Library

> The **Standard Library** provides a comprehensive collection of pre-built modules, functions, and data structures that offer essential utilities and abstractions—such as collections, I/O, concurrency, and networking—serving as a foundational toolkit that enables developers to efficiently build robust and portable applications without reinventing common functionality.
> 

C Language: 📚 Standard Library

## **🔀** Representation

> This note delves into the multifaceted concept of **representation** within language systems, covering critical aspects such as **code representation**, **data structures**, **memory layout**, **execution state**, **resource handles**, and related runtime elements. Understanding how these components are represented and managed at various stages—from high-level source constructs down to low-level machine artifacts—provides deep insights into the design, capabilities, and constraints of a programming language and its execution environment.
> 

> By examining representation along a continuum from **higher-level abstractions** (e.g., source code and data models) to **lower-level concrete implementations** (e.g., memory organization and processor state), we conceptually reduce dimensionality and complexity. This stratified approach facilitates clearer reasoning and more effective analysis of a language’s expressive power, runtime efficiency, safety guarantees, and extensibility.
> 

> Studying representation in this layered fashion is a powerful method for dissecting language systems because it highlights the interplay between language semantics and system architecture, illuminating both strengths and potential limitations inherent in the language’s design and implementation.
> 

C Language**:  🔀** Representation

## **🧩** Modularization

> **Code organizational mechanisms** refer to strategies and structures used to manage, modularize, and maintain code in a way that promotes clarity, efficiency, and scalability throughout the software development process.
> 

C Language: **🧩**Modularization

## **🔄 Computation Flow Primitive**

> This note explores the concurrency model, parallelism, error handling, and control flow mechanisms of the language system.
> 

> A **concurrency model** specifies how multiple **instruction streams** (or threads of execution) interact, overlap, and affect shared state over time, often nondeterministically. It defines the rules governing the execution, synchronization, visibility, and ordering of instructions when multiple agents (threads, processes, actors) are active concurrently.
> 

C Language: **🔄 Computation Flow Primitive**

## **✨**Metaprogramming

> This note explore the  metaprogramming mechanisms provided by this language.
> 

> ¿Can we compute over the **description of computation**? ¿Can code be treated like data?
> 

C Language**: ✨**Metaprogramming

## ⚙️ Execution System

> A **Language Execution System (LES)** is the set of tools, algorithms, and runtime mechanisms that **execute a program** represented by a given **encoding scheme** (e.g., source code, bytecode, machine code). It defines how a program's **semantics** are realized on a computational substrate (hardware, VM, or interpreter) through a series of **transformations** and **runtime behaviors**.
> 

> Related: [**🔀** Representation](https://app.notion.com/p/Representation-3722a849ef3140db9df1b0a6654d29b2?pvs=21).
> 

C Language: ⚙️ Execution System

## **🔗 Interoperability**

> Which type of **Interoperability  Mechanisms  does this Language Supports?**
> 

C Language: **🔗Interoperability**

## 💻 Language System Interface

> The **Language System Interface** encompasses the collection of mechanisms, APIs, and tooling hooks that enable interaction with both the **compile-time** and **runtime** aspects of a programming language system. These interfaces serve as critical access points for developers, compilers, debuggers, profilers, and other tools to analyze, transform, observe, or extend the behavior of programs.
> 

> By exposing internal structures—such as syntax trees, type information, bytecode, runtime metadata, and execution state—the language system interface facilitates tasks ranging from static analysis and metaprogramming to runtime instrumentation and debugging. Studying these interfaces reveals how a language system supports extensibility, introspection, tooling integration, and control over program behavior, making them essential for advanced language engineering and systems programming.
> 

C Language: 💻 Language System Interface

## ⚡Performance

> How does the **computational model's** implementation impact performance?
> 

> What are the key factors in programming language **`X`** that influence the execution speed and overall efficiency of programs?
> 

> How does the language's mapping to **`hardware`** (e.g., CPU, memory, I/O) affect application performance?
> 

> What performance impact do the language's built-in data structures have on memory usage and **`execution time`**?
> 

C Language: ⚡Performance

## 🛠️ Tooling & Ecosystem

> What tools does the language provide?
> 

> List of implementations of the language.
> 

C Language: 🛠️ Tooling & Ecosystem

## `🎭` Miscellanea

> Language Security,  Special Features, Portability, Documentation,  Debugging Support (Interoperability, Ecosystem),  Metadata (Compiler, …),  Intrinsic, …
> 

## References

- https://en.wikipedia.org/wiki/C99
- https://en.wikipedia.org/wiki/C11_(C_standard_revision)
- https://en.wikipedia.org/wiki/C17_(C_standard_revision)
- [GNU Bison](https://en.wikipedia.org/wiki/GNU_Bison)
- [GNU Flex](https://en.wikipedia.org/wiki/Flex_(lexical_analyser_generator))
- [Quick C++ Benchmark](https://quick-bench.com/)
- [C++ Reflection Library](https://github.com/rttrorg/rttr)
- [tgc: A Tiny Garbage Collector for C](https://github.com/orangeduck/tgc)
- [GoogleTest](https://github.com/google/googletest)
- [Google Benchmark](https://github.com/google/benchmark)
- [backward-cpp: A beautiful stack trace pretty printer for C++](https://github.com/bombela/backward-cpp)
- [Minicel](https://github.com/tsoding/minicel)
- [Trace and profile function calls with GCC](https://balau82.wordpress.com/2010/10/06/trace-and-profile-function-calls-with-gcc/)
- [GDB, please set a breakpoint on all my functions](https://blog.0x972.info/?d=2017/02/10/08/25/23-gdb-please-set-a-breakpoint-on-all-my-functions)
- [5.1.7 Breakpoint Command Lists](https://sourceware.org/gdb/current/onlinedocs/gdb/Break-Commands.html)
- [CS3650 | Computer Systems](https://course.ccs.neu.edu/cs3650sp20/index.html)
- [CS 4400 – Computer Systems](https://my.eng.utah.edu/~cs4400/)
- [CRN 36535 Systems Programming](https://cs361-a.cs.uic.edu/)
- [CS4414: Systems Programming](https://www.cs.cornell.edu/courses/cs4414/2021fa/)
- [CS 361 Systems Programming](https://www.youtube.com/playlist?list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP)
- [Debugging C With Cosmopolitan Libc](https://ahgamut.github.io/2022/10/23/debugging-c-with-cosmo/)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C](https://en.wikipedia.org/wiki/C_(programming_language))
- Shebs, S. (2011). GNU Debugger (GDB): Architecture. http://aosabook.org/en/gdb.html
- [The C++ Type System Is Your Friend - Hubert Matthews](https://www.youtube.com/watch?v=MCiVdu7gScs)
- [LD Preload Trick](http://www.goldsborough.me/c/low-level/kernel/2016/08/29/16-48-53-the_-ld_preload-_trick/)
- [CPP Standard Library](https://en.cppreference.com/w/cpp/header)
- [Eric Niebler](https://ericniebler.com/)
- [Denis Bakhvalov](https://easyperf.net/)
- Harbison, S. P., Steele, G. L., Steele, G. (2022). C, a Reference Manual.
- Stroustrup, B. (2022). The C++ Programming Language.
- Brennan, S. (2015). Tutorial - Write a Shell in C. https://brennan.io/2015/01/16/write-a-shell-in-c/
- Google. (2022). Google C++ Style Guide. https://google.github.io/styleguide/cppguide.html
- Facebook. (2022). folly: An open-source C++ library developed and used at Facebook. https://github.com/facebook/folly
- Valgrind. (n.d.). Valgrind instrumentation framework for building dynamic analysis tools. Retrieved July 25, 2022, from https://valgrind.org/
- Facebook. (2022). Wangle is a framework providing a set of common client/server abstractions for building services in a consistent, modular, and composable way. https://github.com/facebook/wangle
- Facebook. (2022). CacheLib. https://cachelib.org/
- Boost C++ Libraries. (n.d.). Retrieved August 6, 2022, from https://www.boost.org/
- libevent. (n.d.). libevent : An event notification library. Retrieved July 25, 2022, from https://libevent.org/
- spencertipping. (2022). jit-tutorial: How to write a very simple JIT compiler. https://github.com/spencertipping/jit-tutorial
- Kubiatowicz, J. (2021). CS262A: Advanced Topics in Computer Systems. https://people.eecs.berkeley.edu/~kubitron/courses/cs262a-F21/index.html
- The GNU C Library. (n.d.). Free Software Foundation. Retrieved April 6, 2022, from https://www.gnu.org/software/libc/manual/html_mono/libc.html
- [tinyvm](https://github.com/jakogut/tinyvm)
- [Everything I wish I knew when learning C](https://tmewett.com/c-tips/)
- [awesome-cpp](https://github.com/fffaraz/awesome-cpp)
- [CPP Links](https://github.com/MattPD/cpplinks)
- [34/64 Bits Software](https://stackoverflow.com/questions/54082459/fatal-error-bits-libc-header-start-h-no-such-file-or-directory-while-compili)
- [C Deep](https://dev.to/fullstackhacker/c-deep-47k8)
- [Tutorial - Write a Shell in C](https://brennan.io/2015/01/16/write-a-shell-in-c/)
- [libevent : An event notification library](https://libevent.org/)
- [CacheLib](https://cachelib.org/)
- [folly: An open-source C++ library developed and used at Facebook](https://github.com/facebook/folly)
- [gprof Quick-Start Guide](https://web.eecs.umich.edu/~sugih/pointers/gprof_quick.html)
- [cyrus-and/gdb-dashboard: Modular visual interface for GDB in Python](https://github.com/cyrus-and/gdb-dashboard)
- An overview of build systems (mostly for C++ projects) https://julienjorge.medium.com/an-overview-of-build-systems-mostly-for-c-projects-ac9931494444
- C reference https://en.cppreference.com/w/c
- Let’s write a setjmp https://nullprogram.com/blog/2023/02/12/
- Few lesser known tricks, quirks and features of C https://blog.joren.ga/less-known-c
- MutexProtected: A C++ Pattern for Easier https://awesomekling.github.io/MutexProtected-A-C++-Pattern-for-Easier-Concurrency/
- [Co Routines](https://probablydance.com/2021/10/31/-c-coroutines-do-not-spark-joy/)
- [C Preprocessor](https://www.wikiwand.com/en/C_preprocessor)
- [Everything I wish I knew when learning C](https://news.ycombinator.com/item?id=33773043)
- [A Compiler for C89](http://tom7.org/abc/)
- [Nine ways to break your systems code using volatile](https://blog.regehr.org/archives/28)
- [A Guide to Study Programming Language](https://app.notion.com/p/A-Guide-to-Study-Programming-Language-5a6ed523a0a94f619061f4051dcca041?pvs=21)
- [Concurrency](note.html?n=technica/computation/concurrency.md)
- [Language System](note.html?n=technica/computation/language-system.md)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- https://github.com/csiglab/language-system-labs