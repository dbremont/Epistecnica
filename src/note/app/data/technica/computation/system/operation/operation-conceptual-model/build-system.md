---
tags: [build-system, tool]
---

# Build System

- [Make](note.html?n=technica/computation/system/operation/operation-conceptual-model/make.md), [Meson](note.html?n=technica/computation/system/operation/operation-conceptual-model/meson.md), [Ninja](note.html?n=technica/computation/system/operation/operation-conceptual-model/ninja.md), [CMake](note.html?n=technica/computation/system/operation/operation-conceptual-model/cmake.md), [GNU Autotools](note.html?n=technica/computation/system/operation/operation-conceptual-model/gnu-autotools.md), [Apache Maven](note.html?n=technica/general/pto/maven.md), [Gradle](note.html?n=technica/computation/system/operation/operation-conceptual-model/gradle.md)

> In this note, we will explore **build systems**: the tools used to turn source code and its dependencies into software that can be executed, packaged, and delivered.
> 

## Formulation

### What is **Build System?**

> A **build system** is a system that describes and executes the transformations required to produce software artifacts from source files and other inputs.
> 

> At its core, a build system maintains a relationship of the form: **Inputs → Transformations → Artifacts**
> 

For example:

```
main.cpp ──────┐
               ├── compile ──→ main.o ──┐
math.cpp ──────┘                         │
                                         ├── link ──→ application
math.h ──────────────────────────────────┘
```

A build system therefore does more than simply invoke a compiler. It determines **what needs to be produced, what it depends on, which transformations must be performed, and when those transformations need to be performed again**.

### What technical problem does it evaluates?

> Given a set of source files and dependencies, how can we reliably and efficiently produce the required software artifacts?
> 

| Problem | What the build system does |
| --- | --- |
| **Dependency management** | Determines which inputs affect each artifact. |
| **Dependency ordering** | Executes transformations in a valid dependency order. |
| **Incremental execution** | Rebuilds only the artifacts affected by changes. |
| **Parallel execution** | Executes independent transformations concurrently. |
| **Reproducibility** | Produces the same artifacts from the same inputs and configuration. |
| **Configuration** | Selects platforms, compilers, features, and build variants. |
| **Artifact production** | Produces executables, libraries, packages, archives, containers, and other outputs. |
| **Failure propagation** | Detects failures and propagates them through the dependency graph. |
| **Caching** | Reuses previously computed results when their inputs have not changed. |

### Which capability set characterizes build systems?

> Note: A Capabilities - a feature (capacity to solve a problem), something related to the way a problem is solved.
> 

> A build system is generally characterized by the following capabilities:
> 

| Capability | Role |
| --- | --- |
| **Input declaration** | Defines source files, generated files, libraries, tools, and other inputs |
| **Dependency modeling** | Represents relationships between inputs and outputs |
| **Rule definition** | Describes how an artifact is produced |
| **Graph construction** | Builds the dependency graph from the declared rules |
| **Scheduling** | Determines the order in which work is executed |
| **Incremental execution** | Avoids unnecessary work |
| **Parallel execution** | Executes independent build actions concurrently |
| **Change detection** | Determines whether an artifact is stale |
| **Caching** | Reuses results of previous build actions |
| **Toolchain management** | Selects compilers, linkers, interpreters, generators, etc. |
| **Configuration** | Supports platforms, architectures, features, and build modes |
| **Artifact management** | Produces and organizes build outputs |
| **Reproducibility** | Controls inputs and execution conditions to make builds repeatable |
| **Packaging** | Converts build outputs into distributable artifacts |
| **Diagnostics** | Reports failed actions, dependency problems, and build information |

## System Space

```jsx
									                Build System
									                      │
									       ┌──────────────┼──────────────┐
									       ↓              ↓              ↓
									   Description     Dependency     Execution
									       │              │              │
									   declarative      explicit       local
									   imperative       implicit       parallel
									   rule-based       hashed         distributed
									                      │
									                      ↓
									                   Artifacts
									                      │
									          ┌───────────┼───────────┐
									          ↓           ↓           ↓
									       binaries    packages    containers
```

### Which are the type of build systems?

| **Type of Build System** | **Description** | Instance(s) |
| --- | --- | --- |
| **Build Executor** | Executes an already-defined build graph: schedules actions, resolves dependencies, and performs transformations. | Make, Ninja |
| **Build Generator** | Describes a project and generates a build graph or configuration for another build executor. | CMake, Meson, GNU Autotools |
| **General-Purpose Build System** | Provides an integrated model for describing, analyzing, scheduling, caching, and executing builds, often at large scale. | Bazel, Buck2, Pants |
| **Language-Integrated Build System** | Provides build, dependency, compilation, and packaging capabilities as part of a specific language ecosystem. | Cargo, Go toolchain, Mix, Swift Package Manager |
| **Ecosystem/Platform Build System** | Integrates building, dependency management, testing, packaging, and deployment around a particular platform or ecosystem. | Gradle, Maven, MSBuild |

### How are the implementation of build systems characterized?

