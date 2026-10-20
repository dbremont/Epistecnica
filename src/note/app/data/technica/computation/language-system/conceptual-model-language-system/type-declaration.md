---
tags: [type-system]
---

# Type Declaration


> A Type Declaration Model is a structured representation in programming languages used to define the structure, behavior, and constraints of data and objects within a system.
> 

Indeed, here’s a list of type declaration models commonly used in programming languages:

- **Interface**: A blueprint for a set of methods that a class must implement, ensuring certain behaviors are defined.
- **Class**: A blueprint for creating objects that encapsulate data and behavior, often used in object-oriented programming.
    - Inheritance Models / Subtyping Models
    
    These models and patterns offer various ways to structure and reuse code through inheritance, each with its own advantages and considerations depending on the programming language and application context.
        1. **Classical Inheritance**: A model where classes are organized in a hierarchy, and a subclass inherits attributes and behaviors from a parent class, forming an “is-a” relationship.
        2. **Prototypal Inheritance**: A model where objects serve as prototypes for creating new objects, with properties and methods inherited from the prototype object, common in languages like JavaScript.
        3. **Mixin**: A design pattern where a class can inherit behaviors and attributes from multiple sources by “mixing in” the traits of other classes, promoting code reuse and modularity.
        4. **Multiple Inheritance**: A model where a class can inherit attributes and methods from multiple parent classes, which can lead to the “diamond problem” of ambiguity in some languages.
        5. **Interface Inheritance**: A model where a class implements an interface, defining a contract for required methods, facilitating polymorphism and standardized behavior.
        6. **Composition**: A design approach where classes are constructed by combining instances of other classes, often achieving code reuse through object composition rather than traditional inheritance.
        7. **Delegate/Proxy**: A pattern where an object (delegate/proxy) acts on behalf of another object, forwarding method calls and interactions, allowing flexible behavior modification.
        8. **Traits**: Similar to mixins, traits are a language feature in some programming languages (e.g., Rust) that define reusable methods that can be used by multiple classes.
        9. **Subtype Polymorphism**: A concept where a subclass can be used wherever a parent class is expected, leveraging inheritance to achieve runtime polymorphism.
        10. **Abstract Classes**: Classes that cannot be instantiated on their own and typically provide a base for other classes to inherit from, often containing abstract methods that must be implemented by subclasses.
        11. **Shadowing**: A situation in which a subclass defines a member with the same name as one in the superclass, potentially causing ambiguity in which version gets accessed.
        12. **Template Method Pattern**: A design pattern where a base class defines a “template” algorithm with certain steps as placeholders, allowing subclasses to implement specific behavior for those steps.
    - …
- **Struct**: A composite data type that groups together variables under a single name in a way that allows for accessing individual elements.
- **Enumeration**: A distinct type that consists of a set of named values, which can make code more readable and less error-prone.
- **Union**: A type that can hold values of different types at different times, useful for modeling flexible data structures.
- **Record**: A data structure that stores an ordered collection of fields, each with its own name and data type.
- **Type Alias**: A new name assigned to an existing data type, used for enhancing code readability and expressiveness.
- **Variant/Tagged Union**: A type that can hold one of several named values, each associated with a specific data type.
- **Abstract Data Type (ADT)**: A data type defined by its behavior rather than its implementation, emphasizing encapsulation.
- **Protocol**: A set of methods that a class can adopt, indicating certain behaviors it supports, often used in Swift programming.
- **Trait**: A set of methods that a class or struct can implement, providing a way to share behavior across different types in Rust.
- **Type Class**: A concept in functional programming that defines a set of operations applicable to different types, enabling polymorphism.
- **Interface Definition Language (IDL)**: A language used to describe interfaces in a distributed system, allowing communication between different components.
- **Parametric Types**: A feature in programming languages that allow the definition of functions, classes, or data structures to work with multiple types of data, with the actual types specified when the function or structure is used, enhancing code reusability and flexibility.
    1. **Generics**: Generics are a programming language feature that allow you to define classes, functions, or interfaces with placeholders for data types. These placeholders, known as type parameters, are replaced with actual data types when the code is used, enabling the creation of reusable and type-safe components.
    2. **Templates**: Templates, commonly found in languages like C++ and D, are a mechanism for creating generic classes or functions where types and values can be parameterized. Template classes and functions are instantiated with specific types or values, allowing for code specialization and reusability.
- **Intersection types**: Intersection types allow a variable or parameter to be of multiple types at the same time.
- **Refinement types**: Refinement types allow for additional constraints or refinements to be specified on basic types, providing more precise type checking and program verification.
- **Primitive Types**: These are the basic building blocks of a programming language’s type system, such as integers, floating-point numbers, and booleans.
- **Bag of Types**: Name Spaces, …
- **Null and Option Types**: How the language deals with the absence of a value (null/nil) and whether optional types are used.