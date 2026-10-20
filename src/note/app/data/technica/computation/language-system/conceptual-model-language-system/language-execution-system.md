---
tags: [language-system]
---

# Language Execution System

- [Memory  Management](note.html?n=technica/computation/language-system/conceptual-model-language-system/memory-management.md), [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md), [Function](note.html?n=technica/computation/language-system/conceptual-model-language-system/function.md)

> A **Language Execution System (LES)** is the set of tools, algorithms, and runtime mechanisms that **execute a program** represented by a given **encoding scheme** (e.g., source code, bytecode, machine code). It defines how a program's **semantics** are realized on a computational substrate (hardware, VM, or interpreter) through a series of **transformations** and **runtime behaviors**.
> 

> **Execution Model**  defines the abstract machine's structure and runtime behavior, 
including memory management, concurrency, and fundamental control flow.
> 

> **High-level LES**: Operates on abstract representations (e.g., Python interpreter).
> 

> **Low-level LES**: Closer to hardware (e.g., C compiler generating ELF binaries).
> 

## Formulation

A **Language Execution System (LES)**  can be defined as:  $\text{LES} = \langle \mathcal{P}, \mathcal{E}, \mathcal{T}, \mathcal{R}, \mathcal{S} \rangle$ where:

**$\mathcal{P}$ (Program Representation)**

- The **encoding scheme** of the program (e.g., text source, AST, bytecode, machine code).
- Governed by a **formal grammar** (BNF, CFG) and **semantic rules** (static/dynamic semantics).

**$\mathcal{E}$ (Execution Model)**

- The **computational paradigm** used to run the program:
    - **Interpretation** (direct execution of AST/bytecode).
    - **Compilation** (translation to machine code).
    - **Hybrid** (JIT compilation, tiered execution).
- Includes **execution strategies** (e.g., stack-based vs. register-based VMs, event loops).
- Note: The **Execution Model** - Contains the **Evaluation Model**.

**Evaluation Model**

**$\mathcal{R}$ (Runtime Environment): Mechanisms** required for execution:

- A **runtime environment** is a structured execution context that provides program code with necessary services, including memory management (heap, stack, garbage collection), execution control (thread scheduling, synchronization, exception handling), system interaction (I/O, networking, process management), and abstraction layers (virtual machines, just-in-time compilation, sandboxing), ensuring that the program operates correctly within its target hardware and operating system constraints.
- Memory management (GC, manual allocation).
- Concurrency (threads, async/await, actors).
- Dynamic features (reflection, metaprogramming).

**$\mathcal{S}$ (System Interface):** How the LES interacts with **external systems**:

- OS (syscalls, signals, I/O).
- Hardware (ABI, registers, SIMD).
- Foreign function interfaces (FFI).

## Structure

> Which are the components of a LES?
> 

| **Component** | **Role in LES** | **Example Implementations** |
| --- | --- | --- |
| **Parser** | Converts source code to AST. | ANTLR, Yacc, Clang’s parser. |
| **Compiler** | Transforms high-level code to lower-level IR/machine code. | GCC, LLVM, Roslyn. |
| **Virtual Machine** | Executes bytecode/intermediate representation. | JVM, CPython VM, Lua VM. |
| **Runtime** | Manages memory, threads, and dynamic features during execution. | V8’s Ignition+TurboFan, .NET CLR. |
| **System Linker** | Resolves external dependencies for execution. | `ld` (Unix), `link.exe` (Windows). |

## **Runtime**

> A **runtime** is the active execution layer of a Language Execution System (LES): the set of mechanisms, services, and abstractions that govern *how* a program behaves once it begins executing. It mediates between the program, the execution model, and the underlying platform.
> 

> A **runtime environment** is a structured execution context that provides program code with necessary services, including memory management (heap, stack, garbage collection), execution control (thread scheduling, synchronization, exception handling), system interaction (I/O, networking, process management), and abstraction layers (virtual machines, just-in-time compilation, sandboxing), ensuring that the program operates correctly within its target hardware and operating system constraints.
> 

## **Runtime Service**

