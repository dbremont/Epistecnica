# Program Element Modifier

- [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md)

> 

## Modifier Type Set

| Modifier Type | Description | Language Instance Set |
| --- | --- | --- |
| Access Modifier | Controls visibility and accessibility scope | `public`, `private`, `protected` (Java, C#) |
| Mutability Modifier | Controls whether state may change after initialization | `const` (C++), `final` (Java), `readonly` (C#), `mut` (Rust) |
| Storage-Class Modifier | Controls storage duration and allocation semantics | `static`, `register`, `auto` (C) |
| Linkage Modifier | Controls symbol linkage across translation units/modules | `extern` (C/C++) |
| Lifetime Modifier | Specifies object/resource lifetime semantics | `'a` (Rust lifetimes), `static` (Rust/C) |
| Thread-Local Modifier | Creates per-thread storage instances | `thread_local` (C++), `ThreadStatic` (C#) |
| Volatility Modifier | Prevents certain compiler optimizations due to external mutation | `volatile` (C/C++, Java) |
| Atomicity Modifier | Enforces atomic memory operations | `_Atomic` (C11), `atomic` (C++), `AtomicInteger` semantics (Java) |
| Synchronization Modifier | Controls synchronization/locking semantics | `synchronized` (Java) |
| Inline Modifier | Requests inline expansion of callable entities | `inline` (C/C++) |
| Compile-Time Evaluation Modifier | Forces/permits compile-time computation | `constexpr` (C++), `consteval` (C++20) |
| Virtual Dispatch Modifier | Enables runtime polymorphic dispatch | `virtual` (C++) |
| Override Modifier | Declares intentional method override | `override` (C++, Java, C#) |
| Finalization Modifier | Prevents further inheritance/overriding | `final` (Java), `sealed` (C#), `final` (C++) |
| Abstract Modifier | Declares incomplete/abstract entities requiring specialization | `abstract` (Java, C#) |
| Static Member Modifier | Associates entity with type rather than object instance | `static` (Java, C#, C++) |
| Native/Foreign Modifier | Indicates externally implemented functionality | `native` (Java), `extern` (C#) |
| Unsafe Modifier | Allows operations outside language safety guarantees | `unsafe` (C#, Rust) |
| Nullable Modifier | Indicates nullable reference/value semantics | `?` (C#, Kotlin), `Optional`-style annotations |
| Immutable Type Modifier | Declares fully immutable structures/types | `immutable` (D language) |
| Dynamic Dispatch Modifier | Enables runtime method resolution | `dynamic` (C#), `dyn` (Rust trait objects) |
| Visibility Export Modifier | Controls symbol export/import behavior | `export` (C++20 modules), `pub` (Rust) |
| Ownership Modifier | Specifies ownership/borrowing semantics | `move` (Rust closures), `borrowed` semantics |
| Reference Modifier | Alters parameter/value passing semantics | `ref`, `out`, `in` (C#), `&` (C++) |
| Async Modifier | Marks asynchronous execution semantics | `async` (JavaScript, Python, Rust, C#) |
| Generator Modifier | Declares coroutine/generator semantics | `yield`-based generator markers (Python, C#) |
| Strictness Modifier | Controls evaluation strictness/laziness | `strictfp` (Java), lazy evaluation annotations (Haskell extensions) |
| Packing/Alignment Modifier | Controls memory layout/alignment | `alignas` (C++), `packed` (GCC attributes) |
| Restriction/Aliasing Modifier | Specifies pointer aliasing guarantees | `restrict` (C99) |
| Security Modifier | Applies security/access execution constraints | `transient` (Java serialization), `safe` (D language) |
| Persistence/Serialization Modifier | Controls persistence/serialization participation | `serializable` annotations, `transient` (Java) |
| Reflection/Metadata Modifier | Adds runtime metadata semantics | `@Entity` (Java), decorators (Python/TypeScript) |
| Calling Convention Modifier | Specifies ABI/calling convention behavior | `stdcall`, `cdecl` (C/C++) |
| Platform/Interop Modifier | Controls platform interoperability semantics | `dllimport`, `dllexport` (C/C++) |
| Pattern-Matching Modifier | Alters destructuring/matching semantics | `case class` (Scala), `data` (Kotlin) |
| Type Variance Modifier | Specifies subtype variance behavior | `out`, `in` (Kotlin), `covariant` (Scala/C#) |
| Capability Modifier | Restricts operational permissions/capabilities | `Send`, `Sync` traits (Rust concurrency semantics) |
| Macro Expansion Modifier | Influences compile-time macro behavior | `macro_rules!` visibility/export controls (Rust) |
| Optimization Hint Modifier | Supplies optimization directives to compiler | `likely`, `unlikely` (C/C++ compiler attributes) |

## Refererences

- …