# Rust: 📜 Language Specification

> A **language specification** formally defines the syntax, semantics,  and behavior of a programming language, including its lexical  structure, grammar, type system, execution model, and standard  libraries, serving as the authoritative reference for implementers and 
developers.
> 

## Lexical Grammar

> aka. Lexical Structure,
> 

> 🔤 **Lexical grammar defines the *tokens***—the smallest meaningful units in the source code.
> 

> **Lexical structure**: Defines how characters combine into **tokens** (identifiers, keywords, literals) and handles **whitespace, comments, and delimiters**.
> 

Guiding Questions:

- [Token Space] How are tokens (keywords, identifiers, literals) defined?
- What characters are allowed in identifiers (e.g., Unicode, sigils like `$`)?
- Does the language use significant whitespace (e.g., Python) or explicit delimiters (e.g., C)?
- *Does the Language Supports Macro Constructs?*
- What is the **literal default type**?  - [X: **🏷️** Type System](https://app.notion.com/p/X-Type-System-fc2456113c894e699643d8ce60a4647f?pvs=21).

| **Lexical Construct** | **Description** | **Case(s)** |
| --- | --- | --- |

## **Syntactic** Grammar

> aka. Linguistic Abstraction - Physical Manifestation of Computational Entity; *Computational Element.*
> 

> 📚 The **syntactic grammar defines how tokens are combined** into valid **expressions**, **statements**, **declarations**, and **programs**.
> 

Guiding Questions:

- What class of formal grammar best describes the grammar of this language? (Note: This may include grammars within or outside the Chomsky hierarchy.)
- Are there syntactic ambiguities in the Language?

## Syntactical Structure

> **Syntactical Construct**: A **language feature** (e.g., loops, functions, conditionals) defined by the grammar, forming the structure of valid programs.
> 

> Literal:  In programming and computer science, a **literal** is a **notation for representing a fixed value directly in the source code**. It’s the actual value written in the code, not a variable or an expression that computes a value.
> 

> **Linguistic Abstractions:**  Set of abstraction building in the syntax of the language.
> 

> Note: This should be improved.
> 

Guiding Questions:

- What are the core language constructs (variables, functions, control flow)?
- *Does the Language Support Macro Constructs?*
- What *statement forms* exist (e.g., loops, conditionals, jumps)?
- What *expression forms* are supported (e.g., arithmetic, lambdas, comprehensions)?
- How are *operator precedence* and *associativity* formally defined?
- What kinds of ‘Architectural Form’  (Module System) does it offers?
- Does the **language** provides supports for annotations?
- To what extent is the language expression-based versus statement-based?

| **Category** | **Form** | **Description** | **Syntax** | **Semantics** |
| --- | --- | --- | --- | --- |

## Language Semantics

> See more in  [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md).
> 

Guiding Questions:

- How are the syntactic constructs evaluated by the language’s execution model?
- How are *operator precedence* and *associativity* formally defined?
- **What formal or informal semantic model describes the language's execution?** (e.g., operational, axiomatic, denotational semantics)
- **How does the language define and enforce correctness?** (e.g., static type checking, contracts, runtime assertions)
- **What are the rules for function calls and argument passing?** (e.g., pass-by-value, pass-by-reference, copy-on-write, closures)
- **What memory model does the language enforce?** (e.g., stack allocation, heap management, reference counting)
- **How does the language handle undefined behavior or execution anomalies?** (e.g., segmentation faults, runtime errors, exception handling)
- **What guarantees does the language provide regarding execution determinism or non-determinism?**
- **What constraints exist on execution order, and how does this affect parallel computation?**
- Which are the **evaluation models** for the **linguistic expressions**? Which are the primitives operators? Take arithmetic,  boolean expressions,etc.  See  Rust: 📚 Standard Library.

| **Aspect** | **Type** | **Evaluation** |
| --- | --- | --- |

## Binding

> **Binding**: Associates **names** (variables, functions) with **memory locations, values, or behaviors**, either at compile-time or runtime.
> 

> **Mutability:  Mutability** refers to the ability of an object or variable to be modified after it is created or assigned a value.
> 

Guiding Questions:

- How are *values bound to names* (e.g., `let` in Rust, `=` in Python)?
- Which binding semantics does the language provides (mutable binding, inmutable binding)
- What categories of values and identifiable constructs does the language support?

### Identifiable Constructs

| **Identifier Type** | **Description** |
| --- | --- |
| **Variable Names** |  |
| **Function Names** |  |
| **Struct Names** |  |
| **Enum Names** |  |
| **Trait Names** |  |
| **Module Names** |  |
| **Type Parameter Names** |  |
| **Lifetime Names** |  |
| … |  |

### Binding Type

> **Binding Type** refers to the method by which a variable or identifier is associated with a value, address, or resource, determining its scope, lifetime, and mutability in a program.
> 

| **Binding Type** | **Description** |
| --- | --- |
| **Static Binding** | The association between a name and a value is fixed at compile time and does not change at runtime. |
| **Dynamic Binding** | The association between a name and a value is resolved at runtime. |
| **Lexical Binding** | A variable’s binding is determined by the scope in which it is defined. |
| **Global Binding** | Variables are bound globally and accessible across the entire program. |
| **Local Binding** | Variables are bound within a specific function or block of code. |

## Scoping Rules

> **Note:** Visibility and scoping rules are synonymous.
> 

> **Visibility**: **Visibility** refers to the scope or access control of an identifier (such as a variable, function, or class) within a program, determining where and how it can be referenced or modified, often enforced by rules such as access modifiers or name resolution mechanisms.
> 

> **Scoping Rules**: Determine **where and when** a binding is accessible (e.g., `block scope`, `function scope`, `global scope`).
> 

Guiding Questions:

- What is the *scope* of a name (lexical vs. dynamic, block vs. function)?
- How are shadowing, closures, and hoisting handled?
- Which are the  visibility rules associated with a binding?

## References

- [Evaluation Model](note.html?n=technica/computation/language-system/conceptual-model-language-system/evaluation-model.md)
- [Program Element](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-element.md)
- [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md)
- [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md)
- [Annotation](note.html?n=technica/computation/system/programming/conceptual-model-programming/annotation.md)
- [Statements and expressions](https://doc.rust-lang.org/reference/statements-and-expressions.html)
- [modules](https://doc.rust-lang.org/reference/items/modules.html)
- [`extern crate` declarations](https://doc.rust-lang.org/reference/items/extern-crates.html)
- [`use` declarations](https://doc.rust-lang.org/reference/items/use-declarations.html)
- [function definitions](https://doc.rust-lang.org/reference/items/functions.html)
- [type definitions](https://doc.rust-lang.org/reference/items/type-aliases.html)
- [struct definitions](https://doc.rust-lang.org/reference/items/structs.html)
- [enumeration definitions](https://doc.rust-lang.org/reference/items/enumerations.html)
- [union definitions](https://doc.rust-lang.org/reference/items/unions.html)
- [constant items](https://doc.rust-lang.org/reference/items/constant-items.html)
- [static items](https://doc.rust-lang.org/reference/items/static-items.html)
- [trait definitions](https://doc.rust-lang.org/reference/items/traits.html)
- [implementations](https://doc.rust-lang.org/reference/items/implementations.html)
- [`extern` blocks](https://doc.rust-lang.org/reference/items/external-blocks.html)
- [Tokens](https://doc.rust-lang.org/reference/tokens.html)
- [Keywords](https://doc.rust-lang.org/reference/keywords.html)
- [Identifiers](https://doc.rust-lang.org/reference/identifiers.html)
- [Comments](https://doc.rust-lang.org/reference/comments.html)
- [Whitespace](https://doc.rust-lang.org/reference/whitespace.html)
- [Tokens](https://doc.rust-lang.org/reference/tokens.html)