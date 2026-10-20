# PHP: Metaprogramming

> An "X: Metaprogramming Model" describes the framework or approach for writing programs that manipulate, generate, or transform other programs or themselves as data.
> 

Questions:

- What is the language’s metaprogramming paradigm?
- What constructs are available at compile-time?
- What runtime reflection capabilities exist?
- How is reflection implemented?
- How are type errors reported in metaprograms?
- What are the costs of metaprogramming?
- How does the language prevent abusive metaprogramming?
- How are metaprograms debugged?

## Mechanism

| **Mechanism** | **Description** |
| --- | --- |
| **Reflection API** | Allows introspection of classes, interfaces, functions, methods, properties, parameters, and extensions at runtime. Provides objects like `ReflectionClass`, `ReflectionMethod`, `ReflectionProperty`, etc., to inspect metadata. |
| **Dynamic Invocation** | Reflection can **dynamically invoke methods** (`invoke`, `invokeArgs`) and construct objects (`newInstance`, `newInstanceArgs`) without knowing them at compile time. |
| **Annotation / DocComment Parsing** | Through `ReflectionClass::getDocComment()` (and similar), developers can parse structured metadata (annotations, attributes, docblocks) and use it for metaprogramming (e.g., dependency injection, ORM mappings). |
| **Attributes (PHP 8+)** | Native structured metadata attached to classes, methods, properties, and functions. Retrieved via reflection (`getAttributes()`), enabling cleaner metaprogramming compared to raw docblocks. |
| **Dynamic Property & Method Handling** | Magic methods like `__get`, `__set`, `__call`, and `__callStatic` provide runtime interception of access/invocation, a metaprogramming mechanism complementary to reflection. |
| **Closure Rebinding (`Closure::bind`)** | Allows changing the scope (`$this` and visibility) of a closure at runtime, enabling manipulation of private/protected members dynamically. |
| **Runtime Code Evaluation (`eval`)** | Executes dynamically generated PHP code at runtime. Powerful but unsafe if misused. Considered a low-level metaprogramming tool. |
| **Dynamic Class/Interface/Function Existence Checks** | `class_exists`, `method_exists`, `property_exists`, `function_exists` allow reflection-like runtime adaptation without full Reflection API. |
| **Debug & Type Introspection Functions** | Functions like `get_class`, `get_class_methods`, `get_parent_class`, `gettype`, `is_subclass_of` provide lightweight reflection. |

## Instrumentation Subsystem

| **Mechanism** | **Description** |
| --- | --- |
| **Error/Exception Hooks** | PHP provides global error/exception handlers (`set_error_handler`, `set_exception_handler`) that let you instrument how errors/exceptions are reported or logged. |
| **Function Hooks (Extensions)** | Extensions like **Xdebug** or **uopz** can intercept function calls, manipulate return values, or redefine functions at runtime. |
| **Tracing & Profiling APIs** | Xdebug, Tideways, and Blackfire provide tracing hooks for function entry/exit, stack traces, memory use, and execution times → core instrumentation for profiling. |
| **Stream Wrappers** | Custom stream wrappers (`stream_wrapper_register`) let you instrument I/O operations (file, HTTP, sockets) to monitor or log activity. |
| **Output Buffering** | With `ob_start` callbacks you can instrument output generation and capture/modify HTML before it is sent. |
| **Opcode Handlers (Zend Engine Hooks)** | At the C-extension level, the Zend Engine exposes hooks to observe or manipulate opcodes during execution. This is how profilers and debuggers instrument PHP internally. |
| **Reflection + Attributes** | While not “instrumentation” in the strict sense, reflection + attributes let you inject behavior based on metadata, e.g., logging every time a method with `#[Loggable]` is called. |
| **Superglobals and Tick Handling** | Superglobals (`$_SERVER`, etc.) can be monitored, and `declare(ticks=N)` with `register_tick_function` can instrument code execution at certain tick intervals. |

## References

- [Metaprogramming](note.html?n=technica/computation/language-system/conceptual-model-language-system/metaprogramming.md)
- https://www.blackfire.io/php/
- https://tideways.com/
- https://github.com/krakjoe/uopz
- https://github.com/perftools/xhgui