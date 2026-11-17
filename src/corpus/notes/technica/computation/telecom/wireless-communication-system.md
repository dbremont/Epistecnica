---
tags: [note, wireless, communication-system, radio, telecom, spectrum]
qa:
 - The channel is open and shared. Which design constraint follows from that alone — the modulation, the medium access, or the regulation of the spectrum?
 - Shannon's limit is a ceiling, not a target. Why do systems keep being sold as if the ceiling were a specification?
 - Every generation from 1G to 5G changed the multiple-access scheme. Is that the real axis of the history, or is it the antenna and the amplifier underneath it?
---

# Wireless Communication System

> A **wireless communication system** is a complete chain that carries information through an unguided medium: source, modulator, transmitter, antenna, the propagation channel, antenna, receiver, demodulator, sink — plus the two coordination layers a cable does not need, **duplexing** (who transmits when in each direction) and **medium access** (who transmits when among many).

> It is defined by what it does not have: no guided medium. The channel is open, shared, unlicensed in principle and regulated in practice, and hostile in ways a cable is not — path loss, multipath, interference, and other people using the same spectrum. Every engineering decision in the chain is a response to that fact, and the whole historical development of the field is the accumulation of those responses.

## Architecture

| **Stage** | **What it does** | **The wireless-specific problem** |
| --- | --- | --- |
| **Source** | Produces the information (voice, data, video) | Bandwidth demand, which grows faster than capacity |
| **Source coding** | Compresses: removes redundancy | Compression makes the stream fragile to errors |
| **Channel coding** | Adds redundancy back, deliberately, to survive errors | The error rate is unknown in advance and varies with position |
| **Modulation** | Maps bits onto a waveform: amplitude, frequency, phase, or all at once | Spectrum efficiency against robustness — the trade never disappears |
| **Up-conversion and power amplifier** | Moves the signal to a carrier and amplifies it | Power is scarce in the handset and expensive in the base station |
| **Antenna** | Couples the electrical signal to the electromagnetic field | Gain, directivity, and the physics of the aperture |
| **Propagation channel** | The medium: free space, ground, buildings, weather | Path loss, shadowing, multipath fading, Doppler — the part the engineer does not control |
| **Antenna** | Receives the field | Small apertures hear little and interference a lot |
| **Low-noise amplification and down-conversion** | Recovers a weak signal without destroying it | Noise figure sets the sensitivity floor |
| **Demodulation and decoding** | Recovers bits, then corrects errors | Equalisation, synchronisation, and the cost of getting it wrong |
| **Sink** | The information, delivered | Delay and jitter, which matter for control as much as for voice |

Two coordination layers sit outside the chain and are what make it a *system* rather than a link:

- **Duplexing** — frequency-division (FDD: separate uplink and downlink bands) or time-division (TDD: one band, alternating slots). The choice fixes the frame structure of everything above it.
- **Medium access** — who may transmit when: scheduled (the base station allocates), contention-based (listen before talk, as in Wi-Fi), or a hybrid. This is where a wireless system differs most from a wired one, because the wire can be switched and the air cannot.

## Transmission

Wireless transmission carries data on **electromagnetic waves** — radio, microwave, infrared, or visible light — by **modulating** a carrier: varying its amplitude, frequency or phase, alone or in combination. The choice of band decides the physics before the protocol does: lower frequencies travel further and penetrate better but carry less; higher frequencies carry more but need line of sight and dense deployment.

Three physical resources bound every design:

- **Spectrum** — a scarce, regulated, and auctioned resource, which is why the air is shared by licence rather than by claim.
- **Power** — energy per bit is the constraint in anything battery-powered, and the thermal constraint in anything transmitting at scale.
- **Noise and interference** — the floor set by physics, and the ceiling set by other users.

And one theoretical one, which is the field's constitution: **Shannon's capacity law** — the maximum error-free rate is a function of bandwidth and signal-to-noise ratio, and no coding, modulation or cleverness exceeds it. Every generation since 1948 has been an attempt to get closer to a limit that was stated before the systems existed.

## Historical developments

