# ioctl


## What is `ioctl`?

- **`ioctl`** stands for **Input/Output Control**.
- It's a **system call** in Unix/Linux used for device-specific input/output operations and other operations that can't be expressed by regular system calls (`read`, `write`, etc.).
- Allows user-space programs to **send commands or control requests directly to device drivers**.

---

## How `ioctl` works

- Each device driver defines a set of **ioctl commands** it understands.
- A user program calls:
    
    ```c
    int ioctl(int fd, unsigned long request, void *argp);
    
    ```
    
    - `fd`: file descriptor for the device (e.g., `/dev/dri/card0` for GPU).
    - `request`: device-specific command code.
    - `argp`: pointer to data passed to or from the driver.
- The kernel passes the request to the device driver’s ioctl handler.
- The driver performs the requested operation (e.g., configure device, submit commands, query info).

## Using `ioctl` with the Intel GPU driver

- Intel GPUs use the **Direct Rendering Manager (DRM)** subsystem in Linux.
- The Intel GPU device node is usually `/dev/dri/card0`.
- DRM exposes many ioctl commands for buffer management, context creation, command submission, synchronization, etc.
- To interact with Intel GPU at a low level, you open `/dev/dri/card0` and call ioctl commands defined by DRM and Intel driver.

## Example

```c
int fd = open("/dev/dri/card0", O_RDWR);
if (fd < 0) {
    perror("open");
    return -1;
}

int ret = ioctl(fd, DRM_IOCTL_SOME_COMMAND, &some_data);
if (ret < 0) {
    perror("ioctl");
    return -1;
}

// use driver response...
close(fd);
```

## Summary

| Aspect | Description |
| --- | --- |
| `ioctl` syscall | Interface to send commands to drivers |
| Device file | `/dev/dri/card0` for Intel GPU DRM driver |
| Commands | Driver-specific codes to control hardware |
| Usage | Open device, call ioctl, close device |

## References

- https://en.wikipedia.org/wiki/Ioctl
- https://man7.org/linux/man-pages/man2/ioctl.2.html
- https://docs.kernel.org/driver-api/ioctl.html