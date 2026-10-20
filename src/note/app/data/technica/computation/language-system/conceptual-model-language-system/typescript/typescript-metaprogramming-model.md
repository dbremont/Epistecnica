# Typescript: Metaprogramming Model

> Rust’s macro system allows for code generation and manipulation at compile time, enabling powerful **metaprogramming** and code generation.
> 

> Rust's **metaprogramming** capabilities are primarily built around its powerful macro system. Unlike traditional macro systems in languages like C, Rust macros are more sophisticated and integrate deeply with its type system and syntax.
> 

## **Macros by Example (Declarative Macros)**

These are the most common form of macros in Rust, often called "macros." They allow you to write something similar to a match statement that operates on the syntactic structure of the code. These macros are declared using `macro_rules!` and are a way to define reusable code patterns. They can expand to produce more code than the shorthand used within the macro. This is particularly useful for reducing boilerplate or repetitive tasks.

Example of a simple macro:

```rust
macro_rules! say_hello {
    () => { // match no arguments
        println!("Hello!");
    };
}

fn main() {
    say_hello!(); // prints "Hello!"
}
```

### **Procedural Macros**

Procedural macros are more powerful and flexible than declarative macros. They allow code generation based on the input code, providing complete programmatic control over the output. Procedural macros come in three varieties:

- **Custom `#[derive]` Macros**: These automatically implement traits for structs and enums. You can create a `derive` macro to automatically generate implementations based on struct or enum definitions.
- **Attribute-like Macros**: These macros are similar to custom-derived macros but can annotate any item, not just structs and enums. They can manipulate or generate additional code for functions, structs, modules, etc.
- **Function-like Macros**: These macros look like function calls and can take a variable number of tokens as input and produce code as output. They are more flexible than `macro_rules!` macros.

Procedural macros operate at a lower level, working directly with the token stream rather than pattern matching on syntax. This makes them powerful but also more complex to implement. They are defined in a separate crate type designed explicitly for macros, often using libraries like `syn` to parse input tokens and `quote` to generate output tokens.

Example of a simple procedural macro using `derive`:

```rust
// This requires setting up a separate crate for procedural macros

use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, DeriveInput};

#[proc_macro_derive(HelloMacro)]
pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
    let ast = parse_macro_input!(input as DeriveInput);
    let name = &ast.ident;
    let gen = quote! {
        impl HelloMacro for #name {
            fn hello() {
                println!("Hello, I'm a {}", stringify!(#name));
            }
        }
    };
    gen.into()
}

// Usage in a different crate:
// #[derive(HelloMacro)]
// struct Pancakes;
// Pancakes::hello(); // prints: Hello, I'm a Pancakes
```

## References

- [Macros](https://doc.rust-lang.org/book/ch19-06-macros.html)
- [Macros Spec](https://doc.rust-lang.org/reference/macros.html)