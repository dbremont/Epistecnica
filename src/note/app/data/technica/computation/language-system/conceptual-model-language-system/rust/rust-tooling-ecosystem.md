# Rust: 🛠️ Tooling & Ecosystem

> 

### Compiler System

> How is the language specification implemented by the compiler, and how does the compiler lower the language’s semantics into assembly or machine code?
> 

### Conditional Compilation

### Linkage

### Intrinsic Set

> In Rust, compiler intrinsics refer to functions provided directly by the compiler that are not part of the standard library but offer low-level operations closely tied to the underlying hardware or compiler capabilities. These functions are typically used for operations that cannot be efficiently or directly expressed in Rust itself. They are found in the `core::intrinsics` module, which is an unstable feature and can only be used with nightly Rust and a feature flag.
> 

## Tool Set

- **Rustc**: The official Rust compiler that is used to compile Rust programs.
- **MRustc**: A Rust compiler written in Rust itself that focuses on performance and compatibility with Rustc.
- **Cranelift**: A low-level, retargetable code generator used by Rust compilers and WebAssembly runtimes.
- **LLVM**: A widespread open-source compiler infrastructure that Rust can target for code generation.
- **Miri**: A specialized interpreter that can run and test Rust programs at compile-time.
- **RLS**: The Rust Language Server that provides IDE-like functionality such as code completion and error highlighting.
- **rust-analyzer**: Another Rust Language Server implementation known for its speed and features.
- **Evcxr** is an “evaluator-explainer” REPL (Read-Eval-Print-Loop) that can be used to write and run Rust code interactively.
- **Redox**: An experimental operating system written in Rust that includes its own Rust compiler and tools.

## References

- [Rust Compiler Development Guide](https://rustc-dev-guide.rust-lang.org/getting-started.html)
- [Rust Internals](https://internals.rust-lang.org/)
- [Linkage](https://doc.rust-lang.org/reference/linkage.html#linkage)
- [High-Level Compiler Architecture](https://rustc-dev-guide.rust-lang.org/part-2-intro.html)
-     - [Queries: [demand-driven compilation]](https://rustc-dev-guide.rust-lang.org/query.html)
        - [Incremental Compilation In Detail](https://rustc-dev-guide.rust-lang.org/queries/incremental-compilation-in-detail.html)
-