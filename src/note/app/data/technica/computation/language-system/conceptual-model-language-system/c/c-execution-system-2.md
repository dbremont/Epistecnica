# C++: 🚀 Execution System

> A **Language Execution System (LES)** is the set of tools, algorithms, and runtime mechanisms that **execute a program** represented by a given **encoding scheme** (e.g., source code, bytecode, machine code). It defines how a program's **semantics** are realized on a computational substrate (hardware, VM, or interpreter) through a series of **transformations** and **runtime behaviors**.
> 

> **The C++ evaluation model** is **eager (strict)**, meaning expressions are evaluated immediately when encountered in the execution order, with an emphasis on well-defined sequence points to manage side effects and undefined behavior.
> 

> A **semantics** for a programming language is a model for the computational meaning
of a program written in that language.
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

> The C++ runtime system provides essential support for executing C++ programs, including memory allocation, object lifecycle management, exception handling, and interaction with the operating system, while relying heavily on static compilation for efficiency.
> 

> Programming environments usually offer runtime services such as memory management, thread management, asynchronous programming, exception handling, input/output (I/O) management, and foreign function interfaces (FFIs).
> 

| **Component** | **Description** | Element(s) | **Purpose** |
| --- | --- | --- | --- |
| **Memory Management** | Manages allocation, deallocation, and reuse of memory during program execution. | `malloc/free`, `new/delete`, RAII | Ensures efficient and safe memory usage. |
| **Object Lifecycle** | Handles construction, destruction, and resource cleanup for objects. | Constructors, destructors, smart pointers | Ensures proper resource allocation and deallocation. |
| **Type Information** | Provides runtime type identification (RTTI) and polymorphic behavior. | `typeid`, `dynamic_cast` | Enables safe type casting and introspection. |
| **Exception Handling** | Manages throwing, catching, and propagating exceptions for error handling. | `try`, `catch`, `throw` | Provides a mechanism for structured error handling. |
| **Threading and Concurrency** | Supports thread creation, synchronization, and coordination in multithreaded applications. | `std::thread`, `std::mutex`, `std::condition_variable` | Enables concurrent execution and thread safety. |
| **I/O Operations** | Provides mechanisms for input/output operations. | `std::cin`, `std::cout`, file streams | Manages communication with files, consoles, and devices. |
| **Program Startup and Exit** | Handles initialization of global objects, main function execution, and cleanup at program termination. | `main()`, `atexit()`, static/global constructors | Ensures program setup and graceful termination. |
| **Standard Library Support** | Provides runtime services for the C++ Standard Library, such as containers, algorithms, and utilities. | `std::vector`, `std::string`, `std::sort` | Enables high-level abstractions and utilities. |
| **Dynamic Linking** | Handles loading and linking of shared libraries during program execution. | `.so`/`.dll` files, `dlopen` | Allows modularity and runtime extension. |
| **Synchronization Primitives** | Provides mechanisms to safely share resources among threads. | `std::mutex`, `std::atomic` | Ensures thread-safe access to shared resources. |
| **Debugging and Diagnostics** | Supports debugging tools and runtime checks for program correctness. | Assertions, stack traces, sanitizers | Helps identify and resolve runtime errors. |

## Execution Model

> The **execution model** of a programming language describes **how programs are carried out by the runtime system or computing platform**. It specifies the mechanisms by which code is translated into actions, including how instructions are executed, how memory and modules are managed, how concurrency is handled, and how the runtime interacts with the operating system and hardware.
> 

