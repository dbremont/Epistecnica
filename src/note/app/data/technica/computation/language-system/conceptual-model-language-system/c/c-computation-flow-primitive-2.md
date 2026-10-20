# C++: 🔄 Computation Flow Primitive

> `X` is a **systems programming language** renowned for its focus on safety and performance, and its approach to concurrency is no exception. Rust's ownership and type systems are designed to prevent race conditions at compile time, offering a robust foundation for writing safe concurrent code.
> 

> **A Control Flow Model** is a **representation** of the **sequence** and order in which statements or instructions are executed in a program. It describes how the program’s control flows from one statement to the next, based on conditions, loops, and other control structures.
> 

Guiding Questions:

- What is the atomic unit of execution?
- How is parallelism exposed?
- Is the concurrency model formally specified?
- Can programs be model-checked for races?
- Memory Model & Synchronization
    - What memory consistency model does the language enforce?
    - What synchronization primitives are provided?
- Data Sharing & Communication
    - How do concurrent units communicate?
    - How is mutable state managed?
- Error Handling & Fault Tolerance
    - How are panics/crashes handled in concurrent contexts?
    - What happens if a thread/actor deadlocks?
- Performance & Scalability
    - What is the cost of spawning a thread/task?
- Tooling & Observability
    - What debugging tools exist?
    - How is backpressure handled?
- Language Specific:
    - <<TO BE FILLED>>
- Control Flow
    - What are the basic control flow constructs?
    - How are exceptions implemented?
    - Does the language support coroutines/generators?
    - Are there first-class continuations (e.g., Scheme call/cc, Kotlin Continuation)?
    - How does control flow interact with concurrency?
    - What synchronization primitives affect control flow?
    - How does the type system restrict control flow?
    - How is control flow represented in the IR?
    - What optimizations are applied to control flow?
    - How are recursive algorithms optimized?
    - How does control flow map to CPU pipelines?
    - What is the cost of context switching (e.g., coroutines vs. threads)?
    - How are stack traces generated?
- Error Handling
    - What constitutes an "error" in the language?
    - **s there a unified error type hierarchy** (e.g., Java `Throwable`), or are errors fragmented (e.g., C’s `errno`, POSIX signals)?
    - What metadata is attached to errors?
    - How are errors encoded?
    - How are errors propagated across boundaries?
    - Is there error suppression (e.g., Python suppress, C++ noexcept)?
    - What is the runtime overhead of error handling?
    - Does the language support zero-cost error handling (e.g., Rust’s Result vs. C++ exceptions)?
    - How do errors interact with concurrent code?
    - How are errors propagated across boundaries?
    - How are errors inspected?
        
        

## Taxonomy

> **Control Flow Model** is a **representation** of the **sequence** and order in which statements or instructions are executed in a program. It describes how the program’s control flows from one statement to the next, based on conditions, loops, and other control structures.
> 

| **Control Flow Model** | **Description** |
| --- | --- |
| **Sequential Control Flow Model** | The default control flow model where statements are executed in the order they appear in the code. |
| **Conditional Control Flow Model** | Using conditional statements to make decisions based on certain conditions. |
| **Iterative Control Flow Model** | Using loops to repeatedly execute a block of code. |
| **Switch Control Flow Model** | Using match or case statements to compare values against multiple patterns and execute the corresponding code. |
| **Exception Handling Control Flow Model** | Using mechanisms to handle runtime errors and unexpected situations. |
| **Thread Control Flow Model** | Using threads to execute code concurrently and manage interactions between them. |
| **Coroutines Control Flow Model** | Writing asynchronous code with the ability to suspend and resume execution. |
| **Data-Driven Control Flow Model** | Using event-driven programming and message passing to respond to external events. |
| Goto Statement | Transfers control to another part of the program (typically to a label). |
| Return Statement | Exits from the current function and optionally returns a value to the caller. |
| Function Calls | Invokes a function to execute its code. |
| Control Flow with Pointers | Control flow involving indirect access to data or functions. |
| Scoped Control Flow (RAII) | Uses resource management within scope to manage control flow. |
| Control Flow with Templates | Allows branching logic to be executed based on the type passed to a template. |
| Type-based Conditional Execution | Executes code based on the type information available at compile time. |

## Concurrency Model

> 

| Concurrency Model | Description |
| --- | --- |
| Threads |  |
| Thread-Based Concurrency Model |  |
| Task-Based Parallelism Model |  |
| Work-Stealing Scheduler Model |  |
| GPU Parallelism Model |  |
| Data Parallelism Model |  |
| Asynchronous Programming Model |  |
| Lock-Free Programming Model |  |
| Shared Memory Model |  |
| Message Passing Model |  |
| Distributed Computing Model |  |
| Coroutines Model |  |

