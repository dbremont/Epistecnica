---
tags: [linguistic-abstraction]
---

# Language Specification

- [Meta Linguistic Abstraction](note.html?n=technica/computation/language-system/conceptual-model-language-system/meta-linguistic-abstraction.md), [Program Element](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-element.md), [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md), [Program Element Modifier](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-element-modifier.md)

> **A Language Specification**  is a  *formal or semiformal* document that defines a programming language’s **syntax**, **semantics**, **type system**, and **execution behavior**, serving as the authoritative reference for how programs in the language are written, interpreted, and evaluated.
> 

> Which syntactical forms does the language provide for constructing descriptions of computations?
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

## **Syntactic** Grammar

> aka. Linguistic Abstraction - Physical Manifestation of Computational Entity; *Computational Element.*
> 

> 📚 The **syntactic grammar defines how tokens are combined** into valid **expressions**, **statements**, **declarations**, and **programs**.
> 

Guiding Questions:

- What class of formal grammar best describes the grammar of this language? (Note: This may include grammars within or outside the Chomsky hierarchy.)
- Are there syntactic ambiguities in the Language?

## Linguistic Abstraction

> In ([Program Element](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-element.md)) we have expanded a taxonomy o syntactical constructs.
> 

> **First-class citizen (object and instrument of computation):** An entity in a programming language that can be **created at runtime, assigned to variables, passed as arguments, returned from functions, and stored in data structures** without restrictions.
> 

> Non-First class citizen (**instrument of computation**):   An entity in a programming language that **cannot be freely created, assigned, passed, returned, or stored in all contexts**. Its use is restricted by the language.
> 

| **Category** | **Form** | **Description** | **Sample Syntax** |
| --- | --- | --- | --- |
| **Lexical** | `Literal` | Fixed value atoms (numbers, strings, booleans). | `42`, `"hello"`, `true` |
|  | `Identifier` | Names used to identify variables, functions, or types. | `x`, `myVar`, `Point` |
|  | `Operator` | Symbols representing operations on values. | `+`, `==`, `>>=` |
|  | `Keyword` | Reserved words with special meaning in the language. | `if`, `class`, `return` |
|  | `Punctuation` | Delimiters and separators for structure. | `;`, `{`, `}`, `,` |
| **Expression** | `Atomic Expr` | The simplest expression units. | `x`, `42` |
|  | `Unary / Binary Expr` | Operations involving one or two operands. | `!a`, `x + 1` |
|  | `Function Call` | Applying a function to arguments. | `f(x)`, `print("hi")` |
|  | `Lambda / Anon Fn` | Anonymous functions defined inline. | `\x -> x+1`, `(x) => x*2` |
|  | `Conditional Expr` | Expressions that return a value based on logic. | `if a then b else c`, `a ? b : c` |
|  | `Match Expr` | Pattern matching expressions that return values. | `match x { A => 1, B => 2 }` |
|  | `Sequence` | A series of expressions evaluated in order. | `(do-this; do-that)` |
|  | `Comprehension` | Constructing collections from existing lists. |  |
| **Statement** | `Assignment` | Binding a value to a storage location. | `x = x + 1;` |
|  | `Return` | Exiting a scope and optionally returning a value. | `return v;` |
|  | `Block` | Grouping multiple statements into a scope. | `{ s1; s2; }` |
|  | `Expr-Statement` | An expression used for its side effect (ignoring return). | `calculate();` |
|  | `Throw / Exception` | Interrupting flow to signal an error. | `throw new Error("fail");` |
|  | `Control (If/While)` | Imperative flow control structures. | `while (x) { ... }` |
| **Declaration** | `Variable / Constant` | Introducing a name for a value or storage. | `let x = 5`, `const PI = 3.14` |
|  | `Function Definition` | Defining a reusable block of logic. | `def f(x) = x+1` |
|  | `Type Definition` | Defining a type alias or new type. | `type Point = {x:Int, y:Int}` |
|  | `Data Structure` | Defining composite data layouts (struct/record). | `struct User { id: Int }` |
|  | `Class` | Defining a blueprint for objects (OOP). | `class A { ... }` |
|  | `Module / Import` | Defining or importing namespaces. | `import math`, `module M` |
| **Pattern** | `Tuple Pattern` | Matching against a tuple structure. | `(x, y)` |
|  | `Constructor Pattern` | Matching against a data constructor/variant. | `Just(x)`, `Some(v)` |
|  | `Wildcard` | Matching anything (usually ignoring the value). | `_` |
|  | `Guarded Pattern` | A pattern match refined by a boolean predicate. | `x if x > 0` |
| **Invocation** | `Method Call` | Invoking a function on an object instance. | `obj.method(y)` |
|  | `Event Handler` | A callback invoked when an event triggers. | `onClick = handler` |
|  | `RPC / Service` | Invoking code across a network boundary. | `stub.GetUser(req)` |
| **Data & Type** | `Type Constructor` | A type that takes parameters to create a concrete type. | `List<T>`, `Map<K,V>` |
|  | `Enum / ADT` | Algebraic Data Types or enumerations. | `enum Color { Red, Green }` |
|  | `Type Annotation` | Explicitly stating the type of a binding. | `x: Int` |
| **Architecture** | `Component` | Large-grain encapsulation unit. | `component UserService {}` |
|  | `Package` | A distributable unit of code/modules. | `package main` |
| **Concurrency** | `Process / Thread` | Independent unit of execution. | `spawn(fn)` |
|  | `Async / Await` | Syntactic sugar for asynchronous promises. | `await fetchData()` |
|  | `Actor` | State isolated entity communicating via messages. | `actor ! message` |
| **Meta / Config** | `Macro` | Code that writes code at compile time. | `macro_rules!`, `#define` |
|  | `Annotation` | Metadata attached to code elements. | `@Override`, `#[derive(Debug)]` |
|  | `Config / Env` | Settings that alter build or runtime behavior. | `DEBUG=true` |
| **I/O & Error** | `IO Action` | Interactions with the outside world (File/Net). | `readFile("log.txt")` |
|  | `Try / Catch` | Handling potential failure blocks. | `try { ... } catch (e) { ... }` |
|  | `Result Handling` | Functional error handling using types. | `match res { Ok(v) => v, Err(e) => 0 }` |

