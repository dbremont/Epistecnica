---
tags: [type-system]
---

# Type System

- [Type Variance](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-variance.md), [Type Compatibility](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-compatibility.md), [Type Checking](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-checking.md), [Annotation](note.html?n=technica/computation/language-system/conceptual-model-language-system/annotation.md), [Effect System](note.html?n=technica/computation/language-system/conceptual-model-language-system/effect-system.md), [Data Type](note.html?n=technica/computation/language-system/conceptual-model-language-system/data-type.md), [Memory  Management](note.html?n=technica/computation/language-system/conceptual-model-language-system/memory-management.md)

> In this note we will explore the **ideas of type** and **type system**.
> 

> A **type system** is best understood as a **formal technical framework for classifying and constraining values, expressions, and program constructs**. It therefore constitutes a **formal component of a programming-language system**, defining the rules under which programs are considered type-correct.
> 

> Note: The type system - is a cross cutting framework - in language system - that is - it’s not in one place.
> 

```jsx
Technical Framework
└── Type System
    ├── Types
    ├── Typing Rules
    ├── Type Relations
    └── Typing Judgments
         │
         ▼
Technical Mechanism

          │                             │
    Static mechanisms              Runtime mechanisms
          │                             │
    ├─ Type checking               ├─ Runtime type checking
    ├─ Type inference              ├─ Dynamic dispatch
    ├─ Constraint solving          └─ Runtime type conversion
    ├─ Unification
    ├─ Subtype checking
    ├─ Type resolution
    └─ Overload resolution
```

QA: 

- Example of type unsounesd in java.
- Which should be the **organizing concepts** of the note?
    - Name
    - Type
    - Value
    - **Operation** (Assignment, Type Inference),
    - Rule
    - Type of Type - Type Creation Mechanism
    - Rule Enforcement Mechanism
    - Type System
        - Declaration
        - Affirmation Set
        - Implementation
        - Primitive Type Set
        - …
    - Theory,  …
- …

## Formulation

> What is a type? What kind of entity is a type?
> 

> A **type** is a set of values, those values usually shared a set of properties.
> 

> A type is a **label** used by a type system to prove some property of the program's behavior.
> 

> A **type** is a formal mathematical abstraction that classifies values and expressions within a type system, defining a set of permissible operations and structural constraints, typically represented as elements of a type domain within a formal semantics framework (e.g., denotational, operational, or categorical semantics), and often encoded using algebraic structures, dependent types, or subtyping relations.
> 

> What is a **type system**?  A **type system** is a formal mathematical framework that assigns types to expressions in a programming language, enforcing constraints through rules of type inference and checking to ensure correctness, safety, and abstraction, often based on a formalism such as $λ$-calculus, **Hindley-Milner**, or **dependent type theory**.
> 

> A **type system** is a set of rules and constraints that govern how data types (such as integers, strings, and objects) can be used and manipulated in a programming language, ensuring data integrity and preventing type-related errors.
> 

### Terminology

| **Concept** | **Definition** |
| --- | --- |
| **Type Declaration** | A type declaration defines the set of types a variable, function, or expression can take, specifying the structure and behavior of values at compile-time through explicit annotations or syntax, ensuring static type safety. |
| **Type Checking** | Type checking is the process of verifying that the types of variables, expressions, and functions comply with the rules and constraints of a type system, typically performed at compile-time to ensure type correctness and prevent runtime errors. |
| **Type Rule** | A type rule is a formal specification within a type system that governs how types can be assigned to expressions or variables, ensuring that operations on these entities preserve the consistency of the type structure in the program. |
| **Type Inference** | Type inference is the mechanism by which a type system automatically deduces the types of expressions and variables based on their context and usage, without requiring explicit type annotations from the programmer. |
| **Type Guarantee** | Type guarantee refers to the assurances provided by a type system that well-typed programs will not result in type-related errors at runtime, typically expressed in terms of **type soundness**, **type safety**, and **type correctness**. |
| **Ill typed** | A program fragment that does not comply with the rules of a given type system. |
| **Well-typed program** | A program (fragment) that complies with the rules of a given type system. |

### **Structural Type System**

> A **classical type system** is a type system where types are defined and checked based on **structural rules** like **contraction, weakening,** and **exchange**, which allow for the manipulation of terms, such as duplication, discarding, and reordering, typically found in **linear** or **non-linear** type systems.
> 

