---
tags: [note, geotechnical-engineering, civil-engineering, earth-science, construction]
---

# Geotechnical Engineering

> Geotechnical engineering is the technical practice that turns the ground into a construction material, a support and a container: it investigates what is there, models what it will do, designs the intervention that will make it carry, hold or contain, builds that intervention under control, and reads the ground's response back into the model.

> Its modern form begins with Coulomb's and Rankine's earth-pressure theories, Darcy's law for seepage and Atterberg's limits for soil consistency. Karl Terzaghi's *Erdbaumechanik* (1925) made the subject calculable by stating the effective-stress principle and the consolidation equation; *Theoretical Soil Mechanics* (1943) consolidated bearing capacity, settlement and stability into the design canon; Peck's observational method (1969) made monitoring a licensed part of design. Critical-state soil mechanics, numerical analysis, geosynthetics, offshore geotechnics and reliability-based design extended that canon without changing its warrant: the design is judged by the measured performance of the site.

## Formulation

### What technical element type does this technical instance belong to?

**Geotechnical engineering belongs to the `Technical Practice` technical element type — a repeatable, organized pattern of technical work integrating activities, techniques, principles, standards and tools.**

```text
Technical Element
└── Technical Practice
    └── Geotechnical Engineering (readable as Technical Element Set)
```

It is a practice because it is a standing way of working — investigate, model, design, build under control, monitor — not a single technique or a single object. It is readable as a `Technical Element Set` because together with the practice come the research field, the standards and code committees, the laboratories and consultancies, and the tooling it carries.

The root type is not ambiguous. Soil and rock mechanics are `Technical Research`: they produce the knowledge the practice applies and are not re-typed here as member practices. The ground itself is not a technical element of this note — the soil, rock and water are read under the naturalis grammar; what is decomposed here is the practice that acts on them. Member practices — foundation, retaining structures, earthworks, ground improvement, geosynthetics, offshore, earthquake, geoenvironmental — are exercises of the same practice on different works, not separate roots.

Read under the epistemicarum grammar, the same body of work is an `Epistemic Practice`, the organized inquiry into the engineering behaviour of earth materials. That reading is recorded as prose, not as a second type: this note decomposes the transformation.

### What is this technical instance?

> Geotechnical engineering is the practice that owns the ground as a technical object. It fixes the soil, rock, groundwater, proposed structure and construction sequence as its segment; registers the ground by borehole, in-situ test, laboratory test, geophysical survey and monitoring; represents it as a stratigraphic model, a parameter set and a constitutive or limit-equilibrium model; designs the foundation, earthwork, retaining structure, tunnel or containment that will carry, hold or contain; controls the ground's response during construction; and validates its predictions against settlement records, pore-pressure readings, load tests, back-analysis and observed performance. Its outputs are a ground model, a design, a specification and a monitoring record; its warrant is agreement with the measured behaviour of the site and with the standards of practice, not derivation from first principles alone.

Boundaries: **earth science** explains what the ground is and how it came to be; geotechnical engineering decides what the ground will do under a proposed load, cut or flow. **Structural engineering** owns the superstructure and its load path; geotechnical engineering owns the ground and its interaction with the structure, from foundation to slope to excavation. **Construction management** owns who builds, in what order and at what cost; geotechnical engineering owns the ground's response to that sequence. **Mining and petroleum engineering** extract resources and borrow geotechnical analysis; here the root is the ground as a support, not the resource. The soil/rock and onshore/offshore divisions are divisions of the segment, not second types.

Verbs: a drilling rig, a piezometer or an analysis code *implements* the technique it carries; a built foundation, embankment or tunnel lining *realizes* the design; the practice *produces* the ground model, the design and the monitoring record.

### What is the recursive instance decomposition of this technical instance?

