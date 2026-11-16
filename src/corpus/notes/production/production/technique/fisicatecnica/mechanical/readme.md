---
tags: [note, production]
---

# Mechanical System

> **Statical Mechanical System:** System at rest or in equilibrium; no motion or velocity changes over time.
> 

> **Dynamic Mechanical System:**  A **dynamic mechanical system** is a system in which **time-dependent forces and motions are significant**. It involves components that experience acceleration, inertia, vibrations, or transient responses, requiring analysis of how the system evolves over time under varying loads.
> 

> Rigid body mechanics is the theory; mechanical mechanisms are the application of that theory to real devices.
> 

> **Mechanical mechanisms** operate under the principles of **rigid body mechanics**, but with a focus on **how multiple rigid bodies interact** through joints and constraints to produce controlled motion.
> 

> Mechanical engineering is fundamentally an art—the creative synthesis of new machines and mechanisms. This process is not purely deductive; it relies on experimentation, intuition, and iterative design. Engineers investigate the interplay of materials, forces, and motions, uncovering solutions through hands-on practice and inventive insight rather than through formal reasoning alone.
> 

## Index

## Formulation

> **Mechanical engineering** deals not just with idealized particles or single rigid bodies, but with **complex assemblies of interconnected rigid bodies**.
> 

These assemblies (mechanisms, machines, structures) exhibit behaviors that are often **non-intuitive and surprising** due to:

1. **Multiple Degrees of Freedom:** Each link or component can move in constrained ways, and the combination creates complex motion patterns.
2. **Interdependencies:** Forces, torques, and accelerations in one part propagate throughout the system.
3. **Nonlinear Effects:** Small changes in configuration or input can produce large, sometimes unexpected changes in output motion or stress.
4. **Emergent Phenomena:** Vibrations, resonance, stability issues, or coupled oscillations emerge only in systems, not in single-body models.

## System S

| Application / Engineering Type | Description | Case Studies |
| --- | --- | --- |
| **Automotive Systems** | Mechanical systems used in vehicles for propulsion, control, suspension, etc. | Engines, transmissions, brakes, steering linkages, suspension systems |
| **Aerospace Systems** | Mechanical systems designed for aircraft and spacecraft | Jet engines, landing gear, control surfaces, actuators, fuel systems |
| **Industrial Machinery** | Machines used in manufacturing and production processes | CNC machines, conveyor belts, robotic arms, presses, pumps |
| **Hydraulic and Pneumatic Systems** | Systems that use fluid power to generate and transmit mechanical force | Hydraulic presses, pneumatic actuators, brake systems, fluid power circuits |
| **Robotics and Automation** | Mechanical subsystems integrated with sensors and controllers for automation | Robot manipulators, grippers, drives, end effectors |
| **Energy Systems** | Mechanical systems related to power generation and energy conversion | Turbines (steam, gas, water), generators, wind turbines, pumps |
| **Building Services and HVAC** | Mechanical systems for building comfort and utilities | Heating systems, ventilation fans, water supply and drainage, elevators |
| **Marine Engineering Systems** | Mechanical systems used in ships and underwater vehicles | Propulsion shafts, pumps, ballast systems, steering gears |
| **Mechatronic Systems** | Hybrid mechanical-electronic systems combining mechanics with control and computation | CNC machines, drones, automotive ABS, smart actuators |
| **Medical Devices** | Precision mechanical systems for healthcare applications | Surgical robots, prosthetics, infusion pumps, imaging equipment |
| **Consumer Products** | Mechanical components in everyday products | Bicycle gears, watches, appliances (washing machines, mixers) |

