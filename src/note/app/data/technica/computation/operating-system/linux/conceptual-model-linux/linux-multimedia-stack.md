# Linux Multimedia Stack

- [Linux Graphics Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-graphics-stack.md)

> The **Linux Multimedia Stack** is a layered, modular subsystem within the Linux operating system that provides kernel-space and user-space interfaces for capturing, processing, encoding, decoding, and rendering multimedia data (audio, video, images), built upon standardized frameworks (e.g., V4L2, ALSA, DRM/KMS, VA-API) and supporting both synchronous and asynchronous data flows through direct hardware interfaces (e.g., DMA, MMAP, IRQs) and software components (e.g., codecs, pipelines, filters), governed by capabilities, node types, memory buffer models, and device-specific controls.
> 

QA:

- Does the Kernel API communicate with the hardware via the drivers? Yes, it always uses the drivers.

## Summary

| **Multimedia Device** | **Driver Type** | **Linux Subsystem** | **Description** |
| --- | --- | --- | --- |
| Webcam / Camera | V4L2 Device Driver | Video4Linux2 (V4L2) | Kernel drivers for video capture devices like webcams and sensors |
| Audio Card / Sound Card | ALSA Driver | Advanced Linux Sound Architecture (ALSA) | Audio capture/playback, mixer controls, MIDI support |
| GPU / Graphics Card | DRM Driver | Direct Rendering Manager (DRM/KMS) | Graphics rendering, display modesetting, buffer management, GPU acceleration |
| TV Tuner / Radio Device | V4L2 Tuner Driver | Video4Linux2 (V4L2) | TV tuner and radio capture hardware |
| Microphone | ALSA Driver | ALSA | Audio input capture devices |
| HDMI Output | DRM Driver | DRM/KMS | Video output over HDMI including display configuration |
| Video Encoder/Decoder | V4L2 M2M Driver | V4L2 Memory-to-Memory (M2M) | Hardware accelerated video encoding and decoding |
| Audio Mixer / DSP | ALSA Driver | ALSA | Digital signal processing, software mixers, equalizers |
| Touchscreen / Input Devices | Input Subsystem Drivers | Linux Input Subsystem | User input devices that interact with multimedia applications |
| Media Controller Device | Media Controller Driver | Media Controller API | Graph-based representation of media pipelines and hardware topology |
| TV Output (CRT, LCD) | DRM or Framebuffer Driver | DRM/KMS or Framebuffer | Video output for legacy or embedded display devices |
| Digital Signal Processors (DSPs) | DSP Drivers | ALSA or custom DSP frameworks | Dedicated hardware for audio/video signal processing |
| Infrared (IR) Receivers | IR Drivers | Input Subsystem or LIRC | Multimedia remote control input devices |
| Camera Sensors (Sub-devices) | V4L2 Subdevice Drivers | V4L2 Media Controller | Control of camera sensor components within complex media pipelines |
| Video Capture Cards | PCIe Capture Card Drivers | V4L2 | Hardware for live video capture and streaming |
| Hardware Accelerated Audio Codecs | Codec Drivers | ALSA or dedicated frameworks | Offload audio codec processing to specialized hardware |
| Remote Control Devices | Input Drivers | Linux Input Subsystem | Input devices for multimedia control via remotes |
| Composite / S-Video Inputs | V4L2 Device Driver | Video4Linux2 (V4L2) | Legacy analog video inputs |
| Screen Capture Devices | Virtual Device Drivers | V4L2 or DRM | Devices enabling screen capture via software or hardware assistance |
| Virtual Devices (Loopback etc.) | Virtual Drivers | V4L2 (v4l2loopback), PulseAudio, PipeWire | Software emulated devices for testing, routing, and mixing |

## Stack (Layers)

