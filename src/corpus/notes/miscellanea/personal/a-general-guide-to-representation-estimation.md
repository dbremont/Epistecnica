---
tags: [note, guia]
---

# A General Guide to Representation & Estimation

**Contains:** [A Guide to Mathematical Problem-Solving](/view.html?p=notes/miscellanea/personal/a-guide-to-mathematical-problem-solving.md), [How to Study Quantum Mechanics?](/view.html?p=notes/miscellanea/personal/how-to-study-quantum-mechanics.md), [Section of Reality Template](/view.html?p=notes/miscellanea/personal/section-of-reality-template.md)

> This guide provides a method for model selection, a set of tools, and even case studies for modeling scientific and engineering systems.
> 

QA:

- Is **Intelligent Compression**?
- What is the Relation of **Theory and Empirics**?

## Index

## Guiding Framework

> How do we **think** and act **about** modelling?
> 

## Meta-Layer for Modelling Framework Selection

### Breviary

⇒ Capture the Problem Space.

⇒ Develop a checklist to evaluate the Modelling Framework.

### **Core Idea**

- **Ordinary flow:** *Modelling Problem* → *Pick a Modelling Framework* → *Build Model*
- **Improved flow with meta-layer:**
    
    *Modelling Problem* → **Meta-Framework Reasoning** → *Select Modelling Framework* → *Build Model*
    

The **meta-framework** is a **reflective tool** that:

- **Maps** problem characteristics to modelling framework capabilities.
- **Surfaces trade-offs** between possible frameworks.
- **Accounts for constraints** (data, computation, interpretability, theory, domain assumptions).
- **Considers meta-criteria** like robustness, extensibility, tractability, alignment with stakeholders, and epistemic soundness.

### **Why This Is Needed**

Without the meta-layer, model choice often:

- Defaults to familiarity or trend rather than suitability.
- Ignores mismatches between **problem ontology** and **framework ontology**.
- Misses opportunities for **framework hybrids** or **novel formulations**.
- Lacks an explicit record of the reasoning behind the choice.

### **Structure of the Meta-Framework**

| **Dimension** | **Questions in the Meta-Framework** | Instance(s) |
| --- | --- | --- |
| **Problem Ontology** | What is the nature of the entities, states, relations, and dynamics? | Continuous vs. discrete, deterministic vs. stochastic, spatial vs. aspatial |
| **Epistemic Access** | What can we observe, measure, or estimate? | Partial observability, noisy measurements, missing data |
| **Data–Model Fit** | How does available data map to model requirements? | Data sparsity vs. deep learning needs |
| **Computational Profile** | What are time/memory constraints? | Real-time processing vs. offline batch |
| **Stakeholder Needs** | Who consumes the model output and how? | Regulatory approval, interpretability for decision-makers |
| **Theory Integration** | How does existing domain theory interact with the model? | Physics-informed ML, agent-based economic models |
| **Tractability vs. Fidelity** | How much complexity is warranted? | Simplified analytical model vs. high-fidelity simulation |
| **Robustness** | How sensitive is the model to assumptions? | Bayesian model averaging, ensemble methods |
| **Adaptivity** | Can the framework evolve as the problem changes? | Online learning, modular simulation components |

### **Meta-Framework Workflow**

1. **Characterize the Problem Space:** Define scope, scale, entities, interactions, uncertainties.
2. **Define Success Criteria:** What counts as a “good” model here? Predictive accuracy? Theoretical insight? Policy impact?
3. **Map Problem Features to Framework Capabilities:** Use a **problem–framework compatibility matrix**.
4. **Evaluate Trade-offs:** Quantify or qualitatively score suitability of candidate frameworks.
5. **Select and Justify:** Document reasoning for reproducibility and stakeholder transparency.
6. **Monitor and Revisit:** Meta-framework remains “live”—adjust mapping when problem evolves.

### Problem–Framework Mapping Table

