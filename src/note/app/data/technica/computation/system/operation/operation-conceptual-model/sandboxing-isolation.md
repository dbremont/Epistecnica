# Sandboxing (Isolation)


> How can we create an isolated, controlled execution environment with comprehensive auditing capabilities?
> 

> Note: Useful spanish names Atalaje, Envoltura, Arnés, Confinamiento, Cascara.
> 

## Formulation

> What is the formulation of the technical problem at hand?
> 

> The technical problem is to construct an execution environment that mediates **all meaningful interaction between a system and its environment**, while providing:
> 
- **Isolation** — constrain what resources and external systems the process can access.
- **Control** — mediate and restrict the actions the process is permitted to perform.
- **Observation** — capture the relevant execution state, actions, inputs, outputs, and interactions.
- **Auditability** — produce a tamper-resistant record sufficient to reconstruct and evaluate what occurred.
- **Policy enforcement** — express and enforce rules governing permitted capabilities.
- **Termination & recovery** — retain the ability to stop, reset, or recover the execution environment when constraints are violated or execution becomes undesirable.

## ML Systems Isolation & Control

> How can we build a harness mechanism that wraps a given system—or, ultimately, ML-based computational processes—to provide controlled, auditable execution?
> 

> **Progression:** Pandora's Box → Harness + Sandbox → Auditable, Controlled Capability.
> 

> **Harness** = controls *how it acts*
> 
> 
> **Sandbox** = controls *where it can act*
> 
> **Audit** = records *what it did*
> 
> **Policy** = determines *what it may do*
> 

## Toolbox

> Which are the set of technical production objects to aid the solution of technical problem?
> 

| **Category** | **Tool** | **Description** | **Note** |
| --- | --- | --- | --- |
| **Isolation** | Linux Namespaces | Isolate processes, filesystem, network, users, and IPC | Fundamental Linux isolation primitive |
| **Isolation** | `bubblewrap` | Lightweight sandbox using Linux namespaces and bind mounts | Good starting point for agent execution |
| **Isolation** | `nsjail` | Sandbox with namespaces, resource limits, and seccomp | Stronger execution-control primitive |
| **Isolation** | Containers | Encapsulate execution inside an isolated userspace | Podman/Docker |
| **Isolation** | gVisor | Provides an additional isolation layer between workloads and the Linux kernel | For stronger isolation |
| **Execution Control** | seccomp | Restricts the system calls available to a process | Limits kernel attack surface |
| **Execution Control** | Linux Capabilities | Decomposes root privileges into granular capabilities | Avoid unrestricted root |
| **Execution Control** | cgroups | Controls CPU, memory, process, and I/O resources | Prevent resource exhaustion |
| **Execution Control** | `systemd-run` | Creates managed, resource-constrained execution units | Useful for host-level orchestration |
| **Environment** | Container Images | Define reproducible execution environments and dependencies | Python, Node, Rust, Java, etc. |
| **Environment** | Filesystem Mounts | Define exactly which host resources are exposed | e.g. `$PWD → /workspace` |
| **Environment** | OverlayFS | Creates writable layers over an immutable base filesystem | Useful for disposable environments |
| **Network Control** | Network Namespaces | Give execution environments independent network stacks | Can completely isolate networking |
| **Network Control** | Firewall / nftables | Controls permitted network connections | Fine-grained egress control |
| **Secrets** | Secret Manager | Stores and controls access to credentials and API keys | Secrets should not be baked into environments |
| **Secrets** | Credential Injection | Provides credentials only when authorized and needed | Prefer ephemeral credentials |
| **Policy** | Policy Engine | Determines which operations are permitted | Separates policy from execution |
| **Audit** | `auditd` | Records Linux security-relevant events | Kernel-level auditing |
| **Audit** | eBPF | Observes and traces processes, syscalls, files, and network activity | Powerful runtime observability |
| **Audit** | Process Tracing | Records commands, processes, exits, and execution events | Essential for agent accountability |
| **Audit** | Filesystem Auditing | Records reads/writes and filesystem changes | Useful for workspace accountability |
| **Audit** | Network Logging | Records connections and network activity | Establishes external-effect history |
| **Observability** | Logs | Persistent record of execution events | Human/system inspection |
| **Observability** | Metrics | Measures CPU, memory, I/O, network, and execution statistics | Operational monitoring |
| **Lifecycle** | Ephemeral Environments | Destroy execution environments after a run | Reduces persistence and contamination |
| **Lifecycle** | Snapshot / Restore | Captures and restores execution state | Useful for reproducibility and investigation |
| **Orchestration** | Execution Supervisor | Creates, configures, monitors, and terminates sandboxes | The **harness** around the execution |
| **Orchestration** | Job Queue | Manages execution requests and concurrency | Useful for multi-agent systems |

## References

- https://en.wikipedia.org/wiki/Sandbox_(computer_security)
- https://martinfowler.com/articles/harness-engineering.html
- [Machine Active Inference](https://app.notion.com/p/Machine-Active-Inference-3a6c0f5171ec801281adf2d5bda5304b?pvs=21)
- https://github.com/NVIDIA/openshell
- [**Secret Management**](note.html?n=technica/computation/system/operation/operation-conceptual-model/secret-management.md)
- https://www.daytona.io/
- https://github.com/firecracker-microvm/firecracker
- [Virtualization](note.html?n=technica/computation/platform/virtualization.md)
- [Linux Virtualization Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-virtualization-stack.md)
- [Docker](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/docker.md)