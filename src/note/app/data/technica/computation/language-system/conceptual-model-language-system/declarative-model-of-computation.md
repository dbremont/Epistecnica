---
tags: [model-of-computation]
---

# Declarative Model of Computation

- [Parsing](note.html?n=technica/computation/language-system/conceptual-model-language-system/parsing.md), [Lazy Evaluation](note.html?n=technica/computation/language-system/conceptual-model-language-system/lazy-evaluation.md), [Time](note.html?n=technica/computation/language-system/conceptual-model-language-system/time.md), [Lambda Calculus](note.html?n=technica/computation/language-system/conceptual-model-language-system/lambda-calculus.md), [Functional Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/functional-model-of-computation.md)

> The **Declarative Model of Computation** is a programming paradigm where the focus is on specifying **what needs to be computed** rather than **how to compute it**.
> 

> A **declarative model of computation** defines programs as expressions whose meanings are given by a **formal semantics**, often based on **mathematical logic**, **rewrite systems**, or **denotational semantics**. The execution model revolves around **evaluating expressions**, often **lazily** or **by demand**, to reach a result.
> 

> A **declarative model** of computation in which a program is expressed as a set of constraints or rules that describe the desired output or behavior, rather than a sequence of imperative instructions that specify how to compute the output. In other words, instead of specifying the steps to achieve a result, a declarative program defines what the result should be based on a set of conditions or relationships between inputs and outputs.
> 

> "The nice thing about **declarative programming** is that you can write a specification and run it as a program. The nasty thing about declarative programming is that some clear specifications make incredibly bad programs. The hope of declarative programming is that you can move from a specification to a reasonable program without leaving the language."
> 
> 
> — *The Craft of Prolog* , Richard O’Keefe
> 

## Key Questions

- (Problem - Process → Model of Computation) In which model of computation is this process most naturally or easily expressed?
- (Model of Computation → Process) What kinds of processes can be naturally represented in this computational model?
- Which programming paradigms does this model of computation enable?
- How is declarative programming connected to AI-assisted software development?

**Features**: - History Sensitivy: No - Predictable: Deterministic - Environmet Interaction: No - Mathematical Tractability: Simple - Declarative Programs are compositional.

There are different types of declarative models of computation, including:

- **Logic programming**: a declarative programming paradigm that uses rules and logic to express a program’s behavior. The most well-known logic programming language is Prolog.
- **Functional programming**: a declarative programming paradigm that emphasizes the use of functions and immutable data structures to express computations. Examples of functional programming languages include Haskell, Lisp, and ML.
- **Constraint programming**: a declarative programming paradigm that allows programmers to specify constraints that must be satisfied by the program’s inputs and outputs. Constraint programming is often used in optimization problems and scheduling.

Declarative models of computation can provide benefits such as improved modularity, reusability, and maintainability of code. They can also enable automatic optimization and parallelization of computations, as well as support for formal verification and reasoning about program correctness.

**¿What computations does the model help us to encode?**

The model helps us encode computations that involve expressing the desired output or result without specifying the step-by-step procedure to achieve it.

**¿What is the abstract machine?**

The abstract machine in the Declarative Model is an interpreter or compiler that translates declarative code (high-level specifications) into lower-level instructions or actions to perform the computation.

**¿How to encode computations?**

Computations in the Declarative Model are encoded by providing high-level specifications or declarations of the problem or desired outcome, typically using languages like declarative programming languages (e.g., SQL for databases, Prolog for logic programming) or descriptive formats (e.g., markup languages like HTML or CSS). The underlying abstract machine then interprets or compiles these declarations to carry out the computation, handling the details of how to achieve the desired result.

## Connotation of ‘Declarative’

Declarative programming is called “declarative” because it emphasizes the declaration of **rules** or **constraints** that **govern the behavior of a program**, rather than specifying a series of steps or operations to be performed. In a declarative program, the programmer declares the desired outcome or behavior of the program, and the program’s execution is determined by a set of rules or constraints that describe how the problem should be solved.

