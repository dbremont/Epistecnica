# Intel OpenCL

> Intel Implementation of OpenCL.
> 

QA:

- Intel Linux kernel DRM driver (`i915`)
- How to interpose ioctl?
- /lib/x86_64-linux-gnu ?
- **OpenCL ICD loader** (`libOpenCL.so`) → Load the ICD?

## Install

```bash
sudo lshw -c display
lsmod | grep i915
sudo apt install intel-opencl-icd ocl-icd-libopencl1 clinfo
clinfo | grep "OpenCL"
```

## Run

```bash
gcc main.c -lOpenCL -o vector
./vector
```

## Analysis

```bash
ldd vectorobj
strace ./vector
ltrace ./vector
readelf -a ./vector | grep NEE 
```

## **Layers in the Intel OpenCL Stack**

| Layer | Description |
| --- | --- |
| **OpenCL API (User app)** | Your OpenCL program written in OpenCL C or SPIR-V |
| **OpenCL runtime (Intel NEO)** | Intel's OpenCL driver & compiler stack for GPUs and CPUs |
| **LLVM-based compiler** | Compiles OpenCL C/SPIR-V to Intel Gen ISA (GPU machine code) |
| **Kernel driver (i915 DRM)** | Linux kernel driver that manages GPU hardware, command submission |
| **Hardware (Intel GPU)** | Execution Units (EUs), memory controllers, etc. |

## **Key Components**

| Component | Role |
| --- | --- |
| **Intel NEO Runtime** | OpenCL API implementation, kernel compiler & driver interface |
| **Intel Graphics Compiler (IGC)** | LLVM-based compiler generating GenISA |
| **Kernel Driver (i915 DRM)** | GPU resource management & command submission |
| **GPU Hardware** | Executes compiled GenISA kernels on SIMD EUs |

## **Compilation Pipeline**

> OpenCL C kernel | SPIR -V → LLVM IR → GenISA
> 

> Intel’s **IGC (Intel Graphics Compiler)** does the final translation.
> 

> GenISA is **not publicly documented in detail** but is partially reverse-engineered by projects like Mesa’s Intel driver.
> 

1. **OpenCL Program Source:** You write OpenCL kernels in OpenCL C (or SPIR-V).
2. **Frontend Compiler** Intel uses a **LLVM-based frontend** to parse OpenCL C or SPIR-V into LLVM IR.
3. **Optimization** LLVM performs optimizations specific to Intel GPU architecture.
4. **Backend Code Generation** LLVM backend (Intel Graphics Compiler - IGC) generates **GenISA assembly** — the native instruction set for Intel GPUs.
5. **Binary Packaging** GenISA instructions are packaged into a GPU kernel binary with metadata.
6. **Runtime Dispatch** The Intel OpenCL runtime loads the kernel binary, sets up GPU resources (buffers, textures), and submits commands via the **i915 DRM kernel driver**.

## **Runtime Execution**

- The OpenCL runtime:
    - Allocates device buffers and manages memory mapping.
    - Prepares command buffers containing kernel dispatch commands.
    - Submits command buffers to the kernel driver (via DRM ioctls).
    - Waits for kernel completion and handles events/synchronization.
- The **i915 kernel driver**:
    - Receives commands.
    - Manages GPU context switching and scheduling.
    - Executes kernels on the Execution Units (EUs).

## **Features**

- Supports **OpenCL 2.1** feature set on compatible GPUs.
- Supports:
    - Vectorized SIMD execution.
    - Shared local memory (SLM).
    - Event-based synchronization.
    - Image and sampler support.
    - Atomic operations.
- Optimized for Intel GPU microarchitecture (Gen9.5 for UHD 630).
- Supports CPU OpenCL runtime too, but GPU uses GenISA.

## IOCTL

Below is the approximate sequence:

### 1. `DRM_IOCTL_I915_GEM_CREATE`

- Allocates a GPU buffer (memory region).
- You use this to hold your kernel code (if using low-level submission) and input/output data.

### 2. `DRM_IOCTL_I915_GEM_MMAP`

- Maps the buffer into user-space for writing kernel code or data.

### 3. `DRM_IOCTL_I915_GEM_CONTEXT_CREATE[_EXT]`

- Creates a GPU execution context (engine config, isolation).

### 4. `DRM_IOCTL_I915_GEM_VM_CREATE`

- (Optional for modern platforms) Create a virtual address space (GPU-side).

### 5. **👉 `DRM_IOCTL_I915_GEM_EXECBUFFER2`**

- **Submits a command buffer to the GPU for execution.**
- The command buffer includes GPU instructions (e.g., GenISA, batch commands) that reference:
    - The kernel binary
    - Buffers (via relocations or virtual memory)
    - Thread dispatch and execution parameters

### 6. `DRM_IOCTL_I915_GEM_WAIT`

- Waits for the execution to complete (fence/sync object).

## **Tools**

- **clinfo**: Query OpenCL platform/device info.
- **Intel Graphics Performance Analyzers (GPA)**: GPU profiling and debugging.
- **intel-gpu-tools**: Command line tools for kernel driver debugging.
- **Intel VTune Profiler**: Performance and hotspot analysis (includes GPU support).

## References

- [- https://linux-hardware.org/?id=pci:8086-3e92-1043-8694
- https://github.com/intel/compute-runtime
- https://github.com/intel/intel-graphics-compiler/tree/master
- https://docs.mesa3d.org/systems.html
- https://en.wikipedia.org/wiki/Standard_Portable_Intermediate_Representation
- [‣](https://app.notion.com/p/b0a2a8d65e9d46d3b9ccfe1614c1bd73?pvs=21)
- [ELF (Executable and Linkable Format)](note.html?n=technica/computation/language-system/conceptual-model-language-system/elf-executable-and-linkable-format.md)
- [Guide to Observability Tools for C/C++ on Linux](https://app.notion.com/p/Guide-to-Observability-Tools-for-C-C-on-Linux-1c1c0f5171ec80ecabd2c048a1f861f5?pvs=21)
- [ltrace](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/ltrace.md)
- [strace](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/strace.md)
- [ioctl](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-syscall-interface/list-of-syscall/ioctl.md)
- https://github.com/KhronosGroup/SPIRV-LLVM-Translator
- https://clang.llvm.org/doxygen/group__CINDEX.html
- https://github.com/intel/intel-graphics-compiler
- https://github.com/intel/metrics-library
- https://man.archlinux.org/man/libOpenCL.7
- https://github.com/intel/compute-runtime/tree/master
- https://github.com/intel/gmmlib
- https://github.com/intel/metrics-discovery/blob/master/external/drm/i915_drm.h
- https://github.com/oneapi-src/level-zero
- [Linux Device Model](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/linux-device-model.md)
- https://wiki.archlinux.org/title/Intel_graphics