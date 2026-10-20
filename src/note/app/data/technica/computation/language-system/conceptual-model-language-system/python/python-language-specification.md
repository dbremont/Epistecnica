# Python: 📜 Language Specification

> A **language specification** formally defines the syntax, semantics,  and behavior of a programming language, including its lexical  structure, grammar, type system, execution model, and standard  libraries, serving as the authoritative reference for implementers and 
developers.
> 

Linguistic abstractions are programming concepts that provide a high-level way to represent and manipulate data or behavior. Here are some of the linguistic abstractions in Python:

- **Functions**: Functions are a way to encapsulate reusable code and can be used to implement algorithms and behavior. They take input arguments and can return output values.
- **Classes**: Classes are a way to define custom types that can have attributes and methods. Classes support encapsulation and abstraction, making it possible to create complex data structures and behaviors.
- **Modules**: Modules are a way to organize Python code into reusable libraries that can be imported and used in other programs. They provide a high-level way to encapsulate functionality and promote code reuse.
- **Iterators**: Iterators provide a way to iterate over a sequence of data, such as a list or a file. They can be used to implement lazy evaluation and support the processing of large datasets.
- **Generators**: Generators are a type of iterator that allows lazy evaluation of data. They are useful for generating infinite or large sequences of data without requiring all of the data to be generated at once.
- **Decorators**: Decorators are a way to modify the behavior of functions or classes. They provide a high-level way to add functionality to existing code without modifying the original code.
- **Context** managers: Context managers are used to manage resources, such as files or network connections. They provide a high-level way to ensure that resources are properly allocated and released, even in the presence of exceptions.
- **Exceptions**: Exceptions are used to handle errors and exceptional conditions in Python code. They provide a high-level way to handle errors and gracefully handle failures.

QA:

- How to `tokenize` a python file?
- How to serialize the `ast tree` in **python**?
- Are there syntactic ambiguities in the Language?

## Lexical Structure

> **Lexical structure**: Defines how characters combine into **tokens** (identifiers, keywords, literals) and handles **whitespace, comments, and delimiters**.
> 

> **Default**: Python 3 source code is UTF-8 by default (PEP 3120).
> 

