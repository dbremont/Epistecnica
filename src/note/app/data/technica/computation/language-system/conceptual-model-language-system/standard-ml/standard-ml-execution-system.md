# Standard ML: ⚙️ Execution System

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

## Runtime System

> 

## Execution Model

> The **execution model** of a programming language describes **how programs are carried out by the runtime system or computing platform**. It specifies the mechanisms by which code is translated into actions, including how instructions are executed, how memory and modules are managed, how concurrency is handled, and how the runtime interacts with the operating system and hardware.
> 

## **Evaluation Model**

> The **evaluation model** of a programming language describes **how expressions and computations are evaluated to produce values**, including the order of evaluation, handling of side effects, argument passing, recursion, and optimizations applied during computation.
> 

## Memory System

> The **memory system** of a programming language or runtime defines **how a program allocates, organizes, accesses, and reclaims memory during execution**. It governs the storage of variables, objects, data structures, code, and execution contexts, and ensures correctness, efficiency, and safety in memory use.
> 

## References

- [Linker](note.html?n=technica/computation/language-system/conceptual-model-language-system/linker.md)
- [Loader](note.html?n=technica/computation/language-system/conceptual-model-language-system/loader.md).
- [Evaluation Model](note.html?n=technica/computation/language-system/conceptual-model-language-system/evaluation-model.md)
- [Memory  Management](note.html?n=technica/computation/language-system/conceptual-model-language-system/memory-management.md)
- [Runtime Representation](note.html?n=technica/computation/language-system/conceptual-model-language-system/runtime-representation.md)
- [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md)