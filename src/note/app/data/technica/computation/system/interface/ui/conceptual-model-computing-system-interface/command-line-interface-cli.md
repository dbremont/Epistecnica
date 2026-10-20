# Command-line Interface (CLI)


> A **CLI UI** (Command-Line Interface User Interface) is a way for users to interact with a program through the **terminal or command line**, rather than a graphical interface. Unlike traditional GUIs with buttons and windows, a CLI UI provides a structured, often interactive text-based interface.
> 

## Formulation

> A **CLI UI** (Command-Line Interface User Interface) is a **text-based interface that allows users to interact with a program through the terminal or command line**. Unlike graphical user interfaces (GUIs), a CLI UI relies entirely on text, but it can be **interactive and structured**, often including menus, prompts, forms, tables, and progress indicators.
> 

Key characteristics:

- **Text-based:** Everything is displayed using characters in the terminal.
- **Interactive:** Supports navigation, selection, and input using the keyboard.
- **Lightweight:** Runs in a terminal without a graphical environment.
- **Structured:** Can organize data, show progress, or simulate GUI-like elements using text.

### Feature Set

> Which are the building blocks of CLI UI’s?
> 

Common features of CLI UIs include:

- **Interactive Menus:** Arrow-key navigation, multi-level menus
- **Forms and Prompts:** Input fields with type validation and default values
- **Progress Indicators:** Loading bars, spinners, percentage completion
- **Tables and Grids:** Well-formatted textual data representation
- **Text Styling:** Colors, bold/italic, highlights for emphasis
- **Keyboard Shortcuts:** Quick actions without typing full commands
- **Logging and Output Control:** Verbosity levels, filters, paging

### Underlying Support

> How this building blocks are supported by the underlying elements?
> 

Building CLI UIs often relies on libraries that abstract terminal control and input handling. Core aspects of underlying support include:

- **Terminal Control:** Cursor positioning, screen clearing, resizing
- **Input Handling:** Non-blocking key detection, multi-key sequences
- **Text Rendering:** Colors, styles, alignment, and wrapping
- **Event Loop / Async Support:** To handle dynamic updates and user actions

## Toolbox

Popular libraries and tools for CLI UI development:

| Language | Library (Tool) | Notes |
| --- | --- | --- |
| Python | `rich` | Rich text, tables, progress bars, syntax highlighting |
| Python | `textual` | Full TUI framework with layout and widgets |
| Python | `prompt_toolkit` | Advanced input prompts, autocompletion |
| Node.js | `ink` | React-style component rendering in terminal |
| Node.js | `blessed` | Terminal interface library, supports widgets |
| Go | `bubbletea` | Modern TUI framework inspired by Elm architecture |
| Go | `tview` | Rich widgets for tables, forms, modals |
| Rust | `tui-rs` | Terminal UI library with flexible layouts |
| Rust | `crossterm` | Cross-platform terminal control |

## Case Study

| **CLI UI** | **Description** | **Characterization** |
| --- | --- | --- |
| **Python Installer CLI** | Interactive installer for a Python package that guides the user through installation options. | Menu-driven; prompts for input; progress bars; success/error indicators; colors for emphasis. |
| **Git** | Version control system interface used entirely via terminal commands. | Command-driven; linear input/output; some interactive prompts (e.g., merge conflicts). |
| **htop** | Real-time system monitoring tool in the terminal. | Dynamic TUI; tables for processes; keyboard navigation; color-coded metrics; live updates. |
| **npm init** | Node.js project scaffolding tool that asks users a series of setup questions. | Prompt-driven; form-like input; linear wizard flow; default values and validation. |
| **aws-cli configure** | AWS command-line configuration setup. | Prompted input; validation; secure storage of credentials; linear step-by-step flow. |

## References

- https://click.palletsprojects.com/en/stable/
- https://rich.readthedocs.io/en/latest/index.html