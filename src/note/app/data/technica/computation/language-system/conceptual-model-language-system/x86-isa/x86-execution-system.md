# x86: 🚀 Execution System

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

## State Model

- Memory
- …

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

## Register System

> Which are the register in x86?
> 

| **Category** | **Register** | **Description** | **Note** |
| --- | --- | --- | --- |
| **General-Purpose (64-bit)** | `RAX` | Accumulator for arithmetic, return values | Aliases: `EAX` (32-bit), `AX` (16-bit), `AL`/`AH` (8-bit) |
|  | `RBX` | Base register, general use | Preserved across function calls (callee-saved) |
|  | `RCX` | Counter register | Used for loops, shift/rotate instructions |
|  | `RDX` | Data register | Used for I/O, multiplication/division, return values |
|  | `RSI` | Source index | Common for string operations, function argument |
|  | `RDI` | Destination index | String operations, function argument |
|  | `RBP` | Base pointer | Stack frame reference (callee-saved) |
|  | `RSP` | Stack pointer | Points to top of the stack (hardware managed) |
|  | `R8-R15` | Additional general-purpose | Used for additional arguments or computation (caller-saved) |
| **Segment Registers** | `CS` | Code segment selector | Usually fixed in modern flat memory mode |
|  | `DS` | Data segment selector | Default for data accesses |
|  | `ES` | Extra segment | Used for string and memory operations |
|  | `SS` | Stack segment | Stack accesses default here |
|  | `FS` / `GS` | Extra segments | Often used for thread-local storage |
| **Instruction Pointer** | `RIP` | Points to next instruction | Cannot be written directly in 64-bit mode (except via `jmp/call`) |
| **Flags / Status** | `RFLAGS` | Condition and status flags | CF, ZF, SF, OF, PF, etc.; affects conditional instructions |
| **Control Registers** | `CR0-CR4`, `CR8` | CPU control and system configuration | E.g., paging, protection modes, task switching |
| **Debug Registers** | `DR0-DR7` | Hardware breakpoints | Used for debugging |
| **Model-Specific / System** | `MSRs`, `XCR0` | CPU-specific configuration | Control extended features like AVX, SSE |
| **SIMD / Vector Registers** | `XMM0-XMM31` | 128/256/512-bit vector operations | Used for SSE, AVX, AVX-512 instructions |
|  | `YMM0-YMM31` | 256-bit AVX registers | Upper 128 bits of `XMM` included |
|  | `ZMM0-ZMM31` | 512-bit AVX-512 registers | Upper 256 bits of `YMM` included |
| **Floating Point Stack** | `ST0-ST7` | x87 FPU stack registers | 80-bit floating point; mostly legacy |
| **Mask Registers (AVX-512)** | `K0-K7` | Predicate/mask registers | Used for masked vector operations |

## Hardware Stack

> How the Hardware Stack Works in x86?
> 

## Stack Model

> The x86 stack model operates with the stack pointer (`%rsp`) growing downward in memory, where function calls use the `call` instruction to push the return address onto the stack, functions create stack frames by saving the previous base pointer (`%rbp`) with `push %rbp`, setting a new base pointer (`mov %rsp, %rbp`), allocating space for local variables (`sub $size, %rsp`), and restoring the stack frame by popping the base pointer (`pop %rbp`) and resetting the stack pointer (`mov %rbp, %rsp`) before returning with `ret`.
> 

### Calling Convention

