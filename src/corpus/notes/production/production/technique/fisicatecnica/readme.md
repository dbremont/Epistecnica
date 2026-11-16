---
tags: [note, production]
---

# Fisicatecnica

> A set of notes analyzing several types of systems and technologies.
> 

> Physics offers an analytical framework for understanding reality, forming the foundation of technical science. Technical science builds on this foundation to design and construct complex objects whose behaviors and properties cannot be fully captured by simplified or idealized models. Studying these systems requires experimentation, intuition, and hands-on engagement with the objects themselves.
> 

## Index

## Research Identity

> **Keywords:** Electromechanical integration, Robotics, Thermal-mechanical actuation, Mechatronics, Cyber-physical systems, Embedded control, Multiphysics engineering.
> 

> My research centers on the **design, analysis, and integration of multidomain engineering systems** where **mechanical, electrical, thermal, and computational subsystems** interact synergistically. These systems are at the heart of emerging intelligent machines, responsive infrastructures, and advanced automation platforms.
> 

> I focus on both **theoretical frameworks** and **practical implementations** that enable precise, efficient, and robust control of physical phenomena across multiple energy domains. I am particularly interested in how foundational systems (energy, information, material) can be composed into novel machines and derived systems, yielding new capabilities through purposeful design.
> 

## Systems

> **Technology** can be defined as the application of scientific knowledge, skills, methods, and processes to create tools, systems, or solutions that solve problems or enhance human capabilities. It encompasses a wide range of fields, including engineering, information technology, biotechnology, and more.
> 

> **Technology** often involves the use of materials, machinery, software, and techniques to improve efficiency, productivity, and quality of life.
> 

> **Technology Space**: The "Technology Space" refers to the broad and dynamic landscape encompassing all technological advancements, innovations, tools, and systems across various fields and industries, as well as the interactions and relationships between them.
> 

| **Domain** | **Category** | **Engineering System** | **Description** | **Tags** |
| --- | --- | --- | --- | --- |
| **Electromagnetic System** | Electronic System | Microcontroller | Embedded digital device that processes signals and controls actuators. | Electronics, Embedded Systems |
|  | Electrical System | Electric Motor | Converts electrical energy into mechanical motion using electromagnetic principles. | Electrical Machines, Power Systems |
|  | Electrical System | Transformer | Device that transfers electrical energy between circuits via electromagnetic induction. | Power Distribution, Energy |
|  | Optical System | Optical Sensor / Laser | Uses light to detect, measure, or communicate information. | Optics, Photonics |
|  | Vision System | … | … | … |
| **Thermodynamical System** | Thermal System | Heat Engine / HVAC System | Converts thermal energy into mechanical work or controls environment temperature. | Thermodynamics, Energy Systems |
|  | Fluid Thermal System | Heat Exchanger | Facilitates thermal energy transfer between fluids for heating or cooling. | Heat Transfer, Fluid Dynamics |
| **Mechanical System** | Rigid Body System | Robotic Manipulator | Mechanical device designed for controlled motion and force application. | Robotics, Mechanics |
|  | Fluid System | Turbine / Pump | Converts fluid flow energy into mechanical work or vice versa. | Fluid Dynamics, Energy Conversion |
| **Chemical System** | Chemical Process | Chemical Reactor | Engineered vessel for carrying out controlled chemical reactions. | Process Engineering, Chemistry |
| **Biological System** | Biomedical System | Prosthetic Device | Engineered system designed to replace or augment biological function. | Biomedical Engineering, Bioelectronics |
| **Information System** | Control System | Feedback Controller | Device or algorithm managing system behavior through sensor input and actuation. | Control Theory, Automation |
|  | Embedded Computing | Real-Time Operating System | Software managing timing-critical computational tasks in physical systems. | Embedded Systems, RTOS |

## Foundation Abstraction

> System  =  Materials + Techniques + Energy + Purpose + Information + Environment.
> 

> A **Foundational System** is a primary, original system that serves as the basic building block or core framework. It provides essential functions, principles, or structures from which other systems can be developed or derived. Foundational systems are often considered fundamental or irreducible within a particular domain.
> 

> A **Derived System** is a system that is built upon, extends, or is constructed from one or more foundational systems. It inherits properties, behaviors, or components from the foundational system(s) but typically includes modifications, specializations, or additional features that distinguish it from the original.
> 

### Energy

> The capacity to perform work or cause physical change. Energy exists in various forms—kinetic, potential, thermal, electrical, chemical—and can be transformed but not created or destroyed (conservation of energy).
> 

