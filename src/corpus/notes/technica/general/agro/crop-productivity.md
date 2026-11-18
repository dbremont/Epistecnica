---
tags: [note, agro, crop, productivity, yield, measure]
---

# Crop Productivity

> **Crop productivity** is the harvested output of a cropped area per unit of the resource committed to it — most simply yield per hectare, more completely total factor productivity, and most usefully the gap between what a field yields and what the best available practice could yield there. It is the number that judges every input, practice and variety in the agro domain.

> The concept is relational from the start. A yield in tonnes per hectare means nothing without the crop, the climate, the water regime and the accounting period; a fertilizer response means nothing without the nutrient already in the soil. Productivity is a ratio, and both of its terms must be stated before the number can be compared.

## Formulation

### What technical element type does this technical instance belong to?

**Crop Productivity belongs to the `Technical Parameter` technical element type — a variable whose value characterizes and controls a technical process.**

It is a parameter because it is measured, not made: the grower acts on the levers, and productivity is the resulting reading. Readable secondarily as a `Technical Evaluation` — the criterion against which a practice, a variety or a season is judged — and as a `Technical Purpose` when the object is to raise it. Those readings are prose here, not second roots.

### What is this technical instance?

> Yield per hectare for a named crop in a named environment; the yield gap between the realized and the attainable; the partial productivity of a nutrient, a cubic metre of water or an hour of labour; and total factor productivity, which divides an index of output by an index of all inputs and is the only measure that does not flatter a system by ignoring what it consumed.

### What is the recursive instance decomposition of this technical instance?

