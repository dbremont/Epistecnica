---
tags: [code-generation, language-system]
---

# Just-in-time (JIT) Compilation

- [Bytecode Virtual Machine](note.html?n=technica/computation/language-system/conceptual-model-language-system/bytecode-virtual-machine.md)

> **Just-in-time (JIT) Compilation** is a dynamic translation technique that converts intermediate bytecode into native machine code at runtime, optimizing execution by leveraging runtime profiling, caching compiled code, and eliminating interpretation overhead.
> 

QA:

- How does the JIT-generated code interact with the VM `state and bytecode`? [How does the JIT-generated code interact with the VM `state and bytecode`?](note.html?n=technica/computation/language-system/conceptual-model-language-system/just-in-time-jit-compilation.md)
- …

## JIT Technique

> Just-in-Time (JIT) compilation is a key optimization technique used by modern runtime  nvironments and engines to improve the execution speed of programs. JIT compilers convert bytecode or intermediate representations into machine code during runtime, allowing for optimizations based on real-time execution data. Below is a summary of the core **JIT compilation techniques** used across various engines and platforms, highlighting their unique approaches to enhancing performance.
> 
> 
> ---
> 

| **JIT Technique** | **Description** | **Engine/Platform** |
| --- | --- | --- |
| **Tracing JIT** | Tracks execution paths and compiles frequently executed traces into machine code. | V8 (JavaScript) |
| **Method-based JIT** | Compiles individual methods from bytecode into native machine code. | HotSpot (Java) |
| **Inline Caching** | Optimizes repeated property lookups by caching the result of dynamic property accesses. | V8 (JavaScript) |
| **Intermediate Code Generation (IR)** | Compiles high-level code into intermediate representation (IR) first, optimizing and then generating machine code. | LLVM |
| **Dynamic Recompilation** | Compiles bytecode to machine code dynamically, with aggressive optimization and re-compilation. | LuaJIT |
| **Partial Evaluation** | Traces and evaluates code dynamically based on runtime behavior, generating optimized code. | PyPy (Python) |
| **Speculative JIT** | Optimizes code based on assumptions (e.g., types) and recompiles if assumptions are incorrect. | JavaScriptCore (Safari) |
| **Ahead-of-Time (AOT) + JIT** | Combines AOT compilation for initial speed with JIT for runtime profiling and optimizations. | GraalVM |

## Case Study

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <sys/mman.h>
#include <string.h>

#define MEM_SIZE 256
#define REG_COUNT 2
#define MAX_PROGRAM_SIZE 256

typedef enum {
    ADD = 0x01,
    SUB = 0x02,
    PRINT = 0x03,
    HALT = 0xFF
} Opcode;

typedef struct {
    uint8_t memory[MEM_SIZE];
    int registers[REG_COUNT];
    uint8_t code[MAX_PROGRAM_SIZE];
    int ip;
} VM;

