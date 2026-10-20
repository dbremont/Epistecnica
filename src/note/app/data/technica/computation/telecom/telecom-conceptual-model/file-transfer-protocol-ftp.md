---
tags: [computer-network, protocol]
---

# File Transfer Protocol (FTP)

- [FTPs](note.html?n=technica/computation/telecom/telecom-conceptual-model/ftps.md)

> FTP (**File Transfer Protocol**) is a **stateful, application-layer protocol** used for transferring files between a client and a server over a network. It operates over **TCP** (Transmission Control Protocol) and follows a **client-server architecture**.
> 

> **Authentication**: Supports **anonymous** access and **user-based authentication**.
> 

> **Unencrypted by Default**: Does **not** encrypt data (use FTPS or SFTP for security).
> 

> **Transport Protocol**: **Uses TCP (port 21 for commands, port 20 for data in active mode)**
> 

> **Stateful**: Maintains a persistent connection between the client and server during a session.
> 

> **Modes**: Supports **Active Mode** and **Passive Mode** for data transfer.
> 

> **File Transfer Protocol (FTP)** is a **stateful, connection-oriented, application-layer protocol** (OSI Layer 7) that facilitates bidirectional file transfer between a client and a server over a **TCP/IP network**. It operates using a **separate control and data channel model**, where the **control connection** (over TCP port 21) persists for issuing commands via a **text-based command/response mechanism** (as defined by RFC 959), while the **data connection** (over TCP port 20 in active mode, or an ephemeral port in passive mode) handles actual file transfer.
> 

> FTP follows a **request-response communication paradigm**, utilizing the **Telnet protocol format** for control commands (`USER`, `PASS`, `PORT`, `PASV`, `RETR`, `STOR`, etc.), and supports **ASCII and binary transfer modes**. It can operate in **active mode** (server initiates data connection) or **passive mode** (client initiates data connection, mitigating firewall/NAT issues). FTP lacks inherent security, transmitting authentication credentials and data in plaintext, necessitating extensions like **FTPS (FTP Secure via SSL/TLS)** or **SFTP (SSH File Transfer Protocol, distinct from FTP)** for encrypted transport.
> 

QA:

- Would you like a comparison between **FTP, FTPS, and SFTP** for security differences?
- How to log in to an FTP server as an anonymous user?  **User**  `anonymous` ; **Pass:**  Just Press Enter and Move On.
- How to find the FTP server directory on my PC using vsftpd? To find the FTP server directory on your PC using **vsftpd**, check the configuration file located at `/etc/vsftpd.conf` for the `local_root` (for local users) or `anon_root` (for anonymous users) directives, which define the directories. If these settings are not explicitly configured, the default directories are typically `/var/ftp` or `/srv/ftp` for anonymous access, and the home directory (`$HOME`) for local users. You can also inspect the system's active FTP sessions or logs for more details.
- What is the difference between **active mode** and **passive mode** in FTP, and how do they affect network security and firewall configuration?
- How does FTP handle **data channel negotiation**, and why is it important for NAT/firewall traversal?
- How can you configure **vsftpd** (or other FTP servers) to enhance security, such as restricting IPs, limiting command usage, and using **chroot** for user isolation?
- How do you configure a **vsftpd** server for **anonymous** vs **authenticated access**, and what are the key configuration parameters to secure them?
- How would you set up **virtual users** in **vsftpd**, and what are the implications of this configuration?
- How do you optimize FTP server performance for large file transfers or high concurrency, especially in a high-latency or bandwidth-constrained environment?
- How does FTP handle **large file transfers**, and what impact do file size and transfer protocol settings have on transfer speed?
- What is **FTP over SSH** (not SFTP) and how does it compare to traditional FTP in terms of security and use cases?
- How can **FTP** be used in an automated workflow for file transfers, and how does it interact with **cron jobs** or **batch scripts** for scheduled file uploads/downloads?

## Security Model

> FTP (**File Transfer Protocol**) was originally designed without security in mind, making it vulnerable to various attacks. Below is an in-depth breakdown of its security model, risks, and mitigations.
> 

### **Authentication & Access Control**

> 🛑 **Security Issue:** Credentials are sent in **plaintext** (unless FTPS or SFTP is used).
> 
- **Username & Password:** FTP relies on plaintext authentication via `USER` and `PASS` commands, making credentials vulnerable to eavesdropping.
- **Anonymous FTP:** Some servers allow access with a public username (e.g., `anonymous`) and an email address as a password.
- **User-Based Access Control:** Supports user authentication with role-based permissions.

### **Data Transmission Security**

