---
tags: [build-system, tool]
---

# Make

- [Build System](note.html?n=technica/computation/system/operation/operation-conceptual-model/build-system.md)

> **Make** is a build automation tool that determines the dependencies between source files and the necessary commands to build target files (such as executable programs or libraries). It uses a **Makefile** to define rules for building these targets. The basic function of Make is to evaluate file modification timestamps, compare them against their dependencies, and execute a series of commands to update out-of-date targets.
> 

> **Target**: The file or object that make is responsible for creating or updating (e.g., executable, object file).
> 

> **Dependency**: A file that is required to build a target, such as source files or header files.
> 

> **Rule**: Defines how to build a target from its dependencies. A rule consists of a target, dependencies, and a set of commands to execute if the target is out-of-date.
> 

> **Makefile**: A file that contains a series of rules and definitions for the build process. It typically specifies targets, dependencies, and commands for building software.
> 

> **Timestamp-based Build System**: Make checks to the modification timestamps of files to determine if a target needs to be rebuilt. If a dependency is newer than the target, the target will be rebuilt.
> 

> **Implicit and Explicit Rules**: Make supports both implicit rules (built-in rules for common file types) and explicit rules (user-defined rules).
> 

> **Variables**: Makefiles can include variables to store values like compiler options, directories, or paths, which can be reused across rules.
> 

> **Shell Execution**: Make executes the build commands in the context of a shell (e.g., `/bin/sh`), which allows for the use of typical shell commands like `gcc`, `cp`, `rm`, etc.
> 

QA

- How to pass the values of variables in make files? [How to pass the values of variables in make files?](note.html?n=technica/computation/system/operation/operation-conceptual-model/make.md)

## Flags

| **Flag** | **Description** |
| --- | --- |
| `-f <file>` | Use a different makefile. Defaults to `Makefile` or `makefile`. |
| `-j <n>` | Run multiple jobs in parallel. `<n>` specifies the number of jobs. |
| `-k` | Continue building other targets even if one fails. |
| `-n` | Show the commands that would be executed without actually running them. |
| `-B` | Force all targets to be rebuilt, even if they are up to date. |
| `-C <dir>` | Change to directory `<dir>` before reading the makefile or doing any work. |
| `-s` | Suppress the output of commands while building. |
| `-v` | Display the version of `make`. |
| `-p` | Print the internal data structures (rules, variables) for debugging. |
| `-t` | Update the timestamps of targets without actually building them. |
| `-l <load>` | Limit the number of jobs based on the system load average. |
| `V=1` | Enable verbose output, showing all commands that `make` runs. |
| `--environment-overrides` | … |

## Makefile

> A `Makefile` follows a specific syntax based on rules, dependencies, and commands.
> 

The basic structure is:

- **Targets**: The output files or actions being created.
- **Dependencies**: Files required before executing the target.
- **Commands**: Shell commands (must be indented with a **TAB**, not spaces).

### **Variables**

> **Conditional Variable Assignment:**  The `?=` operator is used to assign a value to a variable **only if the variable is not already defined**. If the variable already has a value, the assignment is ignored.
> 

```
CC = gcc
CFLAGS = -Wall -O2
VARIABLE ?= value

program: main.o utils.o
    $(CC) $(CFLAGS) -o program main.o utils.o

```

## Rules

```
target: dependencies: <file or target>
    command

```

```
all: program

program: main.o utils.o
    gcc -o program main.o utils.o

main.o: main.c
    gcc -c main.c

utils.o: utils.c
    gcc -c utils.c

clean:
    rm -f *.o program

```

### Pattern Rules

> and  {`$<`,  `$@`,  `$^`} as automatic variables.
> 
- `%.o`: Matches any object file.
- `%.c`: Matches the corresponding source file.
- `$<`: Refers to the first dependency (the source file).
- `$@`: Refers to the target (the object file).
- `$^` → All dependencies

```bash
%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@
```

### **Phony Targets** (Prevent conflicts with filenames)

```
.PHONY: clean

```

## How to pass the values of variables in make files?

```bash
# Default compiler assignment
# This sets the default value of `CC` to `gcc` if no other value is provided.
CC = gcc

# **Override from the Command Line**
# You can override the `CC` variable when running `make`:
make CC=clang
# This will use `clang` instead of the default `gcc`.

#  **Using Environment Variables**
# You can set the `CC` variable in your environment before running `make`:
export CC=clang
make
```

## References

- https://www.gnu.org/software/make/manual/make.html
- http://wiki.osdev.org/Makefile
- https://en.wikipedia.org/wiki/Make_(software)
- [A Short Introduction to Makefile](https://www3.nd.edu/~zxu2/acms60212-40212/Makefile.pdf)
- https://makefiletutorial.com/ **`[Great Tutorial]`**
- Stallman, R. M., McGrath, R., & Smith, P. D. (2001). GNU make.
- https://ocw.mit.edu/courses/1-124j-foundations-of-software-engineering-fall-2000/pages/lecture-notes/gnu_makefile_documentation/