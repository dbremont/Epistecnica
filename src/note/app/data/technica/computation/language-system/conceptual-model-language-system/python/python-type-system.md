# Python: Type System

> The Python type system is a **gradual, dynamically-typed, strongly-typed, and structurally subtyped** system that enforces type safety at runtime through object-level type metadata while supporting optional static type annotations via the `typing` module, leveraging both **nominal typing** (class-based inheritance) and **structural typing** (protocol-based duck typing), with limited type inference, explicit and implicit coercion (e.g., `int` to `float` but not `str` to `int`), runtime metaprogramming via `type()` and metaclasses, and interoperability between dynamically and statically typed codebases through gradual typing mechanisms.
> 

QA:

- …

## Python Type System

> 

| **Aspect** | **Python Type System** |
| --- | --- |
| **Typing Discipline** | Gradual, Dynamic, Strong |
| **Type Checking** | Dynamic (runtime) and Optional Static (via `mypy`, `pyright`) |
| **Type Safety** | Enforced at runtime (strong typing) |
| **Type Inference** | Limited (e.g., function return inference in static checkers) |
| **Type Annotations** | Optional (e.g., `def func(x: int) -> str:`) |
| **Type Enforcement** | Runtime checks (`isinstance`, `type`) + static checks (`mypy`) |
| **Type Mutability** | Variable bindings are mutable; object mutability depends on type |
| **Nominal Typing** | Supported via class inheritance (`isinstance`, `issubclass`) |
| **Structural Typing** | Supported via `Protocol` (duck typing with static checks) |
| **Duck Typing** | Implicit, enforced at runtime |
| **Type Coercion** | Limited implicit (e.g., `int` to `float`), explicit via `cast()` |
| **Generics** | Supported (`List[T]`, `TypeVar`) |
| **Union Types** | Supported (`Union[int, str]` or `int |
| **Metaprogramming** | `type()`, metaclasses, dynamic attribute/method injection |
| **Reflection** | `isinstance()`, `hasattr()`, `getattr()`, `__annotations__` |
| **Runtime Type Creation** | Possible (`type()`, `exec()`, metaclasses) |
| **Function Overloading** | Supported via `@overload` (checked statically) |
| **Variadic Typing** | Supported (`*args: T`, `**kwargs: U`) |

## **Type Creation Mechanisms**

> Here is a table summarizing the different types in `x`:
> 

| **Mechanism** | **Description** | **Example** |
| --- | --- | --- |
| **Class Definition (`class`)** | Standard way to define new types using class syntax. | `python class MyClass: pass` |
| **Metaclasses (`type` subclassing)** | Customizes class creation by modifying class behavior. | `python class Meta(type): pass` |
| **Dynamic Type Creation (`type()`)** | Creates a new type dynamically at runtime. | `python MyClass = type('MyClass', (object,), {'x': 42})` |
| **`dataclass` (via `@dataclass`)** | Generates classes with built-in init, repr, and eq. | `python @dataclass class Point: x: int; y: int` |
| **`namedtuple` (via `collections`)** | Immutable tuple-like class with named fields. | `python Point = namedtuple('Point', ['x', 'y'])` |
| **`TypedDict` (via `typing`)** | Defines structured dictionary types. | `python class Config(TypedDict): debug: bool` |
| **Function Closures** | Functions with internal state acting as lightweight types. | `python def make_counter(): count = 0; def counter(): nonlocal count; count += 1; return count; return counter` |
| **Dynamic Attribute Injection** | Modifies an existing class or instance at runtime. | `python MyClass.new_attr = 100` |
| **Abstract Base Classes (ABCs)** | Defines interfaces and enforces subclassing contracts. | `python class MyABC(ABC): @abstractmethod def method(self): pass` |
| **Protocols (`typing.Protocol`)** | Defines structural subtyping (static duck typing). | `python class SupportsAdd(Protocol): def __add__(self, other): ...` |
| **C Extensions (`cffi`, `ctypes`)** | Creates types at the C level for performance. | Uses `cffi.FFI().new("int *")` |
| **Foreign Function Interfaces (`ctypes`)** | Wraps C structs and functions into Python types. | `python class Point(ctypes.Structure): _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]` |
| **Dynamic Code Execution (`exec()` and `eval()`)** | Creates types dynamically from string source code. | `python exec("class MyClass: pass")` |

## Type Coercions

> **Type coercions** are implicit operations that change the type of a value. They happen automatically at specific locations and are highly restricted in what types actually coerce.
> 

> 

## Module System

> 

## Standard Library Types

- > See  [Python: The Standard Library]
> 

## **Dynamic Typing (Latent Typing)**

- Python is dynamically typed, meaning that type enforcement occurs at runtime, not at compile time.
- Variables do not have explicit types; they are simply references to objects that have types.
- Example:
    
    ```python
    x = 42  # x is bound to an int object
    x = "hello"  # Now bound to a str object
    
    ```
    

## **Strong Typing**

- Python does not implicitly convert types in unexpected ways.
- Type errors occur at runtime if an operation is not supported for a given type.
- Example:
    
    ```python
    "5" + 5  # Raises TypeError
    
    ```
    

## **Structural and Nominal Typing (Hybrid)**

- Python's native objects follow **nominal typing** (based on class inheritance).
- The `typing` module introduces **structural typing** via protocols (akin to duck typing but checked statically).
- Example of nominal typing:
    
    ```python
    class A: pass
    class B(A): pass
    isinstance(B(), A)  # True (nominal typing)
    
    ```
    
- Example of structural typing:
    
    ```python
    from typing import Protocol
    
    class SupportsLength(Protocol):
        def __len__(self) -> int: ...
    
    def get_length(obj: SupportsLength) -> int:
        return len(obj)
    
    get_length([1, 2, 3])  # Works (duck typing with static check)
    
    ```
    

## **Gradual Typing**

- Python allows **optional type annotations**, enforced by static checkers like `mypy` but ignored at runtime.
- Example:
    
    ```python
    def add(x: int, y: int) -> int:
        return x + y
    
    ```
    
- Despite annotations, Python allows violations at runtime:
    
    ```python
    add("a", "b")  # Works but should be caught by static checkers
    
    ```
    

## **Duck Typing**

- An object's compatibility with an operation depends on the presence of methods/attributes rather than explicit inheritance.
- Example:
    
    ```python
    class Duck:
        def quack(self):
            print("Quack!")
    
    def make_quack(animal):
        animal.quack()
    
    make_quack(Duck())  # Works without needing explicit type checks
    
    ```
    

## **Type Inference (Limited)**

- Python does **not** perform full type inference like Haskell but uses limited inference in function return values:
    
    ```python
    def foo(x: int):
        return x * 2  # Static tools infer int -> int
    
    ```
    

## **Metaclass and Dynamic Type Creation**

- Python allows runtime type creation using `type()` and metaclasses.
- Example:
    
    ```python
    MyClass = type("MyClass", (object,), {"attr": 42})
    
    ```
    

## **Type Coercion and Immutability**

- Python supports some implicit type coercion (e.g., `int -> float`).
- `int`, `float`, `str`, `tuple` are immutable; `list`, `dict`, and `set` are mutable.

## **Union and Generic Types**

- Python 3.9+ supports `Union` and generics with `TypeVar`.
- Example:
    
    ```python
    from typing import Union
    
    def process(value: Union[int, str]) -> str:
        return str(value)
    
    ```
    

## References

- https://typing.python.org/en/latest/spec/
- https://realpython.com/python-type-checking/
- [ ]  Rak-Amnouykit, Ingkarat, et al. "Python 3 types in the wild: a tale of two type systems." Proceedings of the 16th ACM SIGPLAN International Symposium on Dynamic Languages. 2020.
- [ ]  https://justapedia.org/wiki/Python_(programming_language)
- [Type System](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-system.md)
- [X: **🏷️** Type System](https://app.notion.com/p/X-Type-System-fc2456113c894e699643d8ce60a4647f?pvs=21)