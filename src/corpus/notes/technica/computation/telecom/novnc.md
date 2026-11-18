---
tags: [note, remote-access, vnc, browser, websocket, novnc]
---

# noVNC

> **noVNC** is a [VNC](/view.html?p=notes/technica/computation/telecom/vnc.md) client written in JavaScript: it speaks [RFB](/view.html?p=notes/technica/computation/telecom/rfb-protocol.md) over a WebSocket, decodes the framebuffer updates and draws them into an HTML5 canvas, and sends keyboard and pointer events back. It is the reason a hypervisor can offer a remote console in a browser tab with no plugin and no native client.

> The name is the design: no native viewer. The client is a web page, so the remote desktop is one URL away — and the protocol that carries it is the same RFB the native clients speak, relayed over the one transport a browser is allowed to open.

## Why a WebSocket bridge

> A browser cannot open a raw TCP connection to port 5900. noVNC therefore talks to a **WebSocket-to-TCP bridge** — canonically `websockify` — which accepts the WebSocket from the browser, opens the TCP connection to the VNC server, and relays bytes in both directions. The bridge is the only piece that needs to run next to the server; the client is static files.

| Piece | Role |
| --- | --- |
| **noVNC client** | HTML page and JavaScript modules: RFB decoding, canvas rendering, input capture |
| **websockify** | The WebSocket ↔ TCP relay that makes the browser able to reach port 5900 |
| **VNC server** | An ordinary VNC server, unaware that its client is a browser |

## What it renders

> The client implements the RFB handshake, the encodings a browser can decode in software — Raw, CopyRect, Hextile, RRE, ZRLE, Tight with its JPEG path — and draws rectangles to a canvas. Pointer and keyboard events are captured on the canvas and translated back into RFB messages; the clipboard is exchanged through the RFB cut-text messages where the browser allows it.

| Concern | How noVNC handles it |
| --- | --- |
| **Transport** | WebSocket, binary frames, to the bridge |
| **Display** | HTML5 canvas, one draw per framebuffer update |
| **Input** | Mouse and keyboard events captured on the canvas and mapped to RFB key and pointer events |
| **Clipboard** | RFB cut text, with the browser's clipboard permissions |
| **Scaling** | Client-side scaling and viewport fitting, at the cost of resampling |
| **Security** | Whatever the bridge and the VNC server provide; typically TLS on the WebSocket plus a tunnelled or authenticated VNC |

## Where it is used

| Use | Why noVNC |
| --- | --- |
| **Hypervisor console** | Proxmox, oVirt, OpenStack and similar expose the VM console as a noVNC page |
| **Remote support** | A user opens a URL; nothing to install |
| **Kiosk and thin-client administration** | The admin surface is a browser |
| **Embedded devices** | A web UI with a remote screen for a headless box |

## Limits

> The browser is a weaker client than a native one: no hardware acceleration, no audio, no USB redirection, and a JavaScript decoder that is slower than a compiled one. noVNC is therefore the console and the support tool, not the daily-driver remote desktop. Where a full session is needed, a native client over the same RFB server — or a protocol with audio and device channels — is the better fit.

## References

- [noVNC](https://github.com/novnc/noVNC) — the client repository
- [websockify](https://github.com/novnc/websockify) — the WebSocket-to-TCP bridge
- [VNC](/view.html?p=notes/technica/computation/telecom/vnc.md) — the remote-framebuffer system
- [RFB Protocol](/view.html?p=notes/technica/computation/telecom/rfb-protocol.md) — the protocol the client implements
- [WebSocket](/view.html?p=notes/technica/computation/telecom/websocket.md) — the transport the browser uses
- [HTTP](/view.html?p=notes/technica/computation/telecom/http.md) — the protocol that serves the client page
