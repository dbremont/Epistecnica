---
tags: [graphics]
---

# X Window System (X11 Version)

- [Hyprland](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/hyprland.md), [Linux Graphics Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-graphics-stack.md)

> The **X Window System**, specifically version 11 (X11), is a robust, network-transparent **windowing system** for bitmap displays, widely used in Unix-like operating systems to provide a foundational framework for graphical user interfaces.
> 

> Note: X11 Does not Provide Any Widgets.
> 

## Protocol

> The protocol is **byte-oriented** and **big-endian** by default, but supports both endiannesses.
> 

Interaction:   There are **two main types** of messages exchanged between client and server:

- **Requests** (Client → Server): Client sends requests to create windows, draw graphics, manage input, etc.
- **Replies, Events, and Errors** (Server → Client): Server responds with replies, asynchronous events (like key presses, mouse movement), or error messages.

### **Message Structure**

a) **Requests**

- **Fixed-size header** (4 bytes):
    - **1 byte**: Major opcode (operation code).
    - **1 byte**: Optional minor opcode (for extension requests).
    - **2 bytes**: Length of the request in 4-byte units (including the header).
- **Additional data** depending on the request type.

 b) **Replies**

- **Fixed-size header** (32 bytes):
    - **1 byte**: Reply code (usually 1).
    - **1 byte**: Unused/padding.
    - **2 bytes**: Sequence number (to match the request).
    - **4 bytes**: Length of reply data in 4-byte units (excluding the first 32 bytes).
    - Followed by reply-specific data.

c) **Events**

- Events are asynchronous messages from server to client.
- Fixed-size of 32 bytes.
- **1 byte**: Event type.
- Other fields depend on the event type (e.g., key press, mouse move).

d) **Errors**

- Fixed-size of 32 bytes.
- Contains error code, sequence number, and request opcode causing the error.

### Opcodes

> A numeric identifier (1 byte) that tells the X server which core protocol request or extension request the client is invoking.
> 

[X11 Opcodes](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/x-window-system-x11-version/x11-opcodes.md)

### Data & Resource Model

> The protocol uses fixed-size types for portability:
> 

| Type | Size | Description |
| --- | --- | --- |
| CARD8 | 1 byte | Unsigned 8-bit integer |
| CARD16 | 2 bytes | Unsigned 16-bit integer |
| CARD32 | 4 bytes | Unsigned 32-bit integer |
| INT8 | 1 byte | Signed 8-bit integer |
| INT16 | 2 bytes | Signed 16-bit integer |
| INT32 | 4 bytes | Signed 32-bit integer |
| BYTE | 1 byte | Raw byte |

### Resource

> 

| **Resource** | **Description** |
| --- | --- |
| **Window** | A drawable region on the screen. Windows can contain other windows, receive events, and display graphics. |
| **Pixmap** | An off-screen image buffer (like an invisible window). Often used for double buffering or icons. |
| **Cursor** | Represents a mouse pointer image. Can be created from bitmaps or fonts. |
| **Font** | Represents a font loaded into the server; used for text rendering. |
| **Graphics Context (GC)** | A collection of drawing state used for rendering (color, line width, font, etc.). |
| **Colormap** | Maps pixel values to RGB colors; essential on systems with limited color depth. |
| **Atom** | A numeric identifier for a string, used for efficient symbolic naming (e.g., property names). |
| **Drawable** | A supertype for objects that can be drawn into: **Window** or **Pixmap**. |
| **Visual** | Describes how pixel values are interpreted (color depth, layout, etc.). |
| **Property** | Arbitrary data attached to a window, identified by atoms. Used for metadata (e.g., window titles, WM hints). |
| **Selection** | A shared mechanism for managing the clipboard and drag-and-drop. |
| **Region** | (Extension) A set of rectangles used for clipping, etc. |
| **Extension-defined** | Extensions (e.g., XRender, XInput2) define new resource types (e.g., Pictures, Input Devices). |

## **X Window System Selection System (clipboard)**