### Unit

### Property

### Control Mechanism

> aka. Synchronization Mechanism
> 

| **Synchronization Mechanism** | **Description** | **How C++ Implements It** |
| --- | --- | --- |
| **Mutex-Based Synchronization Model** | Ensures that only one thread can access a resource at a time, preventing data races. | C++ provides `std::mutex`, `std::lock_guard`, and `std::unique_lock` to enforce exclusive access to shared resources. |
| **Read/Write Lock Model** | Allows multiple threads to read a shared resource concurrently but ensures exclusive access for writing. | C++17 introduces `std::shared_mutex`, allowing multiple threads to acquire read locks simultaneously but only one thread to acquire a write lock. |
| **Condition Variables** | Allows threads to wait for certain conditions to be met, signaling when they can proceed. | C++ provides `std::condition_variable` and `std::condition_variable_any` to synchronize threads by waiting and notifying based on certain conditions. |
| **Atomic Operations Model** | Performs atomic operations on shared variables to ensure thread safety without locks. | C++ supports atomic types and operations via the `<atomic>` library, using `std::atomic` to perform operations atomically. |
| **Lock-Free Programming Model** | Eliminates the need for locks by using atomic operations to ensure thread safety. | C++ atomic operations, like `std::atomic::compare_exchange_weak`, enable lock-free programming, avoiding contention on shared data. |
| **Thread Synchronization with Future/Promise** | Provides synchronization through asynchronous tasks, where one thread waits for a result from another. | C++11 introduces `std::future` and `std::promise` for synchronizing tasks by passing data between threads and ensuring they complete. |
| **Barrier Synchronization Model** | Synchronizes multiple threads, ensuring they all reach a certain point in execution before proceeding. | C++20 introduces `std::barrier`, which blocks a set of threads until all threads have reached the synchronization point. |
| **Spinlock Model** | A lock where the thread repeatedly checks if the lock is available, using busy-waiting. | C++ provides `std::atomic_flag` and `std::atomic::test_and_set` for implementing spinlocks, where threads repeatedly check a flag before proceeding. |
| **Semaphore Model** | Controls access to shared resources by allowing a certain number of threads to access a resource simultaneously. | C++20 introduces `std::counting_semaphore` and `std::binary_semaphore` for controlling access to shared resources, limiting the number of threads accessing a resource concurrently. |
| **Event Model** | Uses events to notify threads of changes in state or completion of tasks. | C++ doesn't directly provide an event model, but libraries like **Boost.Asio** offer event-driven programming with async I/O, allowing threads to wait for events to be triggered. |
| **Thread-Specific Storage Model** | Allows threads to store and access data that is private to each thread. | C++ supports **thread-local storage (TLS)** using the `thread_local` keyword, allowing each thread to have its own private copy of a variable. |
| **Signal and Slot Model (Reactive)** | Uses signals and slots to send notifications between objects, typically used in GUI applications or reactive programming. | Although not native in the C++ standard library, frameworks like **Qt** implement a signal-slot mechanism for thread synchronization and communication. |
| **Mutex with Condition Variable (Producer/Consumer)** | Coordinates producer and consumer threads using a mutex and a condition variable to ensure safe access to shared data. | C++ combines `std::mutex` and `std::condition_variable` to implement a producer-consumer pattern, where threads synchronize access to a shared buffer. |
| **Task Synchronization Model** | Synchronizes tasks, ensuring that a task completes before the next one starts. | C++ provides `std::async`, `std::future`, and `std::promise` to synchronize tasks in asynchronous programming, where the result of one task is used by another. |
| **Critical Section Model** | A section of code that can only be executed by one thread at a time to ensure mutual exclusion. | C++ provides `std::mutex` to create critical sections, ensuring only one thread can execute a given block of code at a time. |
| **Deadlock Prevention Model** | Ensures that threads do not enter a state where they are all waiting on each other. | C++ libraries use techniques such as lock ordering, `std::lock` with `std::unique_lock`, and other strategies to avoid deadlocks in concurrent code. |
| **Priority Inversion Prevention Model** | Ensures that low-priority threads do not block higher-priority threads by holding a lock. | C++ doesn’t have built-in priority inversion prevention, but solutions can be implemented using custom mutexes or libraries like **Boost.Thread**. |

## **Path-of-execution Mechanism**

> 

## **❌** Error Handling

> 

## References

- [Concurrency](note.html?n=technica/computation/concurrency.md)
- [Notion of Change](note.html?n=technica/computation/language-system/conceptual-model-language-system/notion-of-change.md)
- [Unit of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/unit-of-computation.md)
- [Exception Handling System](note.html?n=technica/computation/language-system/conceptual-model-language-system/exception-handling-system.md)