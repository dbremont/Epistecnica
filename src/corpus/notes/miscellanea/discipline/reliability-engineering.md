---
tags: [note, reliability-engineering, systems-engineering, quality, maintenance, discipline, technica]
---

# Reliability Engineering

> **Reliability engineering** is the technical practice that makes failure a design variable: it prevents the failures it can foresee, finds and corrects the causes of the ones that still occur, provides for tolerating the ones that remain, and estimates how long a new design will last before it is built. Its object of work is not the product but the *distribution of its life*.

> Its central quantity is the probability that an item performs its required function, under stated conditions, for a stated period. That definition is exact and its estimation is not: failure rates are the most uncertain parameters in a design, historical data are valid only for an identical design, process and duty, and a single MTBF number is a target, never a requirement. The practice is therefore mostly qualitative before it is quantitative — anticipate the mechanism, remove the stress, then measure what is left.

## Formulation

### What technical element type does this technical instance belong to?

**Reliability engineering belongs to the `Technical Practice` technical element type — a repeatable, organized pattern of technical work integrating tasks, techniques, standards, instruments and evaluations.**

It is a practice because it is a standing way of working — set the requirement, model the system, analyse the failure modes, test the design, monitor the field — not a single analysis or a single test. It is readable as a `Technical Element Set` because with the practice come the analysis methods, the test facilities, the standards and the failure-reporting system.

The root type is not ambiguous. **Quality engineering** owns conformance at the point of manufacture; **safety engineering** owns harm to people and the environment; **maintenance** owns the restoration of the item in service; **dependability** is the property the computational corpus attributes to a system, and reliability is one of its components. Reliability engineering owns the *lifetime distribution* and the programme that improves it.

### What is this technical instance?

> The practice that turns a product's required life into design constraints and evidence: it allocates a reliability requirement, models the system as blocks or trees, analyses how each part can fail and what that failure does, derates and margin the stresses, adds redundancy where a single failure is intolerable, tests the design until it fails so that the mechanism is learned, and follows the field to catch what the analyses missed. Its outputs are a reliability programme plan, a failure-mode record, an demonstrated life or failure rate, and a corrective-action log; its warrant is the field record, not the prediction.

### What is the recursive instance decomposition of this technical instance?