### **What is the definition of this concept in Linux?**

 In Linux systems using the X Window System, the *selection system* is the protocol-level inter-client data exchange mechanism responsible for clipboard semantics, text selection propagation, and transient shared data transfer between graphical applications. Rather than implementing a centralized global clipboard buffer, X11 models selections as dynamically owned named resources—such as `PRIMARY` or `CLIPBOARD`—whose contents are controlled by the client application currently holding ownership of the selection. The X server itself acts primarily as a coordination and event-routing intermediary, maintaining mappings between selections and owner windows while orchestrating asynchronous requests, notifications, and transfer negotiations. Conceptually, the selection system constitutes a distributed, event-driven IPC abstraction embedded within the X11 protocol, designed to support lazy data transfer, heterogeneous representation formats, network transparency, and cooperative inter-application interaction.

### **What is the implementation? Which are the types of selection mechanism?**

The implementation of the X11 selection system is based on a combination of selection ownership semantics, event-based synchronization, atom-based symbolic typing, and property-mediated payload transport. Applications acquire ownership through functions such as `XSetSelectionOwner()`, after which the X server records the owning window associated with a particular selection atom. When another client requests the data, the protocol uses `SelectionRequest`, `SelectionNotify`, and related events to negotiate and transfer the content, typically through window properties encoded in negotiated target formats such as `UTF8_STRING`, `TEXT`, `image/png`, or application-specific MIME representations. The principal selection mechanisms are `PRIMARY`, `CLIPBOARD`, and the largely obsolete `SECONDARY` selection. `PRIMARY` implements the traditional Unix selection model in which merely highlighting text establishes ownership and middle-click performs paste operations, whereas `CLIPBOARD` implements explicit copy-paste semantics associated with keyboard-driven operations like `Ctrl+C` and `Ctrl+V`. For large payloads, the protocol employs the `INCR` incremental transfer mechanism, enabling chunked asynchronous transmission beyond normal property size constraints.

### **What is the interaction forms and mechanisms?**

Interaction within the X11 selection system occurs through asynchronous client-to-client coordination mediated by the X server and realized via event dispatch, property manipulation, and target negotiation protocols. The primary interaction forms include implicit selection transfer through text highlighting (`PRIMARY`), explicit clipboard operations (`CLIPBOARD`), middle-button paste semantics, drag-and-drop exchanges, and remote inter-display clipboard propagation over network-transparent X sessions. Mechanistically, these interactions depend on a sequence of ownership acquisition, request issuance through `XConvertSelection()`, representation negotiation using target atoms such as `TARGETS`, property-based payload serialization, and completion signaling through notification events. Toolkits such as GTK and Qt abstract these low-level operations into higher-level clipboard APIs, while clipboard managers extend the protocol by caching selection contents to overcome the volatile ownership model in which clipboard data disappears when the owning process terminates. Collectively, these mechanisms form a sophisticated distributed interaction framework integrating IPC semantics, type negotiation, event orchestration, and GUI interaction models within the X11 ecosystem.

### **Which others functionality does the ‘selection’ system supports?**

The X11 *selection system* supports substantially more functionality than conventional clipboard operations. Architecturally, it serves as a generalized inter-client data exchange and negotiation framework embedded within the X Window System protocol. Clipboard behavior is merely its most visible specialization. The same underlying mechanisms—selection ownership, asynchronous event routing, target negotiation, and property-based transfer—are reused across multiple interaction domains in graphical Unix environments.

One major functionality supported by the selection system is **text selection propagation**, particularly through the `PRIMARY` selection model, where selecting text immediately publishes it as transferable data without requiring an explicit copy command. This enables interaction paradigms such as middle-click paste and rapid transient text transfer between applications, terminals, and editors. Closely related is support for **rich multi-format data exchange**, where applications negotiate representations dynamically using target atoms such as `UTF8_STRING`, `text/html`, `image/png`, or application-defined binary formats. This allows the same logical selection to be transferred as plain text, formatted markup, images, URIs, or structured objects depending on requester capabilities.

The selection infrastructure also underlies important forms of **drag-and-drop interaction**. Protocols such as XDND reuse selection-style negotiation semantics to advertise supported MIME targets, coordinate transfer acceptance, and asynchronously stream payloads between applications. In this sense, drag-and-drop in X11 is effectively a higher-level behavioral layer built atop generalized selection transfer primitives. Additionally, the mechanism supports **incremental streaming of large payloads** through the `INCR` protocol, enabling efficient transfer of large documents, images, or binary datasets beyond fixed property size limits.

