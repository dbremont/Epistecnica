# Simple DirectMedia Layer (SDL)

> SDL (Simple DirectMedia Layer) does not interact with the hardware directly in the sense of manipulating hardware registers or directly controlling hardware devices. Instead, it serves as an abstraction layer that simplifies access to hardware functionality across different platforms.
> 

> SDL is a minimalistic, efficient, and flexible foundation for writing **portable multimedia applications**, especially when you need direct control over rendering, input, and sound with **low overhead** and **fine performance tuning**.
> 

## Breviarium

| **Aspect** | **Description** |
| --- | --- |
| **Type** | Low-level multimedia framework / hardware abstraction layer |
| **Language** | Written in **C**, with bindings for **C++, Python, Rust**, and many others |
| **Cross-Platform** | Runs on **Windows, macOS, Linux, iOS, Android**, and more |
| **Graphics Support** | 2D rendering via software or hardware acceleration (OpenGL, Direct3D, Vulkan via extensions) |
| **Audio Support** | Abstracts sound output (PCM playback, streaming audio, etc.) |
| **Input Handling** | Unified input API for keyboard, mouse, game controllers |
| **Windowing System** | Provides platform-independent window and event loop management |
| **Threading & Timing** | Cross-platform threading, mutex, semaphores, and timing functions |
| **License** | **Zlib License** (very permissive and business-friendly) |

## Hardware Interface

1. **Abstraction Layer**: SDL abstracts the underlying hardware details, allowing developers to write code that is portable across different operating systems and hardware configurations. This means you can write SDL code that works on Windows, macOS, Linux, and other platforms without needing to change your source code significantly.
2. **Platform-Specific Implementations**: While SDL itself does not directly access hardware, it relies on the underlying operating system and its drivers to manage hardware resources. For example:
    - On **Windows**, SDL uses the Win32 API to interface with the Windows graphics and input systems.
    - On **Linux**, SDL may use X11, Wayland, or other windowing systems to manage graphics and input.
    - On **macOS**, SDL uses the Cocoa API to interact with the graphics and input systems.
3. **Graphics API Integration**: SDL can integrate with lower-level graphics APIs such as OpenGL, Direct3D, or Vulkan. While SDL provides functions to create windows and handle events, the actual rendering to the screen is typically done using these graphics APIs, which may interact more closely with the hardware.
4. **Hardware Acceleration**: SDL can facilitate hardware acceleration by providing access to OpenGL or Direct3D contexts. This allows developers to take advantage of GPU capabilities for rendering graphics, which is often faster than CPU-based rendering.
5. **Input Handling**: SDL handles input devices (keyboard, mouse, game controllers) using the platform's native APIs, allowing for consistent input handling across different systems without direct hardware access.

## References

- https://www.libsdl.org/
- https://en.wikipedia.org/wiki/Simple_DirectMedia_Layer