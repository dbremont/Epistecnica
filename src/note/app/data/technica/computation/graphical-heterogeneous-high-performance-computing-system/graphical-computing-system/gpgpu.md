# GPGPU

> **General-purpose computing on graphics processing units** **(GPGPU)** allows GPU hardware acceleration for tasks other than graphics rendering, such as computations in scientific research, data analysis, and machine learning.
> 

> Here's a table comparing several major GPGPU APIs, outlining their main characteristics and use cases:
> 

`sudo lshw -C display`

| API | Developer | Supported Languages | Key Features | Use Cases |
| --- | --- | --- | --- | --- |
| **CUDA** | NVIDIA | C, C++, Python | Integrates closely with NVIDIA hardware, comprehensive libraries and tools | High-performance computing, deep learning, scientific simulations |
| **OpenCL** | Khronos Group | C, C++, Python | Cross-platform, supports multiple vendors' GPUs and other processors | Portable applications across various hardware platforms |
| **DirectCompute** | Microsoft | HLSL | Integrated into DirectX, it utilizes shaders for computation | Games, Windows applications requiring GPGPU |
| **Metal Compute** | Apple | Metal Shading Language | Optimized for Apple hardware, low-overhead architecture | iOS and macOS applications, including graphics and compute intensive tasks |
| **Vulkan Compute** | Khronos Group | GLSL, HLSL | Modern API with cross-platform capabilities, part of the larger Vulkan graphics and compute ecosystem. | Next-generation graphics and compute applications, cross-platform development |
| **OpenGL Compute Shaders** | Multiple | GLSL | Works alongside traditional OpenGL, easy integration with existing graphics pipelines | Applications that mix graphics and compute but don’t require advanced features of Vulkan |
| **ROCm** | AMD |  | ROCm, or Radeon Open Compute, is an open-source platform designed by AMD to enhance GPU computing by providing a rich set of tools to develop high-performance applications and accelerate processing in a heterogeneous computing environment. |  |
| **OpenGL** |  |  | OpenGL (Open Graphics Library) is a cross-platform, open-source API for rendering 2D and 3D vector graphics. It is often utilized in applications where performance and visual quality are critical, such as video games and simulations. |  |
| **WebGL** |  |  |  |  |

## Compute Kernel

> A **compute kernel** is a fundamental unit of computation in parallel processing frameworks, designed to perform specific tasks or operations on data, often executed concurrently across multiple processing units.
> 

## References

- [General-purpose computing on graphics processing units (gpgpu](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units))
- [GPU Programming, CUDA or OpenCL or? [closed]](https://stackoverflow.com/questions/72204231/gpu-programming-cuda-or-opencl-or)
- [Demystifying GPU Compute Software](https://thechipletter.substack.com/p/demystifying-gpu-compute-software)
- Cuda, or OpenCL?
[https://www.reddit.com/r/GraphicsProgramming/comments/xk2w0s/cuda_or_opencl/](https://www.reddit.com/r/GraphicsProgramming/comments/xk2w0s/cuda_or_opencl/)
- https://en.wikipedia.org/wiki/Compute_kernel
- [GPU](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/gpu.md)