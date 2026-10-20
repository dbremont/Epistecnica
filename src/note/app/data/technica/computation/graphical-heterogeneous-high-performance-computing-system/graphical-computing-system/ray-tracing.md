# Ray Tracing

> **Ray tracing** is a rendering technique that simulates the way light interacts with objects by tracing the paths of rays to produce realistic lighting, shadows, and reflections.
> 

## **Real-Time Ray Tracing**

> **Real-Time Ray Tracing** refers to the computational process of performing **ray tracing algorithms fast enough** to maintain **interactive frame rates (≥30 FPS)**, typically for **graphics rendering in dynamic environments**, using **hardware acceleration** and **algorithmic optimizations**.
> 

> **Real-time ray tracing** is a rendering technique that computes the color of pixels by simulating the physical behavior of light rays as they interact with scene geometry (e.g., reflection, refraction, shadows, global illumination) in a time-constrained environment.
> 

This is achieved using:

1. **Ray Generation**: A ray is cast from a virtual camera through each pixel into the scene.
2. **Ray-Scene Intersection Testing**: Efficient spatial data structures such as **Bounding Volume Hierarchies (BVH)** or **Kd-trees** are used to find the first geometry hit by each ray.
3. **Shading**: Once a hit is detected, material properties are applied using physically-based rendering (PBR) models (e.g., Cook-Torrance BRDF).
4. **Recursive Ray Spawning**: Rays are spawned for reflection, refraction, and sometimes shadow testing (e.g., next-event estimation).
5. **Temporal Constraints**: The above steps must be completed within a tight time budget (~16.7ms per frame for 60 FPS), requiring:
    - **GPU hardware acceleration** (e.g., NVIDIA RTX, AMD Ray Accelerators, DirectX Raytracing (DXR), Vulkan RT).
    - **Denoising techniques** (e.g., AI-based or SVGF) to approximate global effects from limited ray samples.
    - **Hybrid rendering architectures** that combine rasterization and ray tracing (e.g., ray-traced shadows or reflections only).

## References

- https://en.wikipedia.org/wiki/Ray_tracing_(graphics)