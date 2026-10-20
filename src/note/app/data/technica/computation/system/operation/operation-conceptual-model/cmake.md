---
tags: [build-system, tool]
---

# CMake

- [Build System](note.html?n=technica/computation/system/operation/operation-conceptual-model/build-system.md)

> CMake is an open-source cross-platform build system and configuration tool designed to manage the build process of software projects.
> 

> CMake Variables: `cmake -L`
> 

![](https://earthly.dev/blog/assets/images/cmake-vs-make-diff/5Gv149z.png)

cmake

## CMake workflow

The CMake workflow typically involves the following steps:

1. **CMakeLists.txt Creation:** Create a `CMakeLists.txt` file in the root directory of your project, defining project details, dependencies, and build targets.
2. **Configuration:** Run CMake to configure the project, specifying build options, target platforms, and generator (e.g., Makefiles, Visual Studio project, Xcode project).
3. **Generation:** CMake generates the build system files based on the specified configuration and target platform.
4. **Build:** Use the generated build system (e.g., Make, Ninja, Visual Studio) to build the project, compile source files, and link libraries.
5. **Testing:** Run tests (if defined in `CMakeLists.txt`) to ensure the project’s correctness.
6. **Installation (Optional):** Optionally, install the built files in the system directories or at a custom location.
7. **Packaging (Optional):** You can optionally package the built files into a distributable format (e.g., ZIP, DEB, RPM).
8. **Maintenance:** As the project evolves, update the `CMakeLists.txt` to accommodate changes and repeat the configuration, generation, and build steps as needed.

## References

- [CMake](https://aosabook.org/en/v1/cmake.html)
- [Ninja](https://ninja-build.org/)
- https://izzys.casa/2019/02/everything-you-never-wanted-to-know-about-cmake/