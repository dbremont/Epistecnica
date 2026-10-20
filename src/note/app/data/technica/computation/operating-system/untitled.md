# 🌐

> Note: The OS is not only the abstract Kernel - is all the drivers, etc.
> 

> We need intrinsic os capabilities - that is - how to used the hardware.
> 

> Note: The **Term Kernel Interaction** - interface is tricky - because - it can be done using several modalities - System Call,  File Based Interaction - Open a File (It acts as a sort of interaction medium), …
> 

> Note: **DON’T REFERENCE** THIS - THIS IS A GUIDE FOR THIS SUB TREE.
> 

- add Distribute Operating System - Multi  Kernel.
- add New Lines of Research.
- Why does distributeed os failed?

Instead of 

```
         DISTRIBUTED OS
              │
    ┌─────────┼─────────┐
  Node       Node      Node
```

We have

```
     APPLICATION
              │
   distributed middleware
              │
   ┌──────────┼──────────┐
 Linux      Linux      Linux
   │          │          │
 Node       Node       Node
```

| Category | Technical Element | Description |
| --- | --- | --- |
| **Constitutive Technical Object** | **Kernel** | Core constitutive component of the OS responsible for privileged resource management and coordination between software and hardware. |
| **Constitutive Technical Object** | **Device Driver** | Component that provides controlled interaction between the OS and a particular hardware device. |
| **Constitutive Technical Object** | **Filesystem** | Component that organizes persistent data and provides mechanisms for storing, retrieving, and managing files. |
| **Constitutive Technical Object** | **Process Manager** | Component responsible for representing, creating, scheduling, and terminating processes. |
| **Constitutive Technical Object** | **Memory Manager** | Component responsible for managing physical and virtual memory and providing memory abstractions to processes. |
| **Technical Architecture** | **OS Architecture** | Structural organization of the OS into components, layers, subsystems, interfaces, and their relationships. Examples include monolithic, microkernel, hybrid, and layered architectures. |
| **Technical Interface** | **System Call Interface** | Interface through which user-space programs request privileged OS services. |
| **Technical Interface** | **Device Interface** | Interface through which OS components interact with hardware devices and their drivers. |
| **Technical Function** | **Resource Management** | Management and allocation of CPU time, memory, storage, devices, and other computational resources. |
| **Technical Function** | **Process Execution** | Creation, scheduling, synchronization, suspension, and termination of program execution. |
| **Technical Function** | **Hardware Abstraction** | Provides software with standardized abstractions over heterogeneous hardware resources. |
| **Technical Function** | **Protection and Isolation** | Separates processes, users, and resources and controls their access to protected system resources. |
| **Technical Mechanism** | **Process Scheduling** | Mechanism by which the OS determines which runnable computation receives processor time. |
| **Technical Mechanism** | **Virtual Memory** | Mechanism that provides processes with an abstract address space while managing underlying physical memory. |
| **Technical Mechanism** | **Inter-Process Communication** | Mechanisms through which independently executing processes exchange information and synchronize. |
| **Technical Mechanism** | **System Call Dispatch** | Mechanism that transfers execution from an application into the privileged OS execution environment to service a system call. |
| **Technical Activity** | **System Boot** | Ordered activity through which the machine initializes hardware, loads the OS, initializes system components, and reaches an operational state. |
| **Technical Activity** | **Process Execution** | Temporally extended activity involving process creation, scheduling, execution, synchronization, and termination. |
| **Technical Act** | **System Call Invocation** | A discrete technical act through which a program requests an OS service. |
| **Technical Act** | **Context Switch** | Discrete operation that changes the processor's execution context from one computation to another. |
| **Technical Blueprint** | **OS Source Code / Build Configuration** | Generative description from which an OS implementation can be constructed, compiled, and configured. |
| **Technical Specification** | **OS/API Specification** | Precise specification of interfaces, behavioral requirements, resource semantics, and compatibility requirements. |
| **Technical Standard** | **POSIX** | Standardized specification defining interfaces and behavioral requirements for a class of operating-system environments. |
| **Technical Technique** | **Scheduling Algorithm** | Generalized method for determining how computational resources such as CPU time are allocated among competing executions. |
| **Technical Principle** | **Process Isolation** | Principle that independently executing programs should be prevented from improperly interfering with one another. |
| **Technical Constraint** | **Hardware Resource Limits** | Constraints imposed by processor architecture, physical memory, storage capacity, device capabilities, and other environmental limitations. |
| **Technical Resource** | **CPU / Memory / Storage / I/O Devices** | Computational resources managed, allocated, and mediated by the OS. |
| **Technical Infrastructure** | **OS Runtime Environment** | Software and hardware environment that enables applications and other technical processes to execute. |
| **Technical Practice** | **Operating-System Administration** | Organized technical practice concerned with installing, configuring, securing, monitoring, updating, and maintaining operating systems. |
| **Maintenance** | **OS Maintenance** | Activities such as patching, updating, reconfiguration, filesystem maintenance, driver updates, and system recovery. |
| **Technical Feedback** | **Logs / Metrics / Errors / System Events** | Signals generated by the OS that reveal system state, performance, failures, and operational behavior. |
| **Verification** | **OS Testing / System Validation** | Evaluation of OS behavior against specifications, interfaces, security properties, compatibility requirements, and operational requirements. |
| **Technical Failure** | **OS Failure** | Failure of the OS or one of its subsystems to provide required functions, potentially resulting in crashes, resource exhaustion, corruption, or loss of service. |

