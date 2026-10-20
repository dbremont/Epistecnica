---
tags: [language-system, translation]
---

# Compiler System

- [Intermediate Representation](note.html?n=technica/computation/language-system/conceptual-model-language-system/intermediate-representation.md), [Code Generation](note.html?n=technica/computation/language-system/conceptual-model-language-system/code-generation.md), [Bytecode Virtual Machine](note.html?n=technica/computation/language-system/conceptual-model-language-system/bytecode-virtual-machine.md), [Parsing](note.html?n=technica/computation/language-system/conceptual-model-language-system/parsing.md), [Grammar](note.html?n=technica/computation/language-system/conceptual-model-language-system/grammar.md)

> A **compiler** is a software tool that translates source code written in a high-level programming language into a lower-level language (such as machine code) that can be executed directly by a computer.
> 

> **Compiler intrinsics** are built-in functions or operations provided by the compiler that directly map to low-level machine instructions or specific hardware features, often used to optimize performance or access specialized processor capabilities.
> 

## Compilation Strategies

> Compilation strategies are methods by which computer programs are transformed from one form of code into another. The strategies range from traditional static compilation to more dynamic and adaptive methods.
> 

Here's a table that outlines several key compilation strategies, along with a brief description of each:

| **Compilation Strategy** | **Description** |
| --- | --- |
| **Static Compilation** | Code is compiled into machine language at development time before execution. Languages like C and C++ use this approach. |
| **Dynamic Compilation** | Also known as Just-In-Time (JIT) compilation, this strategy compiles code at runtime, allowing for optimizations based on current usage patterns. |
| **Ahead-of-Time (AOT) Compilation** | Compiles bytecode to machine code before execution but after the software has been distributed, as seen in .NET Native and Android’s use of ART. |
| **Interpreter** | It executes source code directly without compiling it to machine language, and it is often used for scripting languages like Python and Ruby. |
| **Hybrid Compilation** | Combines both compiled and interpreted approaches, often using an interpreter initially and a JIT compiler for frequently executed code paths, as seen in Java and Python. |
| **Profile-Guided Optimization (PGO)** | Uses data collected during program execution to optimize subsequent compilations, enhancing performance. |
| **Incremental Compilation** | It compiles parts of the program as needed without recompiling the whole, which is beneficial in development environments for rapid testing and debugging. |
| **Cross Compilation** | Compiles code for a different target platform than the one on which the compiler is running, used for developing software for embedded systems or when targeting multiple platforms. |

## Components

The parts of a compiler typically include:

| **Part of Compiler** | **Description** |
| --- | --- |
| **Lexical Analyzer** | Breaks the source code into tokens or lexemes. |
| **Syntax Analyzer** | Builds the parse tree or abstract syntax tree (AST) to represent the syntactic structure of the program. |
| **Semantic Analyzer** | Performs semantic analysis, checks for type compatibility, and enforces language rules. |
| **Intermediate Code Generator** | Converts the source code into an intermediate representation for further processing. |
| **Optimization Engine** | Optimizes the intermediate code to improve the efficiency of the generated executable. |
| **Code Generator** | Translates the optimized code into the target language (e.g., machine code). |
| **Symbol Table** | Stores information about the program's variables, functions, and other symbols. |
| **Error Handler** | Detects and reports errors or warnings during the compilation process. |
| **Linker** | Resolves external references and combines multiple object files into a single executable file. |
| **Loader** | Loads the executable file into memory for execution. |
| **Preprocessor** | Handles preprocessor directives, such as macro expansions and file inclusions. |
| **Debugger** | Provides debugging capabilities to analyze and troubleshoot the compiled program. |

## Representation

Here’s a table summarizing the various ways to represent a program:

| **Representation** | **Description** |
| --- | --- |
| **Source Code** | Represented as a text file containing the original program written in a high-level programming language. |
| **High-Level Language** | A program expressed in a high-level programming language, abstracting away low-level details. |
| **Bytecode** | Represents the program in terms of a model of computation, often used by virtual machines (e.g., Java bytecode). |
| **Machine Code** | Represents the program using a specific machine code model, such as X86 assembly language. |
| **AST (Abstract Syntax Tree)** | Represents the program as a tree structure, with expressions and sub-expressions modeled using program entities. |
| **IR (Intermediate Representation)** | A translation of the program into another abstract model of computation, used for optimization and analysis. |
| **Three-Address Code** | A low-level representation where each instruction uses at most three operands, commonly used as an intermediate representation for optimization and code generation. |

## Analysis

> 

**Name Resolution / Binding**

In an expression like a + b, we know we are adding a and b, but we don’t know what those names refer to. Are they local variables? Global? Where are they defined?

Mapping these names to the correct symbols is called binding or resolution. We find out where that name is defined for each identifier and wire the two together. This is where scope comes into play—the region of source code where a certain name can be used to refer to a specific declaration.

**Type Checking**

Type checking ensures that a programming follows the rules established by a type system.

## Name Mangling

> 

https://en.wikipedia.org/wiki/Name_mangling

## Register Allocation

> **Register Allocation** refers to the process of assigning variables or temporaries to the limited set of CPU registers in a program’s execution environment.
> 

