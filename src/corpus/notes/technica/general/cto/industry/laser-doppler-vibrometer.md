---
tags: [note, laser-doppler-vibrometer, metrology]
---

# Laser Doppler Vibrometer (LDV)

> The **laser Doppler vibrometer** measures the velocity of a surface without touching it, by interferometry: a laser beam is split, one part reflects from the vibrating surface, the two parts recombine, and the Doppler shift of the moving reflection appears as a frequency modulation of the interference signal.

## Formulation

### What technical element type does this technical instance belong to?

**The LDV belongs to the `Production Technical Object` technical element type** — a produced instrument enabling a measurement action, typed as the [radar](/view.html?p=notes/technica/general/cto/industry/radar.md) on the same shelf is typed: an electromagnetic measurement object rather than a production plant.

Readable secondarily as a `Constitutive Technical Object` when it is one element of a modal-analysis or condition-monitoring installation, and as a `Machine` where its function is the actuation of a scanning stage. Those readings are prose, not second roots.

### What is this technical instance?

> A laser head on a tripod aimed at a loudspeaker cone, a turbine blade through a window, a MEMS diaphragm under a microscope objective, a hard-disk suspension, a human eardrum; a scanning head that sweeps a grid of points over a car body and assembles the mode shapes; a three-beam head that resolves all three velocity components at once.

The instrument's physics is a Michelson interferometer with a moving mirror, and three details make it what it is:

- **The factor of two.** The beam travels to the surface and back, so the measured shift is $f_D = 2v/\lambda$ — twice a one-way Doppler measurement. That is why the output is velocity directly, and displacement or acceleration only by integration or differentiation.
- **Heterodyne detection.** A Bragg cell frequency-shifts the reference beam, so the photodetector sees a carrier that the vibration modulates up and down. Without the carrier, a fringe-counting homodyne system could measure speed but not *sign* — it could not tell approach from recession.
- **Speckle.** The surface is rarely a mirror; the returned light is a speckle pattern, and the instrument lives with the consequence: signal dropouts, the need for a good return, and the reason a retroreflective tape is often stuck to the target.

The applications follow from the measurement being non-contact and direct in velocity: modal analysis and experimental dynamics, MEMS and micro-device characterisation, rotating machinery and turbine blades, loudspeaker and ultrasonic transducer testing, biomedical measurement on structures too delicate to attach a sensor to, and the calibration of accelerometers by laser primary standard.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one instrument, decomposed to its constituent assembly, its kinds, the parameters that govern its measurement and the evaluations that accept it. The interference and Doppler physics belongs to the phenomena notes; the optics design belongs to optical metrology.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique and complete from the root; backticked segments name a type, plain segments an instance.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical Object` → Laser Doppler Vibrometer | Non-contact interferometric velocity sensor. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Constitutive Technical Object` | Grouping: the assembly. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Constitutive Technical Object` → Laser Source | Single-frequency, coherent source — He-Ne, or a diode laser where compactness matters. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Constitutive Technical Object` → Interferometer Optics | Splitter, reference path and recombination: the Michelson core. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Constitutive Technical Object` → Bragg Cell | Acousto-optic frequency shifter that creates the carrier for heterodyne detection and carries the sign of the velocity. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Constitutive Technical Object` → Photodetector | Converts the recombined light into an electrical signal at the beat frequency. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Constitutive Technical Object` → Demodulator and Decoder | Extracts the instantaneous frequency, and hence velocity, from the carrier — the part that turns optics into a number. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Constitutive Technical Object` → Beam Steering | Manual aiming, or a scanning mirror pair for grid measurement. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Constitutive Technical Object` → `Technical Configuration` | Grouping: the settings that decide whether a measurement is valid. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Constitutive Technical Object` → `Technical Configuration` → Stand-off Distance and Focus | Working distance and spot size; a defocused spot averages the surface and lowers the signal. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Constitutive Technical Object` → `Technical Configuration` → Velocity Range and Decimation | The decoder's bandwidth against the vibration amplitude — the setting most often wrong. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Constitutive Technical Object` → `Technical Configuration` → Surface Treatment | Retroreflective tape or paint where the natural return is too weak. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Machine` | Grouping: instrument kinds by function. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Machine` → Single-Point Vibrometer | One beam, one axis: the laboratory standard. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Machine` → Scanning Vibrometer | Two mirrors and a grid: mode shapes assembled from many points. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Machine` → Three-Dimensional Vibrometer | Three (or six) beams from different angles, resolving the full velocity vector. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Machine` → Differential Vibrometer | Two spots, one on each side of a structure: the relative motion, with common-mode noise rejected. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Technical Evaluation` | Grouping: what accepts the measurement, and what bounds it. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Technical Evaluation` → Line-of-Sight Constraint | Only the velocity component along the beam is measured; the rest needs another geometry. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Technical Evaluation` → Speckle Dropout | Rough surfaces produce signal loss; the trace has gaps exactly where the return decorrelates. |
| `Production Technical Object` → Laser Doppler Vibrometer → `Technical Evaluation` → Calibration Traceability | Wavelength is the scale factor, so the instrument is calibrated against the laser, not against a shaker — which is why it is used as the primary standard for accelerometers. |

**Limitations.** *Line of sight* — the target must be visible and stationary enough in the frame; nothing is measured through an opaque wall. *Surface dependence* — a matte, dark, curved or transparent target returns little light, so the measurement often depends on the preparation of the object rather than on the instrument. *Sign ambiguity without heterodyne* — the cheap configurations measure speed only. *Ambient vibration* — the instrument measures its own mount as well as the target, which is why optical tables and tripods matter.

## References

- Yeh, Y., & Cummins, H. Z. (1964). Localized fluid flow measurements with a He-Ne laser spectrometer. *Applied Physics Letters*, 4(10), 176–178. — the first laser Doppler measurement, and the demonstration that the shift is usable as a velocity signal
- Drain, L. E. (1980). *The laser Doppler technique*. Wiley. — the optics and the signal processing, including the heterodyne scheme this instrument depends on
- Rothberg, S. J., Allen, M. S., Castellini, P., et al. (2017). An international review of laser Doppler vibrometry: Making light work of vibration measurement. *Optics and Lasers in Engineering*, 99, 11–22. — the review, with applications and the calibration role
- [Laser Doppler vibrometer](https://en.wikipedia.org/wiki/Laser_Doppler_vibrometer)
- [Doppler Effect](/view.html?p=notes/nature/phenomena/doppler-effect.md) — the phenomenon, and the factor of two
- [Interference](/view.html?p=notes/nature/phenomena/interference.md) · [Polarisation](/view.html?p=notes/nature/phenomena/polarisation.md) — the physics inside the head
- [Radar](/view.html?p=notes/technica/general/cto/industry/radar.md) — the sibling instrument, typed the same way
- [Metrology Services](/view.html?p=notes/technica/general/cto/industry/metrology-services.md) — the practice this instrument serves
