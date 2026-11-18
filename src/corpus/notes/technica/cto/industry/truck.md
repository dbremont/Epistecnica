---
tags: [note, truck, vehicles, transport, freight]
---

# Truck

> A **truck** is a motor vehicle built to carry goods: a chassis carrying a regulated distribution of load over its axles, a powertrain sized to a duty cycle, and a body or a coupling for the cargo. It is the unit in which freight law and vehicle physics meet, and almost every design decision follows from three numbers that are set outside the engineering.

## Formulation

### What technical element type does this technical instance belong to?

**The truck belongs to the `Production Technical Object` technical element type** — a produced machine, typed as the [radar](/view.html?p=notes/technica/cto/industry/radar.md) and the [laser Doppler vibrometer](/view.html?p=notes/technica/cto/industry/laser-doppler-vibrometer.md) on this shelf are typed.

Its parent is a system: [transportation vehicles](/view.html?p=notes/technica/cto/industry/transportation-vehicles.md) is the `Production Technical System` covering autos, trucks, buses and motorcycles, and the truck is one object inside it. Readable secondarily as a `Machine` where its function is the actuation of transport rather than the artefact itself.

### What is this technical instance?

> A rigid lorry delivering to a shop; a tractor unit pulling a trailer across a continent; a tipper leaving a quarry; a tanker of chemical; a refrigerated box on a supermarket schedule; a light van on the last mile.

Three constraints are set before any engineering starts, and the whole architecture follows:

- **Axle load.** Pavement damage scales roughly with the **fourth power** of the axle mass, which is why axle limits are legal rather than advisory: doubling the load on an axle multiplies the damage by about sixteen. AASHTO's road test measured this in the 1950s and it has governed truck design ever since — the reason heavy vehicles have many axles rather than one strong one.
- **Gross vehicle weight and dimensions.** Payload is what is left after the vehicle's own mass, and length limits decide whether the cargo rides on the chassis (a rigid truck) or in a trailer behind a short tractor.
- **Duty cycle.** Stop-start urban delivery stresses brakes, cooling and the clutch; continuous long haul stresses the powertrain and the driver's regulated hours. The same chassis supports both and almost nothing else is shared.

The design variable is **payload**, and that is where electrification bites. A battery is mass that earns nothing: each kilowatt-hour carried is freight not carried, and whether the trade closes depends entirely on the duty cycle — an urban delivery van returns to base and can afford the mass; a long-haul tractor cannot, which is why the two ends of the market have moved at different speeds.

