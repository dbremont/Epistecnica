---
tags: [note, materials-science, metallurgy, heat-treatment, production]
---

# Heat Treatment

> **Heat treatment** is the controlled heating and cooling of a metal to change its internal structure, and with it its hardness, strength, toughness, machinability or surface chemistry — without changing its shape or its composition. It is the technique that makes a steel a spring, a gear or a bearing rather than a bar.

> The lever is the phase transformation. Heat the metal until a new phase forms, hold it there until the structure is uniform, then cool it at a rate chosen to decide what the new phase becomes. The furnace sets the first two; the quenchant sets the third; and the whole practice is the control of that rate.

## Formulation

### What technical element type does this technical instance belong to?

**Heat treatment belongs to the `Technical Practice` technical element type — a repeatable, organized pattern of technical work integrating tasks, techniques, objects, instruments, parameters and evaluations.**

It is a practice because it is a standing way of working — select the cycle, austenitise, hold, quench, temper, verify — not a single operation or a single furnace. It is readable as a `Technical Element Set` because with the practice come the furnaces, the quenchants, the atmosphere control, the test coupons and the standards.

The boundary against **welding** is the heat-affected zone: welding heats metal as a consequence of joining, while heat treatment heats it deliberately to change it. The boundary against **alloying** is that heat treatment changes no composition — it rearranges what is already there.

### What is this technical instance?

> A cycle, run on a furnace: raise the workpiece to an austenitising, solution or stress-relief temperature; hold it long enough for the structure to become uniform; cool it in a medium and at a rate chosen to produce martensite, bainite, pearlite or a precipitate; then temper, age or stress-relieve to trade some hardness for toughness. The outputs are a specified microstructure, a measured hardness and a case depth where relevant; the warrant is the coupon and the hardness test.

### What is the recursive instance decomposition of this technical instance?

