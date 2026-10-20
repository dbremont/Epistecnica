---
tags: [type-system]
---

# Subtyping

- [Polymorphism](note.html?n=technica/computation/language-system/conceptual-model-language-system/polymorphism.md), [Type Variance](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-variance.md)

> **Type Hierarchy**: How types are organized hierarchically, allowing for subtype relationships.
> 

> **Subtyping**: A reflexive and transitive binary relation over types that satisfies subsumption; it asserts the inclusion of collections of values.
> 

> **Subsumption** is a fundamental rule of subtyping, asserting that if a term has type A, which is a subtype of type B, then the term also has type B.
> 

April 16, 2024 Improve legibility using a table (refactor to tables).

## Models

Subtyping models in programming languages refer to the ways in which types can be related to each other, allowing for flexibility and polymorphism. Here are some common subtyping models:

1. **Nominal Subtyping:**  Subtyping is based on explicit type names, and two types are considered subtypes if one type is explicitly declared to be a subtype of another.
    - **Example:** In Java, explicit interface implementations provide nominal subtyping.
2. **Structural Subtyping:** Subtyping is based on the structure or shape of types, where types with compatible structures are considered subtypes.
    - **Example:** Duck typing in dynamically typed languages like Python and TypeScript's structural typing.
3. **Parametric Polymorphism (Generics):**  Types are considered subtypes if they are parameterized by the same generic type and share a common structure.
    - **Example:** Generics in languages like Java, C++, and C#.
4. **Covariant Subtyping:**  Subtyping preserves the ordering of types, meaning that if `A` is a subtype of `B`, then `List<A>` is a subtype of `List<B>`.
    - **Example:** Arrays in Java exhibit covariant subtyping.
5. **Contravariant Subtyping:** Subtyping is reversed, meaning that if `A` is a subtype of `B`, then `Function<B>` is a subtype of `Function<A>`.
    - **Example:** Function arguments in languages with contravariant subtyping.
6. **Bounded Quantification:**  Subtyping is constrained within certain bounds, where types must satisfy specified conditions.
    - **Example:** Bounded type parameters in languages like Java and Scala.
7. **Recursive Subtyping:** Subtyping relationships are defined recursively for complex types or structures.
    - **Example:** Recursive types in languages with advanced type systems.
8. **Intersection Types:** Subtyping is based on the combination of multiple types, where a type is a subtype if it is compatible with all constituent types.
    - **Example:** Intersection types in languages like TypeScript.
9. **Union Types:**  Subtyping allows for a type to be a subtype of multiple types, providing flexibility in handling different possibilities.
    - **Example:** Union types in languages like TypeScript and functional programming languages.
10. **Existential Types:**  Subtyping allows for the abstraction of specific types, creating a more flexible and polymorphic interface.
    - **Example:** Existential types in languages with support for existential quantification.

These subtyping models provide various ways to express relationships between types, contributing to the expressiveness and flexibility of programming languages.

## Inheritance vs Composition

> How to build new types?
> 

Here are some reasons why composition can be favored over inheritance in object-oriented programming:

- **Increased flexibility**: Composition allows for more flexible designs than inheritance, as it enables the creation of objects that can be easily composed of various components. With composition, objects can be composed of smaller, more specialized objects, which can be replaced or modified without affecting the overall behavior of the containing object.
- **Easier to modify**: When using inheritance, making changes to the base class can affect all the subclasses that inherit from it, which can result in a ripple effect that can be difficult to manage. With composition, changes to the behavior of a component can be made independently of the containing object, without affecting other components or the overall behavior of the containing object.
- **Easier to test**: Composition makes it easier to write testable code, as components can be tested in isolation. This can result in more reliable and maintainable code, as tests can be run more quickly and with greater confidence.
- **Improved encapsulation**: Composition can improve encapsulation, as it allows objects to have a more clear and well-defined interface, hiding their implementation details from the rest of the code. This can help prevent unwanted coupling between objects, which can make code more difficult to maintain and modify.
- **Better code reuse**: Composition allows for more fine-grained code reuse than inheritance, as components can be easily composed in different combinations to create new objects. This can result in more efficient and maintainable code, as it reduces the need to duplicate code or make extensive modifications to existing code.
- **Avoiding the “fragile base class” problem**: The “fragile base class” problem is a common issue in inheritance, where changes to the base class can cause unexpected behavior in subclasses. This can be avoided with composition, as changes to a component do not affect the behavior of the containing object unless explicitly designed to do so.

Overall, composition can provide a more flexible, maintainable, and reliable approach to object-oriented programming than inheritance in many cases. However, both composition and inheritance have their place, and the choice between them ultimately depends on the specific requirements and constraints of the project at hand.

- Partial Objects / Partial Appliations / Incremental Computation Definition / Runtime Extention / Personalizatoin / Hook System / Partial Evaluation

## …

Here’s a table summarizing key **polymorphism-related concepts** in object-oriented programming (OOP):

| **Concept** | **Description** | **Example** |
| --- | --- | --- |
| **Polymorphism** | The ability of objects to take on multiple forms or behaviors. | A `Animal` reference can point to a `Dog` or `Cat` object. |
| **Static Polymorphism** | Resolved at compile time (also called compile-time polymorphism). | Method overloading or operator overloading. |
| **Dynamic Polymorphism** | Resolved at runtime (also called runtime polymorphism). | Method overriding using inheritance and virtual functions. |
| **Method Overloading** | Multiple methods with the same name but different parameters (static binding). | `void print(int x)` and `void print(String s)` in the same class. |
| **Method Overriding** | Subclass provides a specific implementation of a method already defined in its superclass (dynamic binding). | `Dog` overrides `sound()` method of `Animal`. |
| **Dynamic Dispatch** | Mechanism to decide which method implementation to call at runtime. | Calling `sound()` on an `Animal` reference that points to a `Dog` object. |
| **Virtual Functions** | Functions in a base class that can be overridden in derived classes (C++). | `virtual void sound() { ... }` in C++. |
| **Abstract Classes** | Classes that cannot be instantiated and may contain abstract methods. | `abstract class Animal { abstract void sound(); }` |
| **Interfaces** | Contracts that define a set of methods a class must implement. | `interface Flyable { void fly(); }` implemented by `Bird` and `Airplane`. |
| **Upcasting** | Treating a derived class object as an instance of its base class. | `Animal myAnimal = new Dog();` |
| **Downcasting** | Treating a base class object as an instance of its derived class (requires explicit casting). | `Dog myDog = (Dog) myAnimal;` |
| **Inheritance** | A mechanism where a class derives properties and behaviors from another class. | `Dog` inherits from `Animal`. |
| **Subtyping** | A relationship where a derived class is considered a subtype of its base class. | `Dog` is a subtype of `Animal`. |
| **Parametric Polymorphism** (Generics) | Writing code that can operate on any data type (e.g., templates in C++ or generics in Java). | `List<T>` in Java or `std::vector<T>` in C++. |
| **Ad-hoc Polymorphism** | Functions or methods that behave differently based on the type of arguments. | Operator overloading (e.g., `+` for integers vs. strings). |

## References

- [A behavioral notion of subtyping](https://dl.acm.org/doi/10.1145/197320.197383)