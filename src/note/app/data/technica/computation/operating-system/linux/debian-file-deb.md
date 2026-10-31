---
tags: [tool]
---

# Debian File (deb)


A Debian package file, often denoted with the `.deb` extension, is a binary package format used by the Debian and Debian-based Linux distributions (such as Ubuntu) for packaging and distributing software. The `.deb` file format has a specific structure and includes various components:

1. **Control Information**:
    - `DEBIAN/control`: This file contains metadata and control information about the package, including its name, version, description, dependencies, maintainer details, and more.
2. **Installation Scripts**:
    - `DEBIAN/preinst`: A script executed before installation.
    - `DEBIAN/postinst`: A script executed after installation.
    - `DEBIAN/prerm`: A script executed before removal.
    - `DEBIAN/postrm`: A script executed after removal.
3. **Package Files**:
    - The actual files and directories that make up the software package, organized according to the Filesystem Hierarchy Standard (FHS).
4. **Configuration Files**:
    - `DEBIAN/conffiles`: A list of configuration files included in the package.
    - Configuration files within the package.
5. **Control Scripts**:
    - `DEBIAN/config`: A configuration script for the package.
    - `DEBIAN/templates`: Template files for configuring the package interactively.
6. **Documentation**:
    - `/usr/share/doc/package/`: Directory containing documentation related to the package.
7. **Optional Files and Directories**:
    - `/usr/share`: Contains architecture-independent data files.
    - `/usr/lib`: Contains architecture-dependent library files.
    - `/usr/bin`: Contains executable binary files.
    - `/etc`: Contains system-wide configuration files.
    - `/var`: Contains variable data files and logs.
    - `/usr/share/man`: Contains manual pages.
8. **Checksums and Signatures**:
    - `DEBIAN/md5sums`: Checksums of files within the package.
    - `DEBIAN/sha256sums`: SHA-256 checksums of files within the package.
    - `DEBIAN/sha1sums`, `DEBIAN/sha512sums`, etc.: Additional checksum files.
    - Digital signatures (if the package is signed for authenticity and integrity).

The `.deb` file format is used primarily for packaging and distributing software on Debian-based Linux distributions. The `dpkg` command is commonly used to install, manage, and remove `.deb` packages, while tools like `apt` and `apt-get` provide higher-level package management capabilities, including resolving dependencies and fetching packages from repositories.