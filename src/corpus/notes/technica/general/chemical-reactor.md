---
tags: [note, production, chemical-engineering, process-engineering]
---

# Chemical Reactor

> A **chemical reactor** is an enclosed volume in which a chemical reaction is carried out — the process vessel that turns a reaction into a unit operation. Reaction engineering is the discipline that sizes it: conversion, selectivity and heat duty follow from the vessel's mixing, its residence-time distribution and its heat-transfer surface, not from the recipe alone.

> Its design problem is economic, stated in physical terms: drive the reaction toward the desired product at the highest yield, with the least capital and the least energy bought in or thrown away. Every reactor decision — batch or continuous, stirred or tubular, jacketed or adiabatic — commits the plant to which of those terms it will pay.

## Formulation

### What technical element type does this technical instance belong to?

**Chemical Reactor belongs to the `Production Technical Object` technical element type, with kind `Material Good Producer` — the physical object in which matter is transformed into the delivered good.**

It is a producer because the transformation happens inside it: feedstock crosses the boundary, leaves as product, and the reaction is the plant's operation. The shell, the jacket and the agitator are its `Constitutive Technical Object`s, and its instruments and relief equipment are `Production Support`s.

It is readable as `Production Equipment` when the reaction is incidental — a holding tank where a slow hydrolysis proceeds while the tank mainly stores — because then the vessel holds another producer's material and transforms nothing the plant sells. That reading is prose, not a second root: this note decomposes the reactor as the site of the transformation.

### What is this technical instance?