## Technical Capability Space

| Category | Technical Capability | Description |
| --- | --- | --- |
| **Process Management** | Process Creation | Create new execution processes |
|  | Process Execution | Load and execute executable programs |
|  | Process Termination | Terminate processes and release their resources |
|  | Process Scheduling | Determine which process/thread executes and when |
|  | Thread Management | Create, schedule, synchronize, and terminate threads |
|  | Process Identification | Assign and manage process/thread identifiers |
|  | Process State Management | Maintain and transition process execution states |
|  | Process Control | Suspend, resume, signal, and otherwise control processes |
| **Memory Management** | Virtual Memory | Provide each process with a virtual address space |
|  | Memory Allocation | Allocate and reclaim physical/virtual memory |
|  | Memory Mapping | Map memory, files, and devices into address spaces |
|  | Memory Protection | Enforce access permissions over memory regions |
|  | Shared Memory | Allow controlled memory sharing between processes |
|  | Memory Paging | Move memory pages between physical memory and backing storage |
|  | Copy-on-Write | Efficiently share memory until modification |
| **Inter-Process Communication** | Pipes | Provide unidirectional kernel-mediated byte streams |
|  | FIFOs | Provide named pipe-based byte-stream communication |
|  | Unix Domain Sockets | Provide local process-to-process communication |
|  | Shared Memory IPC | Provide shared memory regions for processes |
|  | Message Queues | Provide structured message-based IPC |
|  | Signals | Deliver asynchronous event notifications to processes |
|  | Semaphores | Provide process/thread synchronization |
|  | Futexes | Provide efficient user-space/kernel-assisted synchronization |
| **Terminal / Console** | **TTY** | Provide the OS abstraction for terminal devices and terminal sessions |
|  | **PTY** | Provide a pseudo-terminal consisting of a master/slave terminal pair |
|  | Terminal Line Discipline | Process terminal input, canonical mode, echo, signals, etc. |
|  | Terminal Multiplexing | Support multiple virtual terminal sessions |
|  | Console Management | Manage system consoles and virtual consoles |
| **File Systems** | File Creation | Create persistent or temporary filesystem objects |
|  | File Access | Open, read, write, seek, and close files |
|  | Directory Management | Create, enumerate, rename, and remove directories |
|  | File Metadata | Maintain permissions, ownership, timestamps, size, etc. |
|  | File Permissions | Control access to filesystem objects |
|  | Filesystem Mounting | Attach filesystems to the OS namespace |
|  | Virtual Filesystems | Expose kernel/system state through filesystem interfaces |
|  | Device Files | Represent devices through filesystem objects |
|  | File Locking | Coordinate concurrent access to files |
| **Storage** | Block Device Management | Manage block-oriented storage devices |
|  | Storage I/O | Read and write persistent storage |
|  | Storage Caching | Cache storage data in memory |
|  | Storage Scheduling | Schedule block-device I/O operations |
|  | Filesystem Persistence | Maintain filesystem state on persistent media |
| **Device Management** | Device Discovery | Detect and enumerate hardware devices |
|  | Device Driver Management | Provide software interfaces to hardware devices |
|  | Device I/O | Perform operations against hardware devices |
|  | Interrupt Handling | Respond to hardware-generated interrupts |
|  | DMA Management | Allow devices to transfer data directly to memory |
|  | Device Hotplugging | Detect and manage dynamically added/removed devices |
| **Networking** | Network Communication | Exchange data across network interfaces |
|  | Socket Communication | Provide endpoint abstraction for network communication |
|  | TCP/IP Processing | Implement network protocol processing |
|  | Routing | Determine paths for network packets |
|  | Network Interface Management | Configure and manage network interfaces |
|  | Packet Filtering | Inspect and control network traffic |
|  | Network Namespaces | Isolate network environments |
| **Security** | Authentication Support | Establish and represent authenticated identities |
|  | Authorization | Control access to system resources |
|  | Access Control | Enforce permissions and security policies |
|  | Privilege Management | Distinguish privileged and unprivileged operations |
|  | Credential Management | Associate processes with users, groups, and security credentials |
|  | Security Isolation | Establish boundaries between execution domains |
|  | Mandatory Access Control | Enforce centrally defined security policies |
| **Resource Management** | CPU Resource Management | Allocate CPU capacity among execution entities |
|  | Memory Resource Management | Control memory consumption |
|  | I/O Resource Management | Control and prioritize I/O consumption |
|  | Resource Accounting | Measure resource consumption |
|  | Resource Limiting | Restrict resource consumption |
|  | Resource Quotas | Enforce predefined resource limits |
| **Isolation / Virtualization** | Process Isolation | Isolate processes from one another |
|  | Address-Space Isolation | Give processes independent virtual memory spaces |
|  | Namespace Isolation | Provide isolated views of system resources |
|  | Control Groups | Group processes and control their resource consumption |
|  | Containerization | Construct isolated user-space execution environments |
|  | Virtual Machine Support | Provide hardware-assisted virtualization facilities |
| **Time** | System Clock | Provide system-wide time |
|  | Monotonic Clock | Provide monotonic time for measuring intervals |
|  | Timers | Schedule future events |
|  | Sleep / Delay | Suspend execution for a specified duration |
|  | Time Synchronization | Adjust system time against external time sources |
| **Program Execution** | Executable Loading | Load executable binaries into memory |
|  | Dynamic Linking | Support loading and linking shared libraries |
|  | Runtime Environment | Establish the execution context required by programs |
|  | System Call Invocation | Allow user programs to request kernel operations |
|  | ABI Support | Provide the binary interface expected by compiled programs |
| **System Interface** | System Calls | Expose kernel capabilities to user-space programs |
|  | Device Interfaces | Expose devices through standardized OS interfaces |
|  | Filesystem Interfaces | Expose filesystem functionality to applications |
|  | Process Interfaces | Expose process state and control facilities |
|  | `/proc` Interface | Expose process and kernel state through a virtual filesystem |
|  | `/sys` Interface | Expose kernel/device/system information through sysfs |
|  | `/dev` Interface | Expose device endpoints through device nodes |
| **Boot / Initialization** | Hardware Initialization | Initialize hardware required by the OS |
|  | Kernel Initialization | Initialize kernel subsystems |
|  | Root Filesystem Initialization | Establish the initial filesystem environment |
|  | Process 1 Initialization | Start the initial user-space process |
|  | Service Initialization | Start system services |
| **Power Management** | Power-State Management | Control system power states |
|  | CPU Power Management | Manage CPU frequency and power states |
|  | Device Power Management | Suspend/resume and manage device power |
|  | System Suspend | Transition the system into suspended states |
|  | System Shutdown | Safely terminate execution and power down/reboot |
| **Observability** | System Monitoring | Observe processes, memory, CPU, I/O, and other state |
|  | Kernel Logging | Produce kernel/system diagnostic messages |
|  | Event Tracing | Record system execution events |
|  | Performance Counters | Measure hardware/software performance events |
|  | Auditing | Record security and system activity |
|  | Debugging Support | Expose facilities for diagnosing execution |
| **Fault Management** | Exception Handling | Handle processor and software exceptions |
|  | Fault Detection | Detect execution and hardware failures |
|  | Process Fault Isolation | Prevent failures in one process from directly corrupting others |
|  | Core Dumping | Capture process state after abnormal termination |
|  | Recovery | Recover system components from certain failures |
| **User / Session Management** | User Management | Represent and manage system users |
|  | Group Management | Represent collections of users for access control |
|  | Session Management | Establish and manage user sessions |
|  | Login Support | Establish authenticated interactive sessions |
|  | Session Isolation | Separate independent user sessions |
| **System Services** | Service Management | Start, stop, supervise, and restart system services |
|  | Service Discovery | Allow components to locate available services |
|  | IPC Service Infrastructure | Provide system-wide communication facilities |
|  | Configuration Management | Maintain and expose system configuration |
| **Human / Application Interaction** | Command-Line Interface | Provide interactive command execution through shells |
|  | Graphical Interface | Provide graphical interaction facilities |
|  | Desktop Services | Provide higher-level interactive application facilities |
|  | Application Launching | Start applications in user sessions |
|  | Clipboard / Selection | Provide inter-application data exchange mechanisms |
| **Networking Services** | DNS Resolution | Resolve domain names to network addresses |
|  | DHCP | Obtain network configuration dynamically |
|  | Network Configuration | Configure addresses, routes, interfaces, and policies |
| **Software Management** | Package Management | Install, update, remove, and manage software packages |
|  | Dependency Management | Resolve software dependencies |
|  | Software Repository Access | Retrieve software packages from repositories |

