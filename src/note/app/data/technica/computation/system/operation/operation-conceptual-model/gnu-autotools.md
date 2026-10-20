---
tags: [build-system, tool]
---

# GNU Autotools

- [Build System](note.html?n=technica/computation/system/operation/operation-conceptual-model/build-system.md)

> The **GNU Autotools**—primarily **Autoconf, Automake, and Libtool**—are a family of tools for generating portable build systems for Unix-like software projects.
> 

> They are best understood as a **build-system generator and configuration framework** rather than as a build executor. The generated build system is normally executed by **GNU Make**.
> 

> NOTE: What i the role of `autoheader`, and `aclocal?`  Are they represented correctly on this note?
> 

## Formulation

> What is ‘GNU Autotools’? What kind of technical production system is this?
> 

> GNU Autotools is a **build-system generation framework**.
> 

> Its purpose is to transform a relatively portable description of a software project into a build system that can adapt to the particular machine, operating system, compiler, libraries, and platform capabilities on which the software is being built.
> 

### How does GNU Autotools `model`the build workflow?

> Note: I don’t like the term model here.
> 

> The **GNU Autotools workflow** is essentially a pipeline from a **human-maintained build description** to a **configured Make-based build system**.
> 

| Stage | System | Role |
| --- | --- | --- |
| **Description** | `configure.ac`, `Makefile.am` | Describe project configuration and build structure |
| **Generation** | Autotools | Generate the build system |
| **Configuration** | `./configure` | Adapt the generated system to the target machine |
| **Execution** | GNU Make | Execute the build graph |
| **Compilation** | Compiler | Transform source into object/code artifacts |
| **Linking** | Linker / Libtool | Produce executables and libraries |

```jsx
configure.ac / Makefile.am
          │
          ▼
     GNU Autotools
          │
          ├── autoconf ──► configure
          │
          └── automake ──► Makefile.in
                              │
                              ▼
                         ./configure
                              │
                              ▼
                           Makefile
                              │
                              ▼
                         GNU Make
                              │
                              ▼
                    compiler / linker
```

## Interface

> What it’s interface? Which are the parts?
> 

> The Autotools interface consists primarily of **project description files, generated artifacts, configuration commands, and conventions**.
> 

### Interface Surface

| Interface element | Purpose |
| --- | --- |
| `configure.ac` | Describes configuration requirements and platform checks |
| `Makefile.am` | Describes build targets, sources, libraries, programs, and installation |
| `aclocal.m4` | Locally collected/custom Autoconf macros |
| `config.h.in` | Template for configuration header |
| `m4/` | Project-specific Autoconf macros |
| `./configure` | User-facing configuration interface |
| `Makefile` | User-facing build interface |
| `make install` | Installation interface |
| `make clean` | Cleanup interface |
| `make dist` | Source-distribution interface |

### Which are the set of capabilities?

> GNU Autotools provides capabilities for:
> 

| Capability | Description |
| --- | --- |
| **Platform detection** | Determine properties of the host/build environment |
| **Compiler detection** | Find and test C/C++ and other compilers |
| **Feature detection** | Determine whether APIs, headers, functions, types, or tools exist |
| **Dependency detection** | Check for required libraries and external components |
| **Configuration** | Produce configuration appropriate to the target system |
| **Build description** | Describe programs, libraries, sources, tests, and installation |
| **Portability** | Hide many Unix-platform differences behind generated logic |
| **Library portability** | Libtool abstracts platform-specific shared/static library handling |
| **Installation** | Generate standard installation targets |
| **Distribution** | Generate source distributions and distribution checks |
| **Testing integration** | Provide conventions and targets for running project tests |

## Implementation

> Which are the internal elements? Which are the elements supporting the interface? Which are the external dependencies? Which are the guiding principles of the implementation?
> 

> GNU Autotools is implemented as a collection of generators, macro processors, shell scripts, templates, and conventions.
> 

> **Autotools represents the build at a higher level through configuration and build descriptions, generates an executable Make-based representation of that workflow, and delegates actual build execution to GNU Make and the compiler toolchain.**
> 

