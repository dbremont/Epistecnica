# Port-Mapped I/O (PMIO)


> **I/O Controllers**: An **I/O controller** is a hardware component that manages the communication between the CPU and peripheral devices by converting data between the device's native format and the system's bus or memory, while handling device-specific protocols, control signals, and data transfer operations.
> 

QA:

- How the data in the I/O Ports is Communicated to the devices?

## Index

**I/O Ports**:

- In Port-Mapped I/O, certain memory addresses are designated as **I/O ports**.
- These ports are separate from the system's main memory addresses.
- The CPU interacts with the I/O devices by reading from or writing to these I/O ports.
- These ports are typically 16 bits wide but can vary in some systems.

**Address Space**:

- I/O ports have their own address space that is separate from the system's RAM.
- The CPU uses a separate **I/O address bus** to access the ports. This bus doesn't overlap with the memory address bus.
- Typically, systems allocate a limited range of addresses (e.g., 0x0000 to 0xFFFF) to I/O ports.

**Instruction Set**:

- Special CPU instructions are used for interacting with I/O ports. Common instructions include:
    - `IN` (input): Reads data from a specified I/O port into a CPU register.
    - `OUT` (output): Sends data from a CPU register to a specified I/O port.
- These instructions allow direct interaction with I/O devices.

**I/O Controllers**:

- Hardware devices, such as keyboards, disk drives, and network interfaces, are connected to the CPU through I/O controllers.
- These controllers map their functionalities to specific I/O port addresses.
- The operating system and device drivers use these port addresses to interact with the devices.

**I/O Addressing**:

- The I/O addresses are predefined by the hardware or operating system.
- Each peripheral device or controller may have a set of I/O ports assigned to it, allowing the CPU to communicate with the device.

## How the data in the I/O Ports is communized to the devices?

In **Port-Mapped I/O (PMIO)**, data communication between the CPU and peripheral devices via I/O ports occurs through the following steps:

1. **CPU Issues I/O Instruction**: The CPU uses special I/O instructions, such as `IN` (input) and `OUT` (output), to communicate with I/O ports. These instructions allow the CPU to read data from or send data to specific I/O port addresses.
2. **Address Bus**: The CPU places the I/O port address on the **I/O address bus**, which is separate from the system's memory address bus. This tells the system which specific device or peripheral to interact with.
3. **I/O Controller**: Each peripheral device connected to the system has an **I/O controller** that is responsible for managing communication. When the CPU sends an I/O instruction targeting a specific I/O port, the corresponding I/O controller is activated to handle the communication. The I/O controller translates the CPU's request into actions that the device understands.
    - For an **output operation** (`OUT`), the I/O controller takes the data from the CPU's register and sends it to the device, typically through a parallel or serial communication line, depending on the type of peripheral.
    - For an **input operation** (`IN`), the I/O controller retrieves data from the device and sends it back to the CPU.
4. **Control Signals**: The I/O controller generates the necessary **control signals** (e.g., read/write, data direction) to ensure proper data transfer between the CPU and the peripheral device. These control signals synchronize the data flow and inform the device when to send or receive data.
5. **Data Bus**: The actual data is transferred over the **data bus**. When the I/O controller receives a data transfer request from the CPU, it places the data on the data bus, which is then read by the CPU, or vice versa for write operations.
6. **Device Response**: The peripheral device responds to the control signals by either providing data to the I/O controller (for input) or accepting data from the I/O controller (for output), depending on the operation initiated by the CPU.

## References

- https://en.wikipedia.org/wiki/Memory-mapped_I/O_and_port-mapped_I/O