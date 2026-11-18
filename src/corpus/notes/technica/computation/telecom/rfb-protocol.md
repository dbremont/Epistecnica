---
tags: [note, protocol, remote-access, rfb, remote-framebuffer]
---

# RFB Protocol

> **RFB** (Remote Framebuffer) is the wire protocol behind [VNC](/view.html?p=notes/technica/computation/telecom/vnc.md): a small binary protocol in which the server sends rectangles of pixels and the client sends keyboard and pointer events. It is deliberately thin — the specification is short enough to implement in an afternoon — and it assumes nothing about the client's platform beyond a framebuffer.

> The protocol is **pixel-oriented and stateful on the server side**. The client does not describe the remote desktop; it receives pixels in the format it negotiated, and it sends input events addressed to the server's coordinate space.

## Handshake

| Step | Direction | What it carries |
| --- | --- | --- |
| **ProtocolVersion** | Server → client | The RFB version, e.g. `RFB 003.008` |
| **Security** | Server → client | The security types offered (None, VNC password, VeNCrypt, …); the client chooses |
| **SecurityResult** | Server → client | Success or failure of the chosen type (RFB 3.8 and later) |
| **ClientInit** | Client → server | The **shared** flag — may other clients join this session? |
| **ServerInit** | Server → client | Framebuffer width, height, pixel format and desktop name |

> After `ServerInit` the connection is a loop of client messages and server replies. There is no session negotiation beyond this point; the pixel format is fixed for the connection unless the client changes it.

## Client messages

| Message | Purpose |
| --- | --- |
| **SetPixelFormat** | Change the pixel format the server will send |
| **SetEncodings** | Declare which encodings the client understands, in preference order |
| **FramebufferUpdateRequest** | Ask for the next update — incremental, or the full framebuffer |
| **KeyEvent** | A key press or release, by keysym |
| **PointerEvent** | Pointer position and button mask |
| **ClientCutText** | The client's clipboard text |

## Server messages

| Message | Purpose |
| --- | --- |
| **FramebufferUpdate** | A set of rectangles, each with an encoding and its payload |
| **SetColourMapEntries** | Palette entries for indexed colour modes |
| **Bell** | An audible signal from the server |
| **ServerCutText** | The server's clipboard text |

## Encodings

> The encoding is where the protocol's efficiency lives: a rectangle can be sent as raw pixels, as a copy from elsewhere on the screen, as a tiled pattern, or compressed.

| Encoding | Idea |
| --- | --- |
| **Raw** | The pixels, uncompressed — the baseline every client implements |
| **CopyRect** | The rectangle is a copy of another screen region — the cheap scroll |
| **RRE / CoRRE** | The rectangle is a set of solid-colour sub-rectangles |
| **Hextile** | Tiles of 16×16 pixels, each with its own sub-encoding |
| **zlib / ZRLE / TRLE** | Compression of the pixel data, with run-length and palette steps |
| **Tight** | zlib with JPEG for photographic regions and lossless for the rest |
| **H.264 / Open H.264** | Video-codec encoding for motion-heavy screens |

> The client declares its preferences with `SetEncodings`, and the server picks. A modern client asks for Tight or ZRLE for desktop work and H.264 for video; a minimal client asks for Raw and receives a lot of bytes.

## Properties

| Property | Consequence |
| --- | --- |
| **Stateless client** | The client can disconnect and reconnect; the session lives on the server |
| **Multiple viewers** | The `shared` flag admits several clients to one session |
| **Platform independence** | The client only needs a framebuffer and an input device |
| **No audio, no USB, no clipboard by default** | Audio and device redirection are extensions or separate channels |
| **Latency-sensitive** | Updates are request-driven; a slow link means fewer frames, not lower resolution |

> The protocol is the reason VNC is easy to reimplement and hard to secure: it has no built-in encryption, no authentication beyond the shared-password challenge, and no authorisation model. The usual deployment wraps it in SSH, TLS or a gateway.

## References

- [RFB (protocol)](https://en.wikipedia.org/wiki/RFB_(protocol))
- [The RFB protocol specification](https://www.realvnc.com/docs/rfbproto.pdf)
- [VNC](/view.html?p=notes/technica/computation/telecom/vnc.md) — the system the protocol serves
- [noVNC](/view.html?p=notes/technica/computation/telecom/novnc.md) — an RFB client in the browser
- [WebSocket](/view.html?p=notes/technica/computation/telecom/websocket.md) — the transport the browser client uses
- [TCP](/view.html?p=notes/technica/computation/telecom/transmission-control-protocol-tcp.md) — the transport the native protocol assumes
