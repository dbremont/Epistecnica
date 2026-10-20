# OpenGL

> OpenGL (Open Graphics Library) is a cross-language, cross-platform application **programming interface (API)** designed for rendering 2D and 3D vector graphics. It provides a standardized, low-level interface to the GPU (Graphics Processing Unit), enabling direct manipulation of the graphics pipeline through a state machine model.
> 

> **State Machine  Model**: OpenGL operates as a state machine, where the global state affects rendering behavior. Commands issued to modify this state or submit data for rendering.
> 

```bash
## Check the Hardware
sudo lshw -c video

## Install Mesa Utils - Get Some Info About OpenGL.
sudo apt update
sudo apt install mesa-utils

glxinfo | grep "OpenGL"
glxgears
```

## Definition

Technically, OpenGL exposes a procedural API consisting of a large set of functions that allow programmers to:

- Define geometric primitives (points, lines, triangles) and their attributes (color, texture coordinates, normals).
- Manage and manipulate transformation matrices (model, view, projection) to perform coordinate space conversions.
- Control the fixed-function pipeline stages or programmable pipeline via shaders (vertex, fragment, geometry shaders).
- Handle texture mapping, buffer objects (vertex buffer objects, element buffer objects), framebuffers, and renderbuffers.
- Perform rasterization, shading, blending, depth testing, and stencil testing.
- Synchronize GPU commands and manage resource lifetimes.

## List of Implementations

> 

| **Implementation** | **Platform** | **Description** |
| --- | --- | --- |
| **Mesa 3D** | Cross-Platform | Open-source implementation of OpenGL, Vulkan, and other specifications. Used on Linux systems and supports multiple graphics drivers. |
| **Microsoft OpenGL (MS OpenGL)** | Windows | Microsoft's default OpenGL implementation, often limited to older OpenGL versions unless overridden by vendor-specific drivers. |
| **NVIDIA OpenGL** | Cross-Platform (Windows, Linux, macOS) | Proprietary OpenGL implementation provided by NVIDIA for their GPUs. Offers full support for the latest OpenGL versions. |
| **AMD OpenGL** | Cross-Platform (Windows, Linux) | Proprietary OpenGL implementation for AMD GPUs. Full support for modern OpenGL features. |
| **Intel OpenGL** | Cross-Platform (Windows, Linux) | Provided by Intel for integrated GPUs. Supports modern OpenGL features based on the GPU generation. |
| **Apple OpenGL** | macOS | Deprecated implementation of OpenGL on macOS. Apple focuses on Metal, their proprietary graphics API, for modern applications. |
| **ANGLE (Almost Native Graphics Layer Engine)** | Windows, Android | Translates OpenGL ES calls to Direct3D (on Windows) or Vulkan. Used in Chrome and Android for cross-platform graphics compatibility. |
| **OpenGL ES** | Embedded Systems | Subset of OpenGL for embedded systems, such as mobile devices and IoT hardware. Supported on Android, iOS, and other platforms. |
| **Gallium3D** | Linux | Part of Mesa 3D, offering a unified driver architecture for various GPUs. Supports OpenGL and other graphics APIs. |
| **OpenGL SC** | Safety-Critical Systems | A version of OpenGL designed for real-time and safety-critical environments, such as avionics and automotive systems. |
| **MoltenGL** | macOS, iOS | Implementation that translates OpenGL ES calls to Metal. Useful for running OpenGL ES apps on Apple platforms. |
| **GL4ES** | Linux, Android, macOS | A wrapper that converts OpenGL ES calls to OpenGL, allowing legacy OpenGL apps to run on modern platforms. |
| **SwiftShader** | Cross-Platform | Software-based implementation of OpenGL (and Vulkan). Useful for systems without dedicated GPU hardware. |

## Rendering

