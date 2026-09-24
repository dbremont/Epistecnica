# Van Roy, P., & Haridi, S. (2004). Concepts, techniques, and models of computer programming. MIT press.


```bash
@book{van2004concepts,
  title={Concepts, techniques, and models of computer programming},
  author={Van Roy, Peter and Haridi, Seif},
  year={2004},
  publisher={MIT press}
}

```

## Notes

---

> A **model of computation** (computation model) (**or computational formalism)** is a formal system that defines how computations are **represented** and **executed**. How is this process represented? And what are the **semantics** of this **representation**?
> 

> A **computation model** is associated with a set of **techniques and methods** to articulate computations for the model of computation; called **programming paradigm**.
> 

> **Programming**: A General human activity, to mean the act of extending or chancing a system's functionality.
> 

> **Note:** The word *programming language* is synonymous with a model of computation.
> 

> **Note**: An abstraction is informally defined as a tool that solves a specific problem—either within a model of computation or related to the process being represented itself.
> 

> **Note (Meta)**: Given a process   $p \in \text {Process Space}$  → $\text{Model of Computation}$  that “best represent the process.”
> 

> **Note**:  Model of Computation:  Process Space → Representation Space.
> 

> The universe writes itself into existence one step at a time, like a computation unfolding.
Just as a program is an underlying rule that drives the computation, the laws of nature act as the underlying rules that drive the unfolding of the universe.
In both cases, the process builds itself incrementally, step by step, from within.
> 

> A **computation** writes into existence one step at a time; state and state change; driven by the underlying rule (the program).
> 

> Computation (Program)  = Universe (Laws of Physics).
> 

QA:

- How to study a  model of computation?  [How to study a  model of computation?](Van%20Roy,%20P%20,%20&%20Haridi,%20S%20(2004)%20Concepts,%20techniqu%2010e598edb790816bb840d76fb2831140.md)
- Is there a minimal basis of programming languages that can simulate all models of computation up to observational equivalence? [Is there a minimal basis of programming languages that can simulate all models of computation up to observational equivalence?](Van%20Roy,%20P%20,%20&%20Haridi,%20S%20(2004)%20Concepts,%20techniqu%2010e598edb790816bb840d76fb2831140.md)
- How are models of **computation characterized**?  They can be characterized by the concepts that underlies their representational power.

**Approaches to Learning a New Language**

- Kernel Language: …
- A Foundational Calculus:  *π*-calculus,   *λ*-calculus, …
- A Virtual Machine: …

Goals:

- Study Models of Computation & Express Computation  With Them.
- Learn how to design new Abstractions.