Another important capability is **remote inter-display data exchange**. Because X11 is network-transparent, selections can traverse SSH-forwarded sessions or remote X displays, allowing clipboard and selection interactions across machines. The selection system therefore acts as a distributed IPC abstraction spanning process and host boundaries. It also supports **cross-toolkit interoperability**, enabling applications written with different GUI frameworks—such as GTK, Qt, Motif, Java AWT, or terminal emulators—to exchange structured data through a common protocol-level representation system.

Selections additionally support **clipboard persistence and history management** through clipboard manager applications such as CopyQ and Klipper. These tools observe ownership transitions, proactively request data from current owners, and maintain historical caches, effectively extending the original protocol with persistence semantics absent from native X11. The same infrastructure also facilitates **terminal integration mechanisms**, including OSC52 clipboard forwarding, enabling remote shell sessions, editors, and multiplexers such as tmux to interact with the graphical clipboard system indirectly through terminal escape sequences.

More abstractly, the selection system functions as a general-purpose framework for:

- transient shared state publication,
- negotiated typed data interchange,
- asynchronous GUI IPC,
- cooperative ownership coordination,
- event-driven inter-application communication.

Thus, the X11 selection system is not fundamentally “the clipboard”; rather, the clipboard is one specialization of a broader distributed selection and transfer architecture within the X Window System.

## X11 Extensions

> An **X11 extension** is a formal mechanism that adds new protocol-level functionality to the X Window System, allowing the X server and clients to support capabilities **not included in the core X11 protocol**.
> 

> **Extensions ship with the X server**, not user-installable.
> 

```bash
# List extentions: xdpyinfo
xdpyinfo | grep -A1 "number of extensions"
```

| **Extension Name** | **Purpose / Functionality** | **Common Uses** | **Notes** |
| --- | --- | --- | --- |
| `BIG-REQUESTS` | Allows larger-than-normal protocol requests | Large images, big data transfers | Increases max request size > 64 KB |
| `Composite` | Enables window compositing (offscreen rendering) | Window managers with effects | Required by modern desktop environments |
| `DAMAGE` | Reports parts of windows that have changed | Efficient redraws by compositors | Often paired with Composite |
| `DPMS` | Display Power Management Signaling | Screen savers, energy saving | Controls monitor power state |
| `GLX` | OpenGL Extension to the X Window System | Hardware-accelerated 3D graphics | Integrates OpenGL with X11 |
| `RANDR` | Resize and Rotate extension | Monitor hotplug, screen orientation | Used by xrandr, modern DEs |
| `RENDER` | 2D graphics rendering improvements | Alpha blending, antialiased fonts | Prerequisite for modern font rendering |
| `X-Resource` | Allows querying resource usage per client | Debugging, performance analysis |  |
| `XC-MISC` | Helps reclaim resource IDs | Internal resource management |  |
| `XEvIE` (Experimental) | Intercepts input events for filtering/modification | Accessibility tools | Deprecated / rarely used |
| `XFIXES` | Various minor fixes and additions | Cursor tracking, regions | Used with Composite and DAMAGE |
| `XFree86-Bigfont` | Optimizes font rendering using shared memory | Faster large font rendering | Specific to XFree86 |
| `XINERAMA` | Combines multiple physical screens into one logical screen | Multi-head setups | Deprecated in favor of RANDR |
| `XInputExtension` | Extended input device support | Tablets, joysticks, multi-touch | XInput 1.x |
| `XInput2` | Multi-device, multi-touch input support | Touchscreens, complex input | Supersedes XInputExtension |
| `XKB` | X Keyboard extension | Keyboard layouts, LEDs, key remapping | Required for modern keyboard layouts |
| `XTEST` | Simulates input events | Automated testing, accessibility | Often used by xdotool |
| `SHAPE` | Enables non-rectangular window shapes | Rounded or irregular windows | Used by GUI toolkits |
| `MIT-SHM` | Shared memory extension | High-performance image transfers | Enables fast drawing to pixmaps |
| `SYNC` | Synchronization primitives for X clients | Animation timing, frame pacing | Used by toolkits |
| `SELinux` | Security labeling integration | Access control in secure environments | For SELinux systems |
| `Generic Event` | Event routing framework | Base for XInput2 and other event extensions | Used internally |
| `RECORD` | Records all protocol data | Debugging, sniffing | Rarely used today, replaced by xtruss |

