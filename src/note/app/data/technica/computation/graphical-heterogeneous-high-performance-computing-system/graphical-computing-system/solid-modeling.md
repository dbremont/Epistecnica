# Solid Modeling

> "Solid modeling" refers to a **computational representation of three-dimensional solid objects** in a manner that supports unambiguous topology, physical realism, and geometric operations.
> 

## Methods

1. **Manifold Representation**: The model must define a **closed, orientable 2-manifold** (i.e., a boundary that encloses a volume without self-intersections or gaps). This ensures valid topology for volumetric operations.
2. **Boundary Representation (B-rep) or Constructive Solid Geometry (CSG)**:
    - **B-rep** defines a solid using **explicit surfaces**, such as trimmed NURBS patches or polygonal meshes, ensuring connectivity between vertices, edges, and faces.
    - **CSG** represents solids as **boolean combinations** (union, intersection, difference) of primitive volumes like spheres, cylinders, and cubes.
3. **Implicit and Parametric Representations**: Some models use **implicit functions** (e.g., level sets, signed distance fields) to define solids, allowing smooth deformations and robust computational properties. Parametric modeling (e.g., CAD systems) enables constraint-driven modifications.
4. **Topology and Euler-Poincaré Formula**: Valid solid models satisfy the **Euler characteristic** $V - E + F - H = 2(B - G)$, ensuring correct connectivity between vertices $V$, edges $E$, faces $F$, holes $H$, genus $G$, and shells $B$.
5. **Boolean Operations and Feature-Based Design**:
    - Solid models support **robust boolean operations** (set-theoretic operations on 3D volumes).
    - Many modern systems use **feature-based modeling**, where objects are built via a history tree of operations.
6. **Volume and Mass Properties**: Solid models inherently support **mass property calculations** (e.g., volume, centroid, moment of inertia), essential for engineering analysis (FEA, CFD).
7. **Interoperability with Manufacturing and Simulation**: Solid models must integrate with **CAM (Computer-Aided Manufacturing), FEA (Finite Element Analysis), and CNC toolpath generation**, often requiring high-fidelity representations such as STEP, IGES, or Parasolid formats.

## References

- https://en.wikipedia.org/wiki/Solid_modeling