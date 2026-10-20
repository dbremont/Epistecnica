# C++: 📜 Language Specification

> A **language specification** formally defines the syntax, semantics,  and behavior of a programming language, including its lexical  structure, grammar, type system, execution model, and standard  libraries, serving as the authoritative reference for implementers and 
developers.
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

## Grammar

> In this note, *grammar* refers collectively to both **lexical** and **syntactic grammar**: lexical grammar defines how source characters form tokens, while syntactic grammar defines how those tokens combine into valid language constructs.
> 

> A **literal** is a **notation for representing a fixed value directly in the source code**. It’s the actual value written in the code, not a variable or an expression that computes a value.
> 

> The **C++ Preprocessor** is a critical part of the C++ compilation process, responsible for transforming the source code before actual compilation begins. It handles tasks such as macro substitution, file inclusion, conditional compilation, and more.
> 

> Table: Element Category (Lexical,  Syntactical).
> 

Guiding Questions:

- [Token Space] How are tokens (keywords, identifiers, literals) defined?
- What characters are allowed in identifiers (e.g., Unicode, sigils like `$`)?
- Does the language use significant whitespace (e.g., Python) or explicit delimiters (e.g., C)?
- *Does the Language Supports Macro Constructs?*
- Which are the modifiers (const, …) used  the Language?
- What are the core language constructs (variables, functions, control flow)?
- *Does the Language Support Macro Constructs?*
- What *statement forms* exist (e.g., loops, conditionals, jumps)?
- What *expression forms* are supported (e.g., arithmetic, lambdas, comprehensions)?
- How are *operator precedence* and *associativity* formally defined?
- What kinds of ‘Architectural Form’  (Module System) does it offers?
- Does the **language** provides supports for annotations?
- To what extent is the language expression-based versus statement-based?
- What is the **literal default type**? - C++: **🏷️** Type System