> 🛑 **Security Issue:** Both command and data transmissions are unencrypted, making FTP susceptible to **packet sniffing** and **MITM attacks**.
> 
- **Control Channel (Port 21):** Handles authentication and commands in plaintext.
- **Data Channel (Port 20 / Ephemeral Ports):** Used for file transfer, also in plaintext.
- **Active Mode vs. Passive Mode:**
    - **Active Mode:** The server initiates the data connection (firewall-unfriendly).
    - **Passive Mode:** The client initiates both connections, making it more NAT/firewall-friendly.

### Common FTP Security Threats

| **Threat** | **Description** | **Mitigation** |
| --- | --- | --- |
| **Eavesdropping** | Attackers sniff credentials and file transfers in plaintext. | Use **FTPS or SFTP** for encryption. |
| **Man-in-the-Middle (MITM)** | Attackers intercept and modify FTP data in transit. | Use **TLS/SSL certificates** in FTPS. |
| **Brute Force Attacks** | Automated guessing of FTP credentials. | Use **strong passwords, fail2ban, and IP whitelisting**. |
| **Data Integrity Attacks** | No built-in integrity checks, allowing data tampering. | Use **checksum verification** and secure protocols. |
| **Command Injection** | Malicious users exploit FTP commands for privilege escalation. | Restrict **write access**, disable unnecessary commands. |

### **Secure FTP Server Configurations**

- **Disable Anonymous FTP** unless explicitly required.
- **Use Strong Authentication** (e.g., FTPS with TLS, SFTP with SSH keys).
- **Restrict FTP Commands** (Disable `DELE`, `RMDIR`, etc. for untrusted users).
- **Enforce IP Whitelisting** (Restrict access to trusted IPs).
- **Implement Logging & Monitoring** for FTP access and file transfers.

## Tools

> 

| **Category** | **Name** | **Description** | **Platform** | **Protocol Support** |
| --- | --- | --- | --- | --- |
| **FTP Servers** | **vsftpd** | Secure, fast, and lightweight FTP server. | Linux | FTP, FTPS |
|  | **ProFTPD** | Modular and configurable FTP server. | Linux, Unix | FTP, FTPS |
|  | **Pure-FTPd** | Secure and standards-compliant FTP server. | Linux, BSD | FTP, FTPS |
|  | **FileZilla Server** | Open-source FTP server with GUI management. | Windows, Linux | FTP, FTPS |
|  | **Microsoft IIS FTP** | FTP server integrated into Windows IIS. | Windows Server | FTP, FTPS |
|  | **Gene6 FTP Server** | Feature-rich Windows FTP server (discontinued). | Windows | FTP, FTPS |
|  | **War FTP Daemon** | Old but powerful Windows FTP server. | Windows | FTP |
|  | **TFTPd-HPA** | Lightweight TFTP/FTP server for embedded systems. | Linux, Unix | FTP, TFTP |
| **FTP Clients** | **FileZilla** | Popular open-source FTP GUI client. | Windows, Linux, macOS | FTP, FTPS, SFTP |
|  | **WinSCP** | Windows FTP/SFTP client with scripting support. | Windows | FTP, FTPS, SFTP |
|  | **Cyberduck** | User-friendly FTP/SFTP client with cloud storage support. | Windows, macOS | FTP, FTPS, SFTP, WebDAV |
|  | **lftp** | Command-line FTP/SFTP client with advanced features. | Linux, macOS | FTP, FTPS, SFTP |
|  | **ncftp** | Advanced command-line FTP client. | Linux, Windows, macOS | FTP, FTPS |
|  | **gFTP** | GTK-based graphical FTP client. | Linux | FTP, FTPS, SFTP |
|  | **Transmit** | Premium FTP client for macOS. | macOS | FTP, FTPS, SFTP |
|  | **CuteFTP** | Commercial FTP client with automation features. | Windows, macOS | FTP, FTPS, SFTP |
| **FTP Libraries** | **Apache Commons Net** | Java library for FTP operations. | Java | FTP, FTPS |
|  | **Python ftplib** | Standard Python library for FTP. | Python | FTP |
|  | **pyftpdlib** | Python FTP server framework. | Python | FTP, FTPS |
|  | **libcurl** | Multi-protocol file transfer library (supports FTP). | C, C++ | FTP, FTPS, SFTP |
|  | **WinInet API** | Windows API for FTP access. | Windows (C/C++) | FTP |
|  | **libftp** | Lightweight C FTP client library. | C | FTP |
|  | **Go FTP Library** | Golang FTP client/server library. | Go | FTP, FTPS |
|  | **node-ftp** | FTP client library for Node.js. | JavaScript (Node.js) | FTP |

## References

- Postel, Jon, and Joyce Reynolds. File transfer protocol. No. rfc959. 1985.
- https://en.wikipedia.org/wiki/File_Transfer_Protocol
- https://wiki.archlinux.org/title/Very_Secure_FTP_Daemon
- [File Transfer Protocol](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
- 
- 
- [Security](https://app.notion.com/p/Security-abe7b617157f43099a19bee382dd5996?pvs=21)