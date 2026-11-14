---
tags: [note, experiment, method]
order: 0
---

# Experimental Method

> An **experimental method** is a generalized routine by which inquiry makes a system produce observations on purpose — the reproducible order of acts that selects a part of the world, imposes a condition on it, and registers what follows.

> The method is neither the design that allocates conditions nor the instrument that imposes them: the design says which condition goes where, the instrument is what the condition is made to hold through, and the method is the routine that turns the one into the other.

## Formulation

### What is this epistemic instance?

> The method scope of experimental science: the routines by which a system is made to yield observations, gathered as one catalogue and filed by **what the routine does to the system** — impose a state, remove a part, read a state without imposing one, or prepare the system so that any of the three can be done at all.

> The corpus divides the work along this boundary. The material side stays in [data collection](/view.html?p=notes/epistemica/data/data-collection.md): the inventory of collection techniques, the [allocation of conditions](/view.html?p=notes/epistemica/data/experimental-design.md), and the [dated cases](/corpus/notes/epistemica/data/natural-science-data-collection-experimentation.csv). The identification reading — what an intervention licenses you to conclude — stays in the [causality scope](/view.html?p=notes/epistemica/causality/randomized-controlled-trial-rct.md), with the randomized trial and the do-calculus. What is left, and what this scope holds, is the routine itself: the means by which a condition is made to hold, independently of who runs it and on what.

> A method prescribes acts and never contains them. The bearer of a method is an activity — one run, one session, one campaign — and the acts are recorded on the activity's node, not on the method's. That is why one method appears under many activities, and why an experiment is not a method: the *Michelson–Morley experiment* is a dated activity, *interferometry* is the routine it applied.

### What epistemic element type does this epistemic instance belong to?

> Primary type: `Aggregate` — the guide's `Epistemic Element Set` — whose members are `Epistemic Method`s. The chain that places it is `Epistemic Practice (→ Has) Epistemic Activity (→ Has) Epistemic Method`: the practice is the discipline that carries the routine (biological, physical, chemical sciences), the activity is the run, and the method is the reproducible order of acts the run applies. The root type is declared once, and the branches below are read as elements of inquiry.

> `readable as` an `Epistemic Protocol` when the routine is written down as a prescribed course rather than performed; `readable as` an `Epistemic Infrastructure` when attention falls on the instruments, preparations and facilities a routine presupposes.

> The schema is owned by the canonical [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md).

### Is the type of this `epistemic element instance` ambiguous?

> Yes, in five ways the decomposition keeps apart.

> Against a **design**: the design decides which condition is applied to which unit, in what order and how many times — the [experimental-design](/view.html?p=notes/epistemica/data/experimental-design.md) note owns it. The method decides how a condition is made to hold once the design has placed it. A badly designed good method and a well-designed bad method fail differently.

> Against an **instrument**: the microscope, the laser and the electrode are `Epistemic Tool`s, carried under the infrastructure lane. The method is the order of acts that works through them; changing the instrument does not change the method, changing the order of acts does.

> Against a **case**: an experiment is a dated instance with its own history, accident and interpretation. The corpus keeps those separately, in the [natural-science collection](/corpus/notes/epistemica/data/natural-science-data-collection-experimentation.csv), and this scope keeps what recurs across them.

> Against a **principle**: a principle directs inquiry without prescribing an order of acts — *strong inference* says to devise alternative hypotheses and kill them, while the control condition that makes the killing possible is a standard of the method. The [principle scope](/view.html?p=notes/epistemica/principle.md) owns the directives; this scope owns the routines that satisfy them.

> Against a **technical practice**: the same routine, read as a way of producing an effect rather than of learning one, belongs to the technica corpus as a `Technique`. Optogenetics is the clean case — a biotechnical technique there, an epistemic method here — and the two notes decompose the same activity along different axes: the device chain there, the order of inquiry acts here.

