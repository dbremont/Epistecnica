---
tags: [driver, i-o]
---

# TTY Subsystem


> The **Linux TTY subsystem** is a **kernel subsystem** that implements the character-device abstraction and execution semantics for terminal endpoints, providing processes with standardized terminal I/O, line-discipline processing, terminal attributes, signal generation, and job-control integration across physical terminals, virtual consoles, and pseudo-terminals.
> 

> **Note:** This is a **typical kernel design pattern**: implement a mechanism in the kernel and expose that mechanism to user-space applications through a standard interface—in this case, a pair of endpoints.
> 

> **Note:** The level of understanding of this (conceptual internalization, and operationalization capacity) is still low.
> 

## How does the subsystem carry out its goals? How does a process interact with the subsystem?

> The **TTY subsystem carries out its goals through kernel-managed TTY objects, character-device interfaces, line disciplines, and TTY drivers**. User-space processes do not normally call the TTY subsystem through a dedicated API; instead, they interact with a TTY through the standard **file-descriptor and device-file interface**. A process opens a TTY device such as `/dev/pts/3`, obtaining a file descriptor, and then uses operations such as `read()`, `write()`, and `ioctl()` on that descriptor. The kernel routes these operations through the TTY core, which coordinates the appropriate TTY driver and line discipline. For a PTY, the terminal emulator operates on the PTY master while the shell operates on the PTY slave, with the kernel TTY subsystem mediating the communication and applying terminal semantics.
> 

## What is the interaction graph of the elements? What are the elements?

| Element | Layer | Role |
| --- | --- | --- |
| **Terminal emulator** | User space | Produces/consumes terminal characters; e.g. Kitty |
| **PTY master** | Kernel TTY subsystem | Endpoint used by the terminal emulator |
| **TTY core** | Kernel | Common TTY management and I/O machinery |
| **Line discipline** | Kernel | Processes terminal input/output semantics; commonly `N_TTY` |
| **PTY driver** | Kernel | Implements the pseudo-terminal master/slave mechanism |
| **PTY slave** | Kernel | Terminal endpoint presented to the shell |
| **Shell** | User space | Interactive process, e.g. `zsh` |
| **Process group/session** | Kernel process subsystem | Supports terminal job control |
| **Terminal attributes** | Kernel TTY state | Stores modes such as canonical/raw, echo, special characters |

## What is the interaction graph of the elements?

> PTY = **two kernel endpoints** connected by a **kernel-managed bidirectional channel**.
> 

```
                         USER SPACE
────────────────────────────────────────────────────────────────────────

┌─────────────────────────┐              ┌─────────────────────────┐
│   Terminal Emulator     │              │      Shell (zsh)        │
│        Kitty            │              │        process          │
│                         │              │                         │
│      master_fd          │              │   stdin / stdout /      │
│          │              │              │        stderr            │
└──────────┼──────────────┘              └──────────┬──────────────┘
           │                                        │
           │ file descriptor                        │ file descriptor
           │                                        │
           ▼                                        ▼
        /dev/ptmx                              /dev/pts/3
           │                                        │
           │          PTY master/slave              │
           └────────────────┐  ┌────────────────────┘
                            │  │
════════════════════════════╪══╪════════════════════════════════════════
                         KERNEL SPACE
                            │  │
                    ┌───────▼──▼────────┐
                    │    TTY Subsystem   │
                    │                    │
                    │      TTY Core      │
                    └─────────┬──────────┘
                              │
                    ┌─────────▼──────────┐
                    │     PTY Driver     │
                    │                    │
                    │  PTY master ↔      │
                    │  PTY slave         │
                    └─────────┬──────────┘
                              │
                    ┌─────────▼──────────┐
                    │  N_TTY Line        │
                    │    Discipline      │
                    │                    │
                    │  • input buffering │
                    │  • echo            │
                    │  • canonical/raw   │
                    │  • special chars   │
                    └─────────┬──────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
        ┌────────▼────────┐       ┌────────▼─────────┐
        │ Terminal State  │       │    Job Control   │
        │                 │       │                  │
        │ termios         │       │ session          │
        │ modes           │       │ process groups   │
        │ special chars   │       │ foreground group │
        └─────────────────┘       │ terminal signals │
                                  └──────────────────┘
```

## Case Study

> See more in https://github.com/dbremont/linux-api-labs/tree/main/src/tty
> 

## References

- [https://github.com/torvalds/linux/tree/master/drivers/tty](https://github.com/torvalds/linux/tree/master/drivers/tty)
- https://github.com/dbremont/linux-api-labs/