| **Service** | **Description** |
| --- | --- |
| **Memory Management** | Manages the allocation and deallocation of memory, including garbage collection to free up unused memory. |
| **Concurrency & Parallelism** | Supports multi-threading and other concurrency models to enable simultaneous task execution. |
| **Debugging and Profiling** | Provides tools for debugging and profiling, such as stack traces, runtime error messages, and performance monitoring. |
| **Dynamic Loading** | Enables loading and execution of code modules at runtime, enhancing modularity and flexibility. |
| **Just-In-Time (JIT) Compilation** | Dynamically compiles high-level code into low-level code just before execution to optimize performance. |
| **Exception Handling** | Provides mechanisms for detecting and handling runtime errors and exceptions to prevent crashes. |
| **Intrinsic Operation(s)** | Built-in low-level operations exposed by the runtime (e.g., atomic operations, intrinsic functions, memory barriers) that map closely to hardware capabilities. |
| **Safety, Isolation & Sandboxing** | Capability systems, VM isolation, type and bounds checks, security policies. |
| **System Integration** (Interoperability) | Access to I/O, networking, filesystems, OS services, process management. |
| **Execution Control** | Scheduling, stack frames, call dispatch, exception propagation, continuations. |
| **Dynamic & Reflective Capabilities** | Reflection, dynamic loading, metaprogramming, proxies, introspection. |

## Runtime Representation

> See more in [Runtime Representation](note.html?n=technica/computation/language-system/conceptual-model-language-system/runtime-representation.md).
> 

## Memory System

> See more in [Memory  Management](note.html?n=technica/computation/language-system/conceptual-model-language-system/memory-management.md).
> 

## Evaluation Model

> aka.  Semantic [Evaluation Model](note.html?n=technica/computation/language-system/conceptual-model-language-system/evaluation-model.md) & [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md).
> 

## QA

### What is the different between the notions of Evaluation Model and Execution Model?

> **Execution Model** defines the abstract machine's structure and runtime behavior, 
including memory management, concurrency, and fundamental control flow.
> 

> **Evaluation Model**  specifies when function arguments are computed relative to a function's
invocation, primarily distinguishing between strict (eager) and  non-strict (lazy) evaluation.
> 

> Note: The **Evaluation Model** is Part of the **Execution Model**.
> 

## References

