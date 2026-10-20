---
tags: [metacomputation]
---

# Program Modification

- [Code Generation](note.html?n=technica/computation/language-system/conceptual-model-language-system/code-generation.md)

> **Program Modification** is the process of systematically transforming a program's source code, intermediate representation, or executable form to alter its behavior, structure, or properties while preserving semantic correctness or achieving a specific design goal.
> 

QA:

- How to use LD_PRELOAD to overwrite a called? Why is this called an sniffer?

## 🧾 Formalization

Program modification can be viewed as an application of a **computational transformation function**  $T: P \rightarrow P$',  where:

- $P$ is the original program instance, represented in a formal language $L$,
- $P'$ is the modified program instance, also in $L$ or a related language,
- $T$ is a total or partial function defined by a set of transformation rules or operators.

Key technical aspects include:

- **Correctness Preservation:**  $(T(p))\forall p \in P, \; \text{Semantics}(p) \equiv \text{Semantics}(T(p))$, or if semantics are intentionally changed, then $T$ satisfies a formal specification $S$.
- **Levels of Abstraction:** Modifications may occur at multiple levels—source code, abstract syntax trees (ASTs), control-flow graphs (CFGs), bytecode, or machine code.
- **Transformation Mechanisms:** Include but are not limited to refactoring, optimization, instrumentation, code generation, code injection, partial evaluation, and metaprogramming.
- **Automation and Tool Support:** Modifications are often automated via compiler passes, source-to-source translators, program synthesizers, or integrated development environments (IDEs) supporting live code editing.
- **Applications:** Bug fixing, performance optimization, feature addition, adaptation to new platforms, security hardening, dynamic program adaptation (e.g., runtime patching), and enabling introspection or reflection.

## 📌 Uses

| **Use Case** | **Description** | **Examples** | **Relevant Techniques** |
| --- | --- | --- | --- |
| 🛠️ **Iterative Development & Maintenance** | Supports continuous evolution of software through edits, extensions, and refactorings while preserving functionality. | Bug fixing, refactoring legacy code, modular restructuring | AST rewriting, semantic diffing, automated refactoring tools |
| 🔄 **Dynamic & Adaptive Systems** | Enables systems to adapt behavior at runtime in response to environmental changes or internal metrics. | Self-healing systems, runtime patching, plugin injection | Hot-swapping, runtime code generation, self-modifying code |
| 🧠 **Meta-Level Computation** | Programs inspect, manipulate, or generate other programs or themselves as data. | Macros in Lisp, template metaprogramming, compiler plugins | Reflection, macros, code synthesis, symbolic evaluation |
| ✅ **Formal Verification & Synthesis** | Transforms programs to meet correctness specifications, derive test cases, or synthesize implementations from declarative specs. | Test input generation, proof-carrying code, verified compilation | Model checking, symbolic execution, program synthesis, supercompilation |
| ⚙️ **Optimization and Specialization** | Tailors general-purpose code into efficient variants specialized for particular inputs, contexts, or hardware targets. | Loop unrolling, partial evaluation, JIT compilation | Static analysis, peephole optimization, specialization passes |
| 🔍 **Instrumentation & Analysis** | Modifies code to collect runtime or compile-time information for diagnostics, profiling, or debugging. | Performance profiling, memory tracing, coverage analysis | Code injection, compiler hooks, intermediate representation (IR) instrumentation |
| 🔐 **Security Hardening & Sandboxing** | Alters code to enforce safety policies or detect/prevent malicious behavior at runtime. | Taint tracking, bounds checking insertion, secure wrappers | Binary rewriting, static instrumentation, control-flow integrity (CFI) |

## 🛠️ Techniques

> **Techniques** = concrete methods or tools (e.g., “LD_PRELOAD” or “LLVM pass”).
> 

