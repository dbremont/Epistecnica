---
tags: [note, steel, alloy]
---

# Steel

> **Steel** is the iron-carbon alloy family with improved mechanical properties over pure iron, classified by composition, microstructure, treatment, and use. Source: Produceologia `docs/Foundation/Steel.md` (read-only import; the original is untouched).

## Formulation

### What technical element type does this technical instance belong to?

**Steel belongs to the `Constitutive Technical Object` technical element type — a stuff-kind constituting larger objects and systems.**

### What is this technical instance?

> Low-carbon A36 and 1018 for construction and autos, medium 1045 for gears and rails, stainless 304, 316, 410, and 420, low-alloy 4140 and 4340, tool steels M2 and D2, structural A36 and A992, auto DP600, and pipeline API 5L X65 — enabling vehicles, structures, pipelines, aerospace, and tooling.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one alloy family, decomposed at shallow depth — root plus representative grades only.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Constitutive Technical Object` → Steel | Iron-carbon alloy family. |
| `Constitutive Technical Object` → Steel → `Constitutive Technical Object` | Grouping: representative grades. |
| `Constitutive Technical Object` → Steel → `Constitutive Technical Object` → A36 Structural Grade | General construction grade. |
| `Constitutive Technical Object` → Steel → `Constitutive Technical Object` → 304 Stainless Grade | Corrosion-resistant austenitic grade. |
| `Constitutive Technical Object` → Steel → `Constitutive Technical Object` → 4140 Alloy Grade | Hardening machinery grade. |
| `Constitutive Technical Object` → Steel → `Constitutive Technical Object` → DP600 Auto Grade | Formable high-strength auto grade. |

## Characterization

> Steel is usually classified based on chemical composition and microstructure as primary criteria, but real-world classification also considers heat treatment behavior, processing method, mechanical performance, surface treatment, and use case.

| **Feature**                    | **Description**                                                                             | **Common Categories**                                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 🧪 **Chemical Composition**    | Elements present in the alloy, especially carbon and alloying elements like Cr, Ni, Mo, V   | - Carbon Steel<br>- Alloy Steel<br>- Stainless Steel<br>- Tool Steel            |
| 🧬 **Microstructure**          | Crystalline phases (e.g., ferrite, austenite) present after heat treatment or cooling       | - Ferritic<br>- Austenitic<br>- Martensitic<br>- Bainitic<br>- Pearlitic        |
| 🔥 **Heat Treatment Behavior** | How the steel responds to processes like quenching, annealing, tempering                    | - Hardenable vs Non-hardenable<br>- Air vs Water vs Oil Quenching               |
| 🏭 **Manufacturing Process**   | Method of refining, alloying, and shaping the steel                                         | - Basic Oxygen Process<br>- Electric Arc Furnace<br>- Killed/Semi-killed/Rimmed |
| 🎯 **Mechanical Properties**   | Physical characteristics like strength, hardness, ductility, toughness, and wear resistance | - High-strength<br>- Wear-resistant<br>- Ductile<br>- Brittle                   |
| 🛡️ **Corrosion Resistance**   | Ability to resist oxidation and chemical attack                                             | - Stainless vs Non-stainless<br>- Galvanized/Coated                             |
| ⚙️ **Surface Treatment**       | Coatings or treatments applied to enhance properties like corrosion resistance              | - Galvanized (zinc-coated)<br>- Aluminized<br>- Painted or Powder-coated        |
| 🧰 **Application/Use Case**    | The functional role or industry it's designed for                                           | - Structural<br>- Automotive<br>- Aerospace<br>- Food-grade<br>- Tooling        |
| 📏 **Form/Shape**              | Final shape/form factor (especially in standards)                                           | - Sheet<br>- Plate<br>- Bar<br>- Pipe<br>- Rebar                                |
| 📐 **Standards & Grades**      | Classification by standard bodies with grade numbers and specs                              | - ASTM (A36, A572)<br>- SAE (1045, 4140)<br>- EN, DIN, JIS                      |

## Steel Taxonomy

| **Dimension**            | **Category**           | **Subcategory / Type**            | **Key Characteristics**                              | **Typical Uses**                        | **Example Grades**     |
| ------------------------ | ---------------------- | --------------------------------- | ---------------------------------------------------- | --------------------------------------- | ---------------------- |
| **By Composition**       | Carbon Steel           | Low Carbon (< 0.3%)               | Ductile, weldable, low cost                          | Construction, auto panels               | A36, 1018              |
|                          |                        | Medium Carbon (0.3-0.6%)          | Balance of strength and ductility                    | Gears, axles, railway tracks            | 1045, 1050             |
|                          |                        | High Carbon (> 0.6%)              | Hard, wear-resistant, brittle                        | Blades, springs                         | 1095, 1080             |
|                          | Alloy Steel            | Low-Alloy Steel                   | Improved strength, toughness                         | Pipelines, structural parts             | 4140, 4340             |
|                          |                        | High-Alloy Steel                  | Heat- or corrosion-resistant                         | Aerospace, high-temp service            | H13, M2                |
|                          | **Stainless Steel**    | Austenitic                        | High corrosion resistance, non-magnetic, ductile     | Kitchenware, medical tools, piping      | 304, 316               |
|                          |                        | Ferritic                          | Magnetic, moderate corrosion resistance              | Appliances, exhausts                    | 409, 430               |
|                          |                        | Martensitic                       | Magnetic, hardenable, moderate corrosion resistance  | Cutlery, surgical tools                 | 410, 420, 440C         |
|                          |                        | Duplex                            | Mixed microstructure, strong and corrosion-resistant | Marine, chemical processing             | 2205, 2507             |
|                          |                        | PH Stainless                      | Precipitation-hardened for strength                  | Aerospace, shafts, fasteners            | 17-4PH, 15-5PH         |
|                          | Tool Steel             | High-speed, Shock-resisting, etc. | Extremely hard and wear-resistant                    | Cutting tools, dies                     | M2, T1, D2, O1, A2     |
| **By Microstructure**    | Ferritic               | —                                 | BCC, magnetic, low hardenability                     | Structural sheets                       | 430                    |
|                          | Austenitic             | —                                 | FCC, non-magnetic, excellent corrosion resistance    | Pipes, tanks, kitchen sinks             | 304, 316               |
|                          | Martensitic            | —                                 | BCT, hard and brittle after quench                   | Blades, turbines                        | 420, 440C              |
|                          | Bainitic               | —                                 | Tough, good strength                                 | Rails, automotive                       | —                      |
|                          | Pearlitic              | —                                 | Lamellar structure, wear-resistant                   | Wire, rails                             | —                      |
| **By Processing Method** | Electric Furnace Steel | —                                 | Precision control over impurities                    | Specialty steels                        | —                      |
|                          | Basic Oxygen Steel     | —                                 | High volume, efficient production                    | Construction steel                      | —                      |
|                          | Killed Steel           | —                                 | Fully deoxidized, uniform properties                 | Pressure vessels                        | —                      |
|                          | Semi-killed Steel      | —                                 | Partially deoxidized, lower cost                     | General structural use                  | —                      |
|                          | Rimmed Steel           | —                                 | Poorly deoxidized, good surface finish               | Sheet metal                             | —                      |
| **By Surface Treatment** | **Galvanized Steel**   | Hot-dip Galvanized                | Zinc-coated by immersion, thick durable layer        | Roofing, guardrails, outdoor structures | G90, G60 (zinc grades) |
|                          |                        | Electro-galvanized                | Thin zinc coating via electroplating                 | Automotive body panels                  | EG steel               |
|                          | Coated Steel           | Aluminized, Painted               | Surface-coated with aluminum, enamel, or epoxy       | Mufflers, cookware, white goods         | Aluminized Type 1, 2   |
| **By Application**       | Structural Steel       | —                                 | Strong, weldable                                     | Frames, beams                           | A36, ASTM A992         |
|                          | Automotive Steel       | —                                 | Formable, strong, lightweight                        | Chassis, doors                          | DP600, TRIP780         |
|                          | Pipeline Steel         | —                                 | Tough, corrosion-resistant                           | Oil/gas pipelines                       | API 5L X65             |
|                          | Aerospace Steel        | —                                 | Lightweight, fatigue-resistant                       | Aircraft, missiles                      | Maraging 300           |
|                          | Cutlery / Tooling      | —                                 | High hardness, corrosion-resistant                   | Knives, molds                           | 440C, H13, D2          |

## References

- Produceologia `docs/Foundation/Steel.md`
- [Heat Treatment](/view.html?p=notes/technica/general/materiotecnia/heat-treatment.md) — the cycles that make a grade a spring, a gear or a bearing
- [Welding](/view.html?p=notes/technica/general/welding.md) — joining, and the heat-affected zone the carbon equivalent controls
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md)