The emphasis on declarative specification allows the programmer to focus on the **“what”** of the problem, rather than the **“how”**, which can lead to more concise, modular, and expressive programs. The program can also take advantage of automated reasoning and optimization techniques to efficiently solve the problem, without the need for the programmer to specify every step of the computation.

Declarative programming is often contrasted with imperative programming, which emphasizes the specification of a sequence of steps or operations to be performed in order to solve a problem. In an imperative program, the programmer specifies exactly how the program should compute the desired outcome, often using mutable state and control structures like loops and conditionals.

**Levels**: - A descriptive declarativeness. HTML/XHTML. - A programable declarativness. Turing Machine

## Langauge

Representation: - Declarative Variables / Dataflow Variables. - Value Store: A store where all variables are bound to values. - Partial Store: A store that may contain unbouded variables. - Variable to Variable binding. - Dataflow Variables

Types: - Numbers - Atoms - Booleans - Records - Tuples - Lists - Strings

Computation: - Procedure - Primitive Operations / Statements and Expressions.

## Machine

> Evaluating functions (list of statements) over partial data structures.
> 

Key : - Memory / Envirounemnt - Stack - Semantic Statements - Execution State - Computation

## Techniques

**Interactive Computation**:

`fun` {Iterte *Si*}

`if` { IsDone *Si* } `then` *Si*

`else` *S*i+1

*S*i+1 = {Transform *Si*}

{Iterate *S*i+1}

`end`

`end`

Tools: - **Procedures** to create locus of computations, helps to manage complexity.

**Recursive Computations**:

In a interactive computation there is a linear control flow model; an interactive computation has a mroe general control flow model that can be seen as a **tree**.

In order to **structure recursive** computations think dividing the problems into: - Base Case - Recursive Case

Tools: - **Accumulator**: The technique of threading a state through nedted procedure calls is called accumulator programming. - **-**

**Information Trees**

An ordered binary tree can be used as a repository of informtion, if we defined three operations: looking up, inserting, and deleting entries.

To look up for information in an ordered bianry tree means to search wheater a given key is present in one of the three nodes, and if so, return the information present at that node.

**Hiher Order Programming**

It’s a set of techniques that are introduced when procedures are also values.

Basic Operations: - **Procedural Abstraction**: the ability to convert a set of statements in to a procedure value. - **Genericity**: the ability to pass a procedure value to a procedure call. - **Instantiation**: the ability to return a procedure value as a result of a procedure call. - **Embedding**: the hability to put procedure value into data structures.

**Data Driven Techniques** …

**Lazy Evaluation**

Lazy evaluation is a technique in which expressions are only evaluated when they are needed. This allows for more efficient use of resources and can avoid unnecessary computations.

**Currying**

Currying is a technique in which a function that takes multiple arguments is transformed into a series of functions, each of which takes a single argument. This can make it easier to compose functions and create new abstractions.

**Data Structures**: - Stack - Quues - Tree - List

## Derived Models

> ….
> 

## Programming Paradigms

> Which **programming paradigms** does this **model of computation** enable?
> 

## Case Studies

> ….
> 

## References

- [Denotational Semantics](https://app.notion.com/p/Denotational-Semantics-21fc0f5171ec8020bc8fc54803adf870?pvs=21)
- [‣](https://app.notion.com/p/10e598edb7908183ba99f3b404ea8627?pvs=21)
- https://en.wikipedia.org/wiki/Declarative_programming
- https://stackoverflow.com/questions/28291127/declarative-models-of-computation-in-physical-machines
- https://en.wikipedia.org/wiki/Warren_Abstract_Machine
- [‣](https://app.notion.com/p/10e598edb790816bb840d76fb2831140?pvs=21)
- https://www.youtube.com/watch?v=Ru2oZGRJTQg