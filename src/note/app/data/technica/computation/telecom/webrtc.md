---
tags: [computer-network, protocol]
---

# WebRTC

- [PeerJS](note.html?n=technica/computation/telecom/peerjs.md), [XMPP (Extensible Messaging and Presence Protocol)](note.html?n=technica/computation/telecom/xmpp-extensible-messaging-and-presence-protocol.md)

> **WebRTC (Web Real-Time Communication)** is a set of standardized APIs and protocols enabling real-time, peer-to-peer media (audio, video) and data communication directly between web browsers and mobile apps without requiring intermediary servers for media relay under typical scenarios.
> 

> **WebRTC** provides a framework for building applications that support real-time communication over the internet. It uses a combination of JavaScript **APIs**, **HTML5** and other web technologies, and networking protocols such as **UDP** (User Datagram Protocol) and **TCP** (Transmission Control Protocol) to establish peer-to-peer connections.
> 

> **WebRTC** can be used for various applications, including video conferencing, online gaming, file sharing, and screen sharing. All major web browsers, including Google Chrome, Mozilla Firefox, Safari, and Microsoft Edge support it.
> 

> Inter-network core: STUN → TURN.
> 

Guiding Questions:

- What kind of technical object is WebRTC?
- How is WebRTC internally organized?
- How does WebRTC operate across heterogeneous networks?
- Is WebRTC “purely peer-to-peer” in practice?
- How does WebRTC move bits?
- What is the security of ‘WebRTC’?
- How do we measure and evaluate WebRTC systems?
- Where does WebRTC run?
- What competes with or complements WebRTC?
- How does WebRTC scale beyond 2 peers?
- What is the support of ‘WebRTC’?

## Breviarium

> 

| Device | Role |
| --- | --- |
| Client Device | Captures, sends/receives media and data |
| Signaling Server | Coordinates connection setup (SDP + ICE) |
| STUN Server | Discovers public IP/NAT mapping |
| TURN Server | Relays media when direct connection fails |
| Media Server (optional) | Advanced routing, mixing, recording |

## 📦 **Core Components**

### a. **Media Capture and Processing**

- Interfaces with device hardware using [`getUserMedia()`](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia).
- Captured media is encapsulated in `MediaStream` and `MediaStreamTrack` objects.
- Supports optional **audio processing**: AEC (Acoustic Echo Cancellation), AGC (Automatic Gain Control), and NS (Noise Suppression).
- Hardware encoding/decoding is leveraged when possible (e.g., H.264 via VA-API/MediaCodec).

### b. **Media and Data Transmission**

- Real-time transmission via `RTCPeerConnection`.
- Media streams use **SRTP (Secure Real-time Transport Protocol)** for confidentiality and integrity.
- Arbitrary data sent over **SCTP over DTLS over UDP** using `RTCDataChannel`.

### c. **Signaling (Out-of-Scope)**

- Not part of WebRTC spec; developers must implement via WebSockets, HTTP, MQTT, etc.
- Used to exchange **SDP offers/answers** and **ICE candidates** for connection setup.

## 🌐 **Protocol Stack**

### a. **Signaling Phase (Application Layer)**

- Exchange of **Session Description Protocol (SDP)** messages.
- Carries media capabilities (codecs, resolutions, SSRCs), transport info (ICE candidates), and encryption parameters (DTLS fingerprints).

### b. **ICE (Interactive Connectivity Establishment)**

- NAT traversal using:
    - STUN (Session Traversal Utilities for NAT)
    - TURN (Traversal Using Relays around NAT) when P2P fails
- ICE candidates may include:
    - Host candidates (local IP)
    - Server reflexive candidates (via STUN)
    - Relayed candidates (via TURN)

### c. **DTLS (Datagram Transport Layer Security)**

- Mutual authentication via self-signed cert fingerprints in SDP.
- Used to encrypt all subsequent traffic, including SRTP keying (DTLS-SRTP) and SCTP setup.

### d. **SRTP (Secure RTP)**

- Transports media (audio/video).
- Keys derived from DTLS handshake.
- Implements replay protection, authentication, and encryption.

### e. **SCTP (Stream Control Transmission Protocol)**

- Runs over DTLS for `RTCDataChannel`.
- Multiplexed, unordered/reliable delivery options.
- Supports in-order, out-of-order, reliable, and partially reliable modes.

## 🎥 **Media Layer**

### a. **Codec Support**

- Mandatory video: VP8 (Chrome/Firefox), H.264 (mandatory for interoperability per IETF/RFC 7742).
- Audio: Opus (wideband, mandatory), G.711, G.722.

### b. **Jitter Buffer and NACK/PLI/FIR**

- Compensates for packet loss and reordering.
- RTCP feedback mechanisms:
    - **NACK**: Negative Acknowledgment for retransmission
    - **PLI**: Picture Loss Indication
    - **FIR**: Full Intra Request (keyframe)

### c. **Congestion Control and Adaptation**

