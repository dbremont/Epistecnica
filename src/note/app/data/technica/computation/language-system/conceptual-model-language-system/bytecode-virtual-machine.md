---
tags: [language-system]
---

# Bytecode Virtual Machine

- [Interpreter System](note.html?n=technica/computation/language-system/conceptual-model-language-system/interpreter-system.md), [Compiler System](note.html?n=technica/computation/language-system/conceptual-model-language-system/compiler-system.md), [Parsing](note.html?n=technica/computation/language-system/conceptual-model-language-system/parsing.md), [Just-in-time (JIT) Compilation](note.html?n=technica/computation/language-system/conceptual-model-language-system/just-in-time-jit-compilation.md), [Grammar](note.html?n=technica/computation/language-system/conceptual-model-language-system/grammar.md)

> A **Bytecode Virtual Machine (VM)** is a software-based computational abstraction that executes intermediate, platform-independent instructions—known as *bytecode*—through an emulated instruction set architecture (ISA).
> 

## Bytecode VM’s Models

> 

| **Type** | **Execution Model** | **Memory Access** | **Notable Examples** | **Advantages** | **Disadvantages** |
| --- | --- | --- | --- | --- | --- |
| **Stack-based VM** | Operands pushed/popped from a stack | Implicit (stack ops) | JVM, CPython, .NET CLR | Simple bytecode design, compact code | Slower (memory-bound stack ops) |
| **Register-based VM** | Operands stored in virtual registers | Explicit (register ops) | Dalvik VM (Android), Lua 5.0+ | Faster (fewer instructions, closer to hardware) | Larger bytecode, complex compilation |
| **Hybrid VM** | Combines stack/register approaches | Mixed | Erlang BEAM, WASM (later versions) | Balances speed and simplicity | Increased implementation complexity |
| **Tracing JIT VM** | Dynamically traces hot paths to native code | Depends on JIT | PyPy (RPython), LuaJIT | High performance for hotspots | High memory overhead, warmup delay |
| **AOT-Compiled VM** | Bytecode precompiled to native code | Direct native access | .NET AOT, GraalVM Native Image | No interpreter overhead, fast startup | Loss of portability, larger binaries |
| **Hardware-Assisted VM** | Offloads ops to CPU (e.g., Jazelle) | Mixed (HW/SW) | Jazelle (ARM JVM acceleration) | Near-native speed for certain bytecode | Limited ISA support, vendor lock-in |

## References

- [Emulator](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/emulator.md)
- [Virtualization](note.html?n=technica/computation/platform/virtualization.md)
- https://github.com/dbremont/isa-labs
- https://github.com/dbremont/linux-api-labs
- https://github.com/dbremont/virtualization-labs/tree/main/janusvm
- https://www.youtube.com/watch?v=TxLakn190ZA&list=WL&index=2&t=878s
- https://github.com/jakogut/tinyvm
- https://www.andreinc.net/2021/12/01/writing-a-simple-vm-in-less-than-125-lines-of-c
- https://www.jmeiners.com/lc3-vm/
- https://www.youtube.com/playlist?list=PLpM-Dvs8t0VY73ytTCQqgvgCWttV3m8LM
- https://github.com/tsoding/bm
- [‣](https://app.notion.com/p/10e598edb79081d2a549ec868ef75bcd?pvs=21)
- [‣](https://app.notion.com/p/1c7598edb79080a99e37e0c313af53bc?pvs=21)
- [‣](https://app.notion.com/p/1c7598edb790808d9ed5e22c6617dfd1?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081d2af7fededaf67de2c?pvs=21)