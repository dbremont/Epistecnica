# Physical Material Technology

> Physical Material Technology is the engineering of non-living physical materials — metals, ceramics, glasses, polymers, composites, and semiconductors — through transformation, processing, characterization, and utilization into specified forms.

> It is the complement of an observation: materials science states how matter behaves under load, heat, and environment, while material technology intervenes in it — melting, casting, forging, machining, coating, joining, and qualifying it from raw charge to finished part.

> This note treats physical material technology as a full ensemble — the technical domain plus its material families, furnaces, mills, machine tools, test labs, practices, standards, and institutions — following the schema in [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md).

## Formulation

### What technical element type does this technical instance belong to?

**Physical Material Technology belongs to the `Technical Domain` technical element type — readable as a `Technical Element Set`.**

More specifically:

```text
Technical Element Set
└── Physical Material Technology (specified-material ensemble)
    └── Physical Material Technical Domain (bounded field: transform, process, characterize, utilize)
```

Physical Material Technology is a domain because it is a bounded field of technical reality defined by problems (defects, property shortfalls, degradation, dimensional nonconformance), purposes (load-bearing, conduction, containment, function in service), phenomena (phase change, plastic deformation, diffusion, fracture, corrosion), and intervention targets (melts, billets, powders, parts, coatings). It is itself a set: mills, foundries, machine shops, test labs, standards bodies, and material libraries grouped under one umbrella. A mill, furnace, or machine tool *implements* the process standard; a qualified part or heat *realizes* it. As a coherent body of domain + objects + systems + techniques + agents + institutions organized around one capability — specified material in specified form — it can also be read as a `Technical Element Set`.

### What is this technical instance?

> Physical Material Technology is a specified-material ensemble instance: metallurgists, machinists, and inspectors operating furnaces, mills, machine tools, and test labs through melting, forming, machining, joining, and characterization techniques, under defect, property, degradation, and tolerance constraints, to move raw charge from melt or monomer to qualified part.

Lineage: bronze and iron smelting → Bessemer and open-hearth steel → Hall-Héroult aluminum → Bakelite and engineering polymers → Czochralski silicon → composites and superalloys → additive manufacturing and computational alloy design.

### What is the recursive instance decomposition of this technical instance?