| **Aspect** | **Description** |
| --- | --- |
| **Compilation / Execution** | C++ is primarily **compiled ahead-of-time (AOT)** to machine code. It can be executed directly by the OS on hardware. No built-in interpreter is standard. |
| **Modules / Dependencies** | Uses **header files, source files, and modules (C++20)**. The linker resolves symbols and combines translation units into a single executable. |
| **Concurrency / Parallelism** | Supports **threads (std::thread), mutexes, atomics, futures, coroutines (C++20)**. Shared memory is managed explicitly; synchronization primitives control ordering and visibility. |
| **Runtime Environment** | Minimal runtime; relies on OS services. Exceptions, dynamic memory, and RTTI are managed via the C++ runtime. |
| **Memory Management** | Stack for local variables, heap via `new`/`delete` or smart pointers, global/static memory for program lifetime. RAII ensures deterministic cleanup. |
| **Debugging / Profiling** | Supports stack traces, debug symbols, instrumentation hooks, and external profilers; no built-in VM or interpreter. |
| **Program Termination / Cleanup** | `main` returns an exit code; destructors and RAII handle cleanup of objects; static objects destroyed at program exit. |
| **Exception Handling** | Synchronous exception model using `try`/`catch`/`throw`. Uncaught exceptions terminate the program. |
| **Execution Semantics** | Sequential by default; side effects and evaluation order mostly left to the standard (except for sequence points and well-defined ordering). |

## **Evaluation Model**

> The **evaluation model** of a programming language describes **how expressions and computations are evaluated to produce values**, including the order of evaluation, handling of side effects, argument passing, recursion, and optimizations applied during computation.
> 