| **Layer** | **Component / Interface** | **Technical Role** |
| --- | --- | --- |
| **Applications** | GStreamer, FFmpeg, VLC, PipeWire clients | High-level multimedia applications; abstract the backend complexity |
| **User-Space Libraries** | `libv4l2`, `libasound`, `libdrm`, `libva`, `libpipewire` | Provide API access to kernel interfaces (e.g., capture, playback, composition) |
| **User-Space Daemons** | PipeWire, PulseAudio (deprecated), JACK | Route and mix audio/video streams; negotiate formats and policies |
| **Kernel APIs** | V4L2, ALSA, DRM/KMS, Media Controller API | Low-level interfaces exposed via `/dev` (e.g., `/dev/video0`, `/dev/snd/`) |
| **Device Drivers** | V4L2 camera/sensor drivers, ALSA drivers, GPU drivers | Interface with hardware, implement kernel API backends |
| **Hardware** | SoCs, Codecs, DSPs, HDMI, I²S, PCIe devices | Actual signal producers/consumers (e.g., webcams, microphones, GPUs) |

## 📡 **Core Subsystems**

> 

### 🎙️ **Audio: ALSA (Advanced Linux Sound Architecture)**

- **Device model**: `snd_pcm`, `snd_ctl`, `snd_seq`
- **I/O Model**: MMAP or read/write ring buffer interface
- **Subdevice types**: playback, capture, control, MIDI, sequencer
- **Driver layer**: Handles DMA, interrupts, and codec communication (I²S, HDA)
- **Userspace integration**: PulseAudio or PipeWire routes per-client audio streams

### 📹 **Video Input/Output: V4L2 (Video4Linux2)**

- **Device model**: `video_device`, `vb2_queue`, `v4l2_device`, `media_entity`
- **Node types**: `video`, `vbi`, `radio`, `subdev`
- **Buffer model**: mmap, userptr, DMABUF, read/write
- **Control API**: `VIDIOC_QUERYCTRL`, `VIDIOC_S_CTRL`, etc.
- **Media Controller**: Graph-based API for sensor/pipeline topology description

### 💻 **Display/Rendering: DRM/KMS (Direct Rendering Manager / Kernel Mode Setting)**

- **Device model**: `drm_device`, `drm_crtc`, `drm_encoder`, `drm_connector`
- **Render nodes**: `/dev/dri/renderD*`
- **Memory sharing**: GEM, dumb buffers, PRIME, DMABUF
- **Atomic modesetting**: used for synchronized frame updates
- **Integration**: Supports Wayland compositors, X11 drivers, hardware overlays

### 🎞️ **Hardware Video Acceleration: VA-API, V4L2 M2M**

- **VA-API (libva)**: User-space API to GPU video decode units (e.g., Intel iHD, AMD VCN)
- **V4L2 M2M (Memory-to-Memory)**: Kernel interface for encode/decode accelerators
- **Driver support**: MediaTek, Rockchip, Exynos, Qualcomm VPU/ISP
- **Use case**: Low-power video processing for H.264/H.265/VP9

### 📡 **Stream Routing and Policy: PipeWire**

- **Graph-based model**: Nodes, ports, links
- **Realtime audio/video routing** with low-latency guarantees
- **Protocol bridging**: ALSA ↔ PulseAudio ↔ JACK ↔ Bluetooth ↔ Wayland
- **Security model**: Per-application sandboxing and access control via Flatpak portals

## **DRM (Direct Rendering Manager)**

- **DRM (Direct Rendering Manager)** is a **kernel subsystem**.
- It defines a **framework/API in the kernel** for:
    - Buffer management
    - Command submission
    - Display mode setting (via KMS)
    - GPU resource sharing

Drivers:

