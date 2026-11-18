---
tags: [note, production, welding, joining, metallurgy]
---

# Welding

> **Welding** is the joining of materials by fusion or by pressure at the interface, so that the joint becomes continuous with the parts it connects — a metallurgical bond rather than an adhesive one. It is the technique that turns plates, sections and pipes into a structure, and the one whose failures are least forgiving.

> Every welding process answers the same three questions: how is the heat delivered, how is the molten metal protected from the air, and how is the joint filled. The answers differ — an arc, a laser, a current through the contact resistance, friction — and each answer fixes the process's thickness range, its position capability, its distortion and its defects.

## Formulation

### What technical element type does this technical instance belong to?

**Welding belongs to the `Technical Practice` technical element type — a repeatable, organized pattern of technical work integrating tasks, processes, equipment, parameters, standards and inspections.**

It is a practice because it is a standing way of working — design the joint, qualify the procedure, fit up, weld within the parameters, inspect — not a single process or a single machine. It is readable as a `Technical Element Set` because with the practice come the processes, the consumables, the power sources, the qualification standards and the inspection methods.

The boundary against **brazing and soldering** is that they do not melt the parent metal; against **adhesive bonding** that they produce no metallurgical continuity; against **heat treatment** that the heat is a means to join, not the purpose. The joint is the element; the process is the practice.

### What is this technical instance?