| **Category** | **Technique** | **Description** | **Goal** |
| --- | --- | --- | --- |
| **Source-Level** |  |  |  |
|  | **Refactoring** | Structural code improvement without changing behavior. | Maintainability, readability. |
|  | **Source Instrumentation** | Injecting extra code (e.g., logging, counters) into the source. | Profiling, debugging, tracing. |
|  | **Macro Expansion** | Compile-time code substitution using macros. | Code reuse, metaprogramming. |
|  | **Template Metaprogramming** | Generating code at compile time using templates (C++). | Genericity, performance. |
|  | **DSL Embedding** | Inserting code in a domain-specific language embedded in the host language. | Domain-specific abstraction. |
|  | **Conditional Compilation** | Use of `#ifdef`, `#pragma`, etc., to selectively include source code. | Portability, configurability. |
|  | **Aspect-Oriented Injection (Source)** | Use of `aspects` to inject cross-cutting concerns (e.g., logging, security). | Separation of concerns. |
|  | **Preprocessing / Code Generation** | Using external tools (e.g., `m4`, `codegen`) to generate or transform code before compilation. | Automation, configuration management. |
|  | **Mutation Injection** | Systematic changes to code for testing (mutation testing). | Fault injection, test evaluation. |
| **IR-Level / Compilation** |  |  |  |
|  | **Compiler Optimizations (O1-O3)** | Code transformation by compiler passes (e.g., inlining, loop unrolling). | Performance, size reduction. |
|  | **Static Code Transformation** | Use of IR manipulation tools like LLVM passes. | Optimization, instrumentation. |
|  | **Annotation-Guided Compilation** | Use of attributes, pragmas, or decorators to guide compiler behavior. | Performance tuning, inlining, vectorization hints. |
|  | **Intermediate Representation Rewriting** | Modifying code in SSA or bytecode form (e.g., LLVM IR). | Analysis, optimization, verification. |
|  | **Link-Time Optimization (LTO)** | Whole-program optimization during linking. | Global inlining, dead code elimination. |
|  | **Control/Data Flow Injection** | Adding IR elements that affect flow graphs (e.g., dummy branches, trap instructions). | Analysis, obfuscation. |
| **Binary-Level** |  |  |  |
|  | **Binary Instrumentation** | Adding extra instructions to a compiled binary (e.g., with Intel PIN, DynamoRIO). | Profiling, tracing, coverage. |
|  | **Static Binary Rewriting** | Altering the binary layout offline (e.g., binary optimization). | Patching, binary hardening. |
|  | **Binary Translation** | Transforming binary code from one ISA to another (e.g., QEMU, Valgrind). | Portability, analysis. |
|  | **Symbol Table Rewriting** | Changing or injecting entries in ELF/PE symbol tables. | Interposition, sandboxing. |
|  | **Relocation Table Modification** | Adjusting how functions are resolved at load time. | Redirection, replacement of functions. |
|  | **Instruction Substitution** | Replacing instruction sequences with equivalents or traps. | Obfuscation, patching. |
|  | **NOP Injection** | Inserting no-op instructions to alter instruction offsets or timing. | Anti-debugging, timing alteration. |
| **Runtime-Level** |  |  |  |
|  | **Hot Patching** | Injecting new code into a running program’s memory space. | Live updates, runtime fixes. |
|  | **Function Hooking / Trampolines** | Redirecting function calls at runtime to alternative implementations. | Interception, mocking, monitoring. |
|  | **Dynamic Linking Interposition** | Intercepting function calls via mechanisms like `LD_PRELOAD`. | Debugging, sandboxing, shimming. |
|  | **Just-In-Time (JIT) Compilation** | Generating machine code at runtime from IR or bytecode. | Performance, portability, dynamic adaptation. |
|  | **Reflection-Based Rewriting** | Programs modifying their own structure or behavior using runtime introspection. | Adaptation, dynamic behavior injection. |
|  | **Dynamic Bytecode Modification** | Altering JVM/CLR bytecode at runtime (e.g., via agents or instrumentation APIs). | Monitoring, adaptation. |
|  | **Self-Modifying Code** | Code that overwrites or changes its own instructions at runtime. | Optimization, obfuscation (rare today). |
|  | **Inline Caching** | Dynamically modifying code paths for speed based on runtime behavior. | JIT optimization (used in VMs). |
| **Security & Obfuscation** |  |  |  |
|  | **Code Obfuscation** | Transforming code to make reverse engineering difficult. | IP protection, anti-reverse engineering. |
|  | **Control Flow Flattening** | Hiding the original control flow by flattening and adding dispatcher logic. | Obfuscation. |
|  | **Code Virtualization** | Running code on a custom interpreter or VM to hinder analysis. | Tamper resistance. |
|  | **Anti-Debugging Techniques** | Modifying code to behave differently under analysis/debugging tools. | Tamper detection, evasion. |
|  | **Runtime Integrity Checks** | Adding checksums, signatures, or invariants to verify code integrity. | Tamper detection, secure execution. |
|  | **Code Signing Enforcement** | Preventing unauthorized code modification by requiring cryptographic signatures. | Authenticity and trust. |
| **Tool-Assisted Analysis** |  |  |  |
|  | **Dynamic Instrumentation Frameworks** | Tools like DTrace, SystemTap, eBPF dynamically modify kernel/user programs for tracing. | Profiling, observability, forensics. |
|  | **Model Injection for Analysis** | Replacing real modules with mocks or test doubles. | Formal verification, unit testing. |
|  | **Fuzzing Instrumentation** | Adding code to track code paths for better fuzzing input generation. | Automated vulnerability discovery. |