> A stirred tank or a tube, with the surfaces and internals that fix its mixing and its heat duty: a pressure shell, a jacket, half-coil or internal exchanger, an impeller or a packed bed, feed and product nozzles, a relief device and the probes that hold the operating point. It runs a batch, semibatch or continuous regime, catalytic or homogeneous, and delivers an intermediate or a finished chemical — ammonia, sulfuric acid, a polymer, an active pharmaceutical ingredient.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one reactor instance, decomposed at shallow depth — the vessel and its parts, the supports it relies on, and the parameters that fix its operating point. The train or plant it sits in is a `Production Technical System` decomposed in its own note.
>
> Stopping rule: a row is terminal when it names a concrete part, instrument, support or measured variable.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a jacket or a coil *removes* heat; an impeller *mixes*; a relief device *protects*; the reactor *produces* the converted material.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical Object` → Chemical Reactor | The enclosed reaction volume and everything that fixes its operating point. |
| `Production Technical Object` → Chemical Reactor → `Constitutive Technical Object` | Grouping: the parts that constitute the reactor. |
| `Production Technical Object` → Chemical Reactor → `Constitutive Technical Object` → Vessel Shell | The pressure boundary that contains the reacting mixture at its temperature and pressure. |
| `Production Technical Object` → Chemical Reactor → `Constitutive Technical Object` → Heat-Transfer Surface | Jacket, half-coil, internal coil or tube bundle: the area that adds or removes the heat of reaction. |
| `Production Technical Object` → Chemical Reactor → `Constitutive Technical Object` → Agitator Assembly | Shaft, impeller and baffles that fix the mixing time and the homogeneity of the contents. |
| `Production Technical Object` → Chemical Reactor → `Constitutive Technical Object` → Reactor Internals | Packing, trays, catalyst bed, membrane or static mixer: what the flow crosses inside the vessel. |
| `Production Technical Object` → Chemical Reactor → `Constitutive Technical Object` → Nozzle and Manway Set | The openings for feed, product, sampling, cleaning and inspection. |
| `Production Technical Object` → Chemical Reactor → `Production Support` | Grouping: the supports the reactor relies on to run. |
| `Production Technical Object` → Chemical Reactor → `Production Support` → `Production Instrument` | Grouping: the measurement layer that holds the operating point. |
| `Production Technical Object` → Chemical Reactor → `Production Support` → `Production Instrument` → Temperature Probe | Thermocouple or resistance probe reading the reaction temperature. |
| `Production Technical Object` → Chemical Reactor → `Production Support` → `Production Instrument` → Pressure Transmitter | Signal that keeps the shell inside its design pressure. |
| `Production Technical Object` → Chemical Reactor → `Production Support` → `Production Instrument` → Level and Flow Meter | Feed, product and inventory measurement for the mass balance. |
| `Production Technical Object` → Chemical Reactor → `Production Support` → `Production Equipment` | Grouping: the containment and transfer layer around the vessel. |
| `Production Technical Object` → Chemical Reactor → `Production Support` → `Production Equipment` → Pressure-Relief Assembly | Relief valve, rupture disc and vent: the last barrier against overpressure. |
| `Production Technical Object` → Chemical Reactor → `Production Support` → `Production Equipment` → Feed and Product Piping | Lines and valves that carry material in and out at the specified rates. |
| `Production Technical Object` → Chemical Reactor → `Technical Parameter` | Grouping: the variables that fix the operating point. |
| `Production Technical Object` → Chemical Reactor → `Technical Parameter` → Residence Time | Space time — volume divided by volumetric flow — the contact time the conversion is bought with. |
| `Production Technical Object` → Chemical Reactor → `Technical Parameter` → Operating Temperature and Pressure | The window the shell, the reaction and the selectivity allow. |
| `Production Technical Object` → Chemical Reactor → `Technical Parameter` → Conversion and Selectivity | Fraction of limiting reactant converted, and fraction of that conversion that reaches the desired product. |

### What is a critical conceptual evaluation of this technical element instance?

The concept under evaluation is **Chemical Reactor**, defined above as *the enclosed volume in which a chemical reaction is carried out, together with the surfaces, internals and instruments that fix its operating point*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: the reactor is separated from the train it belongs to (a `Production Technical System`), from the separation equipment that follows it, and from the storage vessel that merely holds its product. Definitional Clarity — **pass**: the defining terms — enclosed volume, reaction, residence time, conversion — are operational and measurable. Conceptual Determinacy — **pass with qualification**: the boundary against a plain tank is whether a reaction the plant relies on occurs inside, and that rule admits borderline holding vessels where a slow reaction proceeds; the note states the rule and records the reading rather than hiding it. Internal Consistency — **pass**: the vessel, the supports and the parameters are distinct branches, and no row mixes the reactor with the plant. Representational Adequacy — **qualified**: complete for the vessel and its operating window; the reaction kinetics, the control system and the plant-level integration are linked rather than grown. Purpose Adequacy — **pass**: shaped for design review — every leaf is a part, a support, a parameter or a selection criterion.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Distinguished from the reactor train, the downstream separation and the storage tank; typed as a production technical object, readable as equipment. |
| Definitional Clarity | pass | The definition names the operation (enclosed reaction volume) and the design variables (mixing, residence time, heat duty) in measurable terms. |
| Conceptual Determinacy | pass (qualified) | The rule against a plain tank is the reliance on an in-vessel reaction; slow holding reactions make the boundary a judgement, stated rather than assumed. |
| Internal Consistency | pass | Vessel, supports and parameters are separate branches; the producer and equipment readings do not coexist as roots. |
| Representational Adequacy | qualified | Complete for the object and its operating point; kinetics, control and plant integration are links, not branches. |
| Purpose Adequacy | pass | Every leaf serves specification, operation or selection; the type table and the rules are the design-review surface. |

## Reactor Types

> Two geometries underlie every type: the tank, where the contents mix in the whole volume, and the tube, where they travel without axial mixing. Both run batch or continuous, and real reactors are combinations of the ideal models.

| Type | Regime | Mixing | Characteristic use |
| --- | --- | --- | --- |
| **Batch Reactor** | Transient: charge, react, discharge | Tank, stirred | Small-volume and biological production — brewing, pulping, enzymes; every variable drifts with time. |
| **Semibatch Reactor** | One reactant charged, the other fed | Tank, stirred | Reactions controlled by slow addition (to suppress side reactions) or by continuous removal of a gas or precipitate. |
| **CSTR** | Continuous, steady state | Tank, stirred, assumed homogeneous | Effluent leaves at the reactor concentration, so the reaction runs at its slowest rate; several in series approach plug flow. |
| **PFR / Continuous Tubular Reactor** | Continuous, steady state | None axially; gradient along the tube | Highest conversion per volume for a simple reaction; reagents may be fed at intermediate points. |
| **Packed-Bed Reactor** | Continuous through a fixed catalyst | Tube filled with catalyst pellets | Heterogeneous catalysis where the solid stays in place. |
| **Fluidised-Bed Reactor** | Continuous through a suspended catalyst | Particles fluidised by the upflow | Catalyst that must be moved, regenerated or kept at uniform temperature. |
| **Loop Reactor** | Continuous, recirculating | Tubular loop, behaves like a CSTR | High recirculation for heat removal and mixing, with a tubular geometry. |
| **Membrane Reactor** | Continuous with in-situ separation | Tube or tank plus membrane | Product removed as it forms, pushing an equilibrium-limited reaction past its equilibrium. |
| **Photochemical Reactor** | Continuous or batch | Transparent vessel with a light source | Reactions driven by photons, where the light path is the design variable. |
| **Electrochemical Reactor** | Continuous or batch | Cell with electrodes and separator | Reactions driven by electrode potential rather than by heat or catalyst. |

> A **bioreactor** is the same object family read under the living-agent grammar: a stirred, sparged, jacketed vessel holding cells rather than a chemical catalyst. It is decomposed in the biotechnology notes and typed as a `Production Technical Object` there; the vessel engineering is shared, the kinetics are not.

## Heat Management

> Every reaction is exothermic or endothermic, and the reactor is the object that must carry the heat away or bring it in without losing control of the temperature.

| Duty | Means | Consequence for the design |
| --- | --- | --- |
| **Moderate exothermic** | Jacket, half-coil or internal coil on a tank | Heat-transfer area sets the achievable production rate; mixing must keep the bulk at the probe's temperature. |
| **Strongly exothermic** | Tubular reactor built like a heat exchanger | Small diameter, high area per volume, short residence time; the risk is a hot spot, not a bulk runaway. |
| **Strongly endothermic** | Furnace-fired or internally heated tubular reactor | The tube wall becomes the limiting material; heat flux and coking set the campaign length. |
| **Adiabatic** | No exchange surface | The temperature rise is the reaction's own; acceptable only when the adiabatic temperature is inside the catalyst's and the selectivity's window. |
| **Latent duty** | Boiling or condensing internals | The phase change pins the temperature, which is either the control strategy or the instability. |

## Mixing and Residence-Time Distribution

> The ideal models are assumptions about mixing, and the design is only as good as the assumption.

- **Perfect mixing** (CSTR) holds when the residence time is roughly five to ten times the mixing time; below that the vessel has dead zones and bypasses, and the model overstates conversion.
- **Plug flow** (PFR) holds when radial diffusion erases the velocity profile; under laminar flow the centre travels faster than the wall, and oscillatory baffles or static mixers are used to restore the assumption.
- **Dispersion** is the honest middle: the axial dispersion model carries one parameter, the Péclet number, and interpolation between the two ideals.
- **Accumulation** is not a footnote: a plant that runs a CSTR near its steady state still starts, stops and cleans in transients where the mass and energy balances are differential, and those transients are where most incidents happen.

## Selection Rules

| Question | Favours |
| --- | --- |
| Is production small, seasonal or biological? | Batch or semibatch. |
| Is the reaction simple, fast and heat-moderate? | PFR for conversion per volume; CSTR where solids, fouling or catalyst replacement demand access. |
| Is a solid catalyst involved? | Packed bed if it stays active; fluidised bed if it must be regenerated or replaced continuously. |
| Is the reaction equilibrium-limited? | Membrane or reactive distillation, removing a product in situ. |
| Is the heat release large per unit volume? | Tubular exchanger-type reactor, or a CSTR with a large recirculation loop. |
| Is the chemistry photon- or electron-driven? | Photochemical or electrochemical cell, where the light path or the electrode area is the scale-up variable. |

## References

- https://en.wikipedia.org/wiki/Chemical_reactor
- https://en.wikipedia.org/wiki/Batch_reactor
- https://en.wikipedia.org/wiki/Continuous_stirred-tank_reactor
- https://en.wikipedia.org/wiki/Plug_flow_reactor_model
- https://en.wikipedia.org/wiki/Fluidized_bed_reactor
- [Basic Chemicals Production](/view.html?p=notes/technica/production/industry/chemical-basics.md) — the system a reactor train serves
- [Bioreactor reading](/view.html?p=notes/technica/production/industry/biotech-production-ecosystem.md) — the same vessel holding cells
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) — the schema and the permitted link forms
- [Technica Atlas](/corpus/notes/technica/atlas.html) — the forest this decomposition feeds
