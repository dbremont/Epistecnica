---
tags: [design-idiom]
---

# Design Idiom


> aka. Design Pattern.
> 

> **Note:** I don’t like the name **design pattern** (a template to solve a program design problem). In these notes, I am going to use the term **design idiom** instead, to standardize the language in alignment with the related concept of an idiom.
> 

## Taxonomy

| **Category** | **Pattern** | **Description** |
| --- | --- | --- |
| Creational 🛠️ | Singleton | Ensures a class has only one instance and provides a global point of access. |
|  | Factory Method | Defines an interface for creating an object, but lets subclasses alter the type. |
|  | Abstract Factory | Provides an interface for creating families of related or dependent objects. |
|  | Builder | Separates object construction from its representation. |
|  | Prototype | Creates new objects by copying an existing object (prototype). |
| Structural 🧱 | Adapter | Allows incompatible interfaces to work together. |
|  | Bridge | Separates abstraction from implementation so they can vary independently. |
|  | Composite | Composes objects into tree structures to represent part-whole hierarchies. |
|  | Decorator | Adds responsibilities to objects dynamically. |
|  | Facade | Provides a simplified interface to a larger body of code. |
|  | Flyweight | Reduces memory usage by sharing common parts of objects. |
|  | Proxy | Provides a surrogate or placeholder for another object. |
| Behavioral 🧠 | Chain of Responsibility | Passes the request along a chain of handlers. |
|  | Command | Encapsulates a request as an object. |
|  | Interpreter | Implements a language grammar as a hierarchy of classes. |
|  | Iterator | Provides a way to access elements without exposing structure. |
|  | Mediator | Defines an object that coordinates interactions between others. |
|  | Memento | Captures and restores an object's internal state. |
|  | Observer | Defines a one-to-many dependency between objects. |
|  | State | Allows an object to alter its behavior when its internal state changes. |
|  | Strategy | Defines a family of algorithms, encapsulates each one. |
|  | Template Method | Defines the skeleton of an algorithm in a base class. |
|  | Visitor | Represents an operation to be performed on the elements of an object structure. |
| Concurrency ⚙️ | Thread Pool | Manages a pool of worker threads. |
|  | Active Object | Decouples method execution from method invocation. |
|  | Monitor Object | Encapsulates all aspects of synchronization. |
|  | Scheduler | Centralized object to manage when and how tasks are run. |
|  | Reactor | Handles service requests delivered concurrently to a handler. |
|  | Future | Represents a result of an async computation. |
| Distributed 🌐 | Broker | Provides a centralized registry for remote service access. |
|  | Client Proxy | Local representation of a remote object. |
|  | Microkernel (Plug-in) | Core system with extensible plug-ins. |
|  | Service Locator | Abstracts the process of obtaining service instances. |
|  | Event Bus | Messaging mechanism for event-driven systems. |
|  | Data Transfer Object (DTO) | Transfers data with multiple attributes in one shot. |
|  | Circuit Breaker | Prevents a system from repeatedly trying to execute an operation likely to fail. |
|  | API Gateway | Manages requests to multiple microservices. |
|  | Load Balancer | Distributes workloads across multiple resources. |
|  | Double-Checked Locking | Reduces contention by acquiring a lock only when necessary, typically used for lazy initialization of singletons. |
|  | Balking | Only executes an action on an object if the object is in a particular state; otherwise, it "balks" or returns. |
| **…** | **…** | **…** |
|  | Unit of Work | Maintains a list of objects affected by a business transaction and coordinates the writing out of changes and the resolution of concurrency problems. |
|  | Type Object | Creates a class that holds type information for objects, allowing the type to be changed at runtime. |
|  | Inversion of Control (IoC) | A programming principle where the control of object creation and lifecycle is transferred to a container or framework. (Often implemented with Dependency Injection) |
|  | Dependency Injection | A technique whereby one object supplies the dependencies of another object, rather than the dependent object creating them itself. |
|  | Locking Pattern |  |

## References

- https://en.wikipedia.org/wiki/Software_design_pattern
- [Concurrency](note.html?n=technica/computation/concurrency.md)