| **Method/Model** | **Description** | **Common Architectures** |
| --- | --- | --- |
| **x86 Stack Discipline (System V ABI)** | The stack grows downward, and each function call pushes the return address onto the stack, followed by saving the caller's base pointer (`%rbp`), setting a new base pointer (`%rbp`), and allocating space for local variables. Stack unwinding restores `%rbp` and cleans up local space before returning with `ret`. | x86-32, x86-64 |
| **x86-64 System V ABI (64-bit)** | Similar to the x86-32 ABI but adapted for 64-bit. The return address is pushed by `call`, and each function has a stack frame where `%rbp` is saved and restored to maintain the call chain. Arguments are passed via registers (RDI, RSI, etc.) instead of the stack. | x86-64 |
| **x86-32 Calling Convention (cdecl)** | In this convention, arguments are pushed onto the stack in reverse order, and the caller cleans the stack after the function returns. Return values are passed in `%eax`, and the stack frame is manually managed using `%ebp` to mark the frame boundary. | x86-32 |
| **x86-64 Win64 ABI (Windows 64-bit)** | Arguments are passed in registers (RDI, RSI, etc.), with additional arguments pushed onto the stack. The function uses `push %rbp` to save the base pointer and `mov %rsp, %rbp` to set up a frame. Local variables are allocated using `sub $size, %rsp`. After returning, the base pointer is restored. | x86-64 |
| **ARM (AArch64) Function Call Model** | ARM architecture follows a **register-based** calling convention where arguments are passed via registers (`x0`-`x7`), and the return address is stored in the link register (`lr`). The stack is used for local variable storage, and the function prologue sets up space for these. | ARM64 (AArch64) |
| **MIPS Calling Convention** | MIPS uses the stack to store arguments and local variables. Arguments are passed in registers (`$a0`-$a3`), and the return value is stored in` $v0`. Functions use the stack for saving registers and allocating local variables in a frame. The return address is stored in` $ra`. | MIPS |
| **PowerPC Calling Convention** | Arguments are passed in registers (`r3`-`r10`) and the return address in the link register (`lr`). The function prologue and epilogue save and restore registers using the stack. A return address is stored in the link register for function return. | PowerPC |
| **SPARC Calling Convention** | SPARC uses the stack for storing arguments beyond the first six, and for saving registers. Arguments are passed in `%i0` to `%i5`, and the return address is stored in `%o7`. The function sets up a frame using `save` and cleans up with `restore`. | SPARC |
| **Calling Convention for RISC-V** | RISC-V uses registers for passing arguments (`a0`-`a7`), and return values are passed through `a0`-`a1`. The function prologue saves the return address (`ra`) and creates a stack frame with local variables, while the epilogue restores the stack pointer and returns. | RISC-V |

### Stack Frame

> A stack frame is created when the function uses the `call` instruction to push the return address onto the stack, then within the function's prologue, it pushes the caller's base pointer (`push %rbp`), sets the base pointer (`mov %rsp, %rbp`), allocates space for local variables (`sub $size, %rsp`), and finally, the epilogue restores the base pointer (`mov %rbp, %rsp`, `pop %rbp`) before returning with the `ret` instruction.
> 

## Stack Size

> On Linux, the **maximum stack size** for a process is determined by several layers of configuration:
> 

🧑‍⚖️ Who determines it?

1. **The OS kernel** — defines system-wide defaults and limits.
2. **The shell (`ulimit`)** — defines user/process-level soft and hard limits.
3. **Program headers (for threads)** — e.g., in `pthread_create`, you can specify stack size.
4. **System configuration files** — like `/etc/security/limits.conf`.

👷 Thread stack size (e.g., with pthreads)

> When creating a thread, the default stack size is **usually 8 MB** on 64-bit Linux.
> 

To set a different size:

```bash
pthread_attr_setstacksize(&attr, 1024 * 1024);  // 1 MB
```

Too small, and you'll get `EINVAL`.

## References

- [Linker](note.html?n=technica/computation/language-system/conceptual-model-language-system/linker.md)
- [Loader](note.html?n=technica/computation/language-system/conceptual-model-language-system/loader.md).
- [Evaluation Model](note.html?n=technica/computation/language-system/conceptual-model-language-system/evaluation-model.md)
- [Memory  Management](note.html?n=technica/computation/language-system/conceptual-model-language-system/memory-management.md)
- [Runtime Representation](note.html?n=technica/computation/language-system/conceptual-model-language-system/runtime-representation.md)
- x86: 🚀 Execution System
- [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md)
- 
- [Linux Process Management Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-process-management-stack.md)
- x86: 📜 Language Specification