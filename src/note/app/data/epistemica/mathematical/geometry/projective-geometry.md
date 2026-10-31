---
tags: [framework, geometry]
---

# Projective Geometry

 : Coordinate System (Coordinate%20System%207763fb7722714fa6a95098fd9f1cae44.md), Homogeneous Function (Homogeneous%20Function%20206c0f5171ec80689b80f1933cf6d93e.md)

> **Projective geometry** is a branch of geometry that studies properties of figures that remain **invariant under projection**. It generalizes Euclidean geometry by adding **"points at infinity"** so that parallel lines meet, and it focuses on the relationships between geometric elements rather than measurements like distance or angles.
> 

## 🧭 **Key Ideas of Projective Geometry**

1. **Points at Infinity:** In projective geometry, all lines intersect — even parallel lines. Parallel lines meet at a "point at infinity," which lies on the "line at infinity" (a conceptual addition to the plane).
2. **Homogeneous Coordinates:** Points are represented with **homogeneous coordinates**. A point   in 2D Euclidean space becomes $(x, y, 1)$, and a point at infinity has coordinates like $(x, y, 0)$. This makes projective transformations linear.
3. **Projection:** A central operation is the **projection** of points from one plane to another through a **center of projection** (like a camera lens). This operation preserves **incidence** (which points lie on which lines) but not angles or lengths.
4. **Duality Principle:**  Every theorem in projective geometry has a **dual**, where "points" and "lines" are interchanged. For example:  "Two points determine a line" becomes "Two lines determine a point" (their intersection).
5. **Cross-Ratio Invariance**
    
    A key invariant in projective geometry is the **cross-ratio** of four collinear points:
    
    $(A, B; C, D) = \frac{AC \cdot BD}{AD \cdot BC}$  It remains constant under projective transformations.
    
6. **Projective Transformations (Homographies):** These are transformations that preserve the projective structure. In 2D, they're represented by 3×3 invertible matrices acting on homogeneous coordinates.

## 🔷 **Homogeneous Coordinate System**

> The **homogeneous coordinate system** is a mathematical framework used in **projective geometry** (and extensively in **computer graphics**, **robotics**, and **computer vision**) to represent points, lines, and transformations in a way that naturally includes **points at infinity** and **perspective transformations**.
> 

A point in **homogeneous coordinates** is an **(n+1)-tuple** that represents a point in **n-dimensional projective space**: $(x_0 : x_1 : \dots : x_n)$

These coordinates are **not unique**: $(x_0 : x_1 : \dots : x_n) \sim (\lambda x_0 : \lambda x_1 : \dots : \lambda x_n), \quad \lambda \ne 0$

This defines a point as an **equivalence class** of scalar multiples.

For a point $(x, y) \in \mathbb{R}^2$, the homogeneous form is: $(x : y : 1)$

To move back to Cartesian coordinates:  $(x, y) = \left( \frac{x}{z}, \frac{y}{z} \right)
\quad \text{if } z \ne 0$

If $z = 0$, the point lies **at infinity**.

## 🧮 Euclidean vs Projective Geometry

| Property | Euclidean Geometry | Projective Geometry |
| --- | --- | --- |
| Parallel lines | Never meet | Intersect at a point at infinity |
| Distance and angle | Preserved | Not preserved |
| Coordinates | Cartesian | Homogeneous |
| Transformations | Rigid or affine | Projective (homographies) |
| Key invariant | Lengths, angles | Cross-ratio |

## 📷 Applications

- **Computer Vision**: Modeling cameras (pinhole model), perspective distortion.
- **Graphics**: Perspective projection in 3D rendering.
- **Art**: Renaissance perspective techniques.
- **Algebraic Geometry**: Understanding curves and surfaces in projective space.

## References

- https://en.wikipedia.org/wiki/Projective_geometry
