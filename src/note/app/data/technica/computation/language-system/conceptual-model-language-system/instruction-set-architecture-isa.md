---
tags: [instruction-set-architecture, language]
---

# Instruction Set Architecture (ISA)


> The **Instruction Set Architecture (ISA)** is the formal, abstract interface between software and hardware that defines how a processor behaves from the point of view of machine code.
It specifies what the hardware must do, not how it is implemented.
> 

## Structure

| **Component** | **Description** |
| --- | --- |
| **Instruction Set** | Defines the operations the CPU can perform (e.g., arithmetic, logical, control flow) and their binary encoding and formats. |
| **Architectural State** | The set of programmer-visible storage elements, including general-purpose registers, floating-point/vector registers, program counter, and flags. |
| **Memory & Addressing Model** | Specifies memory organization, address size, endianness, alignment rules, virtual memory abstraction, and addressing modes for instructions. |
| **Exception & Interrupt Model** | Defines types of exceptions and interrupts, how they are delivered, and the required changes to the architectural state. |
| **Privilege Levels & Protection** | Defines user vs kernel modes, access control rules, and behavior of privileged instructions. |
| **Calling Conventions (ABI)** | (Optional/Extended) Specifies stack layout, register usage, and function call semantics for software interoperability. |

## Case Study

| **Feature** | **x86** | **ARM** | **MIPS** | **RISC-V** | **PowerPC** |
| --- | --- | --- | --- | --- | --- |
| **Type** | CISC (Complex Instruction Set Computing) | RISC (Reduced Instruction Set Computing) | RISC | RISC | RISC |
| **Main Usage** | Desktop PCs, Servers, Laptops, Embedded Systems | Mobile Devices, Embedded Systems, IoT | Embedded Systems, Networking | Embedded Systems, IoT, Custom Processors | Embedded Systems, Servers, Consoles |
| **Instruction Set Complexity** | Complex instructions with variable lengths | Simple, fixed-length instructions | Fixed-length, simple instructions | Fixed-length, simple instructions | Fixed-length, simple instructions |
| **Addressing Modes** | Extensive (Registers, Memory, Immediate) | Limited (Mostly Register and Immediate) | Limited (Mostly Register) | Limited (Mostly Register) | Limited (Mostly Register) |
| **Pipeline** | Deep pipeline (Multiple stages) | Simple pipeline (More stages with more registers) | Simple pipeline (Efficient) | Simple pipeline (Highly customizable) | Deep pipeline (Similar to RISC) |
| **Endianness** | Little-endian (Mostly) | Little-endian (Typically) | Bi-endian (Both little and big) | Bi-endian (Both little and big) | Bi-endian (Both little and big) |
| **Registers** | 8 General-purpose, many special registers | 16-31 General-purpose registers | 32 General-purpose registers | 32-64 General-purpose registers | 32-64 General-purpose registers |
| **Instruction Length** | Variable (1–15 bytes) | Fixed (32 bits) | Fixed (32 bits) | Fixed (32 bits) | Fixed (32 bits) |
| **Support for SIMD Extensions** | MMX, SSE, AVX, etc. | NEON | MDMX | Customizable extensions (e.g., SIMD) | AltiVec |
| **Performance/Power Efficiency** | Power-hungry (High performance) | Very power-efficient | Moderate power efficiency | Highly power-efficient | Moderate power efficiency |
| **Popular Implementations** | Intel, AMD | Qualcomm, Apple, ARM Holdings | Broadcom, Cisco, MIPS Computer Systems | SiFive, Western Digital | IBM, Freescale |
| **Instruction Set Customizability** | Limited (Fixed instruction set) | Some customization (ARMv8, ARMv9) | No custom instructions | Highly customizable (Open-source) | Limited (e.g., Altivec for SIMD) |
| **Licensing** | Proprietary (Intel, AMD) | Proprietary (ARM Holdings) | Open (MIPS Technologies) | Open-source (RISC-V Foundation) | Proprietary (IBM) |
| **Popular Use in Servers** | Very common (Intel Xeon, AMD EPYC) | Rare (ARM servers are growing) | Rare (Used in some network devices) | Growing (Data centers using RISC-V) | Somewhat common (IBM Power series) |
| **Backward Compatibility** | High (x86, x86-64) | Limited (ARMv7 to ARMv8) | Limited (MIPS32, MIPS64) | No direct backward compatibility | High (PowerPC to PPC64) |

## References

- https://github.com/dbremont/isa-labs
- https://en.wikipedia.org/wiki/Instruction_set_architecture
- https://en.wikipedia.org/wiki/Comparison_of_instruction_set_architectures