| **Year** | **Development** | **Who** | **What changed** |
| --- | --- | --- | --- |
| 1865 | Maxwell's equations | James Clerk Maxwell | Electromagnetic waves predicted; radio becomes possible in principle |
| 1888 | Experimental demonstration of electromagnetic waves | Heinrich Hertz | The prediction confirmed: a spark gap transmits and a loop receives |
| 1895 | First radio transmission | Guglielmo Marconi | Wireless spans distance, in the laboratory and then across the Channel |
| **1896** | **First radio patent — UK 12039, "Improvements in Transmitting Electrical Impulses and Signals"** | Marconi | Wireless becomes property: the patent is the instrument that turns a demonstration into a business |
| 1900 | Tesla's radio patents (US 645,576 and 649,621) | Nikola Tesla | The priority claim that later disputes would turn on |
| 1901 | Transatlantic transmission | Marconi | The ocean stops being a barrier to signalling |
| 1906 | The audion (triode), patented 1907 (US 841,387); first voice broadcast | Lee de Forest; Reginald Fessenden | Amplification and voice: the receiver no longer needs a coherer and an operator's ear |
| 1920s | Broadcasting | — | One transmitter, many receivers: the mass medium, and the first spectrum regulation |
| 1933 | Frequency modulation | Edwin Armstrong | Interference resistance, at the cost of bandwidth |
| 1935–45 | Radar | Robert Watson-Watt and others | Microwaves, and the wartime component industry that made them |
| **1947–50** | **Transistor (Bardeen and Brattain, patent 1950; Shockley's junction patent the same year)** | Bell Labs | Amplification without valves: radios shrink, power falls, and the handset becomes conceivable |
| 1948 | Information theory | Claude Shannon | The **limit**: capacity as a formula, and the discipline that computes against it |
| **1959** | **Integrated circuit patents (Kilby, US 3,138,743 filed 1959; Noyce, US 2,981,877)** | Jack Kilby; Robert Noyce | The radio becomes a chip, and the chip becomes cheap |
| 1962 · 1965 | Telstar; Intelsat "Early Bird" | — | Satellite links: global reach without a cable |
| 1973 | Handheld cellular prototype | Martin Cooper (Motorola) | Mobility demonstrated; the patent (US 3,906,166, "Radio Telephone System") follows in 1975 |
| 1979 · 1983 | First cellular network (Japan, NTT); AMPS launched in the United States | NTT; Bell System | **1G**: analogue voice, frequency reuse, handover between cells |
| 1991 | GSM launched | ETSI and the GSM consortium | **2G**: digital voice, SMS, roaming — and the standard as the unit of design |
| 1997 | IEEE 802.11 | IEEE | Wi-Fi: unlicensed local wireless, and the ISM bands as a commons |
| 2001 | 3G (W-CDMA) commercial launch | NTT DoCoMo | Data rather than voice: the phone becomes a terminal |
| 2009 | LTE | 3GPP | **4G**: all-IP broadband, OFDMA, the flat architecture |
| 2019 | 5G commercial launch | 3GPP | **5G**: millimetre wave, massive MIMO, network slicing, low latency |
| 2019– | LEO constellations | SpaceX and others | The system moves into orbit: a base station in the sky, and a new interference regime |

**What the table shows.** Three waves, not one. The first (1865–1920) is physics and the patent: waves, then property. The second (1930–1960) is components — valves, radar, the transistor, the chip — which is what made portable wireless possible at all. The third (1971–) is systems: cellular reuse, digital standards, and the shift from a device to a network. The patent rows matter because each wave was financed by a claim to exclusivity, and the disputes over those claims (Marconi and Tesla, de Forest and Armstrong, Kilby and Noyce) are as much a part of the history as the circuits.

## Generations

| **Generation** | **Multiple access** | **Core change** | **What it made possible** |
| --- | --- | --- | --- |
| **1G** | FDMA | Analogue voice, frequency reuse | The mobile phone as a product |
| **2G** | TDMA / CDMA | Digital, SMS, roaming, encryption | The phone as a personal identifier |
| **3G** | W-CDMA | Packet data at usable rates | The phone as a terminal |
| **4G** | OFDMA | All-IP, flat network, MIMO | The phone as a broadband link |
| **5G** | OFDMA + massive MIMO | Millimetre wave, slicing, low latency | The network as infrastructure for other systems |

## Relation

| **Concept** | **Relation** |
| --- | --- |
| [Telecom](/view.html?p=notes/technica/computation/telecom/telecom.md) | The parent technical element: communication through a connectivity mechanism |
| [Antenna](/view.html?p=notes/technica/computation/telecom/antenna.md) | The component that couples the circuit to the field, and the one that decides what the system can hear |
| [Wire Data Transmission](/view.html?p=notes/technica/computation/telecom/wire-data-transmission.md) | The guided counterpart, where the channel is owned and switching is possible |
| [Bluetooth](/view.html?p=notes/technica/computation/telecom/bluetooth.md) | A short-range system using the same chain with a contention-based access scheme |
| [ESIM](/view.html?p=notes/technica/computation/telecom/esim.md) | The identity layer of a cellular system, independent of the radio |
| [Data Plane](/view.html?p=notes/technica/computation/telecom/data-plane.md) · [Control Plane](/view.html?p=notes/technica/computation/telecom/control-plane.md) | How the system separates what it forwards from what it decides |

## References

- Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423. — the capacity law, and the reason the field has a ceiling to design against
- Marconi, G. (1896). *Improvements in transmitting electrical impulses and signals* (UK Patent No. 12039). — the first radio patent
- Bell, A. G. (1876). *Improvement in telegraphy* (U.S. Patent No. 174,465). — included for contrast: the wire that wireless was built to escape
- Bardeen, J., & Brattain, W. H. (1950). *Three-electrode circuit element utilizing semiconductive materials* (U.S. Patent No. 2,524,035). — the transistor, in the form that made portable radios possible
- Kilby, J. S. (1959). *Miniaturized electronic circuits* (U.S. Patent No. 3,138,743, filed 1959). — the integrated circuit
- Molisch, A. F. (2011). *Wireless communications* (2nd ed.). Wiley. — the chain, the channel and the standards, treated as one subject
- Rappaport, T. S. (2002). *Wireless communications: Principles and practice* (2nd ed.). Prentice Hall. — the propagation and link-budget view
- Tse, D., & Viswanath, P. (2005). *Fundamentals of wireless communication*. Cambridge University Press. — the information-theoretic account, where capacity regains its place as the organising idea
- [Wireless](https://en.wikipedia.org/wiki/Wireless) · [History of radio](https://en.wikipedia.org/wiki/History_of_radio) · [Cellular network](https://en.wikipedia.org/wiki/Cellular_network)
- [Telecom](/view.html?p=notes/technica/computation/telecom/telecom.md) — the parent note
- [Antenna](/view.html?p=notes/technica/computation/telecom/antenna.md) — the component the field is built around
