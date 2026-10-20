---
tags: [initialization]
---

# GRUB: GNU GRand Unified Bootloader

- [Booting (Initialization)](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/booting-initialization.md)

> **GRUB (GNU GRand Unified Bootloader)** is a versatile **bootloader** program used to manage and boot multiple operating systems on a computer.
> 

> /etc/default/grub & /etc/grub.d/folder is like a description of the actual grub file that must be generated using update-grub to generate the /boot/grub/grub.cfg, which is the actual file.
> 

Config File Location: /etc/default/grub

The `/etc/default/grub` configuration file is used in Linux distributions, particularly those using the GRUB (Grand Unified Bootloader) bootloader, to define various boot-related settings in a plain text format. Here’s a description of the `/etc/default/grub` config file format:

1. **Key-Value Pairs**: The file consists of key-value pairs, where each line represents a specific configuration parameter.
2. **Syntax**: The syntax for each line is typically `KEY="VALUE"`. The key is a configuration parameter, and the value is the setting associated with that parameter. The key and value are enclosed in double quotes.
3. **Comments**: Lines beginning with a hash (`#`) symbol are treated as comments and are ignored by the configuration parser.
4. **Default Values**: This file contains default values for various bootloader settings, such as the default boot menu timeout, the default boot entry, and kernel options. These values are used when generating the GRUB configuration file, typically at `/boot/grub/grub.cfg`.
5. **Customization**: System administrators can edit this file to customize bootloader settings according to their requirements, such as changing the default boot entry, specifying kernel command-line parameters, or adjusting the timeout for the boot menu.

## Representation

> Example `/etc/default/grub` file:
> 

```
# Default GRUB settings
GRUB_DEFAULT="0"
GRUB_TIMEOUT="5"
GRUB_TIMEOUT_STYLE="menu"

# Kernel options
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
GRUB_CMDLINE_LINUX=""

# Advanced options
GRUB_DISABLE_RECOVERY="true"
GRUB_TERMINAL="console"
```

In this example, the file sets the default boot entry to the first entry (`GRUB_DEFAULT="0"`), configures a boot menu timeout of 5 seconds (`GRUB_TIMEOUT="5"`), and specifies kernel command-line options (`GRUB_CMDLINE_LINUX_DEFAULT` and `GRUB_CMDLINE_LINUX`). These settings will generate the final GRUB configuration file that controls the boot process.

## References

- [GNU GRUB](https://en.wikipedia.org/wiki/GNU_GRUB)
- [GRUB: GNU GRand Unified Bootloader](https://en.wikipedia.org/wiki/GNU_GRUB)