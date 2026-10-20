---
tags: [package-manager, tool]
---

# Composer


> Composer is PHP's dependency management tool that implements a SAT solver (via the `composer.json`  manifest) to resolve version constraints, autoload classmaps 
(PSR-4/PSR-0), and install packages into a vendor directory while 
maintaining a lock file (`composer.lock`) for deterministic builds.
> 

## Parts

Here's a breakdown of its system type:

1. **Package Manager**: Composer is primarily a package manager for PHP, allowing developers to manage libraries and dependencies required for their PHP projects.
2. **Dependency Management Tool**: It handles the installation, updating, and removal of libraries and packages, ensuring that the right versions of dependencies are used.
3. **Open-Source**: Composer is freely available under an open-source license, allowing contributions and customizations by the community.
4. **Command-Line Interface (CLI)**: Composer operates through a command-line interface, where users can execute commands to manage dependencies and project configuration.
5. **Project Configuration**: It uses a `composer.json` file to define project dependencies and configurations, and a `composer.lock` file to lock the dependency versions.

## References

- https://getcomposer.org/