---
tags: [note, essay]
---

# A Guide to Programming Languages


> A **programming language** is a medium for describing computations, and it provides the mechanisms by which those descriptions are executed.
> 

> A **model of computation** (also called a *computation model* or *computational formalism*) is a formal system that defines how computations (processes) are **represented** and **executed**.
> 

## Language Space

| **Language** | **Characterization** | **Implementation** | **Models of Computation** | **Tags** |
| --- | --- | --- | --- | --- |
| **C** | A small, minimal, procedural systems programming language designed for efficiency, low-level access, and predictable performance. | Ahead-of-time compiled (native) | **Imperative Programming** | imperative, systems, static-typed, compiled, low-level |
| **Go** | A statically typed, compiled language for concurrent networked services emphasizing simplicity and goroutine-based concurrency. | Ahead-of-time compiled (native), GC runtime | **Thread**, **Actor Model** (via goroutines/channels) | concurrent, compiled, garbage-collected, systems, network |
| **C#** | A modern, statically typed, object-oriented language with functional features, targeting managed runtimes and large-scale application development. | IL bytecode → JIT/AOT on .NET CLR | **Object-Oriented**, **Thread** | oo, managed, static-typed, jitted, enterprise |
| **Lua** | A lightweight, embeddable, dynamically typed scripting language focused on extensibility. | Bytecode VM + interpreter | **Imperative Programming** | scripting, dynamic, embeddable, interpreted, coroutine |
| **C++** | A general-purpose systems language extending C with abstractions for performance and multiple paradigms. | Ahead-of-time compiled (native) | **Object-Oriented**, **Imperative Programming** | systems, multi-paradigm, static-typed, compiled |
| **APL** | An array-oriented language using concise symbolic notation for high-level array transformations. | Interpreted or JIT on array VM | **Dataflow Models** | array, data-parallel, concise, interpreted |
| **AWK** | Text-processing language for pattern-directed scanning and reporting. | Interpreter | **Imperative Event-Driven Model** | scripting, text-processing, interpreted, declarative-rules |
| **BQL** | Declarative, set-oriented query DSL for analytics (varies). | Query interpreter/compiler (host-dependent) | **Logic Programming** (declarative querying) | query, declarative, data-analytics |
| **SQL** | Declarative language for relational data querying and manipulation. | Query planner + execution engine | **Logic Programming** (declarative querying) | declarative, data, query, transactional |
| **Coq** | Proof assistant and dependently typed functional language for formal proofs and specifications. | Bytecode VM + native-extraction compiler | **Lambda Calculus** (functional/formal) | theorem-proving, dependent-types, functional, formal |
| **Zsh** | Unix shell language with scripting features and command constructs. | Interpreter | **Imperative Programming** | shell, scripting, interactive, interpreted |
| **Vala** | Modern language compiling to C for the GObject ecosystem. | Compiles to C → native via GCC/Clang | **Object-Oriented**, **Imperative Programming** | oo, compiled-to-c, static-ish, gtk |
| **Lisp** | Homoiconic, list-based family emphasizing symbolic computation and macros. | Interpreter + optional compiler (varies by dialect) | **Lambda Calculus** | functional, homoiconic, macro, dynamic |
| **Java** | Statically typed, object-oriented language with portability via the JVM. | Bytecode VM (JIT / AOT) | **Object-Oriented**, **Thread** | oo, managed, static-typed, jvm, enterprise |
| **Perl** | Dynamic language optimized for text processing and pragmatic scripting. | Interpreter (bytecode under the hood) | **Imperative Programming** | scripting, text-processing, dynamic, pragmatic |
| **Rust** | Systems language offering memory safety without GC via ownership/borrowing. | Ahead-of-time compiled (LLVM) | **Imperative Programming**, **Thread** | systems, static-typed, ownership, compiled, safe-concurrency |
| **OCaml** | Functional-first with efficient runtime, static typing, and imperative features. | Bytecode VM + native compiler | **Lambda Calculus**, **Imperative Programming** | functional, static-typed, inference, multi-paradigm |
| **Scheme** | Minimalist Lisp emphasizing functional programming and continuations. | Interpreter + optional native compiler | **Lambda Calculus** | functional, minimal, homoiconic, dynamic |
| **Python** | High-level dynamic language with extensive standard libraries. | Bytecode interpreter (CPython), JIT variants | **Imperative**, **Object-Oriented** | dynamic, interpreted, scripting, multi-paradigm |
| **Erlang** | Functional language for distributed, fault-tolerant systems with lightweight processes. | BEAM VM (bytecode, concurrent scheduler) | **Actor Model** | concurrent, actor-model, functional, distributed |
| **Elixir** | Functional, concurrent language on the BEAM VM with metaprogramming. | BEAM VM | **Actor Model** | functional, actor-model, beam, dynamic |
| **Clojure** | Modern Lisp on the JVM with immutable data structures. | JVM bytecode (JIT) | **Lambda Calculus** | functional, lisp, jvm, immutable |
| **Haskell** | Purely functional, lazily evaluated language with advanced type system. | GHC native code, bytecode, or LLVM | **Lambda Calculus** (pure) | pure-functional, lazy, static-typed, academic |
| **R** | Statistical programming language with vectorization and interactive analysis. | Interpreter with vectorized primitives | **Dataflow Models** | data-science, vectorized, interpreted |
| **JavaScript** | Dynamic, event-driven language with first-class functions and event loop concurrency. | JIT-compiled, event-loop VM | **Imperative Event Driven Model** | dynamic, event-driven, web, jitted |
| **Standard ML** | Functional language with strong inference and module system. | Native or bytecode compiler | **Lambda Calculus**, **Imperative Programming** | functional, static-typed, inference, modular |
| **Ruby** | Dynamic OO language focused on expressiveness and metaprogramming. | Bytecode VM (YARV) | **Object-Oriented**, **Imperative Programming** | dynamic, oo, scripting, metaprogramming |
| **PHP** | Server-side scripting language for web applications. | Interpreter + JIT (PHP 8+) | **Imperative Programming** | web, scripting, dynamic, server-side |