> In engineered systems, energy is the **driving resource** that enables processes, actuation, and transformation.
> 

### Material

> The physical substance or matter from which systems, components, and environments are composed. Materials possess properties—mechanical, thermal, electrical—that determine how they respond to forces, energy, and environmental conditions.
> 

### Information

> Actually: Data.
> 

> A measure of meaningful patterns, distinctions, or correlations in data that reduce uncertainty in a given context. In physical systems, information is represented, processed, and transmitted through symbolic or physical states (e.g., voltage levels, signals, digital codes).
> 

### Machine

> An organized system of interacting components designed to transform, transmit, or utilize **energy**, **material**, and **information** to perform specific functions or tasks. Machines can be mechanical, electrical, biological, or computational, and often combine multiple domains.
> 

### Engine

> An **engine is a specific type of machine** designed to convert one **form of energy** into **mechanical energy or motion**. Engines are commonly associated with power generation and propulsion.
> 

> **Note:** If the source of energy is **electric**, the device is typically called a **motor**; if it uses **chemical fuel** (like gasoline or diesel), it's called an **engine**. However, the two terms are often used interchangeably in everyday language.
> 

> **Note:** An *engine* is a conceptual abstraction, not a system in itself. It can be implemented using various underlying technologies, depending on the context and requirements.
> 


| **Engine Type** | **Energy Source** | **Mechanism** | **Common Applications** |
| --- | --- | --- | --- |
| **Internal Combustion Engines** | Gasoline, Diesel | Combustion of fuel in cylinders to create mechanical work | Automobiles, motorcycles, generators |
| **External Combustion Engines** | Coal, Wood, Biomass | Combustion heats a working fluid (steam) to drive pistons or turbines | Steam locomotives, power plants |
| **Electric Motors** | Electricity | Converts electrical energy into mechanical motion through magnetic fields | Appliances, electric vehicles, industrial machinery |
| **Turbines** | Natural Gas, Steam, Wind | Rotating blades driven by gas expansion or fluid flow | Power generation, aircraft engines, wind energy |
| **Hydraulic Systems** | Pressurized Fluid | Uses fluid pressure to transmit force and perform work | Construction equipment, automotive lifts |
| **Pneumatic Systems** | Compressed Air | Utilizes air pressure to create motion | Air tools, packaging machines |
| **Renewable Energy Systems** | Solar, Geothermal, Biomass | Converts renewable energy into mechanical work | Solar thermal plants, geothermal power stations |
| **Reaction Engines** | Chemical Propellants | Converts chemical energy into thrust through combustion | Rocket propulsion systems |
| **Magnetic Engines** | Magnetic Fields | Theoretical engines using magnetic forces to generate motion | Experimental and theoretical applications |

## Instruction Set Architecture

> aka ISA
> 

References

- https://github.com/dbremont/isa-labs

## Electronics Projects

> An **electronic system** is a combination of interconnected electronic components and circuits that process, transmit, or control electrical signals to perform a specific function.
> 

> An **electrical system** is a network of interconnected electrical components, such as power sources, conductors, and loads, designed to generate, distribute, and utilize electrical energy.
> 

> The ethos of an electronic circuit lies in its ability to manipulate electrical energy through a structured network of components—such as resistors, capacitors, inductors, semiconductors, and interconnects—governed by principles of electromagnetism, signal processing, and feedback control to achieve deterministic functional outcomes with minimal noise, latency, and power dissipation.
> 

> The ethos of an electronic circuit is the orchestration of electrical potential into purposeful motion—an intricate dialogue between matter and energy, where the silent logic of components shapes the flow of current into structured patterns, embodying precision, efficiency, and the relentless pursuit of control over chaos.
> 

> The ethos of an electronic circuit is to efficiently transform, control, and transmit electrical signals to perform a specific function with precision and reliability.
> 

> The telos of an electronic circuit is to actualize the intentional flow of electrical energy into meaningful computation, control, or communication, embodying efficiency, precision, and purpose in its design and function.
> 

> The *technē* of an electronic circuit is the mastery of designing, constructing, and optimizing networks of electrical components to harness, manipulate, and regulate the flow of energy and information with precision, efficiency, and reliability.
> 

> Electronic circuits can implement functionalities such as signal amplification, computation, filtering, power conversion, communication, control systems, data storage, and sensing by manipulating electrical energy through a network of components.
> 

## Emulators

…

References

- https://github.com/DerekTurtleRoe/awesome-emulators
- https://www.reddit.com/r/emulation/

## Electronic Game System

> aka  EGS.
> 

References

