---
tags: [code-generation, language-system]
---

# LLVM (Low Level Virtual Machine)


> In this note we will explore the LLVM project.
> 

> [LLVM Project](https://llvm.org/?utm_source=chatgpt.com) is a modular, retargetable compiler toolchain and optimization infrastructure centered around a strongly typed, SSA-based intermediate representation (LLVM IR) that enables language-agnostic whole-program analysis, aggressive multi-level optimization pipelines, target-independent transformation passes, and machine-specific code generation through a layered architecture comprising frontends (e.g., Clang), IR canonicalization and analysis frameworks, selection DAG/global instruction selection backends, MC-layer object emission, JIT/AOT compilation subsystems, link-time optimization (LTO/ThinLTO), profile-guided optimization (PGO), sanitization/instrumentation frameworks, and reusable compiler/runtime libraries exposing stable semantic abstractions over heterogeneous architectures, object formats, calling conventions, debug metadata, and execution environments.
> 

> LLVM is a huge project - with a very unstable API.
> 

> Which Very Deep Questions Should I be Asking About LLVM?
> 

Guiding questions:

- What are the hidden costs of abstraction inside LLVM?
- What are LLVM’s biggest architectural bottlenecks?
- What is the real difference between AOT and JIT in LLVM?
- Which are some missuses of the LLVM core libraries?
- Which are the main computational elements (abstractions) that underlies computational system description via LLVM Core Libraries?
- Which are the performance characteristic of LLVM Core Libraries?
- Which principles underlying the LLVM Core Libraries? Which are the design issues?

## LLVM Project Product Set

| Type of Product | Product | Description | Instance Set |
| --- | --- | --- | --- |
| Core Infrastructure | LLVM Core Libraries | Provides a modern, source- and target-independent optimizer and code generation support for many CPUs, built around the LLVM Intermediate Representation (IR). | IR, Pass Manager, Analysis Framework, Target Backends, MC Layer, JIT Infrastructure, Bitcode System, Support Libraries |
| Compiler Frontend | Clang | An "LLVM native" C/C++/Objective-C compiler known for fast compiles, useful error and warning messages, and as a platform for source-level tools. | `clang`, `clang++`, `clang-cl`, libclang, clangd, ASTMatchers, Driver, Parser, Sema |
| Compiler Frontend | Flang | A modern Fortran compiler that generates high-performance code and supports Fortran 2023 and all official standards back to Fortran 77. | Frontend Driver, Parser, Semantic Analyzer, FIR (Fortran IR), OpenMP Support |
| Compiler Frontend | MLIR | A novel approach to building reusable and extensible compiler infrastructure, aimed at reducing the cost of building domain-specific compilers and improving compilation for heterogeneous hardware. | Dialects, Rewrite Engine, Affine Framework, Tensor Compiler Components, Conversion Infrastructure |
| Optimization & Analysis | Polly | Implements cache-locality optimizations, auto-parallelism, and vectorization using a polyhedral model. | Polyhedral Optimizer, Dependence Analysis, Loop Transformations, Automatic Parallelization |
| Debugger | LLDB | A great native debugger built on LLVM and Clang libraries, using the Clang ASTs and expression parser, LLVM JIT, and disassembler. | `lldb`, Remote Debugger, Expression Evaluator, Symbol Loader, Platform Plugins |
| Linker | LLD | A new, high-performance linker that is a drop-in replacement for system linkers and runs much faster. | ELF Linker (`ld.lld`), COFF Linker (`lld-link`), Mach-O Linker, Wasm Linker |
| Post-Link Optimizer | BOLT | A post-link optimizer that improves application code layout by optimizing based on execution profiles gathered by a sampling profiler. | Binary Rewriter, Profile-Guided Layout Optimizer, Function Reordering |
| Symbolic Execution | KLEE | A "symbolic virtual machine" that uses a theorem prover to evaluate all dynamic paths through a program to find bugs and prove function properties; it can produce test cases when it detects a bug. | Symbolic Executor, SMT Solver Integration, Test Case Generator, POSIX Runtime |
| Standard Library | libc++ | A standard-conformant and high-performance implementation of the C++ Standard Library, including full support for C++11 and C++14. | Containers, Algorithms, Iterators, Ranges, Threading Library |
| Standard Library | libc++ ABI | Provides the Application Binary Interface (ABI) for the libc++ standard library. | Exception Handling ABI, RTTI Support, Typeinfo System |
| Standard Library | libc | A high-performance, standards-conformant implementation of the C Standard Library, fully integrated with LLVM. | String Library, Math Library, StdIO, Syscall Abstractions |
| Runtime Library | compiler-rt | Provides highly tuned implementations of low-level code generator support routines and runtime libraries for dynamic testing tools like AddressSanitizer, ThreadSanitizer, and MemorySanitizer. | ASan, TSan, MSan, UBSan, Builtins, Profile Runtime, XRay |
| Standard Library | pstl (Parallel STL) | An implementation of the C++ standard library algorithms with support for execution policies, as specified in the C++17 standard. | Parallel Algorithms, Vectorized Algorithms, Execution Policies |
| Parallel Runtime | OpenMP | Provides an OpenMP runtime for use with the OpenMP implementation in Clang and Flang. | `libomp`, Device Runtime, Task Scheduler, OpenMP Offloading |
| Offloading | offload | Aims to provide tooling, runtimes, and APIs to execute code on accelerators or other "co-processors". | GPU Runtime, Device Plugin System, Host-Device Coordination |
| Unwinder | libunwind | A production-quality unwinder with platform support for DWARF unwind info, SjLj, and ARM EHABI. | DWARF Unwinder, ARM EHABI Support, Stack Frame Traversal |
| Standard Library | libclc | Aims to implement the OpenCL standard library. | OpenCL Builtins, GPU-Oriented Math Functions |
| Testing | cross-project-tests | A testing infrastructure designed for tests that require dependencies on multiple LLVM sub-projects. | Integration Tests, Runtime Validation, Multi-Project Regression Tests |
| Extra Tools | clang-tools-extra | Contains additional tools for Clang, such as the clang-tidy static analyzer. | clang-tidy, clang-format, clang-query, include-fixer, modularize |
| Command-Line Tools (Selection) | `opt`, `llc`, `lli`, `llvm-as`, `llvm-dis`, `llvm-link`, `llvm-ar`, `llvm-nm`, `llvm-objdump`, `llvm-readelf`, `llvm-cov`, `llvm-profdata` | A set of command-line utilities for tasks such as running optimizations (`opt`), generating native code (`llc`), executing bitcode with a JIT (`lli`), assembling/disassembling bitcode (`llvm-as`/`llvm-dis`), linking (`llvm-link`), archiving (`llvm-ar`), symbol inspection (`llvm-nm`), and various profiling and analysis tasks. | Optimizers, Assemblers, Disassemblers, Binary Inspectors, Profilers, Coverage Tools, Archive Tools |

## LLVM Core Library Set

> See shell `bin/llvm-config --cxxflags --ldflags --system-libs --libs core`.
> 

| Library | Linker Config Name | Description |
| --- | --- | --- |
| `LLVMCore` | `core` | Fundamental LLVM IR infrastructure including `Module`, `Function`, `BasicBlock`, `Instruction`, types, constants, symbol tables, metadata, and IR construction/manipulation APIs. |
| `LLVMSupport` | `support` | Low-level foundational utility layer providing allocators, containers (`SmallVector`, `DenseMap`), threading primitives, file systems, command-line parsing, error handling, YAML/JSON support, and portability abstractions. |
| `LLVMIRReader` | `irreader` | Parser and loader for textual LLVM IR (`.ll`) into in-memory IR structures. |
| `LLVMBitReader` | `bitreader` | Deserializes LLVM bitcode (`.bc`) into LLVM IR structures. |
| `LLVMBitWriter` | `bitwriter` | Serializes LLVM IR into LLVM bitcode format. |
| `LLVMAsmParser` | `asmparser` | Parses LLVM assembly language into IR form. |
| `LLVMAnalysis` | `analysis` | Compiler analysis framework containing alias analysis, dominance analysis, loop analysis, scalar evolution, CFG analysis, memory dependence analysis, etc. |
| `LLVMTransformUtils` | `transformutils` | Shared transformation utilities used by optimization and canonicalization passes. |
| `LLVMInstCombine` | `instcombine` | Peephole and algebraic instruction simplification engine for canonical IR normalization. |
| `LLVMScalarOpts` | `scalaropts` | Scalar optimization passes such as GVN, SCCP, DCE, LICM, reassociation, and CFG simplification. |
| `LLVMipo` | `ipo` | Interprocedural optimization infrastructure including inlining, dead argument elimination, global optimization, and function attribute propagation. |
| `LLVMVectorize` | `vectorize` | Automatic vectorization passes including loop vectorization and SLP vectorization. |
| `LLVMPasses` | `passes` | Pass manager registration and optimization pipeline orchestration infrastructure. |
| `LLVMCodeGen` | `codegen` | Target-independent machine code generation framework including instruction selection, scheduling, register allocation, and lowering. |
| `LLVMSelectionDAG` | `selectiondag` | DAG-based instruction selection and lowering framework used in backend code generation. |
| `LLVMGlobalISel` | `globalisel` | Modern global instruction selection framework replacing parts of SelectionDAG. |
| `LLVMTarget` | `target` | Abstract target-machine interface and backend integration framework. |
| `LLVMMC` | `mc` | Machine Code (MC) infrastructure for assembly emission, disassembly, object generation, and binary encoding abstraction. |
| `LLVMObject` | `object` | Object-file abstraction layer supporting ELF, COFF, Mach-O, WASM, and archive parsing. |
| `LLVMBitstreamReader` | `bitstreamreader` | Bitstream parsing infrastructure used by bitcode and related binary formats. |
| `LLVMDebugInfoDWARF` | `debuginfodwarf` | DWARF debug information parsing and manipulation infrastructure. |
| `LLVMDemangle` | `demangle` | Symbol demangling infrastructure for C++, Rust, Swift, and other languages. |
| `LLVMExecutionEngine` | `executionengine` | Legacy JIT execution framework for dynamic IR execution. |
| `LLVMOrcJIT` | `orcjit` | Modern ORC-based modular JIT compilation infrastructure. |
| `LLVMLinker` | `linker` | LLVM IR linker for merging multiple modules into unified IR programs. |
| `LLVMLTO` | `lto` | Link-Time Optimization (LTO/ThinLTO) infrastructure for whole-program optimization. |
| `LLVMFrontendOpenMP` | `frontendopenmp` | OpenMP frontend/runtime integration infrastructure. |
| `LLVMProfileData` | `profiledata` | Profile-guided optimization (PGO) data handling and instrumentation support. |
| `LLVMCoverage` | `coverage` | Code coverage analysis and instrumentation infrastructure. |
| `LLVMSymbolize` | `symbolize` | Symbol resolution and source mapping infrastructure for diagnostics/debugging. |
| `LLVMBinaryFormat` | `binaryformat` | Shared binary-format constants and structural definitions for ELF, COFF, Mach-O, DWARF, etc. |
| `LLVMTextAPI` | `textapi` | Apple Text-Based Stub (`.tbd`) parsing and generation infrastructure. |
| `LLVMRemarks` | `remarks` | Optimization remark serialization and analysis framework. |
| `LLVMTableGen` | `tablegen` | TableGen processing infrastructure for declarative compiler/backend specification generation. |
| `LLVMFrontendOffloading` | `frontendoffloading` | Infrastructure for heterogeneous offloading targets (GPU/accelerator compilation support). |
| `LLVMWindowsManifest` | `windowsmanifest` | Windows manifest generation and embedding support. |
| `LLVMObjCARCOpts` | `objcarcopts` | Objective-C ARC optimization passes. |
| `LLVMCoroutines` | `coroutines` | Coroutine transformation and lowering infrastructure. |
| `LLVMExtensions` | `extensions` | Experimental or platform-specific extension integration infrastructure. |

## QA

### Does the LLVM command tools used `LLVM Core Libraries`?

> Most LLVM command-line tools are thin or moderately layered applications built directly on top of the [LLVM Core Libraries](https://llvm.org/docs/?utm_source=chatgpt.com) infrastructure.
> 

| Tool Type | Example Tool | Uses LLVM Core Libraries For |
| --- | --- | --- |
| IR optimizer | opt | Pass management, IR transformations, analyses |
| Static compiler backend | llc | Instruction selection, register allocation, machine code generation |
| IR assembler/disassembler | llvm-as / llvm-dis | IR parsing and serialization |
| Object file tools | llvm-objdump | Object format parsers, disassembly framework |
| Linker | lld | Support libraries, object abstractions, target info |
| Debugger | LLDB | DWARF parsers, disassembler, JIT support |
| Frontend driver | Clang | LLVM IR generation, optimization pipelines, backend emission |

### What is the average abstractional, semantic, and implementation complexity involved in composing LLVM Core Library computational primitives into functioning compiler, analysis, transformation, or execution systems?

> 

### Which others Computational Systems uses LLVM?

| Category | System | System Type | Description |
| --- | --- | --- | --- |
| Programming Language Systems | Clang | Standalone Tool | C/C++/Objective-C frontend targeting LLVM IR and native backends. |
| Programming Language Systems | Rust Compiler | Standalone Tool | Rust compiler using LLVM for optimization and code generation. |
| Programming Language Systems | Swift | Standalone Tool | Native language toolchain built atop LLVM infrastructure. |
| Programming Language Systems | Julia | Standalone Tool | Dynamic language using LLVM-based JIT specialization and optimization. |
| Programming Language Systems | Zig | Standalone Tool | Systems language with LLVM backend integration. |
| Programming Language Systems | Kotlin Native | Standalone Tool | Native Kotlin compiler using LLVM backend infrastructure. |
| Programming Language Systems | Crystal | Standalone Tool | Native compiled language using LLVM for code generation. |
| Programming Language Systems | Nim | Standalone Tool | Multi-backend language with optional LLVM backend support. |
| Programming Language Systems | Mojo | Standalone Tool | MLIR/LLVM-based high-performance programming language. |
| Database Systems | PostgreSQL | Standalone Tool | Database engine using LLVM for JIT query compilation. |
| Database Systems | DuckDB | Standalone Tool | Analytical database experimenting with LLVM-based execution optimization. |
| Database Systems | Apache Impala | Standalone Tool | Distributed SQL engine using runtime code generation via LLVM. |
| Database Systems | HyPer | Standalone Tool | Research database using compiled query execution with LLVM. |
| Browser/Web Systems | WebAssembly | Computational Standard / Runtime Target | Portable low-level virtual ISA commonly generated through LLVM backends. |
| Browser/Web Systems | Emscripten | Standalone Tool | LLVM-to-WebAssembly compilation infrastructure. |
| GPU / Heterogeneous Systems | SYCL | Library / Toolchain | Heterogeneous compute ecosystem leveraging LLVM backends. |
| GPU / Heterogeneous Systems | OpenCL | Framework / Runtime | GPU and accelerator execution systems frequently compiled through LLVM. |
| GPU / Heterogeneous Systems | Mesa3D | Library Stack | Graphics and shader infrastructure using LLVM for shader compilation. |
| GPU / Heterogeneous Systems | TensorFlow XLA | Compiler Subsystem | Tensor computation compiler lowering optimized kernels through LLVM. |
| Scientific Computing Systems | Numba | Library | Python JIT compiler using LLVM for numerical specialization. |
| Scientific Computing Systems | Halide | Library / DSL Compiler | Image-processing compiler framework targeting LLVM backends. |
| Scientific Computing Systems | TVM | Compiler Framework | Tensor compiler stack lowering ML kernels through LLVM. |
| Scientific Computing Systems | MLIR | Compiler Infrastructure Library | Multi-level compiler IR ecosystem integrated with LLVM lowering pipelines. |
| Security / Binary Analysis Systems | AddressSanitizer | Library / Instrumentation Runtime | Memory error detection instrumentation system built on LLVM passes. |
| Security / Binary Analysis Systems | ThreadSanitizer | Library / Instrumentation Runtime | Concurrency race detection system using LLVM instrumentation. |
| Security / Binary Analysis Systems | libFuzzer | Standalone Tool / Library | Coverage-guided fuzzing framework integrated with LLVM instrumentation. |
| Security / Binary Analysis Systems | McSema | Library / Toolchain | Binary lifting framework translating machine code into LLVM IR. |
| Security / Binary Analysis Systems | Remill | Library | Instruction semantics lifting framework targeting LLVM IR. |
| Security / Binary Analysis Systems | BOLT | Standalone Tool | Post-link binary optimizer using LLVM infrastructure. |
| Runtime / VM Systems | ORC JIT | Library | Modular runtime JIT compilation infrastructure. |
| Runtime / VM Systems | GraalVM LLVM Runtime | Runtime Library | LLVM bitcode execution runtime inside GraalVM. |
| Runtime / VM Systems | Mono LLVM Backend | Runtime Compiler Backend | LLVM-powered optimization/code generation backend for .NET runtime. |
| Embedded / OS Toolchains | Android NDK | Toolchain | Android native development ecosystem based on Clang/LLVM. |
| Embedded / OS Toolchains | Apple Xcode | IDE / Toolchain | Apple development environment using LLVM-based native toolchains. |
| Embedded / OS Toolchains | Linux Kernel BPF | Kernel Compilation Subsystem | LLVM-based compilation path for eBPF kernel programs. |
| AI / ML Compiler Systems | XLA | Compiler Infrastructure | Tensor optimization and lowering system targeting LLVM. |
| AI / ML Compiler Systems | IREE | Compiler Framework | MLIR/LLVM-based machine learning compiler runtime stack. |
| AI / ML Compiler Systems | Glow | Compiler Framework | Neural network compiler lowering computations through LLVM backends. |
| AI / ML Compiler Systems | TorchInductor | Compiler Subsystem | PyTorch graph compiler leveraging LLVM-related lowering paths. |

## References

- https://github.com/llvm/llvm-project
- https://github.com/dbremont/language-system-labs
- LLVM Tutorial: Kaleidoscope (Implementing a Language with LLVM) https://github.com/ghaiklor/llvm-kaleidoscope
- [LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation](https://llvm.org/pubs/2004-01-30-CGO-LLVM.pdf)
- A Minimal LLVM JIT example for LLVM-5 [https://gist.github.com/38/39e7b514d916ed6fa6a2bba629fdf6ff](https://gist.github.com/38/39e7b514d916ed6fa6a2bba629fdf6ff)
- A Minimal LLVM JIT example for LLVM-5 https://gist.github.com/38/39e7b514d916ed6fa6a2bba629fdf6ff
- A Complete Guide to LLVM for Programming Language Creators https://mukulrathi.com/create-your-own-programming-language/llvm-ir-cpp-api-tutorial/
- A Minimal LLVM JIT example for LLVM-5 https://gist.github.com/38/39e7b514d916ed6fa6a2bba629fdf6ff
- Speeding up query execution in PostgreSQL using LLVM JIT compiler https://llvm.org/devmtg/2016-09/slides/Melnik-PostgreSQLLLVM.pdf
- See https://github.com/postgres/postgres/blob/master/src/backend/jit/llvm/llvmjit_inline.cpp
- https://eli.thegreenplace.net/2014/01/15/some-thoughts-on-llvm-vs-libjit
- Speeding up query execution in PostgreSQL using LLVM JIT compiler https://llvm.org/devmtg/2016-09/slides/Melnik-PostgreSQLLLVM.pdf
- A Minimal LLVM JIT example for LLVM-5 https://gist.github.com/38/39e7b514d916ed6fa6a2bba629fdf6ff
- A Complete Guide to LLVM for Programming Language Creators https://mukulrathi.com/create-your-own-programming-language/llvm-ir-cpp-api-tutorial/
- https://eli.thegreenplace.net/2014/01/15/some-thoughts-on-llvm-vs-libjit
- How practical is LLVM really? https://www.reddit.com/r/ProgrammingLanguages/comments/hhxisw/how_practical_is_llvm_really/
- LLVM https://aosabook.org/en/v1/llvm.html
- https://github.com/asmjit/asmjit
- https://github.com/avast/retdec
- https://asmjit.com/
- https://gcc.gnu.org/onlinedocs/jit/
- https://news.ycombinator.com/item?id=23137345
- https://news.ycombinator.com/item?id=13334168
- https://news.ycombinator.com/item?id=9998140
- https://llvmweekly.org/
- https://news.ycombinator.com/item?id=46588837