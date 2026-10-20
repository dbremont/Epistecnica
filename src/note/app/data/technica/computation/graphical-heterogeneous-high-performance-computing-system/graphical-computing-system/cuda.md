# CUDA

> CUDA (Compute Unified Device Architecture) is a **parallel computing platform(sdk/toolkit)** and **application programming interface (API)** model created by NVIDIA, allowing developers to use **NVIDIA GPUs** for general purpose processing to achieve dramatic increases in computing performance.
> 

> Breaking down the CUDA SDK into separate detailed tables for each part can provide a clearer view of its structure and functions.
> 

Here's a table describing the primary components of the **CUDA Toolkit**, which encompasses various tools, libraries, and resources essential for developers working with CUDA:

| **Component** | **Description** |
| --- | --- |
| **NVCC (Compiler)** | The NVIDIA CUDA Compiler compiles CUDA code for execution on NVIDIA GPUs. |
| **CUDA Libraries** | A set of optimized libraries such as cuBLAS, cuDNN, cuFFT, and others that provide accelerated routines. |
| **CUDA Runtime API** | An abstraction layer that simplifies device operations, memory management, and kernel launches. |
| **CUDA Driver API** | A lower-level API that offers more direct control over device initialization, context management, and program execution. |
| **NVIDIA Nsight** | An integrated development environment for application debugging and performance profiling. |
| **Visual Profiler** | A performance profiling tool that helps developers find bottlenecks in their CUDA applications. |
| **CUDA-GDB** | The NVIDIA tool for debugging CUDA applications running on Linux and Mac OS X. |
| **CUDA-MEMCHECK** | A suite of runtime tools to help check for errors in CUDA applications, similar to memcheck tools for CPU applications. |

This table provides an overview of the CUDA Toolkit, detailing the tools and resources available to developers for building and optimizing applications on NVIDIA GPUs.

## CUDA Runtime API

> An abstraction layer that simplifies device operations, memory management, and kernel launches.
> 
> 
> 
- Library: `libcudart.so`
- Header Files: **`cuda_runtime.h`,** `cuda_runtime_api.h, cuda.h`

## CUDA Driver API

> A lower-level API that offers more direct control over device initialization, context management, and program execution.
> 
- Library: `libcuda.so`
- Header Files: **`cuda.h`, `cuComplex.h`**

## **CUDA Libraries**

Here's a table that outlines some of the essential CUDA libraries provided by NVIDIA, which are part of the CUDA Toolkit. These libraries are optimized to run on NVIDIA GPUs and are designed to accelerate various computational tasks in different domains:

| **Library** | **Description** | **Use Cases** |
| --- | --- | --- |
| **cuBLAS** | Implements BLAS (Basic Linear Algebra Subprograms) functions using CUDA. | Linear algebra, matrix operations. |
| **cuFFT** | Provides fast Fourier Transform capabilities. | Signal processing, image analysis. |
| **cuDNN** | CUDA Deep Neural Network library is designed to accelerate deep learning frameworks. | Deep learning training and inference. |
| **cuSPARSE** | Provides a set of introductory linear algebra subroutines used for handling sparse matrices. | Graph analytics, computational physics. |
| **cuRAND** | Library for generating random numbers on the GPU. | Monte Carlo simulations, stochastic modeling. |
| **NVIDIA NPP** | NVIDIA Performance Primitives for image and video processing. | Video processing, image manipulation. |
| **cuSOLVER** | A collection of dense and sparse direct solvers and eigenvalue solvers. | Engineering simulations, computational mathematics. |
| **cuGRAPH** | Provides graph analytics capabilities that leverage the massive parallelism of GPUs. | Network optimization, social network analysis. |
| **NCCL** | NVIDIA Collective Communications Library is optimized for multi-GPU and multi-node communication. | Scaling deep learning across multiple GPUs and nodes. |

These libraries are designed to provide high-performance GPU-accelerated implementations of commonly used algorithms and functions, significantly reducing the time and effort required to develop complex, computationally intensive applications.

## References

- [Parallel Thread Execution](https://en.wikipedia.org/wiki/Parallel_Thread_Execution)
- [How CUDA Programming Works](https://www.nvidia.com/en-us/on-demand/session/gtcspring22-s41487/) ([nvidia.com](https://news.ycombinator.com/from?site=nvidia.com))
- [Unified Memory on Pascal and Volta](https://on-demand.gputechconf.com/gtc/2017/presentation/s7285-nikolay-sakharnykh-unified-memory-on-pascal-and-volta.pdf)
- [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html)
- [NVIDIA CUDA Compiler Driver NVCC](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html)
- George Hotz Nvidia
    - [George Hotz | Programming | aside: nvidia open source kernel driver | geohot/cuda_ioctl_sniffer](https://www.youtube.com/watch?v=oVUK1ychsb4)
    - [George Hotz | Programming | aside: a look into NVIDIA open source drivers | part2 cuda_ioctl_sniffer](https://www.youtube.com/watch?v=CE_72X3Wh_U)
    - [George Hotz | Programming | an open source CUDA userspace](https://www.youtube.com/watch?v=FGS6eivIVJI) | [github.com/geohot/cuda_ioctl_sniffer](http://github.com/geohot/cuda_ioctl_sniffer)
- [open-gpu-kernel-modules](https://github.com/NVIDIA/open-gpu-kernel-modules)
- [cuda_ioctl_sniffer](https://github.com/geohot/cuda_ioctl_sniffer)
- [CUDA Toolkit Documentation 12.4 Update](https://docs.nvidia.com/cuda/index.html)
- A few new CUDA hacker friends joined the effort and now llm.c is only 2X slower than PyTorch (fp32, forward pass) compared to 4 days ago, when it was at 4.2X slower 📈
[https://twitter.com/youraimarketer/status/1778992208697258152](https://twitter.com/youraimarketer/status/1778992208697258152)