| **Dimension** | **Operational Definition** | **Problem Assessment** | **Framework Capability Match** |
| --- | --- | --- | --- |
| **Problem Ontology** | Nature of entities, states, relations, dynamics. | E.g., discrete agents, continuous fields, hybrid | Framework handles discrete, continuous, or hybrid structures? |
| **Causal & Structural Assumptions** | Level of determinism, causality structure, process topology. | E.g., deterministic PDEs, stochastic process, feedback loops | Framework supports required causality representation? |
| **Epistemic Access** | Observability, measurability, data coverage. | E.g., partial observations, noisy data, high-resolution time series | Framework tolerates data gaps, noise, and uncertainty? |
| **Data–Model Fit** | Alignment between data type/scale and model requirements. | E.g., tabular, spatial, network, temporal | Framework’s data interface compatible? Needs transformations? |
| **Temporal & Spatial Scales** | Relevant time horizons and spatial granularity. | E.g., real-time, daily aggregation; meters vs. kilometers | Framework matches resolution and multi-scale needs? |
| **Computational Profile** | Available compute/memory, latency tolerance. | E.g., HPC batch, edge processing, real-time | Framework feasible under constraints? |
| **Stakeholder Needs** | Decision context, interpretability, adoption constraints. | E.g., regulatory compliance, transparent logic | Framework meets interpretability/regulatory requirements? |
| **Theory Integration** | Need to incorporate domain laws/theories. | E.g., physics-informed constraints | Framework can integrate domain theory directly? |
| **Tractability vs. Fidelity** | Complexity acceptable vs. required accuracy. | E.g., minimal viable complexity, high-fidelity sim | Framework supports balancing tractability/fidelity? |
| **Robustness Requirements** | Sensitivity to assumption errors, parameter shifts. | E.g., high robustness needed for safety-critical system | Framework offers robustness mechanisms? |
| **Adaptivity** | Ability to evolve with problem changes. | E.g., online learning, modular structure | Framework supports incremental updates? |

## Toolbox

### Taxonomy

| **Domain** | **Modeling Framework** | **Mathematical Structure** | **Application Examples** |
| --- | --- | --- | --- |
| 🔧 **Control Systems** | Classical Control | Transfer functions, Laplace domain | PID control, servo systems, cruise control |
|  | State-Space Models | ODEs, state equations | Aerospace, robotics, power systems |
|  | Optimal Control (LQR, PMP) | Cost functions, Hamiltonians | Spacecraft trajectory, energy systems |
|  | Model Predictive Control (MPC) | Convex optimization + dynamic models | Industrial process control, HVAC, autonomous vehicles |
|  | Robust Control (H∞, μ) | Frequency-domain, worst-case bounds | Aircraft control, uncertain systems |
|  | Hybrid Systems | ODE + automata (discrete & continuous) | Automotive powertrains, embedded systems |
|  | Nonlinear Control | Lyapunov theory, nonlinear ODEs | Satellite attitude control, bioengineering |
|  | Adaptive Control | Time-varying parameters | Robotic arms, actuator compensation |
|  | Intelligent Control | Fuzzy logic, neural networks | Smart appliances, consumer electronics |
| 🎛️ **Signal Processing** | Linear Time-Invariant Systems (LTI) | Linear difference equations | Filter design, communication systems |
|  | Fourier, Laplace, Z Transforms | Integral transforms | Spectral analysis, filter design |
|  | Stochastic Models (AR, ARMA, ARIMA) | Time-series, probabilistic models | Radar, EEG/ECG analysis, forecasting |
|  | Adaptive Filters (LMS, RLS) | Recursive equations | Echo cancellation, system identification |
|  | Time-Frequency Analysis (STFT, Wavelets) | Nonstationary analysis, basis expansion | Speech recognition, seismic signal analysis |
|  | Compressed Sensing | Sparse linear algebra | MRI, wireless sensor networks |
| ⚙️ **Physical Systems** | Lumped Parameter Models | ODEs, algebraic models | Electrical circuits, thermal systems |
|  | Distributed Parameter Models | PDEs | Heat conduction, acoustic waves |
|  | Bond Graphs | Energy domain, port-Hamiltonian systems | Mechatronics, multi-domain systems |
|  | Finite Element Models (FEM) | Mesh-based PDE discretization | Structural stress, electromagnetics |
|  | Multibody Dynamics | ODEs, Newton-Euler or Lagrangian methods | Robotics, vehicle suspensions |
|  | Computational Fluid Dynamics (CFD) | Navier-Stokes PDEs | Aerodynamics, combustion, HVAC |
|  | Thermodynamic Models | Energy balances, equations of state | Power plants, refrigeration systems |
| 📊 **Data-Driven** | System Identification (ARX, NARX) | Time-series fitting | Black-box modeling, online estimation |
|  | Neural Networks (FF, RNN, LSTM) | Nonlinear function approximation, gradient-based | Predictive maintenance, inverse modeling |
|  | Gaussian Processes | Probabilistic regression | Battery modeling, surrogate modeling |
|  | Symbolic Regression | Evolutionary algorithms | Scientific discovery, control law synthesis |
|  | Reinforcement Learning | MDPs, Bellman equations | Adaptive robotics, autonomous systems |
|  | Physics-Informed Neural Networks (PINNs) | PDE constraints in NN training | Inverse problems, fluid dynamics |
| 🎯 **Optimization-Based** | Linear / Nonlinear Programming | Objective + constraints | Scheduling, logistics, power allocation |
|  | Convex Optimization | Convex sets, duality | Signal design, portfolio optimization |
|  | Mixed-Integer Programming (MIP) | Integer constraints | Unit commitment, process planning |
|  | Dynamic Programming | Recursive cost minimization | Inventory control, path planning |
|  | Multi-objective Optimization | Pareto front computation | Tradeoff analysis, design space exploration |
| 🏭 **Domain-Specific** | Circuit Models (SPICE) | KCL/KVL + device models | Analog/digital circuits |
|  | Electromagnetic Field Models | Maxwell’s equations | Antennas, microwave circuits |
|  | Kinematics/Dynamics (D-H, Newton-Euler) | Geometric + dynamic models | Robot motion, manipulators |
|  | Reaction Kinetics Models | ODEs for reaction rates | Chemical reactors, metabolic pathways |
|  | Process Models (DAE, Aspen) | DAEs, thermodynamics | Refining, chemical plants |
|  | Structural Mechanics | Continuum models | Bridge design, aircraft wings |
|  | Materials Models (Fatigue, Plasticity) | Empirical and constitutive models | Safety analysis, durability prediction |
| 🖥️ **Simulation & Integration** | Simulink / Simscape | Block-diagram simulation | Control system prototyping, embedded design |
|  | Modelica / OpenModelica | Acausal, object-oriented modeling | Multi-domain physical systems |
|  | Functional Mock-up Interface (FMI/FMU) | Standardized model exchange | Co-simulation of components |
|  | Discrete-Event Simulation | Queues, events, stochastic models | Manufacturing systems, networks |
|  | Agent-Based Modeling (ABM) | Rule-based, individual agents | Traffic flow, supply chains |

