---
tags: [note, production, material-handling, logistics]
---

# Conveyor System

> A **conveyor system** is mechanical handling equipment that moves material from one location to another without carrying it in a vehicle: a continuous track — belt, rollers, chain, screw, tube or vibrating pan — driven by a power package, loaded at one or more points and discharged at others. It is the object that turns discrete production stations into a line.

> Conveyors are chosen where the load is heavy, bulky, hot, repetitive or continuous enough that carrying it by hand or by lift truck is slower, dearer or more dangerous. The design question is never "what belt" but "what route, at what rate, with what accumulation and what transfer between conveyors".

## Formulation

### What technical element type does this technical instance belong to?

**Conveyor System belongs to the `Production Equipment` technical element type — a `Production Support` that conveys, holds and positions material without transforming the delivered good.**

This is the guide's own ruling: a belt inside a bottling line transforms nothing and produces nothing, so it is equipment, not a producer. The same belt in a parcel depot is a producer, because there the relocation *is* the delivered good — and then it is read as a `Service Good Producer`, or as a `Material Good Producer` when the relocated material is itself what is sold. That promotion is prose, not a second root: this note decomposes the conveyor as equipment.

The test the note applies to every conveyor: does its operation transform reality into the good the plant delivers, or does it only carry another producer's output to the next station?

### What is this technical instance?

> A frame carrying a moving surface — a belt, a roller bed, a chain, a screw flight, a tube of air, a vibrating pan — driven by a gearmotor and kept in line by pulleys, idlers and take-up; loading and discharge points, transfers to other conveyors, accumulation zones, guards and the sensors that report speed, position and jams. It moves cartons, totes, pallets, bulk solids, food, castings, baggage and ore, at rates from a few items a minute to thousands of tonnes an hour.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one conveyor instance, decomposed at shallow depth — the equipment itself, the drive package, the sensing and control layer, and the parameters that fix its duty. The line or plant it serves is a `Production Technical System` decomposed in its own note.
>
> Stopping rule: a row is terminal when it names a concrete part, support or measured variable.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: the drive *actuates* the belt or chain; the frame and idlers *support* it; the sensors *report* its state; the conveyor *conveys* the load.

| Instance Tree Path | Description |
| --- | --- |
| `Production Equipment` → Conveyor System | The continuous track, its drive and its controls, taken as one handling equipment instance. |
| `Production Equipment` → Conveyor System → `Constitutive Technical Object` | Grouping: the parts that constitute the equipment. |
| `Production Equipment` → Conveyor System → `Constitutive Technical Object` → Conveyor Frame | The structure that carries the moving surface and fixes the route, the incline and the transfer heights. |
| `Production Equipment` → Conveyor System → `Constitutive Technical Object` → Belt or Roller Bed | The moving surface: an endless belt, a powered roller bed, a chain, a screw flight or a vibrating pan. |
| `Production Equipment` → Conveyor System → `Constitutive Technical Object` → Idler and Pulley Set | The supports and end pulleys that keep the belt tracking and the load supported between stations. |
| `Production Equipment` → Conveyor System → `Constitutive Technical Object` → Take-Up Assembly | The device that maintains tension as the belt stretches and the chain wears. |
| `Production Equipment` → Conveyor System → `Constitutive Technical Object` → Loading and Discharge Chute | The interfaces where material enters and leaves the track without spillage or damage. |
| `Production Equipment` → Conveyor System → `Machine` | Grouping: the drive package that actuates the equipment. |
| `Production Equipment` → Conveyor System → `Machine` → Gearmotor Drive | Motor and reducer that set the belt or chain speed and supply the traction. |
| `Production Equipment` → Conveyor System → `Machine` → Motorised Drive Roller | A brushless motor inside a roller tube, powering one zone of a roller conveyor. |
| `Production Equipment` → Conveyor System → `Production Instrument` | Grouping: the sensing and control layer. |
| `Production Equipment` → Conveyor System → `Production Instrument` → Speed and Position Sensor | Encoder or proximity sensor reporting belt speed, zone occupancy and load position. |
| `Production Equipment` → Conveyor System → `Production Instrument` → Jam and Pull-Cord Sensor | The safety and fault detection that stops the drive before the load or a person is damaged. |
| `Production Equipment` → Conveyor System → `Technical Parameter` | Grouping: the variables that fix the duty. |
| `Production Equipment` → Conveyor System → `Technical Parameter` → Throughput | Tonnes or items per hour the track carries at its design speed and loading. |
| `Production Equipment` → Conveyor System → `Technical Parameter` → Incline Angle | The maximum rise the surface can carry the load up without sliding or tumbling. |
| `Production Equipment` → Conveyor System → `Technical Parameter` → Load Capacity | The unit load and the accumulated load the frame and drive are sized for. |

### What is a critical conceptual evaluation of this technical element instance?

