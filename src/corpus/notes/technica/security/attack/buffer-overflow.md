---
tags: [note, security, attack, vulnerability]
---

# Buffer Overflow



## What can be done with a buffer overflow?

| **Capability Enabled** | **Description** |
| --- | --- |
| Arbitrary Code Execution | Cause the program to execute attacker-controlled code or instructions. |
| Control Flow Hijacking | Redirect execution to unintended code paths (e.g., ROP/JOP techniques). |
| Privilege Escalation | Gain higher privileges if the vulnerable program runs with elevated permissions. |
| Denial of Service (DoS) | Crash the application or system, making it unavailable. |
| Data Corruption | Modify variables, data structures, or application state. |
| Information Disclosure | Read memory containing sensitive information such as credentials or cryptographic material. |
| Authentication Bypass | Corrupt program state to bypass authentication or authorization logic. |
| Persistence | Install malware or modify startup mechanisms after gaining execution. |
| Sandbox Escape | Escape an application's isolation boundary if additional vulnerabilities exist. |
| Remote System Compromise | If the vulnerable application is network-accessible, compromise it remotely. |

## References

- https://en.wikipedia.org/wiki/Buffer_overflow
