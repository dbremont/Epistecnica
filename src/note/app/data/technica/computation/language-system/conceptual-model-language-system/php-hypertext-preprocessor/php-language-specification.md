# PHP: 📜 Language Specification

> A **language specification** formally defines the syntax, semantics,  and behavior of a programming language, including its lexical  structure, grammar, type system, execution model, and standard  libraries, serving as the authoritative reference for implementers and 
developers.
> 

## Lexical Grammar

> aka. Lexical Structure.
> 

> 🔤 **Lexical grammar defines the *tokens***—the smallest meaningful units in the source code.
> 

> **Lexical structure**: Defines how characters combine into **tokens** (identifiers, keywords, literals) and handles **whitespace, comments, and delimiters**.
> 

Guiding Questions:

- [Token Space] How are tokens (keywords, identifiers, literals) defined?
- What characters are allowed in identifiers (e.g., Unicode, sigils like `$`)?
- Does the language use significant whitespace (e.g., Python) or explicit delimiters (e.g., C)?
- What are the core language constructs (variables, functions, control flow)?
- *Does the Language Supports Macro Constructs?*

| **Lexical Component** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Tokens** | The smallest meaningful units of PHP source code produced by the lexer; include keywords, identifiers, literals, operators, and separators. | `if`, `$x`, `123`, `+`, `;` |
| **Keywords** | Reserved words with predefined meaning in the language grammar; cannot be used as identifiers. | `if`, `else`, `while`, `function`, `class`, `namespace`, `return`, `try`, `catch`, `match` |
| **Identifiers** | Names defined by the programmer for variables, functions, classes, constants, and namespaces. Begin with a letter or `_`, followed by letters, digits, or `_`. Case-sensitive (except class names). | `$var`, `_temp`, `myFunction`, `UserClass` |
| **Literals** | Fixed values directly represented in code: integers, floats, strings, booleans, null. | `42`, `3.14`, `'hello'`, `"world"`, `true`, `false`, `null` |
| **Operators** | Symbols denoting computations or operations on operands: arithmetic, logical, comparison, assignment, concatenation, etc. | `+`, `-`, `*`, `/`, `==`, `===`, `&&`, ` |
| **Separators** | Punctuation symbols structuring statements and expressions. | `;`, `,`, `.`, `:`, `?`, `::`, `->`, `=>`, `()`, `{}`, `[]` |
| **Comments** | Non-executable annotations ignored by the compiler/interpreter. | `// single-line`, `# single-line`, `/* multi-line */` |
| **White Space** | Space, tab, newline used to separate tokens; generally ignored except in strings and heredoc/nowdoc contexts. | `" "`, `\t`, `\n` |
| **Escape Sequences** | Special backslash-prefixed codes used inside double-quoted strings and heredocs. | `\n` (newline), `\t` (tab), `\\` (backslash), `\"` (quote), `\$` (literal dollar), `\u{XXXX}` (Unicode codepoint) |
| **Unicode Characters** | PHP strings (since PHP 7) support UTF-8 encoding by default; Unicode code points can be represented via escape sequences. | `"ñ"`, `"こんにちは"`, `"\u{1F600}"` (😀) |

## **Syntactic** Grammar

> aka. The Grammar.
> 

> 📚 The **syntactic grammar defines how tokens are combined** into valid **expressions**, **statements**, **declarations**, and **programs**.
> 

Guiding Questions:

- What class of formal grammar best describes the grammar of this language? (Note: This may include grammars within or outside the Chomsky hierarchy.)
- Are there syntactic ambiguities in the Language?
- What *statement forms* exist (e.g., loops, conditionals, jumps)?
- What *expression forms* are supported (e.g., arithmetic, lambdas, comprehensions)?
- How are *operator precedence* and *associativity* formally defined?