- [How much memory do you need to run 1M concurrent tasks? (pkolaczk.github.io)](https://news.ycombinator.com/item?id=36024209)
- [What is “runtime”?](https://stackoverflow.com/questions/3900549/what-is-runtime)
- [Runtime System](https://en.wikipedia.org/wiki/Runtime_system)
- [Runtime System](https://web.archive.org/web/20131230235941/https://users-cs.au.dk/hosc/local/LaSC-3-4-pp343-380.pdf)
- [The Case for the Holistic Language Runtime System](https://timharris.uk/papers/2014-wrsc-maas.pdf)
- [Language Run-time Systems: an Overview](https://drops.dagstuhl.de/opus/volltexte/2015/5475/pdf/4.pdf)
- [A Survey: Runtime Software Systems for High Performance Computing](https://dl.acm.org/doi/10.14529/jsfi170103)
- [A survey of runtime monitoring instrumentation techniques](https://iris.rais.is/en/publications/a-survey-of-runtime-monitoring-instrumentation-techniques)
- https://www.wikiwand.com/en/Runtime_system
- Garbage Collection: https://github.com/pebal/sgcl
- A Runtime System https://web.archive.org/web/20131230235941/https://users-cs.au.dk/hosc/local/LaSC-3-4-pp343-380.pdf
- [Garbage Collection is Fast, But a Stack is Faster](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.52.1119&rep=rep1&type=pdf)
- [A real-time garbage collector based on the lifetimes of objects](https://dl.acm.org/doi/10.1145/358141.358147)
- [A LISP garbage-collector for virtual-memory computer systems](https://dl.acm.org/doi/10.1145/363269.363280)
- [Garbage Collection Can Be Faster Than Stack Allocation](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.84.2064&rep=rep1&type=pdf)
- [A Unified Theory of Garbage Collection](https://courses.cs.washington.edu/courses/cse590p/05au/p50-bacon.pdf)
- https://www.oilshell.org/blog/2023/01/garbage-collector.html
- A Survey of Programming Language Memory Models https://dl.acm.org/doi/abs/10.1134/S0361768821060050
- The Case for the Holistic Language Runtime System https://timharris.uk/papers/2014-wrsc-maas.pdf
- A survey of real-time capabilities in functional languages and compilers https://onlinelibrary.wiley.com/doi/abs/10.1002/cpe.4902
- Language Run-time Systems: an Overview https://drops.dagstuhl.de/opus/volltexte/2015/5475/pdf/4.pdf
- A Survey: Runtime Software Systems for High Performance Computing https://dl.acm.org/doi/10.14529/jsfi170103
- A survey of runtime monitoring instrumentation techniques https://iris.rais.is/en/publications/a-survey-of-runtime-monitoring-instrumentation-techniques
- Programming Languages: Principles and Paradigms https://doc.lagout.org/science/0_Computer%20Science/1_Principles%20of%20Programming%20Languages/Programming%20Languages%20-%20Principles%20and%20Paradigms.pdf
- Data structure models for programming languages https://dl.acm.org/doi/abs/10.1145/1115880.1115882
- Programming Languages as Thought Models https://www.cs.kau.se/cs/education/courses/dvgc01/lectures/Rechenberg.pdf
- Fully Abstract Models of Programming Languages https://alleystoughton.us/research/famopl.pdf
- An Abstract View of Programming Languages https://www.ics.uci.edu/~jajones/INF102-S18/readings/09_Moggi.pdf
- A Survey of Programming Language Memory Models https://www.reddit.com/r/ProgrammingLanguages/comments/qz50t7/a_survey_of_programming_language_memory_models/
- Abstract machines for programming language impleme https://www.inf.ed.ac.uk/teaching/courses/lsi/diehl_abstract_machines.pdf
- LLVM Tutorial: Kaleidoscope (Implementing a Language with LLVM) https://github.com/ghaiklor/llvm-kaleidoscope
- https://www.pypy.org/posts/2022/07/toy-optimizer.html
- https://www.cs.cornell.edu/talc/papers/compile_rtcg.pdf
- https://www.itu.dk/people/sestoft/rtcg/rtcg.pdf
- CAS 761: Generative Programming https://www.cas.mcmaster.ca/~carette/CAS761/F2020/index.html
- https://github.com/namin/simple-tracing-jit
- https://eli.thegreenplace.net/2013/11/05/how-to-jit-an-introduction
- https://eli.thegreenplace.net/2014/01/15/some-thoughts-on-llvm-vs-libjit
- A Minimal LLVM JIT example for LLVM-5 https://gist.github.com/38/39e7b514d916ed6fa6a2bba629fdf6ff
- Speeding up query execution in PostgreSQL using LLVM JIT compiler https://llvm.org/devmtg/2016-09/slides/Melnik-PostgreSQLLLVM.pdf
- Everything I wish I knew when learning C (tmewett.com) https://news.ycombinator.com/item?id=33773043
- Building An Efficient JIT the best kind of jit https://llvm.org/devmtg/2008-08/Begeman_EfficientJIT.pdf
- Just-In-Time Compiler Library https://www.gnu.org/software/libjit/doc/libjit.html
- libgccjit https://gcc.gnu.org/onlinedocs/gcc-12.2.0/jit/index.html#
- Libgccjit.so: an embeddable JIT-compiler based on GCC https://news.ycombinator.com/item?id=6488120
- https://github.com/spencertipping/jit-tutorial
- Re: Lazy JIT IR code generation to increase JIT speed with partitions https://mail.google.com/mail/u/0/popout?ver=233og3h6h7x7&search=inbox&th=%23thread-f%3A1751047640390109158&cvid=1
- A Minimal LLVM JIT example for LLVM-5 https://gist.github.com/38/39e7b514d916ed6fa6a2bba629fdf6ff
- A Complete Guide to LLVM for Programming Language Creators https://mukulrathi.com/create-your-own-programming-language/llvm-ir-cpp-api-tutorial/
- Numba https://numba.pydata.org/
- How to write a very simple JIT compiler https://github.com/spencertipping/jit-tutorial
- AoT Compiled Languages Metaprogramming: A Nascent Trend Or Another Esoteric Practice? https://dic.dzinko.org/metaprogramming-overview-classification
- https://github.com/mkirchner/gc
- https://gitlab.com/dbtudes/tgc
- Code Generation: The Inner Sanctum of Database Performance http://highscalability.com/blog/2016/9/7/code-generation-the-inner-sanctum-of-database-performance.html
- LLVM: Diehl, Stephan, Pieter Hartel, and Peter Sestoft. "Abstract machines for programming language implementation." Future Generation Computer Systems 16.7 (2000): 739-751.
.. Read Large Files With Rust
- [**Semantics**](https://app.notion.com/p/Semantics-12e375827ade4a74a4349241b07140c3?pvs=21)