---
tags: [language-system, tool]
---

# CPython

- [Python](note.html?n=technica/computation/language-system/conceptual-model-language-system/python.md)

Python's implementation involves several models of computation, depending on the context—whether we're discussing its execution model, memory management, or underlying abstractions. Below is a structured breakdown:

---

### **1. Execution Model**

- **Imperative Model**: Python is primarily an imperative language, executing statements step-by-step with explicit state changes.
- **Von Neumann Architecture**: Follows the fetch-decode-execute cycle, with mutable memory (like variables in RAM).
- **Interpreter-Based**: Python code is executed by an interpreter (e.g., CPython, PyPy), not directly by hardware.

---

### **2. Memory Model**

- **Object-Oriented Heap**: All Python objects are dynamically allocated on a heap, managed via references.
- **Automatic Memory Management**: Uses **reference counting** (primary) and **garbage collection** (for cyclic references).
- **Dynamic Typing**: Variables are bound to objects at runtime, with no static type enforcement.

---

### **3. Concurrency/Parallelism Models**

- **Global Interpreter Lock (GIL)**: CPython’s GIL restricts true parallel threading (single-threaded execution at the bytecode level).
- **Multi-Processing**: Achieves parallelism via `multiprocessing` (separate processes, no GIL).
- **Async/Await**: Event-driven coroutines (cooperative multitasking via `asyncio`).
- **Shared-Nothing**: Processes communicate via queues/pipes (no shared memory by default).

---

### **4. Abstraction Layers**

- **Bytecode Virtual Machine**: CPython compiles Python to bytecode executed by a stack-based VM.
- **Just-In-Time (JIT)**: PyPy uses a JIT compiler for optimization.
- **Foreign Function Interface (FFI)**: Interfaces with lower-level models (e.g., C via `ctypes`/`CFFI`).

---

### **5. Formal Models**

- **Turing Complete**: Python can simulate any Turing machine (like most general-purpose languages).
- **Lambda Calculus**: Supports functional paradigms (higher-order functions, lambdas).
- **Object-Oriented**: Classes, inheritance, and polymorphism align with OOP models.

---

### **Summary Table**

| **Model of Computation** | **Python Implementation** |
| --- | --- |
| **Execution** | Imperative, interpreter-based, Von Neumann |
| **Memory** | Heap-allocated objects, reference counting + garbage collection |
| **Concurrency** | GIL (threads), multiprocessing, async/await |
| **Abstractions** | Bytecode VM (CPython), JIT (PyPy), FFI for C integration |
| **Formal Power** | Turing complete, supports lambda calculus, OOP paradigms |

---

### **Key Notes**

- **CPython** (reference implementation) dominates, but other interpreters (e.g., PyPy, Jython) may differ.
- Python’s high-level abstractions hide lower-level details (e.g., memory addresses, bytecode), but they underpin its behavior.

## Cpython Internals

CPython is the default implementation of the Python programming language and is the one most commonly used. It is written in the C programming language and is designed to be highly portable across a wide range of platforms.

Here’s a brief overview of how CPython works:

**Compilation**: When you write a Python program, it is first compiled into bytecode. This is a low-level representation of your code that can be executed by the Python interpreter.

**Execution**: Once the bytecode has been generated, it can be executed by the CPython virtual machine. This is a runtime environment that interprets the bytecode and executes the program.

**Memory management**: CPython uses a system of reference counting to manage memory. Each object in Python has a reference count, which is the number of references to that object in the program. When the reference count reaches zero, the object is deleted.

**Standard library**: CPython includes a large standard library that provides a wide range of functionality for tasks such as file I/O, networking, and regular expressions.

**Extensions**: CPython allows you to write C extensions that can be imported and used in your Python code. This can be useful for tasks that require high performance or access to system-level functionality.

Overall, CPython provides a powerful and flexible environment for developing and running Python programs. Its combination of high-level programming constructs and low-level performance optimizations make it a popular choice for a wide range of applications.

**Main Files**: - **Python/main.c** - This is the entry point for the Python interpreter. It sets up the initial Python environment, reads the command-line arguments, and starts the interpreter loop. - **Python/ceval.c** - This file contains the core interpreter loop, which executes Python bytecode and manages the Python stack. - **Objects/object.c** - This file contains the implementation of the base object type, which is the parent class of all Python objects. It also contains the reference counting system used for memory management in CPython. - **Python/compile.c** - This file contains the bytecode compiler, which translates Python source code into bytecode that can be executed by the interpreter. - **Python/import.c** - This file contains the implementation of the Python import system, which is used to load and execute Python modules. - **Python/marshal.c** - This file contains the functions used to serialize and deserialize Python objects to and from a binary format. - **Python/thread.c** - This file contains the functions used for multi-threading in Python, including the Global Interpreter Lock (GIL) mechanism. - **Python/sysmodule.c** - This file contains the implementation of the built-in sys module, which provides access to system-level functionality such as command-line arguments and environment variables.

These are just a few examples of the many files and functions that make up the CPython implementation. The CPython source code is a large and complex system that is constantly evolving and improving, so it can be challenging to keep up with all the changes. However, understanding the basics of how the system works can be a valuable tool for anyone who wants to work with Python at a low level.

## References

- https://github.com/python/cpython