> One gap is worth recording rather than hiding. The guide's `<<Action Element>>` slot admits Inference, Observation, Measurement, Classification, Computation and Comparison — and no type for **intervention**. A perturbation is an act of the method, but the act vocabulary has no seat for "impose a state". The tables therefore type the acts that surround the intervention (observation, measurement) and name the intervention among the method's parts. Whether the slot should be widened is a schema decision taken in the guide, not a filing decision taken here.

### What is the recursive instance decomposition of this epistemic instance?

> Four families do something to the system, one prepares it: **perturbation** imposes a state, **stimulation** excites tissue without naming a population, **ablation** removes a part, **recording** and **imaging** read a state, and **preparation** makes the system accessible at all. A routine that does two things sits in the family that names its principal move.

> Three lanes carry what every routine needs regardless of family: the **access** through which the condition is imposed and the response registered, the **infrastructure** of implements and preparations, and the **evaluation** that decides whether the run supports its conclusion. The evaluation lane is where the scope earns its keep, because an experiment's warrant is carried by its controls, not by its apparatus.

> The controls are invariant across families and are stated once here rather than re-derived in every method note: a **sham** condition (the manipulation's form without its content — light without opsin, opsin without light), a **negative control** (handling without manipulation), the **specificity** of the imposed condition (the state is imposed on the intended part and no other), **dosimetry** (the imposed quantity stays inside the declared range), and **pre-registration** (the analysis fixed before the run). A method note cites this spine; a method note that redefines it is a method note to distrust.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Experimental Method Set | The catalogue of the routines by which a system is made to yield observations on purpose. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` | Grouping: the routines themselves, filed by what each does to the system under study. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Perturbation Method | Grouping: routines that impose a state on a defined part of the system. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Perturbation Method → [Optogenetics](/view.html?p=notes/epistemica/experimental-method/optogenetics.md) | Drive or silence a genetically named cell population with light; the perturbation is specific in cell type and precise in time. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Perturbation Method → Chemogenetic Method | Impose a state by a designer receptor activated by an inert ligand; slower and more diffuse than light, but durable and less invasive. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Perturbation Method → Genetic Perturbation Screen | Remove or force the expression of genes across a library of targets and read which ones change the phenotype. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Stimulation Method | Grouping: routines that excite tissue without naming which cells inside it are driven. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Stimulation Method → Electrical Microstimulation | Pass current through an electrode; the classic perturbation, spatially coarse and blind to cell type. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Stimulation Method → Sensory Stimulation | Present a controlled stimulus to a sense organ and read the response it evokes. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Ablation Method | Grouping: routines that remove a part and read what the system can no longer do. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Ablation Method → Lesion Study | Destroy a region and compare the behaviour with intact controls; irreversible, and blind to fibres passing through. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Ablation Method → Reversible Inactivation | Silence a region temporarily — cooling, local anaesthetic, inhibitory infusion — so that each subject is its own control. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Recording Method | Grouping: routines that register a state without imposing one on the system. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Recording Method → Electrophysiology | Register the electrical activity of cells or membranes, at spike or at channel resolution. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Recording Method → Calcium Imaging | Register fluorescence from a calcium indicator as a proxy for population activity. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Recording Method → Behavioural Assay | Register what the whole organism does, under a protocol that fixes the task and the measurement. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Imaging Method | Grouping: routines that resolve structure, and now function, in space. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Imaging Method → Two-Photon Microscopy | Excite fluorescence only at the focus, so that scattering tissue can be read to depth. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Imaging Method → Confocal Microscopy | Reject out-of-focus light through a pinhole; shallow, sharp, and cheap. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Imaging Method → Electron Microscopy | Resolve structure below the diffraction limit, at the cost of fixing and sectioning the specimen. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Preparation Method | Grouping: routines that make the system accessible before any of the others can run. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Preparation Method → Acute Slice Preparation | Keep a live slice for hours; access without a whole organism, at the cost of severed connections. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Preparation Method → Awake Preparation | Implant and habituate the subject so that the measurement survives without anaesthesia. |
| `Aggregate` → Experimental Method Set → `Epistemic Method` → Preparation Method → Anaesthetised Preparation | Suppress movement and pain so that a long or invasive procedure can be run; the anaesthetic is itself a perturbation. |
| `Aggregate` → Experimental Method Set → `Epistemic Access` | Grouping: the interfaces through which the condition is imposed and the response registered. |
| `Aggregate` → Experimental Method Set → `Epistemic Access` → `Observation Interface` | Grouping: the boundary mechanisms coupling the system to the registration. |
| `Aggregate` → Experimental Method Set → `Epistemic Access` → `Observation Interface` → Stimulus Interface | Where the imposed condition enters — light path, electrode, pipette, sensory apparatus. |
| `Aggregate` → Experimental Method Set → `Epistemic Access` → `Observation Interface` → Registration Interface | Where the response is transduced into a signal — amplifier, photodetector, camera. |
| `Aggregate` → Experimental Method Set → `Epistemic Access` → `Observation Encoding` | Grouping: the format in which the registration is carried. |
| `Aggregate` → Experimental Method Set → `Epistemic Access` → `Observation Encoding` → Trace Record | A continuous signal over time — voltage, current, intensity. |
| `Aggregate` → Experimental Method Set → `Epistemic Access` → `Observation Encoding` → Event Record | Discrete occurrences with times — spikes, licks, responses, trials. |
| `Aggregate` → Experimental Method Set → `Epistemic Access` → `Observation Encoding` → Image Stack | A spatially resolved array over time, read as frames or volumes. |
| `Aggregate` → Experimental Method Set → `Epistemic Infrastructure` | Grouping: what the routines are run with. |
| `Aggregate` → Experimental Method Set → `Epistemic Infrastructure` → `Epistemic Tool` | Grouping: the implements that extend what the experimenter can do. |
| `Aggregate` → Experimental Method Set → `Epistemic Infrastructure` → `Epistemic Tool` → Actuator | The implement that imposes the condition — laser, LED, stimulator, syringe pump, viral vector. |
| `Aggregate` → Experimental Method Set → `Epistemic Infrastructure` → `Epistemic Tool` → Sensor | The implement that registers — electrode, photodiode, camera, force transducer. |
| `Aggregate` → Experimental Method Set → `Epistemic Infrastructure` → `Epistemic Tool` → Preparation Apparatus | The implement that makes the system accessible — stereotaxic frame, microtome, incubator, surgical rig. |
| `Aggregate` → Experimental Method Set → `Epistemic Evaluation` | Grouping: what decides whether the run supports its conclusion. |
| `Aggregate` → Experimental Method Set → `Epistemic Evaluation` → `Epistemic Standard` | Grouping: the norms an experimental run is held to. |
| `Aggregate` → Experimental Method Set → `Epistemic Evaluation` → `Epistemic Standard` → Sham Control | The manipulation's form without its content: light without opsin, opsin without light, surgery without the implant. |
| `Aggregate` → Experimental Method Set → `Epistemic Evaluation` → `Epistemic Standard` → Negative Control | Handling and time without manipulation, so that the preparation itself is not the effect. |
| `Aggregate` → Experimental Method Set → `Epistemic Evaluation` → `Epistemic Standard` → Perturbation Specificity | The condition is imposed on the intended part and no other — the standard that separates a targeted method from a coarse one. |
| `Aggregate` → Experimental Method Set → `Epistemic Evaluation` → `Epistemic Standard` → Dosimetry | The imposed quantity stays inside the declared range, so that the effect is attributable to the manipulation and not to its excess. |
| `Aggregate` → Experimental Method Set → `Epistemic Evaluation` → `Epistemic Standard` → Pre-registration | The analysis is fixed before the run, so that the reported comparison is the one designed and not the one that survived. |
| `Aggregate` → Experimental Method Set → `Epistemic Guidance` | Grouping: the directives under which a run is laid out. |
| `Aggregate` → Experimental Method Set → `Epistemic Guidance` → `Epistemic Protocol` | Grouping: the prescribed course a routine is written as. |
| `Aggregate` → Experimental Method Set → `Epistemic Guidance` → `Epistemic Protocol` → Experimental Protocol | The written order of preparation, manipulation, registration and analysis for one class of run. |

### What is a critical conceptual evaluation of this `epistemic element instance`?

> **Verdicts.** Conceptual Identification — **pass**: the method is separated from the design, the instrument, the case, the principle and the technical reading, and the separations are each carried by a different note. Definitional Clarity — **pass**: the definition names the selection, the imposition and the registration, and the axis of filing. Conceptual Determinacy — **partial**: the boundary to observation is one of degree, since every registration imposes conditions too (a slice is cut, a subject is restrained); the note fixes it by declaring the *imposed condition* the criterion, which is determinate in use but not in the abstract. Internal Consistency — **pass with a recorded gap**: the guide's action slot has no `Intervention`, so a perturbation cannot be typed as an act; the note names the gap instead of inventing a type. Representational Adequacy — **pass**: five families, three lanes and the controls spine cover what the routines are and what holds them to account. Purpose Adequacy — **pass**: the decomposition supports selecting a method, stating its controls, and separating the method's warrant from its apparatus.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Identification** | Pass | Method, design, instrument, case, principle and technical reading are kept apart, each with its own home in the corpus. |
| **Definitional Clarity** | Pass | Selection, imposition and registration are named, and the filing axis — what the routine does to the system — is stated. |
| **Conceptual Determinacy** | Partial | Every registration imposes conditions too, so the line to observation is one of degree; the declared criterion is the *imposed* condition, which is determinate per method but not universally. |
| **Internal Consistency** | Pass | The families partition by principal move and the lanes recur across them; the missing `Intervention` act type is recorded as a schema gap rather than patched locally. |
| **Representational Adequacy** | Pass | Five families, three lanes and one shared controls spine cover the routines, their interfaces and their warrant. |
| **Purpose Adequacy** | Pass | Supports choosing a method, stating its controls, separating warrant from apparatus, and filing a new routine without a new scope. |

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) (schema owner)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md) (evaluation criteria)
- [Data Collection](/view.html?p=notes/epistemica/data/data-collection.md) — the inventory of collection techniques this scope's routines produce material for.
- [Experimental Design](/view.html?p=notes/epistemica/data/experimental-design.md) — the allocation of conditions, which this scope does not own.
- [Natural Science: Data Collection & Experimentation](/corpus/notes/epistemica/data/natural-science-data-collection-experimentation.csv) — the dated cases the routines recur across.
- [Randomized Controlled Trial (RCT)](/view.html?p=notes/epistemica/causality/randomized-controlled-trial-rct.md) and [Do-Calculus](/view.html?p=notes/epistemica/causality/do-calculus.md) — the identification reading of an intervention.
- [Biological Sciences](/view.html?p=notes/epistemica/epistemic/discipline/biological-sciences.md) — the practice that carries most of these routines.
- Hacking, I. (1983). *Representing and Intervening: Introductory Topics in the Philosophy of Natural Science*. Cambridge University Press.
- Franklin, A. (1986). *The Neglect of Experiment*. Cambridge University Press.
- Mayo, D. G. (1996). *Error and the Growth of Experimental Knowledge*. University of Chicago Press.
- Fisher, R. A. (1935). *The Design of Experiments*. Oliver & Boyd.
- Platt, J. R. (1964). Strong inference. *Science*, 146(3642), 347–353. https://doi.org/10.1126/science.146.3642.347

## Related

- [Optogenetics](/view.html?p=notes/epistemica/experimental-method/optogenetics.md) — the perturbation exemplar: the first method note in this scope.
- [Mathematical Method](/view.html?p=notes/epistemica/mathematical/method/method.md) — the sibling scope note, filed by what the routine does to the problem.
- [Experimental Design](/view.html?p=notes/epistemica/data/experimental-design.md) — the design side of the same boundary.
- [Calibration](/view.html?p=notes/epistemica/validation/calibration.md) — instrument calibration, which readies a method's implements without being one.