### **Substructural Type System**

> A **Substructural Type System** is a type system that enforces restrictions on the use of resources, such as **linear types**, **affine types**, or **ownership types**, by modifying or omitting certain structural rules (like **copying** or **discarding**), ensuring precise control over resource management and state changes.
> 

> It is called **substructural** because it **subverts** or **reduces** the **structural rules** typically present in classical type systems, which allow unrestricted manipulation of terms (like copying or discarding), in order to provide finer control over resource management and state.
> 

## Type System

> 

### Characterization

> How to characterize a type system? Is the affirmation set sufficient, or do we need a more abstract view?
> 

> Note: Every type construct must be type-checked; it provides certain guarantees, and type inference for expressions created with the construct must be provided.
> 
- **The Type Creation Mechanism Set** is the collection of formal constructors and formation rules that generate valid types from primitives, type variables, and existing types via operations such as product, sum, function formation, recursion, and abstraction, thereby defining the generative closure of the type universe.
- A **Type Relation** is a formally defined binary or n-ary relation over types—such as equality, subtyping, equivalence, or compatibility—that specifies the structural or semantic conditions under which one type can be considered substitutable, comparable, or transformation-equivalent to another within a type system.
- A **Typing Judgment** is a syntactic-semantically grounded assertion of the form `Γ ⊢ e : T` that expresses that under a typing context Γ mapping identifiers to types, an expression e is derivable as having type T according to the inference rules of the type system, forming the core deductive mechanism of type assignment.
- A **Property Set** is the collection of meta-theoretic predicates over a type system—such as soundness, progress, preservation, normalization, and decidability—that characterize its correctness, computational behavior, and semantic guarantees with respect to an underlying operational or denotational semantics.
- **Expressivity:** Which representations does it facilitate expressing? Which does it not?

Practical Characterization (Axis of Variation) (Structure of the Typesystem Space):

- **Inference model** (HM vs System F)
- **Type dependency strength** (STLC → dependent types)
- **Identity model** (nominal vs structural)
- **Resource model** (linear/affine vs unrestricted)
- **Expressiveness level** (simple → higher-kinded → dependent)
- **Runtime interaction** (static vs gradual vs dynamic)
- Time of checking
- Type inference
- Polymorphism
- Type identity
- Strength
- Expressiveness
- Decidability
- Principal types
- Type computation
- Subtyping

