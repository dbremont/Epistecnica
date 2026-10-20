---
tags: [graphics]
---

# Linux Graphics Stack

- [Linux Multimedia Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-multimedia-stack.md), [Hyprland](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/hyprland.md), [X Window System (X11 Version)](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/x-window-system-x11-version.md), [Direct Rendering Manager (DRM)](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/direct-rendering-manager-drm.md)

> The **Linux Graphics Stack** is a complex and layered architecture consisting of the X Window System or Wayland as display servers, Mesa 3D for rendering, DRI (Direct Rendering Infrastructure) for direct hardware access, and various device drivers that interface with the underlying hardware to provide comprehensive support for rendering graphics on Linux systems.
> 

- **Integrated graphics (iGPU)** refers to a GPU that is **not a separate device with its own dedicated memory**, but instead is **embedded in the same chip (or package) as the CPU** and **shares system RAM**.
- DRM standardizes **resource management**, not **GPU programming semantics**.
    - It is a **low-level, semi-unified kernel interface with strong driver-specific extensions**
    - For meaningful GPU usage:
        - **callers must either know the driver OR use a library (Mesa) that does**
- Which hardware is supported by messa?

![](https://upload.wikimedia.org/wikipedia/commons/2/25/Linux_Graphics_Stack_2015.svg)

## Linux Graphics Stack

> 

| **Display Manager** | … |  |
| --- | --- | --- |
| **Component** | **Description** | Case(s) |
| **Display Server** | Responsible for managing and rendering graphical output, handling input devices, and facilitating communication between applications and the display hardware. | X11, Wayland |
| **Compositor** | Combines different graphical elements, such as windows and user interface elements, to create the final on-screen image, providing visual coherence and effects. | Mutter, Compiz, Gnome-shell |
| **Window Manager** | Controls the placement, appearance, and interaction of application windows on the desktop, including features like window resizing, minimizing, and maximizing. | i3, awesome, xmonad, Mutter, Compiz |
| **Desktop Environment (DE)** | A comprehensive graphical interface for a computer operating system, encompassing a cohesive set of applications, a window manager, and various system utilities, providing users with a unified and user-friendly interaction experience. | Gnome, KDE, XFCE |

## Window Manager

> Controls the placement, appearance, and interaction of application windows on the desktop, including features like window resizing, minimizing, and maximizing.
> 

Tools:

- https://github.com/hyprwm/Hyprland

## **Desktop Environment (DE)**

> 

| **Name** | **Description** | **Performance** |
| --- | --- | --- |
| **Gnome** | A modern and feature-rich DE offering a sleek user interface with advanced graphical effects and integration, commonly used in distributions like Ubuntu. | Moderate to High (Resource-Intensive) |
| **KDE Plasma** | A highly customizable and visually appealing DE with a wide range of features and tools, known for its flexibility and user-friendly interface. | Moderate (Can be resource-intensive with all features enabled) |
| **XFCE** | A lightweight DE designed for speed and low resource usage, offering a traditional desktop experience with minimal graphical effects. | Low (Lightweight and fast) |
| **LXDE/LXQt** | A very lightweight DE focused on providing a simple and fast desktop experience, ideal for older hardware or systems with limited resources. | Very Low (Minimal resource usage) |
| **Cinnamon** | A DE that provides a balance between modern aesthetics and traditional desktop layouts, commonly used in Linux Mint. | Moderate (Balanced performance) |
| **MATE** | A continuation of the GNOME 2 desktop, offering a traditional desktop experience with a focus on simplicity and efficiency. | Low to Moderate (Light and efficient) |
| **Budgie** | A modern DE with a focus on simplicity and elegance, built on top of GNOME technologies, often featured in the Solus distribution. | Moderate (Optimized for performance) |

## Sessions Terminal (Graphical & CLI)

> In Linux, pressing `Ctrl + Alt + F1` (or similar combinations like `Ctrl + Alt + F2`, `F3`, etc.) switches you to a different virtual console or TTY (teletype terminal).
> 

> These are text-based terminals that run independently of **your graphical session**.
> 

> What does the term session in this context denote?
> 

### Key Points:

- **`Ctrl + Alt + F1` (or `F2`, `F3`, etc.)**: Switches to a virtual console (TTY). On many systems, `F1` is associated with the graphical session (`tty1`), but on some systems, the graphical session might be on `F2` or another key.
- **Text-Based Login**: When you switch to one of these TTYs, you'll see a text-based login prompt where you can log in using your username and password.
- **Graphical Session**: You can usually return to your graphical desktop environment by pressing `Ctrl + Alt + F7` or `F1` (depending on how your system is configured).

### Common Virtual Console Mappings:

- **`Ctrl + Alt + F1` to `F6`**: Usually mapped to TTY1 through TTY6 for text-based terminals.
- **`Ctrl + Alt + F7`**: Typically mapped to the graphical session (X server or Wayland compositor) on many systems, though this can vary.

### Navigating Between Multiple Terminal Sessions

> You can have more than one graphical terminal (or graphical session) running simultaneously in Linux. Each graphical session can be associated with a different TTY (teletype terminal), allowing you to switch between them using key combinations.
> 

> **Multiple Graphical Sessions:** You can start additional graphical sessions using different display managers or manually via commands. Each session runs independently, allowing different users or environments (e.g., GNOME on one TTY, KDE Plasma on another) to be active at the same time.
> 

Select:

1. **Using a Display Manager:**
    - Many display managers (like GDM, SDDM) allow switching between users or starting new sessions.
    - After logging in to your first session, you can usually select an option like "New Session" or "Switch User" from the login or lock screen.
2. **Using the `startx` Command:**
    - You can manually start a new graphical session from a TTY by switching to an unused TTY (e.g., `Ctrl + Alt + F3`) and running `startx` or a specific command for your desktop environment.
    - Example:  `startx -- :1`
    - The `:1` specifies that the new session should be on display `:1` (as opposed to `:0`, which is usually the first session).

Switching

1. After starting multiple sessions, you can switch between them using `Ctrl + Alt + F1`, `F2`, `F3`, etc., depending on which TTY the sessions are associated with.

### References

- [Graphics Card](note.html?n=technica/computation/platform/hardware-physical-substrate/conceptual-model-hardware/graphics-card.md)
- [Window Manager](https://en.wikipedia.org/wiki/Window_manager)
- [List of display servers](https://en.wikipedia.org/wiki/List_of_display_servers)
- [The Linux Graphics Stack](http://blog.mecheye.net/2012/06/the-linux-graphics-stack/)
- [Text Rendering Hates You](https://faultlore.com/blah/text-hates-you/)
- [Compositing window manager](https://en.wikipedia.org/wiki/Compositing_window_manager)
- [Linux Graphic Stack and Wayland](http://longwei.github.io/Linux-Graphic-And-Wayland/)
- [An introduction to the Linux graphics stack](https://flusp.ime.usp.br/blogs,/kernel-graphics/an_introduction_to_the_linux_graphics_stack/)
- [A brief introduction to the Linux graphics stack](https://blogs.igalia.com/itoral/2014/07/29/a-brief-introduction-to-the-linux-graphics-stack/)
- [RubyWM – an X11 window manager in pure Ruby](https://news.ycombinator.com/item?id=39087609)