> Boundary: this table decomposes one practice instance — geotechnical engineering as organized technical work — into its purposes, problems, ground model and parameters, constraints, resources, requirements, standards, research, principles, frameworks, strategies, institutions, agents, technique chains, interfaces, architecture, blueprints, evaluations, feedback, hazards, risks, failures, maintenance, lifecycle and built works. The natural ground is not decomposed here; it belongs to the naturalis grammar.
>
> Stopping rule: a row is terminal when it names a concrete instrument, test, standard, role, technique, act, record, institution, failure or built object. No branch is grown into the naturalis or social grammar.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a tool, standard or instrument *implements* the technique it carries; a built foundation, embankment or tunnel lining *realizes* the design; the practice *produces* the ground model, the design and the monitoring record.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Practice` → Geotechnical Engineering | The technical practice that investigates, models, designs, builds and monitors the ground as a construction material, support and container. |
| `Technical Practice` → Geotechnical Engineering → `Technical Purpose` | Grouping: the purposes the practice is constituted to serve. |
| `Technical Practice` → Geotechnical Engineering → `Technical Purpose` → Predict Ground Performance | Predict how the ground will deform, settle, seep or fail under a proposed load, cut or flow. |
| `Technical Practice` → Geotechnical Engineering → `Technical Purpose` → Design Ground Support | Design foundations, retaining structures, tunnels and earthworks that carry the load and stay serviceable. |
| `Technical Practice` → Geotechnical Engineering → `Technical Purpose` → Control Construction Effect | Control the ground's response during excavation, dewatering, compaction and loading. |
| `Technical Practice` → Geotechnical Engineering → `Technical Purpose` → Manage Geotechnical Risk | Identify, quantify and reduce the risk of ground-related failure. |
| `Technical Practice` → Geotechnical Engineering → `Technical Problem` | Grouping: the discrepancies between a current or projected ground state and the desired state. |
| `Technical Practice` → Geotechnical Engineering → `Technical Problem` → Bearing Capacity Problem | The ground may fail beneath the foundation pressure before the structure is served. |
| `Technical Practice` → Geotechnical Engineering → `Technical Problem` → Settlement Problem | The ground may deform under load beyond what the structure tolerates. |
| `Technical Practice` → Geotechnical Engineering → `Technical Problem` → Slope Stability Problem | A natural or constructed slope may fail along a slip surface. |
| `Technical Practice` → Geotechnical Engineering → `Technical Problem` → Seepage Problem | Water flow may soften, erode or destabilise the ground and flood the works. |
| `Technical Practice` → Geotechnical Engineering → `Technical Problem` → Excavation Stability Problem | An excavation or tunnel may close, heave, or move the ground around it. |
| `Technical Practice` → Geotechnical Engineering → `Technical Domain Reality Model` | Grouping: the operative model of the ground the practice works in. |
| `Technical Practice` → Geotechnical Engineering → `Technical Domain Reality Model` → Ground Model | The site's operative model: stratal geometry, material parameters, groundwater regime and stated uncertainty. |
| `Technical Practice` → Geotechnical Engineering → `Technical Domain Reality Model` → Ground Model → `Technical Parameter` | Grouping: the parameters that characterize the ground model. |
| `Technical Practice` → Geotechnical Engineering → `Technical Domain Reality Model` → Ground Model → `Technical Parameter` → Effective Stress | Total stress minus pore pressure: the stress that governs strength and deformation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Domain Reality Model` → Ground Model → `Technical Parameter` → Undrained Shear Strength | The shear strength of saturated fine-grained soil under undrained loading. |
| `Technical Practice` → Geotechnical Engineering → `Technical Domain Reality Model` → Ground Model → `Technical Parameter` → Effective Friction Angle | The friction component of the drained shear-strength envelope. |
| `Technical Practice` → Geotechnical Engineering → `Technical Domain Reality Model` → Ground Model → `Technical Parameter` → Coefficient of Permeability | The ground's capacity to transmit water under a hydraulic gradient. |
| `Technical Practice` → Geotechnical Engineering → `Technical Domain Reality Model` → Ground Model → `Technical Parameter` → SPT Blow Count | N-value: blows to drive the standard sampler 300 mm, corrected for energy and overburden. |
| `Technical Practice` → Geotechnical Engineering → `Technical Domain Reality Model` → Ground Model → `Technical Parameter` → CPT Tip Resistance | qc: the cone tip resistance measured by the piezocone. |
| `Technical Practice` → Geotechnical Engineering → `Technical Domain Reality Model` → Stratigraphic Model | Layers, lenses and weathering profiles correlated between investigation points. |
| `Technical Practice` → Geotechnical Engineering → `Technical Domain Reality Model` → Groundwater Regime | Water table, piezometric heads, flow paths and seasonal variation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Domain Reality Model` → Rock Mass Model | Intact rock, discontinuities, weathering and the mass classification of the site. |
| `Technical Practice` → Geotechnical Engineering → `Technical Constraint` | Grouping: the bounds on what the practice may do. |
| `Technical Practice` → Geotechnical Engineering → `Technical Constraint` → Site Access Constraint | The investigation and the works must reach the ground through existing structures, utilities and traffic. |
| `Technical Practice` → Geotechnical Engineering → `Technical Constraint` → Ground Condition Constraint | The site strata, water and obstructions bound what can be built and how. |
| `Technical Practice` → Geotechnical Engineering → `Technical Constraint` → Construction Tolerance Constraint | Adjacent structures and services set the admissible ground movement. |
| `Technical Practice` → Geotechnical Engineering → `Technical Constraint` → Regulatory Consent Constraint | Permits, environmental consents and code approvals bound the intervention. |
| `Technical Practice` → Geotechnical Engineering → `Technical Resource` | Grouping: the inputs the practice consumes. |
| `Technical Practice` → Geotechnical Engineering → `Technical Resource` → Investigation Crew | Drillers, technicians and surveyors who execute the investigation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Resource` → Laboratory Capacity | The testing slots, apparatus and calibration the test programme consumes. |
| `Technical Practice` → Geotechnical Engineering → `Technical Resource` → Monitoring Instrument Pool | The piezometers, inclinometers, extensometers and settlement plates available to a project. |
| `Technical Practice` → Geotechnical Engineering → `Technical Requirement` | Grouping: the formalized desired states the intervention must satisfy. |
| `Technical Practice` → Geotechnical Engineering → `Technical Requirement` → Ultimate Limit State Requirement | The design must resist bearing failure, sliding, overturning, uplift and structural collapse with the required margin. |
| `Technical Practice` → Geotechnical Engineering → `Technical Requirement` → Serviceability Limit State Requirement | The design must keep settlement, differential movement and vibration within the structure's tolerance. |
| `Technical Practice` → Geotechnical Engineering → `Technical Requirement` → Monitoring Requirement | The construction must be observed at stated intervals against stated trigger values. |
| `Technical Practice` → Geotechnical Engineering → `Technical Specification` | Grouping: the statements of requirement, method and acceptance the works are held to. |
| `Technical Practice` → Geotechnical Engineering → `Technical Specification` → Ground Investigation Specification | The scope, methods, spacing, depths and reporting required of the investigation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Specification` → Earthworks Specification | The materials, compaction, moisture and acceptance testing required of fill and cut. |
| `Technical Practice` → Geotechnical Engineering → `Technical Specification` → Piling Specification | The pile type, dimensions, materials, installation and testing acceptance criteria. |
| `Technical Practice` → Geotechnical Engineering → `Technical Standard` | Grouping: the normative specifications governing the practice. |
| `Technical Practice` → Geotechnical Engineering → `Technical Standard` → Eurocode 7 | EN 1997: the European geotechnical design standard, with its design approaches and partial factors. |
| `Technical Practice` → Geotechnical Engineering → `Technical Standard` → ASTM D2487 | The unified soil classification standard. |
| `Technical Practice` → Geotechnical Engineering → `Technical Standard` → BS 5930 | The British code of practice for site investigation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Standard` → AASHTO LRFD | The US load-and-resistance-factor bridge design specifications, including foundations. |
| `Technical Practice` → Geotechnical Engineering → `Technical Research` | Grouping: the systematic investigation that produces the knowledge the practice applies. |
| `Technical Practice` → Geotechnical Engineering → `Technical Research` → Soil Mechanics | The research field of soil strength, stiffness, consolidation, seepage and critical state. |
| `Technical Practice` → Geotechnical Engineering → `Technical Research` → Rock Mechanics | The research field of rock strength, deformation, discontinuity behaviour and rock mass classification. |
| `Technical Practice` → Geotechnical Engineering → `Technical Research` → Critical State Soil Mechanics | The framework in which soil tends to a unique critical state at large strain. |
| `Technical Practice` → Geotechnical Engineering → `Technical Research` → Constitutive Modelling | The research field of stress–strain models for soil and rock. |
| `Technical Practice` → Geotechnical Engineering → `Technical Principle` | Grouping: the general rules governing construction and operation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Principle` → Effective Stress Principle | Deformation and strength are governed by the intergranular stress, not the total stress. |
| `Technical Practice` → Geotechnical Engineering → `Technical Principle` → Drainage Condition Principle | The drained or undrained reading is chosen from the relative rate of loading and drainage. |
| `Technical Practice` → Geotechnical Engineering → `Technical Principle` → Mohr–Coulomb Failure Principle | Shear failure occurs when the stress state reaches the strength envelope. |
| `Technical Practice` → Geotechnical Engineering → `Technical Principle` → Darcy's Law | Seepage velocity is proportional to hydraulic gradient through permeability. |
| `Technical Practice` → Geotechnical Engineering → `Technical Principle` → Consolidation Principle | Excess pore pressure dissipates with time, producing time-dependent settlement. |
| `Technical Practice` → Geotechnical Engineering → `Technical Principle` → Critical State Principle | Soil tends toward a unique critical state at large strain, independent of its initial state. |
| `Technical Practice` → Geotechnical Engineering → `Technical Principle` → Limit Equilibrium Principle | Stability is judged by comparing driving and resisting actions on a postulated mechanism. |
| `Technical Practice` → Geotechnical Engineering → `Technical Framework` | Grouping: the overarching logics that structure the technical problem. |
| `Technical Practice` → Geotechnical Engineering → `Technical Framework` → Observational Framework | Predict, monitor, compare and revise the design or construction as the ground reveals itself. |
| `Technical Practice` → Geotechnical Engineering → `Technical Framework` → Load and Resistance Factor Design | Design by factored loads and factored resistances rather than a single global factor of safety. |
| `Technical Practice` → Geotechnical Engineering → `Technical Framework` → Performance-Based Design | Design against a stated performance under a stated ground motion or loading, rather than prescriptive rules. |
| `Technical Practice` → Geotechnical Engineering → `Technical Strategy` | Grouping: the context-sensitive regimes for planning and sequencing the work. |
| `Technical Practice` → Geotechnical Engineering → `Technical Strategy` → Class-A Prediction Strategy | State the prediction before construction so that monitoring can test it. |
| `Technical Practice` → Geotechnical Engineering → `Technical Strategy` → Staged Investigation Strategy | Increase investigation detail as the design decision and the ground's variability require. |
| `Technical Practice` → Geotechnical Engineering → `Technical Strategy` → Trigger-Value Strategy | Fix measurable thresholds and pre-planned responses before construction begins. |
| `Technical Practice` → Geotechnical Engineering → `Technical Institution` | Grouping: the durable social structures that organize the practice. |
| `Technical Practice` → Geotechnical Engineering → `Technical Institution` → ISSMGE | The International Society for Soil Mechanics and Geotechnical Engineering: congresses, technical committees and guidance. |
| `Technical Practice` → Geotechnical Engineering → `Technical Institution` → CEN | The European Committee for Standardization, which owns Eurocode 7. |
| `Technical Practice` → Geotechnical Engineering → `Technical Institution` → Professional Institution | The body that accredits engineers, publishes guidance and reviews practice. |
| `Technical Practice` → Geotechnical Engineering → `Technical Institution` → Licensing Board | The statutory body that licenses the practice of engineering. |
| `Technical Practice` → Geotechnical Engineering → `Technical Agent` | Grouping: the entities that execute the practice. |
| `Technical Practice` → Geotechnical Engineering → `Technical Agent` → Geotechnical Engineer | Owns the ground model, the design and the performance prediction. |
| `Technical Practice` → Geotechnical Engineering → `Technical Agent` → Engineering Geologist | Reads the site's geology and supplies the geological ground model. |
| `Technical Practice` → Geotechnical Engineering → `Technical Agent` → Driller | Advances the boreholes, recovers the samples and installs the instruments. |
| `Technical Practice` → Geotechnical Engineering → `Technical Agent` → Laboratory Technician | Prepares the specimens, runs the tests and maintains the calibration. |
| `Technical Practice` → Geotechnical Engineering → `Technical Agent` → Contractor | Executes excavation, compaction, piling, dewatering and ground improvement. |
| `Technical Practice` → Geotechnical Engineering → `Technical Agent` → Asset Owner | Sets the performance requirement and accepts the residual risk. |
| `Technical Practice` → Geotechnical Engineering → `Technical Labor` | Grouping: the purposive effort the practice expends. |
| `Technical Practice` → Geotechnical Engineering → `Technical Labor` → Drilling Labour | The physical work of advancing boreholes, recovering samples and installing instruments. |
| `Technical Practice` → Geotechnical Engineering → `Technical Labor` → Testing Labour | The physical work of specimen preparation, test execution and calibration. |
| `Technical Practice` → Geotechnical Engineering → `Technical Labor` → Monitoring Labour | The physical work of reading, servicing and maintaining instruments on site. |
| `Technical Practice` → Geotechnical Engineering → `Technical Competence` | Grouping: the acquired capacities the practice requires. |
| `Technical Practice` → Geotechnical Engineering → `Technical Competence` → Geotechnical Design Competence | The acquired capacity to turn a ground model into a checked design. |
| `Technical Practice` → Geotechnical Engineering → `Technical Competence` → Site Investigation Competence | The acquired capacity to plan, execute and interpret an investigation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Competence` → Numerical Analysis Competence | The acquired capacity to build and judge a numerical ground model. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` | Grouping: the discrete units of planned work, each owning a technique chain. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task | The planned work of characterizing the ground before design. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` | Grouping: generalized methods for the investigation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Desk Study | Assemble the maps, archives and precedent that frame what the ground may be. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Desk Study → Archive and Map Review | The desk study applied to one site and its records. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Desk Study → Archive and Map Review → Collect the Historical Maps | Retrieve the geological, topographical and historical maps of the site. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Desk Study → Archive and Map Review → Read the Geological Map | Read the mapped strata, faults and former land uses against the proposed works. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Borehole Drilling | Advance a borehole to sample, test and instrument the ground at depth. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Borehole Drilling → Rotary Core Drilling | The drilling method applied where continuous rock or soil core is required. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Borehole Drilling → Rotary Core Drilling → Advance the Borehole | Turn the bit and circulate the flushing medium down the hole. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Borehole Drilling → Rotary Core Drilling → Recover the Core | Retrieve the core barrel and extract the run. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Borehole Drilling → Cable-Percussion Drilling | The drilling method applied where disturbed samples and penetration tests suffice. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Borehole Drilling → Cable-Percussion Drilling → Drive the Casing | Advance the casing to support the hole through unstable ground. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Cone Penetration Testing | Push an instrumented cone to measure resistance and pore pressure continuously. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Cone Penetration Testing → Piezocone Test | The cone test applied with pore-pressure measurement at the site. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Cone Penetration Testing → Piezocone Test → Push the Cone | Drive the cone at the standard rate through the profile. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Cone Penetration Testing → Piezocone Test → Record the Tip Resistance | Log tip resistance, sleeve friction and pore pressure against depth. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Standard Penetration Testing | Drive a split sampler to record blow count and recover a disturbed sample. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Standard Penetration Testing → SPT at the Borehole Base | The penetration test applied at the base of an open borehole. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Standard Penetration Testing → SPT at the Borehole Base → Drive the Sampler | Drop the hammer through the standard fall onto the sampler. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Standard Penetration Testing → SPT at the Borehole Base → Count the Blows | Count the blows for each 150 mm of penetration. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Geophysical Surveying | Image the subsurface from surface or borehole by physical contrast. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Geophysical Surveying → Seismic Refraction Line | The seismic method applied along a survey line over the site. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Geophysical Surveying → Seismic Refraction Line → Lay the Geophone Line | Place the receivers at the designed spacing along the line. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Geophysical Surveying → Seismic Refraction Line → Fire the Source | Strike the source and record the arrivals at each receiver. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Groundwater Monitoring | Observe the water table and piezometric heads through installed access. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Groundwater Monitoring → Standpipe Installation | The monitoring well applied to the borehole response zone. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Groundwater Monitoring → Standpipe Installation → Install the Response Zone | Set the filter and seal the standpipe at the target stratum. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Site Investigation Task → `General Technique` → Groundwater Monitoring → Standpipe Installation → Measure the Water Level | Lower the dipper and record the standing level against the datum. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task | The planned work of measuring ground properties on recovered samples. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` | Grouping: generalized methods for laboratory testing. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Classification Testing | Index the soil by grading, plasticity and unit weight. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Classification Testing → Atterberg Limits Test | The classification test applied to the fine fraction of the sample. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Classification Testing → Atterberg Limits Test → Sieve the Sample | Separate the fractions by sieve and record the grading curve. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Classification Testing → Atterberg Limits Test → Roll the Thread | Roll the fines at decreasing water content to the plastic limit. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Triaxial Shear Testing | Measure strength and stiffness under controlled confining stress. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Triaxial Shear Testing → CU Triaxial Test | The triaxial test applied with consolidation and no drainage during shear. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Triaxial Shear Testing → CU Triaxial Test → Consolidate the Specimen | Bring the specimen to the target effective stress before shear. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Triaxial Shear Testing → CU Triaxial Test → Shear the Specimen | Advance the axial strain and record the deviator stress and pore pressure. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Oedometer Consolidation Testing | Measure one-dimensional compressibility and consolidation rate. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Oedometer Consolidation Testing → Oedometer Test | The consolidation test applied to the specimen in the ring. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Oedometer Consolidation Testing → Oedometer Test → Load the Specimen | Apply the stress increments and record the settlement against time. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Permeability Testing | Measure the coefficient of permeability of the sample. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Permeability Testing → Falling Head Test | The permeability test applied to the low-permeability specimen. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Laboratory Testing Task → `General Technique` → Permeability Testing → Falling Head Test → Measure the Flow | Record the head drop against time through the specimen. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task | The planned work of turning the ground model into a checked intervention. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` | Grouping: generalized methods for analysis and design. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Bearing Capacity Analysis | Compare the applied foundation pressure with the ground resistance. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Bearing Capacity Analysis → Terzaghi Bearing Capacity Check | The bearing analysis applied with the classical mechanism and factors. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Bearing Capacity Analysis → Terzaghi Bearing Capacity Check → Compute the Ultimate Bearing Pressure | Evaluate the capacity from cohesion, surcharge, unit weight and footing geometry. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Settlement Analysis | Predict the deformation the foundation load will produce. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Settlement Analysis → Oedometer-Based Settlement Prediction | The settlement analysis applied to the compressible stratum. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Settlement Analysis → Oedometer-Based Settlement Prediction → Compute the Consolidation Settlement | Integrate the strain over the influence depth from the compression parameters. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Limit Equilibrium Slope Analysis | Compare driving and resisting actions on postulated slip surfaces. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Limit Equilibrium Slope Analysis → Bishop Simplified Analysis | The limit equilibrium method applied to the slope section. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Limit Equilibrium Slope Analysis → Bishop Simplified Analysis → Assign the Slip Surface | Define the circular or non-circular surface to be tested. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Limit Equilibrium Slope Analysis → Bishop Simplified Analysis → Compute the Factor of Safety | Iterate the resisting and driving moments until the ratio converges. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Seepage Analysis | Compute the flow field and pore pressures through the ground. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Seepage Analysis → Flow Net Construction | The seepage analysis applied as a graphical flow net. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Seepage Analysis → Flow Net Construction → Sketch the Flow Lines | Draw the equipotentials and flow lines to satisfy the boundary conditions. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Finite Element Analysis | Discretize the ground and structure to compute stress and deformation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Finite Element Analysis → Staged Construction Analysis | The numerical method applied to the construction sequence. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Analysis and Design Task → `General Technique` → Finite Element Analysis → Staged Construction Analysis → Apply the Excavation Stage | Remove the excavated elements and re-equilibrate the model. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task | The planned work of building the intervention within admissible ground response. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` | Grouping: generalized methods for construction control. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` → Excavation Support | Hold the sides of an excavation while the permanent works are built. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` → Excavation Support → Sheet-Pile Wall Installation | The support method applied as a driven sheet-pile wall. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` → Excavation Support → Sheet-Pile Wall Installation → Drive the Sheet Pile | Advance the interlocking sheet to the design toe level. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` → Dewatering | Lower the water table and control pore pressure around the works. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` → Dewatering → Wellpoint Dewatering | The dewatering method applied as a pumped wellpoint array. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` → Dewatering → Wellpoint Dewatering → Pump the Drawdown | Run the pumps and hold the drawdown at the design level. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` → Compaction | Reduce voids in the fill to achieve the specified density. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` → Compaction → Vibratory Compaction | The compaction method applied with a vibrating roller. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` → Compaction → Vibratory Compaction → Roll the Compactor | Pass the roller over the layer at the specified amplitude and coverage. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` → Grouting | Inject a binder to fill voids, seal seepage or densify the ground. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` → Grouting → Permeation Grouting | The grouting method applied to the pore space of the ground. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Control Task → `General Technique` → Grouting → Permeation Grouting → Inject the Grout | Pump the mix at the controlled pressure and record the take. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Monitoring Task | The planned work of reading the ground response against the prediction. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Monitoring Task → `General Technique` | Grouping: generalized methods for monitoring. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Monitoring Task → `General Technique` → Inclinometer Monitoring | Measure lateral ground movement with depth. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Monitoring Task → `General Technique` → Inclinometer Monitoring → Inclinometer Reading | The inclinometer method applied to an installed casing. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Monitoring Task → `General Technique` → Inclinometer Monitoring → Inclinometer Reading → Lower the Probe | Pass the probe down the casing to the base. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Monitoring Task → `General Technique` → Inclinometer Monitoring → Inclinometer Reading → Read the Profile | Record the inclinations on the way up on both axes. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Monitoring Task → `General Technique` → Piezometer Monitoring | Measure pore pressure at a point in the ground. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Monitoring Task → `General Technique` → Piezometer Monitoring → Piezometer Reading | The piezometer method applied to the installed sensor. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Monitoring Task → `General Technique` → Piezometer Monitoring → Piezometer Reading → Read the Piezometer | Record the pressure head against the datum and the time. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Monitoring Task → `General Technique` → Settlement Surveying | Measure the vertical movement of the ground or the structure. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Monitoring Task → `General Technique` → Settlement Surveying → Settlement Plate Survey | The survey method applied to installed settlement plates. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Monitoring Task → `General Technique` → Settlement Surveying → Settlement Plate Survey → Survey the Point | Level the plate against the reference benchmark. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Investigation Campaign | The planned work of one characterized campaign: borings, in-situ tests, geophysics and laboratory work. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Investigation Campaign → Drill the Borehole | Advance the borehole to the target depth for the campaign. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Investigation Campaign → Log the Strata | Record each stratum, sample and test against depth. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Investigation Campaign → Sample the Ground | Recover the representative samples the test programme requires. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Observation Round | The recurring planned work in which instruments are read, compared with the prediction and answered. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Observation Round → Take the Scheduled Reading | Read the instrument at the scheduled interval. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Observation Round → Compare Reading with Prediction | Set the reading against the predicted value and the trigger value. |
| `Technical Practice` → Geotechnical Engineering → `Technical Task` → Construction Observation Round → Issue the Response | Decide and record the action the observation requires. |
| `Technical Practice` → Geotechnical Engineering → `Constitutive Technique` | Grouping: techniques embodied in the practice that establish its internal operating logic. |
| `Technical Practice` → Geotechnical Engineering → `Constitutive Technique` → Ground Model Construction | The technique of turning investigation data into a parameterized ground model. |
| `Technical Practice` → Geotechnical Engineering → `Constitutive Technique` → Limit-State Design Logic | The technique of checking each failure mode against its limit state and partial factors. |
| `Technical Practice` → Geotechnical Engineering → `Constitutive Technique` → Observational Control Loop | The technique of closing prediction, monitoring and revision into one operating loop. |
| `Technical Practice` → Geotechnical Engineering → `Technical Interface & Actuation` | Grouping: the boundaries and means through which the practice acts on the ground. |
| `Technical Practice` → Geotechnical Engineering → `Technical Interface & Actuation` → Borehole | The drilled interface through which the ground is sampled, tested and instrumented. |
| `Technical Practice` → Geotechnical Engineering → `Technical Interface & Actuation` → Cone Penetrometer | The pushed probe that measures tip resistance, sleeve friction and pore pressure. |
| `Technical Practice` → Geotechnical Engineering → `Technical Interface & Actuation` → Pile | The deep interface that transfers structural load to bearing strata. |
| `Technical Practice` → Geotechnical Engineering → `Technical Interface & Actuation` → Ground Anchor | The tensioned interface that holds a retaining structure into the ground. |
| `Technical Practice` → Geotechnical Engineering → `Technical Interface & Actuation` → Geotextile | The planar interface that separates, filters, drains or reinforces the ground. |
| `Technical Practice` → Geotechnical Engineering → `Technical Interface & Actuation` → Grout Port | The injection interface through which grout enters the ground. |
| `Technical Practice` → Geotechnical Engineering → `Technical Interface & Actuation` → Instrument | The sensing interface: piezometer, inclinometer, extensometer or settlement plate. |
| `Technical Practice` → Geotechnical Engineering → `Technical Architecture` | Grouping: the structural organization of the practice. |
| `Technical Practice` → Geotechnical Engineering → `Technical Architecture` → Investigate–Model–Design–Construct–Monitor Chain | The operating architecture: characterize the ground, model it, design the intervention, build it and read the performance back. |
| `Technical Practice` → Geotechnical Engineering → `Technical Architecture` → Design Check Hierarchy | The arrangement of ultimate and serviceability checks per failure mode and partial factor. |
| `Technical Practice` → Geotechnical Engineering → `Technical Architecture` → Monitoring Feedback Loop | The arrangement in which readings return to the model, the design and the construction sequence. |
| `Technical Practice` → Geotechnical Engineering → `Technical Blueprint` | Grouping: the generative descriptions prescribing how to create or configure the works. |
| `Technical Practice` → Geotechnical Engineering → `Technical Blueprint` → Ground Investigation Plan | The planned locations, depths, methods and tests of the investigation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Blueprint` → Ground Model Report | The written ground model: stratigraphy, parameters, groundwater and uncertainty. |
| `Technical Practice` → Geotechnical Engineering → `Technical Blueprint` → Geotechnical Design Report | The design basis, ground model, analyses, checks and residual risk. |
| `Technical Practice` → Geotechnical Engineering → `Technical Blueprint` → Monitoring Plan | The instruments, locations, frequencies, trigger values and planned responses. |
| `Technical Practice` → Geotechnical Engineering → `Technical Configuration` | Grouping: the arrangements determining the operational state. |
| `Technical Practice` → Geotechnical Engineering → `Technical Configuration` → Design Parameter Set | The characteristic and design values chosen for each ground property. |
| `Technical Practice` → Geotechnical Engineering → `Technical Configuration` → Partial Factor Set | The code's factors applied to actions, resistances and parameters. |
| `Technical Practice` → Geotechnical Engineering → `Technical Configuration` → Construction Sequence Configuration | The staged order and rates of excavation, support, dewatering and filling. |
| `Technical Practice` → Geotechnical Engineering → `Technical Dependency` | Grouping: the relations in which one element requires another. |
| `Technical Practice` → Geotechnical Engineering → `Technical Dependency` → Design Depends on Investigation | The design cannot exceed the ground model the investigation supports. |
| `Technical Practice` → Geotechnical Engineering → `Technical Dependency` → Construction Depends on Dewatering | Excavation stability depends on the drawdown and discharge being maintained. |
| `Technical Practice` → Geotechnical Engineering → `Technical Interaction` | Grouping: the relations through which elements affect one another. |
| `Technical Practice` → Geotechnical Engineering → `Technical Interaction` → Ground–Structure Interaction | The load path and the ground's response determine each other. |
| `Technical Practice` → Geotechnical Engineering → `Technical Interaction` → Adjacent Construction Interaction | New excavation, loading or dewatering changes the ground under neighbouring structures. |
| `Technical Practice` → Geotechnical Engineering → `Technical Interaction` → Groundwater–Structure Interaction | Pore pressure acts on the structure and the structure alters the flow. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evaluation` | Grouping: the checks that judge conformity and purpose. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evaluation` → `Verification` | Grouping: evaluation of whether the work conforms to its specification and drawings. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evaluation` → `Verification` → Design Verification | Each failure mode is checked against its limit state and the governing code's partial factors. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evaluation` → `Verification` → Pile Integrity Test | A low-strain sonic test checking the pile's continuity and section against the specification. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evaluation` → `Verification` → Earthworks Acceptance Testing | Density, moisture and gradation tests checking the compacted fill against the earthworks specification. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evaluation` → `Validation` | Grouping: evaluation of whether the work fulfils its intended purpose. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evaluation` → `Validation` → Back-Analysis | Observed performance inverted to test the ground model and the design assumptions. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evaluation` → `Validation` → Performance Monitoring | The built structure's long-term movement and pore pressure read against the design intent. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evaluation` → `Validation` → Observational Validation | The observational method's comparison of prediction and measurement as the ground is exposed. |
| `Technical Practice` → Geotechnical Engineering → `Technical Feedback` | Grouping: the information about intervention effects that enables adjustment. |
| `Technical Practice` → Geotechnical Engineering → `Technical Feedback` → Monitoring Trigger | A threshold exceedance returned to the observer as a required action. |
| `Technical Practice` → Geotechnical Engineering → `Technical Feedback` → Design Revision | A monitoring or back-analysis result returned to the design as a required change. |
| `Technical Practice` → Geotechnical Engineering → `Technical Feedback` → Construction Adjustment | An observed deviation returned to the construction sequence as a required change. |
| `Technical Practice` → Geotechnical Engineering → `Technical Feedback` → Parameter Update | A back-analysed value returned to the ground model and the design parameter set. |
| `Technical Practice` → Geotechnical Engineering → `Technical Hazard` | Grouping: the conditions capable of producing a harmful outcome. |
| `Technical Practice` → Geotechnical Engineering → `Technical Hazard` → Liquefaction | Saturated loose sand losing strength under cyclic loading. |
| `Technical Practice` → Geotechnical Engineering → `Technical Hazard` → Sinkhole | A cavity or void collapsing into the ground surface. |
| `Technical Practice` → Geotechnical Engineering → `Technical Hazard` → Slope Failure Hazard | A slope whose driving forces may exceed its resistance. |
| `Technical Practice` → Geotechnical Engineering → `Technical Hazard` → Piping | Internal erosion carrying fines along a seepage path. |
| `Technical Practice` → Geotechnical Engineering → `Technical Risk` | Grouping: the possibility and consequence of an undesirable outcome under uncertainty. |
| `Technical Practice` → Geotechnical Engineering → `Technical Risk` → Settlement Damage Risk | The possibility and consequence of the structure being damaged by ground movement. |
| `Technical Practice` → Geotechnical Engineering → `Technical Risk` → Excavation Collapse Risk | The possibility and consequence of an excavation or its support failing. |
| `Technical Practice` → Geotechnical Engineering → `Technical Risk` → Contaminated Ground Risk | The possibility and consequence of contaminant exposure or migration. |
| `Technical Practice` → Geotechnical Engineering → `Technical Trade-off` | Grouping: the relations in which improving one objective constrains another. |
| `Technical Practice` → Geotechnical Engineering → `Technical Trade-off` → Safety–Cost Trade-off | More investigation, support and monitoring buy margin at cost. |
| `Technical Practice` → Geotechnical Engineering → `Technical Trade-off` → Stiffness–Drainage Trade-off | A stiffer support attracts more load; drainage relieves pressure but removes ground. |
| `Technical Practice` → Geotechnical Engineering → `Technical Trade-off` → Speed–Monitoring Trade-off | Faster construction reduces cost but shortens the observation window. |
| `Technical Practice` → Geotechnical Engineering → `Technical Failure` | Grouping: the states in which the work fails to perform its required function. |
| `Technical Practice` → Geotechnical Engineering → `Technical Failure` → Bearing Capacity Failure | The ground shears and the foundation sinks or tilts. |
| `Technical Practice` → Geotechnical Engineering → `Technical Failure` → Excessive Settlement | The ground deforms beyond the structure's serviceability limit. |
| `Technical Practice` → Geotechnical Engineering → `Technical Failure` → Piping Failure | Seepage erodes a continuous channel through the ground. |
| `Technical Practice` → Geotechnical Engineering → `Technical Failure` → Support Failure | A retaining structure or excavation support yields, overturns or collapses. |
| `Technical Practice` → Geotechnical Engineering → `Technical Maintenance` | Grouping: the activity that preserves or restores functional state. |
| `Technical Practice` → Geotechnical Engineering → `Technical Maintenance` → Slope Drainage Maintenance | Clearing and repairing drains, ditches and weep holes on slopes. |
| `Technical Practice` → Geotechnical Engineering → `Technical Maintenance` → Anchor Re-Tensioning | Restoring the design load in ground anchors after lock-off loss. |
| `Technical Practice` → Geotechnical Engineering → `Technical Maintenance` → Monitoring Network Upkeep | Servicing, recalibrating and replacing instruments over the asset's life. |
| `Technical Practice` → Geotechnical Engineering → `Technical Lifecycle` | Grouping: the temporal trajectory of the works. |
| `Technical Practice` → Geotechnical Engineering → `Technical Lifecycle` → Investigation–Design–Construction Lifecycle | The trajectory from desk study to as-built record and operation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Lifecycle` → Asset Operation Phase | The long service period in which monitoring and maintenance preserve performance. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evolution` | Grouping: the historical change in the practice and its knowledge. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evolution` → Coulomb and Rankine Earth Pressure | Coulomb's 1773 wedge analysis and Rankine's 1857 stress theory of earth pressure on retaining walls. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evolution` → Terzaghi's Erdbaumechanik | The 1925 statement of the effective-stress principle and the consolidation equation that made the subject calculable. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evolution` → Theoretical Soil Mechanics | The 1943 consolidation of bearing capacity, settlement and stability into the design canon. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evolution` → Observational Method | Peck's 1969 statement of prediction, monitoring and revision as a licensed part of design. |
| `Technical Practice` → Geotechnical Engineering → `Technical Evolution` → Eurocode 7 Adoption | The 2004 European limit-state code, with its design approaches and partial factors, replacing national factor-of-safety practice. |
| `Technical Practice` → Geotechnical Engineering → `Technical Obsolescence` | Grouping: the condition in which an approach loses viability relative to alternatives. |
| `Technical Practice` → Geotechnical Engineering → `Technical Obsolescence` → Global Factor of Safety | The single-factor stability measure superseded in code design by partial factors. |
| `Technical Practice` → Geotechnical Engineering → `Technical Obsolescence` → Empirical Foundation Rule | Pre-modern sizing rules superseded by effective-stress analysis and testing. |
| `Technical Practice` → Geotechnical Engineering → `Technical Capability` | Grouping: the value-producing possibilities the practice enables. |
| `Technical Practice` → Geotechnical Engineering → `Technical Capability` → Ground Prediction Capability | The capability to predict the ground's response to a proposed intervention. |
| `Technical Practice` → Geotechnical Engineering → `Technical Capability` → Ground Control Capability | The capability to hold the ground's response within admissible limits. |
| `Technical Practice` → Geotechnical Engineering → `Technical Mechanism` | Grouping: the arrangements through which a transformation is produced. |
| `Technical Practice` → Geotechnical Engineering → `Technical Mechanism` → Consolidation | Pore-pressure dissipation driving time-dependent settlement. |
| `Technical Practice` → Geotechnical Engineering → `Technical Mechanism` → Seepage | Groundwater flow through pores and discontinuities under a hydraulic gradient. |
| `Technical Practice` → Geotechnical Engineering → `Technical Mechanism` → Shear Failure | Sliding of a ground mass once the stress state reaches the strength envelope. |
| `Technical Practice` → Geotechnical Engineering → `Technical Mechanism` → Densification | Void reduction by compaction, vibration or consolidation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Property` | Grouping: the characteristics attributable to the ground. |
| `Technical Practice` → Geotechnical Engineering → `Technical Property` → Shear Strength | The ground's resistance to shearing, expressed by cohesion and friction. |
| `Technical Practice` → Geotechnical Engineering → `Technical Property` → Compressibility | The ground's change in volume under a change in stress. |
| `Technical Practice` → Geotechnical Engineering → `Technical Property` → Permeability | The ground's capacity to transmit water. |
| `Technical Practice` → Geotechnical Engineering → `Technical Property` → Stiffness | The ground's resistance to strain under stress. |
| `Technical Practice` → Geotechnical Engineering → `Technical Quality` | Grouping: the degree to which desirable properties are possessed. |
| `Technical Practice` → Geotechnical Engineering → `Technical Quality` → Investigation Coverage | How fully the investigation samples the ground's variability. |
| `Technical Practice` → Geotechnical Engineering → `Technical Quality` → Design Robustness | How little the design's performance depends on the uncertain parameters. |
| `Technical Practice` → Geotechnical Engineering → `Technical Quality` → Construction Workmanship | How faithfully the built work matches the specification. |
| `Technical Practice` → Geotechnical Engineering → `Technical Performance` | Grouping: the quantitative behaviour realized under specified conditions. |
| `Technical Practice` → Geotechnical Engineering → `Technical Performance` → Predicted Settlement | The computed deformation at the structure's foundation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Performance` → Factor of Safety | The ratio of resisting to driving actions for a failure mode. |
| `Technical Practice` → Geotechnical Engineering → `Technical Performance` → Pore Pressure Response | The measured or computed pore-pressure change under load or drawdown. |
| `Technical Practice` → Geotechnical Engineering → `Technical Practice` | Grouping: the member practices that exercise geotechnical engineering on particular works. |
| `Technical Practice` → Geotechnical Engineering → `Technical Practice` → Foundation Engineering | The member practice of footings, piles, rafts and caissons. |
| `Technical Practice` → Geotechnical Engineering → `Technical Practice` → Retaining Structure Engineering | The member practice of walls, sheet piles, anchors and reinforced soil. |
| `Technical Practice` → Geotechnical Engineering → `Technical Practice` → Earthworks Engineering | The member practice of cut, fill, compaction and construction dewatering. |
| `Technical Practice` → Geotechnical Engineering → `Technical Practice` → Ground Improvement | The member practice of densification, consolidation, grouting and reinforcement. |
| `Technical Practice` → Geotechnical Engineering → `Technical Practice` → Geosynthetics Engineering | The member practice of geotextiles, geogrids and geomembranes in separation, reinforcement, drainage and containment. |
| `Technical Practice` → Geotechnical Engineering → `Technical Practice` → Offshore Geotechnical Engineering | The member practice of seabed foundations, anchors, pipelines and offshore site investigation. |
| `Technical Practice` → Geotechnical Engineering → `Technical Practice` → Geotechnical Earthquake Engineering | The member practice of ground motion, liquefaction and seismic stability. |
| `Technical Practice` → Geotechnical Engineering → `Technical Practice` → Geoenvironmental Engineering | The member practice of contaminated ground, waste containment and groundwater protection. |
| `Technical Practice` → Geotechnical Engineering → `Production Technical System` | Grouping: the organized site that turns the ground into supported, retained or contained ground. |
| `Technical Practice` → Geotechnical Engineering → `Production Technical System` → Geotechnical Construction Site | The organized site in which investigation, earthworks, foundation and support works interact to deliver the built ground. |
| `Technical Practice` → Geotechnical Engineering → `Production Technical System` → Geotechnical Construction Site → `Producing Technical Element` | Grouping: the elements that transform reality itself into the delivered good. |
| `Technical Practice` → Geotechnical Engineering → `Production Technical System` → Geotechnical Construction Site → `Producing Technical Element` → Earthworks Producer | Transforms the ground by cut, fill, compaction and dewatering into the designed landform. |
| `Technical Practice` → Geotechnical Engineering → `Production Technical System` → Geotechnical Construction Site → `Producing Technical Element` → Foundation Producer | Transforms the ground by drilling, driving or pouring into a load-carrying foundation. |
| `Technical Practice` → Geotechnical Engineering → `Production Technical System` → Geotechnical Construction Site → `Production Technical Object` | Grouping: the built objects the site delivers. |
| `Technical Practice` → Geotechnical Engineering → `Production Technical System` → Geotechnical Construction Site → `Production Technical Object` → Foundation | The built footing, pile, raft or caisson transferring load to the ground. |
| `Technical Practice` → Geotechnical Engineering → `Production Technical System` → Geotechnical Construction Site → `Production Technical Object` → Retaining Wall | The built wall, sheet pile or reinforced-soil mass holding ground in place. |
| `Technical Practice` → Geotechnical Engineering → `Production Technical System` → Geotechnical Construction Site → `Production Technical Object` → Embankment | The built fill and its prepared foundation. |
| `Technical Practice` → Geotechnical Engineering → `Production Technical System` → Geotechnical Construction Site → `Production Technical Object` → Tunnel Lining | The built support of an underground opening. |

