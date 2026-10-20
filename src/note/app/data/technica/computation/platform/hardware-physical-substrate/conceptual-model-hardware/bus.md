# Bus


> A **computer hardware bus** is a high-speed communication pathway that transfers data, addresses, and control signals between various internal components of a computer, such as the CPU, memory, and peripheral devices, using specific protocols for data transmission and synchronization.
> 

QA:

- Are all devices connected to a bus?
- How are the components networked together?

## Taxonomy

- **System Bus**: The **System Bus** connects the CPU, memory (RAM), and other components. It is typically divided into three sub-buses:
    - **Data Bus**: Carries data between components.
    - **Address Bus**: Carries memory addresses to indicate where data should be read from or written to.
    - **Control Bus**: Carries control signals to manage operations like read/write, memory access, and synchronization.
- **Expansion Buses**: These buses allow the CPU to communicate with peripheral devices or expansion cards. Examples include:
    - **PCI (Peripheral Component Interconnect) Bus**: A parallel bus used to connect expansion cards like network interfaces, sound cards, and storage controllers.
    - **PCIe (PCI Express)**: A high-speed, serial bus standard used for modern expansion cards, offering much higher data transfer rates compared to PCI.
    - **AGP (Accelerated Graphics Port)**: A dedicated bus for graphics cards, primarily used for older PCs.
    - **ISA (Industry Standard Architecture)**: An older parallel bus standard for expansion cards, now largely obsolete.
- **Memory Bus**: The **Memory Bus** connects the CPU to the system's main memory (RAM). It typically includes the data bus, address bus, and control bus specific to memory transactions. Modern systems often have a **Dual-Channel** or **Quad-Channel** memory bus for improved performance.
- **I/O Buses**: These buses are designed to connect peripheral devices such as keyboards, mice, printers, storage devices, etc.
    - **USB (Universal Serial Bus)**: A serial bus used for connecting external devices, including storage, input devices, and peripherals.
    - **SATA (Serial ATA)**: A serial bus used to connect storage devices (HDDs, SSDs).
    - **Thunderbolt**: A high-speed, serial bus for connecting external devices like storage, displays, and docking stations.
- **Video Bus**: This bus is dedicated to handling the communication between the CPU or GPU and display devices.
    - **VGA (Video Graphics Array)**: An older analog video bus.
    - **HDMI (High-Definition Multimedia Interface)**: A modern serial bus for high-definition video and audio output.
    - **DisplayPort**: Another modern video interface used for connecting monitors.
- **Power Bus**: The **Power Bus** distributes electrical power to the various components in the system, including the motherboard, CPU, memory, and expansion cards.

## Bus Technology

| **Bus Type** | **Description** | **Common Usage** | **Example Devices** |
| --- | --- | --- | --- |
| **PCI (Peripheral Component Interconnect)** | A high-speed bus used to connect devices like network cards, sound cards, storage controllers, etc. | Connecting expansion cards to the CPU | Network cards, graphics cards, sound cards |
| **PCI Express (PCIe)** | A faster, more scalable version of PCI. It is the current standard for most internal connections. | Expansion slots for high-performance devices | GPUs, SSDs, NICs, motherboards |
| **USB (Universal Serial Bus)** | A standard interface for connecting external devices to the computer. | Connecting external peripherals | Mice, keyboards, printers, USB drives |
| **SATA (Serial ATA)** | A bus used for connecting storage devices to the system. | Hard drives, SSDs | Hard drives, SSDs, optical drives |
| **I2C (Inter-Integrated Circuit)** | A low-speed, two-wire interface used for communication between low-speed peripherals. | Sensors, EEPROMs, displays, RTCs | Sensors, EEPROM chips, real-time clocks |
| **SPI (Serial Peripheral Interface)** | A high-speed serial bus, typically used for connecting sensors, memory, and other peripherals. | Flash memory, sensors, displays | Flash memory, temperature sensors, displays |
| **Thunderbolt** | A high-speed interface used for connecting external devices, providing data and power. | External storage, monitors, docking stations | External hard drives, docking stations |
| **AGP (Accelerated Graphics Port)** | A bus designed specifically for graphics cards, now largely replaced by PCIe. | Connecting graphics cards | Graphics cards (older systems) |
| **FireWire (IEEE 1394)** | A high-speed bus used for multimedia devices, audio/video equipment, and data transfer. | Digital cameras, external hard drives, audio interfaces | Video cameras, external drives, audio interfaces |
| **M.2** | A newer high-speed interface, primarily used for storage devices and wireless cards. | Solid-state drives, Wi-Fi cards, Bluetooth cards | SSDs, Wi-Fi/Bluetooth cards |
| **EISA (Extended Industry Standard Architecture)** | An older bus used in some servers and workstations, primarily for expansion. | Expansion cards in workstations and servers | Network adapters, video cards (older systems) |
| **VME (Versatile Motherboard Extension)** | A bus used in embedded systems and industrial applications. | Industrial controllers, embedded systems | Industrial controllers, embedded computers |
| **ISA (Industry Standard Architecture)** | A legacy 16-bit bus used in older PCs for connecting expansion cards. | Early PC expansion cards | Sound cards, network cards (older systems) |
| **HID (Human Interface Device)** | A bus type used specifically for input devices like mice and keyboards, typically through USB. | Input devices | Mice, keyboards, touchscreens |
| **Fibre Channel** | A high-speed data transfer protocol used in storage area networks (SAN). | Storage networks | Storage arrays, SAN devices |
| **MIPI (Mobile Industry Processor Interface)** | A high-speed interface used in mobile devices for connecting components like cameras and displays. | Mobile devices (smartphones, tablets) | Cameras, displays, touchscreen controllers |
| **PCI-X** | An extension of the PCI bus for higher performance in servers and workstations. | High-performance computing | Server expansion cards (older systems) |

## References

- https://en.wikipedia.org/wiki/Bus_(computing)#Memory_bus