The concept under evaluation is **Conveyor System**, defined above as *the continuous track, its drive and its controls, taken as one handling equipment instance that conveys material without transforming it*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: the conveyor is separated from the producer it serves, from the vehicle that is a transport object, and from the transfer point that joins two conveyors. Definitional Clarity — **pass**: continuous track, drive, loading and discharge are operational, and the guide's own producer-versus-support test is stated. Definitional Determinacy — **pass with qualification**: the same physical belt is equipment in a bottling line and a producer in a parcel depot; the boundary rule is what the plant sells, and the note states it rather than letting the object's shape decide. Internal Consistency — **pass**: equipment, drive, instruments and parameters are distinct branches; the producer reading appears only as prose. Representational Adequacy — **qualified**: complete for the equipment and its duty; the line-level control, the maintenance organisation and the safety case are linked rather than grown. Purpose Adequacy — **pass**: shaped for selection and maintenance review — the type table, the criteria and the duty parameters are exactly what those decisions need.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Distinguished from the producer it serves, from road and rail vehicles, and from the transfer points between conveyors. |
| Definitional Clarity | pass | Continuous track, drive, loading and discharge defined operationally; the producer/support test is quoted from the guide. |
| Conceptual Determinacy | pass (qualified) | The same belt types differently by what the plant sells; the rule is stated, and the equipment reading is the default root. |
| Internal Consistency | pass | Equipment, drive, instruments and parameters are separate branches; no producer root coexists with the equipment root. |
| Representational Adequacy | qualified | Complete for the object and its duty; line control, maintenance organisation and safety case are links. |
| Purpose Adequacy | pass | Every leaf serves selection, specification or maintenance; the type and criterion tables are the decision surface. |

## Conveyor Types

> The type is chosen by the load — unit or bulk, hot or cold, fragile or abrasive — and by what the route must do: rise, turn, accumulate, sort or meter.

| Type | Moving surface | Typical load | Where it fits |
| --- | --- | --- | --- |
| **Belt Conveyor** | Endless belt on idlers | Bulk solids, cartons, bags | Long hauls, inclines, the default for bulk material. |
| **Roller Conveyor** | Gravity or powered rollers | Cartons, totes, pallets | Distribution centres, accumulation and sortation lines. |
| **Chain Conveyor** | Chain, floor or overhead | Pallets, heavy units, automotive bodies | Assembly lines, paint lines, heavy or hot loads. |
| **Overhead Conveyor** | Chain on an I-beam or enclosed track | Components hung on carriers | Paint finishing, assembly, routes over workstations. |
| **Screw or Auger Conveyor** | Rotating helical flight in a trough | Powders, grains, sludge | Short, enclosed, metered bulk transfer. |
| **Pneumatic Conveyor** | Air stream in pipes or ducts | Powders, pellets, fly ash | Cement, flour, plastic granules; routing around obstacles. |
| **Vibrating Conveyor** | Oscillating trough or pan | Hot, abrasive or fragile bulk | Foundry castings, food-grade lines, screening and cooling. |
| **Vertical Conveyor** | Lifts, forks or parallel belts | Unit loads between levels | Multi-floor plants; not for people. |
| **Spiral Conveyor** | Helical belt or slat chain | Cartons, packaged food | Continuous rise in little floor space; cooling and freezing lines. |
| **Walking Beam** | Reciprocating beam with nests | Heavy, precisely located parts | Press lines and stations where position must be exact. |

## Selection Criteria

| Question | What it fixes |
| --- | --- |
| Unit load or bulk? | Roller, chain and overhead for units; belt, screw, pneumatic and vibrating for bulk. |
| What is the required operation — transport, accumulation, sorting, metering? | The control layer and the number of zones, not just the surface. |
| How heavy and how hot? | Frame, idler and belt material class; chain and overhead where belts fail. |
| What incline and what route? | Belt roughness and cleats, spiral or vertical lift, or a pneumatic detour. |
| Where are the loading and pick-up points? | Chute and transfer design; every transfer is a wear and spillage point. |
| Is static control required? | Conductive or dissipative belt and roller materials. |

## Care and Maintenance

> A conveyor is the line's lifeline, and its failures stop everything downstream. The routine that keeps it running is short and unglamorous: inspect belts, chains and splices; monitor motors and reducers for temperature and noise; keep wear parts in stock; train the operators to report tracking and spillage early; and audit the whole system, not just the failed component.

> Service life is set at design time — the right type, the right route and the right material — and then preserved by maintenance. Most conveyor incidents are not mechanical surprises: they are guards removed, pull-cords bypassed and accumulation zones run past their design load.

## References

- https://en.wikipedia.org/wiki/Conveyor_system
- https://en.wikipedia.org/wiki/Conveyor_belt
- https://en.wikipedia.org/wiki/Roller_conveyor
- https://en.wikipedia.org/wiki/Pneumatic_conveyor
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) — the schema, and the QA ruling on conveyor belts
- [Industrial Machinery](/view.html?p=notes/technica/production/industry/industrial-machinery.md) — the machinery system a conveyor line serves
- [Logistics](/view.html?p=notes/technica/production/industry/logistic/logistics.md) — the wider handling system
- [Technica Atlas](/corpus/notes/technica/atlas.html) — the forest this decomposition feeds
