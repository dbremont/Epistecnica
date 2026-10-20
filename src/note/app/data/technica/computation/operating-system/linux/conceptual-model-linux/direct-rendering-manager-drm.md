---
tags: [driver, graphics, module]
---

# Direct Rendering Manager (DRM)

- [Linux Graphics Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-graphics-stack.md), [Direct Rendering Infrastructure (DRI)](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/direct-rendering-infrastructure-dri.md)

> The **Direct Rendering Manager (DRM)** is a **kernel module** on Linux that provides the necessary infrastructure for **direct access to graphics hardware**. It manages the interaction between the GPU hardware and user-space applications, enabling efficient rendering and video playback without needing the X server. DRM is part of the **Graphics Subsystem** of the Linux kernel.
> 

> Provides user-space applications with access to GPU features (using `ioctl()` system calls).
> 

## Formulation

- What kind of technical element is DRM?

## Interface

> How to interact with DRM?
> 

## Implementation

> How is DRM implemented?
> 

> How does DRM interact with  the graphics hardware? DRM introduces a common kernel-level abstraction and interaction model for graphics hardware, allowing hardware-specific graphics drivers to expose a standardized interface to user-space graphics components.
> 

## QA

### How the DRM system integrated with the specific GPU? Is there another intermediary?

> 

### What is the relationship with **`Direct Rendering Infrastructure (DRI)`?**

> `Direct Rendering Infrastructure (DRI)` is for providing user-space applications with a direct rendering interface to graphics hardware, while `Direct Rendering Manager (DRM)` is for managing the GPU and graphics resources in the Linux kernel.
> 

### Can a user-space process access **Direct Rendering Manager (DRM)** without DRI?

> Yes, while DRI is not required to access DRM, **DRI exists to provide a standardized user-space architecture for direct rendering, allowing graphics libraries and applications to use GPU hardware through DRM without going through a display server such as X11.**
> 

### Why do we need DRI? What problem does it solves?

> DRI was introduced to enable direct, accelerated user-space rendering while keeping GPU resource management in the kernel through DRM; it is not a prerequisite for a user-space process to access DRM.
> 

## References

- https://en.wikipedia.org/wiki/Direct_Rendering_Manager
- https://github.com/torvalds/linux/tree/master/include/drm