### Simulation

| **Simulation Type** | **Description** | **Key Tools/Frameworks** | **Example Usage** |
| --- | --- | --- | --- |
| **Multibody Simulation** | Models and simulates the dynamics of interconnected rigid or flexible bodies. | **ADAMS**, **Simpack**, **MBSim** | Simulating mechanical systems like vehicles or robots |
| **Finite Element Analysis (FEA)** | Solves complex structural and thermal problems by breaking down into finite elements. | **ANSYS**, **ABAQUS**, **COMSOL** | Stress analysis in mechanical components |
| **Computational Fluid Dynamics (CFD)** | Simulates fluid flow, heat transfer, and related phenomena using numerical methods. | **Fluent**, **OpenFOAM**, **CFX** | Aerodynamics of vehicles, weather modeling |
| **Molecular Dynamics (MD)** | Simulates physical movements of atoms and molecules over time. | **GROMACS**, **LAMMPS**, **AMBER** | Protein folding, material science |
| **Discrete Event Simulation (DES)** | Models systems where changes occur at discrete points in time based on events. | **Simul8**, **Arena**, **AnyLogic** | Manufacturing processes, supply chain management |
| **System Dynamics** | Studies and models the feedback loops and time delays in complex systems. | **Vensim**, **Stella**, **Dynasim** | Modeling economic systems, ecological dynamics |
| **Agent-Based Modeling (ABM)** | Simulates interactions of autonomous agents to study emergent behavior in complex systems. | **NetLogo**, **Repast**, **AnyLogic** | Social behavior, traffic systems |
| **Optimization Simulation** | Uses simulation techniques to find optimal solutions for complex systems. | **MATLAB Optimization Toolbox**, **Gurobi**, **CPLEX** | Resource allocation, engineering design optimization |
| **Electromagnetic Simulation** | Simulates electromagnetic fields and interactions within materials. | **COMSOL**, **HFSS**, **CST Studio** | Antenna design, electromagnetic compatibility testing |
| **Monte Carlo Simulation** | Uses random sampling to obtain numerical results for complex problems. | **MATLAB**, **Simulink**, **Python (numpy, scipy)** | Risk analysis, financial modeling |
| **Control Systems Simulation** | Simulates the behavior of control systems and their response to various inputs. | **MATLAB/Simulink**, **LabVIEW**, **Octave** | Designing and testing control algorithms |

