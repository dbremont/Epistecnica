# Cellular Automata


> The Cellular Automata model of computation is a discrete computational model consisting of a grid of cells, each following a set of rules based on its neighbors’ states, leading to emergent patterns and behavior.
> 

> A **Cellular Automaton (CA)** is a **discrete model of computation** used in mathematics, computer science, physics, and biology. It is based on a grid of **cells**, each in one of a finite number of **states**, which evolve through discrete time steps according to a set of **local rules** based on the states of neighboring cells.
> 

> Cellular Automata are a **parallel, spatially distributed model of computation**, where complex behavior emerges from simple local interactions. They offer insights into **emergence**, **computation in physical systems**, and **distributed algorithms**, and they challenge the notion that all computation must be sequential or centralized.
> 
- [ ]  Learn more about CA ([Cellular Automata](note.html?n=epistemica/natural-computing/cellular-automata.md) );  and Continue With Low Level Graphics (https://github.com/dbremont/visiotecnica-labs); Migrate the Results to Python-Matplotlib (No Real Time Updates) (https://github.com/dbremont/algorithms)

QA:

- **¿What computations do the model help us to encode?** The model helps us encode computations that involve the evolution of patterns and structures based on simple local rules, often used in simulations and studying complex systems.
- **¿What is the abstract machine?** The abstract machine in Cellular Automata is the grid of cells, where each cell’s state evolves over discrete time steps according to predefined update rules based on the neighboring cells’ states.
- **¿How to encode computations?** Computations in Cellular Automata are encoded by defining the initial configuration of the grid (cell states), specifying the local update rules, and then observing how the patterns evolve over time through successive iterations or generations.

## 🧠 Structure

- **Grid**: Usually 1D, 2D (like Conway’s Game of Life), or higher-dimensional.
- **Cell**: Each point in the grid has a state (from a finite set, e.g., `{0, 1}`).
- **Neighborhood**: The set of nearby cells that influence a cell’s next state.
- **Rule (Transition Function)**: Determines a cell’s next state using its own state and the states of neighbors.

## **Formal Definition**

A CA is a tuple A = (d, S, N, f)

where:

- $d$: Dimension of the grid (e.g., 1D, 2D)
- $S$: Finite set of cell states
- $N$: Finite neighborhood (e.g., nearest neighbors)
- $f: S^n \rightarrow S$: Local update rule applied synchronously to all cells  (**change the state only to itself**)

### Finite Neighborhood

| **Name** | **Dim** | **Radius (r)** | **# of Neighbors** | **Includes Center?** | **Neighborhood Shape** | **Typical Use Case** |
| --- | --- | --- | --- | --- | --- | --- |
| **Elementary** | 1D | 1 | 2 | ✅ | Linear (3 cells) | Rule 30, Rule 110 (Turing complete) |
| **General 1D** | 1D | $r$ | $2r$ | ✅ | Linear (2r+1 cells) | Extended-range automata |
| **von Neumann** | 2D | 1 | 4 | ✅ | Diamond (Manhattan distance ≤ 1) | Growth, fire spread, traffic |
| **von Neumann (r)** | 2D | $r$ | $2r(r+1)+1$ | ✅ | Diamond (taxicab norm) | Diffusion, coarse simulations |
| **Moore** | 2D | 1 | 8 | ✅ | Square (3×3 block) | Game of Life, image processing |
| **Moore (r)** | 2D | $r$ | $(2r+1)^2 - 1$ | ✅ | Square (block) | Extended-range pattern formation |
| **Hexagonal (axial)** | 2D | 1 | 6 | ✅ | Hexagon | Biological models, urban growth |
| **Face-centered** | 2D | 1 | 4 or 8 | ✅ | Irregular | Lattice gases, soft matter |
| **3D von Neumann** | 3D | 1 | 6 | ✅ | Axes-aligned neighbors | Modeling solids or voxel environments |
| **3D Moore** | 3D | 1 | 26 | ✅ | Cube (3×3×3) | Complex 3D systems, reaction-diffusion |
| **Cross** | 2D | 1 | 4 | ✅ | Plus-shaped | Traffic flow, pathfinding |
| **Knight (Chess)** | 2D | Variable | 8 | ❌ | L-shaped (nonlocal) | Rare, used for jumpy interaction patterns |
| **Extended (Hybrid)** | Any | Variable | Variable | ✅/❌ | Mixed | Custom models, non-uniform rules |

### 🔄 Extensions

- **Probabilistic Rules**: e.g., stochastic CA used in modeling diffusion.
- **Asynchronous Updates**: Cells update at different times.
- **Nonuniform Rules**: Different rules in different regions.
- **Totalistic Rules**: The rule depends only on the **sum** of neighbor states, not their arrangement (e.g., majority rules).

## **Computation**

CA can compute functions or simulate systems by encoding:

- **Initial configuration**: Input
- **Evolution rules**: Program
- **Final configuration**: Output

Some cellular automata are **Turing-complete**, meaning they can simulate any algorithm. Notable examples:

- **Rule 110** (1D CA with 2 states, radius 1)
- **Conway’s Game of Life** (2D CA)

## 💻 Cellular Automaton as an Alternative Model of Computation

| Feature | Traditional (Turing Machine) | Cellular Automaton |
| --- | --- | --- |
| Memory | Infinite tape | Infinite grid of cells |
| Control flow | Finite state machine | Local transition function |
| Execution | Sequential (step by step) | Fully parallel (all cells update) |
| Input/Output | Encoded on the tape | Encoded in initial/final configurations |
| Time | Discrete steps | Discrete steps |
| Universality | Turing-complete (TM) | Some CA are Turing-complete |

## 🔍 Uses

- **Physics**: Lattice gases, Ising model
- **Biology**: Pattern formation, morphogenesis
- **Computer Science**: Parallel computation, cryptography
- **Mathematics**: Complexity theory, fractals

## 🌱Design Guide

> How to design CAs to model real world phenomena?
> 

| **Phenomenon** | **Choose Neighborhood with…** |
| --- | --- |
| Diffusion-like spread | Symmetry + short range (e.g., Moore) |
| Signal routing | Directionality + moderate range (e.g., von Neumann) |
| Biological patterning | Isotropy + larger Moore or hexagonal neighborhoods |
| Computation / logic | Tight locality + discrete rules (e.g., 1D radius-1) |
| Fractal growth | Minimal neighborhood + chaotic rule |
| Probabilistic processes | Add randomness to otherwise structured neighborhoods |

## Limits

> What kinds of processes are inherently difficult or unsuitable to model with cellular automata?
> 

| **Type** | **Limitation** | **Description** | **Impact** |
| --- | --- | --- | --- |
| Structural | **Locality Constraint** | Cells update based only on nearby neighbors | Cannot model long-range interactions |
| Modeling | **Discrete Space and Time** | Operate on fixed grids and time steps | Low resolution; can't model continuous phenomena |
| Practical | **Inefficient Computation** | Turing-complete but inefficient for general tasks | Not suitable for high-performance or large-scale use |
| Usability | **Hard to Calibrate** | Rules are difficult to map to real-world variables | Poor fit for empirical or data-driven modeling |
| Conceptual | **Limited Expressiveness** | Simple rules struggle with complexity | Can’t easily model hierarchical or rich systems |
| Modeling | **Boundary Condition Artifacts** | Artificial grid boundaries or wraparound schemes | May produce unrealistic edge behavior |
| Theoretical | **Emergent Behavior is Hard** | Global behavior is unpredictable from local rules | Difficult to analyze, predict, or control |
| Applicability | **Poor Fit for Some Domains** | Some problems are better solved with other models (e.g., PDEs, agents) | Limited to systems naturally fitting CA framework |

## Case Studies

> 

| **Case Study** | **Neighborhood Type** | **Phenomenon Modeled** | **Emergent Behavior** | **Application Domain** |
| --- | --- | --- | --- | --- |
| **Conway’s Game of Life** | 2D Moore (r = 1) | Biological life / growth | Oscillators, gliders, complex self-replication | Artificial life, computation, education |
| **Rule 110** | 1D Radius-1 | Computation | Turing-complete logic, glider-like signals | Theory of computation |
| **Forest Fire Model** | 2D von Neumann (r = 1) | Spread of fire | Front propagation, firebreaks, extinction | Ecology, emergency simulation |
| **Ising Model (CA version)** | 2D Moore (r = 1) | Magnetic spin interactions | Phase transitions, criticality | Statistical physics |
| **Diffusion-Limited Aggregation** | 2D Moore or Hexagonal | Particle aggregation | Fractal growth, boundary accumulation | Materials science, growth modeling |
| **Urban Growth Simulation** | 2D von Neumann + weights | Spatial development | Clustered cityscapes, street patterns | Urban planning, geography |
| **Reaction-Diffusion (e.g., Turing)** | 2D Moore (r ≥ 2) | Morphogenesis | Stripes, spots, labyrinths | Developmental biology, pattern design |
| **Belousov-Zhabotinsky Simulation** | 2D Moore (r = 1) | Chemical oscillations | Spiral waves, periodic bursts | Nonlinear dynamics, chemistry |
| **Ant Trail CA** | 2D von Neumann (r = 1) | Pheromone trail formation | Dynamic path optimization | Swarm robotics, behavior modeling |
| **Epidemic Spread** | 2D Moore (r = 1) + stochastic | Disease transmission | Infection waves, herd immunity thresholds | Epidemiology, public health |
| **Voting/Consensus Models** | 2D Moore or von Neumann | Opinion dynamics | Majority rule, polarization, domain walls | Sociology, decision theory |
| **Traffic Flow Models** | 1D or 2D directed (asymmetric) | Car movement, queuing | Stop-and-go waves, congestion patterns | Transportation, logistics |
| **Crystal Growth Simulation** | 2D Moore or hexagonal | Solidification | Dendritic or compact growth fronts | Materials engineering |
| **3D Life-Like Automata** | 3D Moore (r = 1) | Volumetric pattern emergence | Cloud-like, expanding geometries | Theoretical modeling, 3D data growth |

## Related Concepts

| **Category** | **Idea** | **Description & Relation to Cellular Automata (CA)** |
| --- | --- | --- |
| **Theoretical Computation Models** | **Turing Machines** | CA can simulate Turing machines; some CA (e.g., Rule 110, Game of Life) are Turing-complete. |
|  | **Finite State Machines (FSMs)** | Individual CA cells behave like FSMs with local state transitions; global CA behavior emerges from these local interactions. |
|  | **Tag Systems** | Simple rewriting systems equivalent to Turing machines; CA can simulate tag systems. |
|  | **Boolean Circuits** | CA update rules correspond to boolean logic; CA acts like evolving circuits over space and time. |
|  | **Register Machines** | Abstract computational models that can be emulated through specific CA configurations. |
|  | **Automata Networks** | Generalization of CA on arbitrary graphs, not just grids; nodes update state based on neighbors. |
|  | **Cellular Neural Networks (CNNs)** | Continuous-time, continuous-state analog of CA used in control and image processing, bridging CA and neural nets. |
| **Discrete Dynamical Systems** | **Discrete Dynamical Systems** | CA are spatially extended discrete dynamical systems with local update rules and discrete time steps. |
|  | **Symbolic Dynamics** | Mathematical study of sequences of symbols; CA configurations correspond to symbolic shift spaces. |
|  | **Subshift of Finite Type (SFT)** | Defines CA constraints by forbidding finite sets of local patterns in configurations. |
|  | **Phase Space and Attractors** | Analysis of CA long-term behavior via fixed points, periodic cycles, and chaotic attractors. |
|  | **Entropy Measures** | Quantifies complexity and unpredictability of CA evolution. |
|  | **Lyapunov Exponents for CA** | Measure of sensitivity to initial conditions in CA; indicates chaotic behavior. |
|  | **Reversible Cellular Automata** | CA where each state has a unique predecessor, modeling physically reversible processes and conservation laws. |
| **Physical and Statistical Models** | **Ising Model** | Spin lattice statistical physics model with local interaction similar to CA update rules. |
|  | **Lattice Gas Automata (LGA)** | CA models simulating fluid and particle dynamics; foundation for lattice Boltzmann methods. |
|  | **Quantum Lattice Gas Automata** | Quantum generalization of LGA for simulating quantum fluids and particles. |
|  | **Reaction-Diffusion Systems** | Continuous PDE-based models for pattern formation; discretized as CA approximations (e.g., Gray–Scott model). |
|  | **Coupled Map Lattices (CML)** | Generalized CA with continuous states updated by coupled nonlinear maps, modeling spatiotemporal chaos. |
|  | **Hamiltonian and Conservative CA** | CA modeling energy-conserving physical systems; often reversible and mimicking physical laws. |
|  | **Percolation Models** | Random lattice occupancy models related to connectivity and phase transitions; related to probabilistic CA. |
|  | **Markov Random Fields (MRF)** | Probabilistic graphical models with local dependencies; extend probabilistic CA concepts. |
| **Probabilistic and Fuzzy Extensions** | **Probabilistic Cellular Automata (PCA)** | CA with stochastic transitions; model noise, uncertainty, and probabilistic phenomena. |
|  | **Fuzzy Cellular Automata** | CA with fuzzy-valued states and rules, capturing uncertainty and degrees of truth. |
|  | **Asynchronous Cellular Automata** | Cells update at non-uniform or random times rather than synchronously; closer to real-world systems. |
|  | **Multistate Cellular Automata** | CA with more than two states per cell, allowing richer, more complex dynamics. |
|  | **Continuous Cellular Automata** | CA with real-valued states; bridge CA with continuous dynamical systems and PDEs. |
|  | **Quantum Cellular Automata** | Quantum-mechanical version of CA, incorporating superposition and entanglement; researched in quantum computing. |
|  | **Stochastic Automata Networks (SANs)** | Combines stochastic processes with automata networks, extending probabilistic CA modeling. |
| **Artificial Life and Biological Models** | **Artificial Life (ALife)** | CA are fundamental for simulating lifelike behaviors, emergence, and self-organization in artificial life research. |
|  | **Langton’s Loops and Self-replication** | Self-replicating CA patterns modeling biological reproduction and evolution. |
|  | **Neural Cellular Automata** | Hybrid models where neural networks learn or control CA update rules or dynamics. |
|  | **Genetic Algorithms (GAs) with CA** | Use of evolutionary algorithms to optimize CA rules or initial states for complex behaviors. |
|  | **Morphogenesis Models** | CA-based models simulating biological pattern formation inspired by reaction-diffusion theory. |
|  | **Swarm Intelligence Models** | Decentralized agent-based models following simple local rules, related to CA principles of emergent behavior. |
| **Applied Modeling and Simulation Platforms** | **NetLogo** | General-purpose multi-agent modeling environment supporting CA-like grid models. |
|  | **Golly** | Dedicated CA simulator for 1D and 2D CAs including Game of Life, Rule 110, and others. |
|  | **MCell / BioCell** | Biochemical simulation platforms using CA principles to model molecular diffusion and interactions. |
|  | **Evolvable Hardware** | Hardware implementations of CA evolved via genetic or evolutionary algorithms for adaptive systems. |
|  | **Repast, Mason** | Agent-based modeling frameworks capable of implementing CA and related spatial models. |
| **Classification and Meta-Analysis** | **Wolfram’s Classification of CA** | Categorizes CA behaviors into four classes: fixed, periodic, chaotic, and complex. |
|  | **Computational Universality** | Conditions under which CA can simulate any computable algorithm; relates to Turing completeness. |
|  | **Computational Complexity of CA** | Studies resource requirements (time, space) for CA computations. |
|  | **Computation Trade-offs in CA** | Analyses efficiency, representability, and limitations in CA computations compared to other models. |
|  | **Emergence and Self-Organization** | Phenomena where complex global patterns arise from simple local CA rules without centralized control. |

## References

- [Cellular Automaton](https://en.wikipedia.org/wiki/Cellular_automaton)
- [Studying Growth with Neural Cellular Automata](https://greydanus.github.io/2022/05/24/studying-growth/)
- [https://mathworld.wolfram.com/ElementaryCellularAutomaton.html](https://mathworld.wolfram.com/ElementaryCellularAutomaton.html)
- [https://plato.stanford.edu/entries/cellular-automata/](https://plato.stanford.edu/entries/cellular-automata/)
- [https://mathworld.wolfram.com/CellularAutomaton.html](https://mathworld.wolfram.com/CellularAutomaton.html)
- https://github.com/hsayama/PyCX → This required mayor adaptation;  for wayland;  remove parameters; etc.
- https://github.com/hsayama/PyCX
- https://www.ai.rug.nl/AS_Labs/CA/
- https://github.com/dbremont/language-system-labs/
- https://github.com/dbremont/algorithms
- https://en.wikipedia.org/wiki/Rule_110
- Wolfram, Stephen. "Statistical mechanics of cellular automata." Reviews of modern physics 55.3 (1983): 601.
- https://plato.stanford.edu/entries/cellular-automata/supplement.html
- https://courses.physics.illinois.edu/phys498cmp/sp2022/Overview.html
- https://www.amazon.com/Cellular-Automata-Applications-Monographs-Mathematics/dp/3319850474
- Sarkar, Palash. "A brief history of cellular automata." Acm computing surveys (csur) 32.1 (2000): 80-107.
- https://cafaq.com/
- https://www.amazon.com/Cellular-Automata-Discrete-Andrew-Ilachinski/dp/981238183X →  [http://lib.ysu.am/disciplines_bk/10601885498bd77aa5069c30185beabd.pdf](http://lib.ysu.am/disciplines_bk/10601885498bd77aa5069c30185beabd.pdf) (If The Book is Good It Must be Bought)
- Toffoli, T. & Margolus, N. (1987). *Cellular Automata Machines: A New Environment for Modeling*. MIT Press. [PDF](https://people.csail.mit.edu/nhm/cam-book.pdf)
- Hedlund, G. A. (1969). Endomorphisms and automorphisms of the shift dynamical system. *Mathematical Systems Theory*, 3(4), 320–375. [Springer](https://link.springer.com/article/10.1007/BF01691062)
- Boccara, N. (2004). *Modeling Complex Systems*. Springer. [PDF](https://ndl.ethernet.edu.et/server/api/core/bitstreams/160340ae-2d4d-492a-a3ee-c53629febfc6/content)
- Kari, J. (2005). Theory of cellular automata: A survey. *Theoretical Computer Science*, 334(1–3), 3–33. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S030439750500054X)
- http://bactra.org/notebooks/cellular-automata.html
- [Subshift of Finite Type](note.html?n=epistemica/mathematical/ds/subshift-of-finite-type.md)
