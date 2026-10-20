# TypeScript:  Name / Identifier Model (+Scoping)

> A [*path*](https://doc.rust-lang.org/reference/paths.html) is a sequence of one or more path segments used to refer to an [entity](https://doc.rust-lang.org/reference/glossary.html#entity) in the current scope or other levels of a [namespace](https://doc.rust-lang.org/reference/glossary.html#namespace) hierarchy.
> 

> Rust supports **currying**, which transforms a function with multiple arguments into a series of functions each taking one argument.
> 

> **Rust Closures**: Rust closures are anonymous functions that can capture their environment and are defined using a syntax that allows for parameters and body expressions, making them highly flexible for on-the-fly tasks like iterating operations, event handling, and customizing behavior within functions.
> 

> What is the **scoping model** of rust? Static Scope (Lexical Scope), Dynamic Scope? Rust is lexically scoped.
> 

How do we refer(bindings) to computational objects?

- Reference,
- Value

## **Rust Identifier Models**

> The Rust Identifier Models employ a combination of lexical scoping, strong type enforcement, and modular visibility rules to manage identifiers, ensuring safe and organized access to functions, variables, and other program entities across modular and concurrent environments.
> 

### Rust Identifier Models

| **Identifier Type** | **Description** | **Naming Conventions** | **Scoping Model** |
| --- | --- | --- | --- |
| **Variable Names** | Names assigned to variables, including constants and mutable variables. | Snake case (e.g., `user_count`, `active_items`). | Lexically scoped to the block, function, or module where declared. |
| **Function Names** | Names given to functions. | Snake case (e.g., `add_item`, `update_status`). | Visible within the declaration module; can be exported with `pub` for external visibility. |
| **Struct Names** | Names for structs are used to define custom data types. | CamelCase (e.g., `UserAccount`, `ShoppingCart`). | Module-local by default; globally visible if declared as `pub` and the module is public. |
| **Enum Names** | Names for enums define a type by enumerating its possible variants. | CamelCase (e.g., `AppState`, `ResponseCode`). | Module-local by default; globally visible if declared as `pub` and the module is public. |
| **Trait Names** | Names for traits define shared behaviors abstractly. | CamelCase (e.g., `Readable`, `Write`). | Module-local by default; globally visible if declared as `pub` and the module is public. |
| **Module Names** | Names for modules are used to organize namespace code. | Snake case (e.g., `utils`, `network_services`). | Structured within the crate's namespace, the `pub` modifier exposes the module at the global scope. |
| **Type Parameter Names** | Names for type parameters in generics applicable to functions, structs, enums, and traits. | Short, often single uppercase letter (e.g., `T`, `E`). | The scope is confined to the entity (function, struct, enum, trait) they are defined. |
| **Lifetime Names** | Names for lifetimes are annotations that relate the lifetimes of multiple references to each other. | Prefixed with an apostrophe, lowercase (e.g., `’a`, `’static`). | Lexical scope, usually within function signatures or type definitions where they are declared. |

### Rust Binding Models

> Rust's variable binding models are central to its design, emphasizing safety, concurrency, and memory management.
> 

> Here is a table that encapsulates the key aspects of variable bindings in Rust:
> 

| **Binding Type** | **Description** | **Key Characteristics** |
| --- | --- | --- |
| **Immutable Binding** | The default state for variables. Once a value is bound to a name, it cannot be changed. | Enhances safety by preventing accidental changes and side effects. Ideal for maintaining a consistent state. |
| **Mutable Binding** | Allows variables to be modified after their initial assignment. Declared with the `mut` keyword. | Necessary for values that need to change over time, such as counters or state within loops. |
| **Shadowing** | Reuses the name of a previous variable in the same scope by declaring a new variable with the same name. | Allows reusing names for new values, often used for type transformation or temporarily modifying values. |
| **Pattern Binding** | Uses patterns to deconstruct a compound data type (like tuples or structs) and bind its elements to names. | Useful in function parameters and match arms to directly access inner values of complex structures. |
| **Binding with Type Annotations** | Explicitly specifies the type of a variable when it is declared. | They are used when the compiler cannot infer the type or when explicit typing is required for clarity or API design. |
| **Binding in Loops** | Introduces new scopes and bindings within loop constructs like `for`, `while`, or `loop`. | Enables re-initialization of variables in each iteration or scope management inside loops. |

## References

- [Names](https://doc.rust-lang.org/reference/names.html)
- Static variable

       [https://en.wikipedia.org/wiki/Static_variable](https://en.wikipedia.org/wiki/Static_variable)

- …