### Numerical Method

> **Fixpoints/iteration** refers to the process of repeatedly applying a function or operation until a stable solution, called a fixpoint, is reached, often used in optimization algorithms and mathematical computations.
> 

| **Method** | **Description** | **Applications** |
| --- | --- | --- |
| **Newton's Method** | An iterative method for finding successively better approximations to the roots (zeroes) of a real-valued function. | Root-finding problems, solving nonlinear equations. |
| **Euler's Method** | A simple numerical procedure for solving ordinary differential equations (ODEs) with a given initial value. | Approximation of solutions to differential equations. |
| **Runge-Kutta Methods** | A family of iterative methods for solving ODEs, which provide more accurate solutions than Euler's method. | Solving differential equations in physics and engineering. |
| **Finite Difference Method** | A technique for approximating the solutions to differential equations by discretizing them. | Solving partial differential equations (PDEs). |
| **Gauss-Seidel Method** | An iterative technique for solving a system of linear equations by improving the solution iteratively. | Linear algebra problems, especially in large systems. |
| **Monte Carlo Method** | A statistical method using random sampling to approximate solutions to complex problems. | Numerical integration, optimization, financial modeling. |
| **Simpson's Rule** | A method for numerical integration that approximates the integral of a function using quadratic polynomials. | Calculating the area under curves, approximating integrals. |
| **Trapezoidal Rule** | A numerical integration method that approximates the area under a curve using trapezoids. | Estimating definite integrals, area calculations. |
| **LU Decomposition** | A method for solving systems of linear equations by decomposing a matrix into a lower and an upper triangular matrix. | Efficiently solving linear systems, matrix inversion. |
| **Gradient Descent** | An optimization method for finding the minimum of a function by iteratively moving towards the steepest descent. | Machine learning, optimization problems. |
| **Jacobian Method** | An iterative method for solving a system of linear equations, similar to the Gauss-Seidel method. | Solving large-scale linear systems. |
| **Fourier Transform** | A mathematical method for transforming a function of time (or space) into a function of frequency. | Signal processing, image analysis, solving PDEs. |
| **Fast Fourier Transform (FFT)** | An efficient algorithm to compute the discrete Fourier transform (DFT) and its inverse. | Digital signal processing, image processing. |
| **Conjugate Gradient Method** | An iterative method for solving systems of linear equations with a symmetric positive-definite matrix. | Solving large-scale linear systems in scientific computing. |
| **Bisection Method** | A root-finding method that repeatedly divides an interval and selects subintervals in which the root must lie. | Simple and reliable root-finding for continuous functions. |

### Mathematical Method

> High Performance Computing (HPC) utilizes a wide range of mathematical methods to solve complex problems efficiently. These methods are crucial for optimizing performance, improving accuracy, and managing large datasets.
> 

| **Method** | **Purpose** | **Applications** |
| --- | --- | --- |
| **Linear Algebra** | The core of most scientific computations | Solving systems of linear equations, eigenvalue problems, matrix operations |
| **Differential Equations** | Model continuous systems | Fluid dynamics, weather modeling, mechanical systems |
| **Fast Fourier Transform (FFT)** | Efficiently compute Fourier transforms | Signal processing, image analysis, solving partial differential equations |
| **Monte Carlo Simulations** | Random sampling for numerical integration | Financial modeling, risk analysis, physical simulations |
| **Finite Element Analysis (FEA)** | Discretizing and solving PDEs | Structural analysis, electromagnetics, heat transfer |
| **Discrete Fourier Transform (DFT)** | Analyze frequency content | Signal and image processing, spectral methods |
| **Optimization Techniques** | Maximize or minimize objective functions | Resource allocation, scheduling, network design |
| **Parallel Algorithms** | Distribute tasks across processors | Large-scale simulations, big data analysis |
| **Numerical Integration** | Approximate the integrals of functions | Area under curves, quantum mechanics |
| **Graph Algorithms** | Data structuring and manipulation | Social network analysis, internet routing |

## Case Study

### Urban Traffic Flow

