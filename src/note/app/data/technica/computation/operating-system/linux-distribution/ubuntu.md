# Ubuntu

> 

## Index

QA:

- How to characterize Ubuntu? Linux Kernel  + System D + …
- How to disable icons package downloads?
- What is the relation of Ubuntu vs System-d?
- How can the systemd service `systemd-resolved` fail to resolve DNS requests?
- In which configuration file is the DNS server address stored? It is /etc/resolv.conf.
    - Who used `/etc/resolv.conf?`

## **Package Management System**

> An **Ubuntu repository** is a collection of software packages, hosted on remote servers, that users can install, update, and manage via the **APT (Advanced Package Tool)** system.
> 

> An **Ubuntu mirror** is a duplicate copy of the official Ubuntu repository, hosted on different servers worldwide to improve download speed, reduce server load, and provide regional access to software packages.
> 

> **Package Management System** *(APT, dpkg, Snap, Flatpak)*
> 

> **Ubuntu Repositories & Mirrors** *(Main, Universe, Multiverse, Restricted, PPAs)*
> 

Definitions:

- **Main** – Officially supported, open-source software.
- **Restricted** – Proprietary drivers and software.
- **Universe** – Community-maintained, open-source software.
- **Multiverse** – Software with licensing restrictions.
- **Security (`jammy-security`)** – Critical security updates.
- **Updates (`jammy-updates`)** – Bug fixes and minor improvements.
- **Backports (`jammy-backports`)** – Newer versions of software.

```bash
cat /etc/apt/sources.list
ls  /etc/apt/sources.list.d/
```

```bash
# Example /etc/apt/sources.list for Ubuntu 22.04 (Jammy)
deb http://archive.ubuntu.com/ubuntu jammy main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu jammy-updates main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu jammy-security main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu jammy-backports main restricted universe multiverse

deb http://archive.canonical.com/ubuntu jammy partner
```

```bash
sudo apt update
sudo apt install netselect-apt
sudo netselect-apt

## Analyze and Swith fo Faster Mirrors
sudo apt install software-properties-common
sudo apt update
sudo apt install apt-transport-https ca-certificates
sudo add-apt-repository 'deb mirror://mirrors.ubuntu.com/mirrors.txt jammy main restricted universe multiverse'

## Enable All Repositories (Optional)
sudo add-apt-repository multiverse
sudo add-apt-repository universe
sudo add-apt-repository restricted
sudo apt update

# Final Step: Full System Update & Fix Broken Packages
sudo apt update && sudo apt full-upgrade -y
sudo apt --fix-broken install
```

## DEP-11

> **DEP-11** refers to a metadata format used by the Advanced Package Tool (APT) system on Debian-based distributions like Ubuntu. It is specifically designed to improve the user experience when managing software packages, particularly in graphical environments like the Ubuntu Software Center or Synaptic Package Manager.
> 

> It’s standard that Graphical Package Managers Used;
> 

> **Purpose**: DEP-11 provides additional metadata that enhances the way packages are displayed in GUI-based package managers. This metadata includes things like package icons, categories, and detailed descriptions.
> 

> **Icon Information**: One of the most noticeable features of DEP-11 is the inclusion of package icons, which are used to visually represent packages in graphical package managers (e.g., icons like `48x48` or `64x64` pixels). These icons help users quickly recognize and differentiate packages.
> 

> **Package Categories and Descriptions**: DEP-11 can also provide categories for packages (e.g., "Office," "Games," "Internet") and more detailed textual descriptions, making it easier for users to search and navigate through large collections of software in a GUI package manager.
> 

## Desktop & UI

> **Graphical User Interface**: GNOME
> 

> **Display Server**: X11, Wayland
> 

> **Development & Customization**: GSettings, Dconf, Tweaks
> 

## References

- https://ubuntu.com/
- https://wiki.debian.org/DEP-11
- https://en.wikipedia.org/wiki/AppStream
- https://askubuntu.com/questions/823329/how-do-i-disable-fetching-of-dep-11-files