- **Google Congestion Control (GCC)**, **Transport-CC**, or **SCReAM**
- Bandwidth estimation and dynamic codec bitrate control

## 📡 **Network Considerations**

### a. **UDP Preferred**

- Lower latency, used when NAT/firewall allows
- Fallback to TCP or TURN relay as needed

### b. **Multistream and Simulcast**

- Simulcast: sending multiple spatial/temporal versions of the same video stream.
- SVC (Scalable Video Coding) optionally supported (e.g., VP9).

## 🔐 **Security**

- End-to-end encryption via DTLS-SRTP.
- Fingerprint verification via SDP.
- Media and data integrity, confidentiality, and authentication.
- Browser sandboxes restrict device access; permissions must be explicitly granted.

## 🧪 **Diagnostics & Tooling**

- `getStats()` API for real-time analytics (RTT, jitter, packet loss, bitrate, codec info).
- Tools: webrtc-internals, `RTCIceTransport`, `RTCStatsReport`.

## 📚 Relevant Standards and RFCs

| Spec | Description |
| --- | --- |
| RFC 3264 | SDP Offer/Answer |
| RFC 5245 | ICE (original) |
| RFC 5763 | DTLS-SRTP |
| RFC 3711 | SRTP |
| RFC 5764 | DTLS-SRTP keying |
| RFC 8835 | WebRTC Security Architecture |
| RFC 8830 | JSEP (Javascript Session Establishment Protocol) |
| RFC 8832 | SCTP over DTLS |

## Support

### ✅ Major Browser Support (2025)

| Browser | Supported Since | Notes |
| --- | --- | --- |
| **Chrome** | v23 (2012) | Full support, originator of libwebrtc |
| **Firefox** | v22 (2013) | Full support, interoperable with Chrome |
| **Safari** | v11 (2017) | Limited quirks on iOS/macOS, slow adoption of newer specs |
| **Edge (Chromium)** | v79 (2020) | Same as Chrome support (Chromium base) |
| **Opera** | v18+ (2013) | Chromium-based, inherits Chrome support |
| **iOS Safari** | iOS 11+ | Full support as of iOS 13+, but with serious limitations in background/multitasking |

### 🎯 Core WebRTC API Support

| API | Chrome | Firefox | Safari | Edge (Chromium) |
| --- | --- | --- | --- | --- |
| `getUserMedia()` | ✅ | ✅ | ✅ | ✅ |
| `RTCPeerConnection` | ✅ | ✅ | ✅ | ✅ |
| `RTCDataChannel` | ✅ | ✅ | ✅ | ✅ |
| `getStats()` | ✅ | ✅ | ✅ | ✅ |
| Simulcast (`RID`) | ✅ | ✅ | ⚠️ | ✅ |
| Insertable Streams | ✅ | ⚠️ | ❌ | ✅ |

### 🎥 Media Codec Support

| Codec | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| **Opus** | ✅ | ✅ | ✅ | Default audio codec |
| **VP8** | ✅ | ✅ | ❌ | Not supported in Safari |
| **VP9** | ✅ | ✅ | ⚠️ | Limited support in Safari (experimental) |
| **H.264** | ✅ | ✅ | ✅ | Required for interoperability |
| **AV1** | ✅ | ⚠️ | ❌ | Not yet in WebRTC path in all browsers |

### 📱 Mobile Support

| Platform | Browser | Notes |
| --- | --- | --- |
| **Android** | Chrome, Firefox | Full support |
| **iOS** | Safari | Required due to WebKit restriction |
| **iOS** | Chrome/Firefox | WebView over Safari – inherits Safari behavior |
| **PWA** | ✅ | WebRTC works inside installed PWAs |

### 🧪 Testing Tools

- webrtc-internals (Chrome)
- `getStats()` telemetry hooks
- Wireshark (SRTP/ICE packet inspection)
- TURN/STUN diagnostics: [`trickle-ice`](https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice/)

## Case Studies

> See more in [https://www.reddit.com/r/selfhosted/comments/wreaxu/best_webrtc_open_source_self_hosted_projects_you/](https://www.reddit.com/r/selfhosted/comments/wreaxu/best_webrtc_open_source_self_hosted_projects_you/)  and https://github.com/nuzulul/awesome-webrtc
> 

## References

- [WebRTC](https://en.wikipedia.org/wiki/WebRTC)
- [WebRTC](https://webrtcforthecurious.com/)
- [Stun](https://en.wikipedia.org/wiki/STUN)
- [Learn how WebRTC actually works](https://news.ycombinator.com/item?id=24323589)
- [JANVS WebRTC Server](https://janus.conf.meetecho.com/index.html)
- [WebRTC technology overview and signaling solution design and implementation](https://ieeexplore.ieee.org/abstract/document/7160422)
- [webrtc](https://github.com/pion/webrtc)
- [Peer JS](https://peerjs.com/)
- https://github.com/csiglab/distributed-system-lab
- [ ]  https://www.youtube.com/watch?v=FExZvpVvYxA