The modular cut is the other thing to understand. A rigid truck and a tractor-trailer are one architecture in two products: the cab-over tractor exists because length limits count the trailer, and the articulation is what lets a long combination take a corner. That is why the same manufacturer sells a chassis and a cab, and someone else sells the body.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one vehicle, decomposed to its constituents, its kinds, the configuration that decides its legality and its performance, and the evaluations that accept it. The freight system it serves belongs to [logistics](/view.html?p=notes/technica/cto/industry/logistics-system.md); the road it damages belongs to the civil notes.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique and complete from the root; backticked segments name a type, plain segments an instance.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical Object` → Truck | Goods-carrying motor vehicle. |
| `Production Technical Object` → Truck → `Constitutive Technical Object` | Grouping: the assembly. |
| `Production Technical Object` → Truck → `Constitutive Technical Object` → Chassis Frame | The ladder frame that carries the load and the axle reactions. |
| `Production Technical Object` → Truck → `Constitutive Technical Object` → Powertrain | Engine or traction motor, and its rating against the duty cycle. |
| `Production Technical Object` → Truck → `Constitutive Technical Object` → Transmission and Final Drive | Gear steps and axle ratio: the choice that trades gradeability against cruise speed. |
| `Production Technical Object` → Truck → `Constitutive Technical Object` → Axles and Suspension | How the load is distributed and how the road is loaded — the fourth-power constraint made structural. |
| `Production Technical Object` → Truck → `Constitutive Technical Object` → Cab | The driver's workplace, and in a cab-over the front of the vehicle's length. |
| `Production Technical Object` → Truck → `Constitutive Technical Object` → Body or Coupling | Rigid body, tank, tipper or fifth-wheel coupling: the interface to the cargo. |
| `Production Technical Object` → Truck → `Constitutive Technical Object` → Braking System | Service, endurance and auxiliary braking; the system a long descent tests. |
| `Production Technical Object` → Truck → `Constitutive Technical Object` → Electrical and Telematics | Lighting, and the reporting that makes a fleet measurable. |
| `Production Technical Object` → Truck → `Machine` | Grouping: kinds by function. |
| `Production Technical Object` → Truck → `Machine` → Rigid Truck | Chassis and body in one unit: the delivery and tipper form. |
| `Production Technical Object` → Truck → `Machine` → Tractor Unit | A cab and a coupling: exists because length limits count the trailer. |
| `Production Technical Object` → Truck → `Machine` → Articulated Combination | Tractor plus semi-trailer: the long-haul form, and the one that corners. |
| `Production Technical Object` → Truck → `Machine` → Light Commercial Vehicle | Van and light chassis: the last mile, and the class where battery mass closes. |
| `Production Technical Object` → Truck → `Technical Configuration` | Grouping: the numbers that decide legality. |
| `Production Technical Object` → Truck → `Technical Configuration` → Gross Vehicle Weight | The total mass the vehicle may be, set by law and by the axles. |
| `Production Technical Object` → Truck → `Technical Configuration` → Axle Load Distribution | Mass per axle, and therefore the pavement damage and the legal limit. |
| `Production Technical Object` → Truck → `Technical Configuration` → Payload | What is left of the gross weight after the vehicle's own mass: the design variable. |
| `Production Technical Object` → Truck → `Technical Evaluation` | Grouping: what accepts or rejects the design. |
| `Production Technical Object` → Truck → `Technical Evaluation` → Axle-Load Legality | The vehicle must be legal at every axle, not only in total. |
| `Production Technical Object` → Truck → `Technical Evaluation` → Braking Performance | Stopping distance under load, including the fade that a long descent produces. |
| `Production Technical Object` → Truck → `Technical Evaluation` → Emissions and Fuel Cycle | The regulated per-kilometre limit, and the payload penalty any compliance technology carries. |
| `Production Technical Object` → Truck → `Technical Evaluation` → Driver Hours | The operational bound: a legal limit on driving that no design can remove. |

**Limitations.** *Payload–mass coupling* — every kilogram of technology is a kilogram of freight lost, so improvements are always trades. *Duty-cycle dependence* — the same vehicle is efficient in one service and wasteful in another; there is no general optimum. *Regulatory heterogeneity* — axle limits, lengths and emissions differ by jurisdiction, so a truck is designed for a market, not for the world. *Partial observability* — the load actually carried, and its distribution, are rarely measured in service.

## References

- Highway Research Board. (1962). *The AASHO road test: Report 5, pavement research* (Special Report 61E). National Academy of Sciences. — the fourth-power law of axle load against pavement damage, which is the origin of axle limits
- Heisler, H. (2002). *Advanced vehicle technology* (2nd ed.). Butterworth-Heinemann. — chassis, driveline, braking and the load-distribution calculations in one place
- [Truck](https://en.wikipedia.org/wiki/Truck)
- [Transportation Vehicles](/view.html?p=notes/technica/cto/industry/transportation-vehicles.md) — the system this object belongs to
- [Logistics System](/view.html?p=notes/technica/cto/industry/logistics-system.md) — the practice it serves
- [Automobile System](/view.html?p=notes/technica/cto/industry/automobile-system.md) — the passenger-vehicle sibling, and the source of much of the shared technology
- [Product Taxonomy — Trucks](/view.html?p=notes/social/good/product-taxonomy.html) — the goods-side classification this object now appears in
