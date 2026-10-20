---
tags: [design-idiom]
---

# Visitor Pattern


> It defines a visiting strategy in an object structure.
> 

> It allows visitor to visit / traverse the object structure.
> 

> Separates an algorithm from an object structure by moving the hierarchy of methods into one object.
> 

> Defining the **visitor structure in an art**  the method sign (parameters, and return return type, body) will depend on the use case.
> 

> **Double Dispatch:** The Visitor pattern leverages the concept of double dispatch. Normally, in single dispatch languages like Java, the method invoked depends on the runtime type of the object. With double dispatch, the operation that is executed depends on both the type of the visitor and the type of the element being visited. This allows the visitor to execute different logic based on the combination of its type and the type of the element.
> 

How to’s?

1. Defines the visitor structure in the object structure.
2. Create the visitor to operate on that structure.

```python
# Interface / Implementation
# Abstraction / Implementation
```

```python
class Element:
    def accept(self, visitor):
        visitor.visit(self)

    def operation(self):
        return "Element operation"
```

```python
class Visitor:
    def visit(self, element):
        pass
```

```python
class ConcreteVisitor(Visitor):
    def visit(self, element):
        result = element.operation()
        print(f"{result} visited by ConcreteVisitor")
```

```python
element = Element()
visitor = ConcreteVisitor()
element.accept(visitor)
```

## References

- https://github.com/dotnet/runtime/blob/main/src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/XmlIlVisitor.cs
- …