# Human Interface Device (HID)


> The **HID** class provides a **standard protocol** for human interface devices. This makes it easier for devices to be compatible with different systems (e.g., Windows, Linux, macOS) without requiring specific drivers for each device.
> 

```
User-space
  ↑
libinput / evdev / Wayland / X11
  ↑
Input Subsystem (/dev/input/eventX)
  ↑
HID Subsystem
  ↑
USB / Bluetooth / I2C Bus Drivers
  ↑
Physical Device
```

## References

- https://en.wikipedia.org/wiki/Human_interface_device
- https://en.wikipedia.org/wiki/USB_human_interface_device_class
- https://docs.kernel.org/hid/index.html