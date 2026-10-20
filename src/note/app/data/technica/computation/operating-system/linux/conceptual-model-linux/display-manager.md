---
tags: [graphics]
---

# Display Manager

- [Hyprland](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/hyprland.md)

**Display Manager ≠ Desktop Environment ≠ Window Manager / Compositor**

```
Display Manager
    ↓
authenticates user
    ↓
selects graphical session
    ↓
starts session
    ↓
Desktop Environment
    └── Window Manager / Compositor
```

### Display Manager

A **display manager** is a graphical application that provides a user interface for users to log in to a desktop environment or a window manager. It typically includes:

- **Graphical Login Screen:** Where users enter their username and password.
- **Session Management:** Allows users to select a desktop environment (e.g., GNOME, KDE, Xfce) or a window manager (e.g., i3, Sway) before logging in.
- **X Server/Wayland Management:** Manages the startup of the X server (in X11) or Wayland compositor.

Common display managers include:

- **GDM (GNOME Display Manager):** Used primarily with the GNOME desktop.
- **SDDM (Simple Desktop Display Manager):** Commonly used with KDE Plasma.
- **LightDM:** A lightweight display manager that can be used with various desktop environments.
- **LXDM:** Used with the LXDE desktop environment.