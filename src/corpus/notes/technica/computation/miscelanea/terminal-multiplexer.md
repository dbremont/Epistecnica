---
tags: [note, terminal, tooling]
---

# Terminal Multiplexer

> A **terminal multiplexer** sits between the terminal emulator and the shell. It owns one or more pseudo-terminals, runs a **session** that survives the terminal that started it, and lets several programs share one window split into panes. Its defining property is persistence: detach from the session and the programs keep running; reattach from another terminal, or another machine, and they are still there.

## What it provides

| Function | Description |
| --- | --- |
| **Session persistence** | The multiplexer's own process holds the ptys, so closing the terminal — or losing the SSH connection — does not kill the programs inside |
| **Detach / attach** | A session is left running and re-entered later, from the same host or remotely |
| **Panes and windows** | One session split into windows, each split into panes, with keyboard switching and resizing |
| **Client sharing** | Several terminals attach to the same session, which makes it a lightweight pair-programming or observation tool |
| **Scripting** | Key bindings and commands can be driven from a config file or from the command line, so layouts are reproducible |

## Tool set

| Tool | Platform | Model | Notes |
| --- | --- | --- | --- |
| **tmux** | Unix | Client–server; session → window → pane | The de facto standard: scriptable, configurable, and the terminal layer most remote work assumes |
| **GNU screen** | Unix | Session → window → region | The older tool; ubiquitous on systems where nothing else is installed |
| **zellij** | Unix | Client–server, layout files, WASM plugins | A modern alternative with a discoverable UI and declarative layouts |
| **herdr** | Cross-platform, Rust | Workspace manager with tabs and panes plus **agent orchestration** | The variant aimed at coding agents: it treats a running agent as a first-class pane, alongside the shell and the editor — [repository](https://github.com/herdrdev/herdr) |

## The model

> The stack is: **terminal emulator** (pixels, fonts, input) → **multiplexer** (ptys, sessions, panes) → **shell** → **program**. The pseudo-terminal is the seam. The multiplexer allocates one per pane, so a program inside a pane cannot tell whether it is running under a multiplexer or a real terminal — which is also why signals, window sizes and job control behave the same way in both.

> This is the distinction against the emulator note: an emulator renders a pty for a human, a multiplexer *owns* ptys and survives the renderer. They compose — Kitty runs tmux, tmux runs Vim — and confusing them is the usual reason a "terminal setup" recommendation does not apply to the question asked.

## References

- [herdrdev/herdr — GitHub](https://github.com/herdrdev/herdr) — the agent-runtime multiplexer
- [tmux — Wikipedia](https://en.wikipedia.org/wiki/Tmux)
- [GNU Screen — Wikipedia](https://en.wikipedia.org/wiki/GNU_Screen)
- [Zellij — website](https://zellij.dev/)
- [Pseudoterminal](/view.html?p=notes/technica/computation/operating-system/linux/pseudoterminal.md) — the interface a multiplexer allocates per pane
- [Terminal Emulator](/view.html?p=notes/technica/computation/miscelanea/terminal-emulator.md) — the layer below, which this note is not
