# OpenCL


> OpenCL (Open Computing Language) **is a standard**  that creates a  framework for writing programs that execute across heterogeneous platforms, including CPUs, GPUs, DSPs (Digital Signal Processors), and other processors.
> 

> Tensorflow you need the **OpenCL driver which isn't installed** by default unlike the OpenGL/Vulkan driver to display stuff .
> 

### **Architecture Overview**

> OpenCL defines a platform model that consists of a host (running on a CPU) and one or more compute devices (like GPUs or other processors). The host is responsible for managing the computing devices and dispatching computing tasks to them.
> 

### **Programming Model**

> OpenCL uses a programming model where the code is written in two parts:
> 
- **Host code** runs on the CPU and is responsible for setting up computing tasks, managing memory, and controlling computing devices.
- **Kernel code**: This is the code that runs on the compute devices. Kernels are functions written in a language based on C99, specifically designed for parallel execution.

### **Memory Model**

> OpenCL introduces a memory model that includes several memory spaces, such as global, local, and private memory, which are used differently depending on their access speed and sharing between processing units:
> 
- **Global Memory**: Accessible by all processing elements but has the slowest access speed.
- **Local Memory** is shared within a single workgroup (a group of processing elements) and is faster than global memory.
- **Private Memory**: Private to each processing element, very fast but limited in size.

### **Execution Model**

> The execution model in OpenCL organizes the execution of a kernel across a set of parallel compute units:
> 
- **Work Items are** the smallest execution units that execute kernels. Each work item is equivalent to a single instance of a kernel.
- **Work Groups**: These are collections of work items executed on a single computing unit and can share local memory.

### **Compilation and Execution**

- **Compilation**: Kernel code can be compiled at runtime from source code or loaded as pre-compiled binaries. This allows applications to compile kernel code specifically optimized for the target device.
- **Execution**: The host schedules kernels for execution on compute devices. It can manage the execution order and synchronization between kernels and memory operations.

### **API and Libraries**

> OpenCL provides an API for the host to interact with the compute devices. This includes functions for:
> 
- Querying devices and their capabilities.
- Allocating memory.
- Managing and scheduling the execution of kernels.
- Synchronizing operations.

## List of Implementations

> Here is a detailed table summarizing the OpenCL implementations available from critical vendors, highlighting the version support and specific features or considerations.
> 

> This overview can help developers choose the proper implementation for their hardware and software requirements.
> 

| Vendor | Implementation | Supported OpenCL Version | Key Features | Notes |
| --- | --- | --- | --- | --- |
| **AMD** | AMDGPU-PRO, ROCm | Up to OpenCL 2.2 | Supports AMD GPUs, CPU fallback, integrated into ROCm platform. | ROCm is AMD's open-source platform that also supports OpenCL. |
| **NVIDIA** | NVIDIA CUDA Toolkit | OpenCL 1.2, OpenCL 3.0 | Provides robust support for OpenCL via the CUDA platform. | While NVIDIA focuses more on CUDA, it still provides support for OpenCL. |
| **Intel** | Intel SDK for OpenCL | OpenCL 2.1, OpenCL 3.0 | Supports Intel CPUs, GPUs, and FPGAs. | Offers a comprehensive suite for developing on Intel devices. |
| **Apple** | Apple OpenCL | Up to OpenCL 1.2 | Integrated into macOS and iOS for legacy support. | Apple has deprecated OpenCL in favor of Metal for macOS and iOS. |
| **Qualcomm** | Qualcomm Adreno SDK | OpenCL 2.0 Full Profile | Optimized for mobile and embedded devices using Adreno GPUs. | Focused on mobile platforms, providing tools and libraries for OpenCL. |
| **ARM** | ARM Mali GPU OpenCL SDK | OpenCL 2.0 | Designed for ARM Mali GPUs, focusing on mobile devices. | Supports efficient computing on ARM-based devices. |
| **Mesa** | Clover | OpenCL 1.1 | Open-source implementation under the Mesa library. | Mainly for development and testing, not recommended for production. |
| **POCL** | Portable Computing Language (POCL) | OpenCL 1.2, partial 2.0 support | Portable and can run on various CPUs; uses LLVM for kernel compilation. | Aims to be an efficient and universal OpenCL implementation across all platforms. |

## Tools

Here's a table that outlines the primary tools, libraries, and header files associated with OpenCL development, which help developers utilize OpenCL for writing and executing programs across heterogeneous platforms:

| **Category** | **Components** | **Description** |
| --- | --- | --- |
| **Tools** | OpenCL SDKs (from vendors like Intel, AMD, NVIDIA) | Provide tools for developing and debugging OpenCL applications, including SDKs specific to vendor hardware. |
|  | OpenCL ICD Loader | A software component that allows applications to access multiple OpenCL platforms from different vendors. |
|  | CodeXL, Intel SDK for OpenCL Applications | Profiling and debugging tools that help optimize and analyze OpenCL code performance. |
| **Libraries** | clBLAS, clFFT, clMAGMA | Libraries that provide optimized OpenCL implementations of linear algebra and other mathematical operations. |
|  | OpenCV with OpenCL acceleration | A library for computer vision that can be accelerated using OpenCL for certain operations. |
| **Header Files** | `CL/cl.h` | The standard header file that includes all OpenCL data types and API functions. |
|  | `CL/cl_ext.h` | Provides extensions to the core OpenCL API, offered by various vendors for added functionality. |
| **Development Environments** | Various IDEs with OpenCL support | Integrated Development Environments (IDEs) that support OpenCL, such as Eclipse with OpenCL plugins. |

## References

- OpenCL
[https://en.wikipedia.org/wiki/OpenCL](https://en.wikipedia.org/wiki/OpenCL)
- [OpenGL vs. OpenCL, which to choose and why?](https://stackoverflow.com/questions/7907510/opengl-vs-opencl-which-to-choose-and-why)
- [OpenCL](https://www.khronos.org/opencl/)
- [Mesa (computer graphics)](https://en.wikipedia.org/wiki/Mesa_(computer_graphics))
- https://registry.khronos.org/OpenCL/specs/
- [https://registry.khronos.org/OpenCL/specs/2.2/pdf/OpenCL_API.pdf](https://registry.khronos.org/OpenCL/specs/2.2/pdf/OpenCL_API.pdf)