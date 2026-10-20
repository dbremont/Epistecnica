---
tags: [type-system]
---

# Type Compatibility

- [Type Variance](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-variance.md), [Type System](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-system.md)

> **Type compatibility** is the set of rules in a programming language that determines whether a value of one type can be assigned to a variable of another type, either directly or through implicit or explicit conversion.
> 

> Assignment compatibility in programming languages is determined by a combination of **type system rules**, which dictate how values of different types can be assigned to variables.
> 

The key rules include:

### **Type Compatibility Rules**

These rules define whether a value of one type can be assigned to a variable of another type.

- **Exact Type Matching**: A value can be assigned if its type matches the variable’s type exactly.
- **Implicit Type Conversion (Type Coercion)**: Some languages allow automatic conversion (e.g., `int` to `float` in Python, Java).
- **Explicit Type Conversion (Casting)**: If a conversion isn't implicit, an explicit cast may be required (e.g., `(int) 3.14` in C).
- **Subtype Polymorphism**: A value of a subclass (derived class) can be assigned to a variable of its superclass (base class) in object-oriented languages.
- **Interface-based Assignment**: If a type implements an interface, it can be assigned to a variable of that interface type.

### **Mutability and Const Rules**

- **Const-Correctness**: In languages like C++, assigning a `const` value to a non-`const` variable is prohibited.
- **Immutable vs. Mutable Types**: Immutable values (e.g., Python strings) can’t be reassigned in place.

### **Reference vs. Value Semantics**

- **Value Assignment**: In languages with value semantics (C, Rust structs), assignment creates a copy.
- **Reference Assignment**: In languages with reference semantics (Java, Python, C++ with pointers), assignment copies the reference.

### **Type Inference and Generic Types**

- **Type Inference**: Some languages infer the type of variables (`auto` in C++, `var` in C#).
- **Generics and Template Rules**: Generic types (e.g., `List<T>` in Java, C#) may have constraints on allowed assignments.

## References

- https://stackoverflow.com/questions/70619201/type-compatibility-understanding-issues