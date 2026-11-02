---
tags: [retail, supply-chain, demand-forecasting, inventory, multi-root]
---

# Retail Supply–Demand Matching

> **Retail Supply–Demand Matching** is the operative system through which a retailer keeps shelves filled: sensing demand, planning orders, allocating scarce supply, and learning from stockouts and substitutions. Source: the three-space reading developed in the ambiguity guide (`guideline/ambiguity_resolution.md`).

## Formulation

### Which readings does this instance carry?

| Space | Root type | Tree |
| --- | --- | --- |
| technique (primary) | `Technical Practice` | Demand planning and replenishment: tasks, techniques, acts, ensemble |
| social (secondary) | `Social Compound` | Retail ensemble: units, roles, norms, coordinators, dynamics |
| epistemic (secondary) | `Concrete Epistemic Artifact` | Demand estimate: interfaces, artifacts, feedback, standards |

### What technical element type does this technical instance belong to?

> **This instance's primary belonging is `Technical Practice` (technique space)** — the repeatable, organized pattern of sensing demand and replenishing shelves. It is readable as a `Social Compound` (social space: the retail ensemble whose coordination it serves) and as a `Concrete Epistemic Artifact` (epistemic space: the demand estimate its sensing task produces). Each reading grows its own well-formed tree below, typed by its own grammar; no row carries two types (`guideline/ambiguity_resolution.md`, multi-root note rule).

### What is this technical instance?

> One retailer's closed loop of demand sensing, order planning, and shortage allocation: register sales become a demand estimate; the estimate becomes orders and quotas under lead times; stockouts and substitutions feed back into the next estimate. Boundary: one matching system, decomposed at middle depth — full intermediate structure through the declared roots, exemplars only where a branch needs one.

### What is the recursive instance decomposition of this instance under technique?

> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Typing reads from grouping segments and the declared root binding (`Technical Practice`).

