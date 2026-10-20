# TypeScript: Linguistic Abstractions

> Rust's linguistic abstractions, encompassing control flow, pattern matching, primitive types, algebraic data types (ADTs), and ownership semantics, provide a comprehensive framework for describing computations with safety, efficiency, and expressive power.
> 

> An *item* is a component of a crate. Items are organized within a crate by a nested set of [modules](https://doc.rust-lang.org/reference/items/modules.html). Every crate has a single "outermost" anonymous module; all further items within the crate have [paths](https://doc.rust-lang.org/reference/paths.html) within the module tree of the crate.
> 

> Rust statements are expressions or declarations that perform actions, define bindings, control flow, or execute functions within the program, and they typically end with a semicolon.
> 

> A list of the **linguistic abstractions** is provided by `x`.
> 

## Lexical Structure

> Rust input is interpreted as a sequence of Unicode code points encoded in **UTF-8**.
> 

> In [computer science](https://en.wikipedia.org/wiki/Computer_science), a **lexical grammar** or **lexical structure** is a [formal grammar](https://en.wikipedia.org/wiki/Formal_grammar) defining the [syntax](https://en.wikipedia.org/wiki/Syntax_(programming_languages)) of [tokens](https://en.wikipedia.org/wiki/Token_(parser)).  The program is written using characters that are defined by the lexical
 structure of the language used. The character set is equivalent to the  alphabet used by any written language. The lexical grammar lays down the  rules governing how a character sequence is divided up into  subsequences of characters, each part of which represents an individual  token. This is frequently defined in terms of [regular expressions](https://en.wikipedia.org/wiki/Regular_expression).
> 

> The lexical structure of Rust defines its basic building blocks, including **identifiers**, **keywords**, **literals**, **operators**, **punctuation**, and **comments**, which are **organized into tokens** and governed by rules for syntax and whitespace handling.
> 

- [Tokens](https://doc.rust-lang.org/reference/tokens.html)
- [Keywords](https://doc.rust-lang.org/reference/keywords.html)
- [Identifiers](https://doc.rust-lang.org/reference/identifiers.html)
- [Comments](https://doc.rust-lang.org/reference/comments.html)
- [Whitespace](https://doc.rust-lang.org/reference/whitespace.html)
- [Tokens](https://doc.rust-lang.org/reference/tokens.html)

## Linguistic Abstractions

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

## Memory Management Model

## ¿Annotations?

[Rust Attributes (Annotations)](note.html?n=technica/computation/language-system/conceptual-model-language-system/typescript/typescript-linguistic-abstractions/rust-attributes-annotations.md)

## References

- [Statements and expressions](https://doc.rust-lang.org/reference/statements-and-expressions.html)
- …