| **Category** | **Construct (Core Form)** | **Description** |
| --- | --- | --- |
| Script / file | `<?php ... ?>` | PHP code block / script entry. Short tags (`<?=`) allowed for echo. |
| Statements | `<expr>;` | Any expression or statement terminated by semicolon. |
| Blocks | `{ ... }` | Compound statement / scope used by functions, classes, control structures. |
| Expressions | *various* | Produce values (arithmetic, logical, function call, etc.). Can appear where values expected. |
| Variable | `$name` | Symbol referencing value. Dynamically typed, created on first use. |
| Constants | `define('NAME', value)` / `const NAME = value;` | Immutable values; `const` for compile-time and in classes. |
| Comments | `// ...`, `# ...`, `/* ... */` | Single-line and multi-line comments. |
| Whitespace | (space, tab, newline) | Insignificant except in strings and heredocs/nowdocs. |
| Identifiers | `[A-Za-z_\x80-\xff][A-Za-z0-9_\x80-\xff]*` | Names for variables, functions, classes, constants (case-insensitive for functions/constants historically). |
| Keywords (examples) | `if`, `else`, `function`, `class`, `return`, `use`, ... | Reserved words with special meaning in syntax. |
| Literals — integer/float/string | `123`, `3.14`, `'str'`, `"str"` | Literal values. Double-quoted strings support interpolation and escape sequences. |
| Heredoc / Nowdoc | `<<<ID\n...\nID;` / `<<<'ID'\n...\nID;` | Multi-line string literals (interpolated vs raw). |
| Array literal | `[1,2]` / `array(1,2)` | Array creation (short `[]` syntax since PHP 5.4). |
| Associative array | `['k' => 'v']` | Key → value mapping. |
| Object instantiation | `new ClassName($args)` | Create an object. |
| Static access | `ClassName::CONSTANT`, `ClassName::method()` | Access class constants/methods/properties statically. |
| Property access | `$obj->prop` / `$obj->method()` | Access instance properties and methods. |
| Method declaration | `function name($a, $b): Type { ... }` | Declares a method or function with optional return type. |
| Function declaration | `function fname($args) { ... }` | Global or within namespaces; supports type hints and variadics. |
| Anonymous function / closure | `function($x) use($y) { ... }` | Inline function; `use` imports outside variables by value or reference. |
| Arrow function | `fn($x) => $x * 2` | Short, implicit-return lambdas (capturing by value). |
| Parameters | `Type $name = default, ...` / `...$rest` | Typed parameters, default values, variadics, by-reference (`&$x`). |
| Return | `return $expr;` | Return a value (or no value). |
| Control — if | `if (cond) { ... } elseif (cond2) { ... } else { ... }` | Conditional branching. |
| Control — switch / match | `switch(expr) { case v: ... }` / `match(expr) => expr` | `switch` with fall-through; `match` (PHP 8+) is expression-like and strict. |
| Loops — for | `for ($i=0; $i<10; $i++) { ... }` | Classical C-style loop. |
| Loops — foreach | `foreach($arr as $k => $v) { ... }` | Iteration over arrays/iterables. |
| Loops — while / do-while | `while(cond) { ... }` / `do { ... } while(cond);` | Condition-checked and post-checked loops. |
| Exceptions | `try { ... } catch (Type $e) { ... } finally { ... }` | Exception handling; `finally` always executes. |
| Generators / yield | `function gen(){ yield $v; }` | Lazy iterators; `yield from` delegates. |
| Namespaces | `namespace Foo\Bar;` | Organize code; influences name resolution. |
| Use / aliasing | `use Foo\Bar as Baz;` | Import classes/functions/constants and create aliases. |
| Traits | `trait T { ... }` | Reusable method/property sets for classes; composed with `use`. |
| Interfaces | `interface I { public function m(); }` | Contract for classes; methods without implementation. |
| Class declaration | `class C extends P implements I { ... }` | Defines blueprint; supports inheritance and interfaces. |
| Visibility | `public`, `protected`, `private` | Member access control inside classes. |
| Static members | `static` | Class-level properties/methods shared across instances. |
| Type declarations | `int`, `string`, `ClassName`, `?Type`, `Type | Type` |
| Typed properties | `public int $x;` | Property type hints (PHP 7.4+). |
| Union / Intersection types | `int | float`/`A&B` |
| Attributes | `#[Attribute]` | Structured metadata on classes/functions/properties (PHP 8+). |
| Named arguments | `fn(a:1, b:2)` | Call-site argument names (PHP 8+). |
| Match expression | `match ($x) { 1 => 'one', default => 'other' }` | Expression that returns value; no fall-through, strict comparison. |
| Casting | `(int)$x`, `(string)$x` | Type cast operators. |
| Error / fatal | `Error`, `TypeError`, `ParseError` | Built-in error classes and exceptions for runtime/compile problems. |
| Magic methods | `__construct`, `__get`, `__set`, `__call`, `__toString`, ... | Special methods invoked by language behaviors. |
| Superglobals | `$_GET`, `$_POST`, `$_SERVER`, `$_SESSION`, `$_ENV`, `$_FILES`, `$_COOKIE` | Built-in global arrays with request/environment data. |
| File inclusion | `include 'file.php';`, `require_once 'file.php';` | Load/execute external PHP files; `require` halts on failure. |
| Namespaced functions/constants | `namespace\function()` / `const` | How functions/constants live under namespaces. |
| Docblocks / PHPDoc | `/** @param int $x */` | Structured comments for IDEs, static analyzers, and documentation. |

