---
tags: [intermediate-representation, language-system]
---

# Intermediate Representation

- [CIL](note.html?n=technica/computation/language-system/conceptual-model-language-system/cil.md), [Compiler System](note.html?n=technica/computation/language-system/conceptual-model-language-system/compiler-system.md)

> A **program representation scheme** refers to a formal method or structure used to encode a program's logic, data, and associated metadata into a specific format. This can include intermediate representations (IRs), source code, object code, or higher-level constructs such as abstract syntax trees, control flow graphs, or bytecode. These representations serve as an intermediary between different stages of program processing (e.g., compilation, optimization, or execution) and are designed to facilitate analysis, transformation, and efficient execution. The scheme ensures consistency in layout, maintains necessary semantic properties, and supports toolchain compatibility across various platforms and environments.
> 

> Note. More than Intermediate; this is about `Representing Programs`.
> 

## Representation Schemes

| **Category** | **Subcategory** | **Scheme** | **Description** |
| --- | --- | --- | --- |
| **Compiler IRs** | **Abstract Syntax Tree (AST)** | AST | A tree representation of the syntactic structure of source code. |
|  | **Control Flow Graphs (CFG)** | CFG | A graph representing the flow of control within a program. |
|  | **Static Single Assignment (SSA)** | SSA Form | A form of IR where each variable is assigned exactly once, simplifying analysis. |
|  | **Three-Address Code (TAC)** | TAC | A low-level IR where each instruction has at most three operands. |
|  | **Quadruples** | Quadruples | An IR where each instruction is represented as a tuple of four elements. |
|  | **Postfix Notation** | Reverse Polish Notation (RPN) | An IR where operators follow their operands (e.g., used in stack-based VMs). |
|  | **Register Transfer Language (RTL)** | RTL | A low-level IR used in compilers to describe operations between registers. |
|  | **Continuation-Passing Style (CPS)** | CPS | An IR where control flow is explicitly represented using continuations. |
|  | **Lambda Calculus** | Lambda Calculus | A mathematical formalism used as an IR for functional programming languages. |
|  | **Gated Single Assignment (GSA)** | GSA | An extension of SSA that includes predicates for conditional execution. |
| **Virtual Machine IRs** | **Bytecode** | Java Bytecode | The IR used by the Java Virtual Machine (JVM). |
|  |  | Python Bytecode | The IR used by the Python interpreter. |
|  |  | .NET Common Intermediate Language (CIL) | The IR used by the .NET runtime. |
|  | **Stack-Based IR** | Forth, PostScript | IRs that use a stack-based execution model. |
|  | **Register-Based IR** | Dalvik Bytecode | The IR used by the Android Runtime (ART), which is register-based. |
|  | **Parrot Bytecode** | Parrot | The IR used by the Parrot virtual machine for dynamic languages. |
|  | **Lua Bytecode** | Lua | The IR used by the Lua virtual machine. |
| **Hardware IRs** | **LLVM IR** | LLVM Intermediate Representation | A low-level, typed IR used by the LLVM compiler infrastructure. |
|  | **SPIR-V** | Standard Portable Intermediate Representation (SPIR-V) | A binary IR for GPU shaders and compute kernels. |
|  | **WebAssembly (Wasm)** | WebAssembly | A stack-based IR designed for execution in web browsers. |
|  | **PTX (Parallel Thread Execution)** | PTX | NVIDIA's IR for GPU programming. |
|  | **HSAIL (Heterogeneous System Architecture Intermediate Language)** | HSAIL | An IR for heterogeneous computing (CPU+GPU). |
| **Domain-Specific IRs** | **Graphics Shader IRs** | GLSL IR, HLSL IR | Intermediate representations for graphics shader languages. |
|  | **Machine Learning IRs** | TensorFlow Graph, ONNX | IRs for representing machine learning models and computations. |
|  | **Database Query IRs** | Relational Algebra, Query Plans | IRs for representing and optimizing database queries. |
|  | **Hardware Description Languages (HDLs)** | Verilog, VHDL | IRs for describing digital circuits and hardware. |
|  | **Music IRs** | MusicXML, MIDI | IRs for representing musical scores and performances. |
| **Optimization IRs** | **Loop Optimization IRs** | Polyhedral Model | An IR for optimizing loops in numerical computations. |
|  | **Dataflow IRs** | Dataflow Graphs | IRs that represent programs as graphs of data dependencies. |
|  | **Dependence Graphs** | Program Dependence Graphs (PDG) | IRs that capture control and data dependencies in programs. |
|  | **Dependence Analysis IRs** | Static Single Information (SSI) | An IR for tracking data dependencies in programs. |
|  | **Intermediate Optimization IRs** | Sea of Nodes | A graph-based IR used in some compilers for optimization. |
| **Hybrid IRs** | **Multi-Level IRs** | MLIR (Multi-Level Intermediate Representation) | A flexible IR that supports multiple levels of abstraction. |
|  | **Graph-Based IRs** | Sea of Nodes | A graph-based IR used in some compilers for optimization. |
|  | **Portable IRs** | Portable Intermediate Representation (PIR) | IRs designed for cross-platform compatibility. |
| **Specialized IRs** | **Security IRs** | Boogie, Why3 | IRs for formal verification and security analysis. |
|  | **Quantum Computing IRs** | QIR (Quantum Intermediate Representation) | IRs for representing quantum computing programs. |
|  | **Biological IRs** | SBML (Systems Biology Markup Language) | IRs for modeling biological systems. |

## References

- https://en.wikipedia.org/wiki/Intermediate_representation
- https://en.wikipedia.org/wiki/Sea_of_nodes
- https://github.com/libfirm
- https://en.wikipedia.org/wiki/Control-flow_graph
- https://v8.dev/blog/leaving-the-sea-of-nodes