![**Note:** A model of computation formalizes the informal concept of programming paradigms.](https://miro.medium.com/v2/resize:fit:1400/1*wS8DsmEejvsswkQjNA-BoQ.png)

**Note:** A model of computation formalizes the informal concept of programming paradigms.

## Index

## Introduction to Programming Concepts

> This chapter introduces the **most important topics** in programming.
> 

- Variable:  Identifier that is bound to a value.
- Function: A name that abstraction a way in a local computation.
- Abstraction Mechanisms:
    - Functional Abstraction,
    - Type Abstraction
- Data Structures
    - List
- **Pattern Matching**: Note, **Pattern Matching** has many semantics; in our `Bremontix Ars` we explore them all.
- Evaluation:
    - Correctness:  A program is correct if it does what we would like it to do. How do we prove that a program is correct?
    - Mathematical Induction
    - Nondeterminism: …
- Performance
    - Complexity: …
- Program Execution:
    - Lazy Evaluation (Demand Driven): An evaluation strategy in which expressions or computations are only evaluated when they are needed. This allows computations on infinite data structures.
    - Eager Evaluation  : …
- Programming Strategies
    - Higher Order Programming: Uses of higher order constructs like higher order functions.
    - **Recursion** is a strategy for defining a computation or data structure in terms of smaller instances of itself, along with a base case. The resulting construct is called a *recursive computation* or *recursive data structure*.
- Threads of Computation (I Have Really Good Notes About This - Bremontix Ars)
    - Concurrency
    - **Dataflow:** What happens if we try to use a variable that hasn’t been bound yet?  If your answer is *“we wait until it is,”* then you're thinking in terms of dataflow. Dataflow concurrency allows expressing incremental computations.  I believe this concept is **polysemic**—it has multiple meanings. You should explore its other  denotations as well.
    - Time: …
- State:
    - Explicit State:  Modelling a store of value; the store can have different values at different points of times.
    - Explicit state makes computations involving change, iteration, and control far more natural and efficient to express. Without it, you must restructure your program around immutable values and explicit state-passing, which increases cognitive and syntactic overhead.
- Objects: A function with internal object.
- Class: A factory of objects.
- Atomicity: Indivisible operations.

## General Computation Models

### Declarative Computation Model

> See more in [‣](https://app.notion.com/p/3d05f4aa25284406ac8f3d2a35af5810?pvs=21).
> 

> Key Questions:
> 
> - (Problem - Process → Model of Computation) In which model of computation is this process most naturally or easily expressed?
> - (Model of Computation → Process) What kinds of processes can be naturally represented in this computational model?

Programming Paradigms:

- Functional Programming,
- Logic Programming,

Derived Models:

- Concurrent Declarative Model

Formal Grammar:

- Tokenizer
- Parser
- Grammar of Grammar - BNF.
    - How to Read Grammar
    - Properties of Grammars: Context-Free; Context-Sensitive Grammars.
    - Ambiguity
- Language Semantics
- Linguistic Abstraction
- Syntatic Sugar
- Abstract Machine
    - Memory Management
    - 

Declarative Model of Computation:

- **Fundamental Data Structure**: Single Assignment Store → Declarative Variables.
- **Partial Value** is a data structure that may contain unbounded variables.
- Dataflow Variables
- Pattern Matching
- Procedures
- Expression
- Control Flow:
    - Conditional Statement.
    - Procedure Application
    - Exceptions
- Type System: Dynamic Typing,
    - (Basic Types)Values :
        - Numbers
        - Atoms
        - Booleans
        - Records
        - Tuples
        - List
        - String
        - Procedures
- Case Studies
    - Lambda Calculus
- Other Programming Concepts
    - Concurrency: dataflow, lazy evaluation,  message passing, active objects, monitors, and transactions.
    - Exception Handling
    - Components
    - Capabilities (For encapsulation and security)
    - …

### Declarative Programming Techniques

- What is declarativeness?
- Iterative Computation
- Recursive Computation
- Programming with recursion
- Time and space efficiency
- Higher-order programming
- Abstract data types
- Nondeclarative needs
- Program design in the small

### Message-Passing Concurrency

### Explicit State

### Share-State Concurrency

### Relational Programming

## Specialized Computation Models

### Graphical User Interface Programming

### Distributed Programming

### Constraint Programming

## Semantics

### Language Semantics

## QA

### How to study a  model of computation?

Note: When studying a model of computation ask yourself:

**Representation:** *How is the computational process formally described?*

- What structures encode inputs, outputs, and state (e.g., strings, graphs, functions)

**Semantics:** *What do these representations mean?*

- How are operations defined (e.g., transitions, reductions, rewrites)?
- What is the model’s notion of "computation" (e.g., reaching a final state, normalizing a term)?

**Relation to Other Models:** How does this model fit within the broader landscape (or hierarchy) of computation models?

### Is there a minimal basis of programming languages that can simulate all models of computation up to observational equivalence?

> There are many languages that are hard to classify; they embed multiple models of computation, like Erlang.
> 
- Logic Model → Prolog
- Functional Model → Haskell & Standard ML
- Java → OOP
- …

## References

- van Roy, P., & Haridi, S. (2004). *Concepts, techniques, and models of computer programming*. MIT Press.