| DRM Driver Module | Supported Hardware |
| --- | --- |
| `i915` | Intel integrated GPUs |
| `amdgpu` | AMD Radeon GPUs (GCN+, RDNA) |
| `nouveau` | Open-source NVIDIA GPUs |
| `vmwgfx` | VMware virtual GPU |
| `virtio_gpu` | Virtualized GPU in QEMU/KVM |
| `rockchipdrm` | ARM SoC GPU/display (Rockchip) |
| `sun4i-drm` | Allwinner ARM SoCs (e.g., A64) |
| `vkms` | Virtual Kernel Mode Setting (no hardware) |
| `tidss`, `omapdrm` | Texas Instruments SoCs |
| `udl` | DisplayLink USB graphics adapters |

## Generic Devices

- Broad hardware class support (e.g., UVC, HDA)
- Emulation and testing (e.g., dummy or loopback devices)
- API unification (e.g., V4L2, ALSA abstraction layers)

| **Driver** | **Purpose** |
| --- | --- |
| `v4l2loopback` | Creates a virtual video device (e.g., fake webcam) |
| `snd-dummy` | ALSA dummy sound card for testing |
| `uvcvideo` | Generic USB Video Class driver (many webcams) |
| `snd-hda-intel` | Generic driver for Intel HD Audio-compliant devices |
| `drm-virtual` / `vkms` | Virtual KMS driver for testing graphics stack |
| `pipewire-virt` | Virtual device emulation for audio/video streams |

## **User Space Tools**

| **Category** | **Tool** | **Description** |
| --- | --- | --- |
| **Multimedia Libraries** | **FFmpeg** | Powerful library for video/audio encoding, decoding, streaming, and transcoding. |
|  | **Libav** | Fork of FFmpeg providing multimedia libraries and tools for processing audio/video. |
| **Multimedia Frameworks** | **GStreamer** | Framework to build multimedia apps; supports streaming, encoding, playback, and extensible via plugins. |
| **Audio Servers** | **PulseAudio** | Sound server managing audio streams, providing a higher-level interface for applications. |
| **Audio APIs** | **OpenAL** | Cross-platform audio API for 3D spatial sound, used in gaming and simulations. |
| **Media Players** | **VLC Media Player** | Open-source player supporting most audio/video formats and streaming. |
|  | **MPlayer** | Popular open-source media player supporting a wide variety of formats. |
| **Graphics APIs** | **OpenGL** | API for rendering 2D and 3D graphics, widely used in gaming and graphical applications. |
|  | **Vulkan** | Modern low-level API for high-performance 3D graphics rendering. |
| **Streaming Software** | **OBS Studio** | Open-source software for video recording and live streaming. |
| **Streaming Servers** | **Icecast** | Streaming server to broadcast audio over the internet. |
|  | **Shoutcast** | Popular streaming media server used for internet audio broadcasting. |
| **Video Codecs** | **H.264** | Widely used video codec standard for video compression and decompression. |
|  | **VP9** | Open-source video codec by Google for efficient video compression. |
|  | **HEVC (H.265)** | Successor to H.264 offering improved video compression efficiency. |
| **Audio Codecs** | **MP3** | Common audio codec widely used for streaming and playback. |
|  | **AAC** | Advanced audio codec with better compression than MP3, used for streaming and playback. |
|  | **Opus** | Versatile audio codec optimized for interactive speech and music over the internet. |

## References

- https://lwn.net/Articles/955376/
- https://lwn.net/Articles/955708/
- https://news.ycombinator.com/item?id=38702271
- https://flusp.ime.usp.br/blogs,/kernel-graphics/an_introduction_to_the_linux_graphics_stack/
- https://unix.stackexchange.com/questions/7943/how-is-the-linux-graphics-stack-organised
- [**V4L**] https://en.wikipedia.org/wiki/Video4Linux
- https://en.wikipedia.org/wiki/Advanced_Linux_Sound_Architecture
- https://en.wikipedia.org/wiki/Video_Acceleration_API
- [Alsa] https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture
- [OpenGL](note.html?n=technica/computation/graphical-heterogeneous-high-performance-computing-system/graphical-computing-system/opengl.md)
- [OpenCL](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/opencl.md)