### What is a critical conceptual evaluation of this `technical element instance`?

> **Verdict.** Geotechnical engineering is a genuine technical practice with a sharp operative segment and a strong performance warrant, but a moderate conceptual boundary: its laws are borrowed from mechanics and geology, its constitutive models are site-specific idealizations, and its ground models are interpolations from sparse samples. It is not earth science, because it transforms rather than explains; not structural engineering, because it owns the ground rather than the superstructure; and not construction management, because it decides what the ground will do, not who builds it. Its principal limit is *predictive reach*: the ground model is only as good as the investigation that samples it, and the site's spatial variability, sampling disturbance and construction sequence exceed any single deterministic prediction. The observational method is the practice's distinctive technical response — where prediction outruns knowledge, it converts construction into a monitored operation with trigger values and a pre-planned response.

| Criterion | Verdict | Diagnostic Focus |
| --- | --- | --- |
| Conceptual Identification | Strong | Distinguished from earth science (explains the ground, does not transform it), from structural engineering (owns the superstructure, not the ground), and from construction management (owns the works, not the ground's response); the practice test is whether the element transforms the ground into a supported, retained or contained state. |
| Definitional Clarity | Strong | "Transforms the ground into a construction material, support and container" states the operation; "agreement with measured site performance and standards of practice" states the warrant. |
| Conceptual Determinacy | Moderate–Strong | Boundary rule: a claim is geotechnical iff it predicts, measures or controls the ground's response to a proposed load, cut, flow or construction sequence. Borderline cases — engineering geology, geoenvironmental engineering, offshore geotechnics — are placed by the decision they serve and the warrant they carry, not by subject matter alone. |
| Internal Consistency | Strong | Soil/rock and onshore/offshore are divisions of the segment, not of the type; one practice carries them; member practices do not claim separate warrants; research is typed as research, not as practice. |
| Representational Adequacy | Strong | The decomposition separates the ground model and its parameters from the techniques, the interfaces and the evaluations; borrowed principles are typed as principles, and built works as production objects. Predictive reach is the residual limit: a ground model interpolates from sparse boreholes. |
| Purpose Adequacy | Strong | Prediction, design, construction control and risk management are all served; the note never claims a ground model is a law or a code check is a proof. |

## References

- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md) (schema owner)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md) (evaluation criteria)
- [Earth Science](/view.html?p=notes/epistemica/epistemic/discipline/earth-science.md) — the neighbouring inquiry into the Earth as an object
- [Soil](/view.html?p=notes/nature/matter/geological/soil.md) — the natural reading of the material
- [Construction Technology](/view.html?p=notes/technica/general/cto/industry/construction-technology.md) — the construction methods this practice designs for
- [Construction Project System](/view.html?p=notes/technica/general/cto/industry/construction-project-system.md) — the delivery system the works belong to
- [EES](/view.html?p=notes/epistemica/ees.md) — the epistemic companion reading
- [Technica Atlas](/corpus/notes/technica/meta/atlas.html) — the forest this decomposition feeds
- https://en.wikipedia.org/wiki/Geotechnical_engineering
- Terzaghi, K. *Erdbaumechanik auf bodenphysikalischer Grundlage* (1925).
- Terzaghi, K. *Theoretical Soil Mechanics* (1943).
- Schofield, A. N., and Wroth, C. P. *Critical State Soil Mechanics* (1968).
- Peck, R. B. "Advantages and Limitations of the Observational Method in Applied Soil Mechanics." *Géotechnique* 19, no. 2 (1969): 171–187.
- EN 1997-1. *Eurocode 7: Geotechnical design — Part 1: General rules* (2004).
- Das, B. M. *Principles of Geotechnical Engineering*. Cengage Learning.
- Lancellotta, R. *Geotechnical Engineering*. Taylor & Francis.
- Clayton, C. R. I., Matthews, M. C., and Simons, N. E. *Site Investigation*. Blackwell.
