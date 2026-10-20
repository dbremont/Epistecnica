# x86 Security

> The **x86 architecture** includes several security features, especially in modern processors (particularly in **x86-64**), to help mitigate vulnerabilities and enhance system protection. These features are designed to safeguard data, enforce access control, and reduce the risk of exploits.
> 

| **Security Feature** | **Description** |
| --- | --- |
| **NX (No eXecute) Bit / DEP** | Prevents execution of code in certain memory regions, protecting against buffer overflow attacks by marking data areas as non-executable. |
| **SMEP (Supervisor Mode Execution Prevention)** | Prevents code execution from user-mode addresses when the processor is in kernel mode, mitigating privilege escalation attacks. |
| **KASLR (Kernel Address Space Layout Randomization)** | Randomizes the memory addresses of the kernel to make it harder for attackers to predict and exploit memory locations. |
| **ASLR (Address Space Layout Randomization)** | Randomizes the base addresses of executable binaries, libraries, and other components to make memory-based attacks more difficult. |
| **SGX (Software Guard Extensions)** | Provides isolated, encrypted regions (enclaves) for sensitive operations, protected from external access, including from the OS and hypervisor. |
| **VT-x (Intel Virtualization Technology) / AMD-V (AMD Virtualization)** | Hardware virtualization technologies that isolate virtual machines and prevent exploits from escaping the VM to the host OS. |
| **Intel CET (Control-flow Enforcement Technology)** | Protects against control-flow hijacking attacks (ROP, JOP) by ensuring that execution follows a valid control flow path. |
| **Intel PT (Processor Trace)** | Provides low-overhead hardware tracing to monitor program execution and detect anomalous or malicious behavior. |
| **MDS (Microarchitectural Data Sampling) Mitigations** | Mitigations for the MDS vulnerabilities to protect against leakage of sensitive data across internal processor buffers. |
| **TPM (Trusted Platform Module)** | Hardware-based security module for secure cryptographic key storage, secure boot, disk encryption, and other security applications. |
| **Secure Boot** | Ensures that only trusted, signed software is loaded during the boot process to prevent rootkits and bootkits from compromising the system. |
| **Intel PTI (Process-Context Isolation)** | Isolates user-space and kernel-space memory to prevent exploitation of vulnerabilities like Spectre and Meltdown. |
| **AES-NI (Advanced Encryption Standard New Instructions)** | Accelerates AES encryption/decryption operations, improving performance for disk encryption and secure communication protocols. |
| **FIPS 140-2 Compliance** | Supports cryptographic modules compliant with FIPS 140-2, ensuring secure encryption operations for government and regulated industries. |
| **SMC (Secure Memory Controller)** | Provides physical memory protection, blocking unauthorized access to memory by unprivileged processes or users. |
| **Intel TXT (Trusted Execution Technology)** | Protects against attacks during boot by using TPM, secure boot, and other features to ensure the system starts in a trusted state. |