| Element Category | Element Type | Grammar Element Name | Form | Description | Semantics (Meaning) |
| --- | --- | --- | --- | --- | --- |
| Lexical | Character Set | Source Character Set | `UTF-8`, Unicode code points | Character repertoire accepted by the source file. | Defines valid source characters. |
| Lexical | Character | Whitespace | `\\t` `\\n` | Separates tokens. | Token delimiter. |
| Lexical | Character | Line Terminator | `\\n` | Marks line boundary. | Ends source line / preprocessing line. |
| Lexical | Comment | Line Comment | `// ...` | Single-line comment. | Ignored by compiler. |
| Lexical | Comment | Block Comment | `/* ... */` | Multi-line comment. | Ignored by compiler. |
| Lexical | Token | Identifier | `myVar` | User-defined symbolic name. | Refers to declared entity. |
| Lexical | Token | Keyword | `if`, `return`, `class` | Reserved word. | Has fixed grammatical meaning. |
| Lexical | Token | Operator Token | `+`, `-`, `=` | Operator symbol. | Performs built-in or overloaded operation. |
| Lexical | Token | Alternative Operator Token | `and`, `or`, `not` | Keyword operator spelling. | Equivalent operator representation. |
| Lexical | Token | Punctuator | `;`, `::`, `{}`, `()` | Structural punctuation. | Separates or groups syntax. |
| Lexical | Token | Digraph | `<%`, `%>`, `<:` | Alternative punctuator spelling. | Alternate lexical representation. |
| Lexical | Token | Literal | `42`, `"abc"` | Value written directly in source. | Produces constant expression value. |
| Lexical | Literal | Integer Literal | `42`, `0x2A` | Whole number constant. | Integer value. |
| Lexical | Literal | Floating Literal | `3.14`, `1e-8` | Floating constant. | Floating-point value. |
| Lexical | Literal | Character Literal | `'a'` | Character constant. | Character code unit value. |
| Lexical | Literal | String Literal | `"hello"` | Character sequence literal. | String object / array literal. |
| Lexical | Literal | Raw String Literal | `R"(text)"` | String without escape processing. | Literal text sequence. |
| Lexical | Literal | Boolean Literal | `true`, `false` | Boolean constant. | Truth value. |
| Lexical | Literal | Null Pointer Literal | `nullptr` | Null pointer token. | Null pointer value. |
| Lexical | Literal | User-defined Literal | `42_km` | Literal with custom suffix. | Calls literal operator. |
| Lexical | Literal | Wide Character Literal | `L'a'` | Wide character literal. | Wide character value. |
| Lexical | Literal | UTF Character Literal | `u'a'`, `U'a'` | Unicode character literal. | Unicode code point value. |
| Lexical | Literal | Wide String Literal | `L"text"` | Wide string literal. | Wide character sequence. |
| Lexical | Literal | UTF String Literal | `u8"text"` | Unicode string literal. | Encoded Unicode string. |
| Lexical | Literal | Numeric Suffix | `42u`, `3.0f` | Type suffix on numeric literal. | Adjusts literal type. |
| Lexical | Escape Sequence | Escape Sequence | `\\n`, `\\t`, `\\\\` | Encoded special character. | Inserts non-printable/special character. |
| Lexical | Unicode | Universal Character Name | `\\u03C0` | Unicode escape notation. | Represents Unicode code point. |
| Lexical | Preprocessing | Preprocessing Token | `pp-number`, identifier | Token recognized before parsing. | Input to preprocessor. |
| Lexical | Preprocessing | Preprocessor Directive | `#include` | Preprocessing instruction. | Executed before compilation. |
| Lexical | Preprocessing | Macro Definition | `#define X` | Macro declaration. | Token substitution rule. |
| Lexical | Preprocessing | Conditional Directive | `#if`, `#ifdef` | Conditional preprocessing. | Includes/excludes source. |
| Lexical | Preprocessing | Undef Directive | `#undef` | Removes macro. | Cancels macro expansion. |
| Lexical | Preprocessing | Pragma Directive | `#pragma` | Compiler directive. | Compiler-specific instruction. |
| Lexical | Preprocessing | Header Name | `<vector>` | Include target. | Names included translation dependency. |
| Syntactic | Declaration | Variable Declaration | `int x;` | Declares object. | Introduces storage-bound name. |
| Syntactic | Declaration | Function Declaration | `void f();` | Declares callable signature. | Introduces callable entity. |
| Syntactic | Declaration | Function Definition | `void f(){}` | Defines function body. | Supplies executable implementation. |
| Syntactic | Declaration | Class Declaration | `class X {};` | Defines class type. | Introduces class type. |
| Syntactic | Declaration | Struct Declaration | `struct X {};` | Defines struct type. | Introduces aggregate/class type. |
| Syntactic | Declaration | Enum Declaration | `enum Color {};` | Defines enumeration. | Introduces finite named constants. |
| Syntactic | Declaration | Namespace Declaration | `namespace N {}` | Declares namespace scope. | Creates named scope. |
| Syntactic | Declaration | Alias Declaration | `using T = int;` | Declares alias. | Introduces alternate name. |
| Syntactic | Declaration | Typedef Declaration | `typedef int T;` | Legacy alias declaration. | Alternate type name. |
| Syntactic | Declaration | Template Declaration | `template<typename T>` | Generic declaration. | Parameterized entity definition. |
| Syntactic | Declaration | Using Declaration | `using std::cout;` | Imports declaration into scope. | Makes name directly visible. |
| Syntactic | Declaration | Using Directive | `using namespace std;` | Imports namespace members. | Makes namespace scope available. |
| Syntactic | Declaration | Friend Declaration | `friend class X;` | Friend relationship declaration. | Grants access privileges. |
| Syntactic | Declaration | Linkage Specification | `extern "C"` | Declares language linkage. | Alters symbol linkage convention. |
| Syntactic | Declaration | Static Assert Declaration | `static_assert(x);` | Compile-time assertion. | Validates program during compilation. |
| Syntactic | Declaration | Constructor Declaration | `X();` | Constructor declaration. | Defines initialization entry point. |
| Syntactic | Declaration | Destructor Declaration | `~X();` | Destructor declaration. | Defines destruction behavior. |
| Syntactic | Specifier | Type Qualifier | `const`, `volatile` | Type modifier. | Constrains type usage. |
| Syntactic | Specifier | Storage Class Specifier | `static`, `extern` | Storage declaration modifier. | Defines duration/linkage properties. |
| Syntactic | Specifier | Function Specifier | `inline`, `virtual` | Function modifier. | Changes function declaration behavior. |
| Syntactic | Specifier | Constant Evaluation Specifier | `constexpr` | Compile-time evaluation specifier. | Enables constant evaluation. |
| Syntactic | Specifier | Access Specifier | `public`, `private` | Member visibility label. | Restricts member accessibility. |
| Syntactic | Specifier | Exception Specification | `noexcept` | Exception declaration. | States throw contract. |
| Syntactic | Specifier | Attribute | `[[nodiscard]]` | Metadata annotation. | Compiler hint / annotation. |
| Syntactic | Statement | Expression Statement | `x++;` | Statement containing expression. | Evaluates expression. |
| Syntactic | Statement | Compound Statement | `{ ... }` | Statement block. | Groups statements into scope. |
| Syntactic | Statement | Selection Statement | `if`, `switch` | Conditional branching. | Chooses execution path. |
| Syntactic | Statement | Iteration Statement | `for`, `while`, `do` | Looping construct. | Repeats execution. |
| Syntactic | Statement | Range-based For Statement | `for(auto x : xs)` | Range iteration. | Iterates sequence elements. |
| Syntactic | Statement | Jump Statement | `break`, `return`, `continue`, `goto` | Explicit control transfer. | Redirects execution flow. |
| Syntactic | Statement | Declaration Statement | `int x = 0;` | Declaration used as statement. | Introduces entity during execution. |
| Syntactic | Statement | Try Statement | `try {}` | Exception handling block. | Handles thrown exceptions. |
| Syntactic | Statement | Labeled Statement | `label:` | Statement label. | Jump target. |
| Syntactic | Statement | Case Statement | `case 1:` | Switch case label. | Matches switch branch. |
| Syntactic | Statement | Default Statement | `default:` | Default switch branch. | Fallback switch branch. |
| Syntactic | Statement | Null Statement | `;` | Empty statement. | No operation. |
| Syntactic | Expression | Primary Expression | `x`, `42`, `(x)` | Smallest expression form. | Produces value/reference. |
| Syntactic | Expression | Unary Expression | `!x`, `++x` | Single-operand expression. | Applies unary operation. |
| Syntactic | Expression | Binary Expression | `a+b` | Two-operand expression. | Combines operands. |
| Syntactic | Expression | Assignment Expression | `x = y` | Assignment expression. | Stores value. |
| Syntactic | Expression | Conditional Expression | `a ? b : c` | Ternary expression. | Selects one of two values. |
| Syntactic | Expression | Call Expression | `f(x)` | Function invocation. | Calls callable entity. |
| Syntactic | Expression | Member Access Expression | `obj.x`, `ptr->x` | Member access. | Refers to subobject/member. |
| Syntactic | Expression | Subscript Expression | `a[i]` | Indexed access. | Selects indexed element. |
| Syntactic | Expression | Cast Expression | `static_cast<T>(x)` | Explicit conversion. | Converts value form/type. |
| Syntactic | Expression | Lambda Expression | `[&](int x){}` | Anonymous function expression. | Produces callable closure object. |
| Syntactic | Expression | Fold Expression | `(args + ...)` | Variadic fold reduction. | Expands parameter pack. |
| Syntactic | Expression | `sizeof` Expression | `sizeof(T)` | Size query expression. | Produces object/type size. |
| Syntactic | Expression | `alignof` Expression | `alignof(T)` | Alignment query. | Produces alignment requirement. |
| Syntactic | Expression | `typeid` Expression | `typeid(x)` | RTTI query. | Produces runtime type info. |
| Syntactic | Expression | `noexcept` Expression | `noexcept(expr)` | Exception property query. | Evaluates throwability. |
| Syntactic | Expression | `new` Expression | `new T` | Dynamic allocation expression. | Allocates object storage. |
| Syntactic | Expression | `delete` Expression | `delete ptr` | Dynamic deallocation expression. | Releases allocated storage. |
| Syntactic | Expression | Throw Expression | `throw x` | Exception expression. | Throws exception object. |
| Syntactic | Expression | Comma Expression | `a, b` | Sequential expression. | Evaluates left then right. |
| Syntactic | Expression | Requires Expression | `requires(...)` | Constraint expression. | Forms compile-time requirement. |
| Syntactic | Initializer | Default Initialization | `T x;` | No explicit initializer. | Initializes using default rules. |
| Syntactic | Initializer | Copy Initialization | `T x = y;` | Assignment-form initialization. | Initializes from expression. |
| Syntactic | Initializer | Direct Initialization | `T x(y)` | Constructor-style initialization. | Direct initialization syntax. |
| Syntactic | Initializer | List Initialization | `T x{1,2}` | Brace initialization. | Initializes via initializer list. |
| Syntactic | Initializer | Aggregate Initialization | `Point{1,2}` | Aggregate member initialization. | Initializes aggregate members. |
| Syntactic | Initializer | Designated Initializer | `{ .x = 1 }` | Named field initializer. | Initializes specific members. |
| Syntactic | Initializer | Member Initializer List | `: x(1)` | Constructor initializer list. | Initializes base/member subobjects. |
| Syntactic | Structural Form | Parameter List | `(int x)` | Function parameter sequence. | Declares accepted parameters. |
| Syntactic | Structural Form | Argument List | `(x, y)` | Function call arguments. | Supplies invocation operands. |
| Syntactic | Structural Form | Template Parameter List | `<typename T>` | Template parameter declaration list. | Declares template parameters. |
| Syntactic | Structural Form | Template Argument List | `<int>` | Template argument list. | Supplies template arguments. |
| Syntactic | Structural Form | Capture List | `[&x]` | Lambda capture specification. | Captures enclosing variables. |
| Syntactic | Structural Form | Base-Clause | `: public Base` | Inheritance clause. | Declares base classes. |
| Syntactic | Structural Form | Qualified Name | `std::vector` | Scope-qualified identifier. | Refers to scoped entity. |
| Syntactic | Structural Form | Nested Name Specifier | `std::` | Scope prefix. | Resolves namespace/class scope. |
| Syntactic | Structural Form | Enumerator List | `{ Red, Green }` | Enum member sequence. | Defines enumeration constants. |
| Syntactic | Structural Form | Declarator | `*ptr`, `&ref` | Declared entity form. | Shapes declared type/name. |
| Syntactic | Structural Form | Init-Declarator | `x = 42` | Declarator with initializer. | Declares and initializes entity. |
| Syntactic | Structural Form | Requires Clause | `requires Integral<T>` | Template constraint clause. | Restricts template participation. |
| Syntactic | Architectural Form | Translation Unit | `.cpp` file | Unit compiled by compiler. | Compilation boundary. |
| Syntactic | Architectural Form | Header Unit | `.hpp`, `.h` | Shared declaration unit. | Included declaration source. |
| Syntactic | Architectural Form | Module | `export module X;` | Named module boundary. | Modular compilation/interface boundary. |
| Syntactic | Specifier | Attribute Argument Clause | `[[deprecated("use X")]]` | Optional attribute argument list. | Parameterizes attribute behavior. |
| Syntactic | Specifier | Alignment Specifier | `alignas(16)` | Alignment declaration specifier. | Requests storage alignment constraint. |
| Lexical | Preprocessing | Include Directive | `#include <vector>` | Includes source/header file. | Inserts translation dependency textually. |
| Lexical | Preprocessing | Define Directive | `#define X 1` | Macro definition directive. | Defines token substitution rule. |
| Lexical | Preprocessing | If Directive | `#if expr` | Conditional compilation directive. | Includes source if condition evaluates true. |
| Lexical | Preprocessing | Ifdef Directive | `#ifdef X` | Conditional macro existence test. | Includes source if macro exists. |
| Lexical | Preprocessing | Ifndef Directive | `#ifndef X` | Conditional negated macro existence test. | Includes source if macro absent. |
| Lexical | Preprocessing | Elif Directive | `#elif expr` | Alternative conditional branch. | Continues preprocessing selection chain. |
| Lexical | Preprocessing | Else Directive | `#else` | Fallback conditional branch. | Selects default preprocessing branch. |
| Lexical | Preprocessing | Endif Directive | `#endif` | Ends preprocessing condition block. | Terminates conditional preprocessing region. |
| Lexical | Preprocessing | Error Directive | `#error "msg"` | Emits preprocessing error. | Forces compilation failure. |
| Lexical | Preprocessing | Line Directive | `#line 42` | Alters reported line/file metadata. | Adjusts diagnostic source mapping. |
| Lexical | Preprocessing | Null Directive | `#` | Empty directive. | Has no effect. |
| Lexical | Preprocessing | Import Directive | `import std;` | Module import directive. | Imports module interface unit. |
| Syntactic | Declarator Modifier | Pointer Declarator | `*p` | Pointer declarator suffix/prefix. | Declares pointer type. |
| Syntactic | Declarator Modifier | Reference Declarator | `&x` | Lvalue reference declarator. | Declares reference alias. |
| Syntactic | Declarator Modifier | Rvalue Reference Declarator | `&&x` | Rvalue reference declarator. | Binds movable/temporary value. |
| Syntactic | Declarator Modifier | Array Declarator | `x[10]` | Array declarator. | Declares array object. |
| Syntactic | Declarator Modifier | Function Declarator | `f(int)` | Callable declarator. | Declares function signature. |
| Syntactic | Declarator Modifier | Pointer-to-member Declarator | `T C::*` | Member pointer declarator. | Refers to member via class instance. |
| Syntactic | Declarator Modifier | CV Qualifier Sequence | `const volatile` | Qualifier sequence. | Refines type mutability/access semantics. |
| Syntactic | Specifier | `mutable` Specifier | `mutable int x;` | Member mutability specifier. | Allows modification inside const object. |
| Syntactic | Specifier | `explicit` Specifier | `explicit X(int)` | Constructor/conversion specifier. | Prevents implicit conversion. |
| Syntactic | Specifier | `consteval` Specifier | `consteval` | Immediate function specifier. | Requires compile-time evaluation. |
| Syntactic | Specifier | `constinit` Specifier | `constinit` | Static initialization specifier. | Requires constant initialization. |
| Syntactic | Specifier | `thread_local` Specifier | `thread_local` | Thread storage specifier. | Declares per-thread storage duration. |
| Syntactic | Specifier | `register` Specifier | `register` | Legacy storage specifier. | Historical storage hint. |
| Syntactic | Specifier | `decltype` Specifier | `decltype(x)` | Type deduction specifier. | Produces type from expression. |
| Syntactic | Specifier | Elaborated Type Specifier | `class X` | Explicit type-category specifier. | Refers to previously declared type. |
| Syntactic | Expression | Parenthesized Expression | `(x + y)` | Grouped expression. | Controls precedence/evaluation grouping. |
| Syntactic | Expression | Postfix Expression | `x++`, `x--` | Postfix operator expression. | Evaluates then modifies operand. |
| Syntactic | Expression | Pointer-to-member Expression | `obj.*ptr`, `obj->*ptr` | Member pointer access. | Accesses member through pointer-to-member. |
| Syntactic | Expression | Functional Cast Expression | `T(x)` | Constructor-style conversion. | Converts or initializes value. |
| Syntactic | Expression | Braced Init Expression | `T{1}` | Brace-based expression initialization. | Constructs object using list initialization. |
| Syntactic | Expression | Pack Expansion | `args...` | Parameter pack expansion syntax. | Expands variadic template arguments. |
| Syntactic | Expression | Await Expression | `co_await expr` | Coroutine await expression. | Suspends coroutine pending result. |
| Syntactic | Expression | Yield Expression | `co_yield value` | Coroutine yield expression. | Produces coroutine output value. |
| Syntactic | Expression | Coroutine Return Expression | `co_return expr` | Coroutine return expression. | Terminates coroutine with result. |
| Syntactic | Statement | Coroutine Statement | `co_return` | Coroutine control statement. | Controls coroutine execution flow. |
| Syntactic | Exception Handling | Catch Handler | `catch(...)` | Exception handler clause. | Handles matching exception type. |
| Syntactic | Exception Handling | Function Try Block | `X() try {...}` | Try block attached to function. | Handles exceptions during initialization/body. |
| Syntactic | Template | Template-id | `vector<int>` | Named template specialization. | Refers to instantiated template entity. |
| Syntactic | Template | Type Template Parameter | `typename T` | Type parameter declaration. | Declares generic type placeholder. |
| Syntactic | Template | Non-type Template Parameter | `int N` | Constant parameter declaration. | Declares value parameter. |
| Syntactic | Template | Template Template Parameter | `template<class> class C` | Higher-order template parameter. | Declares template as argument. |
| Syntactic | Template | Constraint | `Integral<T>` | Named template requirement. | Restricts template substitution. |
| Syntactic | Class Member | Data Member Declaration | `int x;` | Member object declaration. | Introduces class state. |
| Syntactic | Class Member | Member Function Declaration | `void f();` | Member function declaration. | Introduces class behavior. |
| Syntactic | Class Member | Conversion Function | `operator bool()` | User-defined conversion member. | Converts object to target type. |
| Syntactic | Class Member | Operator Overload Declaration | `operator+` | Operator overload declaration. | Defines custom operator semantics. |
| Syntactic | Namespace | Namespace Alias | `namespace fs = std::filesystem;` | Namespace alias declaration. | Provides alternate namespace name. |
| Syntactic | Module | Module Declaration | `module;` | Module unit declaration. | Declares module compilation context. |
| Syntactic | Module | Export Declaration | `export` | Module export declaration. | Makes declaration visible outside module. |

