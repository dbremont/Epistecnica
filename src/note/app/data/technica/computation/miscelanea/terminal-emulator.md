---
tags: [operative-system, tool]
---

# Terminal Emulator

- [Shell Interpreter](note.html?n=technica/computation/miscelanea/shell-interpreter.md), [Kitty](note.html?n=technica/computation/miscelanea/kitty.md), [Terminal Session Recorder](note.html?n=technica/computation/miscelanea/terminal-session-recorder.md)

> **Terminal Emulator** — is a program that provides **display and interaction services** for terminal applications, essentially emulating the behavior of a traditional interactive terminal interface.
> 

> **Note:** A useful way to think about it is: **Web Application → Browser :: Terminal Application → Terminal Emulator**.
> 

## Formulation

> A terminal emulator provides a **standard interactive interface** that applications can rely on instead of implementing their own display and input mechanisms.
> 

> **Terminal Emulator → provides a common display and interaction interface for terminal applications.**
> 

> Applications such as shells, editors, pagers, and interactive tools can then focus on their **application semantics**, while the terminal emulator handles the **interaction mechanics**.
> 

> The terminal emulator centralizes these responsibilities into a **shared interaction environment**.
> 

Without a terminal abstraction, each interactive application would need to:

- manage keyboard input;
- render text and cursor movement;
- handle screen layout;
- interpret control sequences;
- manage scrolling and resizing;
- interact directly with the graphical environment.

## Capability Dimension

| **Capability Dimension** | **Description** | **Value Set** |
| --- | --- | --- |
| **Terminal Emulation** | Defines the terminal interfaces, standards, and control sequences understood by the emulator. | VT100; VT220; VT320; ANSI; xterm; escape-sequence processing |
| **Rendering** | Defines how terminal state is converted into visual output. | CPU rendering; GPU rendering; font rasterization; Unicode; accelerated rendering |
| **Session Management** | Defines how terminal processes and sessions are created, organized, persisted, and restored. | Windows; tabs; profiles; persistent sessions; session restoration |
| **Spatial Composition** | Defines how multiple terminal sessions are spatially arranged within the UI. | Panes; splits; tiling; grids; layouts; arbitrary arrangements |
| **Interaction** | Defines the mechanisms through which users interact with terminal content and sessions. | Keyboard; mouse; selection; clipboard; synchronized input |
| **Customization** | Defines how terminal behavior, appearance, and interaction can be configured. | Colors; fonts; themes; profiles; key bindings; configuration files |
| **Extension** | Defines mechanisms for extending terminal functionality or programming its behavior. | Plugins; scripting; extensions; APIs; programmable configuration |
| **Remote Control** | Defines mechanisms for controlling terminal instances and sessions from external processes. | Control socket; CLI/API; remote commands; SSH integration |
| **Graphics** | Defines support for graphical content and terminal-specific graphical protocols. | Hyperlinks; inline images; Sixel; Kitty graphics protocol; semantic text |
| **Performance** | Defines the computational and resource characteristics of the emulator. | Low resource usage; GPU acceleration; high-throughput rendering; low latency |
| **Desktop Integration** | Defines integration with the host desktop environment and its services/toolkits. | GNOME; KDE; Xfce; GTK; Qt; desktop settings; system notifications |

## Terminal Emulator System Set

| **Terminal Emulator** | **Description** | **Capability Set** |
| --- | --- | --- |
| **GNOME Terminal** | The default terminal emulator for the GNOME desktop environment. It is user-friendly and integrates well with GNOME, offering tabs and profile management. |  |
| **Konsole** | The default terminal emulator for the KDE Plasma desktop environment. Known for its rich feature set, it supports split views, tabs, and extensive customization. |  |
| **Xfce Terminal** | The default terminal for the Xfce desktop environment, providing a balance between simplicity and functionality, with support for tabs and customizable appearance. |  |
| **Terminator** | A powerful terminal emulator that allows users to arrange multiple terminals in a grid, offering split windows and grouping. It’s great for multitasking. |  |
| **Tilix** | A tiling terminal emulator with features similar to Terminator, offering drag-and-drop support for terminals, customizable layouts, and session management. |  |
| **Alacritty** | A modern terminal emulator that focuses on speed and performance. It is written in Rust and is highly optimized, though it is relatively minimal in features. |  |
| **URxvt (rxvt-unicode)** | A highly customizable terminal emulator known for its low resource usage and support for Unicode. It is suitable for users who need a lightweight and powerful terminal. |  |
| **Kitty** | A GPU-accelerated terminal emulator designed for speed and efficiency. It supports advanced features like tabs, windows, and remote control via SSH. |  |
| **Hyper** | An Electron-based terminal emulator that is highly extensible through plugins and themes, with a focus on a modern, web-based approach. |  |
| **LXTerminal** | The default terminal for the LXDE desktop environment, designed to be lightweight and fast. It provides essential features without the overhead of more complex terminals. |  |
| **xterm** | One of the oldest and most stable terminal emulators available. It is the default for many X Window System environments, offering a basic and reliable experience. |  |
| **st (Simple Terminal)** | A minimalistic terminal emulator from the suckless project, focused on simplicity and efficiency, with very few features and a small codebase. |  |
| **Sakura** | A lightweight terminal emulator based on GTK and VTE. It aims to be simple, with few dependencies and a clean interface, providing basic features like tabs. |  |
| **Cool Retro Term** | A terminal emulator that mimics the look and feel of old CRT monitors, providing a retro experience with a variety of effects and themes. |  |

## QA

### How does it related with a TTY?

> A **TTY** is an operating-system interface that connects a `terminal session` to a process, while a **terminal emulator** is a user-space application that provides the terminal interface and communicates with that TTY.
> 

> What is a `terminal session?`  A **terminal session** is an instance of an interactive terminal environment managed by that application.
> 

> Does `terminal session` related with `user session` ?
> 

> **User session** = the user's overall login/runtime context.
> 

> **Terminal session** = an interactive terminal environment within that context.
> 

> **Process session** = a specific Unix process-management abstraction.
> 

## References

- [Kitty](note.html?n=technica/computation/miscelanea/kitty.md)
- [Linux](note.html?n=technica/computation/operating-system/linux.md)
- https://en.wikipedia.org/wiki/Pseudoterminal
- https://en.wikipedia.org/wiki/Terminal_emulator
- https://en.wikipedia.org/wiki/List_of_terminal_emulators
- https://terminaltrove.com/terminals/
- [**TTY Subsystem**](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/tty-subsystem.md)