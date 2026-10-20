# Python: Performance

> How does the **computational model's** implementation impact performance?
> 

> What are the key factors in programming language **`X`** that influence the execution speed and overall efficiency of programs?
> 

> How does the language's mapping to **`hardware`** (e.g., CPU, memory, I/O) affect application performance?
> 

> What performance impact do the language's built-in data structures have on memory usage and **`execution time`**?
> 

QA:

- What is the model of the **system under investigation**?
- Which are the metrics being evaluated?
- What is the evaluation workload?
- How to get a **reproducible benchmark**?

## System Model

> Setting: CPython, …
> 

> To evaluate the performance of the Python language system, we need to model its key components and their interactions.
> 

### Interpreter Layer: **CPython**

> **CPython:** Parses, compiles, and executes Python code.
> 

> **Python Virtual Machine (PVM)**: Executes bytecode instructions
> 

> What are the performance impacts of Python's code execution system?
> 

**Performance Impact**:

- **Compilation:  Source Code → Abstract Syntax Tree (AST) → Bytecode**: Python code is first parsed into an AST, then compiled into bytecode.
- **Global Interpreter Lock (GIL)**: Limits multi-threaded performance by allowing only one thread to execute Python bytecode at a time.
- **Bytecode Execution**: Python code is compiled to bytecode, which is then interpreted. This adds overhead compared to native machine code execution.
    - **Instruction Dispatch**: Each bytecode instruction incurs interpretation overhead.
    - **Dynamic Lookups**: Attribute and method lookups are resolved at runtime, adding overhead.
- **Function Calls:** Each function call creates a new stack frame.
    - **Frame Creation**: Allocating and deallocating stack frames adds overhead.
    - **Dynamic Argument Handling**: Supports variable-length arguments and keyword arguments, which adds complexity.
- **Object Overhead (Metadata)**: Each object stores type information, reference count, and other metadata.
    - **Memory Usage**: Increased memory footprint due to metadata.
    - **Access Time**: Additional indirection when accessing object attributes.

### Memory Management

> **Garbage Collection**: Uses reference counting and a cyclic garbage collector to manage memory.
> 

**Performance Impact**:

- **Reference Counting**: Adds overhead for every object creation, assignment, and deletion.
- **Cyclic Garbage Collection**: Periodic collection of unreachable objects can cause pauses.

### Native Code Execution

> Write performance-critical code in C and expose it to Python.
> 
- **Performance Impact**:
    - **Native Speed**: Executes at machine code speed.
    - **GIL Bypass**: Can release the GIL during execution.

### Language-Hardware Interaction

> 

### Standard Library

- > See More in [Python: The Standard Library]
> 

**Object Model**

- **Everything is an Object**: All data types (e.g., `int`, `str`, `list`) are objects with metadata (type, reference count, etc.).
- **Performance Impact**:
    - **Object Overhead**: Each object has additional metadata, increasing memory usage and access time.
    - **Dynamic Typing**: Type checking at runtime adds overhead.

**Primitive Types**

- **`int`, `float`, `bool`, `str`, etc.**: Immutable and often optimized.
- **Performance Impact**:
    - **Small Integer Caching**: Small integers (e.g., -5 to 256) are cached for reuse.
    - **String Interning**: Short strings are interned to save memory.

**Collections**

- **`list`, `tuple`, `dict`, `set`, etc.**: Mutable and immutable containers.
- **Performance Impact**:
    - **Dynamic Resizing**: `list` and `dict` resize dynamically, which can cause occasional performance spikes.
    - **Hash Table Overhead**: `dict` and `set` use hash tables, which have O(1) average-time complexity but can degrade to O(n) in worst-case scenarios.

**Built-in Algorithms**

- **Sorting**: Python uses **Timsort** (a hybrid of merge sort and insertion sort) for `list.sort()` and `sorted()`.
    - **Performance Impact**:
        - **Time Complexity**: O(n log n) in the average and worst cases.
        - **Space Complexity**: O(n) due to temporary storage.
- **Searching**: Linear search is used for lists, while hash-based lookups are used for dictionaries and sets.
    - **Performance Impact**:
        - **List Search**: O(n) for linear search.
        - **Dictionary/Set Lookup**: O(1) average time due to hash tables.

**Asynchronous Programming**

- **`asyncio` Module**: Uses event loops for asynchronous I/O.
- **Performance Impact**:
    - **I/O-bound Tasks**: Efficient for handling many I/O-bound tasks concurrently.
    - **CPU-bound Tasks**: Not suitable for CPU-bound tasks.

## **Evaluation Metrics**

To evaluate Python's performance, consider the following metrics:

- **Execution Time:** Measure the time taken to execute a specific task or program.
- **Memory Usage:** Measure the memory footprint of a program, including object overhead and garbage collection.
- **Scalability:** Evaluate how performance scales with increasing input size or workload.
- **Concurrency Efficiency:** Measure the performance of multi-threaded, multi-process, and asynchronous programs.
- **Latency and Throughput:** For I/O-bound tasks, measure latency (response time) and throughput (requests processed per second).
- Energy Efficiency: …

## Workload

> 

## References

- https://github.com/attractivechaos/plb2
- [‣](https://app.notion.com/p/b0a2a8d65e9d46d3b9ccfe1614c1bd73?pvs=21)
- https://github.com/sharkdp/hyperfine
- [Language System](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/language-system.md)
- https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3DRrHGX1wwSYM&ved=2ahUKEwj29Pa57sqLAxVCfzABHcUAH2k4FBC3AnoECAkQAg&usg=AOvVaw1bDGjCEVz0p7pCIa6LMH8v
- Weicker, R. P. (1990). An overview of common benchmarks. *Computer*, *23*(12), 65-75.
- https://programming-language-benchmarks.vercel.app/
- https://www.gingerbill.org/article/2024/01/22/comparing-language-benchmarks/
- https://attractivechaos.github.io/plb/
- https://en.wikipedia.org/wiki/The_Computer_Language_Benchmarks_Game
- https://benchmarksgame-team.pages.debian.net/benchmarksgame/index.html
- https://lemire.me/blog/2017/01/16/best-programming-language-for-high-performance-january-2017/
- https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python.html
- https://discuss.python.org/t/python-benchmarking-in-unstable-environments/22334
- https://en.lewoniewski.info/2024/python-3-12-vs-python-3-13-performance-testing/
- https://speed.python.org/comparison/
- https://perfpy.com/#/
- https://blog.miguelgrinberg.com/post/is-python-really-that-slow
- https://pyperformance.readthedocs.io/
- https://github.com/python/pyperformance
- https://github.com/python/pyperformance/tree/main/pyperformance/data-files/benchmarks
- [X: ⚡Performance](https://app.notion.com/p/X-Performance-19dc0f5171ec8035b297f5db0fb99cfa?pvs=21)
- https://github.com/csiglab/language-system-labs
- https://github.com/csiglab/performance-labs