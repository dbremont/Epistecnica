# Nystrom, R. (2021). Crafting interpreters. Genever Benning.


```python
@book{nystrom2021crafting,
  title={Crafting interpreters},
  author={Nystrom, Robert},
  year={2021},
  publisher={Genever Benning}
}

```

## Notes

---

> …
> 

## Index

## Introduction

> A **programming language** is a formally defined system of symbolic rules and syntactic constructs equipped with a semantics that maps well-formed expressions to computational behaviors or abstract machine transitions, enabling the precise specification, manipulation, and execution of algorithms and data structures.
> 

> The mechanism by which we encode and express the rules that drive (underlies) a given  computation.
> 

> **Note:** The pedagogy involves teaching language system concepts while developing two systems: an interpreter and a bytecode virtual machine.
> 

![image.png](documents/books/nystrom-2021-crafting-interpreters-genever-benning/image.png)

### A Map of the Territory

> “You must have a map, no matter how rough. Otherwise you wander all over the place. In The Lord of the Rings I never made anyone go farther than he could on a given day.” - J. R. R. Tolkien
> 

> Though a map simplifies and omits, it enables effective orientation within complex terrain.
> 

![A Map of the Language System Mountain.](documents/books/nystrom-2021-crafting-interpreters-genever-benning/image-1.png)

A Map of the Language System Mountain.

![image.png](documents/books/nystrom-2021-crafting-interpreters-genever-benning/image-2.png)

The Parts of a Language:

- **Scanning or Lexing**: A **scanner** (or **lexer**) takes in the linear stream of characters and chunks
them together into a series of something more akin to “words”. In programming languages, each of these words is called a **token**. Some tokens are single characters, like `(` and `,`. Others may be several characters long, like numbers (`123`), string literals (`"hi!"`),
and identifiers (`min`).
- **Parsing (Uncover the Grammatical Structure Underlying a Sentence)**:  A **parser** takes the flat sequence of tokens and builds a tree structure that mirrors the nested nature of the grammar. These trees have a couple of different names—**parse tree** or **abstract syntax tree**—depending on how close to the bare syntactic structure of the source language they are. In practice, language hackers usually call them **syntax trees**, **ASTs**, or often just **trees**.
- **Static Analysis**:
    - **Binding or Resolution**: For each **identifier**, we find out where that name is defined
    and wire the two together. This is where **scope** comes into play—the region of source code where a certain name can be used to refer to a certain declaration.
    - **Type Analysis**: Type Checking, …
    - **Data Models Used for Static Analysis**: …
        - Control Flow Models
        - Data Flow Models
        - Abstract Memory Models
        - Type and Effect Systems
        - Program Dependency Graphs (PDG)
        - Symbolic Models
        - Semantic and Logical Models
        - Symbol Table
- **Program Representation**:
    - IR (Intermediate Representation)
    - …
- **Optimization:** Once we understand what the user’s program means, we are free to swap it out
with a different program that has the *same semantics* but implements them more
efficiently—we can **optimize** it.
    - Constant Folding
    - …
- **Code Generation**: We have applied all the optimizations we can think of to the user’s program. The last step is converting it to a form the machine can actually run. In other words, **generating code** (or **code gen**), where “code” here usually refers to the kind of primitive assembly-like instructions a CPU runs and not the kind of “source code” a human might want to read.
- **Virtual Machine**:  A **Bytecode Virtual Machine (BVM)** is an abstract computing architecture that executes programs represented in **bytecode**—a compact, intermediate, platform-independent binary format. The BVM emulates a CPU and runtime environment in software, interpreting or just-in-time compiling the bytecode into native machine instructions at runtime.
- **Runtime:** The collection of services, mechanisms, and infrastructure provided by the execution environment that supports and manages the behavior of a program while it runs.
- Taxonomy of Language Systems:
    - Single Pass Compiler,
    - Tree-walk interpreters,
    - Transpiler,
    - Just-in-time compilation
- **Compiling** is an *implementation technique* that involves translating a source language to some other—usually lower-level—form. When you generate bytecode or machine code, you are compiling. When you transpile to another high-level language, you are compiling, too.
- List of Open Source Languages
    - ‣
    - https://github.com/ruby/ruby

### The Lox Language

## A Tree-Walk Interpreter

### Scanning

### Representing Code

### Parsing Expressions

### Evaluating Expressions

### Statements and State

### Control Flow

### Functions

### Resolving and Binding

### Classes

### Inheritance

## A Bytecode Virtual Machine

### Chunks of Bytecode

### A Virtual Machine

### Scanning on Demand

### Compiling Expressions

### Types of Values

### Strings

### Hash Tables

### Global Variables

### Jumping Back and Forth

### Calls and Functions

### Closures

### Garbage Collection

### Classes and Instances

### Methods and

## References

- https://craftinginterpreters.com/contents.html
