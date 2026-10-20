# Java: 📜 Language Specification

> A **language specification** formally defines the syntax, semantics,  and behavior of a programming language, including its lexical  structure, grammar, type system, execution model, and standard  libraries, serving as the authoritative reference for implementers and 
developers.
> 

> **Java linguistic abstractions** are the various constructs and language features, such as classes, interfaces, inheritance, and control structures, that allow developers to write and organize code at different levels of complexity and functionality, enabling clear, maintainable, and scalable software development.
> 

> A [*path*](https://doc.rust-lang.org/reference/paths.html) is a sequence of one or more path segments used to refer to an [entity](https://doc.rust-lang.org/reference/glossary.html#entity) in the current scope or other levels of a [namespace](https://doc.rust-lang.org/reference/glossary.html#namespace) hierarchy.
> 

> **Java closures** refer to the ability of a lambda expression or anonymous inner class to capture and utilize variables from its surrounding context, allowing those variables to be accessed even after their defining scope has ended.
> 

Guiding Questions:

- Lexical Structure
    - How are tokens (keywords, identifiers, literals) defined?
    - Are there context-sensitive or ambiguous syntactic rules?
    - What characters are allowed in identifiers (e.g., Unicode, sigils like `$`)?
    - Does the language use significant whitespace (e.g., Python) or explicit delimiters (e.g., C)?
- Grammar:
    - Is the grammar *context-free* (most languages) or context-sensitive (e.g., C’s typedef ambiguity)?
    - Are there syntactic ambiguities (e.g., JavaScript’s ASI, Rust’s turbofish `::<>`)?
    - Does the language distinguish them (e.g., Rust’s expression blocks) or unify them (e.g., Lisp)?
- Syntactical Constructs
    - What are the core language constructs (variables, functions, control flow)?
    - *Does the Language Supports Macro Constructs?*
    - What *statement forms* exist (e.g., loops, conditionals, jumps)?
    - What *expression forms* are supported (e.g., arithmetic, lambdas, comprehensions)?
    - How are *operator precedence* and *associativity* formally defined?
- Binding
    - How are *values bound to names* (e.g., `let` in Rust, `=` in Python)?
    - What categories of values and identifiable constructs does the language support?
- Scoping Rules
    - What is the *scope* of a name (lexical vs. dynamic, block vs. function)?
    - How are shadowing, closures, and hoisting handled?

## Lexical Structure

> **Lexical structure**: Defines how characters combine into **tokens** (identifiers, keywords, literals) and handles **whitespace, comments, and delimiters**.
> 

Guiding Questions:

- [Token Space] How are tokens (keywords, identifiers, literals) defined?
- What characters are allowed in identifiers (e.g., Unicode, sigils like `$`)?
- Does the language use significant whitespace (e.g., Python) or explicit delimiters (e.g., C)?

| **Lexical Component** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Tokens** | The smallest units of meaning in a Java program, including keywords, identifiers, literals, and symbols. | `int`, `public`, `class`, `+`, `=` |
| **Keywords** | Reserved words with predefined meanings in the Java language, used to define the structure and behavior of the code. | `if`, `else`, `for`, `while`, `return` |
| **Identifiers** | Names given to variables, methods, classes, and other entities in the program, following specific naming conventions. | `myVariable`, `calculateSum`, `Person` |
| **Literals** | Fixed values assigned to variables, including numeric, character, string, and boolean literals. | `42`, `'a'`, `"Hello"`, `true`, `3.14` |
| **Operators** | Symbols that perform operations on variables and values, including arithmetic, logical, and relational operators. | `+`, `-`, `*`, `/`, `&&`, `==`, `!` |
| **Separators** | Symbols used to separate tokens in the code, defining the structure of statements and expressions. | `;`, `,`, `()`, `{}`, `[]` |
| **Comments** | Non-executable text that provides explanations or notes within the code, ignored by the compiler. | `// single-line comment`, `/* multi-line comment */` |
| **White Space** | Spaces, tabs, and line breaks used to separate tokens and improve code readability, ignored by the compiler. |  (space), `\\t` (tab), `\\n` (new line) |
| **Escape Sequences** | Special characters that start with a backslash (`\\`) to represent characters that cannot be typed directly. | `\\n` (newline), `\\t` (tab), `\\"` (double quote) |
| **Unicode Characters** | Java source code can include Unicode characters, allowing for a wide range of international characters and symbols. | `\\u0041` (for 'A'), `\\u03B1` (for 'α') |

## Grammar

> **Grammar**:  Specifies the **rules** for constructing valid statements/expressions from tokens, typically defined via **BNF** or **context-free grammars**.
> 

Guiding Questions:

- What class of formal grammar best describes the grammar of this language? (Note: This may include grammars within or outside the Chomsky hierarchy.)
- Are there syntactic ambiguities in the Language?

## Syntactical Structure

> **Syntactical Construct (Syntatic Form)**: A **language feature** (e.g., loops, functions, conditionals) defined by the grammar, forming the structure of valid programs.
> 

> Literal:  In programming and computer science, a **literal** is a **notation for representing a fixed value directly in the source code**. It’s the actual value written in the code, not a variable or an expression that computes a value.
> 

> Note: This should be improved.
> 

Guiding Questions:

- What are the core language constructs (variables, functions, control flow)?
- *Does the Language Supports Macro Constructs?*
- What *statement forms* exist (e.g., loops, conditionals, jumps)?
- What *expression forms* are supported (e.g., arithmetic, lambdas, comprehensions)?
- How are *operator precedence* and *associativity* formally defined?

| Category | Construct (core form) | Description |
| --- | --- | --- |
| Primitive Type | `int x = 5;` | 32-bit signed two’s-complement integer. |
| Primitive Type | `double rate = 3.14;` | 64-bit IEEE-754 floating-point. |
| Primitive Type | `boolean flag = false;` | One-bit logical value (`true` or `false`). |
| Reference Type | `String s = "hello";` | Immutable sequence of UTF-16 code units. |
| Reference Type | `Point p = new Point(3, 4);` | Instance of a user-defined class. |
| Array | `int[] nums = {1, 2, 3};` | Homogeneous fixed-length container. |
| Variable | `final double PI = 3.14159;` | Named storage location that can be declared constant. |
| Literal | `0xCAFEBABE` | Hexadecimal integer literal. |
| Literal | `"text\\n"` | String literal supporting escape sequences. |
| Operator | `a + b` | Addition; also string concatenation. |
| Operator | `a && b` | Conditional-AND (short-circuit). |
| Control Flow | `if (cond) { … } else { … }` | Selective execution based on Boolean expression. |
| Control Flow | `for (init; test; update) { … }` | Count-controlled loop. |
| Control Flow | `while (cond) { … }` | Pre-test loop. |
| Control Flow | `do { … } while (cond);` | Post-test loop. |
| Control Flow | `switch (x) { case 1: … break; default: … }` | Multi-way branch (supports `String`, `enum`, primitives). |
| Control Flow | `break;` / `continue;` | Premature loop exit / skip to next iteration. |
| Control Flow | `return value;` | Exit method and optionally hand back a value. |
| Exception Handling | `try { … } catch (IOException e) { … } finally { … }` | Structured error management with guaranteed cleanup. |
| Exception Handling | `throw new IllegalArgumentException("bad arg");` | Explicitly raise an exception. |
| Exception Handling | `throws IOException` | Method-level declaration of checked exceptions. |
| Method | `int max(int a, int b) { … }` | Parameterized, optionally generic, executable member with return type. |
| Method | `static void main(String[] args)` | Program entry point. |
| Method | `varargs: void log(String msg, Object... objs)` | Accepts zero or more trailing arguments as an array. |
| Class | `public class Point { … }` | Blueprint for objects: fields, methods, constructors, initializers. |
| Object Creation | `new Point(2, 3)` | Heap allocation plus constructor invocation. |
| Constructor | `public Point(int x, int y) { this.x = x; this.y = y; }` | Special block run once per instantiation. |
| Field | `private final double mass;` | Per-instance state; may be constant or mutable. |
| Static Member | `public static int counter;` | One per class, shared by all instances. |
| Inheritance | `class ColoredPoint extends Point { … }` | Single inheritance of implementation. |
| Interface | `interface Drawable { void draw(Graphics g); }` | Pure type: abstract methods, `default`/`static` methods, constants. |
| Interface | `class Sprite implements Drawable, Movable { … }` | A class may implement multiple interfaces. |
| Record (Java 16+) | `record Range(int min, int max) { }` | Immutable transparent carrier for data. |
| Enum | `enum Day { MON, TUE, … }` | Type-safe finite set of constants; may have fields/methods. |
| Annotation | `@Override`, `@Deprecated`, custom `@interface` | Metadata attached to program elements. |
| Package | `package com.example.tools;` | Namespace and access-control boundary. |
| Import | `import java.util.*;` / `import static java.lang.Math.PI;` | Bring types or static members into scope. |
| Module (Java 9+) | `module com.foo.bar { requires java.base; exports com.api; }` | Explicit dependency & encapsulation unit above packages. |
| Generic | `class Box<T> { T value; }` | Parameterized type with compile-time type safety. |
| Wildcard | `List<? extends Number>` | Unknown subtype bound; read-only projection. |
| Lambda | `(x, y) -> x + y` | Inline implementation of a single-abstract-method interface (functional interface). |
| Method Reference | `String::length` | Shorthand for lambda: `s -> s.length()`. |
| Stream API | `list.stream().filter(p).map(f).collect(toList())` | Declarative bulk operations on sequences. |
| Try-with-resources | `try (BufferedReader br = Files.newBufferedReader(p)) { … }` | Automatic `close()` for `AutoCloseable` resources. |
| Assertion | `assert x > 0 : "x must be positive";` | Optional runtime check, disabled by default. |
| Synchronization | `synchronized (lock) { … }` | Intrinsic monitor lock for mutual exclusion. |
| Synchronization | `synchronized int getId() { … }` | Instance or static method-level locking. |
| Thread | `new Thread(task).start();` | Lightweight concurrent execution unit. |
| Var (Java 10+) | `var list = new ArrayList<String>();` | Local-variable type inference. |
| Text Block (Java 15) | `"""Hello, "world"!"""` | Multi-line string literal without most escapes. |
| Sealed Class (Java 17) | `sealed class Shape permits Circle, Rectangle { … }` | Restrict which classes may extend or implement. |

## Language Semantics

> See more in  [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md).
> 

Guiding Questions

- How are the syntactic constructs evaluated by the language’s execution model?
- How are *operator precedence* and *associativity* formally defined?
- **What formal or informal semantic model describes the language's execution?** (e.g., operational, axiomatic, denotational semantics)
- **How does the language define and enforce correctness?** (e.g., static type checking, contracts, runtime assertions)
- **What are the rules for function calls and argument passing?** (e.g., pass-by-value, pass-by-reference, copy-on-write, closures)
- **What memory model does the language enforce?** (e.g., stack allocation, heap management, reference counting)
- **How does the language handle undefined behavior or execution anomalies?** (e.g., segmentation faults, runtime errors, exception handling)
- **What guarantees does the language provide regarding execution determinism or non-determinism?**
- **What constraints exist on execution order, and how does this affect parallel computation?**
- Which are the **evaluation models** for the **linguistic expressions**? Which are the primitives operators? Take arithmetic,  boolean expressions,etc.  See Java: 📚 Standard Library.

| **Aspect** | **Type** | **Evaluation** |
| --- | --- | --- |

## Binding

> **Binding**: Associates **names** (variables, functions) with **memory locations, values, or behaviors**, either at compile-time or runtime.
> 

> **Mutability:  Mutability** refers to the ability of an object or variable to be modified after it is created or assigned a value.
> 

Guiding Questions:

- How are *values bound to names* (e.g., `let` in Rust, `=` in Python)?
- Which binding semantics does the language provides (mutable binding, inmutable binding)
- What categories of values and identifiable constructs does the language support?
- How do we refer(bindings) to computational objects?
    - Reference,
    - Value

### Identifiable Constructs

> Java Identifier Models define the naming conventions and rules for different types of identifiers in Java code, including variables, classes, methods, constants, packages, interfaces, enums, annotations, and local variables, ensuring clarity, consistency, and adherence to the language's syntax and semantic rules.
> 

| **Identifier Type** | **Naming Conventions** | **Rules** |
| --- | --- | --- |
| **Variable Names** | Camel case (e.g., `myVariable`, `totalAmount`) | Start with a letter, underscore (`_`), or dollar sign (`$`). Subsequent characters can be letters, digits, underscores, or dollar signs. It must not be a keyword. |
| **Class Names** | Pascal case (e.g., `MyClass`, `EmployeeRecord`) | Start with an uppercase letter. Subsequent words are capitalized. It must not be a keyword. |
| **Method Names** | Camel case (e.g., `calculateTotal`, `getUserName`) | Start with a lowercase letter. Subsequent words are capitalized. It must not be a keyword. |
| **Constant Names** | Uppercase with underscores (e.g., `MAX_VALUE`, `PI`) | All letters are uppercase. Underscores separate words. It must not be a keyword. |
| **Package Names** | Lowercase, usually with hierarchical structure (e.g., `com.example.app`) | Start with a lowercase letter. Hierarchical structure separated by dots. It must not be a keyword. |
| **Interface Names** | Pascal case (e.g., `Readable`, `Writable`) | Start with an uppercase letter. Subsequent words are capitalized. It must not be a keyword. |
| **Enum Names** | Pascal case (e.g., `Color`, `DayOfWeek`) | Start with an uppercase letter. Subsequent words are capitalized. It must not be a keyword. |
| **Annotation Names** | Pascal case (e.g., `Override`, `Entity`) | Start with an uppercase letter. Subsequent words are capitalized. It must not be a keyword. |
| **Local Variables** | Camel case (e.g., `count`, `tempValue`) | It is the same as variable names. It is limited to method or block scope and must not be a keyword. |

### Binding Type

> **Binding Type** refers to the method by which a variable or identifier is associated with a value, address, or resource, determining its scope, lifetime, and mutability in a program.
> 

> Java's variable binding models are central to its design, emphasizing safety, concurrency, and memory management.
> 

| **Binding Model** | **Description** |
| --- | --- |
| **Static Binding** | Also known as compile-time binding, method calls and variable references are resolved at compile time based on the reference type. |
| **Dynamic Binding** | This is also known as runtime binding, where method calls are resolved at runtime based on the actual object type, supporting polymorphism and method overriding. |
| **Variable Binding** | Refers to the association of variable names with their storage locations, where the binding occurs at compile time for local variables and runtime for instance variables. |
| **Method Binding** | Refers to the association of method calls with their implementations, which can be resolved at compile time (static) or runtime (dynamic). |
| **Class Binding** | Refers to the association of class names with their class definitions, established at compile time. |
| **Field Binding** | Refers to the association of field names with their corresponding data fields in a class, determined at compile time. |
| **Type Binding** | Refers to the association of type names with their type definitions, including primitive types and reference types, established at compile time. |
| **Scope Binding** | Refers to the association of names with their declarations within a specific scope, including block, method, or class level. |
| **Exception Binding** | This refers to the association of exception names with their exception classes and handlers, which allows for runtime resolution when exceptions are thrown. |

## Scoping Rules

> **Note:** Visibility and scoping rules are synonymous.
> 

> **Visibility**: **Visibility** refers to the scope or access control of an identifier (such as a variable, function, or class) within a program, determining where and how it can be referenced or modified, often enforced by rules such as access modifiers or name resolution mechanisms.
> 

> **Scoping Rules**: Determine **where and when** a binding is accessible (e.g., `block scope`, `function scope`, `global scope`).
> 

> The Java scoping model defines the visibility and lifetime of variables within different parts of a program, determining where variables can be accessed or modified based on their location in the code, such as within blocks, methods, classes, or packages.
> 

> Java uses a **lexical (or static) scoping model**, meaning that the scope of a variable is determined by its position within the source code. The visibility of variables is defined at compile-time, based on the block structure and nesting of the code, rather than being influenced by the runtime execution flow.
> 

Guiding Questions:

- What is the *scope* of a name (lexical vs. dynamic, block vs. function)?
- How are shadowing, closures, and hoisting handled?
- Which are the  visibility rules associated with a binding?

## How to tokenize a Java file?

> 
- Java Compiler API (Built-in)
- ANTLR with Java Grammar
- JavaParser

## Miscellanea

### Finally

In Java, the `finally` clause is designed to execute after a `try` block has completed its execution, regardless of whether an exception was thrown or not. It serves as a reliable place to put cleanup code, such as closing file streams or releasing other resources.

However, there are a few scenarios where the `finally` block may not execute:

1. **If the JVM exits prematurely**: If the Java Virtual Machine (JVM) exits while the `try` or `catch` block is executing, the `finally` block will not execute. This can happen if `System.exit()` is called or if the JVM crashes due to a severe error.
2. **If a thread running the `try` or `catch` block is killed or interrupted**: If the thread executing the `try` or `catch` block is killed or interrupted before it reaches the `finally` block, the `finally` block won't be executed.
3. **Uncaught exceptions in the `finally` block itself**: If an exception is thrown in the `finally` block and is not caught within the same `finally` block, it will propagate out of the block, potentially preventing further execution of the `finally` block.
4. **Infinite loops or blocking operations**: If there is an infinite loop or a blocking operation (like waiting for I/O that never completes) in the `try` or `catch` block, the `finally` block will not be reached.

## References

- [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md)
- [X: 📜 Language Specification](https://app.notion.com/p/X-Language-Specification-b37fd4f7c824484898c467ed1a48b8f2?pvs=21)