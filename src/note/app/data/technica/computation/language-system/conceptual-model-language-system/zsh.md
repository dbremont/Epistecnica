---
tags: [language, tool]
---

# ZSH


> Zsh (Z Shell) is a powerful and highly customizable command-line shell with many advanced features that go beyond what is available in other shells like Bash. It offers advanced tab completion, extended globbing, command-line editing, directory stack, auto-correction, plugins and themes, job control, multi-platform support, path expansion, and built-in commands. Its flexibility and extensibility make it a popular choice for power users and developers who need a powerful and efficient shell for their command-line work.
> 

> NOTE: THIS NOTE NEEDS TO BE BETTER STRUCTURE INTERFACE → IMPLEMENTATION → USAGE → QA (Build From Source, …),  Debugging, Related Project (Oh-My-Zsh).
> 

## Features

> **Zsh (short for Z Shell)** is a popular command-line shell that offers many advanced features beyond what is available in other shells like Bash.
> 

Here are some of the main features of Zsh:

| **Feature** | **Description** |
| --- | --- |
| **Tab completion** | Advanced tab completion that suggests and completes commands, options, and file names based on context. Supports auto-completion of command names and aliases. |
| **Extended globbing** | Powerful feature that allows selecting files based on advanced patterns like file size, modification time, permissions, and more. |
| **Command-line editing** | Advanced command-line editing with vi-mode and emacs-mode, enabling command line editing using key bindings similar to those in vi or emacs. |
| **Directory stack** | Maintains a directory stack, allowing quick navigation between recently visited directories using the pushd and popd commands. |
| **Auto-correction** | Automatically corrects common spelling errors and typos in command names. |
| **Plugins and themes** | Highly extensible with support for third-party plugins and themes that enhance functionality and appearance. |
| **Job control** | Advanced job control features for managing and manipulating running processes, including backgrounding, foregrounding, and suspending processes. |
| **Multi-platform support** | Runs on a wide variety of platforms, including Linux, macOS, and Windows. |
| **Path expansion** | Supports path expansion, allowing quick navigation to directories by typing part of the directory name. |
| **Built-in commands** | Includes many built-in commands for advanced functionality like text manipulation, arithmetic operations, and file system interaction. |
| **ZLE (Zsh Line Editor)** | A powerful command-line editing and customization tool providing features like history navigation, keyboard shortcuts, and customizable key bindings. |
| **Shell builtins** | Provides various built-in commands and functionalities within the shell. |

## Shell Buildints

> aka . Zsh intrinsics.
> 

> Zsh, like other programming languages, also has built-in functions (intrinsic commands) that are implemented directly by the shell itself. These functions provide low-level operations that can be used to optimize shell scripts and customize shell behavior
> 

| **Command** | **Description** |
| --- | --- |
| `zle` | Zsh Line Editor (ZLE) system for advanced command-line editing with vi-mode and emacs-mode key bindings. |
| `cd` | Changes the current working directory. |
| `echo` | Prints a message to the terminal. |
| `history` | Views or manipulates the command history. |
| `jobs` | Views or manipulates background jobs. |
| `kill` | Sends a signal to a process. |
| `pushd/popd` | Manages the directory stack. |
| `source` | Executes commands from a file. |
| `typeset/declare` | Defines and manipulates variables and functions. |
| `fg/bg` | Brings a process to the foreground or background. |
| `trap` | Sets a signal handler for a specific signal. |
| `builtin` | Runs a built-in command explicitly. |
| `test` | Evaluates expressions and returns a boolean result. |
| `time` | Measures the execution time of a command. |
| `set` | Sets shell options and parameters. |
| `unset` | Removes a variable or function definition. |
| `export` | Sets an environment variable. |
| `autoload` | Loads functions automatically when they are called (additional description not provided). |
| `zcompile` | Compiles Zsh function files into bytecode (additional description not provided). |
| `` | Empty entry—no description provided. |
| `bg` | Puts a job in the background. |
| `continue` | Resumes the next iteration of a loop. |
| `disable` | Disables a built-in shell command. |
| `eval` | Evaluates a string as a shell command. |
| `false` | Returns an unsuccessful status code. |
| `enable` | Enables a built-in shell command. |
| `exit` | Exits the shell. |
| `noglob` | Temporarily disables filename expansion (globbing). |
| `disown` | Removes a job from the job table so it is no longer tracked by the shell. |
| `fc` | Lists or edits the command history. |
|   | Lists or defines shell functions. |
| `getln` | Reads a line of input (additional description not provided). |
| `getopts` | Parses command-line options. |
| `hash` | Caches the location of commands. |
| `integer` | Declares an integer variable. |
| `local` | Declares a local variable. |
| `logout` | Logs out of the current login shell session. |
| `popd` | Pops the top directory off the directory stack and changes to it. |
| `print` | Prints arguments to the terminal. |
| `printf` | Formats and prints arguments. |
| `pushd` | Pushes a directory onto the directory stack and changes to it. |
| `pushln` | Pushes the last line to the input buffer (additional description not provided). |
| `pwd` | Prints the current working directory. |
| `r` | Re-executes a command from the history (additional description not provided). |
| `read` | Reads a line of input into a variable. |
| `readonly` | Marks variables or functions as read-only. |
| `rehash` | Rebuilds the command location hash table. |
| `return` | Exits a function with a status code. |
| `setopt` | Sets or unsets shell options. |
| `shift` | Shifts the positional parameters to the left. |
| `suspend` | Suspends the shell. |
| `ttyctl` | Controls whether terminal settings are changed by the shell (additional description not provided). |
| `times` | Prints the accumulated user and system times for the shell and its children. |
| `true` | Returns a successful status code. |
| `type` | Displays the type of command (built-in, function, alias, etc.). |
| `umask` | Sets the file creation mode mask. |
| `unalias` | Removes an alias. |
| `unfunction` | Removes a shell function. |
| `unhash` | Removes commands from the hash table. |
| `unsetopt` | Unsets shell options. |
| `wait` | Waits for a background process to finish. |
| `whence` | Displays how a command would be interpreted. |
| `where` | Locates the binary, source, and manual page for a command. |
| `zmodload` | Loads or unloads Zsh modules (additional description not provided). |
| `bindkey` | Binds key sequences to ZLE commands. |

