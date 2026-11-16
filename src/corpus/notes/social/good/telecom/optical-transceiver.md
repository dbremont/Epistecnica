---
tags: [note, catalog, good, hardware]
---

# Optical Transceiver

> An **optical transceiver** is a pluggable module that converts an electrical signal into light and light back into an electrical signal, so a switch, router or line-card port reaches across a fibre link.

It is the priced, swappable unit of a datacenter or carrier build: the port, the fibre and the rack outlive the module, so the module is bought per link — one per rate, one per reach, one per wavelength.

## Forms

| Form factor | Lanes and rate | Where it is used |
| --- | --- | --- |
| SFP, SFP+, SFP28 | One lane: 1G, 10G, 25G | Access ports and short-reach links |
| QSFP+, QSFP28 | Four lanes: 40G, 100G | Spine–leaf uplinks |
| QSFP-DD, OSFP | Eight lanes: 200G, 400G, 800G | Current datacenter fabrics |

## What defines a part number

A module is not interchangeable with another of the same form factor: what a buyer specifies is the combination below, and every one of them has to match at both ends of the link.

| Parameter | What it fixes |
| --- | --- |
| Rate | The line rate the host port drives and the far end expects |
| Reach | The distance grade the optics are qualified for — short-reach multimode to long-haul single-mode |
| Wavelength grid | 850 nm on multimode, 1310 nm and 1550 nm on single-mode, and the CWDM/DWDM grids that put several links on one fibre |
| Connector | LC duplex for one lane, MPO/MTP ribbon for parallel lanes |
| Coding and FEC | The line coding and forward error correction the host is configured for |
| Compliance | The multi-source agreement (SFF, QSFP) that fixes the mechanical and electrical interface, and the standard the link answers to — IEEE 802.3 Ethernet, ITU-T OTN |

## Where the value sits

The module carries no proprietary lock of its own: interoperability is the product. Its value is set by compliance with the MSAs and the host's qualified-vendor list, by yield and test cost at the rate it is built for, and by the reach it buys — the same bit rate travels further as the optics and the coding improve.

## References

- https://en.wikipedia.org/wiki/Optical_transceiver
- [Transceiver](/view.html?p=notes/social/good/telecom/transceiver.md) — the family the module is the fibre instance of
- [Ethernet](/view.html?p=notes/technica/computation/telecom/ethernet.md) — the standard the link answers to
- [Interconnect](/view.html?p=notes/technica/computation/platform/hardware-physical-substrate/interconnect.md) — the technical-object reading of the link the module terminates
