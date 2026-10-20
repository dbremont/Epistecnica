# OCaml: 📜 Language Specification

> A **language specification** formally defines the syntax, semantics,  and behavior of a programming language, including its lexical  structure, grammar, type system, execution model, and standard  libraries, serving as the authoritative reference for implementers and 
developers.
> 

## Grammar

> In this note, *grammar* refers collectively to both **lexical** and **syntactic grammar**: lexical grammar defines how source characters form tokens, while syntactic grammar defines how those tokens combine into valid language constructs.
> 

> A **literal** is a **notation for representing a fixed value directly in the source code**. It’s the actual value written in the code, not a variable or an expression that computes a value.
> 

> Table: Element Category (Lexical,  Syntactical).
> 

Guiding Questions:

- [Token Space] How are tokens (keywords, identifiers, literals) defined?
- What characters are allowed in identifiers (e.g., Unicode, sigils like `$`)?
- Does the language use significant whitespace (e.g., Python) or explicit delimiters (e.g., C)?
- *Does the Language Supports Macro Constructs?*
- Which are the modifiers (const, …) used  the Language?
- What are the core language constructs (variables, functions, control flow)?
- *Does the Language Support Macro Constructs?*
- What *statement forms* exist (e.g., loops, conditionals, jumps)?
- What *expression forms* are supported (e.g., arithmetic, lambdas, comprehensions)?
- How are *operator precedence* and *associativity* formally defined?
- What kinds of ‘Architectural Form’  (Module System) does it offers?
- Does the **language** provides supports for annotations?
- To what extent is the language expression-based versus statement-based?
- What is the **literal default type**?  - [X: **🏷️** Type System](https://app.notion.com/p/X-Type-System-fc2456113c894e699643d8ce60a4647f?pvs=21).

| Element Category | **Element Type** | Grammar Element Name | Form | **Description** |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Grammar Characterization

> aka. Linguistic Abstraction - Physical Manifestation of Computational Entity; *Computational Element.*
> 

> 📚 The **syntactic grammar defines how tokens are combined** into valid **expressions**, **statements**, **declarations**, and **programs**.
> 

Guiding Questions:

- What class of formal grammar best describes the grammar of this language? (Note: This may include grammars within or outside the Chomsky hierarchy.)
- Are there syntactic ambiguities in the Language?

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
- Which are the **evaluation models** for the **linguistic expressions**? Which are the primitives operators? Take arithmetic,  boolean expressions,etc.  See [X: 📚 Standard Library](https://app.notion.com/p/X-Standard-Library-fc444f130f9a4937ad9a96024b6f6bba?pvs=21).

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

### Scoping Rule Set

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

## Miscellanea

> **Specific Elements** of **The Language**.
> 

## References

- [Evaluation Model](note.html?n=technica/computation/language-system/conceptual-model-language-system/evaluation-model.md)
- [Program Element](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-element.md)
- [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md)
- [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md)
- [Annotation](note.html?n=technica/computation/system/programming/conceptual-model-programming/annotation.md)