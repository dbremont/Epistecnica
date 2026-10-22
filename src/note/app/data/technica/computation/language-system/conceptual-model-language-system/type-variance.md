---
tags: [type-system]
---

# Type Variance

- [Subtyping](note.html?n=technica/computation/language-system/conceptual-model-language-system/subtyping.md), [Type System](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-system.md), [Type Compatibility](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-compatibility.md)

> **Type variance** is a **type judgment** that governs the behavior of type substitutions in the presence of subtyping, ensuring the correct propagation of type relationships (covariant, contravariant, or invariant) for parameterized types in both function input and output positions, thereby preserving type safety and consistency in polymorphic contexts.
> 

> **Type variance** refers to how subtyping relationships (covariant, contravariant,  bi-variant or invariant) between **types** in a type system affect their **compatibility** and behavior in the context of inheritance, generics, or function types.
> 

> Note:  This note focus too much on parameterized types;  but Type Variance maybe a more fundamental and general idea of defining type relationships.
> 

> Note: The Idea of Variance; Is also used  with a deep, fundamental philosophical connection in **Linear Algebra**.
> 

> Covariance and contravariance are just **monotonicity** and **anti-monotonicity**, applied to **types ordered by subtyping**. See more in [Monotonicity](https://app.notion.com/p/Monotonicity-1bac0f5171ec80df8facc313b54a24b5?pvs=21).
> 

QA:

- What is **contra variance**? Why the concept is used? Which type systems supported?
- What is **variance in typing**? Variance refers to how sub-typing between composite types relates to sub-typing between their components. Variance is **about assignment compatibility**.

## Type Variance

> The notation `$Y <: X$` is common in type theory, meaning that **Y can be used wherever X is expected** (subtyping relationship).
> 

> Given types `$X$` and `$Y$` with the relation  `$Y <: X$` , variance is a way to describe the relation between the composite types:
> 
- **Covariant** means the ordering of component types is preserved: `Composite<Y> <: Composite<X>`.
- **Contravariant** means the ordering is reversed: `Composite<X> <: Composite<Y>`.
- **Bivariant** means both covariant and contravariant.
- **Invariant** means neither covariant nor contravariant.

![Covariance vs Contra-Variance](../assets/note/technica/computation/language-system/conceptual-model-language-system/type-variance/image.png)

Covariance vs Contra-Variance

## Function Type Variance

> Function Type Variance governs the type relationship between the `function signature type` and the `function implementation type`.
> 

> **Function type variance** refers to how the types of function arguments and return values behave when you create a subtype or superclass of a function type.
> 

> **Covariance** allows more specific return types in function signatures.
> 

> **Contravariance** allows more general argument types in function signatures.
> 

> Invariant types are where no variance applies. The function is neither covariant nor contravariant regarding its inputs and outputs. A function type `A -> B` is invariant if you cannot substitute it for a function of a different type (e.g., `Dog -> Animal`).
> 

> Function types with different argument or return types can exhibit these variances, enhancing flexibility in how functions can be assigned and used.
> 

![**Contra-variance** allows more general argument types in function signatures.](../assets/note/technica/computation/language-system/conceptual-model-language-system/type-variance/image-1.png)

**Contra-variance** allows more general argument types in function signatures.

```csharp
using System;

class Animal {}
class Dog : Animal {}
class Cat : Animal {}

public class Program
{
    // Covariant return type: A function returning a more specific type can be used where one returning a more general type is expected
    public static Func<Animal> CovariantReturn() => () => new Dog();

    // Contravariant argument type: A function that accepts a more general type can be used where one accepting a more specific type is expected
    public static void AcceptAnimal(Animal a) => Console.WriteLine(a.GetType().Name);
    public static void Main()
    {
        // Covariance example
        Func<Dog> dogFunction = CovariantReturn(); // Covariant: Func<Dog> can be used where Func<Animal> is expected
        Animal animal = dogFunction(); // Works fine, Dog is a subtype of Animal
        Console.WriteLine(animal.GetType().Name); // Output: Dog

        // Contravariance example
        Action<Dog> dogAction = AcceptAnimal; // Contravariant: Action<Animal> can be used where Action<Dog> is expected
        dogAction(new Dog()); // Works fine because AcceptAnimal can accept a Dog, a subclass of Animal
    }
}
```

## Case Studies

> How to know if a type is read or write only in C#?
> 

### **Covariance Example (`out` in C#)**

> Covariance allows **subtyping to be preserved** for **read-only** generic types.
> 

> ✅ `IEnumerable<T>` is **covariant (`out T`)**, so `IEnumerable<Cat>` is **a subtype of** `IEnumerable<Animal>`.
> 

```csharp
using System;
using System.Collections.Generic;

class Program
{
    static void PrintAnimals(IEnumerable<Animal> animals)  // Accepts IEnumerable<Animal>
    {
        foreach (var animal in animals)
            Console.WriteLine(animal.GetType().Name);
    }

    static void Main()
    {
        IEnumerable<Cat> cats = new List<Cat> { new Cat(), new Cat() };
        PrintAnimals(cats);  // Allowed because IEnumerable<T> is covariant
    }
}

class Animal {}
class Cat : Animal {}

```

### **Contravariance Example (`in` in C#)**

> Contravariance allows **subtyping to be reversed** for **write-only** generic types.
> 

> ✅ `IComparer<T>` is **contravariant (`in T`)**, so `IComparer<Animal>` is **a subtype of** `IComparer<Cat>`.
> 

```csharp
using System;
using System.Collections.Generic;

class Animal {}
class Cat : Animal {}

class AnimalComparer : IComparer<Animal>
{
    public int Compare(Animal? x, Animal? y) => 0;
}

class Program
{
    static void Main()
    {
        IComparer<Animal> animalComparer = new AnimalComparer();
        IComparer<Cat> catComparer = animalComparer;  // Allowed because IComparer<T> is contravariant
    }
}

```

### **Invariance Example (Default in Java & C#)**

> If a generic type is **invariant**, **subtyping is not preserved**.
> 

> ✅ `List<T>` is **invariant**, meaning `List<Cat>` is **not a subtype** of `List<Animal>`.
> 

```java
import java.util.*;

class Animal {}
class Cat extends Animal {}

public class Main {
    public static void main(String[] args) {
        List<Cat> cats = new ArrayList<>();
        // List<Animal> animals = cats;  // ❌ Compilation error! List<T> is invariant.
    }
}

```

## References

- https://en.wikipedia.org/wiki/Liskov_substitution_principle
- https://news.ycombinator.com/item?id=14831290
- https://eli.thegreenplace.net/2018/covariance-and-contravariance-in-subtyping/
- https://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science)
- https://web.archive.org/web/20150905085310/http://blogs.msdn.com/b/ericlippert/archive/2009/11/30/what-s-the-difference-between-covariance-and-assignment-compatibility.aspx
- [‣](https://app.notion.com/p/195598edb7908091a8bed6606187c18d?pvs=21)
- [‣](https://app.notion.com/p/1ba598edb79080fabf61fffa6b498a3e?pvs=21)
- https://softwareengineering.stackexchange.com/questions/149478/why-is-invariance-covariance-and-contravariance-necessary-in-typed-languages