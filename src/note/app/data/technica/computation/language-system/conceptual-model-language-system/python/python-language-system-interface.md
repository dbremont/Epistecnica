# 💻🔧 Python: Language System Interface

> The **Language System Interface** encompasses the collection of mechanisms, APIs, and tooling hooks that enable interaction with both the **compile-time** and **runtime** aspects of a programming language system. These interfaces serve as critical access points for developers, compilers, debuggers, profilers, and other tools to analyze, transform, observe, or extend the behavior of programs.
> 

> By exposing internal structures—such as syntax trees, type information, bytecode, runtime metadata, and execution state—the language system interface facilitates tasks ranging from static analysis and metaprogramming to runtime instrumentation and debugging. Studying these interfaces reveals how a language system supports extensibility, introspection, tooling integration, and control over program behavior, making them essential for advanced language engineering and systems programming.
> 

Guiding Questions:

- What mechanisms does the language system provide to interface with its internal compile-time and runtime components?

## Mechanisms

| **Mechanism Category** | Description | Support |
| --- | --- | --- |
| **Compiler APIs** |  |  |
| **Macro Systems** |  |  |
| **Type Reflection APIs** |  |  |
| **Instrumentation APIs** |  |  |
| **Debugging Interfaces** |  |  |
| **Execution Tracing Hooks** |  |  |
| **Plugin/Extension Interfaces** |  |  |
| **Build Tool Integrations** |  |  |
| **Virtual Machine APIs** |  |  |
| **Intermediate Representation (IR) Access** |  |  |
| **Scripting/REPL Interfaces** |  |  |
| **Linker and Loader Hooks** |  |  |
| **Language Server Protocol (LSP)** |  |  |

## References

- [Language System Interface](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-system-interface.md)

## How python debugging works?

> If **GDB** uses **OS** tools to debug a running process, how is a **Python process debugged**?
> 

> 

| **Tool** | **Purpose** |
| --- | --- |
| **`bdb`** | **…** |
| **`pdb`** | Interactive debugging |
| **`trace`** | Logging executed lines |
| **`warnings`** | Handling runtime warnings |
| **`cProfile`** | Performance profiling |
| **`faulthandler`** | Debugging crashes |
| **`sys.settrace()`** | Low-level execution tracing |

- https://github.com/Delgan/loguru
- https://github.com/microsoft/debugpy
- https://github.com/hynek/structlog
- https://github.com/microsoft/picologging
- https://github.com/python/cpython/blob/3.13/Lib/bdb.py
- https://microsoft.github.io/debug-adapter-protocol//
- https://realpython.com/python-logging/
- https://docs.python.org/3/library/debug.html
- https://docs.python.org/3/library/bdb.html
- https://docs.python.org/3/library/pdb.html
- https://docs.python.org/3/library/logging.html
- https://docs.python.org/3/library/trace.html
- https://docs.python.org/3/library/sys.html (Debug Support)