> Boundary: this table decomposes one practice instance — reliability engineering as organized technical work — into its purposes, problems, tasks, technique chain, instruments, standards, agents, constraints and evaluations. The product it acts on is decomposed in its own note; the statistics it uses belong to the mathematical domain.
>
> Stopping rule: a row is terminal when it names a concrete technique, standard, instrument, role, criterion or measured quantity.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a standard *implements* the technique it carries; a test facility *realizes* the test; the practice *produces* the requirement, the analysis record and the demonstrated life.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Practice` → Reliability Engineering | The practice that prevents, finds, tolerates and estimates failure over a stated life. |
| `Technical Practice` → Reliability Engineering → `Technical Purpose` | Grouping: the purposes the practice is constituted to serve. |
| `Technical Practice` → Reliability Engineering → `Technical Purpose` → Prevent Failure | Remove or reduce the likelihood of a failure before it can occur — the first priority, because it is the cheapest. |
| `Technical Practice` → Reliability Engineering → `Technical Purpose` → Find and Correct Causes | Diagnose the failures that still occur and remove their root cause. |
| `Technical Practice` → Reliability Engineering → `Technical Purpose` → Tolerate Residual Failures | Keep service when a failure happens whose cause cannot be removed. |
| `Technical Practice` → Reliability Engineering → `Technical Purpose` → Estimate Reliability | Put a number and a confidence on the life of a new or existing design. |
| `Technical Practice` → Reliability Engineering → `Technical Problem` | Grouping: the discrepancies between the required and the realized life. |
| `Technical Practice` → Reliability Engineering → `Technical Problem` → Random Failure | A failure whose time is not predictable from age — the constant-rate regime. |
| `Technical Practice` → Reliability Engineering → `Technical Problem` → Wear-Out | Degradation that accumulates until the item can no longer perform — the increasing-rate regime. |
| `Technical Practice` → Reliability Engineering → `Technical Problem` → Common-Cause Failure | One event defeats several redundant channels at once, so redundancy does not buy what it promised. |
| `Technical Practice` → Reliability Engineering → `Technical Problem` → Latent Failure | A failure present but undetected until a demand reveals it, so neither redundancy nor maintenance can act on it. |
| `Technical Practice` → Reliability Engineering → `Technical Problem` → Human Error | A failure introduced by design, manufacture, maintenance or operation rather than by the item's physics. |
| `Technical Practice` → Reliability Engineering → `Technical Task` | Grouping: the tasks the practice runs. |
| `Technical Practice` → Reliability Engineering → `Technical Task` → Specify the Reliability Requirement | Turn the availability need into design constraints a designer can design to and a test can verify. |
| `Technical Practice` → Reliability Engineering → `Technical Task` → Model the System | Represent the system as success paths or failure paths before any number is estimated. |
| `Technical Practice` → Reliability Engineering → `Technical Task` → Analyse Failure Modes | Enumerate how each part can fail, what it does, and how it is detected. |
| `Technical Practice` → Reliability Engineering → `Technical Task` → Test the Design | Run the design to failure under accelerated or representative stress to learn the mechanism and the life. |
| `Technical Practice` → Reliability Engineering → `Technical Task` → Monitor the Field | Collect field failures, classify their causes and feed the corrections back. |
| `Technical Practice` → Reliability Engineering → `General Technique` | Grouping: the generalized methods the tasks draw on. |
| `Technical Practice` → Reliability Engineering → `General Technique` → FMEA and FMECA | Enumerate failure modes, their effects and their severity, and rank them for action. |
| `Technical Practice` → Reliability Engineering → `General Technique` → Fault Tree Analysis | Decompose an undesired top event into the combinations of basic events that produce it. |
| `Technical Practice` → Reliability Engineering → `General Technique` → Reliability Block Diagram | Represent the system as series and parallel success paths and compute its reliability from the parts'. |
| `Technical Practice` → Reliability Engineering → `General Technique` → Life-Data and Weibull Analysis | Fit a life distribution to failure times to read the shape of the hazard — decreasing, constant or increasing. |
| `Technical Practice` → Reliability Engineering → `General Technique` → Accelerated Life Testing | Raise stress to compress time, then extrapolate to service conditions through a life–stress model. |
| `Technical Practice` → Reliability Engineering → `General Technique` → Derating | Operate a part below its rated stress so that the margin absorbs variation and degradation. |
| `Technical Practice` → Reliability Engineering → `General Technique` → Redundancy | Add parallel channels, and decide the detection and switching that make them real. |
| `Technical Practice` → Reliability Engineering → `General Technique` → Reliability-Centred Maintenance | Choose the maintenance task by the failure consequence and the detectable condition, not by the calendar. |
| `Technical Practice` → Reliability Engineering → `General Technique` → FRACAS | Failure reporting, analysis and corrective action: the loop that turns field data into design change. |
| `Technical Practice` → Reliability Engineering → `Constitutive Technique` | Grouping: the techniques embodied in the design itself. |
| `Technical Practice` → Reliability Engineering → `Constitutive Technique` → Fault-Tolerant Architecture | Redundancy, voting, isolation and fail-safe states built into the system's structure. |
| `Technical Practice` → Reliability Engineering → `Constitutive Technique` → Physics-of-Failure Margin | Design against the actual mechanism — fatigue, corrosion, creep, electromigration — with measured margin. |
| `Technical Practice` → Reliability Engineering → `Constitutive Technique` → Condition Monitoring | Sensors and inspection that make a latent failure detectable before it becomes functional. |
| `Technical Practice` → Reliability Engineering → `Production Instrument` | Grouping: the facilities the evidence is produced with. |
| `Technical Practice` → Reliability Engineering → `Production Instrument` → Environmental Chamber | Temperature, humidity and thermal-cycling stress at controlled and repeatable conditions. |
| `Technical Practice` → Reliability Engineering → `Production Instrument` → Vibration Table | Mechanical stress representative of transport and service vibration. |
| `Technical Practice` → Reliability Engineering → `Production Instrument` → HALT Rig | Highly accelerated life test: step stress until the design's operating and destruct limits are found. |
| `Technical Practice` → Reliability Engineering → `Production Instrument` → Burn-In Rack | Screens early-life failures out of a production lot before shipment. |
| `Technical Practice` → Reliability Engineering → `Technical Standard` | Grouping: the norms the practice works to. |
| `Technical Practice` → Reliability Engineering → `Technical Standard` → IEC 60300 | Dependability management — the programme-level standard for reliability, maintainability and availability. |
| `Technical Practice` → Reliability Engineering → `Technical Standard` → IEC 60812 | Failure modes and effects analysis procedure. |
| `Technical Practice` → Reliability Engineering → `Technical Standard` → IEC 61025 | Fault tree analysis procedure. |
| `Technical Practice` → Reliability Engineering → `Technical Standard` → IEC 61078 | Reliability block diagram procedure. |
| `Technical Practice` → Reliability Engineering → `Technical Standard` → MIL-STD-785 | The reliability programme for systems and equipment: tasks, evidence and reporting. |
| `Technical Practice` → Reliability Engineering → `Technical Standard` → IEEE 1332 | Reliability programme for electronic systems. |
| `Technical Practice` → Reliability Engineering → `Technical Standard` → ARP4761 | Aerospace guidelines for safety assessment — the reliability evidence a safety case consumes. |
| `Technical Practice` → Reliability Engineering → `Technical Agent` | Grouping: who runs the practice. |
| `Technical Practice` → Reliability Engineering → `Technical Agent` → Reliability Engineer | The agent who allocates the requirement, runs the analyses, designs the test and signs the demonstrated life. |
| `Technical Practice` → Reliability Engineering → `Technical Constraint` | Grouping: the bounds the practice works inside. |
| `Technical Practice` → Reliability Engineering → `Technical Constraint` → Failure-Data Scarcity | Few failures, inconsistent classification and censored lives bound what any estimate can claim. |
| `Technical Practice` → Reliability Engineering → `Technical Constraint` → Prediction Uncertainty | The failure rate is the most uncertain parameter in the design, and a small design change can move it by decades. |
| `Technical Practice` → Reliability Engineering → `Technical Constraint` → Cost of Over-Specification | Every margin, redundancy and test is bought; a requirement above the need is a cost with no benefit. |
| `Technical Practice` → Reliability Engineering → `Technical Evaluation` | Grouping: how the practice is judged. |
| `Technical Practice` → Reliability Engineering → `Technical Evaluation` → `Verification` | Grouping: conformance to the stated reliability requirement. |
| `Technical Practice` → Reliability Engineering → `Technical Evaluation` → `Verification` → Life-Test Demonstration | A test of stated duration and confidence that shows the required life or failure rate is met. |
| `Technical Practice` → Reliability Engineering → `Technical Evaluation` → `Validation` | Grouping: fitness of the achieved reliability in service. |
| `Technical Practice` → Reliability Engineering → `Technical Evaluation` → `Validation` → Field Reliability | The observed failure record in the actual duty, environment and maintenance regime. |

## Reliability Measures

| Measure | Definition | What it is for |
| --- | --- | --- |
| **Reliability function** $R(t)$ | Probability the item performs its required function for the interval $[0,t]$ under stated conditions | The object the practice designs to; $R(0)=1$, non-increasing. |
| **Failure rate** $\lambda(t)$ | Hazard: failures per unit time among the survivors at $t$ | The shape of the life distribution — decreasing, constant or increasing. |
| **MTTF / MTBF** | Mean time to failure / between failures | A single summary of a distribution; meaningful only with the distribution stated. |
| **Availability** | $A=\dfrac{\text{MTBF}}{\text{MTBF}+\text{MTTR}}$ (steady state) | The measure the operator actually buys; it mixes reliability with maintainability. |
| **Maintainability** | The distribution of repair time, summarized by MTTR | The half of availability that is usually easier and cheaper to improve. |
| **Mission reliability** | Probability of completing a stated mission without a failure that prevents it | The measure for one-shot and mission-critical systems, where availability is irrelevant. |
| **Basic reliability** | Failure rate counting all failures, including those repaired without operational effect | The logistics measure — spares, manpower and cost of ownership. |

> The **bathtub curve** — decreasing early-life rate, constant useful-life rate, increasing wear-out rate — is a model, not a law. Many electronic items show no early-life hump after burn-in, and some show no constant region at all. The practice reads the hazard shape from data and designs against the regime it finds; it does not assume the curve.

## Failure Regimes

| Regime | Hazard | Mechanism | Design response |
| --- | --- | --- | --- |
| **Early life** | Decreasing | Manufacturing defects, assembly damage, weak parts | Burn-in, screening, process control — remove the population, not the design. |
| **Useful life** | Constant (approximately) | Random overstress exceeding a variable strength | Derating, margin, redundancy, protection. |
| **Wear-out** | Increasing | Fatigue, corrosion, creep, wear, insulation ageing | Life limit, replacement interval, condition monitoring, material change. |
| **System-level** | Not a sum of parts | Common cause, latent failure, human error, software | Architecture — independence, detection, diversity, procedure. |

> Reliability is not only mathematics and statistics. The uncertainty in the parameters is often larger than the differences the calculation is asked to resolve, which is why the practice begins with the physics of failure and the failure mode, and uses the number as evidence rather than as proof.

## Analysis Techniques

| Technique | Question it answers | Input | Output |
| --- | --- | --- | --- |
| **FMEA / FMECA** | How can each part fail, what happens, and how bad is it? | Design or process description | Ranked failure modes with severity, occurrence and detection |
| **Fault tree** | Which combinations of basic events produce the undesired top event? | Top event, system logic | Boolean cut sets, qualitative and quantitative |
| **Reliability block diagram** | What system reliability follows from the parts' reliabilities and the success logic? | Success paths, part failure rates | System reliability, availability, criticality ranking |
| **Markov model** | How does the system move between working, degraded and failed states? | States, transition rates | State probabilities, availability, MTTF |
| **Life-data / Weibull analysis** | What is the shape of the life distribution, and which regime dominates? | Failure and censored times | Hazard shape, characteristic life, confidence bounds |
| **Accelerated life test** | What life at service stress follows from life at raised stress? | Life–stress model, test data | Extrapolated life with uncertainty |
| **HALT** | Where are the design's operating and destruct limits? | Step-stressed hardware | Margin to the limits, dominant weakness |
| **Derating and stress analysis** | Is the part operating inside a margin that absorbs variation? | Loads, ratings, environment | Stress ratios, parts to change |
| **RCM** | Which maintenance task is worth doing, on which item, at which interval? | Failure modes, consequences, detectability | Maintenance policy per item |
| **FRACAS** | What keeps failing in the field, and what was done about it? | Field failure reports | Corrective actions closed against causes |

## Requirements and Programme

> A reliability requirement is not a target number. A lone MTBF value cannot be allocated with confidence, cannot be verified until years of service have passed, and is falsified by the next design change. A usable requirement states the function, the duty and environment, the life, the confidence and the evidence that will demonstrate it — and it constrains the design, rather than merely accounting for it afterwards.

> The **reliability programme plan** fixes which tasks are done for this system, by whom, with what evidence, and at which gate. It is scaled to the consequence of failure: a safety-critical system carries formal hazard logs, independent review and verification testing; a consumer product may carry screening and field monitoring. The plan is approved with the resources to execute it, or it is a wish.

## Reliability, Quality and Safety

| Practice | Owns | Boundary |
| --- | --- | --- |
| **Reliability engineering** | The lifetime distribution and the programme that improves it | Begins where conformance ends: a unit can be perfectly built and still fail at an unacceptable rate. |
| **Quality engineering** | Conformance to specification at the point of manufacture, and process stability | Six Sigma reduces variation and defects; it does not by itself produce a life distribution. |
| **Safety engineering** | Harm to people, environment and property, and the safety case | Consumes reliability evidence (failure rates, common-cause analysis) but is judged by risk to people, not by uptime. |
| **Maintenance** | Restoring and preserving the item in service | Can realize the inherent reliability and no more; RCM is where the two practices meet. |

## What is a critical conceptual evaluation of this technical element instance?

The concept under evaluation is **Reliability Engineering**, defined above as *the practice that prevents, finds, tolerates and estimates failure over a stated life*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: the practice is separated from quality (conformance at manufacture), safety (harm), maintenance (restoration) and dependability (the computational property), and the separation is the one that matters — a conforming unit can still be unreliable. Definitional Clarity — **pass**: reliability, failure rate, availability and maintainability are defined operationally, and the note states that the number is an estimate with confidence rather than a property of the object alone. Conceptual Determinacy — **pass with qualification**: the boundary of "a failure" depends on the stated function and duty, so the same event is or is not a reliability failure according to a specification that must be fixed first; the note makes that dependence explicit instead of assuming it. Internal Consistency — **pass**: purposes, problems, tasks, techniques, instruments, standards and evaluations are distinct branches; the statistical theory stays in the mathematical domain. Representational Adequacy — **qualified**: complete for the programme and its evidence; the economics, the organisational culture and the software-reliability reading are linked rather than grown. Purpose Adequacy — **pass**: shaped for programme review — every leaf is a task, a method, a standard or a piece of evidence a gate can check.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Distinguished from quality engineering, safety engineering, maintenance and dependability; the conformance-versus-life boundary is stated. |
| Definitional Clarity | pass | Function, duty, life, confidence and evidence are the definition's terms; MTBF is presented as a summary, not the concept. |
| Conceptual Determinacy | pass (qualified) | What counts as a failure is fixed by the stated function and environment; the note states the dependence rather than hiding it. |
| Internal Consistency | pass | Purposes, problems, tasks, techniques, instruments, standards and evaluations are separate branches; statistics stay mathematical. |
| Representational Adequacy | qualified | Complete for the programme and its evidence; economics, culture and software reliability are links. |
| Purpose Adequacy | pass | Every leaf serves a programme gate, a design decision or a verification. |

## References

- https://en.wikipedia.org/wiki/Reliability_engineering
- https://en.wikipedia.org/wiki/Failure_rate
- https://en.wikipedia.org/wiki/Bathtub_curve
- https://en.wikipedia.org/wiki/Failure_mode_and_effects_analysis
- https://en.wikipedia.org/wiki/Fault_tree_analysis
- https://en.wikipedia.org/wiki/Reliability_centered_maintenance
- https://en.wikipedia.org/wiki/Accelerated_life_testing
- O'Connor, P. D. T., & Kleyner, A. (2012). *Practical reliability engineering* (5th ed.). Wiley. — the practice as a programme, with the estimation limits stated
- Nelson, W. (2004). *Accelerated testing: Statistical models, test plans, and data analyses*. Wiley. — the life–stress models behind the extrapolation
- Weibull, W. (1951). A statistical distribution function of wide applicability. *Journal of Applied Mechanics*, 18(3), 293–297. — the life distribution the hazard-shape reading comes from
- [Dependability](/view.html?p=notes/technica/computation/dependability.md) — reliability as a property of computational systems
- [Home Maintenance Practice](/view.html?p=notes/technica/production/industry/home-maintenance-practice.md) — the maintenance practice that realizes inherent reliability
- [Metrology Services](/view.html?p=notes/technica/production/industry/metrology-services.md) — the measurement that makes the evidence credible
- [Structural Mechanics](/view.html?p=notes/miscellanea/discipline/structural-mechanics.md) · [Stability Analysis](/view.html?p=notes/miscellanea/discipline/stability-analysis.md) — the limit-state practice whose failure modes reliability engineering quantifies
- [Product Safety](/corpus/notes/social/good/safety.html) — the hazard catalogue a reliability programme feeds
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) — the schema and the permitted link forms
- [Technica Atlas](/corpus/notes/technica/atlas.html) — the forest this decomposition feeds