> **Register allocation** occurs during the optimization phase of a compiler, often after instruction selection but before instruction scheduling. Its main goal is to decide which variables (either compiler-generated temporaries or program variables) should reside in the limited registers provided by the processor. Since the number of registers is finite, effective register allocation reduces memory access overhead (from RAM or the stack) by keeping frequently used variables in registers.
> 

**Register Allocation Mechanisms**:
The process typically involves a **graph coloring** or **interference graph** model:

- **Interference Graph Construction**: Each variable (or virtual register) is a node. An edge is drawn between two nodes if their lifetimes overlap, meaning they must be assigned to different registers.
- **Graph Coloring**: The interference graph is then "colored," with each color representing a distinct register. The objective is to assign registers in a way that no two interfering variables share the same register.

**Types of Register Allocation**:

- **Global Register Allocation**: This allocation is done across the entire program, considering all variables and temporaries that will be alive throughout the program’s execution.
- **Local Register Allocation**: In contrast, local register allocation is performed on a function level, considering only the variables live within the scope of a particular function.
- **Spilling**: If there aren’t enough registers to hold all variables, some variables must be "spilled" to memory (stack or heap), leading to extra memory accesses. The register allocator decides which variables are spilled based on their frequency of use or their lifetime in the program.

**Heuristics and Algorithms**:
Several algorithms exist to handle register allocation, each with varying complexity:

- **Graph Coloring Algorithms**: The simplest and most commonly used technique in modern compilers is **graph coloring**, which approximates the problem of register allocation as a graph coloring problem. The coloring process attempts to assign registers such that no two variables that interfere (i.e., are live at the same time) are assigned the same register. A key issue here is that graph coloring is an NP-complete problem in its most general form, so compilers often use heuristics or approximation algorithms.
- **Linear Scan Register Allocation**: A simpler, often faster approach, which allocates registers by scanning through the program’s instruction sequence and assigning registers to live ranges in a greedy fashion. While less precise, it’s particularly used for just-in-time (JIT) compilers or in environments where speed is prioritized over optimality.
- **Priority-Based Allocation**: Variables that are frequently used or whose lifetimes are long (i.e., their live ranges span across many instructions) are often assigned to registers first, based on priority heuristics.

## References

- Scott, M. L. (2015). Programming language pragmatics (4th ed.). Morgan Kaufmann.
- Parr, T. (2010). Language implementation patterns. Pragmatic Programmers.
- Cooper, K. D., Torczon, L. (2012). Engineering a Compiler. Elsevier.
- Yeates, S. A. (1997). Design Pattern in Garbage Collection.
- Nystrom, R. (2021). Crafting Interpreters. Genever Benning.
- Gabbrielli, M., & Martini, S. (2010). Programming languages: principles and paradigms. Springer Science & Business Media.
- Sovetov, P. N. "Development of dsl compilers for specialized processors." *Programming and Computer Software* 47.7 (2021): 541-554.
- [On the Formalization of Programming Languages: Early History and Approaches](https://link.springer.com/content/pdf/10.1007/3-540-08766-4_8.pdf)
- [Domain Specific Languages](http://cs448h.stanford.edu/DSEL-Little.pdf)
- [Name mangling](https://en.wikipedia.org/wiki/Name_mangling)
- [Domain Specific Languages](http://bitrary.softf1.com/images/b/bc/1997_12_15_Domain_Specific_Languages_by_Paul_Hudak.pdf)
- [Syntax Design](https://cs.lmu.edu/~ray/notes/syntaxdesign/)
- [Creating a language using only assembly language](https://speakerdeck.com/nineties/creating-a-language-using-only-assembly-language)
- [A Survey of Programming Language Memory Models](https://dl.acm.org/doi/abs/10.1134/S0361768821060050)
- [Compiling for Runtime Code Generation](https://www.cs.cornell.edu/talc/papers/compile_rtcg.pdf)
- [Runtime Code Generation with JVM and CLR](https://www.itu.dk/people/sestoft/rtcg/rtcg.pdf)
- [Fully Abstract Models of Programming Languages](https://era.ed.ac.uk/bitstream/handle/1842/14496/Stoughton1986.Pdf?isAllowed=y&sequence=1)
- [A survey of real-time capabilities in functional languages and compilers](https://onlinelibrary.wiley.com/doi/abs/10.1002/cpe.4902)
- [Data structure models for programming languages](https://dl.acm.org/doi/abs/10.1145/1115880.1115882)
- [Programming Languages as Thought Models](https://www.cs.kau.se/cs/education/courses/dvgc01/lectures/Rechenberg.pdf)
- [An Abstract View of Programming Languages](https://www.ics.uci.edu/~jajones/INF102-S18/readings/09_Moggi.pdf)
- [Abstract machines for programming language implementation](https://www.inf.ed.ac.uk/teaching/courses/lsi/diehl_abstract_machines.pdf)
- [AoT Compiled Languages Metaprogramming: A Nascent Trend Or Another Esoteric Practice?](https://dic.dzinko.org/metaprogramming-overview-classification)
- [Position-independent code](https://www.wikiwand.com/en/Position-independent_code)
- https://en.wikipedia.org/wiki/Register_allocation
- https://news.ycombinator.com/item?id=23644391