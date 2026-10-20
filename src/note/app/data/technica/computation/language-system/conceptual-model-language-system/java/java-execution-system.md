# Java: 🚀 Execution System

> A **Language Execution System (LES)** is the set of tools, algorithms, and runtime mechanisms that **execute a program** represented by a given **encoding scheme** (e.g., source code, bytecode, machine code). It defines how a program's **semantics** are realized on a computational substrate (hardware, VM, or interpreter) through a series of **transformations** and **runtime behaviors**.
> 

> **The Java Evaluation (Semantic)** Model defines how expressions and statements in a Java program are executed, specifying the order of operations, type-checking, and the runtime behavior of the code to produce the final output.
> 

> A **semantics** for a programming language is a model for the computational meaning
of a program written in that language.
> 

> A runtime is a software environment that provides the necessary services and libraries to execute and manage computer programs at runtime. It is the infrastructure that allows a program to run and interact with the underlying system, including hardware resources, operating system services, and other software components.
> 

> The Java Runtime System is a key part of the Java platform that manages the execution of Java applications. It includes several components and concepts essential for running Java programs efficiently.
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

## **Java Runtime Environment (JRE) Components**

| **Component** | **Description** | **Examples** |
| --- | --- | --- |
| **Java Virtual Machine (JVM)** | Executes Java bytecode and provides the runtime environment for Java applications. | JVM implementations: HotSpot, OpenJ9. |
| **Class Loader** | Loads Java classes into the JVM, including application, system, and user-defined classes. | Bootstrap Class Loader, Platform Class Loader, Application Class Loader. |
| **Bytecode Interpreter** | Executes Java bytecode instructions by translating them into machine code. | Part of the JVM that interprets the bytecode directly. |
| **Just-In-Time (JIT) Compiler** | Compiles bytecode into native machine code at runtime to improve performance. | HotSpot JIT Compiler, GraalVM JIT. |
| **Garbage Collector** | Manages memory by automatically reclaiming memory used by objects that are no longer reachable. | G1 GC, Parallel GC, CMS, ZGC. |
| **Runtime Libraries** | Provides standard Java API classes and methods used by Java applications. | java.lang, java.util, [java.io](http://java.io/), etc. |

## Execution Model: …

> 

## **Evaluation Model**

> 

| **Component** | **Description** | **Example** |
| --- | --- | --- |
| **Expression Evaluation** | Determines how expressions (e.g., arithmetic, logical, and relational) are evaluated according to operator precedence and associativity. | `3 + 5 * 2` evaluates to `13` (multiplication before addition) |
| **Type Checking** | Ensures that operations are performed on compatible data types, enforcing Java's strong typing system. | `int x = "string";` results in a compile-time error |
| **Type Conversion (Casting)** | Automatic or manual conversion of one data type to another, following specific rules for widening or narrowing conversions. | `double d = 10;` (automatic widening from `int` to `double`) |
| **Variable Resolution** | Determines how variable references are resolved, taking into account the scope and visibility of variables. | Resolving `x` to the nearest enclosing scope's `x` variable |
| **Method Invocation** | Specifies how methods are called and how arguments are passed, with Java using pass-by-value semantics. | `obj.method(param1, param2);` |
| **Operator Precedence** | Defines the order in which operators are applied in expressions, with higher-precedence operators evaluated before lower-precedence ones. | `a + b * c` (multiplication before addition) |
| **Short-Circuit Evaluation** | In logical expressions with `&&` and ` |  |
| **Block and Control Flow** | Defines how code blocks and control flow statements like `if`, `for`, `while`, and `switch` are executed. | `if (x > 0) { ... } else { ... }` |
| **Object Creation** | Handles the instantiation of objects and the initialization of their fields through constructors. | `new MyClass();` creates and initializes an object |
| **Exception Handling** | Manages the flow of execution when exceptions are thrown and caught using `try`, `catch`, and `finally` blocks. | `try { ... } catch (Exception e) { ... } finally { ... }` |
| **Garbage Collection** | Automatically reclaims memory by removing objects that are no longer referenced, ensuring efficient memory management. | Objects without references are collected by the JVM |
| **Thread Execution** | Defines how multiple threads are managed, including synchronization and communication between threads. | `synchronized` blocks ensure that only one thread executes a block at a time |

## Memory Model

> 

## Memory System

> 

| **Memory Area** | **Description** | **Examples** |
| --- | --- | --- |
| **Heap** | Memory area where objects are allocated and garbage collection occurs. | Used for dynamic memory allocation. |
| **Stack** | Memory area where method call frames are stored, including local variables and method parameters. | Each thread has its own stack. |
| **Method Area** | Stores class metadata, including class structures, method information, and static variables. | Part of the JVM’s memory model. |
| **Program Counter (PC) Register** | Tracks the address of the currently executing instruction in a thread. | Specific to each thread. |
| **Native Method Stack** | Used for native method calls made via JNI (Java Native Interface). | Stores native method frames. |

### Garbage Collection

> 

## References

- [Evaluation Model](note.html?n=technica/computation/language-system/conceptual-model-language-system/evaluation-model.md)
- [Memory  Management](note.html?n=technica/computation/language-system/conceptual-model-language-system/memory-management.md)
- [Runtime Representation](note.html?n=technica/computation/language-system/conceptual-model-language-system/runtime-representation.md)
- [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md)
- 
- Bruns, Daniel. "Formal Semantics for the Java Modeling Language." *Informatiktage*. 2010.
- https://shipilev.net/blog/2014/jmm-pragmatics/
- 
- [How do I find out what keystore my JVM is using?](https://stackoverflow.com/questions/8980364/how-do-i-find-out-what-keystore-my-jvm-is-using)
- [How do you import a .cer certificate into a Java keystore?](https://stackoverflow.com/questions/4325263/how-to-import-a-cer-certificate-into-a-java-keystore)
- [How do you check the certificate name and alias in keystore files?](https://stackoverflow.com/questions/12893995/how-to-check-certificate-name-and-alias-in-keystore-files)
- [KeyStore Explorer](http://keystore-explorer.org/)
- [Java Cryptography](https://jenkov.com/tutorials/java-cryptography/index.html)
- [Java and SSL certificates](https://stackoverflow.com/questions/7219989/java-and-ssl-certificates)
- [JAR Signing](https://introcs.cs.princeton.edu/java/85application/jar/sign.html)
- [Java SSL Debug Logging](https://stackoverflow.com/questions/23659564/limiting-java-ssl-debug-logging)
- [G1 GC Deep Dive](https://javaspecialists.teachable.com/courses/enrolled/301873)
- [Java - Is binary code the same as ByteCode?](https://stackoverflow.com/questions/4841083/java-is-binary-code-the-same-as-bytecode)
- …

> [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md),[Evaluation Model](note.html?n=technica/computation/language-system/conceptual-model-language-system/evaluation-model.md),[Memory  Management](note.html?n=technica/computation/language-system/conceptual-model-language-system/memory-management.md),[Runtime Representation](note.html?n=technica/computation/language-system/conceptual-model-language-system/runtime-representation.md),[Linker](note.html?n=technica/computation/language-system/conceptual-model-language-system/linker.md),[Loader](note.html?n=technica/computation/language-system/conceptual-model-language-system/loader.md)
> 

Guiding Questions:

- Execution Model
    - Does execution involve interpretation, compilation (AOT/JIT), or hybrid approaches?
    - Are there intermediate representations (e.g., bytecode, IR, AST transformations)?
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
- Code Resolution
    - How are modules or dependencies resolved and loaded?
    - 
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
    - **What are the trade-offs between different runtime representations for performance, safety, and portability?**
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