## Modules

List the actual load modules:

```bash
zmodload -L
```

Here are some of the commonly used Zsh modules:

- **zsh/complist**: Provides advanced command line completion features.
- **zsh/parameter**: Provides advanced parameter expansion features.
- **zsh/cap**: Provides access to terminal capabilities and functions.
- **zsh/stat**: Provides access to file status information.
- **zsh/zpty**: Provides access to pseudo-terminals and the ability to control interactive programs from shell scripts.
- **zsh/regex**: Provides support for regular expressions.
- **zsh/system**: Provides access to system information and functions.
- **zsh/zselect**: Provides advanced I/O multiplexing features.
- **zsh/complete**: Provides additional command-line completion functions.

## ZSH Internals

Zsh is a powerful shell with a number of advanced features and customization options. Here are some of the key internals of Zsh:

- **Parsing**: Zsh uses a built-in parser to analyze command lines and execute them. The parser supports a variety of features, including command substitution, parameter expansion, and process substitution.
- **Prompt Expansion**: Zsh allows for customizable prompt expansion, so you can customize your shell prompt with various colors and text effects.
- **Job Control**: Zsh provides a powerful job control mechanism that allows you to manage and manipulate multiple jobs simultaneously. You can use job control to stop, start, and monitor running processes.
- **Command Line Editing**: Zsh provides advanced command line editing features, including customizable key bindings, history expansion, and spell checking.
- **Modules**: Zsh is built with a modular architecture, which allows you to load and unload modules dynamically. Modules provide additional features and functionality, such as advanced command-line completion, access to system information, and support for regular expressions.
- **Functions**: Zsh allows you to define custom functions to automate common tasks or extend the functionality of the shell. You can define functions in your .zshrc file or in a separate script.
- **Aliases**: Zsh allows you to define custom aliases to simplify and shorten command lines. Aliases are defined using the alias command, including simple string substitutions and complex command sequences.

## Build From Source

- [https://zsh.sourceforge.io/Arc/source.html](https://zsh.sourceforge.io/Arc/source.html)
- `sudo apt-get install libncurses5-dev libncursesw5-dev`
- mkdir build;   cd build; mkdir build
- `../configure \
--enable-zsh-debug \
--prefix=/home/dbremont/Downloads/zsh-5.9.2/build/build \
CFLAGS="-g -O0 -fPIC"`
- `make -j && make install`

## oh my zsh

> 

![](https://ohmyz.sh/img/OMZLogo_BnW.png)

## References

- https://zsh.sourceforge.io/Arc/source.html
- [Shebang (Unix)](https://en.wikipedia.org/wiki/Shebang_(Unix))
- [mastering-zsh](https://github.com/rothgar/mastering-zsh)
- [A Guide to the Zsh Line Editor with Examples](https://thevaluable.dev/zsh-line-editor-configuration-mouseless/)
- [The Z Shell Manual](https://zsh.sourceforge.io/Doc/Release/index.html#Top)
- [the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line)
- [A Guide to the Terminal, Console, and Shell](https://thevaluable.dev/guide-terminal-shell-console/)
- Interesting commands for the Linux shell ([lopezferrando.com](http://lopezferrando.com/)) [https://news.ycombinator.com/item?id=15246302](https://news.ycombinator.com/item?id=15246302)
- [Oh My Shell](https://ohmyz.sh/)
- [Zsh Line Editor](https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html)
- [Shell Builtin Commands](https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html)
- https://dev.to/abdfnx/oh-my-zsh-powerlevel10k-cool-terminal-1no0
- https://medium.com/@anisettyanudeep/elevate-your-terminal-exploring-the-top-zsh-themes-for-a-stylish-shell-experience-af43d21ba3dc
- oh my zsh
    - https://github.com/ohmyzsh/ohmyzsh/wiki/themes
    - https://github.com/ohmyzsh/ohmyzsh/wiki/Settings#zsh_custom
- [AWK](note.html?n=technica/computation/language-system/conceptual-model-language-system/awk.md)
- [A Collection of Bash Utilities for Everyday Tasks](https://app.notion.com/p/A-Collection-of-Bash-Utilities-for-Everyday-Tasks-195c0f5171ec805a8caed838d363d3e8?pvs=21)
- [Linux](note.html?n=technica/computation/operating-system/linux.md)
- https://zsh.sourceforge.io/FAQ/
- [**Build System**](note.html?n=technica/computation/system/operation/operation-conceptual-model/build-system.md)
- [GNU Autotools](note.html?n=technica/computation/system/operation/operation-conceptual-model/gnu-autotools.md)
- [GDB (GNU Project Debugger)](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/gdb-gnu-project-debugger.md)
- [Shell Interpreter](note.html?n=technica/computation/miscelanea/shell-interpreter.md)
- https://news.ycombinator.com/item?id=15246302