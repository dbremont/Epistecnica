---
tags: [note, production]
---

# Electronic Circuit

tags: EE, Electronic Circuit
: 18

> …
> 

## Electronic Circuit Design Workflow

> …
> 

| **Stage** | **Description** | **Key Activities** | **Tools Used** |
| --- | --- | --- | --- |
| **Specification & Requirements** | Define design objectives, constraints, and performance metrics. | Functional specifications, power/performance targets, technology selection. | Documents, MATLAB, Excel, SystemC |
| **System-Level Design** | High-level modeling and simulation of the system's behavior. | Algorithm development, block diagrams, architectural exploration. | MATLAB, Simulink, SystemC, LabVIEW |
| **Circuit Design & Schematic Capture** | Create a circuit schematic representing the logical connections. | Component selection, circuit topology design, signal flow analysis. | OrCAD Capture, KiCad, Altium Designer, Cadence Virtuoso |
| **Simulation & Verification** | Validate circuit functionality and performance through simulations. | SPICE simulations, functional verification, timing analysis. | LTspice, HSPICE, Cadence Spectre, ModelSim, Verilator |
| **PCB / IC Layout Design** | Convert schematic into a physical layout for fabrication. | Component placement, routing, DRC (Design Rule Check). | Altium Designer, KiCad PCBnew, Cadence Innovus, Synopsys IC Compiler |
| **Physical Verification** | Ensure design adheres to manufacturing constraints and design rules. | DRC, LVS (Layout vs. Schematic), parasitic extraction. | Calibre DRC/LVS, Mentor Graphics PEX, Cadence Assura |
| **Prototyping & Testing** | Build a prototype and validate performance under real-world conditions. | PCB assembly, IC testing, debugging, hardware validation. | Oscilloscope, Logic Analyzer, Multimeter, FPGA Boards |
| **Fabrication & Manufacturing** | Send the design for production as an IC or PCB. | Tape-out for ICs, Gerber file generation for PCBs. | Foundries (TSMC, Intel, GlobalFoundries), PCB manufacturers (JLCPCB, OSHPark) |
| **Post-Manufacturing Validation** | Perform final tests to ensure the fabricated design meets requirements. | Reliability testing, failure analysis, optimization. | Lab Equipment, ATE (Automatic Test Equipment) |

## Design Abstractions

> …
> 
- …
- Transistor-Level Circuit Simulation
- Simulation Program with Integrated Circuit Emphasis (SPICE)

| **Abstraction Level** | **Description** | **Examples** | **Tools Used** |
| --- | --- | --- | --- |
| **System Level** | Models the system behavior without specifying hardware implementation details. | UML Diagrams, Algorithmic Models, SystemC, MATLAB/Simulink | MATLAB, Simulink, SystemC, LabVIEW |
| **Behavioral Level** | Describes the functionality of a circuit using algorithms and data flow without defining the structure. | High-Level Synthesis (HLS), Algorithmic State Machines (ASM), Transaction-Level Modeling (TLM) | C/C++, SystemC, Verilog Behavioral Code, VHDL |
| **Register-Transfer Level (RTL)** | Specifies circuit design in terms of registers, logic operations, and data flow between them. | Verilog, VHDL, FSMs (Finite State Machines) | Vivado, Quartus Prime, Verilator, ModelSim, QuestaSim |
| **Gate Level** | Describes the circuit in terms of logic gates and their connections. | Boolean Expressions, Logic Gate Diagrams, Netlists | Design Compiler, Genus, Synopsys IC Compiler |
| **Transistor Level** | Represents circuits as networks of transistors (e.g., CMOS, FinFET). | CMOS Inverter, NAND/NOR Gates, SPICE Models | Cadence Virtuoso, HSPICE, LTspice |
| **Physical Layout Level** | Defines the actual physical placement of transistors and interconnections on silicon. | GDSII, Standard Cells, Layout Design | Cadence Innovus, Synopsys IC Compiler, Magic VLSI |

## References

- …
- https://github.com/google/skywater-pdk
- https://en.wikipedia.org/wiki/Ngspice
- https://en.wikipedia.org/wiki/Electronic_circuit
- https://en.wikipedia.org/wiki/Process_design_kit
- https://en.wikipedia.org/wiki/Electronic_circuit_simulation