| Type | Description | Key Characteristics |
| --- | --- | --- |
| **Static Mechanical System** | System at rest or in equilibrium; no motion or velocity changes over time. | Forces balanced, no acceleration, no inertia effects. Examples: a bridge holding load, a stationary crane. |
| **Dynamic Mechanical System** | System involving motion, acceleration, and time-dependent forces. | Includes inertia, vibrations, oscillations, transient behaviors. Examples: engines, pendulums, vehicles. |
| **Rigid Body System** | Assumes components do not deform; idealized solid objects. | Simplifies analysis by ignoring elastic deformation. Examples: gears, linkages modeled as rigid parts. |
| **Deformable Body System** | Components experience elastic or plastic deformation under loads. | Requires stress-strain analysis; accounts for material behavior. Examples: beams bending under load, springs. |
| **Open Mechanical System** | Exchanges energy and/or matter with the environment. | Example: an internal combustion engine exchanging heat, exhaust, and fuel. |
| **Closed Mechanical System** | No matter crosses system boundary; may exchange energy (like heat or work). | Example: a sealed hydraulic cylinder. |
| **Discrete Mechanical System** | Consists of a finite number of components or bodies with defined interactions. | Examples: a gearbox, a robotic arm. |
| **Continuous Mechanical System** | Described by continuous parameters, often modeled by PDEs. | Examples: beams, plates, fluid-structure interaction systems. |
| **Linear Mechanical System** | System behavior can be approximated by linear equations (forces proportional to displacements). | Easier to analyze, often used in vibrations and control. |
| **Nonlinear Mechanical System** | Exhibits nonlinear behavior—stiffness, damping, or forces are nonlinear functions. | Complex dynamics, can exhibit chaos or bifurcations. |

## Building Blocks Taxonomy

| **Category** | **Building Block** | **Function** | **Physical Domain** | **Roles** |
| --- | --- | --- | --- | --- |
| **Structural Elements** | Frame / Chassis | Support system, define geometry | Mechanical | Machine bed, vehicle frame |
|  | Beam / Rod | Carry axial and bending loads | Mechanical | Shafts, struts, tie rods |
|  | Plate / Shell | Support surface loads, enclosures | Mechanical | Housings, armor plates |
|  | Joint | Enable/restrict movement between parts | Mechanical | Hinge, revolute joint, slider |
|  | Fastener | Rigidly connect elements | Mechanical | Bolts, rivets, pins |
| **Motion Transmission** | Bearing | Constrain motion, reduce friction | Mechanical | Ball, roller, journal bearings |
|  | Gear | Transfer torque and speed (rotary) | Mechanical | Spur gear, bevel gear |
|  | Pulley | Redirect force, change mechanical advantage | Mechanical | Block-and-tackle |
|  | Belt / Chain | Transmit motion over distance | Mechanical | Timing belts, roller chains |
|  | Screw / Thread | Convert rotary to linear motion | Mechanical | Lead screw, bolt |
|  | Link | Transmit force or motion between elements | Mechanical | Rods in a linkage system |
| **Actuation** | Motor | Convert electrical to mechanical energy | Electro-mechanical | DC motor, stepper |
|  | Cylinder | Convert fluid pressure to linear motion | Hydraulic / Pneumatic | Pneumatic actuator |
|  | Spring | Store and release mechanical energy | Mechanical | Coil spring, leaf spring |
|  | Mass | Resist acceleration; provides inertia | Mechanical | Counterweight |
|  | Valve | Control flow of fluid energy | Fluidic (hydraulic/pneumatic) | Directional or pressure control valve |
| **Energy Flow Control** | Nozzle / Orifice | Modulate or direct fluid flow | Fluidic / Thermal | Jet engines, spray heads |
|  | Heat Sink / Conductor | Transfer heat away from components | Thermal | Cooling fins, radiators |
|  | Seal / Gasket | Prevent fluid or pressure leakage | Mechanical / Fluidic | O-rings, packing seals |
| **Measurement & Interface** | Sensor Base (Transducer) | Detect physical quantity (foundation of sensors) | Multidomain | Strain gauge, piezoelectric element |
|  | Interface Surface | Contact layer for interaction | Mechanical | Cam profile, clutch plate |

## Reference Space