| Instance Tree Path | Description |
| --- | --- |
| `Technical Practice` → Demand Planning & Replenishment | Repeatable pattern matching store demand to supply through sensing, planning, and allocation. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` | Grouping: tasks of the practice. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Demand Sensing Task | Scheduled task converting observed sales into a demand estimate. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Demand Sensing Task → `General Technique` | Grouping: estimation techniques of the task. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Demand Sensing Task → `General Technique` → Censored Demand Estimation | Generalized method recovering true demand from sales censored by stockouts. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Demand Sensing Task → `General Technique` → Censored Demand Estimation → `Operative Technique` | Grouping: situated estimations. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Demand Sensing Task → `General Technique` → Censored Demand Estimation → `Operative Technique` → Weekly SKU Forecast Run | This week's estimation of one SKU's demand at one store cluster. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Demand Sensing Task → `General Technique` → Censored Demand Estimation → `Operative Technique` → Weekly SKU Forecast Run → `Technical Act` | Grouping: primitive acts of the run. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Demand Sensing Task → `General Technique` → Censored Demand Estimation → `Operative Technique` → Weekly SKU Forecast Run → `Technical Act` → Forecast Publication Act | Primitive act of publishing the forecast to the planning tasks. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Order Planning Task | Scheduled task converting forecasts into orders given lead times. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Order Planning Task → `General Technique` | Grouping: planning techniques. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Order Planning Task → `General Technique` → Lot-Sizing Rule | Generalized method balancing ordering and holding cost. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Order Planning Task → `General Technique` → Lot-Sizing Rule → `Operative Technique` | Grouping: situated planning runs. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Order Planning Task → `General Technique` → Lot-Sizing Rule → `Operative Technique` → Nightly Reorder Computation | Tonight's order quantities for one distribution center's stores. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Order Planning Task → `General Technique` → Lot-Sizing Rule → `Operative Technique` → Nightly Reorder Computation → `Technical Act` | Grouping: primitive acts of the computation. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Order Planning Task → `General Technique` → Lot-Sizing Rule → `Operative Technique` → Nightly Reorder Computation → `Technical Act` → Purchase Order Release Act | Primitive act of releasing orders to suppliers. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Allocation Task | Scheduled task rationing scarce supply across stores. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Allocation Task → `General Technique` | Grouping: allocation techniques. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Allocation Task → `General Technique` → Fair-Share Allocation | Generalized method splitting limited stock by need and priority. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Allocation Task → `General Technique` → Fair-Share Allocation → `Operative Technique` | Grouping: situated rationing runs. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Allocation Task → `General Technique` → Fair-Share Allocation → `Operative Technique` → Shortage Rationing Run | This morning's rationing of one scarce SKU. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Allocation Task → `General Technique` → Fair-Share Allocation → `Operative Technique` → Shortage Rationing Run → `Technical Act` | Grouping: primitive acts of the run. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Task` → Allocation Task → `General Technique` → Fair-Share Allocation → `Operative Technique` → Shortage Rationing Run → `Technical Act` → Store Quota Assignment Act | Primitive act of assigning store quotas. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Parameter` | Grouping: parameters characterizing the practice. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Parameter` → Lead-Time Parameter | Days between order and receipt (exemplar value per deployment). |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Parameter` → Service-Level Target | Fill rate the practice must sustain (exemplar value per deployment). |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Interface & Actuation` | Grouping: boundaries through which agents act. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Interface & Actuation` → Point-Of-Sale Capture Boundary | Boundary through which register sales enter the sensing task. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Interface & Actuation` → Dock Handoff Interface | Boundary through which replenishment leaves the distribution center for stores. |
| `Technical Practice` → Demand Planning & Replenishment → `Constitutive Technique` | Grouping: techniques embodied in the planning elements. |
| `Technical Practice` → Demand Planning & Replenishment → `Constitutive Technique` → Allocation Engine Logic | Technique embodied in the allocation engine establishing its rationing logic. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Standard` | Grouping: normative specifications. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Standard` → EDI Order Standard | Normative message contract for orders and invoices between retailer and suppliers. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Feedback` | Grouping: adjustment signals. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Feedback` → Stockout Signal | Signal of empty shelves triggering re-estimation. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Feedback` → Forecast Error Residual | Gap between forecast and realized sales steering the next run. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Evaluation` | Grouping: evaluations of execution. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Evaluation` → `Verification` | Grouping: conformance checks. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Evaluation` → `Verification` → On-Time Delivery Verification | Check that deliveries conform to the planned schedule. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Evaluation` → `Validation` | Grouping: purpose checks. |
| `Technical Practice` → Demand Planning & Replenishment → `Technical Evaluation` → `Validation` → Shelf Availability Validation | Determination that execution fulfills the availability purpose. |

### What is the recursive instance decomposition of this instance under social?

> Identity: Instance Tree Path is stable and unique. Typing reads from grouping segments and the declared root binding (`Social Compound`), read against the economic facet and the Multi layer (ontic venues and goods, synontic prices and contracts).

| Instance Tree Path | Description |
| --- | --- |
| `Social Compound` → Retail Matching Ensemble | Bounded ensemble of retailer, stores, suppliers, rules, and coordinators matching supply to demand in one basin. |
| `Social Compound` → Retail Matching Ensemble → `Interaction Unit` | Grouping: units. |
| `Social Compound` → Retail Matching Ensemble → `Interaction Unit` → Retail Chain | Agentive unit operating stores and the distribution center. |
| `Social Compound` → Retail Matching Ensemble → `Interaction Unit` → Corner Store | Agentive unit selling to final customers (exemplar deployments). |
| `Social Compound` → Retail Matching Ensemble → `Interaction Unit` → Produce Supplier | Agentive unit delivering cucumbers and substitutes. |
| `Social Compound` → Retail Matching Ensemble → `Collective / Organization` | Grouping: compound units. |
| `Social Compound` → Retail Matching Ensemble → `Collective / Organization` → Buying Cooperative | Compound unit pooling orders across stores. |
| `Social Compound` → Retail Matching Ensemble → `Institution` | Grouping: stabilized configurations. |
| `Social Compound` → Retail Matching Ensemble → `Institution` → Procurement Institution | Stabilized configuration of buying roles and rules. |
| `Social Compound` → Retail Matching Ensemble → `Institution` → Procurement Institution → `Social Role` | Grouping: roles. |
| `Social Compound` → Retail Matching Ensemble → `Institution` → Procurement Institution → `Social Role` → Store Buyer Role | Expectation-tag binding ordering authority to the buyer. |
| `Social Compound` → Retail Matching Ensemble → `Institution` → Procurement Institution → `Social Role` → Store Buyer Role → `Norm / Regulation` | Grouping: norms. |
| `Social Compound` → Retail Matching Ensemble → `Institution` → Procurement Institution → `Social Role` → Store Buyer Role → `Norm / Regulation` → Service-Level Norm | Shared protocol: shelves stay filled to the agreed fill rate. |
| `Social Compound` → Retail Matching Ensemble → `Institution` → Procurement Institution → `Social Role` → Store Buyer Role → `Norm / Regulation` → Service-Level Norm → `Right / Obligation` | Grouping: deontic positions. |
| `Social Compound` → Retail Matching Ensemble → `Institution` → Procurement Institution → `Social Role` → Store Buyer Role → `Norm / Regulation` → Service-Level Norm → `Right / Obligation` → Late-Delivery Penalty | Obligation allocating compensation for missed windows. |
| `Social Compound` → Retail Matching Ensemble → `Synontic Element` | Grouping: recognition-constituted coordinators. |
| `Social Compound` → Retail Matching Ensemble → `Synontic Element` → Supply Contract | Coordinator persisting through shared recognition of terms. |
| `Social Compound` → Retail Matching Ensemble → `Price / Asset` | Grouping: scalar variables and claim-objects. |
| `Social Compound` → Retail Matching Ensemble → `Price / Asset` → Spot Cucumber Price | Scalar variable coordinating offers (exemplar value per deployment). |
| `Social Compound` → Retail Matching Ensemble → `Price / Asset` → Markdown Allowance | Claim-object funding price cuts on surplus. |
| `Social Compound` → Retail Matching Ensemble → `Capital / Labor` | Grouping: multi-layer operators. |
| `Social Compound` → Retail Matching Ensemble → `Capital / Labor` → Shelf-Stocking Labor | Productive capacity shelving goods (exemplar size per deployment). |
| `Social Compound` → Retail Matching Ensemble → `Social Relation / Network` | Grouping: ties. |
| `Social Compound` → Retail Matching Ensemble → `Social Relation / Network` → Supplier–Retailer Supply Tie | Structured exchange tie binding deliveries to orders. |
| `Social Compound` → Retail Matching Ensemble → `Belief / Expectation` | Grouping: shared anticipations. |
| `Social Compound` → Retail Matching Ensemble → `Belief / Expectation` → Availability Expectation | Shared anticipation that shelves are stocked. |
| `Social Compound` → Retail Matching Ensemble → `Process / Event` | Grouping: transformations. |
| `Social Compound` → Retail Matching Ensemble → `Process / Event` → Late Delivery Event | Punctual occurrence disrupting the plan. |
| `Social Compound` → Retail Matching Ensemble → `Process / Event` → Harvest Glut Event | Punctual oversupply forcing markdowns. |
| `Social Compound` → Retail Matching Ensemble → `Mechanism / Phenomenon` | Grouping: trajectories. |
| `Social Compound` → Retail Matching Ensemble → `Mechanism / Phenomenon` → Substitution Cascade | Trajectory of demand shifting across SKUs after a stockout. |
| `Social Compound` → Retail Matching Ensemble → `Mechanism / Phenomenon` → Bullwhip Amplification | Trajectory of order variance growing upstream. |
| `Social Compound` → Retail Matching Ensemble → `State` | Grouping: snapshots. |
| `Social Compound` → Retail Matching Ensemble → `State` → Shelf Snapshot | Complete relevant-variable snapshot of shelves at a moment (exemplar per deployment). |

### What is the recursive instance decomposition of this instance under epistemic?

> Identity: Instance Tree Path is stable and unique. Typing reads from grouping segments and the declared root binding (`Concrete Epistemic Artifact`).

| Instance Tree Path | Description |
| --- | --- |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate | Structured claim about one SKU's demand at one store cluster this week, evaluable against realized sales. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observation Interface` | Grouping: feeds. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observation Interface` → Point-Of-Sale Feed | Boundary transducing register events into a persistent log. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observation Interface` → Point-Of-Sale Feed → `Transduction` | Grouping: signal conversions. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observation Interface` → Point-Of-Sale Feed → `Transduction` → Register Scan | Conversion of a barcode pass into a measurable event. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observation Interface` → Point-Of-Sale Feed → `Sampling` | Grouping: registrations selected from the flux. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observation Interface` → Point-Of-Sale Feed → `Sampling` → Nightly Batch Pull | Discrete registration set drawn each night. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observation Interface` → Point-Of-Sale Feed → `Quantization` | Grouping: finite-value mappings. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observation Interface` → Point-Of-Sale Feed → `Quantization` → SKU Bucketing | Mapping of scans onto SKU-day bins. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observation Interface` → Point-Of-Sale Feed → `Observation Encoding` | Grouping: storable-value procedures. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observation Interface` → Point-Of-Sale Feed → `Observation Encoding` → EDI 852 Encoding | Procedure encoding movement data into the product-activity message. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observation Interface` → Point-Of-Sale Feed → `Encoding Substrate` | Grouping: instantiation media. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observation Interface` → Point-Of-Sale Feed → `Encoding Substrate` → POS Log Database | Medium in which the encoded log persists. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Phenomenon` | Grouping: unified explanatory objects. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Phenomenon` → Censored Demand Pattern | Pattern of true demand hidden by stockouts. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Phenomenon` → Substitution Pattern | Pattern of demand shifting across SKUs. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observable` | Grouping: registrable measurements. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Observable` → Shelf Gap Reading | Measurement of empty facings under the observation regime. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Epistemic Operator` | Grouping: construction and validation mechanisms. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Epistemic Operator` → Censoring-Aware Estimator | Mechanism recovering true demand from censored sales. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Epistemic Representation Form` | Grouping: encoding formats. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Epistemic Representation Form` → Seasonal Regression Form | Format expressing demand as trend plus seasonal and promo effects. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Epistemic Feedback` | Grouping: reality signals steering estimation. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Epistemic Feedback` → Stockout Censoring Flag | Signal marking which sales observations are censored. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Epistemic Feedback` → Forecast Error Residual | Prediction error feeding the next estimation round — and the next technical sensing run. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Epistemic Standard` | Grouping: validity criteria. |
| `Concrete Epistemic Artifact` → Weekly SKU Demand Estimate → `Epistemic Standard` → Forecast Accuracy Criterion | Normative bar on forecast error (exemplar threshold per deployment). |

### Nature substrate

> The goods moved (cucumbers, substitutes) and their conditioning (cold chain, ripening rooms) decompose naturally — as `Natural Object`s, `Substance / Matter`, and `Natural Process`es at the appropriate level of organization — not here. This note cross-links that reading instead of growing a fourth tree (`guideline/ambiguity_resolution.md`: canonical multi-root note).

## References

- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
- [Philosophia Artium Epistemicarum et Operis](note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Socialium et Operis](note.html?n=meta/philosophia-socialium-et-operis.md)
- Ambiguity Resolution (`guideline/ambiguity_resolution.md`)
- [Logistics System](note.html?n=technica/general/cto/industry/logistics-system.md)
