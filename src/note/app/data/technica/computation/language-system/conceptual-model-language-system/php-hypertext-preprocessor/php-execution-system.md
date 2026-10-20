# PHP: 🚀 Execution System

> A **Language Execution System (LES)** is the set of tools, algorithms, and runtime mechanisms that **execute a program** represented by a given **encoding scheme** (e.g., source code, bytecode, machine code). It defines how a program's **semantics** are realized on a computational substrate (hardware, VM, or interpreter) through a series of **transformations** and **runtime behaviors**.
> 

Guiding Questions:

- Execution Model
    - Does execution involve interpretation, compilation (AOT/JIT), or hybrid approaches?
    - Are there intermediate representations (e.g., bytecode, IR, AST transformations)?
    - How are modules or dependencies resolved and loaded?
    - **How does the language handle concurrency and parallelism?** (e.g., threads, coroutines, message passing, shared memory)
    - **How are execution environments isolated or shared?** (e.g., VM sandboxes, process models, containerization)
    - **What debugging and profiling capabilities does the execution model provide?** (e.g., stack traces, instrumentation hooks, profiling APIs)
    - **How does the runtime handle program termination and cleanup?** (e.g., exit codes, finalizers, destructors)
- **Evaluation Model**
    - **What evaluation strategy does the language use?** (e.g., eager, lazy, speculative execution)
    - **How are expressions evaluated in different contexts?** (e.g., function calls, conditional branches, loops)
    - **Does the language support memoization or caching of evaluations?** How is it implemented?
    - **How are side effects managed and controlled during evaluation?** (e.g., referential transparency, transactional memory, effect systems)
    - How does the language handle short-circuiting and speculative execution?
    - **What optimizations does the evaluation model enable?** (e.g., constant folding, loop unrolling, dead code elimination)
    - **How are recursive and higher-order function evaluations managed?** (e.g., call stack growth, tail call optimization, trampolining)
    - What call semantics does the language provides?
    - **What are the rules for function calls and argument passing?** (e.g., pass-by-value, pass-by-reference, copy-on-write, closures)
- Runtime Services:
    - What mechanisms manage memory (GC, manual, borrow checking)?
    - Is GC generational, reference-counted, or region-based?
    - **What components of the runtime system contribute to execution?** (e.g., virtual machine, native execution, interpreter loop, OS-level support)
    - How are **system calls** or external resources (I/O, threads) integrated?
    - Is there a **runtime scheduler** (e.g., for coroutines, async/await)?
    - **What memory model does the language enforce?** (e.g., stack allocation, heap management, reference counting)
- Semantics
    - **What formal or informal semantic model describes the language's execution?** (e.g., operational, axiomatic, denotational semantics)
    - **How does the language define and enforce correctness?** (e.g., static type checking, contracts, runtime assertions)
    - **What are the rules for function calls and argument passing?** (e.g., pass-by-value, pass-by-reference, copy-on-write, closures)
    - **What memory model does the language enforce?** (e.g., stack allocation, heap management, reference counting)
    - **How does the language handle undefined behavior or execution anomalies?** (e.g., segmentation faults, runtime errors, exception handling)
    - **What guarantees does the language provide regarding execution determinism or non-determinism?**
    - **What constraints exist on execution order, and how does this affect parallel computation?**
- **Control Flow**:
    - How are loops, recursion, and **tail calls** handled? Are they optimized?
    - Does the language support **non-local exits** (e.g., exceptions, continuations)?
- Runtime Representation (Encoding of Data, State, and Computation)
    - **How are language-level constructs (e.g., objects, functions, closures) represented in memory?**
    - **How are primitive data types encoded at the binary level?** (e.g., alignment, endianness, type tagging)
    - **How does the runtime manage heap and stack memory?** (e.g., garbage collection, allocation strategies, frame layout)
    - **How are function calls represented at runtime?** (e.g., stack frames, activation records, calling conventions)
    - **How does the runtime encode computational states?** (e.g., registers, memory-mapped variables, interpreter state machines)
        - **How does the language support serialization and deserialization of runtime structures?**
- **How is referential integrity maintained in complex data structures?** (e.g., pointer tracking, reference counting, garbage collection algorithms)
    - What are the trade-offs between different runtime representations for performance, safety, and portability?
- **Data Layout**:
    - How are primitive types (integers, floats) and composite types (structs, objects) encoded?
    - Are types **boxed** or **unboxed**? How is **memory alignment** handled?
- **Type Erasure vs. Reification**:
    - Does the runtime retain type information (e.g., Java generics vs. C++ templates)?
    - How is **reflection** or dynamic type inspection supported?