| **Aspect** | **Description** |
| --- | --- |
| **Evaluation Strategy** | C++ uses **eager/strict evaluation** by default: expressions are evaluated as they are encountered. Certain operators (like `&&`, ` |
| **Expression Evaluation** | Expressions are evaluated according to **operator precedence and associativity**. Function arguments are evaluated in an **unspecified order**, except where the standard enforces sequence points. |
| **Function Calls / Call Semantics** | Supports **pass-by-value**, **pass-by-reference**, and **move semantics**. Higher-order functions are supported via function pointers, functors, and `std::function`. |
| **Side Effects** | Side effects occur in the order defined by the **sequence points / sequencing rules**. Undefined behavior arises if multiple side effects conflict on the same object without proper sequencing. |
| **Recursion / Stack Management** | Recursion is supported via the **call stack**. Tail-call optimization is **implementation-dependent**. |
| **Memoization / Caching** | Not built-in; can be implemented manually via static variables, containers, or template metaprogramming. |
| **Optimization Opportunities** | Compiler optimizations can include **constant folding, loop unrolling, inlining, dead code elimination, copy elision**, and template-based compile-time evaluation. |
| **Evaluation Contexts** | Evaluation depends on **context**: initialization, assignment, conditional branches, loops, template instantiation, etc. |
| **Effect Management** | C++ is **imperative**, so side effects are explicit. RAII patterns help manage resource lifetimes deterministically. |
| **Speculative Execution / Short-Circuiting** | Some operators (`&&`, ` |

## Memory System

> The **memory system** of a programming language or runtime defines **how a program allocates, organizes, accesses, and reclaims memory during execution**. It governs the storage of variables, objects, data structures, code, and execution contexts, and ensures correctness, efficiency, and safety in memory use.
> 

> The ***items*** of a program are those functions, modules, and types that have their value calculated at compile-time and stored uniquely in the memory image of the rust process. Items are neither dynamically allocated nor freed.
> 

> The ***heap*** is a general term that describes boxes.  The lifetime of an allocation in the heap depends on the lifetime of the box values pointing to it. Since box values may themselves be passed in and out of frames, or stored in the heap, heap allocations may outlive the frame they are allocated within. An allocation in the heap is guaranteed to reside at a single location in the
heap for the whole lifetime of the allocation - it will never be relocated as
a result of moving a box value.
> 

> A *variable* is a component of a stack frame, either a named function parameter,
an anonymous [temporary](https://doc.rust-lang.org/reference/expressions.html#temporaries), or a named local variable.
> 

> The **C++ Memory Model** defines how memory is managed and accessed in concurrent environments, ensuring consistent and predictable behavior in multithreaded programs. It outlines how threads interact with memory, how to ensure data synchronization across threads, and how to avoid issues like race conditions and undefined behavior.
> 

| **Aspect** | **Description** | **How C++ Implements It** |
| --- | --- | --- |
| **Memory Ordering** | Refers to the order in which operations (loads/stores) are executed relative to each other. | C++ enforces memory ordering through atomic operations and synchronization mechanisms like `std::atomic` with memory order semantics (`std::memory_order`). |
| **Atomic Operations** | Operations that execute on data atomically (i.e., without interruption) to avoid race conditions. | The `<atomic>` header provides `std::atomic`, supporting atomic load, store, compare-and-swap (CAS), fetch-and-add, and more. |
| **Data Races** | A situation where two or more threads access the same memory location simultaneously, and at least one access is a write. | The C++ memory model requires synchronization mechanisms (like mutexes or atomics) to avoid data races in concurrent code. |
| **Sequential Consistency** | The guarantee that the operations in a program will appear to execute in a sequential order, preserving order of operations. | C++'s memory model doesn't guarantee sequential consistency, but provides memory order options (`std::memory_order_seq_cst`) to impose a consistent ordering where necessary. |
| **Happens-Before Relationship** | Defines the order in which memory operations (reads/writes) are guaranteed to be visible to other threads. | C++ ensures a **happens-before** relationship between synchronized operations, such as unlocking a mutex after locking it, or the release of one thread's atomic variable visible to another thread. |
| **Fence Operations** | Memory barriers that ensure proper ordering of memory operations, preventing certain types of optimizations that could lead to race conditions. | C++ provides memory fences via `std::atomic_thread_fence` and `std::atomic_signal_fence` to enforce memory order constraints. |
| **Synchronization Mechanisms** | Tools to ensure memory visibility and proper sequencing in multithreaded environments. | C++ supports synchronization mechanisms like `std::mutex`, `std::lock_guard`, `std::condition_variable`, and atomic operations to synchronize memory accesses across threads. |
| **Thread-Local Storage (TLS)** | Each thread has its own private memory for storing data that is not shared with other threads. | The `thread_local` keyword in C++ ensures that variables are stored in thread-local storage, providing each thread with its own instance of the variable. |
| **Memory Visibility** | Ensures that updates to memory made by one thread are visible to other threads under proper synchronization. | Proper synchronization mechanisms, including atomic operations and memory fences, are used to ensure memory visibility across threads. |
| **Release/Acquire Semantics** | Release semantics ensure writes in one thread are visible to other threads after synchronization. Acquire semantics ensure that reads are correctly synchronized. | `std::atomic::store`, `std::atomic::load`, and `std::memory_order_acquire`, `std::memory_order_release` provide the necessary memory synchronization for release and acquire operations. |
| **Relaxed Memory Order** | Memory operations can be performed without any ordering guarantees, except for the atomicity of the operation itself. | The memory order `std::memory_order_relaxed` allows operations to be performed without enforcing synchronization between threads, improving performance in non-critical sections. |
| **Store-Load Ordering** | Refers to the order in which stores and loads are executed, ensuring proper memory visibility in multithreaded environments. | C++'s memory model supports store-load synchronization using specific memory orderings such as `std::memory_order_acquire` and `std::memory_order_release` to maintain visibility. |

## References

- [Linker](note.html?n=technica/computation/language-system/conceptual-model-language-system/linker.md)
- [Loader](note.html?n=technica/computation/language-system/conceptual-model-language-system/loader.md).
- [Evaluation Model](note.html?n=technica/computation/language-system/conceptual-model-language-system/evaluation-model.md)
- [Memory  Management](note.html?n=technica/computation/language-system/conceptual-model-language-system/memory-management.md)
- [Runtime Representation](note.html?n=technica/computation/language-system/conceptual-model-language-system/runtime-representation.md)
- [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md)
- 
- [X: ⚙️ Execution System](https://app.notion.com/p/X-Execution-System-f10db63e79ca4ca188bdf74310d2b2c6?pvs=21)
- https://www.youtube.com/watch?v=JaKKzgqINhI
- https://www.youtube.com/watch?v=ZAji7PkXaKY
- [Memory model](https://doc.rust-lang.org/reference/memory-model.html#memory-model)
- https://en.cppreference.com/w/cpp/language/memory_model
- https://www.youtube.com/watch?v=SVEYNEWZLo4
- https://en.wikipedia.org/wiki/Runtime_system
- https://stackoverflow.com/questions/42728239/runtime-system-in-c