| **Technique** | **Category** | **Supported Directly?** | **How in OpenGL** | **Notes** |
| --- | --- | --- | --- | --- |
| **Forward Rendering** | Shading Strategy | ✅ Yes | Vertex + Fragment shaders, `glDraw*` | Default pipeline |
| **Deferred Rendering** | Shading Strategy | 🛠️ Manual | G-buffers + multiple render targets + shaders | Implemented with FBOs and multiple passes |
| **Instanced Rendering** | Geometry Optimization | ✅ Yes | `glDrawArraysInstanced`, `glVertexAttribDivisor` | For rendering many similar objects efficiently |
| **Shadow Mapping** | Lighting Technique | 🛠️ Manual | Depth texture from light POV, compare in fragment shader | Requires framebuffer + shaders |
| **Screen Space Effects** | Post-processing | 🛠️ Manual | Render to texture, process via fullscreen quad | SSAO, SSR, bloom, DoF, etc. |
| **Toon / Cel Shading** | NPR (Stylized) | 🛠️ Manual | Lighting model via fragment shader | Stylized edge and quantized shading |
| **Multi-Pass Rendering** | Composition Strategy | ✅ Yes | Bind different FBOs and re-render multiple times | Core technique for post FX |
| **Environment Mapping** | Reflection / Lighting | ✅ Yes | Cube maps + `reflect()` in fragment shader | For skyboxes and fake reflections |
| **Parallax Mapping** | Surface Detail | 🛠️ Manual | Normal map + depth simulation in fragment shader | Adds pseudo-depth to surfaces |
| **Raymarching** | Procedural / SDF rendering | 🛠️ Manual | Fullscreen quad + SDF in fragment shader | Great for effects and volumetrics |
| **Path Tracing** | Global Illumination | 🛠️ Manual | Monte Carlo in fragment or compute shaders | Realistic, but slow; often done in compute shaders |
| **Compute Shader Rendering** | Procedural / GPGPU | ✅ Yes (GL 4.3+) | `glDispatchCompute`, write to image buffers | Full control, not raster-based |
| **Volume Rendering** | Scientific / Volumetric | 🛠️ Manual | 3D textures + ray casting in fragment shader | For medical, smoke, or cloud rendering |
| **Point Cloud Rendering** | Geometry Representation | ✅ Yes | Use `GL_POINTS`, optional geometry shader | Visualize particles or LIDAR data |
| **Tessellation** | Geometry Refinement | ✅ Yes (GL 4.0+) | Tessellation control/evaluation shaders | Subdivide patches dynamically |
| **Geometry Shader Effects** | Procedural Geometry | ✅ Yes | Generate primitives in the geometry shader | For explosion, ribbon, trail effects |
| **Line Rendering** | Geometry Type | ✅ Yes | `GL_LINES`, `GL_LINE_STRIP`, or `GL_LINE_LOOP` | Wireframes, charts |
| **Wireframe Mode** | Visualization | ✅ Yes | `glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)` | Useful for debugging geometry |

## QA

### How OpenGL Interact with the GPU?

> Internally, **OpenGL** drivers translate API calls into GPU-specific instructions, interacting with the GPU hardware to execute the graphics pipeline stages efficiently.
> 

> **OpenGL** specification abstracts hardware details, allowing developers to write portable code for real-time rendering on various platforms, including desktop, embedded, and mobile GPUs.
> 

### Can OpenGL alone, without relying on external windowing systems or context creation libraries, be used to render graphics directly to the screen?

> No, you **cannot render directly to the display using OpenGL alone** because OpenGL is purely a *graphics rendering API* that assumes a valid **graphics context** and a **drawable surface** (like a window or framebuffer) already exist.
> 

Why?

- OpenGL **does not create windows, handle input, or manage display buffers.** It only issues rendering commands inside an existing context.
- To actually display graphics on the screen, you need:
    - A **windowing system or display server** (like X11, Wayland, Windows API, macOS Cocoa) to create a window or surface.
    - A **graphics context** linked to that window/surface where OpenGL can draw.
    - A **context management interface** (like GLX on X11, WGL on Windows, EGL on embedded platforms) to bind OpenGL to the window.

In practical terms:

- You use libraries like **GLFW**, **SDL**, **SFML**, or platform-specific APIs to:
    - Create a window.
    - Create and manage the OpenGL context.
    - Handle user input and events.
- Then, inside that context, you use OpenGL commands to render your graphics.
- Finally, you swap the buffers (front/back) to present the rendered image on screen.

Summary:

| Component | Responsibility |
| --- | --- |
| OpenGL | Rendering commands, shaders, pipeline control |
| Windowing system (X11, Windows API, etc.) | Creating windows, managing display |
| Context interface (GLX, WGL, EGL) | Binding OpenGL context to window |
| Utility libraries (GLFW, SFML, SDL) | Wrapping window and context creation |

## References

- https://en.wikipedia.org/wiki/OpenGL
- [‣](https://app.notion.com/p/214598edb79080bea9f1c1de878e5896?pvs=21)
- [X Window System (X11 Version)](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/x-window-system-x11-version.md)
- https://dri.freedesktop.org/wiki/libGL/
- https://github.com/eug/awesome-opengl?tab=readme-ov-file
- [OpenGL By Example] https://github.com/McNopper/OpenGL
- https://cs.lmu.edu/~ray/notes/openglexamples/
- https://github.com/progschj/OpenGL-Examples
- [https://www.opengl-tutorial.org/](https://www.opengl-tutorial.org/)
- https://en.wikipedia.org/wiki/Wavefront_.obj_file
- https://zeromake.github.io/learnopengl-examples/
- https://learnopengl.com/
- https://en.wikipedia.org/wiki/Tessellation