| Element Category | Element Type | Grammar Element Name | Form | Description | Semantics (Meaning) |
| --- | --- | --- | --- | --- | --- |
| Lexical | Preprocessing | Include Directive | `#include <vector>` | Includes source/header file. | Inserts translation dependency textually. |
| Lexical | Preprocessing | Define Directive | `#define X 1` | Macro definition directive. | Defines token substitution rule. |
| Lexical | Preprocessing | If Directive | `#if expr` | Conditional compilation directive. | Includes source if condition evaluates true. |
| Lexical | Preprocessing | Ifdef Directive | `#ifdef X` | Conditional macro existence test. | Includes source if macro exists. |
| Lexical | Preprocessing | Ifndef Directive | `#ifndef X` | Conditional negated macro existence test. | Includes source if macro absent. |
| Lexical | Preprocessing | Elif Directive | `#elif expr` | Alternative conditional branch. | Continues preprocessing selection chain. |
| Lexical | Preprocessing | Else Directive | `#else` | Fallback conditional branch. | Selects default preprocessing branch. |
| Lexical | Preprocessing | Endif Directive | `#endif` | Ends preprocessing condition block. | Terminates conditional preprocessing region. |
| Lexical | Preprocessing | Error Directive | `#error "msg"` | Emits preprocessing error. | Forces compilation failure. |
| Lexical | Preprocessing | Line Directive | `#line 42` | Alters reported line/file metadata. | Adjusts diagnostic source mapping. |
| Lexical | Preprocessing | Null Directive | `#` | Empty directive. | Has no effect. |
| Lexical | Preprocessing | Import Directive | `import std;` | Module import directive. | Imports module interface unit. |
| Syntactic | Declarator Modifier | Pointer Declarator | `*p` | Pointer declarator suffix/prefix. | Declares pointer type. |
| Syntactic | Declarator Modifier | Reference Declarator | `&x` | Lvalue reference declarator. | Declares reference alias. |
| Syntactic | Declarator Modifier | Rvalue Reference Declarator | `&&x` | Rvalue reference declarator. | Binds movable/temporary value. |
| Syntactic | Declarator Modifier | Array Declarator | `x[10]` | Array declarator. | Declares array object. |
| Syntactic | Declarator Modifier | Function Declarator | `f(int)` | Callable declarator. | Declares function signature. |
| Syntactic | Declarator Modifier | Pointer-to-member Declarator | `T C::*` | Member pointer declarator. | Refers to member via class instance. |
| Syntactic | Declarator Modifier | CV Qualifier Sequence | `const volatile` | Qualifier sequence. | Refines type mutability/access semantics. |
| Syntactic | Specifier | `mutable` Specifier | `mutable int x;` | Member mutability specifier. | Allows modification inside const object. |
| Syntactic | Specifier | `explicit` Specifier | `explicit X(int)` | Constructor/conversion specifier. | Prevents implicit conversion. |
| Syntactic | Specifier | `consteval` Specifier | `consteval` | Immediate function specifier. | Requires compile-time evaluation. |
| Syntactic | Specifier | `constinit` Specifier | `constinit` | Static initialization specifier. | Requires constant initialization. |
| Syntactic | Specifier | `thread_local` Specifier | `thread_local` | Thread storage specifier. | Declares per-thread storage duration. |
| Syntactic | Specifier | `register` Specifier | `register` | Legacy storage specifier. | Historical storage hint. |
| Syntactic | Specifier | `decltype` Specifier | `decltype(x)` | Type deduction specifier. | Produces type from expression. |
| Syntactic | Specifier | Elaborated Type Specifier | `class X` | Explicit type-category specifier. | Refers to previously declared type. |
| Syntactic | Expression | Parenthesized Expression | `(x + y)` | Grouped expression. | Controls precedence/evaluation grouping. |
| Syntactic | Expression | Postfix Expression | `x++`, `x--` | Postfix operator expression. | Evaluates then modifies operand. |
| Syntactic | Expression | Pointer-to-member Expression | `obj.*ptr`, `obj->*ptr` | Member pointer access. | Accesses member through pointer-to-member. |
| Syntactic | Expression | Functional Cast Expression | `T(x)` | Constructor-style conversion. | Converts or initializes value. |
| Syntactic | Expression | Braced Init Expression | `T{1}` | Brace-based expression initialization. | Constructs object using list initialization. |
| Syntactic | Expression | Pack Expansion | `args...` | Parameter pack expansion syntax. | Expands variadic template arguments. |
| Syntactic | Expression | Await Expression | `co_await expr` | Coroutine await expression. | Suspends coroutine pending result. |
| Syntactic | Expression | Yield Expression | `co_yield value` | Coroutine yield expression. | Produces coroutine output value. |
| Syntactic | Expression | Coroutine Return Expression | `co_return expr` | Coroutine return expression. | Terminates coroutine with result. |
| Syntactic | Statement | Coroutine Statement | `co_return` | Coroutine control statement. | Controls coroutine execution flow. |
| Syntactic | Exception Handling | Catch Handler | `catch(...)` | Exception handler clause. | Handles matching exception type. |
| Syntactic | Exception Handling | Function Try Block | `X() try {...}` | Try block attached to function. | Handles exceptions during initialization/body. |
| Syntactic | Template | Template-id | `vector<int>` | Named template specialization. | Refers to instantiated template entity. |
| Syntactic | Template | Type Template Parameter | `typename T` | Type parameter declaration. | Declares generic type placeholder. |
| Syntactic | Template | Non-type Template Parameter | `int N` | Constant parameter declaration. | Declares value parameter. |
| Syntactic | Template | Template Template Parameter | `template<class> class C` | Higher-order template parameter. | Declares template as argument. |
| Syntactic | Template | Constraint | `Integral<T>` | Named template requirement. | Restricts template substitution. |
| Syntactic | Class Member | Data Member Declaration | `int x;` | Member object declaration. | Introduces class state. |
| Syntactic | Class Member | Member Function Declaration | `void f();` | Member function declaration. | Introduces class behavior. |
| Syntactic | Class Member | Conversion Function | `operator bool()` | User-defined conversion member. | Converts object to target type. |
| Syntactic | Class Member | Operator Overload Declaration | `operator+` | Operator overload declaration. | Defines custom operator semantics. |
| Syntactic | Namespace | Namespace Alias | `namespace fs = std::filesystem;` | Namespace alias declaration. | Provides alternate namespace name. |
| Syntactic | Module | Module Declaration | `module;` | Module unit declaration. | Declares module compilation context. |
| Syntactic | Module | Export Declaration | `export` | Module export declaration. | Makes declaration visible outside module. |