## Language Semantics

Guiding Questions

- **What formal or informal semantic model describes the language's execution?** (e.g., operational, axiomatic, denotational semantics)
- **How does the language define and enforce correctness?** (e.g., static type checking, contracts, runtime assertions)
- **What are the rules for function calls and argument passing?** (e.g., pass-by-value, pass-by-reference, copy-on-write, closures)
- **What memory model does the language enforce?** (e.g., stack allocation, heap management, reference counting)
- **How does the language handle undefined behavior or execution anomalies?** (e.g., segmentation faults, runtime errors, exception handling)
- **What guarantees does the language provide regarding execution determinism or non-determinism?**
- **What constraints exist on execution order, and how does this affect parallel computation?**

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

| Type | Description |
| --- | --- |
| **Variable Identifiers** | Begin with `$` followed by a valid name (`$var`, `$my_value`). Case-sensitive. |
| **Function Identifiers** | Names for user-defined or built-in functions (`myFunction()`). Case-insensitive when called, but case-sensitive when declared in modern practice. |
| **Class Identifiers** | Names for classes (`class User {}`), case-insensitive. |
| **Interface Identifiers** | Names for interfaces (`interface JsonSerializable {}`), define contracts. |
| **Trait Identifiers** | Names for traits (`trait Logger {}`), reusable sets of methods. |
| **Constant Identifiers** | Uppercase by convention; defined via `const NAME = value;` or `define("NAME", value)`. Case-sensitive by default (except old `define`). |
| **Namespace Identifiers** | Namespaces organize code (`namespace App\Services;`). Used to fully qualify identifiers. |
| **Label Identifiers** | Names used for `goto` labels (`start: ... goto start;`). Rarely used. |
| **Property Identifiers** | Names for object properties (`$this->property`), case-sensitive. |
| **Method Identifiers** | Names for class methods (`$obj->method()`), case-insensitive like functions. |
| **Parameter Identifiers** | Variable names in function/method signatures (`function foo($x) {}`). |
| **Static Variable Identifiers** | Special variables within function scope (`static $count = 0;`). |
| **Superglobals** | Special predefined variable identifiers (`$_GET`, `$_POST`, `$_SERVER`, etc.). Always available regardless of scope. |

### Binding Type

> **Binding Type** refers to the method by which a variable or identifier is associated with a value, address, or resource, determining its scope, lifetime, and mutability in a program.
> 

| Binding Type | Description |
| --- | --- |
| **Name Binding** | Association between an identifier (variable, function, class name) and its meaning (value, function body, type, etc.). In PHP, variables bind dynamically at runtime when first assigned. |
| **Type Binding** | Association of identifiers with a type. PHP is dynamically typed (late binding), but modern PHP supports explicit type declarations for parameters, return values, and properties (early binding enforced at runtime). |
| **Value Binding** | Association between a variable identifier and a stored value. In PHP, assignment is usually by value (copy-on-write), but objects are bound by reference semantics. |
| **Reference Binding** | Using `&`, variables can be bound to the same storage location, so modifying one modifies the other. |
| **Scope Binding** | Binding of names to visibility regions: local (function), global, static, class (properties/methods), namespace. Determines where an identifier is accessible. |
| **Lifetime Binding** | Binding of variables to memory duration: local variables exist during function execution; `static` variables persist across calls; global/superglobals persist during the request lifecycle. |
| **Object Binding** | Association of `$this` with the current instance inside methods. Defines context-sensitive behavior. |
| **Closure Binding** | Anonymous functions can capture variables from their surrounding scope using `use(...)`. By default captured by value, but can also bind by reference. |
| **Late Static Binding** | Inheritance-related binding that allows `static::` to refer to the class where the method is called (PHP 5.3+), not just where it was defined. |
| **Dynamic Property Binding** | Prior to PHP 8.2, properties could be added dynamically to objects at runtime (`$obj->newProp = 1`). From PHP 8.2, this is deprecated unless using `__get`/`__set`. |
| **Superglobal Binding** | Predefined arrays (`$_GET`, `$_POST`, etc.) are always bound in the global scope, available everywhere without declaration. |
| **File/Include Binding** | Files brought in via `include` / `require` bind their variables and function/class definitions into the caller’s scope at runtime. |

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

## References

- [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md)
- https://www.php.net/manual/en/langref.php