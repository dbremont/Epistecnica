---
tags: [model-of-computation]
---

# Lambda Calculus

- [Declarative Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/declarative-model-of-computation.md), [Turing Machine](note.html?n=technica/computation/language-system/conceptual-model-language-system/turing-machine.md), [Functional Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/functional-model-of-computation.md)

> Note: This is the foundational basis of the declarative models of computation.
> 

> The **lambda calculus** is a **minimal, universal model of computation** based on function abstraction and application. It provides a syntactic framework for defining and manipulating **anonymous functions** through variable binding and substitution, with **no primitive data types or control structures**.
> 

![](https://lh3.googleusercontent.com/-UlDDkX52Ra0/YIXTvhmzH-I/AAAAAAAACvg/2hsLntnO5rkBekTYnalMEBAzIgWjZJkxACLcBGAsYHQ/w640-h296/terms.png)

## Formalism

The untyped lambda calculus consists of expressions defined inductively as follows:

**Syntax** (λ-terms)

Let `x ∈ Var` be variables.

```
M, N ::= x            -- variable
       | λx.M         -- abstraction (function)
       | M N          -- application
```

That is:

- **Variables**: identifiers representing parameters or expressions.
- **Abstraction**: function definitions (λx.M), binding variable `x` in body `M`.
- **Application**: function application (M N), applying function `M` to argument `N`.

### 🔁 **Semantics**

> Lambda calculus operates through **β-reduction**, the rule of function application via substitution.
> 

**Core Reduction Rules:**

1. **α-conversion (α-equivalence)**: Renaming of bound variables. `λx.x ≡α λy.y`
2. **β-reduction (β-equivalence)**: Function application via substitution. `(λx.M) N →β M[x := N]` This means: replace every free occurrence of `x` in `M` with `N`.
3. **η-conversion (optional in some systems)**: Expresses extensionality. `λx.(f x) ≡η f      if x ∉ FV(f)`

### 🧮 **Evaluation Strategies**

The order of β-reduction affects termination and normalization:

- **Normal order**: Leftmost outermost — always finds normal form if it exists.
- **Applicative order**: Leftmost innermost — evaluates arguments first (used in strict evaluation).
- **Call-by-name**: Like normal order but avoids evaluating arguments unless needed.
- **Call-by-need**: Lazy evaluation (like in Haskell) — shares computed values to avoid recomputation.

### 🔗 **Free vs Bound Variables**

- A variable `x` is **bound** in `λx.M`; otherwise, it's **free**.
- `FV(M)` denotes the set of free variables in M.

Example:

```
λx.(x y)        -- `x` is bound, `y` is free
```

### ⛓️ **Substitution Formalized**

If `M[x := N]` is the substitution of `N` for `x` in `M`, we must avoid **variable capture** using α-conversion.

Substitution rules:

```
x[x := N] = N
y[x := N] = y                   if x ≠ y
(λx.M)[x := N] = λx.M           (x is bound)
(λy.M)[x := N] = λy.(M[x := N]) if x ≠ y, y ∉ FV(N)
(M1 M2)[x := N] = M1[x := N] M2[x := N]
```

### 🏗️ **Computational Expressivity**

Lambda calculus is **Turing-complete** and can encode:

- **Booleans**:
    
    ```
    TRUE  := λx.λy.x
    FALSE := λx.λy.y
    ```
    
- **Pairs**:
    
    ```
    PAIR := λx.λy.λf.f x y
    ```
    
- **Natural Numbers (Church encoding)**:
    
    ```
    0 := λf.λx.x
    1 := λf.λx.f x
    2 := λf.λx.f (f x)
    ...
    ```
    
- **Recursion**: via fixed-point combinators like **Y combinator**:
    
    ```
    Y := λf.(λx.f (x x)) (λx.f (x x))
    
    ```
    

## History

> The **lambda calculus** was introduced by **Alonzo Church** in the **early 1930s** as part of an effort to formalize the foundations of mathematics and logic. Its original goal was to provide a foundation for functions, computation, and effective calculability. Church's initial formulation was part of a broader system of logic and was intended as an alternative to set-theoretic foundations.
> 

> In **1936**, Church proved the **undecidability of the Entscheidungsproblem** using the lambda calculus, around the same time as **Alan Turing** independently introduced the **Turing machine**. Church and Turing showed that their models of computation were equivalent in expressive power, establishing the **Church–Turing thesis**: that all effectively computable functions can be computed by these formal systems.
> 

> Originally, the lambda calculus was **untyped**, allowing arbitrary self-application and leading to paradoxes. To address these, **typed lambda calculi** were later developed, starting with **Church’s Simple Theory of Types** in the 1940s. This gave rise to a family of typed systems, eventually influencing **type theory**, **proof theory**, and **functional programming languages**.
> 

> In the **1970s–1980s**, the lambda calculus became a theoretical foundation for **functional programming**, particularly influencing languages like **LISP**, **ML**, and **Haskell**. It also became central to the **Curry–Howard correspondence**, which connects proofs in logic to programs in type theory.
> 

> Today, the lambda calculus serves as a **core theoretical model of computation**, a **basis for programming language semantics**, and a bridge between **logic**, **type systems**, and **computation**.
> 

## Encoding

Here is a list of methods for **encoding** in **Lambda Calculus**:

- **Church Encoding**: A method developed by Alonzo Church to represent data and operations within the Lambda Calculus.
- **Scott Encoding**: A technique used to encode data types as functions in the Lambda Calculus, named after Dana Scott.
- **Gödel Numbering**: An encoding method representing data and formulas in the Lambda Calculus as natural numbers.
- **Church-Rosser Encoding**: A way to encode pairs and other data structures that ensure the Church-Rosser property.
- **Continuation-Passing Style (CPS) Encoding** is a technique for representing control flow in the Lambda Calculus, often used in functional programming languages.
- **Y Combinator Encoding**: An encoding method that allows for recursion in the Lambda Calculus using fixed-point combinators.
- **Curry-Howard Correspondence**: A mapping between types and logical propositions that allows encoding of logical systems in the Lambda Calculus.

## Typed Lambda Calculus

> Extensions of untyped λ-calculus introduce **types**:
> 
1. **Simply Typed Lambda Calculus (STLC)**: assigns types to terms, disallows self-application.
2. **System F**: polymorphic types via second-order lambda calculus.
3. **Dependent Types**: types can depend on terms (as in Coq, Agda).
4. **Linear Types**: resource-sensitive λ-calculus.

## Practice

### Evaluation

1. `(λx. x) y`
2. (λx. λy. x) a b
3. (λx. x x) (λx. x x)
4. (λx. λy. x y) (λz. z) a
5. (λx. λy. λz. x z (y z)) (λa. a) (λb. b)
6. (λf. λx. f (f x)) (λy. y + 1) 2
7. (λx. (λy. y) x) z
8. (λx. λy. x) ((λz. z z) (λz. z z)) b
9. Evaluate `(λn. λf. λx. f (n f x)) TWO` on the basis of (Church numerals)

```bash
ZERO := λf. λx. x  
ONE  := λf. λx. f x  
TWO  := λf. λx. f (f x)
```

## QA

### How does a lambda expression denote the return value?

Given a lambda expression:

```bash
λx. M
```

- This defines a function that takes an argument `x`.
- The expression `M` is the **body** and represents the **result** (i.e., the return value) of the function when it is applied.

When you apply the function to a value `N`:

```bash
(λx. M) N → M[x := N]
```

- The expression evaluates by substituting `N` for `x` in `M`.
- The resulting expression is the **evaluated return value**.

### How do we evaluate a lambda expression to obtain its value?

> **Lambda expressions are evaluated by a process called *reduction*, where function applications are simplified by systematically applying rules such as β-reduction.** The *value* of a lambda expression is the result of this reduction process, typically a **normal form** (a term with no further reductions possible).
> 

### How to define recursion in Lambda Calculus?

> 

## References

- [Introducción al Cálculo Lambda Usando Racket](https://www.researchgate.net/publication/339000267_Introduccion_al_calculo_lambda_usando_Racket)
- [Church Encoding](https://en.wikipedia.org/wiki/Church_encoding)
- [Mogensen–Scott encoding](https://en.wikipedia.org/wiki/Mogensen%E2%80%93Scott_encoding)
- [Intro to hacking with the lambda calculus](https://www.lesswrong.com/posts/D4PYwNtYNwsgoixGa/intro-to-hacking-with-the-lambda-calculus)
- Rojas, Raúl. "A tutorial introduction to the lambda calculus." arXiv preprint arXiv:1503.09060 (2015).
- Scott, Dana. "Lambda calculus: some models, some philosophy." Studies in Logic and the Foundations of Mathematics. Vol. 101. Elsevier, 1980. 223-265.
- [Term Rewriting System](https://app.notion.com/p/Term-Rewriting-System-909cccb0aa0b4c4a9b7c1d856f4bc252?pvs=21)
- https://en.wikipedia.org/wiki/System_F