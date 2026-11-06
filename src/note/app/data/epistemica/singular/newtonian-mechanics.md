---
tags: [formulation, mechanics]
---

# Newtonian Mechanics

   : Hamiltonian Mechanics (Hamiltonian%20Mechanics%2096f6bccbf3fd44c5a348cf022c9a6462.md), Rigid Body Mechanics (Rigid%20Body%20Mechanics%20298c0f5171ec80398214c9f933804930.md)

> 

## Newtonian Ontology

### Principle

- **Substance ontology** — matter as *thing-in-itself* with inherent properties.
- **Spatial absolutism** — reality has a geometric structure independent of phenomena.
- **Causal realism** — causes are objective and mathematically expressible.
- **Deterministic world-picture** — every state follows necessarily from prior states under fixed laws.
- **Separation of metaphysical orders** — space-time vs. dynamics, geometry vs. matter.
- Ontology is *static*: entities have essences and exist independently of observation.
- Time is **non-phenomenal** — it does not emerge from process, but *conditions* process.

### Element

| **Domain** | **Element** | **Ontological Commitment** | **Notes** |
| --- | --- | --- | --- |
| **Space** | *Absolute Space* | Exists independently of objects and events. | It is a *container ontology*: space is the stage on which reality unfolds, not defined by relations among bodies. |
| **Time** | *Absolute Time* | Flows uniformly, independent of change or perception. | Time is a “universal clock” — a background parameter, not emergent from events. |
| **Matter** | *Substance with mass* | Exists as inert extension — occupies space and resists acceleration. | Newton reifies mass: it’s both quantity of matter and measure of inertia. |
| **Force** | *Causal agent* | Exists as a real cause that changes motion. | Forces are not just descriptive; they are **ontologically active** — the real causes of motion. |
| **Motion** | *Change of position in absolute space* | Objective and measurable independent of observers. | Unlike relational motion (Leibniz), Newton treats motion as absolute. |

## Representation

> What’s behind representation in the Newton  Formulation of the physical-mechanical facet of nature?
> 

> In the **Newtonian framework**, representation is grounded in the idea that **nature can be described as a deterministic system of bodies moving within absolute space and time**, governed by universal mathematical laws.
> 

**Core Representational Principles**

1. **Geometric–kinematic representation**
    - The world is represented as a **Euclidean 3-space** (( \mathbb{R}^3 )) evolving through an **absolute time** parameter (( t \in \mathbb{R} )).
    - Motion is depicted as a continuous curve ( \mathbf{x}(t) ) in this space.
    - Geometry provides the framework of *localization* and *measurement*.
2. **Dynamic representation**
    - The change of motion is represented by **forces** as causes:
        
        [
        
        m \ddot{\mathbf{x}} = \mathbf{F}(\mathbf{x}, t)
        
        ]
        
    - This equation encodes both **causality** and **prediction**, expressing nature as a *computable mechanism*.
3. **Ontological correspondence**
    - Mathematical objects (points, vectors, trajectories) **correspond directly** to real physical entities.
    - Space and time are **absolute ontological arenas**—the “stage” on which bodies exist and interact, not mere relational abstractions.
4. **Representation as idealization**
    - Physical phenomena (like planets, projectiles, pendulums) are idealized as **mass points** under **exact forces**.
    - Representation thus abstracts from material complexity to reveal *universal mathematical structure*.
5. **Epistemic stance**
    - Knowledge of nature is achieved through the *mathematization* of motion.
    - Representation in Newtonian mechanics is **realist**: the mathematical model is not a mere tool, but a *mirror* of the world’s causal structure.

### State Structure

> Momentum and force are the **dynamic connectors**, linking the static properties (mass, position) with changes (velocity, acceleration).
> 