## libGL

> `libGL` is the **client-side OpenGL library** that implements the OpenGL API and connects X11 applications to the underlying **OpenGL rendering system**—either software or hardware-accelerated.
> 

### 🧠 **Who Uses `libGL`?**

| **Type of Software** | **Examples** | **Purpose** |
| --- | --- | --- |
| **OpenGL applications** | Games, simulations, CAD tools | Use OpenGL API calls (e.g., `glDrawArrays`) to render 2D/3D graphics |
| **Windowing toolkits** | GTK, Qt, SDL, GLFW | Use `libGL` internally to provide OpenGL contexts or accelerated drawing |
| **Compositing window managers** | GNOME Shell, KWin, Compiz | Use `libGL` (via `GLX` or `EGL`) for GPU-based window compositing |
| **Browsers** | Firefox, Chromium | Use `libGL` for WebGL, GPU acceleration, and video rendering |
| **Machine learning/vision tools** | Blender, TensorFlow (with OpenGL backends) | Use OpenGL shaders or GPU interop for rendering or acceleration |
| **3D APIs** | OpenSceneGraph, VTK, Three.js (via emulation) | Depend on OpenGL as backend |
| **GLX / X11 clients** | Any X11 app using `GLX` | `libGL` bridges X11 (`GLX`) and OpenGL functions |

### 🔧 How `libGL` Works

1. Application calls OpenGL function (e.g., `glClear`, `glDrawElements`) provided by `libGL`.
2. `libGL` translates this into:
    - **GLX requests** (if using X11)
    - Or **EGL/DRI** commands (for Wayland or direct rendering)
3. Commands are routed to:
    - The **GPU driver** (via Mesa, NVIDIA, or AMD binary driver)
    - Or a **software renderer** (like LLVMpipe)

## **Tools**

- **xwininfo**: Provides information about a specific window, such as its geometry, parent, and children.
- **xprop** allows you to view and modify the properties of a specific window. It can display information like the window title, class, and resource.
- **xev**: This program captures and displays X11 event information generated by various input devices, such as mouse clicks and key presses.
- **xset**: Enables you to control various X11 server settings, including screensaver, keyboard, pointer, and font settings.
- **xrandr**: Configuring the screen resolution, refresh rate, and orientation. It can be used to add, remove, or modify display outputs.
- **xdotool**: Automates and controls X11 windows and actions programmatically. It can simulate key presses, mouse movements, and window manipulations.
- **xkill**: Allows you to forcefully terminate an X11 client by clicking on its window.
- **xlsclients**: Lists all client applications connected to the X11 server.
- **xmodmap**: Modifies keymaps and pointer button mappings. It can remap keys and change the behavior of modifier keys.
- **xdpyinfo**: Provides detailed information about the X11 display, including screen dimensions, supported extensions, and available visuals.
- **xclip**: Manipulates the clipboard in X11. It can be read from or written on the clipboard from the command line or scripts.
- **xauth**: Manages X11 authority files, which control client access to the X server.
- **xhost**: Controls the X server’s access control mechanisms, allowing or denying connections from specific hosts.
- **xmessage**: Displays a simple message dialog box on the X11 display.
- **xterm**: A terminal emulator for X11, providing a text-based interface within a graphical environment.
- **xtruss**: Debug the x11 server.

## References

- [X11](https://magcius.github.io/xplain/article/index.html)
- [xtruss / X11 Debug](https://www.chiark.greenend.org.uk/~sgtatham/xtruss/)
- [Overview of X Windows](http://www-h.eng.cam.ac.uk/help/tpl/graphics/X/X11R5/node3.html)
- https://www.x.org/releases/current/doc/xproto/x11protocol.html
- https://cyber.dabamos.de/unix/x11/
- [How to copy image to clipboard, to paste to another application?](https://superuser.com/questions/199285/how-to-copy-image-to-clipboard-to-paste-to-another-application)