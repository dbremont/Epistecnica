---
tags: [principle]
---

# SOLID


> The **SOLID** principles are a set of five foundational guidelines for designing maintainable, flexible, and scalable object-oriented software. Coined by Robert C. Martin (“Uncle Bob”), these principles help developers create systems that are easier to understand, extend, and refactor over time. By following SOLID, software components become more modular, reducing bugs and improving collaboration across teams. Each principle addresses a specific aspect of software design, collectively promoting clean architecture and robust codebases.
> 

![image.png](../assets/note/technica/computation/system/programming/conceptual-model-programming/solid/image.png)

## Principle

| **Principle** | **Description** | **Key Idea** | **Benefit** |
| --- | --- | --- | --- |
| **Single Responsibility Principle (SRP)** | A class should have only one reason to change. | One class, one responsibility | Easier maintenance, less complexity |
| **Open/Closed Principle (OCP)** | Software entities should be open for extension, but closed for modification. | Extend behavior without modifying existing code | Safer code changes, easier feature addition |
| **Liskov Substitution Principle (LSP)** | Subtypes must be substitutable for their base types without altering correctness. | Subclasses follow base class behavior | Correctness, reliability of inheritance |
| **Interface Segregation Principle (ISP)** | Clients should not depend on interfaces they do not use. | Use many specific interfaces instead of one general interface | Reduced unnecessary dependencies |
| **Dependency Inversion Principle (DIP)** | Depend on abstractions, not on concretions. | High-level modules depend on abstractions | Looser coupling, easier testing and flexibility |

## References

- https://en.wikipedia.org/wiki/SOLID