- **Serialization**:
    - What formats are used for persistence/networking (e.g., Python’s `pickle`, JSON)?
    - How is **memory shared** across threads (e.g., atomic operations, immutability)?
- **Optimizations**
    - **Inlining/Caching**: Are function calls or computations memoized (e.g., React’s `useMemo`)?
    - **JIT Tricks**: Does the runtime specialize hot code paths (e.g., LuaJIT trace compilation)?

## Execution Model: …

> The **execution model** of PHP defines how source code is **parsed, compiled, and executed** within the **Zend Engine** runtime. PHP follows a compiled**–execute** cycle at runtime, rather than ahead-of-time compilation.
> 

| **Stage** | **Description** |
| --- | --- |
| **Lexing / Parsing** | PHP source code is tokenized and parsed into an **Abstract Syntax Tree (AST)** by the PHP parser. |
| **Compilation** | The AST is compiled into **Zend opcodes** (intermediate instructions), which represent low-level operations for the Zend Engine virtual machine. |
| **Execution** | The Zend VM executes opcodes sequentially, managing **function calls, memory, symbol tables, and runtime errors**. |
| **Memory Management** | Uses a **reference-counting garbage collector** with cycle detection to free unused variables and objects. |
| **Error Handling** | Execution may raise **notices, warnings, or fatal errors** depending on the error type and configuration. |
| **Extensions / Hooks** | Execution can be extended or intercepted using **PHP extensions, stream wrappers, reflection, and instrumentation hooks**. |

## **Evaluation Model**

> The **evaluation model** of PHP specifies **how expressions and statements are interpreted and reduced to values or effects** during execution. It defines the **rules of evaluation order, type conversion, and scope resolution** that govern program behavior.
> 

| **Aspect** | **Description** |
| --- | --- |
| **Expression Evaluation** | PHP evaluates expressions in a **left-to-right order** (with operator precedence/associativity rules). Intermediate results are stored in temporary variables (zvals). |
| **Typing** | PHP uses **dynamic typing**: variable types are determined at runtime. Automatic **type juggling** occurs during evaluation (e.g., string to int in arithmetic). |
| **Scoping & Binding** | Variable resolution follows **function scope, class scope, and global scope**, with lexical binding rules (except for `$this`, late static binding, closures). |
| **Function / Method Calls** | Arguments are evaluated **before the call** (call-by-value by default, unless references `&` are explicitly declared). |
| **Control Structures** | Conditionals and loops evaluate boolean expressions with PHP’s **truthiness rules** (`0`, `""`, `null`, `[]` → false). |
| **Errors & Exceptions** | Invalid evaluations may yield **notices/warnings**, or throw **exceptions** (e.g., division by zero, type errors in strict mode). |
| **Reflection & Eval** | The runtime allows **meta-evaluation** through `eval()`, reflection APIs, and dynamic function construction. |

## Memory System

> The **memory system** in PHP defines how variables, objects, and resources are represented, allocated, shared, and freed at runtime by the Zend Engine.
> 

| **Component** | **Description** |
| --- | --- |
| **zval Container** | Every PHP variable is stored in a **`zval` structure**, containing the value, type, and reference count. |
| **Reference Counting** | Memory is managed via **reference counting**: each `zval` tracks how many variables reference it. When the count drops to zero, the value is freed. |
| **Copy-on-Write** | PHP implements **copy-on-write (COW)** for efficiency: variables share memory until one is modified, at which point a copy is created. |
| **Garbage Collector (GC)** | Introduced in PHP 5.3, the GC detects and frees **cyclic references** (e.g., objects referencing each other). |
| **Symbol Table** | Variable names map to `zval` pointers stored in **symbol tables** (per scope). |
| **Memory Manager** | The Zend Memory Manager sits on top of the C heap, optimizing allocation with custom **arena allocators** and caching. |
| **Resource Management** | Special types (e.g., file handles, sockets, streams) are tracked by a **resource manager** with reference counting. |
| **Opcache** | In PHP 5.5+, Opcache caches compiled opcodes in shared memory to reduce parsing and compilation overhead across requests. |

## References

- [Linker](note.html?n=technica/computation/language-system/conceptual-model-language-system/linker.md)
- [Loader](note.html?n=technica/computation/language-system/conceptual-model-language-system/loader.md).
- [Evaluation Model](note.html?n=technica/computation/language-system/conceptual-model-language-system/evaluation-model.md)
- [Memory  Management](note.html?n=technica/computation/language-system/conceptual-model-language-system/memory-management.md)
- [Runtime Representation](note.html?n=technica/computation/language-system/conceptual-model-language-system/runtime-representation.md)
- [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md)
-