## References

- [C Language](https://app.notion.com/p/C-Language-8655c4697ccf46dab526d2c63f25652c?pvs=21)
- [Go](https://app.notion.com/p/Go-a01cf8490d314b4081a4114d65880f7b?pvs=21)
- [C#](https://app.notion.com/p/C-72158b6dd114476383d95a8a6fd0c074?pvs=21)
- [Lua](https://app.notion.com/p/Lua-5ad30262f2ed4e81b6393c637fd3902e?pvs=21)
- [C++](https://app.notion.com/p/C-4ebda9647a1d49aebd7e6a2eea53253a?pvs=21)
- [APL](https://app.notion.com/p/APL-46e5250d436d42bcb4aa022a44e0ea87?pvs=21)
- [AWK](https://app.notion.com/p/AWK-0f9235de4dc8440d85d5e1df04772ee7?pvs=21)
- [**BQL**](https://app.notion.com/p/BQL-28a3fa6a8abe4faa8f2321deaa1b3351?pvs=21)
- [SQL](https://app.notion.com/p/SQL-d93e3824987846fabbb815915eeb2f41?pvs=21)
- [ARM](https://app.notion.com/p/ARM-1aec0f5171ec805da4e6c4ec49c91bde?pvs=21)
- [Coq](https://app.notion.com/p/Coq-1c0c0f5171ec80fd9697cbe58a2cde84?pvs=21)
- [ZSH](https://app.notion.com/p/ZSH-ff3d2c303af14d4a82c5e3964a1a1e5a?pvs=21)
- [Vala](https://app.notion.com/p/Vala-199c0f5171ec80238c6aedee4144cf15?pvs=21)
- [Lisp](https://app.notion.com/p/Lisp-3ec5fc2235964ff382393ad3114be8a8?pvs=21)
- [Java](https://app.notion.com/p/Java-26ddaf23fa274f99b0a3c04050bc50cb?pvs=21)
- [Perl](https://app.notion.com/p/Perl-ed62ba5c58b9406baf2936c689d7ca08?pvs=21)
- [Rust](https://app.notion.com/p/Rust-a19d921577244147970d4ce09498455e?pvs=21)
- [OCaml](https://app.notion.com/p/OCaml-f28faa49d8c4487c824d43a3094b0d7f?pvs=21)
- [Racket](https://app.notion.com/p/Racket-570cd34a8cfb483fb7a1b2d0c3ba84b9?pvs=21)
- [Python](https://app.notion.com/p/Python-83a6b3510b4a422b97c763b18ff9739a?pvs=21)
- [Erlang](https://app.notion.com/p/Erlang-7cf4c8a7ba99424c8275ef1665650357?pvs=21)
- [Elixir](https://app.notion.com/p/Elixir-1c1c0f5171ec80c2a6cffa328b3d204e?pvs=21)
- [Clojure](https://app.notion.com/p/Clojure-1c5c0f5171ec8088b676cbfef994f954?pvs=21)
- [Haskell](https://app.notion.com/p/Haskell-19ac0f5171ec8016a681d5c867e38b3f?pvs=21)
- [R Language](https://app.notion.com/p/R-Language-140c0f5171ec80af9804c8dcf34bf4f2?pvs=21)
- [Javascript](https://app.notion.com/p/Javascript-003a9408e9a0462e87e0b89b07fa1dc0?pvs=21)
- [Standard ML](https://app.notion.com/p/Standard-ML-195c0f5171ec801c81fee9531d62494f?pvs=21)
- [**WebAssembly**](https://app.notion.com/p/WebAssembly-aa00b60e0139413f9da8a04c6da0f9d7?pvs=21)
- [Ruby Language](https://app.notion.com/p/Ruby-Language-257f2cbe63894ac3bc3257f1c4f8de3b?pvs=21)
- 
- [PHP: Hypertext Preprocessor](https://app.notion.com/p/PHP-Hypertext-Preprocessor-cbbaef9b29ef497090f6e36ec6e5c77c?pvs=21)