| **Dimension** | **Problem Assessment** | **Candidate: Agent-Based Model** | **Fit Notes / Trade-offs** |
| --- | --- | --- | --- |
| Problem Ontology | Discrete agents (cars), network topology | ✓ Designed for agents and interactions | High fidelity, but computationally heavy |
| Causal & Structural Assumptions | Local rules → emergent behavior | ✓ Natural fit | May be harder to calibrate from data |
| Epistemic Access | Partial sensor coverage | ✓ Can simulate missing data scenarios | Requires assumptions for unobserved areas |
| Data–Model Fit | Real-time traffic sensor data | ✓ Can integrate streaming data | Needs preprocessing |
| Temporal & Spatial Scales | Seconds, road segments | ✓ Supports fine temporal/spatial resolution | May need scaling strategies |
| Computational Profile | Real-time dashboard | △ Heavy for large networks | Parallelization needed |
| Stakeholder Needs | City planners, need interpretable outputs | ✓ Visual and explainable | Complexity may require training |
| Theory Integration | Traffic flow theory available | ✓ Can integrate known rules | — |
| Tractability vs. Fidelity | High fidelity needed for policy | ✓ Suits detailed sim | Computation trade-off |
| Robustness Requirements | Must handle sensor failures | ✓ Scenario analysis possible | — |
| Adaptivity | Road network changes over time | ✓ Modifiable rules | — |

### Student Dropout

| **Dimension** | **Problem Assessment** | **Candidate Framework: Statistical Survival Analysis** | **Candidate Framework: Machine Learning (Gradient Boosted Trees)** | **Fit Notes / Trade-offs** |
| --- | --- | --- | --- | --- |
| **Problem Ontology** | Entities = students; states = enrolled, dropout, graduated; transitions in discrete time (semesters); covariates = academic, socio-economic, behavioral. | ✓ Naturally models time-to-event with censoring. | △ Treats dropout as classification, loses explicit time modelling. | Survival analysis more faithful to temporal dropout process. |
| **Causal & Structural Assumptions** | Multiple interacting causal factors, some unobserved; feedback possible (low grades → disengagement). | △ Needs assumptions about proportional hazards, covariate independence. | ✓ Non-parametric, flexible with interactions. | ML handles complex non-linearities, but less causal interpretability. |
| **Epistemic Access** | Historical records, survey data, partial observability for socio-economic factors; some missingness. | ✓ Handles censoring; statistical imputation possible. | ✓ Handles missingness with tree splits; can impute internally. | Both can cope; ML more forgiving with messy features. |
| **Data–Model Fit** | Mixed data: categorical (major, gender), continuous (GPA), temporal (attendance), ordinal (engagement scale). | ✓ Handles mixed data well in Cox / AFT models with preprocessing. | ✓ Handles mixed data natively; no strong distributional assumptions. | ML slightly lower preprocessing burden. |
| **Temporal & Spatial Scales** | Semester-based observations over 4–6 years; no spatial component unless campuses differ. | ✓ Designed for time-to-event data. | △ Needs temporal features engineered. | Survival wins on temporal elegance. |
| **Computational Profile** | Moderate dataset (10k–200k students), low latency needed. | ✓ Fast for medium datasets. | ✓ Also fast; scalable to larger datasets. | Both feasible. |
| **Stakeholder Needs** | University admin wants interpretable risk factors + actionable insights; policy compliance may require explainability. | ✓ Coefficients interpretable; hazards give intuitive meaning. | △ Feature importance available, but models more opaque. | Survival better for policy transparency. |
| **Theory Integration** | Education research already has dropout risk factor frameworks. | ✓ Easily integrates known variables & hazard structures. | △ Theory can be embedded indirectly (feature engineering). | Survival more directly theory-aligned. |
| **Tractability vs. Fidelity** | Dropout is multi-factorial; don’t need ultra-fine micro-dynamics. | ✓ Moderate complexity, interpretable. | ✓ Captures non-linear, high-dimensional effects. | Depends if priority is prediction or explanation. |
| **Robustness Requirements** | Must be robust to missing data, changing cohort composition. | ✓ Relatively stable if covariates relevant. | ✓ Very robust if retrained periodically. | ML adapts faster to shifting patterns. |
| **Adaptivity** | Annual updates; possible shifts in demographics and policies. | △ Manual model refit needed; assumptions may degrade. | ✓ Retrains easily with new data. | ML wins on adaptivity. |

## QA

### Which are the most fundamental notion that a modeler should master?

In a **synthetic form:**

- **What exists?** → entity, state, structure
- **How does it change?** → process, dynamics, trajectory
- **How do we know?** → abstraction, uncertainty, inference
- **Why does it occur?** → cause, mechanism, constraint
- **Why model it at all?** → objective, robustness, validity

**Notions Set:**

