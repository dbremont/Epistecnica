# FreeCAD


> FreeCAD is a powerful, open-source parametric 3D CAD modeler that is widely used for designing real-life objects. It supports various workflows, including **Part Design, Architecture, FEM (Finite Element Analysis), Robotics, and more**.
> 

QA:

- What can be represented?
- How to represent?
- What are the internal abstraction that underlings such representations?

## Uses Cases

| **Category** | **Use Case** | **Description** |
| --- | --- | --- |
| **Mechanical Engineering** | 3D Part Design | Create precise mechanical parts, assemblies, and machinery components. |
|  | Technical Drawings (2D Drafting) | Generate 2D schematics, blueprints, and manufacturing drawings. |
|  | Finite Element Analysis (FEA) | Simulate stress, thermal, and vibration effects on parts using FEM workbench. |
| **Architecture & Construction** | Building Design (BIM) | Model architectural structures, walls, windows, and doors. |
|  | Interior & Space Planning | Design room layouts, furniture, and interior elements. |
|  | Structural Analysis | Evaluate load-bearing structures with reinforcement modeling. |
| **Product Design** | Prototyping & 3D Printing | Design and export models for 3D printing (STL, OBJ). |
|  | Consumer Product Development | Create casings, tools, and ergonomic designs. |
| **Electrical & Electronics** | PCB & Circuit Design | Use KiCad integration for electronic enclosures and PCB layouts. |
|  | Cable & Wiring Routing | Plan cable management in mechanical assemblies. |
| **Automotive & Aerospace** | Vehicle Components | Model car parts, frames, and aerodynamic components. |
|  | Drone & Aircraft Design | Design lightweight structural components for UAVs and aircraft. |
| **Robotics** | Robot Arm & Mechanism Design | Simulate robotic movements and linkages. |
| **Education & Research** | STEM Learning | Teach CAD, parametric modeling, and engineering principles. |
|  | Academic Research (Physics Simulations) | Conduct computational studies in mechanics and material science. |
| **DIY & Hobbyist** | Custom Parts & Repairs | Design replacement parts, tools, or hobby projects (e.g., RC models). |
|  | Woodworking & Crafting | Create CNC-ready designs for woodworking. |
| **Additive Manufacturing** | 3D Printing Optimization | Prepare models with supports, hollowing, and slicing adjustments. |
| **Custom Scripting & Automation** | Python Scripting & Macros | Automate repetitive tasks or extend FreeCAD’s functionality via Python. |

## **Parametric Modeling**

- FreeCAD is **parametric**, meaning objects are defined by parameters (e.g., dimensions, constraints) that can be modified later.
- Changes propagate through the model automatically, updating dependent features.

## **Workbenches**

FreeCAD is organized into **workbenches** (specialized tool sets for different tasks):

- **Part Design**: For creating complex parts with sketches and features (extrusions, pockets, etc.).
- **Part Workbench**: Basic 3D shapes (primitives) and Boolean operations (union, cut, intersect).
- **Sketcher**: 2D constraint-based sketching (used as a base for 3D features).
- **Arch (Architecture)**: BIM (Building Information Modeling) tools.
- **FEM**: Finite Element Analysis for simulations.
- **Draft**: 2D CAD-style drafting.
- **TechDraw**: Generating 2D technical drawings from 3D models.

## **Key Data Structures**

- **Document**: Contains all objects in a project (`.FCStd` file).
- **Objects**: Elements in the document (Part, Sketch, Mesh, etc.).
- **Properties**: Adjustable parameters (length, angle, position).
- **Features**: Operations applied to objects (Pad, Pocket, Fillet, etc.).

## **Dependency Graph**

- FreeCAD maintains a **dependency graph** to track relationships between objects.
- Changing one object affects downstream dependent objects (e.g., modifying a sketch updates an extrusion).

## **Coordinate System & Placement**

- Objects have a **Placement** property (position & rotation in 3D space).
- The **Global Coordinate System (XYZ)** is used as a reference.

## **Constraints (Sketcher)**

- Sketches use **geometric constraints** (e.g., horizontal, vertical, tangent) and **dimensional constraints** (e.g., length, radius).
- A fully constrained sketch has no degrees of freedom.

## **Boolean Operations**

- Used to combine shapes (Union/Cut/Intersection) in the **Part Workbench**.

## **App vs. GUI Separation**

- FreeCAD has a **console mode (`FreeCADCmd`)** for scripting without a GUI.
- The **Python API** allows automation and customization.

## **File Formats**

- Native format: `.FCStd` (FreeCAD Document).
- Exports to: `.STEP`, `.STL`, `.OBJ`, `.DXF`, `.SVG`, etc.

## **Scripting & Automation**

- FreeCAD is **scriptable in Python**.
- Macros can automate repetitive tasks.

## **Basic Workflow Example**

1. **Create a Sketch** (in Sketcher Workbench).
2. **Apply Constraints** (dimensions, geometric relations).
3. **Extrude the Sketch** (Part Design → Pad).
4. **Modify Parameters** (change dimensions, update model).
5. **Export** (e.g., `.STL` for 3D printing).

## References

- https://en.wikipedia.org/wiki/Archicad
- https://github.com/FreeCAD/FreeCAD
- https://www.freecad.org/
- https://wiki.freecad.org/Main_Page
- https://floorplanner.com/
- https://www.reddit.com/r/FreeCAD/
- https://en.wikipedia.org/wiki/Comparison_of_CAD,_CAM,_and_CAE_file_viewers
- https://wiki.freecad.org/Macros_recipes
- https://www.sweethome3d.com/importModels.jsp
- https://wiki.freecad.org/Arch_tutorial