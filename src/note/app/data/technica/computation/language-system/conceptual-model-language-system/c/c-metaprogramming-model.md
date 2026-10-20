# C++: Metaprogramming Model

> C++'s metaprogramming model allows developers to write programs that manipulate types and generate code at compile time using template metaprogramming, constexpr functions, and type traits, enabling highly efficient and flexible code generation.
> 

Questions:

- What is the language’s metaprogramming paradigm?
- What constructs are available at compile-time?
- What runtime reflection capabilities exist?
- How is reflection implemented?
- How are type errors reported in metaprograms?
- What are the costs of metaprogramming?
- How does the language prevent abusive metaprogramming?
- How are metaprograms debugged?

## Mechanism

| **Category (Model)** | **Element** | **Description** | **Case(s)** |
| --- | --- | --- | --- |
| **Compile-Time Programming** | Templates | Parameterized code producing specialized types/functions at compile time | `template<typename T> struct Vec { ... };` |
|  | Template Specialization | Custom implementation for specific types | `template<> struct Vec<int> { ... };` |
|  | Template Metafunctions | Functions evaluated at compile time | `std::conditional`, `std::is_same` |
|  | `constexpr` Functions | Functions evaluated at compile-time if arguments are constexpr | `constexpr int factorial(int n) { ... }` |
|  | `consteval` / `constinit` | Enforces compile-time evaluation / initialization | `consteval int f() { ... }` |
| **Type-Level Programming** | Type Traits | Type properties queried/manipulated at compile-time | `std::is_integral<T>::value` |
|  | Concepts | Compile-time constraints for templates | `template<typename T> requires Integral<T> ...` |
|  | SFINAE (Substitution Failure Is Not An Error) | Enable/disable templates based on substitution success | `template<typename T> auto f(T t) -> std::enable_if_t<std::is_integral_v<T>>;` |
|  | Variadic Templates | Templates accepting arbitrary number of parameters | `template<typename... Ts> struct Tuple { ... };` |
| **Expression-Level / Functional MP** | `decltype` | Compute type of an expression | `decltype(a + b) c;` |
|  | `auto` / `decltype(auto)` | Type deduction for variables / functions | `auto x = f();` |
|  | `if constexpr` | Conditional compilation at compile-time | `if constexpr(std::is_integral_v<T>) ...` |
| **Library/Algorithmic MP** | `std::integer_sequence` | Compile-time sequences for iteration / folding | Used in tuple unpacking |
|  | Fold Expressions | Compile-time reduction over parameter packs | `(args + ...)` |
|  | `std::conditional_t`, `std::enable_if_t`, `std::is_same_v` | Building type-level logic | Type selection and branching |

## References

- https://en.wikipedia.org/wiki/Template_metaprogramming
- [Metaprogramming](note.html?n=technica/computation/language-system/conceptual-model-language-system/metaprogramming.md)
- [**X: ✨**Metaprogramming](https://app.notion.com/p/X-Metaprogramming-82992f7f69a442f786c3ae4f27ce7fce?pvs=21)