## 🧩 Strategies

> **Strategies** = conceptual patterns, language-agnostic (e.g., “hooking” or “delegation”).
> 

> Hook Point:  Punto de enganche, Punto de inserción, Punto de anclaje, Punto de  Interceptación.
> 

| **Category** | **Strategy** | **Description** | **Common Use Cases** | **Typical Mechanisms** |
| --- | --- | --- | --- | --- |
| **Interception** | **Hooking** | Intercept function/system calls to insert custom logic. | Monitoring, patching, redirection | Trampolines, interposition, vtable hacking |
|  | **Trampolines** | Redirect execution by modifying function entry points. | Redirection, instrumentation | Inline jump, overwritten prologue |
|  | **Function Interposition** | Inject replacement functions dynamically or statically. | Debugging, mocking | `LD_PRELOAD`, dynamic linker tricks |
| **Instrumentation** | **Instrumentation** | Add probes/logs for observability. | Profiling, tracing, testing | Static/dynamic injection |
|  | **Stub Insertion** | Replace real modules with mocks or simplified versions. | Testing, simulation | Mocks, test doubles |
|  | **Mutation Injection** | Systematic perturbation of code for testing. | Mutation testing | AST/binary mutation |
| **Adaptation** | **Monkey Patching** | Replace/extend behavior at runtime. | Prototyping, quick fixes | Object field replacement |
|  | **Just-In-Time Injection** | Modify/generate code dynamically during execution. | Dynamic optimization, adaptation | JITs, runtime patching |
|  | **Reflection / Introspection** | Modify behavior based on program structure introspected at runtime. | Debugging, meta-adaptation | Reflection APIs |
|  | **Inline Caching** | Optimize dynamic dispatch by caching prior behavior. | VM optimization | JIT-generated code paths |
| **Transformation** | **Metaprogramming** | Write code that writes or modifies code. | Automation, abstraction | Macros, templates, generators |
|  | **Code Generation** | Automatically produce source or IR. | Reducing boilerplate, DSLs | Generators, compilers |
|  | **Partial Evaluation** | Precompute portions of a program. | Staged computation, optimization | Specializers, JIT |
|  | **Template Method Pattern** | Use abstract methods to define extensible algorithm steps. | Inheritance-based reuse | OOP subclassing |
|  | **Behavioral Overriding** | Override or redefine specific behaviors in subclasses. | Extension, plugin systems | Virtual methods, polymorphism |
| **Routing / Delegation** | **Proxy / Wrapper** | Interpose intermediary to control behavior. | Logging, access control | Forwarders, decorators |
|  | **Delegation** | Pass behavior to another component for execution. | Modularity, composition | Wrappers, message forwarding |
|  | **Patch-and-Forward** | Modify behavior, then defer to original. | Transparent modification | Combined wrapper + original call |
| **Composition / Injection** | **Aspect-Oriented Programming** | Inject cross-cutting concerns orthogonally to main logic. | Logging, validation, security | Weaving at compile/load/runtime |
|  | **Dependency Injection** | Provide external components rather than hardcoding dependencies. | Decoupling, testability | Constructor, property, or service injection |
| **Optimization** | **Devirtualization** | Replace indirect (virtual) calls with direct ones. | Performance optimization | Compiler passes, JIT |
|  | **Polymorphic Dispatch** | Dynamically resolve behavior based on runtime types. | Dynamic dispatch | Vtables, type checks |
| **Security / Evasion** | **Control Flow Hijacking** | Divert or manipulate execution flow. | Obfuscation, attack simulation | Jumps, return-to-libc, trampoline chains |
|  | **Dynamic Dispatch Swizzling** | Swap method pointers at runtime. | Mocking, hotfixing, plugin systems | Vtable rewriting, method map editing |
| ,,, | ,,, |  |  |  |
|  | Observer Pattern |  |  |  |
|  | Callbacks |  |  |  |
|  | Plugin Architecture |  |  |  |
|  | Dependency Injection / Inversion of Control |  |  |  |
|  | Template Pattern |  |  |  |

## 📚 References**📚**

- [Hooking](https://en.wikipedia.org/wiki/Hooking)
- [AspectJ](https://en.wikipedia.org/wiki/AspectJ)
- [BEAM](note.html?n=technica/computation/language-system/conceptual-model-language-system/beam.md)
- [Java Bytecode](note.html?n=technica/computation/language-system/conceptual-model-language-system/java-bytecode.md)
- 
- https://github.com/jacoco/jacoco