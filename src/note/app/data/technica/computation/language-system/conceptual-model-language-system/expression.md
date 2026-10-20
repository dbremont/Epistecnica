---
tags: [linguistic-abstraction]
---

# Expression


> An **expression** is a syntactic construct that can be evaluated to produce a value or result within a computational system. It consists of one or more operands (which can be variables, constants, or functions) and operators (such as arithmetic, logical, relational, or functional operators) that define how the operands are combined or transformed.
> 

## Operator Precedence

> To simplify, resolve ambiguities by using parentheses. This ensures that the expression is evaluated in the correct order.
> 

> **Operator precedence models** refer to the rules that govern the order in which different operations are performed in expressions, especially in mathematical, logical, or programming contexts. These models define how operators with different precedence levels interact to determine the evaluation order of expressions. The evaluation order can be crucial in ensuring that calculations are done correctly and consistently.
> 

### **Mathematical Operator Precedence Model**

This model defines the precedence of mathematical operators used in arithmetic expressions. The general order of precedence is:

1. **Parentheses** `()` – operations inside parentheses are evaluated first, overriding all other precedence rules.
2. **Exponentiation** `^`, `*` – typically has higher precedence than multiplication and division.
3. **Multiplication and Division** , `/` – evaluated from left to right.
4. **Addition and Subtraction** `+`,  – also evaluated from left to right.

### **Boolean Operator Precedence Model**

> In logical operations, the precedence of operators determines how boolean expressions are evaluated. The common order of precedence is:
> 
1. **NOT** (negation) – evaluated first.
2. **AND** – evaluated after negation.
3. **OR** – evaluated last.

### **Programming Language Operator Precedence Model**

> In programming languages, operator precedence follows a similar structure but may have additional operators or variations based on the language's design. Here's a typical hierarchy:
> 
1. **Postfix operators** `++`, `-` (increment, decrement) – highest precedence.
2. **Prefix operators** `++`, `-`, , `+`, `!`, `~` – evaluated after postfix.
3. **Multiplicative operators** , `/`, `%`.
4. **Additive operators** `+`, .
    1. **Relational operators** `==`, `!=`, `<`, `<=`, `>`, `>=`.
5. **Logical AND** `&&`.
6. **Logical OR** `||`.
7. **Assignment operators** `=`, `+=`, `=`, etc.
8. **Ternary conditional operator** `?:` – often with lower precedence than assignment but higher than logical operators.

## Evaluation Model & Call Semantics

> See more in [](https://app.notion.com/p/1c5c0f5171ec8088b71cdda914a4d5d6?pvs=21).
> 

| **Evaluation Strategy** | **Description** | **Example Languages** |
| --- | --- | --- |
| **Eager Evaluation (Strict Evaluation)** | Expressions are evaluated as soon as they are bound to variables. | C, Java, Scheme |
| **Lazy Evaluation (Non-strict Evaluation)** | Expressions are evaluated only when their values are actually needed during program execution. | Haskell |
| **Call by Name** | Arguments are passed to functions without being evaluated first, and the arguments are re-evaluated each time they are used in the function. | ALGOL 60, Simula |
| **Call by Need** | A variant of call by name where arguments are evaluated only once, and the result is cached for subsequent uses. | Haskell (implementation of lazy evaluation) |
| **Call by Value** | Actual parameters are evaluated before the function is applied, and the resulting values are passed to the function. | C, Scheme, MATLAB |
| **Call by Sharing** | Function arguments are passed by reference, meaning that mutable arguments can be altered within the function. | Python, Java, Ruby |
| **Call by Reference** | The address of the actual parameter is passed to the function, allowing the function to modify the original parameter. | Fortran, C++ |
| **Short-Circuit Evaluation** | Logical expressions are evaluated left to right, and the evaluation stops as soon as the result is determined. This avoids unnecessary computations. | C, Java, Python |
| **Memoization** | A technique where function results are cached based on input arguments, avoiding redundant computations for the same inputs. | Python (with `functools.lru_cache`), Haskell, JavaScript |

## References

- https://en.wikipedia.org/wiki/Associative_property
- https://en.wikipedia.org/wiki/Operator_associativity
- https://en.wikipedia.org/wiki/Expression_(mathematics)