- https://news.ycombinator.com/item?id=31590724
- https://www.reddit.com/r/learnprogramming/comments/17pd2je/is_there_any_source_code_of_video_games_that_yall/

## Notes

> ...

## References

- [Modelado](https://www.notion.so/Modelado-a6727ea210124fb9a00ff6bb5bcf7cd5?pvs=21)
- https://github.com/dbremont/ee-labs
- https://en.wikipedia.org/wiki/Physical_computing
- https://en.wikipedia.org/wiki/Multiphysics_simulation
- https://en.wikipedia.org/wiki/Model-based_systems_engineering
- https://en.wikipedia.org/wiki/Applied_science
- https://en.wikipedia.org/wiki/Mass_production
- https://en.wikipedia.org/wiki/Outline_of_technology
- https://www.aspi.org.au/program/critical-technology-tracker
- https://en.wikipedia.org/wiki/List_of_emerging_technologies
- https://en.wikipedia.org/wiki/History_of_technology
- [Defense Technology Taxonomy](https://eda.europa.eu/docs/default-source/documents/osra-defence-technology-taxonomy.pdf)
- [Introducing the Universal Technology Taxonomy](https://cipher.ai/wp-content/uploads/2022/05/ML4Patents-Webinar_UTT.pdf)
- https://en.wikipedia.org/wiki/Technology
- https://en.wikipedia.org/wiki/High_tech
- https://en.wikipedia.org/wiki/Deep_tech
- https://en.wikipedia.org/wiki/Low_technology
- https://en.wikipedia.org/wiki/Nanoelectronics
- [**Electromagnetic System**](https://www.notion.so/Electromagnetic-System-225c0f5171ec8041b3eec1564b45c5dc?pvs=21)
- Materials Science → https://next-gen.materialsproject.org/
- [2020 NASA Technology Taxonomy  -](https://ntrs.nasa.gov/api/citations/20200000399/downloads/20200000399.pdf)  [2020 NASA Technology Taxonomy  - Poster](https://www3.nasa.gov/sites/default/files/atoms/files/nasa_technology_taxonomy_poster_print.pdf)
- https://research.umd.edu/rso/advisories-and-resources/2024-critical
- ‣
- https://github.com/dbremont/ee-labs
- https://en.wikipedia.org/wiki/VHDL
- https://en.wikipedia.org/wiki/Verilog
- https://en.wikipedia.org/wiki/Ngspice
- https://en.wikipedia.org/wiki/Transmission_line
- https://en.wikipedia.org/wiki/MEMS
- https://en.wikipedia.org/wiki/Quite_Universal_Circuit_Simulator
- https://en.wikipedia.org/wiki/List_of_free_electronics_circuit_simulators
- https://docs.kicad.org/
- NGSPICE- Usage and Examples / [https://www.ee.iitb.ac.in/course/~dghosh/ngspice-2.pdf](https://www.ee.iitb.ac.in/course/~dghosh/ngspice-2.pdf)
- https://en.wikipedia.org/wiki/Arduino
- https://en.wikipedia.org/wiki/FreeRTOS
- https://en.wikipedia.org/wiki/Radio_frequency
- https://en.wikipedia.org/wiki/Embedded_system
- https://en.wikipedia.org/wiki/Software-defined_radio
- https://www.youtube.com/watch?v=sXwDrcd1t-E
- https://espargos.net/
- https://ep.intec.edu.do/oferta-academica/ingenierias-y-tecnologia/item/diplomado-en-diseno-testing-y-produccion-de-placas-electronicas
- https://github.com/dbremont/xv6
- https://github.com/dbremont/linux-api-labs
- https://github.com/dbremont/algorithms
- https://github.com/dbremont/modelarium
- https://github.com/dbremont/video-stream-lab
- https://github.com/dbremont/tinylisp
- https://github.com/dbremont/simpledb
- https://github.com/dbremont/avian
- https://github.com/csiglab/cs-analyst-labs
- https://github.com/csiglab/web-extention-labs
- https://github.com/csiglab/networking-labs
- https://github.com/csiglab/language-system-labs
- https://github.com/csiglab/security-labs
- https://github.com/csiglab/data-system-labs
- https://github.com/csiglab/visualization-lab
- https://github.com/csiglab/web-frameworks-labs
- https://github.com/csiglab/search-lab
- https://github.com/csiglab/mlsys-lab
- https://github.com/csiglab/distributed-system-lab
- https://github.com/csiglab/devops-labs
- https://github.com/csiglab/eis-labs
- https://www.youtube.com/watch?v=ngo3ZTrT69A