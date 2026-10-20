# Mouse


> In Linux, the kernel models the mouse as part of the Input Subsystem, which abstracts hardware interactions and provides a unified interface to user-space. The mouse is typically exposed via `evdev` (event device) or legacy /dev/input/mouseX nodes.
> 

> The Linux mouse I/O model follows an interrupt-driven event-based architecture, where hardware signals are captured by HID/PS2 drivers, processed by the Input Subsystem, and exposed via evdev (/dev/input/eventX) or legacy nodes (/dev/input/mouseX), enabling user-space applications like libinput, X.Org, and Wayland to interpret and act on mouse events.
> 

| **Layer** | **Description** |
| --- | --- |
| **Hardware Layer** | The physical mouse (USB, PS/2, Bluetooth). |
| **Bus Interface Layer** | The communication method (USB HID, PS/2, Bluetooth HID). |
| **Device-Specific Driver** | `usbhid.ko` (USB), `psmouse.ko` (PS/2), `hidp.ko` (Bluetooth). |
| **Input Core Subsystem** | Standardizes input events via `input.c`, `evdev.c`. |
| **User-Space Exposure** | `/dev/input/eventX` (evdev) or `/dev/input/mouseX` (legacy). |

Mouse Device Model:
[] dmesg | grep -i mouse
[] cat /proc/bus/input/devices

How the OS abstract the mouse?

- 
- Which are the mouse events type?
- How the mouse is discover?
- How is the mouse register?
- Which is the device model
- How does the mouse get's map to the proc file system?
- How to discover mouse capabilites?
- How to know the driver that mangages the mouse?
- How does the interaction model betweeen the OS and the Mouse Works?
- How the interaction model between the Mouse/OS and User-Lang Applications works?
- How to use QEMU to write a mouse driver; or integrate a mouse driver in a small OS?
- ...

Mouse - Kernel Interaction Model:

- Interrupt Handling (For USB or PS/2): - When the mouse moves or a button is pressed, an interrupt request (IRQ) is generated. For USB, usb_interrupt handles the event; for PS/2, it’s serio_interrupt.
- Driver Processing: The interrupt is handled by usbhid (USB) or psmouse (PS/2). The driver translates raw signals into Linux input events (input_event structure).
- Event Dispatching in the Input Core: The event is sent to evdev.c or mouse.c in the input subsystem. The kernel formats it as evdev or raw mouse events.
- ...

Kernel:

- What are kernel events?
- evtest - Direct Event Monitoring

Driver:

- USB HID Driver
- ...

X Server:

- xinput list

Device Connection

- ...
- ...

## References

- [https://en.m.wikipedia.org/wiki/USB_human_interface_device_class](https://en.m.wikipedia.org/wiki/USB_human_interface_device_class)
- [Linux USB HID Gadget Driver](https://docs.kernel.org/usb/gadget_hid.html)
- USB Set of Specifications / [https://en.m.wikipedia.org/wiki/USB_human_interface_device_class](https://en.m.wikipedia.org/wiki/USB_human_interface_device_class)