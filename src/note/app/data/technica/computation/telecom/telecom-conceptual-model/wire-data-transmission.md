---
tags: [wire-data-transmission]
---

# Wire Data Transmission

- [Ethernet](note.html?n=technica/computation/telecom/telecom-conceptual-model/ethernet.md), [Twisted Pair Cable](note.html?n=technica/computation/telecom/telecom-conceptual-model/twisted-pair-cable.md), [Wireless Data Transmission](note.html?n=technica/computation/telecom/telecom-conceptual-model/wireless-data-transmission.md)

> Signal: In [electronics](https://en.wikipedia.org/wiki/Electronics) and [telecommunications](https://en.wikipedia.org/wiki/Telecommunications), *signal* refers to any time-varying [voltage](https://en.wikipedia.org/wiki/Voltage), [current](https://en.wikipedia.org/wiki/Electric_current), or [electromagnetic wave](https://en.wikipedia.org/wiki/Electromagnetic_wave) that carries information.
> 

> **Analog Signals**: Continuous waveforms representing data (e.g., voice signals in traditional telephony).
> 

> **Digital Signals**: Discrete waveforms representing binary data (e.g., Ethernet signals).
> 

> **Electrical Signals (Copper Wires)**: Data is transmitted as electrical voltage or current variations.
> 

> **Optical Signals (Fiber Optics)**: Data is transmitted as light pulses.
> 

QA:

- How is data transmitted through a wire medium?

## Transmission Methods

> 

| **Category** | **Method/Technique** | **Description** | **Applications** |
| --- | --- | --- | --- |
| **Analog Transmission** | Amplitude Modulation (AM) | Varies the amplitude of the carrier signal to encode information. | Radio broadcasting, traditional telephony. |
|  | Frequency Modulation (FM) | Varies the frequency of the carrier signal to encode information. | Radio broadcasting, analog communication. |
|  | Phase Modulation (PM) | Varies the phase of the carrier signal to encode information. | Advanced communication systems. |
| **Digital Transmission** | Baseband Transmission | Sends digital signals directly over the wire without modulation. | Ethernet (twisted-pair cables). |
|  | Broadband Transmission | Modulates digital signals onto a carrier wave for transmission. | Cable TV (DOCSIS), DSL. |
| **Transmission Media** | Twisted-Pair Cables (UTP/STP) | Two insulated copper wires twisted together to reduce interference. | LANs, telephone networks. |
|  | Coaxial Cables | Central conductor surrounded by insulation and shielding. | Cable TV, broadband internet. |
|  | Fiber-Optic Cables | Uses light pulses to transmit data through glass or plastic fibers. | High-speed internet, data centers. |
| **Signal Encoding** | Non-Return-to-Zero (NRZ) | Represents binary data using two voltage levels. | Digital communication systems. |
|  | Manchester Encoding | Encodes data by transitioning voltage levels mid-bit for synchronization. | Ethernet, RFID. |
|  | 4B/5B Encoding | Maps 4 bits of data to 5-bit symbols for synchronization. | Fiber Channel, Fast Ethernet. |
|  | Pulse Code Modulation (PCM) | Converts analog signals into digital data by sampling and quantizing. | Digital telephony, audio recording. |
| **Multiplexing** | Time-Division Multiplexing (TDM) | Divides the transmission medium into time slots for multiple signals. | Digital telephony, SONET/SDH. |
|  | Frequency-Division Multiplexing (FDM) | Divides the transmission medium into frequency bands for multiple signals. | Radio broadcasting, cable TV. |
|  | Wavelength-Division Multiplexing (WDM) | Transmits multiple light wavelengths simultaneously in fiber optics. | High-capacity fiber-optic networks. |
| **Error Detection/Correction** | Parity Check | Adds a parity bit to detect single-bit errors. | Simple error detection in communication. |
|  | Cyclic Redundancy Check (CRC) | Adds a checksum to detect errors in data frames. | Ethernet, storage systems. |
|  | Forward Error Correction (FEC) | Adds redundancy to correct errors without retransmission. | Satellite communication, fiber optics. |
| **Protocols/Standards** | Ethernet (IEEE 802.3) | Defines wired LAN transmission using twisted-pair or fiber-optic cables. | Local area networks (LANs). |
|  | DSL (Digital Subscriber Line) | Uses existing telephone lines for high-speed internet. | Broadband internet. |
|  | SONET/SDH | Standard for high-speed data transmission over fiber optics. | Long-distance communication, telecom. |
| **Key Considerations** | Bandwidth | The range of frequencies a medium can support. | Determines data rate and capacity. |
|  | Attenuation | Signal loss over distance. | Limits transmission distance. |
|  | Noise and Interference | External disturbances affecting signal quality. | Reduces signal integrity. |
|  | Impedance Matching | Ensures proper signal transfer between components. | Prevents signal reflections. |
|  | Crosstalk | Interference between adjacent wires. | Affects signal quality in twisted-pair cables. |

## **Signal Encoding and Modulation**

- **Digital Transmission**:
    - **Baseband Transmission**: Digital signals are sent directly over the wire without modulation (e.g., Ethernet).
    - **Broadband Transmission**: Digital signals are modulated onto a carrier wave for transmission (e.g., DSL, cable modems).
- **Analog Transmission**:
    - **Amplitude Modulation (AM)**: Varies the amplitude of the carrier wave.
    - **Frequency Modulation (FM)**: Varies the frequency of the carrier wave.
    - **Phase Modulation (PM)**: Varies the phase of the carrier wave.

## **Multiplexing**

- **Time-Division Multiplexing (TDM)**:
    - Divides the transmission medium into time slots for multiple signals.
- **Frequency-Division Multiplexing (FDM)**:
    - Divides the transmission medium into frequency bands for multiple signals.
- **Wavelength-Division Multiplexing (WDM)**:
    - Used in fiber optics to transmit multiple light wavelengths simultaneously.

## **Error Detection and Correction**

- **Parity Check**: Adds a parity bit to detect single-bit errors.
- **Cyclic Redundancy Check (CRC)**: Adds a checksum to detect errors in data frames.
- **Forward Error Correction (FEC)**: Adds redundancy to correct errors without retransmission.

## **Reception and Decoding**

- **Signal Reception**: The receiver detects the transmitted signal from the wire medium.
- **Demodulation**: For modulated signals, the carrier wave is removed to extract the original data.
- **Decoding**: The received signal is decoded back into its original format (e.g., binary data, audio, video).

## References

- https://en.wikipedia.org/wiki/Wired_communication
- https://en.wikipedia.org/wiki/Telecommunications_cable
- https://en.wikipedia.org/wiki/Submarine_communications_cable
- https://en.wikipedia.org/wiki/Networking_cable
- https://en.wikipedia.org/wiki/Category:Signal_cables
- https://www.youtube.com/watch?v=CQSEXh0nIzE
- 
- [Electric Current](https://app.notion.com/p/Electric-Current-10cc0f5171ec809b883fcd91de073375?pvs=21)
- [Electromagnetism](https://app.notion.com/p/Electromagnetism-ecb3d9ce10f0425a85326aa81634a0d9?pvs=21)
- 
- [Atom](https://app.notion.com/p/Atom-10cc0f5171ec8083b1baf8f9d2d99620?pvs=21)
- [Electron](https://app.notion.com/p/Electron-4a58d4f541064542a3a7ca2a62efd4de?pvs=21)
- 
- [Electric Charge](https://app.notion.com/p/Electric-Charge-1b0c0f5171ec80e98af5c745a32f391b?pvs=21)
- [**Standard Model**](https://app.notion.com/p/Standard-Model-114c0f5171ec80e1a308d797b3aa3236?pvs=21)
- [Fundamental Interaction](https://app.notion.com/p/Fundamental-Interaction-16dc0f5171ec807cb855fab0666eb952?pvs=21)
- [Magnetism](https://app.notion.com/p/Magnetism-c282c3b0c9d140e7859e81c620f3b78a?pvs=21)
- [Electrical Conductor](https://app.notion.com/p/Electrical-Conductor-1b0c0f5171ec807ab173e5d49b9e81ac?pvs=21)