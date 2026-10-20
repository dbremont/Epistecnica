# Rendering

> **Rendering** is the computational process of converting **scene data** (geometry, lighting, materials, textures, and camera) into a **raster image or pixel values**, using mathematical models of **light transport**, **projection**, and **shading**.
> 

> `[ Scene ] → [ Geometry Processing ] → [ Rendering ] → [ Image ]`
> 

## Taxonomy

| **Dimension** | **Category** | **Description** | **Instance(s)** | **Typical Use Cases** |
| --- | --- | --- | --- | --- |
| **Rendering Architecture** | Rasterization | Geometry projected & filled as pixels | OpenGL, DirectX, WebGL, Metal | Real-time 3D games, UI rendering |
|  | Ray-Based | Trace rays per pixel for visibility & lighting | Ray Tracing (RTX, Vulkan RT), OptiX | Film, VFX, accurate lighting |
|  | Hybrid | Combination of rasterization & ray tracing | Unreal Engine 5, RTX Hybrid | Realistic real-time rendering |
|  | Compute-Based | GPGPU compute shaders for full control over rendering | OpenGL Compute Shader, Vulkan Compute | Procedural generation, simulations |
| **Illumination Model** | Local Illumination | Light interaction at surface point only | Phong, Blinn-Phong | Games, interactive applications |
|  | Global Illumination | Simulate inter-surface light transport | Path Tracing, Radiosity | Offline rendering, architectural viz |
|  | Screen-Space Effects | Approximate global effects using screen data | SSAO, SSR, Screen-Space GI | Real-time effects in games |
|  | Image-Based Lighting | Environment maps to simulate complex lighting | IBL, HDR Environment Maps | Realistic reflections and lighting |
| **Geometry Representation** | Mesh-Based | Triangle or polygon meshes | Traditional 3D models | Games, CAD, VR |
|  | Voxel-Based | 3D grid-based volumetric data | Minecraft, medical imaging | Volume rendering, voxel engines |
|  | Point-Based | Point clouds or surfels | LIDAR scans, particle systems | Scientific visualization, effects |
|  | Implicit Surfaces | Geometry defined by functions (SDFs, metaballs) | Raymarching SDFs | Stylized rendering, volumetrics |
|  | Image-Based Geometry | No explicit geometry; generated in shaders | Fullscreen quad shaders | Post-processing, raymarching |
| **Shading Strategy** | Forward Shading | Lighting computed during geometry pass | Classic OpenGL, mobile engines | Simple scenes, mobile apps |
|  | Deferred Shading | Geometry pass separates lighting pass | Unreal Engine, custom OpenGL pipelines | Many dynamic lights |
|  | Tiled/Clustered Shading | Divide screen into tiles/clusters for efficient lighting | Frostbite engine, Unity HDRP | Large scenes, VR |
|  | Path-Based Shading | Recursive light simulation per pixel | Path tracers like Cycles, Arnold | Offline photorealistic renders |
| **Computation Method** | Fixed-Function | Predefined pipeline stages with limited programmability | OpenGL 1.x, DirectX 9 | Legacy applications |
|  | Shader-Based | Programmable pipeline stages | OpenGL 3+, Vulkan, WebGL | Modern real-time graphics |
|  | Compute Shader | General-purpose GPU computation | OpenGL 4.3+, Vulkan | Simulation, procedural content |
|  | Multi-pass / Post FX | Multiple rendering passes combined | Bloom, Depth of Field, Tone mapping | Complex visual effects |
| **Rendering Purpose** | Real-Time | High frame rate, interactive | Games, simulators | Interactive graphics |
|  | Offline / High Quality | Time-consuming, high fidelity | Film VFX, architectural renderers | Movie production, product design |
|  | Stylized / NPR | Artistic, non-photorealistic rendering | Toon shading, cel shading | Animation, comics, stylized games |
|  | Scientific / Analytical | Emphasizes data accuracy or structure | Medical imaging, volume rendering | Scientific visualization |

## Structure

| **Component** | **Role** |
| --- | --- |
| **Geometry** | Objects in the scene (meshes, points, etc.) |
| **Materials** | Surface properties (color, roughness, etc.) |
| **Lighting** | Light sources that illuminate the scene |
| **Camera** | Defines the viewpoint and projection |
| **Shaders** | Programs that compute pixel or vertex attributes |
| **Rendering Algorithm** | The method (rasterization, ray tracing, etc.) used to compute the final image |

## References

- https://en.wikipedia.org/wiki/Rendering_(computer_graphics)
- (Text Rendering) [**Computational Typography**](note.html?n=technica/computation/miscelanea/computational-typography.md)
- https://github.com/dbremont/rendering/tree/main