| Category | Technical Capability | Description |
| --- | --- | --- |
| **Process Execution** | Process Creation | Create processes |
|  | Process Execution | Execute programs |
|  | Process Termination | Terminate processes |
|  | Thread Management | Create and manage threads |
|  | CPU Scheduling | Allocate CPU execution |
|  | Process Control | Suspend, resume, signal, and control processes |
| **Memory Management** | Virtual Memory | Provide isolated virtual address spaces |
|  | Memory Allocation | Allocate memory |
|  | Memory Mapping | Map memory, files, and devices |
|  | Memory Protection | Control memory access |
|  | Shared Memory | Share memory between processes |
|  | Memory Paging | Manage virtual-to-physical memory |
| **IPC** | Pipes | Kernel-mediated byte streams |
|  | FIFOs | Named byte streams |
|  | Unix Domain Sockets | Local IPC |
|  | Message Queues | Message-based IPC |
|  | Shared Memory IPC | Shared memory communication |
|  | Signals | Asynchronous process notification |
|  | Semaphores | Synchronization |
|  | Futexes | Low-level synchronization |
| **Terminal** | TTY | Terminal abstraction |
|  | PTY | Virtual terminal endpoints |
|  | Terminal Line Discipline | Process terminal input/output |
|  | Virtual Consoles | Multiple virtual system terminals |
| **Filesystem** | File Operations | Create, read, write, seek, delete files |
|  | Directory Operations | Create and manage directories |
|  | Filesystem Mounting | Attach filesystems to namespace |
|  | File Permissions | Control filesystem access |
|  | File Locking | Coordinate concurrent file access |
|  | Virtual Filesystem | Common filesystem abstraction |
|  | `/proc` | Expose process/kernel state |
|  | `/sys` | Expose device/kernel state |
|  | `/dev` | Expose device endpoints |
| **Storage** | Block Storage | Access block devices |
|  | Disk Management | Manage storage devices |
|  | Partitioning Support | Access partitioned storage |
|  | Storage I/O | Read/write storage |
|  | Storage Caching | Cache storage data |
|  | RAID | Aggregate storage devices |
|  | Logical Volumes | Abstract physical storage into logical volumes |
|  | Storage Encryption | Encrypt block storage |
| **Networking** | Network Communication | Exchange network packets |
|  | Sockets | Provide communication endpoints |
|  | TCP/IP | Process Internet protocols |
|  | Routing | Forward packets |
|  | Packet Filtering | Filter network traffic |
|  | Network Namespaces | Isolate network stacks |
|  | Network Interfaces | Expose network devices |
| **Device I/O** | Device Access | Communicate with hardware devices |
|  | Device Discovery | Detect hardware |
|  | Device Enumeration | Enumerate available devices |
|  | Device Driver Binding | Associate devices with drivers |
|  | Driver Loading | Load device drivers |
|  | Hotplug | Handle dynamic hardware changes |
| **Input** | Keyboard Input | Receive keyboard events |
|  | Mouse Input | Receive pointer events |
|  | Touch Input | Receive touchscreen events |
|  | HID | Generic human-interface-device support |
|  | Game Controller Input | Receive controller events |
| **Display** | Framebuffer | Provide display memory access |
|  | Display Management | Configure displays |
|  | GPU Management | Manage graphics processors |
|  | DRM/KMS | Kernel graphics/display management |
|  | Display Output | Drive display interfaces |
| **Audio** | Audio Input | Capture audio |
|  | Audio Output | Produce audio |
|  | Audio Device Management | Manage audio hardware |
|  | ALSA | Kernel audio subsystem |
| **USB** | USB Host Management | Manage USB buses |
|  | USB Device Access | Communicate with USB devices |
|  | USB HID | Support USB input devices |
|  | USB Storage | Support USB storage |
|  | USB Serial | Support USB serial devices |
| **PCI** | PCI Device Management | Discover/configure PCI devices |
|  | PCIe | Manage PCI Express devices |
| **Serial / Embedded I/O** | UART | Serial communication |
|  | I²C | Peripheral-bus communication |
|  | SPI | Synchronous peripheral communication |
|  | GPIO | Control general-purpose I/O pins |
|  | PWM | Generate pulse-width signals |
|  | ADC | Read analog signals |
|  | DAC | Produce analog signals |
| **Wireless Hardware** | Wi-Fi | Manage wireless LAN hardware |
|  | Bluetooth | Manage Bluetooth hardware |
|  | NFC | Interface with NFC hardware |
|  | WWAN | Interface with cellular hardware |
| **Sensors** | Temperature Sensors | Read hardware temperature |
|  | Voltage Sensors | Read voltage measurements |
|  | Current Sensors | Read current measurements |
|  | Accelerometers | Read acceleration |
|  | Gyroscopes | Read angular velocity |
|  | Ambient-Light Sensors | Read illumination |
|  | Proximity Sensors | Detect proximity |
| **Camera / Video** | Camera Devices | Capture images/video |
|  | Video Capture | Provide camera frames |
|  | Video Output | Provide video output |
|  | Video Encoding/Decoding | Hardware-assisted media processing |
| **Power Management** | Power Management | Manage system power states |
|  | CPU Frequency Scaling | Adjust processor frequency |
|  | CPU Idle Management | Manage processor idle states |
|  | Suspend/Resume | Suspend and restore system |
|  | Battery Management | Monitor battery state |
|  | Thermal Management | Control thermal conditions |
| **Time** | System Clock | Provide system time |
|  | Monotonic Clock | Provide monotonic time |
|  | Timers | Schedule timed events |
|  | High-Resolution Timing | Provide fine-grained timing |
| **Security** | User Identity | Represent users/groups |
|  | Credentials | Associate identities with processes |
|  | Permissions | Enforce discretionary access control |
|  | Capabilities | Represent fine-grained privileges |
|  | Mandatory Access Control | Enforce security policies |
|  | Secure Boot Support | Participate in trusted boot |
|  | Cryptographic Primitives | Provide kernel cryptographic facilities |
|  | Random Number Generation | Provide system randomness |
|  | TPM Interface | Access hardware security modules |
| **Isolation** | Process Isolation | Isolate process execution |
|  | Address-Space Isolation | Isolate memory |
|  | Namespace Isolation | Isolate system-resource views |
|  | cgroups | Control and account for resources |
|  | Seccomp | Restrict system calls |
|  | Capability Isolation | Restrict privileged operations |
| **Virtualization** | Hardware Virtualization | Support virtual-machine execution |
|  | Virtual CPU | Virtualize CPU execution |
|  | Virtual Memory | Virtualize guest memory |
|  | Virtual Network Devices | Provide virtual network hardware |
|  | Virtual Block Devices | Provide virtual storage |
| **Interrupt / DMA** | Interrupt Handling | Respond to hardware interrupts |
|  | MSI/MSI-X | Handle message-signaled interrupts |
|  | DMA | Transfer device data directly to memory |
|  | IOMMU | Control device memory access |
| **Firmware** | UEFI Interface | Interact with platform firmware |
|  | ACPI Interface | Obtain/manage platform hardware information |
|  | SMBIOS/DMI | Obtain system hardware information |
|  | Firmware Loading | Load device firmware |
| **Observability** | Kernel Logging | Produce kernel diagnostic information |
|  | System Statistics | Expose resource statistics |
|  | Event Tracing | Trace system activity |
|  | Performance Counters | Measure execution/hardware events |
|  | Auditing | Record security-relevant operations |
|  | Debugging | Inspect and control execution |
| **Fault Management** | Exception Handling | Handle CPU/software exceptions |
|  | Fault Isolation | Contain failures |
|  | Core Dumps | Capture process state |
|  | Watchdog | Detect system hangs |
| **Boot / Initialization** | Hardware Initialization | Initialize platform hardware |
|  | Kernel Initialization | Initialize kernel subsystems |
|  | Root Filesystem | Establish initial filesystem |
|  | Initial Process | Start initial user-space execution |
| **Resource Management** | CPU Accounting | Track CPU consumption |
|  | Memory Accounting | Track memory consumption |
|  | I/O Accounting | Track I/O consumption |
|  | Resource Limits | Restrict resource usage |
|  | Quotas | Enforce resource quotas |