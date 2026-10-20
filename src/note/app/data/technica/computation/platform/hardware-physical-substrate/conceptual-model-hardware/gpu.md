# GPU


> **GPU Computation** refers to the process of using **Graphics Processing Units (GPUs)** to perform general purpose scientific and **engineering computations** more efficiently than traditional CPUs, particularly by exploiting their parallel processing capabilities.
> 

QA:

- How to monitor code executing in GPUs?

## Components

| **Component** | **Description** |
| --- | --- |
| **GPU Chip (Die)** | The central processor of the card; executes shaders, rendering, and compute workloads in parallel. |
| **VRAM (Video RAM)** | High-speed memory (usually GDDR6, GDDR6X, HBM2) used to store textures, framebuffers, shaders, etc. |
| **VRAM Controller / Memory Interface** | Manages communication between GPU and VRAM with high bandwidth and low latency. |
| **Shader Cores / ALUs** | SIMD units that execute shader programs (vertex, pixel, geometry, compute shaders). |
| **Texture Mapping Units (TMUs)** | Handle texture sampling, filtering, and addressing. |
| **Render Output Units (ROPs)** | Perform final pixel operations like blending, anti-aliasing, and writing to the framebuffer. |
| **Display Engine** | Converts framebuffer content to output protocols (e.g., HDMI, DisplayPort) for monitors. |
| **PCIe Interface** | Connects the GPU to the CPU/motherboard over the PCI Express bus. |
| **Voltage Regulation Module (VRM)** | Power delivery system that converts and regulates voltage to the GPU and VRAM. |
| **Cooling System (Fans / Heatsinks)** | Maintains thermal stability through air or liquid cooling. |
| **BIOS / Firmware ROM** | Contains low-level code to initialize and configure the GPU at boot time. |
| **Power Connectors** | External power (e.g., 6/8/12-pin PCIe connectors) for high-performance cards. |
| **Backplate / PCB** | Structural and electrical platform that connects all components; includes multi-layer traces. |

## Chip Structure

| **Sub-Component** | **Function** |
| --- | --- |
| **SM / CU (Streaming Multiprocessor / Compute Unit)** | Groups of shader cores that execute threads in parallel. |
| **Instruction Cache** | Stores decoded instructions close to the compute units for speed. |
| **Register File** | High-speed internal memory for thread-local variables. |
| **L1 Cache / Shared Memory** | Fast low-level cache for intra-kernel thread collaboration. |
| **L2 Cache** | Larger cache for memory transactions shared across SMs. |
| **Scheduler / Warp Dispatcher** | Distributes threads and manages execution pipelines. |
| **Command Processor** | Parses and dispatches commands from the CPU/driver (draw calls, compute dispatches, etc.). |
| **Geometry / Raster Engine** | Transforms geometry and rasterizes primitives into pixels/fragments. |
| **Video Decoder / Encoder (NVDEC/NVENC, VCN)** | Hardware blocks for accelerating video decoding and encoding. |

## Software Stack

| **Layer** | **Function** | **Case Studies** | **Vendors** |
| --- | --- | --- | --- |
| **Application Layer** | High-level apps that request rendering or compute | Games, TensorFlow, Blender, PyTorch, OBS, MATLAB | All |
| **High-Level APIs** | Frameworks abstracting GPU access | Unreal Engine, Unity, WebGL, WebGPU, OpenCV, TensorRT | Varies (vendor backend required) |
| **Graphics APIs** | 2D/3D rendering, shader pipelines | OpenGL, Vulkan, Direct3D, Metal, WebGPU | NVIDIA, AMD, Intel, Apple |
| **Compute APIs** | GPGPU computing, general-purpose parallel tasks | CUDA, OpenCL, ROCm/HIP, Vulkan Compute, DirectCompute | CUDA (NVIDIA), ROCm (AMD), OpenCL (All) |
| **Shader Languages / IRs** | GPU programs for rendering and compute | GLSL, HLSL, SPIR-V, PTX, SASS, Metal SL, WGSL | Depends on stack (e.g., PTX = NVIDIA) |
| **Runtime Libraries** | Provide API implementations, JIT compilers, memory mgmt | libGL, libvulkan, nvcuda, OpenCL runtime, hipruntime | Vendor-provided or Mesa OSS |
| **Driver Interface Layer** | Converts API/IR to hardware ops | Mesa Gallium, NVIDIA proprietary stack, AMDGPU LLVM backend | Vendor-specific or open source |
| **Kernel Driver (KMD)** | Manages hardware access, scheduling, memory protection | NVIDIA kernel module, AMDGPU, i915, Nouveau, KFD (ROCm) | NVIDIA, AMD, Intel |
| **Firmware / Microcode** | Initializes GPU and controls hardware-level features | VBIOS, GSP (NVIDIA), PSP (AMD), firmware blobs | Vendor-supplied |
| **Hardware (GPU)** | Executes instructions on shader cores, TMUs, encoders, etc. | GeForce, Radeon, Arc, Mali, Adreno | NVIDIA, AMD, Intel, ARM, Qualcomm |