## Representation

### Type

> 

> Specify a representation.
> 

> A type that abstract and specify a representation.
> 

> Note: Remember, there are also untyped data.
> 

> Modelling Data.
> 

Abstractions:

- Move Semantics
- Copy Semantics
- RAII (Resource Acquisition Is Initialization)
- Smart Pointers (std::unique_ptr, std::shared_ptr)
- Iterator Abstraction
- Classes/Objects
- Containers (std::vector, std::string)
- Type Erasure (std::any, std::function)
- Value vs. Reference Semantics
- Object Lifetimes & Ownership
- Borrowing: References to data can be borrowed immutably or mutably, allowing safe concurrent access to shared resources.
- Pattern Matching: Pattern matching allows for concise and expressive handling of different cases or patterns within data structures, aiding control flow and data manipulation.
- Immutable: …
- Visibility: …

### Computation Type

> Specify a computation.
> 

> **Modelling Computation.**
> 

> A type that abstract and specify a computation.
> 

> Note: Remember there are also untyped functions or just first-class functions.
> 

> **First-Class Functions**: These languages allow functions to be treated as **objects** or **values**, meaning you can pass them as arguments, return them from other functions, and assign them to variables.
> 

> **Higher-Order Functions**: These mechanisms support **higher-order functions**, which are functions that can accept other functions as arguments or return them.
> 

> **Lambda Expressions / Closures**: Many of these languages support **lambda expressions** (anonymous functions) or **closures**, allowing functions to capture variables from their surrounding scope.
> 