| **Book** | **Description** | **Era** | **Origina** |
| --- | --- | --- | --- |
| **“De Re Metallica” by Georgius Agricola** | Systematic treatise on mining, metallurgy, and mechanical devices used in extraction and processing. | 1556 | German |
| **“Machines et Mécanique” by Jacques Besson** | Illustrated manual of mechanical devices and automata; emphasizes practical mechanisms. | 1578 | French (influenced German and Italian engineering) |
| **“Theatrum Machinarum” by Johann Besson / Besson's works** | Early collection of mechanical designs, including pumps, presses, and automata. | 17th century | German/French |
| **“Le diverse et artificiose machine” by Agostino Ramelli** | Italian Renaissance “encyclopedia” of mechanical inventions; includes over 100 innovative machines with illustrations. | 1588 | Italian |
| **“The New Book of Machines” by Vittorio Zonca** | Italian engineering compendium with water-lifting devices, mills, and mechanical systems. | 1607 | Italian |
| **“Theatrum Machinarum Novum” by Giovanni Branca** | Early Italian treatise showing practical mechanical devices, including Branca’s famous steam turbine concept. | 1629 | Italian |
| **“Theatrum Machinarum” by Johann Besson (expanded)** | German compendium of mechanical devices, automata, mills, and tools. | 17th century | German |
| **“Mechanica” by Giovanni Alfonso Borelli** | Mathematical treatment of mechanics; applies physics to real-world mechanical systems. | 1670 | Italian |
| **“Principia Mathematica” by Isaac Newton** | Foundations of classical mechanics, motion, and forces; crucial for machine theory. | 1687 | English (widespread European influence) |
| **“Traité de Mécanique” by d’Alembert** | Advanced mathematical mechanics; d’Alembert’s principle bridges theory and applied mechanics. | 1743 | French (influential in German-speaking Europe) |
| **“Encyclopédie ou Dictionnaire Raisonné des Sciences, des Arts et des Métiers” by Diderot & d’Alembert** | Comprehensive encyclopedia covering mechanical devices, industrial arts, and practical engineering knowledge. | 1751–1772 | French (used across Europe) |
| **“Technische Enzyklopädie” by Johann Beckmann** | German encyclopedia of technical and mechanical arts; detailed descriptions of machines and industrial processes. | 1777–1800 | German |
| **“An Elementary Treatise on Mechanics” by William Rankine** | Explanation of mechanics with engineering applications; widely adopted in the Industrial Revolution. | 1850s | British |
| **“A Treatise on Machinery” by Robert Willis** | Systematic study of machines, including kinematics and mechanisms; foundational in machine design. | 1841–1844 | British |
| **“Applied Mechanics” by James Thomson** | Covers statics, dynamics, and strength of materials; standard in engineering education. | 1879 | British/Scottish |
| **“The Engineer’s Pocket-Book” by Lionel S. Marks** | Practical handbook for engineers; mechanics, thermodynamics, materials, and machinery design. | 1890s | British (international reach)


## References

- https://en.wikipedia.org/wiki/Machine#Mechanical_systems
- Mechanisms and Mechanical Devices Sourcebook - …
- Mechanical Engineering Design	J.E. Shigley & Richard Budynas
- Machinery’s Handbook - Industrial Press
- Design of Machine Elements - 	M.F. Spotts & T.E. Shoup
- 507 Mechanical Movements – Henry T. Brown
- **The Way Things Work Now** – David Macaulay
- https://de.wikipedia.org/wiki/Taschenbuch_f%C3%BCr_den_Maschinenbau
- Standard Handbook of Machine Design - Joseph Shigley, Charles Mischke
- Structural Analysis	R.C. Hibbeler
- Advanced Structural Analysis	Devdas Menon
- https://en.wikipedia.org/wiki/Cyclop%C3%A6dia,_or_an_Universal_Dictionary_of_Arts_and_Sciences
- https://en.wikipedia.org/wiki/Lexicon_Technicum
- https://hackaday.com/2016/02/29/2100-mechanical-mechanisms/