| **Modern Term** | **Newton Term** | **Description** |
| --- | --- | --- |
| **Position** | Place / Location | The location of a body in absolute space. Newton represents it as a point in Euclidean 3-space, (\mathbf{x} \in \mathbb{R}^3). |
| **Velocity** | Rate of Motion | The rate of change of position with respect to absolute time, (\mathbf{v} = \dot{\mathbf{x}}). Describes how fast and in what direction the body moves. |
| **Acceleration** | Rate of Change of Motion | The rate of change of velocity, (\mathbf{a} = \dot{\mathbf{v}}). In Newton’s Second Law, acceleration is proportional to applied force. |
| **Mass** | Quantity of Matter | The intrinsic property of a body quantifying inertia. Determines resistance to changes in motion and enters directly into momentum: (\mathbf{p} = m\mathbf{v}). |
| **Momentum** | Quantity of Motion | Product of mass and velocity, (\mathbf{p} = m \mathbf{v}). Change in momentum is caused by forces; central to dynamics. |
| **Force** | Motive Force / Impressed Force | The agent causing change in motion. Newton expresses it as ( \mathbf{F} = \frac{d\mathbf{p}}{dt} ). Forces are real, ontologically active, and not just descriptive. |
| **Energy** | Vis Viva (Living Force) | Early Newtonian concept: proportional to ( m v^2 ). Newton did not formalize “energy” as modern physics does, but vis viva foreshadows kinetic energy. |
| **Angular Momentum** | Moment of Motion | The rotational analogue of linear momentum, ( \mathbf{L} = \mathbf{r} \times \mathbf{p} ). Conserved in absence of external torques. |
| **Impulse** | Change of Motion | Integral of force over time, ( \mathbf{J} = \int \mathbf{F} dt ), producing change in momentum. Used for collisions and short-duration interactions. |

## *Newtonian Spacetime*

> Mathematically, *Newtonian spacetime* (often called **Galilean spacetime**) is modeled as a 4-dimensional affine manifold with additional geometric structure.
> 

Formally: $\mathcal{N} = (M, t, h, \nabla)$ where:

| Symbol | Meaning | Description |
| --- | --- | --- |
| $M$ | 4-dimensional affine manifold | The set of all spacetime points. No metric, but affine structure. |
| $t: M \to \mathbb{R}$ | Absolute time function | Assigns to each event a real-valued “moment of time.” Level sets $t^{-1}(c)$ are *spatial slices*. |
| $h$ | Spatial metric | On each constant-time slice  $\Sigma_c = t^{-1}(c)$, ($h$) defines a Euclidean 3-metric. |
| $\nabla$ | Flat affine connection | Defines straight (inertial) worldlines and allows comparison of spatial vectors at different points. |

## QA

### Which phenomena that capture the configuration of a physical system can impact its future states?

> The **configuration** of a system is the complete specification of all its relevant state variables at a given time.
> 

> The **future evolution** of the system depends on this configuration through the system’s **dynamical laws** (e.g., Newton’s laws, Schrödinger equation).
> 

### Why  does momentum is a central abstraction in Physics?

### Which are the abstraction derived from the fundamental notion of motion?

> All these abstractions **emerge from the primitive idea of motion**. They are **higher-level constructs** that let physics move from **observation of displacement** to **laws, predictions, and conservation principles**.
> 

| **Abstraction** | **Derived From** | **Role** |
| --- | --- | --- |
| Position | Motion in space | Describes configuration |
| Velocity | Change of position | Captures motion rate & direction |
| Acceleration | Change of velocity | Quantifies motion change |
| Momentum | Mass × velocity | Conserved quantity; causal capacity |
| Force | Cause of acceleration | Connects dynamics to motion change |
| Energy | Motion & interactions | Scalar measure of system’s capacity to do work |
| Impulse | Integrated force | Links forces to momentum changes |
| Angular Momentum | Rotational motion | Captures rotational invariance & conservation |
| Trajectory | Time evolution of position | Global representation of motion |

### What is the relation of Kinetic Energy and Momentum?

> **Momentum (Newton)** = quantity of motion, vectorial, causal link to force.
> 

> **Vis viva (Leibniz)** = scalar “living force,” precursor to kinetic energy, not the same as momentum.
> 
> 
> Historical confusion arose because both describe “motion,” but **with different mathematical forms and physical interpretations**.
> 

## References

- https://en.wikipedia.org/wiki/Newtonian_dynamics
- Friedman, M. (1983). *Foundations of Space-Time Theories*. Princeton University Press.
- https://www.youtube.com/watch?v=VTyqGh5t2MI
- https://brilliantlightpower.com/partial-list-of-physical-phenomena-solved-by-classical-physics/