> Boundary: the measure and its components, the resources and constraints that set it, and the levers that move it. The practices themselves are decomposed in their own notes — this note decomposes the reading, not the field work.
>
> Stopping rule: a row is terminal when it names a measure, a resource, a constraint or a named lever.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.
>
> Verbs: the resource *bounds* the yield; the lever *moves* it; the measure *reports* the result.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Parameter` → Crop Productivity | The harvested output per unit resource, and the gap to the attainable. |
| `Technical Parameter` → Crop Productivity → `Technical Parameter` | Grouping: the measures the concept is read as. |
| `Technical Parameter` → Crop Productivity → `Technical Parameter` → Yield per Hectare | Harvested mass or value per unit area for a named crop and season. |
| `Technical Parameter` → Crop Productivity → `Technical Parameter` → Yield Gap | The difference between the realized yield and the attainable yield under the same climate and water. |
| `Technical Parameter` → Crop Productivity → `Technical Parameter` → Total Factor Productivity | Output index divided by an index of all inputs — the measure that counts what the system consumed. |
| `Technical Parameter` → Crop Productivity → `Technical Parameter` → Water Productivity | Output per cubic metre of water, the decisive ratio in irrigated and dryland systems. |
| `Technical Parameter` → Crop Productivity → `Technical Parameter` → Partial Factor Productivity | Output per unit of one input — nitrogen, labour, capital — useful and easy to misread. |
| `Technical Parameter` → Crop Productivity → `Technical Resource` | Grouping: the resources that set the ceiling. |
| `Technical Parameter` → Crop Productivity → `Technical Resource` → Genetic Potential | The yield the variety can reach in the environment, before management limits it. |
| `Technical Parameter` → Crop Productivity → `Technical Resource` → Nutrient Supply | The nitrogen, phosphorus, potassium and micronutrients available from soil and fertilizer. |
| `Technical Parameter` → Crop Productivity → `Technical Resource` → Water Supply | Rainfall, irrigation and stored soil water through the season. |
| `Technical Parameter` → Crop Productivity → `Technical Resource` → Labour and Machinery | The power and timing available for tillage, sowing, protection and harvest. |
| `Technical Parameter` → Crop Productivity → `Technical Constraint` | Grouping: the bounds the environment imposes. |
| `Technical Parameter` → Crop Productivity → `Technical Constraint` → Climate | Temperature, radiation and season length — the ceiling no management can exceed. |
| `Technical Parameter` → Crop Productivity → `Technical Constraint` → Pest and Disease Pressure | The loss the standing crop suffers before and after protection. |
| `Technical Parameter` → Crop Productivity → `Technical Constraint` → Soil Constraint | Depth, texture, pH, salinity and organic matter that limit root growth and nutrient availability. |
| `Technical Parameter` → Crop Productivity → `Technical Constraint` → Timing | The sowing and harvest windows that decide whether the resources are used at all. |

## Measures

| Measure | Definition | What it is for | What it hides |
| --- | --- | --- | --- |
| **Yield per hectare** | Harvested mass (or value) ÷ area | Comparing fields, seasons and varieties | Inputs consumed, quality, environmental cost |
| **Yield gap** | Attainable − realized yield | The size of the improvement available | Whether closing it is economic |
| **Total factor productivity** | Output index ÷ input index | Long-run system performance | Distribution, environment, quality |
| **Water productivity** | Output ÷ water consumed | The ratio that matters where water is scarce | Water source and downstream effects |
| **Partial factor productivity** | Output ÷ one input | Quick input-use diagnostics | Substitution between inputs |
| **Nutrient use efficiency** | Nutrient taken up ÷ nutrient applied | Fertilizer performance and loss | Soil reserves and long-run balance |

## The Levers

| Lever | Mechanism | Note |
| --- | --- | --- |
| **Genetics** | A variety with higher potential, resistance or quality | [Plant Genetic Improvement](/view.html?p=notes/technica/general/plant-genetic-improvement.md) |
| **Nutrients** | Relieving the nutrient that limits the crop | [Fertilizer Industry](/view.html?p=notes/technica/production/industry/chemical/fertilizer.md) |
| **Water** | Relieving drought stress and matching supply to demand | [Plant Cultivation](/view.html?p=notes/technica/general/plant-cultivation-technical-domain-set.md) |
| **Protection** | Reducing the loss to weeds, pests and pathogens | [Plant Health](/view.html?p=notes/technica/general/plant-health-technical-set.md) · [Glyphosate](/view.html?p=notes/technica/general/agro/glyphosate.md) |
| **Management** | Timing, density, rotation and tillage | [Plant Cultivation](/view.html?p=notes/technica/general/plant-cultivation-technical-domain-set.md) |
| **Climate** | The ceiling and the variability — not a lever | [Earth Science](/view.html?p=notes/miscellanea/discipline/earth-science.md) |

> The levers are not additive. Liebig's law of the minimum says the scarcest resource sets the yield; the response to relieving any one lever is therefore a function of the others, which is why a fertilizer trial in a dry year and a wet year can give opposite answers. The yield gap is not a single number to be closed but a set of constraints to be relieved in order.

## What is a critical conceptual evaluation of this technical element instance?

The concept under evaluation is **Crop Productivity**, defined above as *the harvested output per unit resource, read as yield, gap or total factor productivity*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: the parameter is separated from the practices that move it, from the yield itself and from the economic productivity of the farm. Definitional Clarity — **pass**: every measure is stated as a ratio with both terms named. Conceptual Determinacy — **pass with qualification**: which measure is "the" productivity depends on the question — land, water, labour, capital or total factor — and the note refuses to collapse them. Internal Consistency — **pass**: measures, resources and constraints are distinct branches; the levers stay in their own notes. Representational Adequacy — **qualified**: complete for the reading; the agronomy, the economics and the environmental accounting are links. Purpose Adequacy — **pass**: shaped for diagnosis — every row either measures the result or bounds it.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Distinguished from the practices, the yield itself and farm economic productivity. |
| Definitional Clarity | pass | Each measure is a ratio with both terms stated. |
| Conceptual Determinacy | pass (qualified) | Land, water, labour, capital and total-factor readings are kept apart by question. |
| Internal Consistency | pass | Measures, resources and constraints are separate branches; levers stay elsewhere. |
| Representational Adequacy | qualified | Complete for the reading; agronomy, economics and environmental accounting are links. |
| Purpose Adequacy | pass | Every row measures the result or bounds it. |

## Crop Yield Modelling

> Two quantitative traditions meet on this measure, and they answer different questions. The **process model** simulates the crop — carbon, nitrogen and water balances on daily or hourly steps — and is asked what a changed climate, management or cultivar would do. The **response function** fits yield against a controllable input — usually nutrient rate — and is asked what rate is economically optimal. The first extrapolates through mechanism; the second interpolates from trials.

| Approach | Question it answers | What it buys | What it costs |
| --- | --- | --- | --- |
| **Process crop model** | What would happen under a condition not yet observed? | Extrapolation to new CO₂, temperature, cultivar and management; the G×E×M interaction made explicit | Many parameters, and the field data to calibrate them |
| **Nutrient response function** | What rate of nutrient is optimal here? | An unbiased recommendation with a stated variance | The form must fit the site and the season; carryover and stochastic plateaus complicate it |
| **Yield-gap analysis** | How much is available to close? | A bound on the improvement, and its constraint | Says nothing about whether closing it is economic |

> The process-model case is made in [Boote et al. (2013)](/view.html?p=documents/papers/boote-2013-putting-mechanisms-crop-production-models-plant-cell-environment.md): put mechanisms in the model, because a calibrated empirical fit interpolates today's weather and extrapolates badly, and because a model that carries a trait rather than a yield is the bridge between genetics and the field.
>
> The response-function case is made in [Dhakal & Lange (2021)](/view.html?p=documents/papers/dhakal-2021-crop-yield-response-functions-nutrient-application-agronomy-journal.md): the functional form decides the recommendation, the plateau is stochastic rather than fixed, and the fit should carry the previous season's nutrient forward into a dynamic optimisation.

> The process tradition has its own canonical texts, and the two sit one level apart. [Thornley (1976)](/view.html?p=documents/books/thornley-1976-mathematical-models-plant-physiology.md) wrote the plant as a system of state variables and rate equations — carbon fixed and respired, translocated and allocated to growth, with water and mineral nitrogen as the other pools — and made plant physiology a modelling discipline. [Thornley & Johnson (1990)](/view.html?p=documents/books/thornley-johnson-1990-plant-and-crop-modelling.md) carried the same grammar up to the canopy and the crop, and it is the lineage every later mechanistic crop model descends from.
>
> The two are complements, not rivals. A process model without a response function gives no economic recommendation; a response function without a process model cannot say what happens outside the range of the trials. The practical programme uses the first to bound the second.

## References

- [Agricultural productivity](https://en.wikipedia.org/wiki/Agricultural_productivity)
- [Crop yield](https://en.wikipedia.org/wiki/Crop_yield) · [Yield gap](https://en.wikipedia.org/wiki/Yield_gap)
- [Total factor productivity](https://en.wikipedia.org/wiki/Total_factor_productivity)
- [Liebig's law of the minimum](https://en.wikipedia.org/wiki/Liebig%27s_law_of_the_minimum)
- [Fertilizer Industry](/view.html?p=notes/technica/production/industry/chemical/fertilizer.md) — the nutrient lever
- [Plant Genetic Improvement](/view.html?p=notes/technica/general/plant-genetic-improvement.md) — the genetic lever
- [Plant Cultivation Technical Domain Set](/view.html?p=notes/technica/general/plant-cultivation-technical-domain-set.md) — the management lever
- [Plant Health Technical Set](/view.html?p=notes/technica/general/plant-health-technical-set.md) — the protection lever
- [Thornley (1976). Mathematical Models in Plant Physiology](/view.html?p=documents/books/thornley-1976-mathematical-models-plant-physiology.md) — the plant-level founding text of the process tradition
- [Thornley & Johnson (1990). Plant and Crop Modelling](/view.html?p=documents/books/thornley-johnson-1990-plant-and-crop-modelling.md) — the crop-level reference every mechanistic model descends from
- [Agro](/view.html?p=notes/technica/general/agro/agro.md) — the domain entry note
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) — the schema and the permitted link forms
- [Technica Atlas](/corpus/notes/technica/atlas.html) — the forest this decomposition feeds