> **Encoding Declaration**: Optional header (e.g., # -*- coding: latin-1 -*-) for non-UTF-8 files.
> 

> **Operator Ambiguity**: `x:=1` (walrus) vs `x: int` (type hint).
> 

> **Implicit String Concatenation**:  `"hello" "world"  # → "helloworld" (at compile time)`.
> 

Guiding Questions:

- [Token Space] How are tokens (keywords, identifiers, literals) defined?
- What characters are allowed in identifiers (e.g., Unicode, sigils like `$`)?
- Does the language use significant whitespace (e.g., Python) or explicit delimiters (e.g., C)?

### Token

| **Category** | **Subcategory** | **Definition** | **Examples** | **Rules/Notes** |
| --- | --- | --- | --- | --- |
| **Keywords** | — | Reserved words with fixed syntax roles. | `if`, `else`, `for`, `while`, `def`, `class` | Case-sensitive. Full list: `import keyword; keyword.kwlist`. |
| **Identifiers** | — | Names for variables/functions/classes. | `x`, `calculate_total`, `_private_var` | Regex: `[_a-zA-Z][_a-zA-Z0-9]*`. Cannot be a keyword. |
| **Literals** | **Integer** | Whole numbers (base 10/2/8/16). | `42`, `0b1010`, `0o52`, `0x2F` | Arbitrary precision. Underscores allowed: `1_000_000`. |
|  | **Float** | Decimal or scientific notation. | `3.14`, `1e-5`, `6.022e23` | Underscores allowed: `1_000.000_1`. |
|  | **String** | Text in single/double/triple quotes. | `"hello"`, `'''multiline'''`, `r"raw"`, `f"{x}"` | Escape chars: `\\n`, `\\t`. Prefixes: `r` (raw), `f` (f-string), `b` (bytes). |
|  | **Boolean** | Logical values. | `True`, `False` | Subclass of `int` (`True == 1`). |
|  | **None** | Singleton for "no value". | `None` | Used as default return value. |
| **Operators** | **Arithmetic** | Math operations. | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `**` = exponentiation, `//` = floor division. |
|  | **Comparison** | Value comparisons. | `==`, `!=`, `<`, `>`, `<=`, `>=` | Chaining allowed: `1 < x <= 10`. |
|  | **Logical** | Boolean logic. | `and`, `or`, `not` | Short-circuit evaluation. |
|  | **Assignment** | Variable assignment. | `=`, `+=`, `-=`, `:=` (walrus) | `:=` introduced in Python 3.8 (PEP 572). |
|  | **Bitwise** | Binary bit manipulations. | `&`, `\|`, `^`, `~`, `<<`, `>>` | `^` = XOR, `~` = NOT. |
|  | **Membership** | Container membership tests. | `in`, `not in` | Used with iterables (lists, strings, etc.). |
|  | **Identity** | Object memory checks. | `is`, `is not` | Compares memory addresses (`id(obj)`). |
| **Delimiters** | **Brackets** | Grouping/collection syntax. | `()`, `[]`, `{}` | `{}` also used for dictionaries/sets. |
|  | **Punctuation** | Syntax separators. | `:`, `,`, `.`, `;`, `@` | `:` for blocks/lambdas, `@` for decorators. |
| **Whitespace** | **Indentation** | Tabs/spaces for block structure. |  (space), `\\t` (tab) | Must be consistent (error if mixed). Converted to `INDENT`/`DEDENT` tokens. |
|  | **Newlines** | Line endings. | `\\n`, `\\r\\n` | Terminates statements (unless `\\` or parentheses used). |
| **Special Tokens** | **Comments** | Ignored text. | `# This is a comment` | Excluded during execution. |
|  | **Docstrings** | Multi-line documentation strings. | `"""This is a docstring"""` | Stored in `__doc__` attribute. |

## Grammar

> **Grammar**:  Specifies the **rules** for constructing valid statements/expressions from tokens, typically defined via **BNF** or **context-free grammars**.
> 

> Python’s grammar is **context-free but indentation-sensitive**, making it unique among mainstream programming languages. The move to **PEG parsing** in Python 3.9+ improves flexibility and expressiveness.
> 

Guiding Questions:

- What class of formal grammar best describes the grammar of this language? (Note: This may include grammars within or outside the Chomsky hierarchy.)  Parsing Expression Grammar (PEG)
- Are there syntactic ambiguities in the Language? Yes Many.

## Syntactical Structure

> aka. Syntax Form.
> 

> **Syntactical Construct**: A **language feature** (e.g., loops, functions, conditionals) defined by the grammar, forming the structure of valid programs.
> 

> **Note:** `@` denotes a decorator. Python has many built-in decorators.
> 

> **Magic Method:**  Special method (dunder) for operator overloading or hooks.
> 

Guiding Questions:

- What are the core language constructs (variables, functions, control flow)?
- *Does the Language Supports Macro Constructs?*
- What *statement forms* exist (e.g., loops, conditionals, jumps)?
- What *expression forms* are supported (e.g., arithmetic, lambdas, comprehensions)?
- How are *operator precedence* and *associativity* formally defined?
- How is the `@classmethod` decorator implemented in Python's internals (e.g., CPython)? Which part of the interpreter handles its semantics?

Python includes several built-in decorators, such as:

1. `@staticmethod` – Defines a static method in a class.
2. `@classmethod` – Defines a class method.
3. `@property` – Allows defining getter/setter methods for class attributes.
4. `@functools.lru_cache` – Memoization decorator for caching function results.

| **Category** | **Syntax Construct** | **Example** | **Description** |
| --- | --- | --- | --- |
| **Variables** | Assignment (`=`) | `x = 10` | Binds a value to a name. |
|  | Unpacking | `a, *b = [1, 2, 3]` | Extended iterable unpacking. |
|  | Type hints | `name: str = "Alice"` | Variable type annotation. |
| **Literals** | Numeric | `42`, `3.14`, `1j` | Integers, floats, complex. |
|  | Strings | `"hello"`, `r"\\n"`, `f"{x}"` | Raw, f-strings, bytes. |
|  | Collections | `[1, 2]`, `{"a": 1}`, `{1, 2}`, `(1,)` | Lists, dicts, sets, tuples. |
| **Operators** | Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**`, `@` | Math operations. |
|  | Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` | Value comparisons. |
|  | Logical | `and`, `or`, `not` | Boolean logic. |
|  | Bitwise | `&`, `\|`, `^`, `~`, `<<`, `>>` | Binary operations. |
|  | Membership | `in`, `not in` | Iterable containment. |
|  | Identity | `is`, `is not` | Object identity checks. |
|  | Walrus (`:=`) | `if (n := len(x)) > 10: ...` | Assignment in expressions. |
|  | Call `()` | `print("Hello")` | Invokes a callable. |
|  | Dot `.` | `obj.attr` | Accesses object attributes. |
|  | Index `[]` | `lst[0]`, `dict["key"]` | Accesses sequences/mappings. |
|  | Slice `:` | `lst[1:3]`, `[::-1]` | Extracts subsequences. |
|  | Ellipsis `...` | `arr[..., 0]` (NumPy) | Advanced slicing. |
| **Control Flow** | `if`/`elif`/`else` | `python<br>if x > 0:<br>    print("+")` | Conditional branching. |
|  | `for` loop | `for x in range(5): ...` | Iteration. |
|  | `while` loop | `while x < 10: x += 1` | Conditional looping. |
|  | `break`/`continue` | `python<br>for x in lst:<br>    if x == 0:<br>        break` | Loop control. |
|  | `match`/`case`  | `python<br>match x:<br>    case 1:<br>        print("One")` | Pattern matching (3.10+). |
| **Functions** | `def` | `python<br>def f(x):<br>    return x * 2` | Function definition. |
|  | `lambda` | `lambda x: x + 1` | Anonymous function. |
|  | `*args`/`**kwargs` | `python<br>def f(*args, **kwargs):<br>    pass` | Variadic arguments. |
|  | `yield` | `python<br>def gen():<br>    yield 1` | Generator function. |
|  | Keyword-only (`*`) |  |  |
|  | Positional-only (`/`) |  |  |
| **Classes** | `class` | `python<br>class C:<br>    pass` | Class definition. |
|  | Inheritance | `python<br>class D(C):<br>    pass` | Subclassing. |
|  | Decorators | `python<br>@decorator<br>def f():<br>    pass` | Function/class modifiers. |
|  | `@property` |  |  |
|  | `@classmethod` |  |  |
|  | `@staticmethod` |  |  |
|  | `__slots__` |  |  |
| **Error Handling** | `try`/`except`/`finally` | `python<br>try:<br>    1/0<br>except:<br>    print("Error")` | Exception handling. |
|  | `raise` | `raise ValueError("Invalid")` | Throws exceptions. |
|  | `raise from` |  |  |
|  | `assert` |  |  |
| **Context Managers** | `with` | `python<br>with open("file.txt") as f:<br>    data = f.read()` | Resource management. |
|  | `@contextmanager` |  |  |
| **Imports & Modules** | `import` | `import os` | Module imports. |
|  | `from ... import` | `from sys import exit` | Selective imports. |
|  | `__import__()` |  |  |
| **Coroutines** | `async`/`await` | `python<br>async def f():<br>    await coro()` | Asynchronous functions. |
| **Special Syntax** | `pass` | `python<br>def f():<br>    pass` | Null operation. |
|  | `del` | `del x` | Reference deletion. |
|  | `nonlocal` | `python<br>def outer():<br>    x = 1<br>    def inner():<br>        nonlocal x` | Enclosing scope var. |
|  | `@` | Decorator |  |
|  | `@` | It performs matrix multiplication (a.k.a. dot product for 2D arrays).  It’s syntactic sugar for calling the special method **matmul**(). |  |
| **Metaprogramming** | `eval()`/`exec()` |  |  |
|  | `globals()`/`locals()` |  |  |
|  | `__annotations__` |  |  |

## Binding

> **Binding**: Associates **names** (variables, functions) with **memory locations, values, or behaviors**, either at compile-time or runtime.
> 

> **Mutability:  Mutability** refers to the ability of an object or variable to be modified after it is created or assigned a value.
> 

Guiding Questions:

- How are *values bound to names* (e.g., `let` in Rust, `=` in Python)?
- Which binding semantics does the language provides (mutable binding, inmutable binding)
- What categories of values and identifiable constructs does the language support?

### Identifiable Constructs

| **Identifier Type** | **Description** |
| --- | --- |
| **Variable** | A named reference to a value that can store data of any type. Python variables are dynamically typed. Example: `count = 5` |
| **Function** | A reusable block of code defined with `def` that performs a specific task. May accept parameters and return values. Example: `def greet(name): return f"Hello {name}"` |
| **Class** | A blueprint for creating objects that encapsulates data (attributes) and behavior (methods). Example: `class Car: pass` |
| **Decorator** | A design pattern that allows modifying or extending the behavior of functions/methods using the `@` syntax. Example: `@property` |
| **Module** | A Python file containing reusable code (functions, classes, variables) that can be imported. Example: `math.py` |
| **Attribute** | A value or method associated with an object or class. Can be data attributes or method attributes. Example: `obj.name` or `Class.method` |
| **Package** | A collection of related modules organized in a directory hierarchy (must contain `__init__.py`). Example: `numpy` |
| **Method** | A function that is defined inside a class and is associated with class instances (or the class itself). Example: `def bark(self): print("Woof!")` |
| **Exception** | A special object that represents an error condition, used for error handling. Example: `ValueError`, `try/except` blocks |
| **Generator** | A special kind of iterator defined using `yield` that generates values on-the-fly. Example: `(x**2 for x in range(10))` |

### Binding Type

> **Binding Type** refers to the method by which a variable or identifier is associated with a value, address, or resource, determining its scope, lifetime, and mutability in a program.
> 

| **Binding Type** | **Description** | **Supported?** |
| --- | --- | --- |
| **Static Binding** | The association between a name and a value is fixed at compile time and does not change at runtime. | ❌ (Mostly) |
| **Dynamic Binding** | The association between a name and a value is resolved at runtime. | ✅ (Fully) |
| **Lexical Binding** | A variable’s binding is determined by the scope in which it is defined. | ✅ (Closures) |
| **Global Binding** | Variables are bound globally and accessible across the entire program. | ✅ |
| **Local Binding** | Variables are bound within a specific function or block of code. | ✅ |

## Scoping Rules

> **Note:** Visibility and scoping rules are synonymous.
> 

> **Visibility**: **Visibility** refers to the scope or access control of an identifier (such as a variable, function, or class) within a program, determining where and how it can be referenced or modified, often enforced by rules such as access modifiers or name resolution mechanisms.
> 

> **Scoping Rules**: Determine **where and when** a binding is accessible (e.g., `block scope`, `function scope`, `global scope`).
> 

Guiding Questions:

- What is the *scope* of a name (lexical vs. dynamic, block vs. function)?
- How are shadowing, closures, and hoisting handled?
- Which are the  visibility rules associated with a binding?

## How to tokenize a python file?

```c
from tokenize import tokenize
from io import BytesIO

# Example Python code as a string
code = """
def hello():
    print("Hello, World!")

hello()
"""

# Tokenize the code
tokens = tokenize(BytesIO(code.encode('utf-8')).readline)

# Print tokens
for token in tokens:
    print(token)
```

## How to serialize the `ast tree` in **python**?

> 

```c
import ast

# Sample Python code
code = """
def greet(name):
    return f"Hello, {name}!"
"""

# Parse the code into an AST
```

## Are there syntactic ambiguities in the Language?

> 
- The walrus operator (`:=`) introduced in Python 3.8 can lead to ambiguity in complex expressions.
- Decorators look like function calls but are not executed immediately.

### Which are the semantics of the [] operator in python?

| **Use Case** | **Description** | **Instance(s)** |
| --- | --- | --- |
| Access by index | Get element at position | `lst[2]` |
| Negative indexing | Count from the end | `lst[-1]` |
| Slicing | Extract subsequence | `lst[1:4]` |
| Assignment | Set element value (if mutable) | `lst[0] = 99` |
| Dictionary key access | Access dict value by key | `d['key']` |
| Custom object indexing | `__getitem__` override | `obj[5]` |
| Multidimensional indexing | Index tuples, matrices | `arr[1,2]` |
| Boolean masking | Filter elements by boolean condition | `arr[[True, False]]` |

## References

- [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md)
- https://docs.python.org/3/reference/lexical_analysis.html#literals
- https://github.com/python/cpython/blob/main/Lib/token.py
- https://github.com/python/cpython/blob/main/Grammar/Tokens
- [Formal Language](https://app.notion.com/p/Formal-Language-195c0f5171ec8012bf0fd0530a135871?pvs=21)