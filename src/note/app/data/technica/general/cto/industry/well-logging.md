# Well Logging

> Well logging is technical in means but epistemic in goal: a borehole is drilled and wireline
> sondes are lowered to measure the geological formations around it. The intervention succeeds
> when it yields warranted belief about what lies underground — judged by confirmation,
> predictive yield, and reproducibility — not by transformation performance. Decomposed twice,
> once per reading, per `guideline/ambiguity_resolution.md`:
> the means under the technical grammar, the end under the epistemic grammar, cross-linked
> at the Observation Interface. No row ever carries both types.

## Formulation

### What technical element type does this technical instance belong to?

Default root: a `Technical Element Set` — the **well logging practice** (drilling, conveyance,
transduction, and recording organized to evaluate a formation). Readable as an epistemic
endeavor whose product is formation knowledge; that reading grows its own tree below rather
than a compromise type.

### What is this technical instance?

**Well logging**: the organized method of drilling a **borehole** and lowering **wireline sondes**
on a **logging cable** to transduce formation properties (natural radioactivity, resistivity,
acoustic slownness, density) into continuous **log curves** indexed by depth, for formation
evaluation. The cut includes the rig, the tool string, the borehole, and the recording chain;
it excludes the drilling-for-production operation and the reservoir-investment decision, which
consume the logs but belong to other readings.

### What is the recursive instance decomposition of this technical instance?

Tree 1 — the means (technicarum grammar). Instances plain; bare grouping
types `` `code` ``; every leaf resolves to a technical instance.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element Set` → Well Logging Practice | The organized method of evaluating a formation through borehole measurement. |
| `Technical Element Set` → Well Logging Practice → Wireline Crew | Agents executing the logging run. |
| `Technical Element Set` → Well Logging Practice → Wireline Crew → `Technical Competence` | Grouping: crew capabilities. |
| `Technical Element Set` → Well Logging Practice → Wireline Crew → `Technical Competence` → Tool-String Handling | Acquired capacity to assemble and run sondes without sticking the string. |
| `Technical Element Set` → Well Logging Practice → Drilling Rig | Plant creating the borehole the sondes travel. |
| `Technical Element Set` → Well Logging Practice → Borehole | The open hole exposing the formation to measurement. |
| `Technical Element Set` → Well Logging Practice → `Technical Interface & Actuation` | Grouping: the motoric boundary into the hole. |
| `Technical Element Set` → Well Logging Practice → `Technical Interface & Actuation` → Logging Winch | Controlled cable payout setting logging speed. |
| `Technical Element Set` → Well Logging Practice → `Technical Interface & Actuation` → Logging Cable | Armored conductor lowering sondes and carrying signals up. |
| `Technical Element Set` → Well Logging Practice → Resistivity Sonde | Tool transducing formation resistivity. |
| `Technical Element Set` → Well Logging Practice → Gamma-Ray Sonde | Tool transducing natural radioactivity. |
| `Technical Element Set` → Well Logging Practice → Sonic Sonde | Tool transducing acoustic transit time. |
| `Technical Element Set` → Well Logging Practice → Density Sonde | Tool transducing bulk density via gamma scattering. |
| `Technical Element Set` → Well Logging Practice → `Technical Interface` | Grouping: boundaries exchanging matter, energy, information. |
| `Technical Element Set` → Well Logging Practice → `Technical Interface` → Sonde–Formation Coupling | Acoustic and electrical contact between tool and borehole wall. |
| `Technical Element Set` → Well Logging Practice → `Technical Interface` → Surface Recording Unit | Acquisition system digitizing and depth-indexing the signals. |
| `Technical Element Set` → Well Logging Practice → `Technical Standard` | Grouping: normative specifications. |
| `Technical Element Set` → Well Logging Practice → `Technical Standard` → Sonde Calibration | Shop and in-hole calibration against reference blocks. |
| `Technical Element Set` → Well Logging Practice → `Technical Standard` → Depth Control | Cable-stretch correction tying samples to true depth. |
| `Technical Element Set` → Well Logging Practice → `Technical Parameter` | Grouping: variables controlling the run. |
| `Technical Element Set` → Well Logging Practice → `Technical Parameter` → Logging Speed | Hoist rate trading vertical resolution against stick risk. |
| `Technical Element Set` → Well Logging Practice → `Technical Quality` | Grouping: measured qualities of the run. |
| `Technical Element Set` → Well Logging Practice → `Technical Quality` → Repeat-Section Agreement | Overlap-logged interval quantifying precision. |

Tree 2 — the end (epistemicarum grammar): the same operation read as inquiry. The boundary
between the trees runs between executing the observation and warranting its product.

| Instance Tree Path | Description | Epistemic Category | Epistemic Element Type Tree Path |
| --- | --- | --- | --- |
| Formation Evaluation | The inquiry the logging run serves: what lies underground. | Target | `(root) := <<Epistemic Element>> >  Domain Concrete Epistemic Artifact Set (DCESA)` |
| Formation Evaluation → `Observation Interface` | Grouping: the transduction chain into persistent artifacts. | Access | `(root) := <<Epistemic Element>> >  Observation Interface` |
| Formation Evaluation → `Observation Interface` → Resistivity Transduction | Conversion of formation conductivity into measurable current. | Access | `(root) := <<Epistemic Element>> >  Observation Interface > Transduction` |
| Formation Evaluation → `Observation Interface` → Depth Sampling | Discrete registrations of the continuous formation flux. | Access | `(root) := <<Epistemic Element>> >  Observation Interface > Sampling` |
| Formation Evaluation → `Observation Interface` → Signal Quantization | Mapping of samples onto finite digital values. | Access | `(root) := <<Epistemic Element>> >  Observation Interface > Quantization` |
| Formation Evaluation → `Observation Interface` → LAS Encoding | Conversion of registered signals into storable log files. | Access | `(root) := <<Epistemic Element>> >  Observation Interface > Observation Encoding` |
| Formation Evaluation → Gamma-Ray Log Curve | Depth-indexed radioactivity track; shale indicator. | Representation | `(root) := <<Epistemic Element>> >  Concrete Epistemic Artifact` |
| Formation Evaluation → Resistivity Log Curve | Depth-indexed resistivity track; hydrocarbon indicator. | Representation | `(root) := <<Epistemic Element>> >  Concrete Epistemic Artifact` |
| Formation Evaluation → Porosity Cross-Plot | Joint density–neutron reading warranting porosity claims. | Representation | `(root) := <<Epistemic Element>> >  Concrete Epistemic Artifact` |
| Formation Evaluation → `Epistemic Standard` | Grouping: criteria judging the artifacts. | Validation | `(root) := <<Epistemic Element>> >  Epistemic Standard` |
| Formation Evaluation → `Epistemic Standard` → Extraction Confirmation | Later production or coring confirming (or refuting) the reading. | Validation | `(root) := <<Epistemic Element>> >  Epistemic Standard` |
| Formation Evaluation → `Epistemic Standard` → Run Reproducibility | Repeat-section and offset-well agreement. | Validation | `(root) := <<Epistemic Element>> >  Epistemic Standard` |

## References

- Ambiguity Resolution (`guideline/ambiguity_resolution.md`) (canonical case, multi-root forest rule)
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md) (Tree 1 grammar, CRM case-study style)
- [Philosophia Artium Epistemicarum et Operis](note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md) (Tree 2 grammar, Observation Interface, DCESA)
- https://en.wikipedia.org/wiki/Well_logging
