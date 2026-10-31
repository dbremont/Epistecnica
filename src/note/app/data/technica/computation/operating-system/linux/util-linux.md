---
tags: [tool]
---

# util-linux


> The **util-linux** package is a collection of essential utilities for Linux systems, many of which interact directly with the kernel or provide low-level system management capabilities.
> 

 Below is a table of the most commonly used utilities from the **util-linux** package:

| **Utility** | **Description** | **Example Command** |
| --- | --- | --- |
| **lsblk** | Lists information about block devices. | `lsblk` |
| **fdisk** | Disk partitioning tool. | `sudo fdisk /dev/sda` |
| **cfdisk** | Curses-based disk partitioning tool. | `sudo cfdisk /dev/sda` |
| **mkfs** | Creates a filesystem on a device. | `sudo mkfs.ext4 /dev/sda1` |
| **mount** | Mounts filesystems. | `sudo mount /dev/sda1 /mnt` |
| **umount** | Unmounts filesystems. | `sudo umount /mnt` |
| **swapon** | Enables swap space. | `sudo swapon /dev/sdb1` |
| **swapoff** | Disables swap space. | `sudo swapoff /dev/sdb1` |
| **blkid** | Displays UUIDs and filesystem types of block devices. | `blkid` |
| **findmnt** | Displays mounted filesystems. | `findmnt` |
| **dmesg** | Displays kernel ring buffer messages (boot and runtime logs). | `dmesg` |
| **ipcs** | Displays information about inter-process communication (IPC) resources. | `ipcs -m` |
| **ipcrm** | Removes IPC resources. | `ipcrm -m <shmid>` |
| **renice** | Changes the priority of running processes. | `renice +5 1234` |
| **chrt** | Manipulates real-time attributes of a process. | `chrt -f 99 ./program` |
| **ionice** | Sets I/O scheduling class and priority for a process. | `ionice -c 2 -n 7 ./program` |
| **taskset** | Sets or retrieves CPU affinity for a process. | `taskset -c 0,1 ./program` |
| **flock** | Manages file locks from shell scripts. | `flock /tmp/lockfile ./script.sh` |
| **logger** | Sends messages to the system log. | `logger "This is a test message"` |
| **cal** | Displays a calendar. | `cal` |
| **whereis** | Locates the binary, source, and manual pages for a command. | `whereis ls` |
| **namei** | Displays the pathname resolution of a file or directory. | `namei /usr/bin/ls` |
| **script** | Records a terminal session. | `script session.log` |
| **scriptreplay** | Replays a terminal session recorded by `script`. | `scriptreplay session.log` |
| **wall** | Sends a message to all users' terminals. | `wall "System shutdown in 5 minutes"` |
| **mesg** | Controls write access to a user's terminal. | `mesg n` |
| **col** | Filters reverse line feeds and backspaces from text. | `man ls |
| **colcrt** | Filters terminal control characters for CRT displays. | `colcrt file.txt` |
| **colrm** | Removes columns from a file. | `colrm 5 10 < file.txt` |
| **column** | Formats input into columns. | `ls -l |
| **hexdump** | Displays file contents in hexadecimal, decimal, or octal format. | `hexdump -C file.bin` |
| **hwclock** | Queries or sets the hardware clock (RTC). | `sudo hwclock --show` |
| **fallocate** | Preallocates or deallocates space for a file. | `fallocate -l 1G file.img` |
| **fsck** | Checks and repairs a filesystem. | `sudo fsck /dev/sda1` |
| **losetup** | Manages loop devices. | `sudo losetup /dev/loop0 file.img` |
| **wipefs** | Wipes filesystem signatures from a device. | `sudo wipefs /dev/sda1` |
| **setterm** | Sets terminal attributes. | `setterm -blank 10` |

## References

- https://github.com/util-linux/util-linux
- https://www.kernel.org/pub/linux/utils/util-linux/v2.41/
- https://www.rfc-editor.org/rfc/rfc9562.html