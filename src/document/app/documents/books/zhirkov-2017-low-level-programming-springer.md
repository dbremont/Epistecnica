---
tags: [physical]
---

# Zhirkov, I. (2017). Low-Level Programming. Springer.


```python
@book{zhirkov2017low,
  title={Low-Level Programming},
  author={Zhirkov, Igor},
  year={2017},
  publisher={Springer}
}
```

## Notes

---

> Note: This book covers only the Intel 64 Architecture.
> 

## Index

## Assembly Language and Computer Architecture

### Basic Computer Architecture

> The term **“Model  of Computation”** is defined as the set of primitive “operations → computation” and their cost.
> 

> The term **“Model  of Computation”** will also be used to denote “an abstract machine” - that is a model of a computer - what is can do and how does it do it. - This will not be treated in this book.
> 

> Von Newman Architecture: A computational architecture in which **program instructions and data share the same memory space**, are represented in the same addressable format, and are fetched sequentially through a unified bus. The CPU operates using a **fetch–decode–execute cycle**, retrieving both instructions and operands from main memory, which creates the characteristic **Von Neumann bottleneck**: system throughput is constrained by the bandwidth of the memory–CPU channel.
> 

![image.png](documents/books/zhirkov-2017-low-level-programming-springer/image.png)

> The **assembly language** for a given processor is a set of mnemonics that correspond to the machine code — the binary-encoded instructions executed by the hardware.
> 

**Intel 64 Architecture**

> Aka **Intel 64 System Model.**
> 

| **Category** | **Part** | **Description** |
| --- | --- | --- |
| **Execution Core** | General-Purpose Registers (GPRs) | RAX, RBX, RCX, RDX, RSI, RDI, RBP, RSP, R8–R15; integer arithmetic, pointers, stack, calling conventions. |
|  | Instruction Pointer (RIP) | Address of the next instruction to execute; updated automatically by control-flow instructions. |
|  | RFLAGS | Condition codes (ZF, CF, OF…), control bits, system flags. |
|  | SIMD/Vector Registers | XMM0–31, YMM0–31, ZMM0–31 for SSE/AVX/AVX-512 floating-point & vector operations. |
|  | Floating-Point Stack (x87 FPU) | Eight 80-bit FP registers in stack form; legacy but still architecturally present. |
|  | Segment Registers | CS, DS, ES, SS, FS, GS; hold segment base/cache; mostly flat in 64-bit mode except FS/GS base. |
| **Control & Privilege** | Control Registers | CR0/CR2/CR3/CR4/CR8; enable paging, protection, system features, TLB behavior. |
|  | Model-Specific Registers (MSRs) | Per-core configuration registers for APIC, power, performance monitoring, syscall, etc. |
|  | Privilege Levels (Rings) | Four privilege rings (0–3); OS kernel in ring 0, user apps in ring 3. |
|  | System Call Interface | SYSCALL/SYSRET, SYSENTER/SYSEXIT; transitions between user and kernel mode. |
| **Interrupts & Exceptions** | Interrupt Descriptor Table (IDT) | Table of gate descriptors for hardware interrupts, traps, faults, NMIs. |
|  | APIC / x2APIC | Local APIC + IOAPIC for interrupt routing, timers, IPI, vector assignment. |
|  | Fault Handling | Page faults, GP faults, protection faults, FP exceptions, debug traps. |
|  | Debug State | DR0–DR7 registers; breakpoints and single-step state. |
| **Memory System** | Virtual Memory | 4-level or 5-level paging (PML4/PDPT/PD/PT); 48–57-bit virtual addresses. |
|  | Page Tables | Hierarchical translation structures referenced by CR3; cached in TLB. |
|  | Hardware Stack | Stack pointer (RSP), call/return operations, red zone, shadow stack (CET). |
|  | Memory Protection | Paging, supervisor/user bits, NX bit, memory-type boundaries. |
| **Translation & Coherency** | TLB (Translation Lookaside Buffer) | Caches virtual→physical translations; separate L1 DTLB, ITLB, unified L2 TLB. |
|  | Memory Ordering | TSO (Total Store Order) with fences (LFENCE, SFENCE, MFENCE); reordering rules. |
|  | Cache Coherency Protocol | MESI/MOESI implemented in hardware across cores. |
|  | Paging & EPT | Hardware-assisted virtualization (Extended Page Tables) for VMs. |
| **Cache Hierarchy** | L1 Caches | Per-core: L1I (instructions), L1D (data), lowest latency. |
|  | L2 Cache | Private per core; larger, slower than L1. |
|  | L3 Cache | Shared among cores; last-level cache (LLC). |
|  | Cache Line | Fundamental unit of coherency and movement (typically 64 bytes). |
| **Branching & Speculation** | Branch Predictor | BTB, BPU, indirect predictors; reduce control hazards. |
|  | Speculative Execution | Execution before resolution of branches/memory dependencies. |
|  | Reorder Buffer (ROB) | Tracks speculative instructions for in-order retirement. |
|  | Micro-Op Cache | Caches decoded µops to bypass instruction decode. |
| **Microarchitecture Pipeline** | Fetch Unit | Retrieves instructions (speculatively). |
|  | Decode Unit | Decodes complex x86 instructions into µops. |
|  | Reservation Stations | Dispatching and scheduling of µops to execution units. |
|  | Execution Units | ALUs, FPUs, vector units, AGUs, crypto units, etc. |
|  | Retirement Unit | Commits architectural state after speculation clears. |
| **System & Power** | Power Management | C-states, P-states; turbo boost control. |
|  | Performance Monitoring | PMCs, PEBS, LBRs; used by profilers (perf, VTune, Tracy). |
|  | RDT / QoS | Resource partitioning of caches and memory bandwidth. |

### Assembly Language

### Legacy

### Virtual Memory

### Compilation Pipeline

### Interrupts and Systems Calls

### Models of Computation

## The C Programming Language

### Basics

### Type System

### Code Structure

### Memory

### Syntax, Semantics, and Pragmatics

### Good Code Practices

## Between C and Assembly

### Translation Details

### Shared Objects and Code Models

### Performance

### Multithreading

## Appendices

### Using GDB

### Using Make

### System Calls

### Performance Test Information

## References

- …