| **Feature** | **Dimension** | **Value** | **Description** |
| --- | --- | --- | --- |
| **Time of Checking (Enforcement)** | Static   (Strict Typing) | … | Type checking occurs at compile-time, ensuring type correctness before execution. |
|  | Dynamic (Strict Typing) | … | Type checking occurs at runtime, allowing flexibility but risking runtime errors. |
|  | Gradual Typing | … | Combines static and dynamic typing, allowing gradual adoption of type annotations. |
| Type Inference (Type Deduction) | Scope | Local Inference | Types are inferred within a limited scope (e.g., variable initialization). |
|  |  | Global Inference | Types are inferred across the entire program (e.g., Hindley-Milner in Haskell). |
|  | Type Annotation | Inferred (Implicit) | Types are deduced by the compiler without explicit annotations. |
|  |  | Manifest (Explicit) | Types must be explicitly declared by the programmer. |
|  |  | Partial Inference | Some types are inferred, while others require annotations. |
| Type Conversion  | Strength of Checking | Strong | No implicit conversions; strict type rules (e.g., Haskell). |
|  |  | Weak | Allows implicit conversions (e.g., JavaScript). |
|  | Conversion Direction |  |  |
|  |  | Narrowing Conversion | Converts a broader type to a narrower one (e.g., double to int). |
|  |  | Widening Conversion | Converts a narrower type to a broader one (e.g., int to double). |
|  | Conversion Automaticity | Implicit (Automatic)  (Type Coercion) | Conversions happen automatically (e.g., JavaScript "5" + 2 → "52"). |
|  |  | Explicit  (Manual)  (Type Casting)   | Conversions require explicit syntax (e.g., (int) 3.14 in C). |
| Type Relation | Type Compatibility  | Nominal | Types are compatible if they have the same name (e.g., Java classes). |
|  |  | Structural → (**Duck Typing, …**) | Types are compatible if they have the same structure (e.g., TypeScript interfaces). |
|  |  | Nominal Structural Typing | Hybrid approach (e.g., Scala). |
|  | **T**ype Equivalence | … | Rules for determining if two types are equivalent (e.g., aliases). |
|  | Polymorphism (Flexibility) | … |  |
|  |  |  Row Polymorphism | … |
|  |  | Parametric Polymorphism |  |
|  |  | Ad-hoc Polymorphism |  |
|  | Subtyping Polymorphism | … |  |
| Context Sensitivity | Flow-Sensitive Typing | … | Type checking considers control flow (e.g., TypeScript narrowing). |
|  | Latent Typing | … | Types are associated with values, not variables (e.g., Racket). |
| **Type Declaration** | Type Constructor (Kinds of Types) | Algebraic Type | Composite types built via sums (e.g., Either) or products (e.g., tuples). |
|  |  | Quotient Type | Types modulo an equivalence relation (e.g., int as Nat / {0}). |
|  |  | Generic Type (Parameterized Type) | Types abstracted over other types (e.g., List<T>). |
|  |  | Dependent Type | Types depend on values (e.g., Vector n where n is a runtime value). |
|  |  | Type Composition | Union Type |
|  |  |  | Intersection Type |
|  |  |  | Product Type |
|  |  |  | Record (Structure) |
|  |  |  | Tuple |
|  |  | Recursive Type | Types that refer to themselves (e.g., Tree with Node(Tree)). |
|  |  | Function Type | Types representing functions (e.g., int → string). |
|  |  | Lambda Type | Anonymous function types (e.g., λx.x in typed lambda calculus). |
|  |  | Class | OOP class types (e.g., class Person). |
|  |  | Interface | Abstract types defining behavior (e.g., interface Serializable). |
|  |  | Enumeration | Finite set of named values (e.g., enum Color {Red, Green}). |
|  |  | Primitive Type | Built-in types (e.g., int, boolean). |
|  |  | Abstract Type | Opaque types with hidden implementation (e.g., abstract type Id). |
|  |  | Interop Type | Types for foreign language interoperability (e.g., extern in Rust). |
|  | Type Constraint | … | Restrictions on type parameters (e.g., T: Comparable). |
|  | Type Erasure | … | Generic type info removed at runtime (e.g., Java). |
|  | Type Reification | … | Generic type info retained at runtime (e.g., C#). |
|  | Refinement Type | … | Types constrained by predicates (e.g., {x: int | x > 0}). |
|  | Type Property | Linear Type | Values must be used exactly once (e.g., Rust’s ownership). |
|  |  | Affine Type | Values can be used at most once (e.g., Rust’s move semantics). |
|  |  | Ownership Type | Tracks resource ownership (e.g., Rust’s borrow checker). |
|  |  | Uniqueness Type | Ensures no aliasing (e.g., Clean language). |
|  |  | Session Type | Types for communication protocols (e.g., channels in Go). |
|  |  | Mutability | … |
|  | Type Variance | … | Covariance, contravariance, invariance (e.g., List<+T>). |
|  | Type Reflection | … | Runtime inspection of types (e.g., typeof in JavaScript). |
|  | Peudo-Type (Void Type) | … | … |
|  | Null Type |  |  |
| Error Handling | … | … | How types handle errors (e.g., Result<T, E> in Rust). |
| Effect System | … | … | Tracks side effects (e.g., IO, state) in types (e.g., Haskell’s monads). |
| Pattern Matching | … | … | … |
| Type Guarantee | Type Safety | … | Prevents undefined behavior (e.g., no memory corruption). |
|  | Null Safety |  | Ensures null values are handled explicitly (e.g., Kotlin’s ?). |
|  | Soundness |  | **No false negatives** in type checking (e.g., Haskell). |
|  | Completeness |  | **No false positives** (rare; most systems are unsound for practicality). |
|  | **Correctness** |  | Overall assurance that types enforce program correctness. |
| Type Metadata | … | … | .. |
|  |  |  |  |

### Affirmation Set

> Which properties or predicates can be expressed in terms of a type system?
> 

| Subject | Affirmation Type | Description | Note |
| --- | --- | --- | --- |
| Type System | Soundness | Well-typed programs respect semantics | If `Γ ⊢ e : T`, then `e` cannot produce type errors at runtime |
| Type System | Type Safety | No type errors occur in execution | Typically derived from Progress + Preservation |
| Evaluation Relation | Progress | Well-typed terms are either values or can step | Ensures no “stuck states” |
| Evaluation Relation | Preservation (Subject Reduction) | Evaluation preserves types | If `e : T` and `e → e'`, then `e' : T` |
| Type System | Decidability | Type checking terminates | There exists an algorithm that decides `Γ ⊢ e : T` |
| Type System | Completeness (Inference) | All typable programs can be inferred | Hindley–Milner-style inference |
| Type System | Principal Typing | Most general type exists | Every type is an instance of a principal type |
| Type System | Consistency | No contradictions are derivable | Especially in dependent type systems |
| Type System | Normalization | Type-level computation terminates | Strong normalization prevents infinite reduction |
| Type System | Conservativity | Extensions preserve existing judgments | New features do not break old derivations |
| Type System | Parametricity | Polymorphic functions are uniform | No type-dependent branching in `∀T` functions |
| Type System | Representation Independence | Abstract types cannot be distinguished externally | Ensures module encapsulation |
| Type System | Effect Soundness | Effects are correctly tracked | `IO`, `State`, `Exception` encoded in types |
| Type System | Memory Safety | No invalid memory access | No dangling pointers, no use-after-free |
| Type System | Race Freedom | No concurrent data races | Enforced by ownership or linear logic |
| Type System | Security (Non-interference) | No illegal information flow | High-security data cannot influence low-security outputs |
| Type System | Termination (Totality) | All programs terminate | Only total functions allowed |
| Type System | Determinism | Same input produces same output | Pure functional semantics |
| Type System | Substitution Soundness | Replacing equals preserves typing | Foundational property of lambda calculus |
| Typing Judgment | Well-Formedness | Judgments are syntactically valid | `Γ ⊢ e : T` is well-formed only if `Γ` is valid |
| Typing Judgment | Determinacy | A judgment has at most one derivation | No ambiguity in typing result |
| Type Relation | Subtyping Soundness | Subtypes can replace supertypes safely | Liskov Substitution Principle |
| Type Relation | Transitivity | Type relations compose consistently | If `A <: B` and `B <: C`, then `A <: C` |
| Type Relation | Reflexivity | Every type relates to itself | `A <: A`, `A ≡ A` |
| Type Relation | Antisymmetry (Equivalence Collapse) | Mutual subtyping implies equality | If `A <: B` and `B <: A`, then `A ≡ B` |
| Type Inference System | Algorithmic Soundness | Inference matches formal typing rules | Inferred types correspond to derivations |
| Type Inference System | Algorithmic Completeness | All derivable types can be inferred | No missing typable programs |
| Type Constructor | Well-Formedness | Type constructors produce valid types | Kinding rules ensure correctness |
| Type Constructor | Arity Correctness | Correct number of type arguments | `List<T>` invalid if missing `T` |
| Type Universe | Stratification | Prevents paradoxes in type hierarchies | Universe hierarchy avoids inconsistency |
| Value / Expression Type | Structural Property | Expresses shape/structure of data | `{x: Int, y: Int}`, `(A, B)` |
| Value | Membership Predicate | Value belongs to a type domain | `42 : Int`, `"a" : String` |
| Expression | Well-Typedness | Expression is valid under typing rules | `Γ ⊢ e : T` |
| Type | Equality Predicate | Type equivalence relation | `A ≡ B`, alias resolution |
| Type | Subtyping Predicate | Inclusion relation between types | `A <: B`, inheritance |
| Type Variable | Constraint Satisfaction | Bounds on polymorphic types | `T extends Comparable`, `where T: Clone` |
| Type (Parametric System) | Parametric Universality | Uniform behavior across all types | `∀T. List<T>` |
| Value (Resource Domain) | Resource Usage | Rules for copying/moving/discarding values | linear / affine types |
| Reference / Value | Aliasing Control | Restrictions on multiple references | Rust ownership / borrow rules |
| Value | Mutability Constraint | Whether state can be modified | `const`, immutable objects |
| Expression | Effect Predicate | Captures computational side effects | `IO A`, `State S A` |
| Value | Null Safety | Absence or controlled presence of null | `Option<T>`, `T?` |
| Runtime Memory | Memory Safety | Safe memory access guarantees | no dangling pointers, no UAF |
| Concurrent Processes | Concurrency Safety | Absence of race conditions | Send/Sync traits, ownership |
| Function Type | Determinism Predicate | Same input produces same output | pure function `A → B` |
| Program / Function | Termination Property | Computation always halts | total functions |
| Evaluation Step | Progress Property | Execution never gets stuck | progress theorem |
| Evaluation Step | Preservation Property | Types preserved during evaluation | preservation theorem |
| Data Flow | Security / Information Flow | Control of information leakage | taint types, IFC systems |
| Capability / Context | Capability Predicate | Permission-based access control | capability types |
| Communication Type | Protocol Correctness | Valid ordering of interactions | session types |
| Value / Type | Refinement Predicate | Logical constraint over values | `{x: Int |
| Abstract Type | Existential Abstraction | Hidden implementation behind interface | `exists T. (T, T→Bool)` |
| Type Shape | Structural Compatibility | Compatibility via structure | TypeScript object typing |
| Type Constructor | Type Computability | Type-level evaluation feasibility | type families, constexpr types |

### Type  System Space

> Which are the types of types of systems?
> 

| Type | Description | Structure | Instance(s) |
| --- | --- | --- | --- |
| **Static Type System** | Type correctness is enforced at compile-time before execution | `J ⊢ e : T` derivations checked statically | Haskell, ML, Rust |
| **Dynamic Type System** | Types are enforced at runtime during evaluation | Runtime tagging + dynamic checks | Python, JavaScript, Ruby |
| **Gradual Type System** | Mixes static and dynamic typing with optional annotations | Static + dynamic boundary checks | TypeScript, Python (mypy mode), Hack |
| **Strong Type System** | Prevents unsafe implicit conversions and enforces strict type rules | Strict coercion lattice | Haskell, Rust (mostly) |
| **Weak Type System** | Allows implicit coercions and unsafe conversions | Coercion-heavy runtime semantics | C, JavaScript |
| **Nominal Type System** | Type equivalence is based on explicit declarations/names | Name-based identity relation | Java, C#, Go |
| **Structural Type System** | Type equivalence is based on shape/fields | Structural matching rules | TypeScript, OCaml (records) |
| **Subtyping Type System** | Types are organized in an inclusion hierarchy | Partial order `(A <: B)` | Java, Scala, C++ |
| **Polymorphic Type System** | Supports parametric abstraction over types | `∀T. e : T → T` | Haskell, ML |
| **Ad-hoc Polymorphic System** | Supports overloading via type-specific implementations | Resolution by dispatch rules | C++, Haskell typeclasses |
| **Dependent Type System** | Types depend on values | `Vec n A`, propositions-as-types | Coq, Agda, Idris |
| **Refinement Type System** | Types refined with logical predicates | `{x : T | P(x)}` constraints |
| **Linear Type System** | Enforces single-use resource semantics | Linear logic constraints | Rust (ownership core), Clean |
| **Affine Type System** | At-most-once use semantics | Weak linearity constraint | Rust (borrowed values) |
| **Effect Type System** | Tracks computational effects in types | Effect annotations `IO, State` | Haskell, Koka |
| **Session Type System** | Types describe communication protocols | Duality + protocol automata | Rust async protocols, π-calculus systems |
| **Intersection Type System** | Types can simultaneously satisfy multiple constraints | Type conjunction `A & B` | TypeScript, theoretical λ-calculus |
| **Union Type System** | Types allow multiple alternatives | Type disjunction `A | B` |
| **Recursive Type System** | Supports self-referential type definitions | Fixed-point type equations | OCaml, Haskell |
| **Existential Type System** | Supports abstraction hiding concrete types | `∃T. (T, …)` packaging | ML modules, Rust `impl Trait` |
| **Higher-Kinded Type System** | Supports type constructors over type constructors | `F[_] : * → *` | Haskell, Scala |
| **Type-Level Computation System** | Enables computation at the type level | Reduction over types | Haskell type families, C++ templates |
| **Dependent Object Type System (DOT)** | Combines path-dependent types and subtyping | Object + type projection system | Scala |
| **Universe / Hierarchical Type System** | Prevents paradoxes via stratified type levels | `Type₀ : Type₁ : Type₂` | Coq, Agda |
| **Effectively Typed System (Untyped + constraints)** | Runtime system with optional static constraints | Hybrid constraint enforcement | Gradual languages, scripting runtimes |

### Mechanism Space

> Which is the space of **types of types**, that is the space of type creation mechanisms?
> 

| Category | Type of Type (Mechanism) | Description | Instance(s) |
| --- | --- | --- | --- |
| **Primitive** | Primitive Type | Atomic built-in types with no internal decomposition | `int`, `bool`, `char`, `float`, `void` |
| **Algebraic** | Product Type Constructor | Combines multiple types into a single compound type | `struct`, `(A, B)`, record |
| **Algebraic** | Sum Type Constructor | Disjoint union of alternatives | `A | B`, `enum`, `Either<A,B>` |
| **Functional** | Function Type Constructor | Defines mapping between input and output types | `A → B`, `fn(A)->B`, `(A)=>B` |
| **Parametric** | Parametric Type Constructor | Type abstraction over type variables | `List<T>`, `Option<T>`, `Map<K,V>` |
| **Higher-Kinded** | Higher-Kinded Type Constructor | Abstraction over type constructors | `F[_]`, `Functor F`, `Monad M` |
| **Recursive** | Recursive Type Constructor | Self-referential type definition (fixed-point) | `List`, `Tree`, `data Nat = Zero |
| **Dependent** | Dependent Type Constructor | Types indexed by values | `Vec n A`, `Fin n`, `Matrix(m,n)` |
| **Refinement** | Refinement Type Constructor | Types constrained by predicates | `{x: Int |
| **Abstract / Existential** | Existential Type Constructor | Hides implementation behind abstraction | `exists T. (T, T→Bool)`, `impl Trait` |
| **Abstract / Existential** | Abstract Type Constructor | Opaque type definition hiding representation | `abstract type Id`, ML module signature |
| **Type-Level Computation** | Type Function / Type Family | Computation at the type level mapping types → types | `type F<T> = ...`, Haskell `type family` |
| **Type-Level Computation** | Type Inference Mechanism | Algorithmic deduction of types from expressions | Hindley–Milner, local inference |
| **Relational** | Subtype Constructor | Defines hierarchy / inclusion relations between types | `A <: B`, inheritance, interfaces |
| **Relational** | Constraint Type Constructor | Types defined via bounds or constraints | `T extends Comparable`, trait bounds |
| **Logical (Set-Based)** | Union Type Constructor | Logical disjunction of types | `A | B`, `Union[A,B]` |
| **Logical (Set-Based)** | Intersection Type Constructor | Logical conjunction of types | `A & B`, `T with U` |
| **Structural** | Structural Type Constructor | Compatibility defined by shape | `{x: number}`, TypeScript object types |
| **Structural** | Duck Type Formation | Compatibility defined by behavior | “has method `.quack()`” |
| **Resource-Aware** | Linear Type Constructor | Exactly-once usage constraint | Rust linear/ownership types |
| **Resource-Aware** | Affine Type Constructor | At-most-once usage constraint | borrow systems |
| **Resource-Aware** | Session Type Constructor | Protocol-structured communication types | channel/session protocols |
| **Effectful** | Effect Type Constructor | Encodes computational effects in types | `IO A`, `State S A`, `Future A` |
| **Runtime / Dynamic** | Reflective Type Constructor | Runtime inspection or manipulation of types | `typeof`, RTTI, reflection |
| **Runtime / Dynamic** | Dynamic Type Constructor | Type determined at runtime rather than compile-time | Python objects, `dynamic` |
| General | class
 | … |  |
|  | struct | … |  |
|  | `record` |  |  |
|  | `enum` |  |  |
|  | `interface` |  |  |
|  |  |  |  |
|  | Type Alias Constructor (typedef
, using
, type) | Renaming / synonym formation over existing types |  |
| Abstract Data Types (ADTs) | … | .. | … |
| **Category-Theoretic** | F-Algebras / GADTs | `data Expr a where ...` | Constructor-specific return types. |
|  | F-Algebras / GADTs | `GADT` | Generalized algebraic data type. |
|  | Type Constructors as Functors | `Functor` | Interface for mapping over containers. |
|  | Type Constructors as Functors | `F[_]` | Type constructor of one argument. |
|  | Type Constructors as Functors | `map`, `flatMap` | Operations for functor-like types. |

### Type System Case Study

> Let’s explore a set of theoretical and practical type systems.
> 

| Type System | Description | Structure |
| --- | --- | --- |
| **Hindley–Milner (HM)** | A statically typed, implicitly polymorphic type system based on rank-1 universal quantification and first-order unification, guaranteeing principal types and decidable type inference for λ-calculus extended with let-polymorphism. | λ-calculus + let-polymorphism + unification + rank-1 ∀-types |
| **System F (Polymorphic λ-calculus)** | A statically typed system introducing explicit universal quantification over types, enabling full parametric polymorphism but sacrificing decidable type inference. | λ-calculus + explicit ∀ types + second-order polymorphism |
| **Simply Typed Lambda Calculus (STLC)** | The foundational statically typed λ-calculus where every term has a single monomorphic type and functions are explicitly typed. | λ-calculus + simple function types + typing rules (Γ ⊢ e : T) |
| **Dependent Type Theory (Martin-Löf Type Theory)** | A type system where types depend on values, enabling propositions-as-types and full program verification within the type system. | λ-calculus + dependent products (Π-types) + dependent sums (Σ-types) |
| **Calculus of Constructions (CoC)** | A higher-order dependent type system combining polymorphism and dependent types in a single unified framework underlying proof assistants. | λ-calculus + higher-order polymorphism + dependent types + universes |
| **System Fω** | An extension of System F allowing higher-kinded types and type operators, increasing abstraction over type constructors. | System F + type-level functions + kind system |
| **Rust Type System** | A statically typed system combining affine/linear ownership, lifetimes, and trait-based polymorphism to ensure memory and concurrency safety. | affine types + borrow checker + traits + lifetimes |
| **Haskell Type System (GHC Core)** | A statically typed, polymorphic system with advanced features like higher-kinded types, type families, and effect encoding via monads. | System Fω + type classes + type families + higher-kinded types |
| **Scala Type System (DOT-based core)** | A highly expressive object-oriented + functional type system combining path-dependent types, subtyping, and higher-kinded polymorphism. | DOT calculus + subtyping lattice + objects + type members |
| **TypeScript Type System** | A structurally typed, gradual type system enabling static analysis over a JavaScript runtime with union/intersection types. | structural typing + gradual typing + union/intersection types |
| **OCaml Type System** | A statically typed system based on Hindley–Milner with structural typing for records and algebraic data types. | HM + algebraic data types + structural records |
| **Java Type System** | A nominally typed, object-oriented type system with bounded generics and runtime type erasure. | nominal subtyping + generics + JVM erasure model |
| **C++ Type System** | A highly expressive static system with templates enabling compile-time metaprogramming and partial type inference. | templates + nominal typing + compile-time evaluation |
| **Coq Type System (CIC)** | A dependent type system used for formal verification, where types represent propositions and programs represent proofs. | Calculus of Inductive Constructions + universes + dependent types |
| **Agda Type System** | A dependently typed functional language emphasizing totality, termination checking, and proof construction. | dependent types + termination checker + pattern matching |
| **Kotlin Type System** | A statically typed system with null-safety, variance annotations, and JVM interoperability. | nullable types + generics + subtyping + inference |
| **Go Type System** | A statically typed, nominal system emphasizing simplicity, interfaces, and structural interface satisfaction. | nominal types + interfaces + implicit structural conformance |

## **Type Expression**

> **A Type Expression** is an expression that denotes a type. e.j `[2][3]`.
> 

## Type Rules

> A **rule** stating the conditions under which a particular program construct will not cause forbidden errors.
> 

> A formal, syntactic constraint or inference in a type system that governs how expressions, terms, or constructs can be assigned, manipulated, or transformed based on their types, ensuring that operations are consistent with the types of the involved entities and preserving type safety throughout the program.
> 

## Type **Judgment**

> A **type judgment** is a formal assertion in a type system, written as **Γ ⊢ e : T**, meaning that under the type environment **Γ**, the expression **e** has the type **T**.
> 

## Type Inference

> Aka. Type Deduction.
> 

> Is a **mechanism** by which a type system automatically deduces the types of expressions and variables based on their context and usage, without requiring explicit type annotations from the programmer.
> 

## **Type compatibility**

> **Type Compatibility and Conversion**: Rules for how different types can be used together and whether implicit type conversions are allowed.
> 

See [Type Compatibility](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-compatibility.md).

## Role of Type System

> How does a type system contribute to building more robust and reliable programs?
> 

| **Role/Use** | **Description** |
| --- | --- |
| **Memory Management** | Enforces rules for resource usage (ownership, borrowing) and ensures memory safety. |
| **Safety and Reliability** | Prevents type-related errors, such as null pointer dereferencing or type mismatches, ensuring safe execution. |
| **Concurrency and Parallelism** | Ensures safe communication and synchronization between concurrent processes, often using session types or other concurrency-specific types. |
| **Program Verification** | Uses dependent and refinement types to ensure program correctness through formal verification. |
| **Code Optimization** | Leverages type information to optimize code, particularly in memory layout, data handling, and function calls. |
| **Polymorphism and Code Reusability** | Enables writing generic code that can work with different types, increasing flexibility and maintainability (e.g., generics). |
| **Interoperability Between Systems** | Ensures different systems or languages can communicate by defining clear type boundaries and conversion mechanisms (FFI). |
| **Tooling and Developer Support** | Enhances IDE features like autocompletion, refactoring, and error checking based on type information. |
| **Security** | Enforces security policies, such as preventing unauthorized access to sensitive data, and ensures safe memory management. |
| **Expressiveness and Language Design** | Defines the complexity and flexibility of a language's abstraction mechanisms, supporting DSLs and domain-specific needs. |
| **Computational Effect** | Captures the impact of operations on the program's state, ensuring that side effects such as mutations, input/output, and exceptions are handled according to type system rules. |

## References

- [Run-time type information](https://www.wikiwand.com/en/Run-time_type_information)
- [Type Introspection](https://www.wikiwand.com/en/Type_introspection)
- [Typeof](https://www.wikiwand.com/en/Typeof)
- [Typed, modular macros for OCaml (oliviernicole.github.io)](https://news.ycombinator.com/item?id=13044221)
- [Cliff Click Language Hacking](https://github.com/cliffclick/aa)
- [Implementations of Type Systems in OCaml](https://github.com/tomprimozic/type-systems)
- [Counterexamples in Type Systems](https://counterexamples.org/intro.html)
- [Type Theory](https://en.wikipedia.org/wiki/Type_system)
- [Dependent Types at Work](http://www.cse.chalmers.se/~peterd/papers/DependentTypesAtWork.pdf)
- [Programming with abstract data types](https://dl.acm.org/doi/10.1145/942572.807045)
- [Type erasure and reification](https://eli.thegreenplace.net/2018/type-erasure-and-reification/)
- [Type inference](https://eli.thegreenplace.net/2018/type-inference/)
- [Challenges in Type Systems](https://dl.acm.org/doi/pdf/10.1145/251595.251607)
- [CS 331 Spring 2018 A Primer on Type Systems](https://www.cs.uaf.edu/users/chappell/public_html/class/2018_spr/cs331/docs/types_primer.html)
- [Type System](https://www.wikiwand.com/en/Type_system)
- [Type Conversion](https://www.wikiwand.com/en/Type_conversion)
- [Uniqueness type](https://www.wikiwand.com/en/Uniqueness_type)
- [Type Systems for Programming Languages](https://people.mpi-sws.org/~dreyer/ats/papers/harper-tspl.pdf)
- [The Derivative of a Regular Type is its Type of One-Hole Contexts](http://strictlypositive.org/diff.pdf)
- Clancy, Kevin, Heather Miller, and Christopher Meiklejohn. "Monotonicity Types." (2017).
- [Monotonicity Types: Towards A Type System for Eventual Consistency](https://prl.khoury.northeastern.edu/blog/2017/10/22/monotonicity-types-towards-a-type-system-for-eventual-consistency/)
- [Type Theory](https://app.notion.com/p/Type-Theory-110c0f5171ec803ab9d3c7cf057b7da8?pvs=21)
- https://www.hedonisticlearning.com/posts/understanding-typing-judgments.html
- https://en.wikipedia.org/wiki/Tagged_union
- https://en.wikipedia.org/wiki/Algebraic_data_type