# ROCm

> ROCm (Radeon Open Compute) is AMD's open-source platform designed to optimize GPU-accelerated computing across diverse applications, from high-performance computing to machine learning, by providing a comprehensive suite of tools, compilers, and libraries that enhance and simplify development on AMD GPUs.
> 

ROCm (Radeon Open Compute) provides a rich ecosystem of tools, libraries, and components designed to leverage AMD GPUs for high-performance computing, machine learning, and scientific applications. Here's a table summarizing some of the key components of the ROCm ecosystem:

| Component | Type | Description |
| --- | --- | --- |
| **HIP** | Tool | A C++ Runtime API and kernel language that allows developers to write portable code that runs on AMD and NVIDIA GPUs. |
| **HCC** | Compiler | A compiler for heterogeneous computing that allows execution of C++ code on both CPU and GPU. |
| **ROCm-dkms** | Driver | ROCm's kernel driver package, providing the base driver needed to run ROCm on compatible GPUs. |
| **ROCm Libraries** | Libraries | A collection of GPU-accelerated libraries optimized for AMD GPUs, including rocBLAS, rocFFT, rocRAND, and others. |
| **rocBLAS** | Library | Provides BLAS functionality on AMD GPUs. |
| **rocFFT** | Library | A library dedicated to fast Fourier transforms, optimized for AMD GPUs. |
| **rocRAND** | Library | Random number generation library optimized for AMD GPUs. |
| **MIOpen** | Library | A machine learning library that provides GPU-accelerated routines for deep neural networks. |
| **rocSPARSE** | Library | A library that provides sparse matrix operations on AMD GPUs. |
| **ROCm SMI** | Tool | ROCm System Management Interface, a tool for managing and monitoring ROCm compatible GPUs. |
| **rocProfiler** | Profiling Tool | A performance analysis tool for profiling ROCm applications to measure and analyze GPU performance. |
| **rocTracer** | Profiling Tool | A library providing precise, low-overhead API tracing for ROCm applications, enabling performance analysis. |

These components form the backbone of the ROCm platform, enabling high-performance, efficient, and scalable computing solutions on AMD GPUs. This robust toolkit supports various applications, making it a versatile choice for developers working in domains that require significant computational resources.

## Installation

- `lspci -k | grep -EA3 'VGA|3D|Display`
- `sudo apt install linux-generic-hwe-22.04`
- `amdgpu-install` `--opencl=rocr`
- `sudo dpkg -l | grep AMD`

## References

- [HIP Compiler: C++ Heterogeneous-Compute Interface for Portability](https://github.com/ROCm/HIP)
- [https://github.com/ROCm](https://github.com/ROCm)
- [https://github.com/ROCm/ROCm](https://github.com/ROCm/ROCm)
- [Radeon™ Software for Linux® Installation](https://amdgpu-install.readthedocs.io/en/latest/index.html)
- [https://github.com/torvalds/linux/tree/master/drivers/gpu/drm/amd/amdgpu](https://github.com/torvalds/linux/tree/master/drivers/gpu/drm/amd/amdgpu)
- The Last Time I Installed the Things / Give Me Errors with video output !!!