# Computer Numerical Control (CNC)

> **CNC** is a programmable automation system in which a digital computer directs the movements and operations of a mechanical tool (e.g., mill, lathe, cutter) based on numerical instructions (typically in G-code), enabling precise, repeatable, and complex machining tasks without manual intervention.
> 

## Study Guide

> CNC machines rely heavily on **real-time control software**, with **G-code** as the main language interface. The stack spans from **CAM software** down to **firmware in motor drivers**, and real-time execution is crucial for precision.
> 

If you're looking into **developing or hacking** CNC machines, you'll want to understand:

- G-code semantics (interpreter level)
- Real-time control and motion planning
- Communication protocols (like EtherCAT or Modbus)
- Embedded firmware on motor drivers

## Taxonomy

| Type | Description | Common Use |
| --- | --- | --- |
| **CNC Milling Machine** | Uses rotating cutting tools to remove material; moves in X, Y, Z axes. | Complex metal or plastic parts, molds, precision components. |
| **CNC Lathe / Turning Center** | Rotates the workpiece while a stationary cutting tool removes material. | Cylindrical parts, shafts, bushings, bolts. |
| **CNC Router** | Similar to a mill but optimized for softer materials (wood, plastic, foam). | Sign making, furniture, composite panels. |
| **CNC Plasma Cutter** | Uses high-velocity ionized gas (plasma) to cut metal. | Sheet metal fabrication, automotive bodywork. |
| **CNC Laser Cutter** | Uses a focused laser beam to cut or engrave material. | Precision cutting, engraving of plastics, metals, and wood. |
| **CNC EDM (Electrical Discharge Machine)** | Uses electrical discharges to shape conductive materials. | Mold and die making, hard metals, fine features. |
| **CNC Waterjet Cutter** | Uses high-pressure water (with or without abrasives) to cut any material. | Stone, glass, composites, metals. |
| **CNC Grinder** | Uses a rotating abrasive wheel to finish surfaces. | Surface finishing, ultra-precise tolerances. |
| **CNC Bending Machine / Press Brake** | Precisely bends sheet metal using hydraulic or electric force. | Sheet metal forming, brackets, enclosures. |
| **CNC Drilling Machine** | Automates high-speed, precise drilling operations. | PCBs, mechanical components, mass production. |
| **CNC 3D Printer** | Adds material (typically plastic or resin) layer by layer. | Prototypes, product development, low-volume production. |
| **CNC Pick-and-Place Machine** | Places electronic components on PCBs with high speed and accuracy. | Electronics manufacturing, SMT assembly. |

## References

- https://en.wikipedia.org/wiki/Computer_numerical_control
- https://en.wikipedia.org/wiki/G-code
- https://en.wikipedia.org/wiki/LinuxCNC
- https://en.wikipedia.org/wiki/RTLinux
- https://en.wikipedia.org/wiki/Multiaxis_machining
