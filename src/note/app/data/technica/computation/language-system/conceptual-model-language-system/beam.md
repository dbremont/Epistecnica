---
tags: [metacomputation, tool]
---

# BEAM


## Instruction Set

…

## Beam File Spec

**BEAM** files are the compiled bytecode files used by the **BEAM virtual machine** to execute Erlang and Elixir programs. The **BEAM file format** is binary and follows a specific grammar or structure. Here’s a high-level overview of the grammar of a **BEAM file**:

In Erlang’s BEAM file format, different sections or chunks have specific names, each serving a particular purpose. Here’s a list of common chunk names found in Erlang BEAM files:

1. **Atom Chunk (Atom):** This chunk contains atoms used in the module. Atoms are often used for identifiers in Erlang code.
2. **String Chunk (StrT):** It stores string literals used in the module.
3. **Export Chunk (ExpT):** This chunk contains information about functions and attributes exported by the module.
4. **Import Chunk (ImpT):** It stores information about functions and attributes imported by the module from other modules.
5. **Literal Chunk (LitT):** This chunk contains literal values used in the module, including atoms, integers, floats, and more.
6. **Code Chunk (Code):** It contains the bytecode instructions for the functions defined in the module.
7. **Line Number Chunk (Line):** This chunk holds information about the mapping of bytecode instructions to source code line numbers, aiding in debugging.
8. **Function Chunk (FunT):** It is used to store information about fun expressions (closures) defined within the module.
9. **Attribute Chunk (Attr):** The attribute chunk may contain various attributes, including compiler-specific or custom attributes that provide additional information about the module.
10. **Compile Chunk (CInf):** This chunk stores compiler information and can include details about the compiler version and options used during compilation.
11. **Import Info Chunk (ImpI):** It contains information about the imports of the module.
12. **Module Info Chunk (ModI):** This chunk provides metadata about the module, such as its name and attributes.
13. **Opt Info Chunk (OptI):** It may contain optimization-related information.

Please note that the exact set of chunks and their contents may vary depending on the version of Erlang/OTP and the specific compilation options used when creating the BEAM file. The BEAM file format can evolve over time, so it’s important to consult the documentation or specifications for the particular Erlang/OTP version you are working with to get the most accurate and up-to-date information on BEAM file chunks.

## Engine

The BEAM virtual machine is the runtime environment for executing Erlang and Elixir applications. It is known for its concurrency, fault tolerance, and distributed computing capabilities. Here is an overview of the BEAM virtual machine architecture:

1. **Processes**:
    - BEAM follows the Actor model of computation, where processes are lightweight, isolated units of computation.
    - Each process has its own heap memory, stack, and message queue.
    - Processes communicate by sending and receiving messages, promoting concurrency and isolation.
2. **Memory Management**:
    - BEAM uses a generational garbage collector to manage memory.
    - Processes have separate heaps, and the garbage collector operates independently on each process’s heap.
    - The memory system efficiently handles the creation and cleanup of processes and their associated memory.
3. **Scheduler**:
    - BEAM employs a preemptive scheduler that allocates CPU time to processes.
    - The scheduler ensures fair and efficient execution of processes.
    - It uses a concept called “reductions” to measure the amount of work done by a process and make scheduling decisions.
4. **Hot Code Loading**:
    - BEAM supports hot code swapping, allowing you to update code in a running system without interrupting its operation.
    - This feature is vital for achieving high availability and continuous deployment.
5. **Concurrency**:
    - BEAM provides lightweight concurrency with processes, making it efficient to create and manage thousands of concurrent processes.
    - Erlang and Elixir applications are inherently concurrent and parallel, which is ideal for building systems with high concurrency requirements.
6. **Fault Tolerance**:
    - BEAM encourages the design of fault-tolerant systems.
    - Processes can be linked together, and if one process fails, linked processes can be notified and handled accordingly.
    - Supervision trees and supervision strategies allow processes to be structured for fault tolerance.
7. **Distribution**:
    - BEAM supports distribution of Erlang and Elixir processes across networked nodes.
    - Processes on different nodes can communicate seamlessly, enabling the development of distributed applications.
    - The distribution is transparent to developers, making it easy to build scalable and distributed systems.
8. **Ports and NIFs**:
    - BEAM allows interfacing with external libraries and languages through ports (external processes) and NIFs (Native Implemented Functions).
    - This flexibility enables integration with C, Python, and other languages.
9. **Loadable Modules**:
    - BEAM loads modules at runtime, which facilitates code loading and distribution.
    - This runtime loading enables the development of highly dynamic and adaptable systems.
10. **Monitoring and Debugging**:
    - BEAM provides tools like `Observer` for monitoring running processes, message queues, and system metrics.
    - Remote debugging tools are available for diagnosing issues in distributed systems.
11. **Security**:
    - BEAM is designed with security in mind. Processes are isolated, and message passing is controlled.
    - It’s challenging for one process to compromise the integrity of another.
12. **BIFs (Built-In Functions)**:
    - BEAM includes a set of built-in functions for low-level operations and system interaction.
13. **Modules and Code Organization**:
    - BEAM loads and manages modules, making it possible to structure code into reusable components.

## References

- [BEAM File Format](https://beam-wisdoms.clau.se/indepth-beam-file.html)
- [Erlang VM Internals](https://github.com/AlexanderKaraberov/Erlang-BEAM-Links)
- [A brief introduction to BEAM](https://www.erlang.org/blog/a-brief-beam-primer/)
- [Implementations and Ports of Erlang](https://www.erlang.org/faq/implementations.html)
- [The Erlang BEAM Virtual Machine Specification](http://www.cs-lab.org/historical_beam_instruction_set.html)
- [A peak into the Erlang compiler and BEAM bytecode](http://gomoripeti.github.io/beam_by_example/)