| **Category** | **Notion** | **Description** |
| --- | --- | --- |
| Ontological | Entity / Unit | Basic component or object in the system being modeled. |
| Ontological | State | Complete specification of an entity or system at a given time. |
| Ontological | Property / Attribute | A measurable or characterizable aspect of an entity or state. |
| Ontological | Relation | Structured dependency or association between entities or variables. |
| Ontological | Structure | Organized arrangement of entities and relations. |
| Dynamical | Process / Mechanism | Rule or causal pathway generating change in the system. |
| Dynamical | Transition / Update Rule | Formal specification of how states evolve. |
| Dynamical | Dynamics | Overall behavior of the system induced by repeated transitions. |
| Dynamical | Trajectory / Path | Sequence of states over time. |
| Dynamical | Equilibrium / Attractor | Stable long-term configuration of a system. |
| Epistemic | Model | Formal representation of a system for understanding, prediction, or control. |
| Epistemic | Abstraction | Deliberate omission of detail to focus on relevant structure. |
| Epistemic | Representation | Language or medium used to encode the model (equations, graphs, code). |
| Epistemic | Uncertainty | Lack of knowledge (epistemic) or intrinsic variability (aleatory). |
| Epistemic | Information | Quantified reduction of uncertainty about the system. |
| Statistical | Signal vs. Noise | Distinction between structured regularity and unstructured variability. |
| Statistical | Random Variable | Representation of uncertain quantities in the system. |
| Statistical | Distribution | Probabilistic description of variability in a variable. |
| Statistical | Correlation / Dependence | Measure of association between variables. |
| Statistical | Inference | Updating beliefs or estimates from observed data. |
| Causal | Cause | Factor whose manipulation produces a change in outcomes. |
| Causal | Mechanism | Structured causal process explaining how a pattern arises. |
| Causal | Constraint | Limitation that restricts possible system behaviors. |
| Causal | Counterfactual | Hypothetical alternative used to test causal relationships. |
| Causal | Explanation | Mapping from observed regularities to generative structure. |
| Structural | Function | Role a component plays within the system. |
| Structural | Modularity | Decomposability into semi-independent subsystems. |
| Structural | Hierarchy / Scale | Organization across levels of aggregation. |
| Structural | Interface | Controlled boundary between components or subsystems. |
| Structural | Emergence | System-level properties not trivially reducible to components. |
| Normative | Objective / Purpose | Goal or reason for building the model. |
| Normative | Fitness / Loss Function | Criterion for evaluating model performance. |
| Normative | Robustness | Stability of conclusions under perturbations or uncertainty. |
| Normative | Validity / Scope | Conditions under which the model is reliable. |
| Normative | Trade-off | Structured compromise (e.g., realism vs. tractability). |
| Meta-Modeling | Assumption | Premise taken as given in constructing a model. |
| Meta-Modeling | Idealization | Deliberate simplification or distortion for analytical leverage. |
| Meta-Modeling | Identifiability | Whether parameters can be uniquely inferred from data. |
| Meta-Modeling | Complexity | Structural or computational richness of the model. |
| Meta-Modeling | Refinement / Revision | Iterative improvement of the model in light of failure or new data. |
| Pattern | Pattern | Non-accidental regularity in structure, behavior, or distribution of elements. |

## References

- [Modelado](https://app.notion.com/p/Modelado-a6727ea210124fb9a00ff6bb5bcf7cd5?pvs=21)
- [Philosophy](https://app.notion.com/p/Philosophy-ccc223e791024b4181a87d0d2b5d1cec?pvs=21)
- [NLF Modelling](https://app.notion.com/p/NLF-Modelling-27ac0f5171ec80bf86bcc7e406fe68af?pvs=21)
- https://en.wikipedia.org/wiki/Applied_physics
- https://www.jmeiners.com/think-in-math/
- [A Guide to Language and Cognition](/view.html?p=notes/miscellanea/personal/a-guide-to-language-and-cognition.md)
- [Multiple-Criteria Decision-Making (MCDM)](https://app.notion.com/p/Multiple-Criteria-Decision-Making-MCDM-222c0f5171ec801f912effc86df5a7b1?pvs=21)
- [A Guide to Mathematical Problem-Solving](/view.html?p=notes/miscellanea/personal/a-guide-to-mathematical-problem-solving.md)
- [On the Limits of Language for Representation and Inference](/view.html?p=notes/miscellanea/personal/on-the-limits-of-language-for-representation-and-i.md)
- Wolpin, Kenneth I. The limits of inference without theory. MIT Press, 2013.