## Grammar Characterization

> aka. Linguistic Abstraction - Physical Manifestation of Computational Entity; *Computational Element.*
> 

> 📚 The **syntactic grammar defines how tokens are combined** into valid **expressions**, **statements**, **declarations**, and **programs**.
> 

Guiding Questions:

- What class of formal grammar best describes the grammar of this language? (Note: This may include grammars within or outside the Chomsky hierarchy.)

## Binding

> **Binding**: Associates **names** (variables, functions) with **memory locations, values, or behaviors**, either at compile-time or runtime.
> 

> **Mutability:  Mutability** refers to the ability of an object or variable to be modified after it is created or assigned a value.
> 

Guiding Questions:

- How are *values bound to names* (e.g., `let` in Rust, `=` in Python)?
- Which binding semantics does the language provides (mutable binding, inmutable binding)
- What categories of values and identifiable constructs does the language support?

### Identifiable Construct Set

| **Identifier Type** | **Syntax** | **Description** | **Case(s)** |
| --- | --- | --- | --- |
| **Variable Names** | `T varName` | Identifiers for variables that hold data. | `int age;` |
| **Function Names** | `T functionName()` | Identifiers for functions that perform actions or return values. | `int sum(int a, int b) { return a + b; }` |
| **Class Names** | `class ClassName` | Identifiers for classes that define object templates. | `class Person { int age; };` |
| **Type Names** | `typedef NewType` | Identifiers for user-defined types or aliases (typedef, `using`). | `typedef int Integer;` |
| **Namespace Names** | `namespace NamespaceName` | Identifiers for namespaces that organize code. | `namespace MyNamespace { int x; }` |
| **Template Parameters** | `template <typename T>` | Identifiers for template parameters that allow generic programming. | `template <typename T> T add(T a, T b) { return a + b; }` |
| **Enumerator Names** | `enum EnumName { ... }` | Identifiers for enumerated constants within an `enum` type. | `enum Color { Red, Green, Blue };` |
| **Constant Variable Names** | `const T varName` | Identifiers for constants whose values do not change. | `const int MAX_SIZE = 100;` |
| **Global Variable Names** | `T varName` | Identifiers for global variables that are accessible throughout the program. | `int globalVar;` |
| **Member Variable Names** | `T varName` inside class | Identifiers for variables that belong to a class or struct instance. | `class MyClass { int x; };` |
| **Member Function Names** | `T functionName()` | Identifiers for functions that belong to a class or struct. | `class MyClass { void foo() {}; };` |
| **Constructor/Destructor Names** | `ClassName()` | Identifiers for class constructors and destructors. | `MyClass::MyClass() {}` |
| **Operator Overload Names** | `operator op` | Identifiers for operators that are overloaded to work with custom types. | `class Complex { Complex operator+(const Complex& c) {}; };` |
| **Lambda Expression Names** | `[]() { ... }` | Anonymous function identifiers used in lambdas. | `auto add = [](int a, int b) { return a + b; };` |
| **Type Aliases** | `using NewType = OldType` | Identifiers for creating aliases for existing types. | `using IntPtr = int*;`
Binding |

