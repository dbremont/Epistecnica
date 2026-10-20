---
tags: [type-system]
---

# Type Checking

- [Type System](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-system.md)

> **Type Checking**: The process of verifying that types are used consistently and correctly in a program.
> 

> **Type Checking** ensures that valid operations are invoked on variables and expressions.
> 

> **A Type Checker** implements a type system - check the rules defined by the type system. (Type System, Program) -> Yes / No
> 

> **Dynamic checking**. A collection of run time tests aimed at detecting and preventing forbidden errors.
> 

> **Statically checked language**: A language where good behavior is determined before execution.
> 

> **Strongly checked language**: A language where no forbidden errors can occur at run time (depending on the definition of forbidden error).
> 

> **Dynamically checked language**: A language where good behavior is enforced during execution.
> 

> **Decidability**: Decidability refers to the ability of a type-checking algorithm to determine, in a finite amount of time, whether a given program satisfies the system's type rules. A type system is decidable if it can mechanically determine whether a program is well-typed without using manual proof or analysis.
> 

> **Typing error**: An error reported by a typechecker to warn against possible execution errors.
> 

## Type Checking Algorithms

Here's a table that organizes the list of type-checking algorithms along with a brief description of each, suitable for understanding their usage in various programming environments:

| **Algorithm** | **Description** |
| --- | --- |
| Hindley-Milner Algorithm | Used in functional programming languages like Haskell and ML; provides efficient type inference for polymorphism. |
| Algorithm W | A specific implementation of the Hindley-Milner type inference method known for producing principal types. |
| Algorithm X | A variant of the Hindley-Milner system adapted for more complex type inference scenarios. |
| Nominal Type Checking | Common in Java and C#; checks types based on name equivalence and proper class/interface hierarchies. |
| Structural Type Checking | Used in TypeScript and Go; types are compatible if they share the same structure, regardless of name. |
| Flow-based Type Checking | Found in TypeScript; analyzes how values flow through code to determine types dynamically across branches. |
| Dependent Type Checking | Supports dependent types (types depending on values) in languages like Idris and Coq. |
| Duck Typing | Informal method used in dynamically typed languages like Python, based on method and property presence. |
| Subtype Polymorphism Checking | Ensures correct usage of subtypes and supertypes in method overriding and object instantiation. |
| Generics and Type Parameters | Checks generics in Java, C#, Scala, etc., ensuring flexible code with correct use of type parameters. |

This table encapsulates the essence of each type-checking algorithm, highlighting their primary applications and characteristics, which are crucial for language design and compiler implementation.

## References

- [Static Checking](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/01-static-checking/)
- [An accessible introduction to type theory and implementing a type-checker](https://mukulrathi.com/create-your-own-programming-language/intro-to-type-checking/)
- [What are the broad classes of type checking algorithms?](https://www.reddit.com/r/ProgrammingLanguages/comments/perr4i/what_are_the_broad_classes_of_type_checking/)
- [Type Checking / Princetonce](https://www.cs.princeton.edu/courses/archive/fall18/cos326/lec/17-type-checking.pdf)
- [So you want to write a type checker (2014)](https://news.ycombinator.com/item?id=15583515) ([languagengine.co](http://languagengine.co/))
- Dunfield, Jana, and Neelakantan R. Krishnaswami. "Complete and easy bidirectional typechecking for higher-rank polymorphism." ACM SIGPLAN Notices 48.9 (2013): 429-442.