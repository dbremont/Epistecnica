# Quarry

> A quarry read naturally: an excavated rock mass and its landform — the observer-independent
> furniture (rock body, faces, water, air, colonizing life) that remains when the diesel fleet,
> the firm, and the market price are set aside. The extraction plant is decomposed technically,
> the operating firm socially; this note holds the natural reading. Worked per
> [How to decompose any natural instance?](note.html?n=meta/philosophia-naturalis-et-operis.md).

## Formulation

### What natural element type does this natural instance belong to?

`Natural System` at meso level of organization: a bounded segment of quarried ground with
interacting components (rock faces, floor, groundwater, dust plume, biota), inputs/outputs
(runoff, sediment, propagules), and feedback (slope — drainage — revegetation).

### What is this natural instance?

A **quarry**: an open excavation in bedrock (here the archetype is a limestone **quarry**)
with stepped **bench faces**, a **quarry floor**, exposed **overburden**, an intercepted
**water table**, and the derived **talus** and **dust plume**. The cut includes the rock body,
its landform, water, air, and colonizing organisms at meso scale; it excludes extraction
machinery, the operating organization, and product markets — those are secondary readings
(see below), each with its own tree.

### What is the recursive instance decomposition of this natural instance?

Instances are styled `**bold**`; bare grouping types `` `code` ``; every leaf resolves to a
natural instance; prefixes are valid paths (recursion rule).

| Instance Tree Path | Description | Natural Category | Natural Element Type Tree Path |
| --- | --- | --- | --- |
| **quarry** | The bounded excavated rock mass under study. | System | `(root) := Natural System` |
| **quarry** > **bench face** | Stepped rock wall exposing jointed strata. | Constituent | `(root) := Natural System -> Natural Object` |
| **quarry** > **quarry floor** | Excavation base with ponding and sediment. | Constituent | `(root) := Natural System -> Natural Object` |
| **quarry** > **bench face** > **limestone bed** | Recurring carbonate stratum worked by the faces. | Constituent | `(root) := Natural System -> Natural Object -> Building Block` |
| **quarry** > **bench face** > **limestone bed** > **calcite** | Compositional substance of the bed. | Constituent | `(root) := Natural System -> Natural Object -> Building Block -> Substance` |
| **quarry** > **talus** | Fallen block apron at the face foot. | Constituent | `(root) := Natural System -> Natural Object` |
| **quarry** > **quarry lake** | Groundwater-fed pond on the floor. | Constituent | `(root) := Natural System -> Natural Object` |
| **quarry** > **pioneer vegetation** | Self-maintaining colonizers of floor and benches. | Living | `(root) := Natural System -> Organism` |
| **quarry** > **face spalling** | Gravity-driven detachment of joint-bounded blocks. | Manifestation | `(root) := Natural System -> Natural Process` |
| **quarry** > **face spalling** > **rockfall regime** | Unified explanatory object over spalling events. | Manifestation | `(root) := Natural System -> Natural Process -> Phenomenon` |
| **quarry** > **groundwater inflow** | Seepage through joints into the excavation. | Manifestation | `(root) := Natural System -> Natural Process` |
| **quarry** > **groundwater inflow** > **flooding state** | Snapshot water-level configuration after inflow. | Manifestation | `(root) := Natural System -> Natural Process -> State` |
| **quarry** > **ecological succession** | Ordered recolonization trajectory on worked ground. | Manifestation | `(root) := Natural System -> Natural Process -> Trajectory` |
| **quarry** > `Property` > **joint spacing** | Measurable discontinuity attribute bounding block size. | Quantity | `(root) := Natural System -> Property` |
| **quarry** > `Property` > **slope angle** | Measurable face attribute bounding stability. | Quantity | `(root) := Natural System -> Property` |
| **quarry** > `Constraint` > **shear strength** | Material bound on face stability. | Constraint | `(root) := Natural System -> Natural Constraint` |
| **quarry** > `Constraint` > **flood recurrence interval** | Scale bound on floor inundation. | Constraint | `(root) := Natural System -> Natural Constraint` |

Limitation checklist (ontic properties of the segment, not method failures): Complexity
(coupled hydro-mechanical-ecological), Nonlinearity (failure thresholds), Uncertainty (hidden
joints), Scale (face to catchment), Partial Observability (subsurface), Non-Repeatability
(one excavation history), Many-Body coupling (blocks, water, roots). Chaos, Emergence,
Irreducibility, Measurement Disturbance, Data Availability, and Computational Complexity apply
only where the concrete site shows them — record per instance, do not assume.

Secondary readings (kept as prose, never merged into the tree above): readable as technique —
drill-blast-crush-screen and dewatering methods (decompose under the technicarum grammar);
readable as production facility — the quarry as operated site with products (aggregates,
limestone) and firm (decompose under the socialium grammar; if it plays a production role it
is a Social node tagged `production-view`). The instrument technically, the formation
naturally (`guideline/ambiguity_resolution.md`).

## References

- [Philosophia Naturalis et Operis](note.html?n=meta/philosophia-naturalis-et-operis.md) (workflow, schemas, Limitation checklist)
- [Philosophia Artium Epistemicarum et Operis](note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md) (presupposed definitions)
- Ambiguity Resolution (`guideline/ambiguity_resolution.md`) (multi-root forest rule)