> A joint made by melting the parent metal, or the parent plus a filler, under a shield that keeps oxygen and nitrogen out, then letting it solidify into a cast structure continuous with the parts. Around it sits a heat-affected zone whose properties are changed without melting, and residual stress distributed across the assembly. The outputs are a joint that meets a procedure and an acceptance standard; the warrant is the qualified procedure plus the inspection record.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one welding practice, decomposed at shallow depth — purposes, problems, tasks, processes, equipment, instruments, parameters, standards and evaluations. The structure being welded and the metallurgy of its alloy are separate elements.
>
> Stopping rule: a row is terminal when it names a process, an item of equipment, a measured parameter, a standard or an inspection.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.
>
> Verbs: the arc *melts*; the shield *protects*; the procedure *qualifies*; the inspection *accepts*.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Practice` → Welding | The practice that joins metal by fusion or pressure into a continuous joint. |
| `Technical Practice` → Welding → `Technical Purpose` | Grouping: the purposes the practice is constituted to serve. |
| `Technical Practice` → Welding → `Technical Purpose` → Join Permanently | Make a connection that carries load and cannot be undone without cutting. |
| `Technical Practice` → Welding → `Technical Purpose` → Seal | Make a joint tight to fluid or gas — the pipe and pressure-vessel case. |
| `Technical Practice` → Welding → `Technical Purpose` → Restore | Rebuild worn or damaged metal to its original section. |
| `Technical Practice` → Welding → `Technical Problem` | Grouping: the discrepancies between the required and the achieved joint. |
| `Technical Practice` → Welding → `Technical Problem` → Distortion | Non-uniform heating and cooling shrink the assembly out of shape. |
| `Technical Practice` → Welding → `Technical Problem` → Residual Stress | The joint cools against restraint and locks stress into the structure. |
| `Technical Practice` → Welding → `Technical Problem` → Hydrogen Cracking | Diffusible hydrogen plus hard microstructure plus restraint cracks the joint after it cools. |
| `Technical Practice` → Welding → `Technical Problem` → Porosity | Gas trapped in the solidifying metal leaves voids. |
| `Technical Practice` → Welding → `Technical Problem` → Lack of Fusion | The arc fails to melt the joint face or the previous pass. |
| `Technical Practice` → Welding → `Technical Problem` → Heat-Affected-Zone Degradation | The parent metal beside the weld loses toughness or hardens beyond specification. |
| `Technical Practice` → Welding → `Technical Task` | Grouping: the tasks the practice runs. |
| `Technical Practice` → Welding → `Technical Task` → Design the Joint | Choose the joint type, preparation, root gap and access for the process. |
| `Technical Practice` → Welding → `Technical Task` → Qualify the Procedure | Write and prove the welding procedure and the welder's qualification on test pieces. |
| `Technical Practice` → Welding → `Technical Task` → Fit Up | Assemble and tack the parts within tolerance before welding. |
| `Technical Practice` → Welding → `Technical Task` → Weld Within Parameters | Run the passes at the qualified current, voltage, speed and heat input. |
| `Technical Practice` → Welding → `Technical Task` → Inspect | Examine the joint against the acceptance criteria and record the result. |
| `Technical Practice` → Welding → `General Technique` | Grouping: the processes the practice uses. |
| `Technical Practice` → Welding → `General Technique` → Shielded Metal Arc Welding | A coated consumable electrode struck against the work — the portable, all-position process. |
| `Technical Practice` → Welding → `General Technique` → Gas Metal Arc Welding | A continuous wire fed into a gas-shielded arc — MIG for reactive metals, MAG for steel. |
| `Technical Practice` → Welding → `General Technique` → Tungsten Inert Gas Welding | A non-consumable tungsten electrode in an inert shield — the precision process, with or without filler. |
| `Technical Practice` → Welding → `General Technique` → Submerged Arc Welding | The arc buried under a granular flux — high deposition for thick plate. |
| `Technical Practice` → Welding → `General Technique` → Flux-Cored Arc Welding | A tubular wire carrying its own flux — field welding without a gas bottle. |
| `Technical Practice` → Welding → `General Technique` → Resistance Welding | Current through the contact resistance — spot and seam welding of sheet. |
| `Technical Practice` → Welding → `General Technique` → Laser and Electron-Beam Welding | A focused energy beam for narrow, deep, low-distortion joints. |
| `Technical Practice` → Welding → `General Technique` → Friction Stir Welding | A rotating tool stirs the plasticised metal — solid state, no melting. |
| `Technical Practice` → Welding → `General Technique` → Oxyfuel Welding | A fuel-gas flame melts the joint — the older, portable process. |
| `Technical Practice` → Welding → `Constitutive Technique` | Grouping: the techniques embodied in the joint. |
| `Technical Practice` → Welding → `Constitutive Technique` → Heat-Input Control | Fix the energy per unit length so the cooling rate and the heat-affected zone are the qualified ones. |
| `Technical Practice` → Welding → `Constitutive Technique` → Preheat and Post-Weld Heat Treatment | Slow the cooling and temper the hardened zone to keep hydrogen cracking away. |
| `Technical Practice` → Welding → `Constitutive Technique` → Shielding | Exclude oxygen and nitrogen from the molten metal with gas, flux or slag. |
| `Technical Practice` → Welding → `Constitutive Technical Object` | Grouping: the equipment the practice runs on. |
| `Technical Practice` → Welding → `Constitutive Technical Object` → Welding Power Source | Constant-current or constant-voltage supply, chosen by process. |
| `Technical Practice` → Welding → `Constitutive Technical Object` → Torch or Electrode Holder | Delivery of current, filler and shield to the joint. |
| `Technical Practice` → Welding → `Constitutive Technical Object` → Filler Metal | Consumable wire, rod or electrode whose composition matches the joint's duty. |
| `Technical Practice` → Welding → `Constitutive Technical Object` → Fixture and Positioner | Support and rotation that hold the assembly and the position. |
| `Technical Practice` → Welding → `Constitutive Technical Object` → Shielding Gas Supply | Bottle, manifold and flow control for the inert or active gas. |
| `Technical Practice` → Welding → `Production Instrument` | Grouping: the measurement and inspection the practice relies on. |
| `Technical Practice` → Welding → `Production Instrument` → Welding Parameter Meter | Current, voltage, wire feed and travel speed recorded against the procedure. |
| `Technical Practice` → Welding → `Production Instrument` → Visual and Dimensional Inspection | The first and cheapest check: bead shape, undercut, alignment. |
| `Technical Practice` → Welding → `Production Instrument` → Radiographic Testing | X-ray or gamma transmission for internal volumetric defects. |
| `Technical Practice` → Welding → `Production Instrument` → Ultrasonic Testing | Reflection from internal defects, including planar lack of fusion. |
| `Technical Practice` → Welding → `Production Instrument` → Magnetic Particle and Dye Penetrant Testing | Surface and near-surface defect detection. |
| `Technical Practice` → Welding → `Technical Parameter` | Grouping: the variables that fix the joint. |
| `Technical Practice` → Welding → `Technical Parameter` → Welding Current | The amperage that sets penetration and deposition rate. |
| `Technical Practice` → Welding → `Technical Parameter` → Arc Voltage | The arc length and bead shape. |
| `Technical Practice` → Welding → `Technical Parameter` → Travel Speed | The rate that, with current and voltage, fixes heat input. |
| `Technical Practice` → Welding → `Technical Parameter` → Heat Input | Energy per unit length, in kJ/mm — the variable that controls the heat-affected zone. |
| `Technical Practice` → Welding → `Technical Parameter` → Preheat and Interpass Temperature | The temperatures that govern cooling rate and hydrogen escape. |
| `Technical Practice` → Welding → `Technical Parameter` → Carbon Equivalent | The alloy's weldability index, fixing preheat and procedure. |
| `Technical Practice` → Welding → `Technical Standard` | Grouping: the norms the practice works to. |
| `Technical Practice` → Welding → `Technical Standard` → AWS D1.1 | Structural welding code for steel. |
| `Technical Practice` → Welding → `Technical Standard` → ISO 9606 | Qualification testing of welders. |
| `Technical Practice` → Welding → `Technical Standard` → ISO 3834 | Quality requirements for fusion welding. |
| `Technical Practice` → Welding → `Technical Standard` → ASME Section IX | Welding and brazing qualifications for pressure equipment. |
| `Technical Practice` → Welding → `Technical Evaluation` | Grouping: how the practice is judged. |
| `Technical Practice` → Welding → `Technical Evaluation` → `Verification` | Grouping: conformance of the joint to its procedure and acceptance criteria. |
| `Technical Practice` → Welding → `Technical Evaluation` → `Verification` → Procedure Qualification Test | Destructive and nondestructive testing of a test joint to qualify the WPS and the welder. |
| `Technical Practice` → Welding → `Technical Evaluation` → `Validation` | Grouping: fitness of the welded structure in service. |
| `Technical Practice` → Welding → `Technical Evaluation` → `Validation` → Service and Fatigue Performance | The joint's behaviour under the real load spectrum, including fatigue and corrosion. |
| `Technical Practice` → Welding → `Technical Constraint` | Grouping: the bounds the practice works inside. |
| `Technical Practice` → Welding → `Technical Constraint` → Weldability of the Alloy | Composition and section fix what the process can join without cracking. |
| `Technical Practice` → Welding → `Technical Constraint` → Distortion Tolerance | The assembly must finish inside its dimensional tolerance. |
| `Technical Practice` → Welding → `Technical Constraint` → Inspection Access | A joint that cannot be examined cannot be accepted. |

## Processes

| Process | Heat source | Shield | Thickness | Position | Character |
| --- | --- | --- | --- | --- | --- |
| **SMAW (stick)** | Arc from coated electrode | Electrode coating | 2–30 mm | All | Portable, cheap, slow, slag to remove |
| **GMAW (MIG/MAG)** | Arc from continuous wire | Gas | 1–20 mm | All, best flat | Fast, clean, sensitive to draughts |
| **GTAW (TIG)** | Arc from tungsten electrode | Inert gas | 0.5–10 mm | All | Precise, slow, the root-pass standard |
| **SAW** | Arc under granular flux | Flux | 6–100 mm | Flat | Very high deposition, mechanised |
| **FCAW** | Arc from flux-cored wire | Self-shielded or gas | 1–25 mm | All | Field-capable, high deposition |
| **Resistance** | Joule heat at the contact | None | 0.5–5 mm sheet | Flat | Spot and seam, automotive |
| **Laser / EB** | Focused beam | Vacuum or gas | 0.5–30 mm | Flat | Narrow, deep, low distortion, high capital |
| **Friction stir** | Friction and plastic flow | None | 1–50 mm | Flat | Solid state, aluminium, no fume |
| **Oxyfuel** | Fuel-gas flame | Flame envelope | 0.5–10 mm | All | Independent of power, slow, high heat input |

## Joints and Positions

| Joint type | Preparation | Where it is used |
| --- | --- | --- |
| **Butt** | Square, V, U or J groove | Plate and pipe seams carrying load |
| **Tee** | Fillet or full-penetration groove | Stiffeners, brackets, branch connections |
| **Lap** | Fillet | Sheet and thin plate |
| **Corner** | Fillet or groove | Boxes and frames |
| **Edge** | Square or groove | Sheet edges |

> The **position** matters as much as the joint: flat, horizontal, vertical and overhead change how gravity acts on the molten pool, and they are the reason a welder is qualified per process, per position and per thickness.

## The Heat-Affected Zone

> The metal beside the weld is heated without melting, and it passes through the same transformation ranges as a heat treatment — but with a thermal cycle nobody designed. It can harden, lose toughness, grow grains or soften, depending on the alloy and the heat input. That zone is where most weld failures start, and it is why a welding procedure is a metallurgical document as much as a mechanical one.

> **Hydrogen** is the specific hazard of steels: moisture, grease or coating hydrogen enters the arc, diffuses into the hardened zone, and cracks it hours after the weld cools. Preheat lets it escape before the microstructure hardens; low-hydrogen consumables and post-weld heat treatment close the remaining routes.

## Defects and Inspection

| Defect | Cause | Detection |
| --- | --- | --- |
| **Porosity** | Gas trapped in the pool; damp consumables; dirty surface | Radiography, ultrasonic |
| **Lack of fusion** | Low current, fast travel, wrong angle, thick oxide | Ultrasonic, radiography |
| **Incomplete penetration** | Wrong root gap or preparation; low heat input | Radiography, ultrasonic |
| **Undercut** | Excessive current or travel speed | Visual, dimensional |
| **Slag inclusion** | Poor interpass cleaning in flux processes | Radiography |
| **Hydrogen cracking** | Hydrogen plus hard zone plus restraint | Delayed inspection, ultrasonic |
| **Solidification cracking** | Sulphur, phosphorus or wide freezing range | Radiography, visual |
| **Distortion** | Uneven shrinkage, sequence, restraint | Dimensional measurement |

> Inspection is chosen by defect type: radiography for volumetric defects, ultrasonics for planar ones, magnetic and penetrant methods for the surface, and visual for everything the eye can reach. The inspection plan is part of the procedure, not an afterthought.

## What is a critical conceptual evaluation of this technical element instance?

The concept under evaluation is **Welding**, defined above as *the practice that joins metal by fusion or pressure into a continuous metallurgical joint*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: separated from brazing and soldering (no parent-metal melting), adhesive bonding (no metallurgical continuity), and heat treatment (the heat is a means). Definitional Clarity — **pass**: the heat source, the shield, the filler and the procedure are operational. Conceptual Determinacy — **pass with qualification**: the boundary against a solid-state process such as friction stir, which joins without melting, is the *joint's continuity* rather than fusion; the note admits it under the pressure branch. Internal Consistency — **pass**: processes, tasks, equipment, parameters, standards and inspections are distinct branches; the heat-affected zone is a consequence, not a root. Representational Adequacy — **qualified**: complete for the practice and its defects; the structural design, the metallurgy of each alloy and the economics are linked. Purpose Adequacy — **pass**: every leaf serves joint design, procedure, operation or inspection.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Distinguished from brazing, soldering, bonding and heat treatment. |
| Definitional Clarity | pass | Heat source, shield, filler, joint and procedure are operational. |
| Conceptual Determinacy | pass (qualified) | Solid-state joining is admitted by continuity, not fusion; stated. |
| Internal Consistency | pass | Processes, tasks, equipment, parameters, standards and inspections are separate branches; the HAZ is a consequence. |
| Representational Adequacy | qualified | Complete for the practice and its defects; structural design, per-alloy metallurgy and cost are links. |
| Purpose Adequacy | pass | Every leaf serves joint design, procedure, operation or inspection. |

## References

- [Welding](https://en.wikipedia.org/wiki/Welding)
- [Gas metal arc welding](https://en.wikipedia.org/wiki/Gas_metal_arc_welding) · [Gas tungsten arc welding](https://en.wikipedia.org/wiki/Gas_tungsten_arc_welding) · [Shielded metal arc welding](https://en.wikipedia.org/wiki/Shielded_metal_arc_welding)
- [Submerged arc welding](https://en.wikipedia.org/wiki/Submerged_arc_welding) · [Resistance welding](https://en.wikipedia.org/wiki/Resistance_welding)
- [Friction stir welding](https://en.wikipedia.org/wiki/Friction_stir_welding) · [Laser beam welding](https://en.wikipedia.org/wiki/Laser_beam_welding)
- [Heat-affected zone](https://en.wikipedia.org/wiki/Heat-affected_zone) · [Hydrogen embrittlement](https://en.wikipedia.org/wiki/Hydrogen_embrittlement)
- [Steel](/view.html?p=notes/technica/production/industry/steel.md) — the alloy most often welded, and the one whose carbon equivalent governs the procedure
- [Alloy](/view.html?p=notes/technica/general/materiotecnia/alloy.md) — the families and their weldability
- [Heat Treatment](/view.html?p=notes/technica/general/materiotecnia/heat-treatment.md) — the deliberate thermal cycle the HAZ reproduces unintentionally
- [Metals Production](/view.html?p=notes/technica/production/industry/metals-production.md) — the system welding serves
- [Physical Material Technology](/view.html?p=notes/technica/general/physical-material-technology.md) — the joining practice in the wider materials system
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) — the schema and the permitted link forms
- [Technica Atlas](/corpus/notes/technica/atlas.html) — the forest this decomposition feeds
