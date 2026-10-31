---
tags: [security]
---

# Login Manager


> How the **login manager** chooses **Compositor** or **Window Manager**?
> 

> A login manager chooses the compositor or window manager by allowing the user to select a session type from a predefined list, where each session corresponds to a specific compositor or window manager, as defined in session files typically located in `/usr/share/xsessions/` or `/usr/share/wayland-sessions/`. Once a session is selected, the login manager starts the corresponding compositor or window manager when the user logs in.
> 

Guiding questions:

- What is a session in Linux?
- To which sub-system does this concept belongs to?

## Login Manager

> A **login manager** is a more general term that refers to the program responsible for handling user authentication and session initiation. This term can encompass both graphical and non-graphical login methods.
> 
- **Graphical Login Manager:** Typically, this is the same as a display manager, where the graphical interface is provided for logging in.
- **Text-Based Login Manager:** On systems without a graphical environment (or when using virtual terminals), the login manager might be a simple text-based prompt provided by `getty` or `agetty`. Users log in by entering their credentials directly into the terminal.

## Getty: Login Manager

> 

## References

- https://wiki.archlinux.org/title/Getty