| **Dimension** | **Description** |
| --- | --- |
| **Build Description** | How the build process and its rules are expressed and specified. |
| **Build Execution** | How build actions are scheduled and executed, e.g. sequentially, in parallel, locally, or remotely. |
| **Dependency Model** | How relationships between inputs, transformations, and outputs are represented and determined. |
| **Build Granularity** | The size of the units of work managed by the build system, such as files, compilation units, targets, or actions. |
| **Artifact Space** | The types of artifacts the build system produces, such as executables, libraries, packages, containers, or documentation. |
| **Environment** | The computational environment in which builds are performed, such as developer machines, CI servers, containers, or build clusters. |
| **Build Strategy** | How the system determines what work needs to be performed, such as always rebuilding, timestamp-based, dependency-based, or content-addressed builds. |
| **Scope** | The extent of the build graph managed by the system, from a single program or repository to a monorepo or multiple repositories. |

### Which are the set of known and used build  systems?

| Build System | Description | Characterization | Usage Note |
| --- | --- | --- | --- |
| **Make** | Rule-based build automation system based on targets, prerequisites, and commands. | Declarative-ish rules; timestamp-based dependency model; file-level granularity; local execution; incremental builds. | Classic Unix/C/C++ projects; simple and ubiquitous. |
| **Ninja** | Small, fast build execution engine designed to execute a generated build graph. | Explicit dependency graph; highly parallel execution; fine-grained actions; local execution; incremental builds. | Commonly used underneath CMake and other build generators. |
| **CMake** | Build-system generator that describes a project and generates native build files. | Declarative project description; generator-based; supports multiple backends; cross-platform configuration. | Widely used for C/C++ projects. |
| **Meson** | Modern build-system generator focused on fast, declarative project configuration. | Declarative description; Ninja-oriented execution; dependency-aware; cross-platform. | C/C++ and other compiled-language projects. |
| **Bazel** | General-purpose build system based on explicit rules and a dependency graph. | Declarative rules; content-aware/incremental builds; caching; parallel and remote execution; hermeticity. | Large codebases, monorepos, polyglot projects. |
| **Buck2** | Build system developed by Meta for large-scale software development. | Graph-based; highly parallel; incremental; remote execution/caching; extensible rules. | Large monorepos and multi-language systems. |
| **Pants** | Build system focused on large multi-language repositories. | Dependency inference; incremental execution; caching; parallelism; monorepo-oriented. | Python, Go, Java, Scala, and multi-language monorepos. |
| **Gradle** | General-purpose build automation system with a programmable build model. | Task graph; incremental execution; caching; parallel execution; extensible configuration. | JVM projects, Android, and multi-language builds. |
| **Maven** | Convention-oriented build and dependency-management system for Java. | Lifecycle-based; declarative XML configuration; dependency resolution; repository-based artifacts. | Java/JVM applications and libraries. |
| **MSBuild** | Microsoft build platform based on project files and targets. | Declarative project descriptions; target/task model; dependency graph; incremental and parallel execution. | .NET, Visual Studio, and Windows development. |
| **Ant** | Java build automation system based on explicit tasks and targets. | XML-based; task-oriented; explicit dependencies; procedural/declarative hybrid. | Older Java projects and legacy build environments. |
| **SCons** | Build system implemented in Python with Python-based build descriptions. | Programmatic build description; dependency analysis; incremental execution; platform-aware. | C/C++ and projects requiring highly programmable builds. |
| **Bazel-like systems** | Build systems centered around explicit dependency graphs, caching, and reproducible actions. | Graph-oriented; incremental; parallel; cacheable; often supports remote execution. | Large-scale and distributed software production. |
| **Cargo** | Rust's package manager and build system. | Dependency-aware; convention-based; incremental compilation; package registry integration. | Rust projects. |
| **Go toolchain (`go build`)** | Go's integrated build and dependency system. | Convention-based; dependency-aware; incremental compilation/cache; integrated tooling. | Go projects. |
| **Mix** | Elixir's build tool and project management system. | Task-oriented; dependency management; compilation; configuration; incremental builds. | Elixir projects. |
| **Swift Package Manager** | Package manager and build system for Swift. | Declarative package description; dependency resolution; compilation; platform configuration. | Swift applications and libraries. |
| **Buck2** | High-performance build system emphasizing graph evaluation and remote execution. | Fine-grained dependency graph; parallelism; caching; remote execution; extensible rules. | Large monorepos and high-scale builds. |
| GNU Autotools | Suite of tools for **generating portable build configuration and Make-based** build systems. | `autoconf` generates `configure`; `automake` generates Makefiles; `libtool` supports portable library builds; feature/platform detection; source-tree configuration. | Traditional Unix/Linux C/C++ projects; especially portable and legacy software. |

## QA

### Which are the alternatives to build tools?

## References

- https://en.wikipedia.org/wiki/List_of_build_automation_software
- https://en.wikipedia.org/wiki/Build_automation
- https://en.wikipedia.org/wiki/Software_build
- Färber, M., & Härtig, H. (2018). *Build systems à la carte: Theory and practice*. arXiv.
- CMake. (n.d.). *CMake documentation*.
- Bazel. (n.d.). *Bazel documentation*.
- GNU Project. (n.d.). *GNU Make manual*.