| **Mechanism** |  |  |  | **Description** |
| --- | --- | --- | --- | --- |
| **First-Class Functions** | JavaScript | Python | Ruby | Functions are **first-class citizens**, meaning they can be assigned to variables, passed as arguments, and returned from other functions. |
| **Higher-Order Functions** | JavaScript | Python | Scala | **Higher-order functions** are functions that take other functions as arguments or return them as values. |
| **Lambda Expressions** | JavaScript | Python | Ruby | **Lambda expressions** are concise, anonymous functions often used for inline functionality. |
| **Closures** | JavaScript | Python | Go | A **closure** is a function that captures variables from its surrounding environment, allowing access to those variables even after the outer function has finished execution. |
| **Delegates** | C# | Kotlin | Swift | **Delegates** are types that allow methods or functions to be assigned and invoked dynamically, similar to Java’s functional interfaces. |
| **Functional Interfaces** | Java | Kotlin | C# | **Functional interfaces** represent a single method (like a function), enabling functional programming techniques (such as lambda expressions). |
| **Function Types** | Scala | Haskell | Kotlin | **Function types** define the signature of a function (e.g., input and output types) and can be passed as values or returned from functions. |
| **Type Aliases for Functions** | TypeScript | Go | Scala | **Type aliases** allow you to define a name for a function type, making it easier to reuse and manage. |
| **Currying (Automatic or Manual)** | Haskell | JavaScript | Scala | **Currying** is the process of transforming a function that takes multiple arguments into a series of functions that each take one argument. |
| **Anonymous Functions** | JavaScript | Python | Ruby | **Anonymous functions** are functions without names, typically passed as arguments or used inline. |
| **First-Class Objects (Functions)** | JavaScript | Python | Swift | **Functions as first-class objects** means they can be assigned to variables, passed around, and invoked. |
| **Function Literals** | Kotlin | Swift | Scala | **Function literals** are anonymous functions created inline and passed as values to other functions or variables. |
| **Function Signatures** | Go | Rust | C# | **Function signatures** define the types and number of parameters a function accepts, as well as its return type. |
| **Partial Application** | Haskell | Scala | JavaScript | **Partial application** is a technique where some arguments of a function are pre-applied, creating a new function with the remaining arguments. |
| **Function Composition** | Haskell | JavaScript | Scala | **Function composition** allows creating a new function by combining two or more functions, where the output of one function becomes the input of another. |
| **Type Classes (Function-related)** | Haskell | Scala | Rust | **Type classes** enable functions to operate on different types without explicitly specifying the types, enhancing flexibility and reusability. |
| **Function Overloading** | C++ | Java | C# | **Function overloading** allows defining multiple functions with the same name but different parameter types, enabling more flexible and readable code. |
| **Closures with Variable Capture** | Python | JavaScript | Swift | **Closures with variable capture** allow functions to "remember" and use variables from their surrounding scope even after that scope has finished executing. |

## Naming & Environment

### Identifier

> What is a identifier? What are the types?
> 

> An **identifier** is a symbolic name used to refer to a program entity within a language system.
> 

> It acts as a linguistic handle that binds a name to some semantic object, resource, or construct inside a computational environment.
> 