> Boundary: this table decomposes one physical-material ensemble instance (domain, material families, furnaces, mills, machine tools, test labs, practices, agents, control, lifecycle); deployment-specific values and named grades or vendors appear only in rows marked exemplar. Excluded by boundary: ore-extraction and mining internals upstream, finished-product design internals downstream.
>
> Stopping rule: a row is terminal when it names a concrete alloy or grade, machine, instrument, file, config attribute, measured value, or named actor.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a mill, furnace, or machine tool *implements* the process standard; a qualified part or heat *realizes* it.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element Set` → Physical Material Technology | Specified-material ensemble: domain, material families, furnaces, mills, machine tools, test labs, practices, and governance. |
| `Technical Element Set` → Physical Material Technology → `Technical Principle` | Grouping: Technical Principle elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Principle` → Membership criterion | Rule distinguishing members from non-members: all elements required to move raw charge from melt or monomer to qualified part. |
| `Technical Element Set` → Physical Material Technology → `Technical Principle` → Membership criterion → `Technical Specification` | Grouping: Technical Specification elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Principle` → Membership criterion → `Technical Specification` → Class-membership condition | Member handles a material class within scope: metallic, ceramic, polymeric, composite, or semiconducting. |
| `Technical Element Set` → Physical Material Technology → `Technical Principle` → Membership criterion → `Technical Specification` → Stage-membership condition | Member sits on the chain: transformation, processing, characterization, or utilization. |
| `Technical Element Set` → Physical Material Technology → `Technical Element Set` | Grouping: Technical Element Set elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Element Set` → Physical Material Technical Domain | Bounded field: transforming, processing, characterizing, and utilizing non-living materials under defect, property, and tolerance bounds. |
| `Technical Element Set` → Physical Material Technology → `Technical Capability` | Grouping: Technical Capability elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Capability` → Realized capability | Capability realized: specified material in specified form, qualified for service. |
| `Technical Element Set` → Physical Material Technology → `Technical Capability` → Shaping capability | Value realized: raw charge brought to net-shape geometry. |
| `Technical Element Set` → Physical Material Technology → `Technical Capability` → Strengthening capability | Value realized: microstructure tuned to specified mechanical properties. |
| `Technical Element Set` → Physical Material Technology → `Technical Capability` → Joining capability | Value realized: separate pieces united into load-bearing assemblies. |
| `Technical Element Set` → Physical Material Technology → `Technical Capability` → Qualification capability | Value realized: demonstrated conformance of a heat or lot to specification. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` | Grouping: Technical Problem elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem | The overall problematique: the gap between as-processed material states and specified service-ready states across classes and forms. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` | Grouping: Technical Problem elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Defectivity Problem | Discrepancy between current and desired freedom from porosity, inclusions, and cracks. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Defectivity Problem → `Technical Requirement` | Grouping: Technical Requirement elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Defectivity Problem → `Technical Requirement` → Inclusion-rating requirement | Formalized cleanliness objective per product form (exemplar per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Defectivity Problem → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Defectivity Problem → `Technical Parameter` → Porosity ceiling | Maximum tolerable void fraction in cast or printed stock (exemplar value per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Property-shortfall Problem | Discrepancy between current and desired strength, toughness, and hardness. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Property-shortfall Problem → `Technical Requirement` | Grouping: Technical Requirement elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Property-shortfall Problem → `Technical Requirement` → Tensile-strength requirement | Formalized minimum strength objective per grade and temper (exemplar per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Property-shortfall Problem → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Property-shortfall Problem → `Technical Parameter` → Toughness floor | Minimum acceptable impact energy at service temperature (exemplar value per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Degradation Problem | Discrepancy between current and desired resistance to corrosion, fatigue, and creep in service. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Degradation Problem → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Degradation Problem → `Technical Parameter` → Corrosion-rate ceiling | Maximum tolerable mass loss per year in the service environment (exemplar value per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Degradation Problem → `Technical Requirement` | Grouping: Technical Requirement elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Degradation Problem → `Technical Requirement` → Fatigue-life requirement | Formalized cycle-count objective at service stress (exemplar per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Dimensional-nonconformance Problem | Discrepancy between current and desired geometry against drawing tolerances. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Dimensional-nonconformance Problem → `Technical Requirement` | Grouping: Technical Requirement elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Dimensional-nonconformance Problem → `Technical Requirement` → Dimensional-conformance requirement | Formalized drawing-conformance objective per feature class (exemplar per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Dimensional-nonconformance Problem → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Problem` → Material Problem → `Technical Problem` → Dimensional-nonconformance Problem → `Technical Parameter` → Tolerance band | Accepted deviation around nominal geometry (exemplar value per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` | Grouping: Technical Practice elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice | The overall organized patterns of technical work in physical material technology, decomposed below into specific practices. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` | Grouping: Technical Practice elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Melting-casting Practice | Repeatable organized pattern of converting charge to solid stock: melting, refining, casting, and homogenizing. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Melting-casting Practice → `Technical Task` | Grouping: Technical Task elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Melting-casting Practice → `Technical Task` → Melt Task | Discrete unit of planned work bringing a charge to pouring condition. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Forming Practice | Repeatable organized pattern of bringing stock to shape by plastic deformation: forging, rolling, and extrusion. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Forming Practice → `Technical Task` | Grouping: Technical Task elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Forming Practice → `Technical Task` → Hot-rolling Task | Discrete unit of planned work reducing slab to strip at temperature. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice | Repeatable organized pattern of bringing stock to net shape by controlled material removal. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice → `Technical Task` | Grouping: Technical Task elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice → `Technical Task` → Machine-part Task | Discrete unit of planned work producing a finished part from stock on a machine tool. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice → `Technical Task` → Machine-part Task → `General Technique` | Grouping: General Technique elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice → `Technical Task` → Machine-part Task → `General Technique` → Machining | Generalized method for removing material to specified geometry and finish. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice → `Technical Task` → Machine-part Task → `General Technique` → Machining → `Operative Technique` | Grouping: Operative Technique elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice → `Technical Task` → Machine-part Task → `General Technique` → Machining → `Operative Technique` → CNC milling | Situated application of machining to a programmed three-axis envelope (exemplar machine per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice → `Technical Task` → Machine-part Task → `General Technique` → Machining → `Operative Technique` → CNC milling → `Technical Act` | Grouping: Technical Act elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice → `Technical Task` → Machine-part Task → `General Technique` → Machining → `Operative Technique` → CNC milling → `Technical Act` → Cut | Primitive act of separating a chip from the workpiece along the programmed path. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice → `Constitutive Technique` | Grouping: Constitutive Technique elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice → `Constitutive Technique` → Shear-cutting logic | Technique embodied in the tool-workpiece engagement establishing chip-formation logic for the programmed path. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice → `Technical Interface & Actuation` | Grouping: Technical Interface & Actuation elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Machining Practice → `Technical Interface & Actuation` → CNC plus G-code | Boundary and means through which the machinist encodes toolpaths and acts on the stock. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Joining Practice | Repeatable organized pattern of uniting pieces into assemblies: welding, brazing, bonding, and fastening. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Joining Practice → `Technical Task` | Grouping: Technical Task elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Joining Practice → `Technical Task` → Weld Task | Discrete unit of planned work fusing a joint to procedure. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Characterization Practice | Repeatable organized pattern of determining microstructure, properties, and conformance. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Characterization Practice → `Technical Task` | Grouping: Technical Task elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Characterization Practice → `Technical Task` → Tensile-test Task | Discrete unit of planned work pulling a specimen to specified strain. |
| `Technical Element Set` → Physical Material Technology → `Technical Practice` → Practice → `Technical Practice` → Characterization Practice → `Technical Task` → Metallography Task | Discrete unit of planned work revealing microstructure under the microscope. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` | Grouping: Production Technical System elements. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System | Organized set of furnaces, mills, and machine tools realizing specified stock. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` | Grouping: Production Technical Object elements. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Ferrous alloys | Production object family converting iron-based melts to structural stock. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Ferrous alloys → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Ferrous alloys → `Technical Parameter` → Grade 316L | Exemplar austenitic stainless grade for corrosive service (exemplar deployment). |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Nonferrous alloys | Production object family converting light and refractory melts to stock. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Nonferrous alloys → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Nonferrous alloys → `Technical Parameter` → Grade 6061-T6 | Exemplar heat-treatable aluminum grade for structural service (exemplar deployment). |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Ceramics and glass | Production object family converting powders and melts to hard, brittle stock. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Ceramics and glass → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Ceramics and glass → `Technical Parameter` → Grade Y-TZP | Exemplar transformation-toughened zirconia for wear service (exemplar deployment). |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Polymers | Production object family converting monomers to engineering plastics. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Polymers → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Polymers → `Technical Parameter` → Grade PEEK | Exemplar high-temperature thermoplastic for demanding service (exemplar deployment). |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Composites | Production object family combining fibers and matrices into anisotropic stock. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Composites → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Composites → `Technical Parameter` → Grade CFRP quasi-isotropic | Exemplar carbon-fiber layup for stiffness-critical service (exemplar deployment). |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Semiconductors | Production object family converting purified melts to electronic stock. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Semiconductors → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Processing System → `Production Technical Object` → Semiconductors → `Technical Parameter` → Grade CZ-Si | Exemplar Czochralski silicon for device service (exemplar deployment). |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Test lab | Organized set of instruments realizing demonstrated conformance. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Test lab → `Constitutive Technical Object` | Grouping: Constitutive Technical Object elements. |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Test lab → `Constitutive Technical Object` → Tensile frame | Constitutive object pulling specimens under controlled strain (exemplar capacity per deployment). |
| `Technical Element Set` → Physical Material Technology → `Production Technical System` → Test lab → `Constitutive Technical Object` → Scanning electron microscope | Constitutive object imaging microstructure and fracture surfaces (exemplar resolution per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Resource` | Grouping: Technical Resource elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Resource` → Charge stock | Input melted and cast per heat (exemplar mass per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Resource` → Cutting-tool stock | Input consumed at the cutting edge per part program (exemplar life per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Resource` → Shielding-gas stock | Input blanketing melts and welds per operation (exemplar volume per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Agent` | Grouping: Technical Agent elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Agent` → Metallurgist | Human agent specifying alloys and signing off heats (exemplar actors per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Agent` → Machinist | Human agent proving out and running part programs (exemplar actors per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Agent` → Inspector | Human agent witnessing tests and accepting lots (exemplar actors per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Feedback` | Grouping: Technical Feedback elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Feedback` → Melt temperature | Thermal signal of furnace state enabling chemistry and pouring moves. |
| `Technical Element Set` → Physical Material Technology → `Verification` | Grouping: Verification elements. |
| `Technical Element Set` → Physical Material Technology → `Verification` → Test verification | Check that a lot conforms to its specification through witnessed testing. |
| `Technical Element Set` → Physical Material Technology → `Technical Specification` | Grouping: Technical Specification elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Specification` → Mill certificate | Documented heat chemistry, properties, and conformance statement (exemplar per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Maintenance` | Grouping: Technical Maintenance elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Maintenance` → Furnace relining | Work restoring refractory functional state per campaign (exemplar schedule per deployment). |
| `Technical Element Set` → Physical Material Technology → `Technical Lifecycle` | Grouping: Technical Lifecycle elements. |
| `Technical Element Set` → Physical Material Technology → `Technical Lifecycle` → Heat lifecycle | Temporal trajectory of a heat from charge through processing to qualified stock. |

## References

- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md)
- [Energy Technology (companion domain pattern)](note.html?n=technica/cto/es/multinode/energy-technology.md)
- https://www.asminternational.org/
- https://www.nist.gov/