## Comparison

| **Aspect** | **MESA** | **CUDA** | **ROCm** | **OpenCL** | **Vulkan** |
| --- | --- | --- | --- | --- | --- |
| **Developer Origin** | OSS Community + Intel/AMD | NVIDIA | AMD | Khronos Group | Khronos Group |
| **Open Source?** | ✅ Fully open | ❌ Proprietary | ✅ Mostly open | ✅ (spec) / ❌ (many impls) | ✅ (spec) / ❌ (some impls) |
| **Target Hardware** | Intel, AMD, NVIDIA (via Nouveau), ARM | NVIDIA GPUs only | AMD GPUs (RDNA, GCN) | Intel, AMD, NVIDIA, ARM, etc. | Intel, AMD, NVIDIA, mobile GPUs |
| **Main Purpose** | Graphics (OpenGL/Vulkan), limited compute | High-performance compute (GPGPU) | GPGPU (via HIP/OpenCL) | General-purpose GPU compute | Graphics + Compute (modern, low-level) |
| **Compute Capability** | ⚠️ Limited (OpenCL via Clover, Vulkan compute) | ✅ Full | ✅ Full | ✅ Full | ✅ Full (Vulkan Compute Shaders) |
| **Shader / Kernel Language** | GLSL, SPIR-V | CUDA C++, PTX | HIP, OpenCL C, LLVM IR | OpenCL C / C++ | GLSL / HLSL → SPIR-V |
| **Compiler Infrastructure** | NIR, TGSI, LLVM IR (AMD) | NVCC (closed), PTX JIT | LLVM-based, clang, llc | LLVM-based (AMD, Intel), SPIR-V optional | SPIR-V with validation layers, glslang, etc. |
| **Low-Level ISA Access** | Partial (e.g., GCN via LLVM, NVC0 via rev-eng) | PTX (IR), SASS (unofficial) | ✅ GCN via LLVM | ❌ Abstracted by vendors | ⚠️ Some via SPIR-V → Driver |
| **PTX Support** | ❌ | ✅ Native | ❌ | ❌ | ❌ |
| **LLVM-Based?** | ✅ Many drivers (RadeonSI, RADV) | ❌ | ✅ Fully | ✅ (in many backends) | ❌ (but uses external LLVM tools in tooling) |
| **Runtime API** | OpenGL/Vulkan | CUDA Driver API / Runtime API | HIP Runtime API, OpenCL Runtime | OpenCL C API | Vulkan API (low-level) |
| **Kernel Mode Driver** | DRM / KMS | Proprietary NVIDIA kernel module | AMDGPU + ROCk | Depends on vendor | DRM (Linux), WDDM (Windows), vendor kernel |
| **Debugging Tools** | shader-db, Mesa tools | cuda-gdb, Nsight | roc-gdb, rocminfo | Intel VTune, clinfo, CodeXL, gdb extensions | RenderDoc, validation layers |
| **Use in Scientific Compute** | ❌ Experimental | ✅ Industry-standard | ✅ Growing in HPC | ✅ Widely used in research/HPC | ⚠️ Niche (used in graphics-first pipelines) |
| **Control Granularity** | Medium (high in Mesa RADV) | High | High | Medium | ✅ Very High (explicit resource/sync) |
| **Industry Maturity** | ✅ High (for graphics) | ✅ Very High | ⚠️ Medium (HPC niches) | ✅ Very High (portable standard) | ✅ Increasing rapidly |
| **Cross-Platform?** | ✅ (Linux, BSD) | ❌ Mostly Linux + Windows | ⚠️ Linux-only (officially) | ✅ Broad (Windows, Linux, macOS, mobile, FPGAs) | ✅ Broad (Windows, Linux, Android) |

## References

- [GPU Programming: When, Why and How?](https://news.ycombinator.com/item?id=36385938) ([enccs.github.io](http://enccs.github.io/))
- [WebGPU — All of the cores, none of the canvas](https://surma.dev/things/webgpu/)
- [Introducing Triton: Open-source GPU programming for neural networks](https://openai.com/research/triton)
- [How a GPU Works](https://www.cs.cmu.edu/afs/cs/academic/class/15462-f11/www/lec_slides/lec19.pdf)
- George Hotz | Exploring | finding exploits in AMD's GPU firmware | Giving up on AMD for the tinybox
[https://www.youtube.com/watch?v=6fFUfyT-EyA&t=333s](https://www.youtube.com/watch?v=6fFUfyT-EyA&t=333s)
- 7900xtx
[https://github.com/geohot/7900xtx?tab=readme-ov-file](https://github.com/geohot/7900xtx?tab=readme-ov-file)
- umr
[https://www.mankier.com/1/umr](https://www.mankier.com/1/umr)
- [Khronos Group](https://en.wikipedia.org/wiki/Khronos_Group)
- https://damek.github.io/random/basic-facts-about-gpus/
- [**DRM (Direct Rendering Manager)**](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-multimedia-stack.md)
- [OpenCL](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/opencl.md)
- https://github.com/jalexine/gpucodes