### Binding Model Type

> **Binding Type** refers to the method by which a variable or identifier is associated with a value, address, or resource, determining its scope, lifetime, and mutability in a program.
> 

| **Binding Type** | **Description** | **Note(s)** |
| --- | --- | --- |
| **Static Binding (Early Binding)** | Binding occurs at compile time. | Examples: non-virtual function calls, overload resolution, template instantiation, type checking. |
| **Dynamic Binding (Late Binding)** | Binding occurs at runtime. | Virtual function dispatch via vtables; dynamic linking; `dynamic_cast`, RTTI. |
| **Lexical Binding (Static Scoping)** | Names are resolved according to the lexical structure of the program. | C++ uses lexical scoping: variable refers to nearest enclosing scope. |
| **Dynamic Scoping** | Names resolved along the call chain at runtime (not lexical scopes). | **Not used in C++**; occurs in Lisp, shell languages. |
| **Global Binding** | Names bound in the global namespace with program-wide visibility. | Global variables, global functions, namespace-level symbols. |
| **Local Binding** | Names bound within functions or blocks. | Automatic variables; block-scope bindings (`for`, `{}` blocks). |
| **Type Binding** | Association of a name with a type. | All type declarations; `auto` deduction; `typedef`, `using`. |
| **Storage Binding** | Binding between a name and a storage location. | Storage classes: automatic, static, dynamic (`new`), thread-local. |
| **Lifetime Binding** | Association between an object and how long it exists. | RAII objects, static objects, heap objects (`new/delete`). |
| **Value Binding** | Binding a name to a value. | Initialization, assignment, constant expressions, lambda captures by value. |
| **Reference Binding** | Binding a reference to an object. | `T&` and `const T&`; temporary lifetime extension; forwarding references. |
| **Name Binding / Identifier Binding** | Binding a name to its declaration. | Resolving scopes, namespaces, overload sets. |
| **Overload Binding (Overload Resolution)** | Choosing the correct overloaded entity based on argument types. | All function/operator overload selection at compile time. |
| **Template Binding (Instantiation Binding)** | Binding template parameters to concrete arguments. | Template instantiation during compile-time substitution. |
| **Link-Time Binding** | Binding external references across translation units. | Static linking and dynamic linking of symbols. |
| **Namespace Binding** | Binding names inside or across namespaces. | `std::vector`, ADL (Argument-Dependent Lookup). |
| **Capture Binding (Lambda Capture)** | Binding variables into a lambda by value or reference. | `[]`, `[&]`, `[=]`, `[x, &y]`, capture of `this`. |
| **Parameter Binding** | Binding function parameters to supplied arguments. | Function calls; default argument binding; virtual dispatch chooses dynamic override. |

### Reference Model Type

How do we refer(bindings) to computational objects?

- Reference,
- Value

| **Reference Type** | **Syntax** | **Binds to** | **Modifiable** | **Use Case** |
| --- | --- | --- | --- | --- |
| **Lvalue Reference** | `T&` | Lvalues (objects with a persistent address) | Yes | Allows modifying the original object. |
| **Const Lvalue Reference** | `const T&` | Lvalues (objects with a persistent address) | No | Useful for passing objects without copying and ensuring immutability. |
| **Rvalue Reference** | `T&&` | Rvalues (temporary objects) | Yes (enables move semantics) | Enables move semantics and efficient resource transfer. |
| **Const Rvalue Reference** | `const T&&` | Rvalues (temporary objects) | No | Used to extend the lifetime of temporary objects without modifying them. |
| **Reference to Pointer** | `T*&`, `const T*&`, `T*&&` | Pointers (objects pointing to memory) | Yes (for pointer modification) | Allows modifying the pointer itself, not just the object it points to. |

### Scoping Rule Set

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

- [Names](https://doc.rust-lang.org/reference/names.html)
- [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md)
- [Program Element Modifier](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-element-modifier.md)
- https://en.cppreference.com/w/cpp/language/identifiers