> Boundary: the practice as a set of cycles, techniques, equipment, parameters and checks. The part being treated, the alloy it is made of and the furnace builder's own practice are separate elements.
>
> Stopping rule: a row is terminal when it names a cycle, a technique, an item of equipment, a measured parameter or an evaluation.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.
>
> Verbs: the furnace *heats*; the quenchant *cools*; the cycle *fixes* the microstructure; the coupon *verifies* the result.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Practice` → Heat Treatment | The controlled heating and cooling of metal to fix its structure and properties. |
| `Technical Practice` → Heat Treatment → `Technical Purpose` | Grouping: the purposes the practice is constituted to serve. |
| `Technical Practice` → Heat Treatment → `Technical Purpose` → Harden | Form martensite or a hard precipitate and raise resistance to wear and deformation. |
| `Technical Practice` → Heat Treatment → `Technical Purpose` → Soften | Anneal to relieve stress, spheroidise carbides and restore machinability. |
| `Technical Practice` → Heat Treatment → `Technical Purpose` → Toughen | Temper or age to trade hardness for the toughness the service demands. |
| `Technical Practice` → Heat Treatment → `Technical Purpose` → Refine the Surface | Carburise, nitride or induction-harden a case while leaving the core tough. |
| `Technical Practice` → Heat Treatment → `Technical Problem` | Grouping: the discrepancies between the specified and the achieved result. |
| `Technical Practice` → Heat Treatment → `Technical Problem` → Distortion | Uneven heating or cooling changes the shape and forces rework. |
| `Technical Practice` → Heat Treatment → `Technical Problem` → Quench Cracking | Thermal and transformation stresses exceed the metal's strength during cooling. |
| `Technical Practice` → Heat Treatment → `Technical Problem` → Insufficient Hardenability | The alloy cannot form martensite at the section size and cooling rate available. |
| `Technical Practice` → Heat Treatment → `Technical Problem` → Decarburisation | The surface loses carbon to the furnace atmosphere and softens. |
| `Technical Practice` → Heat Treatment → `Technical Problem` → Retained Austenite | Austenite survives the quench and later transforms unpredictably. |
| `Technical Practice` → Heat Treatment → `Technical Task` | Grouping: the tasks the practice runs. |
| `Technical Practice` → Heat Treatment → `Technical Task` → Select the Cycle | Choose temperatures, holds and cooling rates for the alloy and the required properties. |
| `Technical Practice` → Heat Treatment → `Technical Task` → Austenitise or Solution-Treat | Raise the part into the single-phase field so the structure can be reset. |
| `Technical Practice` → Heat Treatment → `Technical Task` → Hold | Keep the part at temperature until the structure is uniform through the section. |
| `Technical Practice` → Heat Treatment → `Technical Task` → Quench | Cool at the rate the transformation requires, in the chosen medium. |
| `Technical Practice` → Heat Treatment → `Technical Task` → Temper or Age | Reheat to the temperature that yields the specified hardness and toughness. |
| `Technical Practice` → Heat Treatment → `Technical Task` → Verify | Test hardness, case depth and microstructure against the specification. |
| `Technical Practice` → Heat Treatment → `General Technique` | Grouping: the cycles the practice runs. |
| `Technical Practice` → Heat Treatment → `General Technique` → Annealing | Heat and cool slowly to soften, relieve stress and homogenise. |
| `Technical Practice` → Heat Treatment → `General Technique` → Normalising | Cool in air from above the critical temperature to refine the grain. |
| `Technical Practice` → Heat Treatment → `General Technique` → Hardening and Quenching | Austenitise and cool fast enough to form martensite. |
| `Technical Practice` → Heat Treatment → `General Technique` → Tempering | Reheat martensite to the hardness–toughness point the service needs. |
| `Technical Practice` → Heat Treatment → `General Technique` → Case Hardening | Carburise, carbonitride or nitride the surface and harden the case only. |
| `Technical Practice` → Heat Treatment → `General Technique` → Precipitation Hardening | Solution-treat, quench and age to precipitate a strengthening phase. |
| `Technical Practice` → Heat Treatment → `General Technique` → Induction and Flame Hardening | Heat only the surface layer, then quench it in place. |
| `Technical Practice` → Heat Treatment → `Constitutive Technique` | Grouping: the techniques embodied in the cycle. |
| `Technical Practice` → Heat Treatment → `Constitutive Technique` → Transformation-Diagram Selection | Read the TTT or CCT diagram to choose a cooling path that misses the wrong phases. |
| `Technical Practice` → Heat Treatment → `Constitutive Technique` → Quenchant Selection | Match the cooling curve to the section and the hardenability — water, oil, polymer, air, salt. |
| `Technical Practice` → Heat Treatment → `Constitutive Technique` → Atmosphere Control | Fix carbon potential and oxygen to prevent decarburisation or scaling. |
| `Technical Practice` → Heat Treatment → `Constitutive Technical Object` | Grouping: the equipment the practice runs on. |
| `Technical Practice` → Heat Treatment → `Constitutive Technical Object` → Heat-Treatment Furnace | Batch or continuous furnace with controlled temperature and atmosphere. |
| `Technical Practice` → Heat Treatment → `Constitutive Technical Object` → Quench Tank | The bath and agitation that set the cooling rate. |
| `Technical Practice` → Heat Treatment → `Constitutive Technical Object` → Fixture and Jig | Supports that hold the part against distortion during heating and quenching. |
| `Technical Practice` → Heat Treatment → `Constitutive Technical Object` → Test Coupon | A representative piece treated with the load and tested for hardness and case depth. |
| `Technical Practice` → Heat Treatment → `Production Instrument` | Grouping: the measurement that makes the cycle verifiable. |
| `Technical Practice` → Heat Treatment → `Production Instrument` → Thermocouple and Pyrometer | Temperature measurement at the furnace and at the part. |
| `Technical Practice` → Heat Treatment → `Production Instrument` → Hardness Tester | Rockwell, Brinell or Vickers measurement of the result. |
| `Technical Practice` → Heat Treatment → `Production Instrument` → Dilatometer | Length change with temperature, used to locate transformation temperatures. |
| `Technical Practice` → Heat Treatment → `Technical Parameter` | Grouping: the variables that fix the cycle. |
| `Technical Practice` → Heat Treatment → `Technical Parameter` → Austenitising Temperature | The temperature at which the structure becomes austenite or the solution single-phase. |
| `Technical Practice` → Heat Treatment → `Technical Parameter` → Holding Time | Time at temperature, scaled to section thickness and furnace load. |
| `Technical Practice` → Heat Treatment → `Technical Parameter` → Cooling Rate | The rate that decides which transformation products form. |
| `Technical Practice` → Heat Treatment → `Technical Parameter` → Tempering Temperature | The reheat that fixes the final hardness and toughness. |
| `Technical Practice` → Heat Treatment → `Technical Parameter` → Case Depth | The depth of the hardened or alloyed surface layer. |
| `Technical Practice` → Heat Treatment → `Technical Parameter` → Hardness | The measured resistance to indentation, and the acceptance number. |
| `Technical Practice` → Heat Treatment → `Technical Standard` | Grouping: the norms the practice answers to. |
| `Technical Practice` → Heat Treatment → `Technical Standard` → AMS 2750 | Aerospace furnace and pyrometry requirements, including uniformity surveys. |
| `Technical Practice` → Heat Treatment → `Technical Standard` → ASTM E18 | Rockwell hardness testing. |
| `Technical Practice` → Heat Treatment → `Technical Standard` → ISO 4885 | Heat-treatment terminology and classification. |
| `Technical Practice` → Heat Treatment → `Technical Evaluation` | Grouping: how the practice is judged. |
| `Technical Practice` → Heat Treatment → `Technical Evaluation` → `Verification` | Grouping: conformance of the treated part to its specification. |
| `Technical Practice` → Heat Treatment → `Technical Evaluation` → `Verification` → Hardness and Case-Depth Test | Coupon and part hardness, case depth and microstructure against the drawing. |
| `Technical Practice` → Heat Treatment → `Technical Evaluation` → `Validation` | Grouping: fitness of the treated part in service. |
| `Technical Practice` → Heat Treatment → `Technical Evaluation` → `Validation` → Service Performance | Fatigue, wear and fracture behaviour of the treated part under its real duty. |
| `Technical Practice` → Heat Treatment → `Technical Constraint` | Grouping: the bounds the practice works inside. |
| `Technical Practice` → Heat Treatment → `Technical Constraint` → Hardenability of the Alloy | The alloy and the section size limit what the quench can achieve. |
| `Technical Practice` → Heat Treatment → `Technical Constraint` → Distortion Tolerance | The part must survive the cycle inside its geometric tolerance. |
| `Technical Practice` → Heat Treatment → `Technical Constraint` → Furnace Capacity and Energy | Batch size, cycle time and energy set the cost of the treatment. |

## The Cycles

| Cycle | Heating | Cooling | What it produces | Typical use |
| --- | --- | --- | --- | --- |
| **Annealing** | Above the critical temperature, or below it for process annealing | Very slow, in the furnace | Soft, stress-free, coarse or spheroidised structure | Machining stock, cold-worked parts |
| **Normalising** | Above the critical temperature | In still air | Fine, uniform grain; moderate strength | Forging stock, structure refinement before hardening |
| **Hardening** | Austenitising temperature | Fast quench — water, oil, polymer, salt | Martensite, maximum hardness | Cutting tools, gears, wear surfaces |
| **Tempering** | Below the critical temperature, after hardening | Air or furnace | Tempered martensite — hardness traded for toughness | Every hardened part that must not be brittle |
| **Case hardening** | Carburising or nitriding atmosphere | Quench, or slow cool for nitriding | A hard, carbon- or nitrogen-rich surface over a tough core | Gears, shafts, cams |
| **Precipitation hardening** | Solution treatment, quench, then age | Quench, then hold at ageing temperature | Fine precipitates that strengthen without a martensitic quench | Aluminium and nickel alloys, maraging steels |
| **Stress relief** | Below the transformation range | Slow | Residual stresses reduced without changing structure | Weldments, machined parts, castings |

## The Transformation

> Steel is the clearest case. Above about 727 °C (the eutectoid temperature, higher with carbon) the structure is **austenite**, a face-centred cubic phase that dissolves carbon. Cooling slowly lets carbon diffuse out and the steel becomes **ferrite and pearlite** — soft. Cooling faster produces **bainite**, then **martensite**, a body-centred tetragonal phase formed without diffusion, hard and brittle, and therefore always tempered.

> The **TTT diagram** plots when each transformation starts and finishes at a given temperature; the **CCT diagram** does the same for continuous cooling. Both are maps of cooling paths: the cycle is chosen so the path avoids the phases that must not form and reaches the ones that must. That is the entire technique — everything else is equipment.

## Quenching and Its Discontents

| Medium | Cooling rate | Where it is used | Cost |
| --- | --- | --- | --- |
| **Water** | Very fast | Simple carbon steels, large sections | Highest distortion and cracking risk |
| **Polymer solution** | Fast, adjustable by concentration | Alloy steels, distortion-sensitive parts | Concentration control |
| **Oil** | Moderate | Most alloy steels | Fire and fume; still distorts |
| **Molten salt or metal** | Fast at high temperature, slow below | Martempering and austempering | Equipment and safety |
| **Air or gas** | Slow | Lean alloys, vacuum furnaces | Needs high hardenability |

> The three failures of a quench are all stress: **distortion** from uneven cooling, **cracking** from the volume change when austenite becomes martensite, and **soft spots** from a cooling rate below the critical one. The first two are controlled by fixture, agitation and medium; the third by alloy choice — and the alloy choice is made at design time, which is why heat treatment and alloy selection are the same conversation.

## What is a critical conceptual evaluation of this technical element instance?

The concept under evaluation is **Heat Treatment**, defined above as *the controlled heating and cooling of a metal to change its structure and properties without changing its composition or shape*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: separated from alloying (no composition change), welding (heat is a consequence, not the purpose) and machining (shape change). Definitional Clarity — **pass**: the cycle's four variables — temperature, hold, cooling rate, reheat — are operational and measurable. Conceptual Determinacy — **pass with qualification**: the boundary against a thermal process that incidentally changes structure, such as welding's heat-affected zone, is one of intent; the note names it. Internal Consistency — **pass**: purposes, problems, tasks, cycles, equipment, parameters, standards and evaluations are distinct branches. Representational Adequacy — **qualified**: complete for the practice; alloy design, furnace manufacture and the metallurgy of each alloy family are linked. Purpose Adequacy — **pass**: every leaf serves cycle specification, operation or verification.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Distinguished from alloying, welding and machining by what it changes and why. |
| Definitional Clarity | pass | Temperature, hold, cooling rate and reheat are operational. |
| Conceptual Determinacy | pass (qualified) | The boundary against incidental heating (HAZ) is intent; stated. |
| Internal Consistency | pass | Purposes, problems, tasks, cycles, equipment, parameters, standards and evaluations are separate branches. |
| Representational Adequacy | qualified | Complete for the practice; alloy design and per-alloy metallurgy are links. |
| Purpose Adequacy | pass | Every leaf serves cycle specification, operation or verification. |

## References

- [Heat treating](https://en.wikipedia.org/wiki/Heat_treating)
- [Annealing](https://en.wikipedia.org/wiki/Annealing_(metallurgy)) · [Quenching](https://en.wikipedia.org/wiki/Quenching) · [Tempering](https://en.wikipedia.org/wiki/Tempering_(metallurgy))
- [Case hardening](https://en.wikipedia.org/wiki/Case_hardening) · [Carburizing](https://en.wikipedia.org/wiki/Carburizing) · [Nitriding](https://en.wikipedia.org/wiki/Nitriding)
- [Precipitation hardening](https://en.wikipedia.org/wiki/Precipitation_hardening)
- [Steel](/view.html?p=notes/technica/production/industry/steel.md) — the alloy whose transformation the practice exploits
- [Alloy](/view.html?p=notes/technica/general/materiotecnia/alloy.md) — the families and the property trade
- [Tooling](/view.html?p=notes/technica/general/materiotecnia/tooling.md) — the tool steels the cycles are written for
- [Welding](/view.html?p=notes/technica/general/welding.md) — the joining practice that creates its own heat-affected zone
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) — the schema and the permitted link forms
- [Technica Atlas](/corpus/notes/technica/atlas.html) — the forest this decomposition feeds
