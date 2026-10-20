---
tags: [clock]
---

# Clock


## **Computer Clock Cycle**

> A computer clock cycle is the basic unit of time in a processor, determining the pace at which a CPU executes instructions.
> 

### What is a Clock Cycle?

- The smallest unit of time in a processor's operation
- Determined by the processor's clock speed (measured in Hz)
- One complete oscillation of the processor's clock signal
- Each tick represents when transistor gates can change states

### How It Works

- Synchronizes all operations in the CPU
- Each operation (fetch, decode, execute, etc.) takes a certain number of cycles
- Modern processors use pipelining to execute multiple instructions simultaneously across different cycle stages

### Physical Limits and Challenges

1. **Transistor Switching Time**
    - Modern FinFET transistors: ~1 ps switching time
    - Quantum tunneling effects become significant below 0.5 ps
2. **Signal Propagation Limits**
    - Light travels ~0.3 mm in 1 ps (constraining chip design)
    - Transmission line effects dominate at picosecond scales
3. **Measurement Challenges**
    - Requires superconducting nanowire single-photon detectors
    - Cryogenic equipment for femtosecond measurements