| Identifier Type | Description | Language Instance Set |
| --- | --- | --- |
| Variable Identifier | Names a storage location or bound value | `counter` (C), `x` (Python), `total` (Java) |
| Constant Identifier | Names an immutable binding/value | `PI` (C++), `MAX_SIZE` (Java), `nil` (Lua) |
| Function Identifier | Names a callable computational unit | `printf` (C), `map` (Haskell), `println` (Java) |
| Method Identifier | Names a class/object-associated function | `toString` (Java), `push_back` (C++), `append` (Python) |
| Parameter Identifier | Names a formal input variable of a callable entity | `argc` (C), `self` (Python), `ctx` (Go) |
| Type Identifier | Names a type abstraction | `String` (Java), `Result` (Rust), `List` (Haskell) |
| Class Identifier | Names a class definition | `User` (Java), `Vector` (C++), `FileStream` (C#) |
| Interface Identifier | Names a behavioral contract/interface | `Runnable` (Java), `Serializable` (C#) |
| Enum Identifier | Names an enumeration type | `Color` (Rust), `DayOfWeek` (Java) |
| Field Identifier | Names a member inside a structure/object | `length` (JavaScript), `size` (C++), `capacity` (Rust) |
| Property Identifier | Names managed attribute accessors | `Name` (C#), `Value` (Swift) |
| Module Identifier | Names a module/unit of organization | `math` (Python), `Data.List` (Haskell) |
| Package Identifier | Names a package/namespace grouping | `java.util` (Java), `std` (Rust) |
| Namespace Identifier | Names a namespace scope | `std` (C++), `System` (C#) |
| Label Identifier | Names a jump/control-flow target | `loop_start` (Assembly), `retry` (C) |
| Macro Identifier | Names a macro expansion rule | `MAX` (C), `println!` (Rust) |
| Generic Type Parameter Identifier | Names a type variable in polymorphic abstractions | `T` (Java), `K`/`V` (C#), `'a` (OCaml) |
| Lifetime Identifier | Names a lifetime region | `'a` (Rust) |
| Trait Identifier | Names a trait/typeclass abstraction | `Display` (Rust), `Functor` (Haskell) |
| Concept Identifier | Names a compile-time semantic constraint | `Sortable` (C++20 Concepts) |
| Annotation Identifier | Names metadata annotations/decorators | `@Override` (Java), `@dataclass` (Python) |
| Keyword-like Builtin Identifier | Reserved/predefined symbolic binding | `self` (Python), `this` (Java), `super` (JavaScript) |
| Environment Identifier | Names an external/system binding | `PATH` (Unix Shell), `HOME` (POSIX) |
| Database Identifier | Names schema entities in databases | `employees` (SQL), `customer_id` (PostgreSQL) |
| Resource Identifier | Names external/system resources | `stdin` (C), `stdout` (POSIX), `stderr` (Unix) |
| Template Identifier | Names generic/template abstractions | `vector` (C++), `Option` (Rust) |
| Operator Identifier | Names overloadable operator functions | `operator+` (C++), `plus` (Haskell) |
| Event Identifier | Names an event/signal abstraction | `onClick` (JavaScript), `MouseDown` (C#) |
| State Identifier | Names symbolic machine/program states | `READY`, `BLOCKED`, `RUNNING` (Operating Systems/State Machines) |

### Modifier

> What is an **identifier modifier**?
> 

> An **identifier modifier** is a linguistic or semantic annotation that alters, constrains, qualifies, or extends the meaning, behavior, visibility, mutability, accessibility, storage, or lifecycle of an identifier-associated entity.
> 

> **Note:** The Modifiers can be provided by the language - or created on top of the language -using metadata - based mechanisms.
> 

> See the list here [Program Element Modifier](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-element-modifier.md).
> 

### Binding

> **Binding**: Associates **names** (variables, functions) with **memory locations, values, or behaviors**, either at compile-time or runtime.
> 

> **Mutability:  Mutability** refers to the ability of an object or variable to be modified after it is created or assigned a value.
> 

Guiding Questions:

- How are *values bound to names* (e.g., `let` in Rust, `=` in Python)?
- Which binding semantics does the language provides (mutable binding, inmutable binding)
- What categories of values and identifiable constructs does the language support?

Identifiable Construct

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

Binding Type

> **Binding Type** refers to the method by which a variable or identifier is associated with a value, address, or resource, determining its scope, lifetime, and mutability in a program.
> 

| **Binding Type** | **Description** |
| --- | --- |
| **Static Binding** | The association between a name and a value is fixed at compile time and does not change at runtime. |
| **Dynamic Binding** | The association between a name and a value is resolved at runtime. |
| **Lexical Binding** | A variable’s binding is determined by the scope in which it is defined. |
| **Global Binding** | Variables are bound globally and accessible across the entire program. |
| **Local Binding** | Variables are bound within a specific function or block of code. |

### Scoping Rule

> How are **identifiers** resolved to bindings within an **execution environment**?
> 

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

| **Scoping Model** | **Description** | **Binding Resolution Strategy** | **Characteristics** | **Case(s)** |
| --- | --- | --- | --- | --- |
| **Lexical Scoping** | Variable bindings are resolved according to the static textual structure of the program | Identifier lookup follows nested source-code scopes determined at compile/parse time | Predictable; closure-friendly; enables static analysis | CPython, JavaScript, Rust, Haskell |
| **Dynamic Scoping** | Bindings are resolved using the runtime call stack rather than source structure | Identifier lookup walks active caller environments at runtime | Context-sensitive; harder to reason about statically | Early Lisp systems, shell environments |
| **Static Scoping** | Another term for lexical scoping emphasizing compile-time scope structure | Resolution based on program text | Stable bindings independent of caller chain | Most modern languages |
| **Global Scoping** | Bindings exist in a program-wide namespace | Lookup checks shared global environment | Easy access; risk of namespace pollution | Global variables/modules |
| **Local Scoping** | Bindings restricted to a local block/function region | Lookup starts in nearest local frame | Encapsulation; reduced interference | Function/block-local variables |
| **Block Scoping** | Scope attached to syntactic blocks `{}` or equivalent | Bindings visible only within enclosing block | Enables fine-grained lifetime control | C, Java |
| **Function Scoping** | Variables scoped to entire function body regardless of inner blocks | Function activation record defines visibility | Simpler but coarser than block scope | Older JavaScript (`var`) |
| **Module Scoping** | Bindings visible within a module/package boundary | Lookup constrained to module namespace | Supports encapsulation and separate compilation | Modules/packages/namespaces |
| **Namespace Scoping** | Named scope hierarchy partitions identifiers | Qualified lookup through namespace tree | Prevents naming collisions | C Plus Plus namespaces |
| **Closure Scoping** | Inner functions capture bindings from enclosing lexical environments | Environment persists after outer function exits | Fundamental to higher-order functions | Functional languages, closures |
| **Class/Object Scoping** | Bindings associated with object/class contexts | Lookup includes object/class hierarchy | Supports encapsulation and inheritance | Object-oriented systems |
| **Prototype Scoping** | Property lookup traverses prototype chains | Delegation-based resolution | Dynamic object extension | JavaScript |
| **Package Scoping** | Visibility restricted to package-level units | Package acts as encapsulation boundary | Intermediate visibility granularity | Go, Java |
| **Thread-Local Scoping** | Bindings isolated per execution thread | Each thread has separate environment instance | Concurrency isolation | TLS/thread-local storage |
| **Contextual / Ambient Scoping** | Bindings implicitly supplied by execution context | Runtime context propagation | Often used in dependency injection/config systems | Context variables, implicit parameters |
| **Capability-Based Scoping** | Access determined by possession of explicit references/capabilities | No ambient/global lookup | Security-oriented design | Capability-secure systems |
| **Temporal Scoping** | Binding validity constrained by time/lifetime | Bindings expire after execution phase | Resource/lifetime management | Region systems, RAII |
| **Phase Scoping** | Separate scopes exist across compilation/evaluation phases | Compile-time and runtime namespaces separated | Macro hygiene, staged computation | Lisp macro systems |
| **Hygienic Macro Scoping** | Macro expansions preserve lexical binding correctness | Expansion avoids accidental capture | Prevents identifier collisions | Scheme macro systems |

## Language Semantics

> Note in this section we specify the How a syntactical construct get’s evaluated?
> 

> See more in [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md) - [Evaluation Model](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md).
> 

## Expression Evaluation

> Which are the aspects that capture expression evaluation?
> 

| Aspect | Description | Case |
| --- | --- | --- |
| **Evaluation Model** | Global strategy governing when expressions and arguments are evaluated | Applicative order, normal order |
| **Operand Evaluation Order** | Sequencing rule for evaluating operands/subexpressions | Left-to-right, right-to-left, unspecified |
| **Operator Precedence** | Binding strength determining parse structure of operators | `a + b * c` → `a + (b * c)` |
| **Associativity** | Rule determining grouping of operators of equal precedence | `a - b - c` → `(a - b) - c` |
| **Short-Circuit Semantics** | Conditional suppression of operand evaluation | `a && b` skips `b` if `a == false` |
| **Strictness** | Whether operands must be evaluated before operator application | Strict vs non-strict functions |
| **Reduction Strategy** | Formal reduction ordering in rewriting/evaluation systems | Innermost-first β-reduction |
| **Evaluation Context** | Structural location in which reduction is permitted | Context grammars in operational semantics |
| **Side-Effect Semantics** | Interaction between evaluation and mutable state or I/O | `i++ + f()` |
| **Sequence Points / Sequencing Rules** | Constraints on visibility/order of side effects | C/C++ sequencing semantics |
| **Type Conversion Semantics** | Rules governing coercion during evaluation | Integer promotion in C |
| **Dispatch Semantics** | Resolution mechanism for operators/functions | Dynamic dispatch, overload resolution |
| **Binding Semantics** | Resolution of identifiers during evaluation | Lexical vs dynamic scope |
| **Environment Model** | Runtime structure storing bindings and values | Stack frames, closures |
| **Value Category Semantics** | Classification of expressions by storage/value behavior | lvalue/rvalue/xvalue |
| **Exception Propagation Semantics** | Behavior when evaluation raises exceptions/errors | Stack unwinding |
| **Lazy Materialization** | Deferred construction/computation of values | Streams, generators |
| **Memoization / Sharing** | Reuse of previously computed expression values | Call-by-need |
| **Concurrency Semantics** | Interaction between evaluation and parallel execution | Futures, async expressions |
| **Memory Visibility Semantics** | Ordering/visibility guarantees across threads | Happens-before relations |
| **Determinism** | Whether identical evaluations always produce same result | Pure functional expressions |
| **Purity** | Whether evaluation mutates observable state | Referential transparency |
| **Termination Behavior** | Whether evaluation is guaranteed to complete | Divergence vs normalization |
| **Cost Semantics** | Resource consumption model of evaluation | Time/space complexity |
| **Symbolic vs Concrete Evaluation** | Whether expressions are reduced symbolically or executed concretely | Symbolic execution engines |
| **Compile-Time vs Runtime Evaluation** | Phase in which evaluation occurs | Constant folding, constexpr |
| **Meta-Evaluation Semantics** | Evaluation of code representing code | `eval`, macro systems |
| **Execution Substrate** | Runtime mechanism executing the expression | AST walker, bytecode VM, JIT |
| **Optimization Semantics** | Permitted transformations preserving meaning | Common subexpression elimination |
| **Numeric Semantics** | Rules for arithmetic precision and overflow | IEEE-754 floating-point |
| **Undefined / Unspecified Behavior** | Semantic gaps intentionally left unconstrained | Unsequenced modifications in C |

### Model Set

- Applicative Order:  Evaluation model where function arguments are evaluated **before** the function is applied
- Normal Order (Lazy Evaluation) : Evaluation model where function arguments are substituted into the function body **without immediate evaluation**

### Evaluation Order

> 
> 

| Evaluation Order | Description | Operational Behavior | Example Systems |
| --- | --- | --- | --- |
| **Left-to-Right Evaluation** | Operands/subexpressions are evaluated sequentially from left to right | The left operand is fully evaluated before the right operand begins | Java Virtual Machine, CPython, C Sharp |
| **Right-to-Left Evaluation** | Operands are evaluated from right to left | Right operand evaluation precedes left operand evaluation | Some historical compilers and ABI-dependent calling conventions |
| **Unspecified Evaluation Order** | Language specification does not define operand evaluation sequence | Compiler/runtime may choose any order | GNU Compiler Collection for many C and pre-C++17 constructs |
| **Short-Circuit Evaluation** | Evaluation stops once the final boolean result is determined | Remaining operands may never execute | Boolean operators like `&&`, ` |
| **Lazy Evaluation** | Expressions are evaluated only when their values are required | Deferred computation; may never execute | Haskell |
| **Eager Evaluation** | Expressions are evaluated immediately upon encounter | Immediate computation of operands | Most imperative languages |
| **Outermost-First Evaluation** | Evaluate higher-level expressions before nested expressions | Characteristic of normal-order reduction | Lambda calculus normal-order systems |
| **Innermost-First Evaluation** | Evaluate deepest nested expressions first | Characteristic of applicative-order reduction | Strict functional and imperative systems |
| **Parallel Evaluation** | Multiple independent expressions evaluated concurrently | Exploits independence/dataflow | Parallel runtimes, SIMD/dataflow systems |
| **Demand-Driven Evaluation** | Evaluation triggered by observable need/consumption | Pull-based execution semantics | Stream processing, lazy functional runtimes |

## References

- [Algorithm](note.html?n=technica/computation/algorithm.md)
- [Programming](note.html?n=technica/computation/system/programming.md)
- [Type System](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-system.md)
- [Formal Language](https://app.notion.com/p/Formal-Language-195c0f5171ec8012bf0fd0530a135871?pvs=21)
- https://en.wikipedia.org/wiki/Metalinguistic_abstraction
- https://en.wikipedia.org/wiki/Abstraction_(computer_science)
- [‣](https://app.notion.com/p/10e598edb7908162af92c422bb1be3e2?pvs=21)
- https://en.wikipedia.org/wiki/Scope_(computer_programming)