void *create_executable_memory(size_t size) {
    return mmap(NULL, size, PROT_READ | PROT_WRITE | PROT_EXEC, 
                MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
}

// JIT compile ADD or SUB into machine code
typedef int (*jit_func)(int, int);

jit_func jit_compile_op(Opcode op) {
    uint8_t code[] = {
        0x55,                         // push   %rbp
        0x48, 0x89, 0xe5,             // mov    %rsp, %rbp
        0x89, 0xf8,                   // mov    %edi, %eax
        (op == ADD ? 0x01 : 0x29),     // add (%edx) or sub (%edx)
        0xd0,                          // eax = eax (op) edx
        0x5d,                          // pop    %rbp
        0xc3                           // ret
    };

    void *mem = create_executable_memory(sizeof(code));
    memcpy(mem, code, sizeof(code));
    return (jit_func)mem;
}

void run_vm(VM *vm) {
    jit_func jit_add = jit_compile_op(ADD);
    jit_func jit_sub = jit_compile_op(SUB);

    while (1) {
        uint8_t op = vm->code[vm->ip++];
        switch (op) {
            case ADD: {
                uint8_t r1 = vm->code[vm->ip++];
                uint8_t r2 = vm->code[vm->ip++];
                vm->registers[r1] = jit_add(vm->registers[r1], vm->registers[r2]);
                break;
            }
            case SUB: {
                uint8_t r1 = vm->code[vm->ip++];
                uint8_t r2 = vm->code[vm->ip++];
                vm->registers[r1] = jit_sub(vm->registers[r1], vm->registers[r2]);
                break;
            }
            case PRINT: {
                uint8_t r = vm->code[vm->ip++];
                printf("Reg[%d] = %d\n", r, vm->registers[r]);
                break;
            }
            case HALT:
                return;
        }
    }
}

void init_vm(VM *vm, uint8_t *program, size_t size) {
    memset(vm->memory, 0, MEM_SIZE);
    memset(vm->registers, 0, sizeof(vm->registers));
    vm->ip = 0;
    memcpy(vm->code, program, size);
}

int main() {
    VM vm;
    uint8_t program[] = {
        ADD, 0, 1,  // r0 = r0 + r1
        PRINT, 0,   // Print r0
        HALT        // Stop execution
    };

    vm.registers[0] = 10;
    vm.registers[1] = 20;

    init_vm(&vm, program, sizeof(program));
    run_vm(&vm);

    return 0;
}
```

## How does the JIT-generated code interact with the VM `state and bytecode`?

> The CPU state is synchronized with the VM state by mapping VM registers to physical registers or stack locations, ensuring that before invoking a JIT-compiled function, the VM saves necessary context (such as registers and stack pointers) and restores it upon return, while arguments and return values follow the platform’s calling convention for seamless execution.
> 

> See https://github.com/LuaDist/luajit/blob/master/src/lib_jit.c
> 

### 1. **Fetching and Decoding Bytecode**

- The JIT compiler monitors the execution of bytecode and identifies "hot" functions or loops that are executed frequently.
- Once a segment of bytecode is deemed worth optimizing, the JIT compiles it into native machine code.

### 2. **VM State Synchronization**

- The JIT-compiled code must maintain consistency with the VM state, including registers, stack, heap, and global variables.
- VM data structures such as the operand stack (in stack-based VMs) or registers (in register-based VMs) are mapped efficiently to CPU registers or memory.

### 3. **Optimizing Execution Paths**

- The JIT may inline frequently used functions, eliminate redundant computations, and reorder instructions for better CPU pipeline utilization.
- It may also introduce speculative optimizations, which assume certain execution conditions (e.g., type stability in dynamically typed languages).

### 4. **Handling Calls and Returns**

- Calls to other functions (both JIT-compiled and interpreted) require handling the transition between native code and the VM interpreter.
- Return addresses may need to be adjusted so that execution resumes correctly in the appropriate context.

### 5. **Safepoints and Deoptimization**

- The JIT must include safepoints—locations where execution can be paused to allow VM operations like garbage collection.
- If speculative optimizations prove incorrect (e.g., an assumption about variable type is violated), execution can revert to the interpreter through deoptimization.

### 6. **Exception Handling**

- JIT-generated code must properly integrate with the VM’s exception handling system.
- This includes setting up exception-handling tables, ensuring stack unwinding works correctly, and allowing the VM to regain control when an exception is thrown.

### 7. **Garbage Collection Integration**

- The JIT must ensure that object references in registers and stack locations are visible to the garbage collector.
- Some VMs use a shadow stack or write barriers to track references from JIT-compiled code.

### 8. **Interfacing with the Interpreter**

- Not all code is JIT-compiled; some functions may remain interpreted.
- Transitions between JIT-compiled code and the interpreter require mechanisms like trampolines, glue code, or inline caching.

## References

- [How to write a very simple JIT compiler](https://github.com/spencertipping/jit-tutorial)
- [A simple interpreter featuring a tracing JIT](https://github.com/namin/simple-tracing-jit)
- [How to JIT - an introduction](https://eli.thegreenplace.net/2013/11/05/how-to-jit-an-introduction)
- [Building An Efficient JIT the best kind of jit](https://llvm.org/devmtg/2008-08/Begeman_EfficientJIT.pdf)
- [Just-In-Time Compiler Library](https://www.gnu.org/software/libjit/doc/libjit.html)
- [libgccjit](https://gcc.gnu.org/onlinedocs/gcc-12.2.0/jit/index.html#)
- [Libgccjit.so: an embeddable JIT-compiler based on GCC](https://news.ycombinator.com/item?id=6488120)
- [A Brief History of Just-In-Time](http://eecs.ucf.edu/~dcm/Teaching/COT4810-Spring2011/Literature/JustInTimeCompilation.pdf)
- [Just-in-time Compilation Techniques](https://wiki.aalto.fi/download/attachments/40010375/intro-report.pdf)
- [Getting started with libjit - part 1](https://eli.thegreenplace.net/2013/10/17/getting-started-with-libjit-part-1)
- [awesome-jit](https://github.com/wdv4758h/awesome-jit)
- [Re: Lazy JIT IR code generation to increase JIT speed with partitions](https://mail.google.com/mail/u/0/popout?ver=233og3h6h7x7&search=inbox&th=%23thread-f%3A1751047640390109158&cvid=1)
- https://github.com/namin/simple-tracing-jit