| Implementation Element | Type | Description | Role |
| --- | --- | --- | --- |
| `configure.ac` | **Build configuration description** | Declarative description of system requirements, feature tests, tools, and configuration decisions | Defines **what must be discovered/configured** |
| `Makefile.am` | **Build description** | Declarative description of programs, libraries, sources, targets, installation, and dependencies | Defines **what must be built** |
| Autoconf | **Build-system generator** | Processes `configure.ac` and generates the `configure` script | Generates the **configuration workflow** |
| Automake | **Build-system generator** | Processes `Makefile.am` and generates `Makefile.in` templates | Generates the **build workflow representation** |
| Libtool | **Portability abstraction** | Provides portable machinery for building and linking libraries | Abstracts **platform-specific library construction** |
| M4 | **Macro processor** | Expands Autoconf macros into shell/configuration logic | Provides the **metaprogramming mechanism** behind Autoconf |
| `configure` | **Configuration program** | Generated shell script that probes the target system and substitutes configuration values | **Instantiates** the build system for a particular environment |
| `Makefile.in` | **Build-system template** | Generated template containing project build rules plus configuration substitutions | Intermediate representation of the **build workflow** |
| `config.h.in` | **Configuration template** | Template for configuration-dependent C/C++ preprocessor definitions | Represents **compile-time configuration state** |
| `./configure` | **Configuration interface** | User executes the generated configuration program with options such as `--prefix` | Selects and establishes the **target build configuration** |
| `Makefile` | **Build execution description** | Configured Makefile containing concrete paths, flags, dependencies, and targets | Provides the **executable build workflow** to Make |
| `config.h` | **Configuration artifact** | Concrete configuration header generated from `config.h.in` | Makes detected system properties available to the **source code** |
| `autoreconf` | **Orchestration tool** | Runs the necessary Autotools generators in the appropriate sequence | Regenerates the **complete build-system machinery** |
| GNU Make | **Build executor** | Reads the generated `Makefile` and executes its depende |  |

## Usage

> How to used the tool?
> 

| Use Case | Description | How to? |
| --- | --- | --- |
| **Create a build system** | Define how programs and libraries are built without manually writing complete Makefiles | Write `configure.ac` and `Makefile.am`, then run `autoreconf --install` |
| **Configure for a platform** | Adapt the build to the compiler, operating system, libraries, and capabilities available on the target system | Run `./configure` |
| **Build the project** | Execute the generated build workflow | Run `make` |
| **Run tests** | Execute the project's test suite through generated Make targets | Run `make check` |
| **Install the software** | Install the generated artifacts into the configured installation prefix | Run `make install` |
| **Clean build artifacts** | Remove generated compilation artifacts | Run `make clean` |
| **Configure optional features** | Enable, disable, or customize build features | Run `./configure --enable-<feature>` or `./configure --disable-<feature>` |
| **Select installation location** | Control where the software is installed | Run `./configure --prefix=/path` |
| **Build portable libraries** | Handle platform-specific shared/static library construction | Use Libtool and build with `make` |
| **Regenerate the build system** | Update generated files after changing `configure.ac` or `Makefile.am` | Run `autoreconf --install` |
| **Create a source distribution** | Package the project with the files required to reproduce the build | Run `make dist` |
| **Validate the distribution** | Check that the generated source package can be configured and built | Run `make distcheck` |

## QA

### Which are the tool that compose the toolbox?

> The major GNU Autotools components can be characterized as follows:
> 

| **Tool** | **Input** | **Output** | **Primary Role** |
| --- | --- | --- | --- |
| **Autoconf** | `configure.ac` | `configure` | Build-system configuration generator |
| **Automake** | `Makefile.am` | `Makefile.in` | Makefile generator |
| **Libtool** | library build information | library build machinery | Portable library construction |
| **Autoheader** | `configure.ac` | `config.h.in` | Configuration-header generator |
| **Autoreconf** | Autotools project | regenerated artifacts | Build-system regeneration orchestrator |
| **M4** | macro input | expanded text | Macro-processing substrate |
| **Aclocal** | macro usage | `aclocal.m4` | Macro collection |

The relationship can be summarized as:

```
                    GNU Autotools
                         │
        ┌────────────────┼────────────────┐
        │                │                │
     Autoconf         Automake         Libtool
        │                │                │
        ▼                ▼                ▼
   configure        Makefile.in     library machinery
        │                │
        └──────────┬─────┘
                   ▼
              ./configure
                   │
                   ▼
                Makefile
                   │
                   ▼
                GNU Make
```

### How to specify the build directory?

> It’s done **indirectly through the directory from which `configure` is executed**. By running `configure` from a separate directory, Autotools creates the generated build files and artifacts there, keeping the source directory clean. This is known as an **out-of-source build**.
> 

```bash
mkdir build
cd build
../configure
make
```

Here, `build/` becomes the **build directory**, while `../` points to the source directory containing `configure`.

## References

- [Using Autotools](https://developer-old.gnome.org/anjuta-build-tutorial/stable/create-autotools.html.en)
- [The Basics of Autotool](https://devmanual.gentoo.org/general-concepts/autotools/index.html)
- [GNU Autotools: a tutorial](https://elinux.org/images/4/43/Petazzoni.pdf)
- [Philosophia Artium Technicarum et Operis](https://app.notion.com/p/Philosophia-Artium-Technicarum-et-Operis-355c0f5171ec808b82f8d7a85e8134cd?pvs=21)