---
tags: [configuration, metadata]
---

# pkg-config


> Package: pkgconf-bin
> 

> **pkg-config** is a **build configuration and metadata retrieval system** used in Unix-like operating systems to **simplify the discovery and integration of software libraries** during the compilation and linking stages of software development. It provides a standardized mechanism for querying metadata about installed libraries, including compiler flags, linker options, and dependency resolution, ensuring consistency and portability across different build environments.
> 

QA:

- What is `pkg-config`, and why is it used in build systems?
- How does `pkg-config` determine which package metadata to use?
- What command would you use to retrieve the compiler flags for a library?
- How do you check if a package is installed using `pkg-config`?
- Where does `pkg-config` search for `.pc` files by default?
- What is the difference between `PKG_CONFIG_PATH` and `PKG_CONFIG_LIBDIR`?
- How does `PKG_CONFIG_SYSROOT_DIR` affect package resolution in cross-compilation?
- How can you specify additional directories for `pkg-config` to search?
- Where does `pkg-config` search for `.pc` files by default?
- How does CMake handle `pkg-config` dependencies via `find_package(PkgConfig)`?
- How can you specify platform-specific paths (e.g., Windows vs. Linux) in a `.pc` file?
- What steps would you take if `pkg-config` returns an incorrect version of a package?
- How do you ensure that `pkg-config` uses a custom `.pc` file rather than a system-installed one?
- How does Meson use `pkg-config` for dependency resolution?
- How can `pkg-config` be used in a raw Makefile without a build system like CMake or Meson?
- How does `pkg-config --static` affect the output?
- …

## Uses

> Provides a command-line tool (`pkg-config`) to retrieve library metadata via structured queries:
> 
- `pkg-config --cflags <package>` → Compiler flags.
- `pkg-config --libs <package>` → Linker flags.
- `pkg-config --modversion <package>` → Library version.
- `pkg-config --exists <package>` → Check availability.
- `pkgconf --validate <package>`	→ Validates the .pc file for a package.
- `pkg-config --list-all` → List all modules found in the pkg-config path.
- `PKG_CONFIG_DEBUG_SPEW=1 pkg-config --exists zlib` → **Shows verbose debug output**, including all paths searched and detailed information about how `pkg-config` tries to locate the `.pc` file for `zlib`.
- `pkg-config --variable=pc_path pkg-config` → **Lists the default search paths** used by `pkg-config` to locate `.pc` files, as a colon-separated string.

## **Metadata Storage & Format**

> Uses **`.pc` (package configuration) files** stored in **predefined directories** (e.g., `/usr/lib/pkgconfig/`, `/usr/share/pkgconfig/`), containing:
> 
- **Library Name** (`Name`)
- **Version Information** (`Version`)
- **Compilation Flags** (`Cflags`)
- **Linking Flags** (`Libs`, `Libs.private`)
- **Dependencies** (`Requires`, `Requires.private`)

## Dependency Model

> Resolves **direct and transitive dependencies** using `Requires` and `Requires.private`, ensuring proper linkage of statically or dynamically linked libraries.
> 

## Search Path Customization

> Supports **environment variable overrides** (`PKG_CONFIG_PATH`, `PKG_CONFIG_LIBDIR`) to facilitate cross-compilation and multi-architecture package resolution.
> 

## References

- https://github.com/pkgconf/pkgconf