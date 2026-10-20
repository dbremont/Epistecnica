---
tags: [technique]
---

# Refactoring


> Refactoring is the disciplined process of restructuring existing code to improve its internal design, readability, and maintainability without changing its external behavior.
> 

## Technique

| Technique | Description |
| --- | --- |
| **Defunctionalization** | Transformation that replaces higher-order functions with equivalent first-order ones. |
| **Extract Method** | Extracts a section of code from a larger method and places it in a new method to improve readability and maintainability. |
| **Inline Method** | Removes a method call and places the method code directly in the calling method to simplify code and improve performance. |
| **Extract Variable** | Extracts a complex expression or value into a named variable to improve readability and maintainability. |
| **Inline Variable** | Removes a variable and replaces it with its value in code to simplify code and improve performance. |
| **Rename Method/Variable/Class** | Changes the name of a method, variable, or class to better reflect its purpose and improve readability. |
| **Move Method/Field** | Moves a method or field from one class to another to improve organization and cohesion. |
| **Replace Conditional with Polymorphism** | Replaces a complex conditional with a set of polymorphic classes to improve maintainability and reduce complexity. |
| **Extract Interface** | Extracts related methods from a class and defines them in an interface to improve reusability and flexibility. |
| **Collapse Hierarchy** | Collapses a class hierarchy into a single class to simplify code and improve maintainability. |
| **Introduce Parameter Object** | Combines a set of related parameters into a single object to improve readability and maintainability. |
| **Replace Method with Method Object** | Creates a new class to represent a complex method and moves the method code to that class to simplify code and improve maintainability. |
| **Remove Duplicate Code** | Identifies and removes duplicate code to improve readability and maintainability. |

## References

- How to Change a System ([enablingchange.com.au](http://enablingchange.com.au/)) [https://news.ycombinator.com/item?id=39499704](https://news.ycombinator.com/item?id=39499704)
- https://blog.sigplan.org/2019/12/30/defunctionalization-everybody-does-it-nobody-talks-about-it/