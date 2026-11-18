---
tags: [note, remote-access, vnc, remote-framebuffer, protocol]
---

# VNC

> **VNC** (Virtual Network Computing) is a remote-framebuffer system: a server exports the pixels of a display, a client renders them in a window and sends back keyboard and pointer events, and the two exchange updates over the **RFB** protocol. It is not a remote shell and not a remote desktop protocol in the Windows sense — the server sends an image, and the client is a viewer.

> The design principle is **statelessness at the client**: the server holds the framebuffer and the state, the client is replaceable, and the same session can be viewed from different devices and even from different VNC clients at the same time. That is why VNC became the remote-console layer of virtualisation, support desks and thin clients.

## How it works

| Side | Role |
| --- | --- |
| **VNC server** | Captures the framebuffer, tracks changes, encodes updates, and injects the client's input into the local input system |
| **VNC client** | Decodes the framebuffer updates, draws them, and sends key and pointer events |
| **RFB channel** | The protocol that carries the handshake, the updates and the events — see [RFB Protocol](/view.html?p=notes/technica/computation/telecom/rfb-protocol.md) |
| **Display number** | Each server listens on port 5900 + the display number (`:1` is 5901) |

> The server can be a real X display (`x11vnc` attaching to an existing session), a virtual display (`Xvnc`, `TigerVNC`), or a framebuffer exported by a hypervisor for a virtual machine's console. The last case is the one most people meet: the console tab of a hypervisor is usually noVNC talking RFB to the host.

## The security record

> VNC's original authentication is a password shared by all clients, checked through a challenge–response that DES-encrypts a random value with the password — a scheme with a short key space and no per-user identity. Later extensions add TLS (VeNCrypt, `-ssl`), X.509 client certificates and tunnelling, but the default expectation remains: **VNC is run inside SSH, a VPN or a private network, not exposed to the internet**.

| Concern | Status |
| --- | --- |
| Confidentiality | Optional TLS; otherwise plaintext pixels and keystrokes |
| Authentication | Shared password by default; stronger via VeNCrypt or a gateway |
| Authorisation | Coarse — a session is either shared or not |
| Auditing | Minimal in the protocol; the server log is the record |
| Exposure | Port 5900+ is a frequent scan target; keep it behind a tunnel |

> The counterweight is that the protocol is simple enough to implement and to proxy. That is why noVNC can render a session in a browser and why a hypervisor can expose a console with almost no client software.

## Where it is used

| Use | Why VNC |
| --- | --- |
| **Hypervisor console** | A virtual machine's framebuffer is available before any OS or agent runs |
| **Remote support** | A technician sees the user's screen without a client install |
| **Thin clients and kiosks** | The session lives on the server; the device is a viewer |
| **Headless lab machines** | A virtual display for software that needs a graphical session |
| **Shared session** | Several clients can watch or drive the same display |

## References

- [Virtual Network Computing](https://en.wikipedia.org/wiki/Virtual_Network_Computing)
- [RFB Protocol](/view.html?p=notes/technica/computation/telecom/rfb-protocol.md) — the wire protocol VNC runs on
- [noVNC](/view.html?p=notes/technica/computation/telecom/novnc.md) — the browser client
- [SSH](/view.html?p=notes/technica/general/ssh/ssh-secure-shell.md) — the usual tunnel for a VNC session
- [WebSocket](/view.html?p=notes/technica/computation/telecom/websocket.md) — the transport noVNC uses
- [Virtualization](/view.html?p=notes/technica/computation/platform/virtualization/topic.md) — the platform whose console VNC often serves
