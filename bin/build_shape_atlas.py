#!/usr/bin/env python3
"""Build the Geometric Shape Atlas store.

Parses the recursive instance-decomposition table of
`epistemica/mathematical/geometry/geometric-shape.md` and writes the
figure-first atlas store beside it:

    src/corpus/notes/epistemica/mathematical/geometry/atlas.json

Every table row becomes one node under the `Geometric Shape` root.  The
node keeps its table path, description, family (the top-level branch),
dimension, optional corpus-note link, and a `figure` specification the
atlas page turns into an inline SVG.

The table is the source of truth; the store is generated data and should
never be hand-edited.  Run:

    make shape-atlas-index

or `make index`.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

from indexlib import Progress, atomic_write_text, run_builder

REPO = Path(__file__).resolve().parent.parent
NOTES = REPO / "src" / "corpus" / "notes"
SOURCE = NOTES / "epistemica" / "mathematical" / "geometry" / "geometric-shape.md"
OUT = SOURCE.with_name("atlas.json")
ROOT_LABEL = "Geometric Shape"

FAMILY_ORDER = [
    "Elemental Shapes",
    "One-Dimensional Shapes",
    "Planar Shapes",
    "Spherical Shapes",
    "Hyperbolic Shapes",
    "Solid Shapes",
    "Higher-Dimensional Shapes",
    "Shape Arrangements",
    "Shape Properties",
]

FAMILIES = {
    "Elemental Shapes": {
        "id": "elemental-shapes",
        "color": "--accent-cyan",
        "dimension": "degenerate",
        "essence": "The degenerate forms with empty interior in their ambient space.",
    },
    "One-Dimensional Shapes": {
        "id": "one-dimensional-shapes",
        "color": "--accent-violet",
        "dimension": "1d",
        "essence": "Curves and the pieces curves are built from.",
    },
    "Planar Shapes": {
        "id": "planar-shapes",
        "color": "--accent-copper",
        "dimension": "2d",
        "essence": "Polygonal and curved regions of the plane.",
    },
    "Spherical Shapes": {
        "id": "spherical-shapes",
        "color": "--accent-sage",
        "dimension": "curved-2d",
        "essence": "Figures drawn on a sphere, where angle sums exceed the Euclidean.",
    },
    "Hyperbolic Shapes": {
        "id": "hyperbolic-shapes",
        "color": "--accent-plum",
        "dimension": "curved-2d",
        "essence": "Figures drawn in hyperbolic space, where angle sums fall short.",
    },
    "Solid Shapes": {
        "id": "solid-shapes",
        "color": "--accent-gold",
        "dimension": "3d",
        "essence": "Polyhedra, quadric surfaces, and closed surfaces in three dimensions.",
    },
    "Higher-Dimensional Shapes": {
        "id": "higher-dimensional-shapes",
        "color": "--accent-rose",
        "dimension": "nd",
        "essence": "Polytopes, balls, and spheres beyond three dimensions.",
    },
    "Shape Arrangements": {
        "id": "shape-arrangements",
        "color": "--accent-amber",
        "dimension": "mixed",
        "essence": "Shapes taken together: compounds, tessellations, and packings.",
    },
    "Shape Properties": {
        "id": "shape-properties",
        "color": "--accent-steel",
        "dimension": "property",
        "essence": "Predicates asserted of a shape rather than figures beside it.",
    },
}

DIMENSIONS = [
    {"id": "degenerate", "name": "Degenerate"},
    {"id": "1d", "name": "1D"},
    {"id": "2d", "name": "2D"},
    {"id": "curved-2d", "name": "Curved 2D"},
    {"id": "3d", "name": "3D"},
    {"id": "nd", "name": "nD"},
    {"id": "mixed", "name": "Mixed"},
    {"id": "property", "name": "Property"},
]

TRIANGLES = {
    "Triangle", "Equilateral Triangle", "Isosceles Triangle", "Scalene Triangle",
    "Right Triangle", "Acute Triangle", "Obtuse Triangle", "Isosceles Right Triangle",
    "Golden Triangle", "30-60-90 Triangle", "Heronian Triangle", "Equable Triangle",
    "Golden Gnomon",
}

QUADRILATERALS = {
    "Quadrilateral", "Rectangle", "Square", "Parallelogram", "Rhombus",
    "Trapezoid", "Isosceles Trapezoid", "Right Trapezoid", "Kite", "Dart",
    "Trapezium", "Cyclic Quadrilateral", "Tangential Quadrilateral",
    "Antiparallelogram", "Orthodiagonal Quadrilateral", "Equidiagonal Quadrilateral",
    "Bicentric Quadrilateral", "Ex-tangential Quadrilateral",
}

POLYGON_SIDES = {
    "Pentagon": 5, "Regular Pentagon": 5,
    "Hexagon": 6, "Regular Hexagon": 6,
    "Heptagon": 7,
    "Octagon": 8, "Regular Octagon": 8,
    "Nonagon": 9,
    "Decagon": 10,
    "Hendecagon": 11,
    "Dodecagon": 12,
    "N-gon": 7,
    "Regular Polygon": 6,
}

STAR_POLYGONS = {
    "Pentagram": (5, 2),
    "Hexagram": (6, 2),
    "Octagram": (8, 3),
    "Heptagram": (7, 3),
    "Enneagram": (9, 2),
    "Decagram": (10, 3),
    "Hendecagram": (11, 2),
    "Dodecagram": (12, 5),
}

EXACT_FIGURES = {
    # Elemental
    "Point": {"kind": "point"},
    "Line": {"kind": "line"},
    "Line Segment": {"kind": "segment"},
    "Ray": {"kind": "ray"},
    "Plane": {"kind": "plane"},
    "Hyperplane": {"kind": "hyperplane"},
    # Curves
    "Curve": {"kind": "curve", "variant": "generic"},
    "Simple Curve": {"kind": "curve", "variant": "simple"},
    "Closed Curve": {"kind": "curve", "variant": "closed"},
    "Jordan Curve": {"kind": "curve", "variant": "jordan"},
    "Space Curve": {"kind": "curve", "variant": "space"},
    "Unknot": {"kind": "curve", "variant": "unknot"},
    "Trefoil Knot": {"kind": "curve", "variant": "trefoil"},
    "Figure-Eight Knot": {"kind": "curve", "variant": "figure-eight"},
    "Hopf Link": {"kind": "curve", "variant": "hopf"},
    "Conic Section": {"kind": "curve", "variant": "conic"},
    "Parabola": {"kind": "curve", "variant": "parabola"},
    "Hyperbola": {"kind": "curve", "variant": "hyperbola"},
    "Degenerate Conic": {"kind": "curve", "variant": "degenerate-conic"},
    "Cycloid": {"kind": "curve", "variant": "cycloid"},
    "Epicycloid": {"kind": "curve", "variant": "epicycloid"},
    "Hypocycloid": {"kind": "curve", "variant": "hypocycloid"},
    "Astroid": {"kind": "curve", "variant": "astroid"},
    "Deltoid": {"kind": "curve", "variant": "deltoid"},
    "Epitrochoid": {"kind": "curve", "variant": "epitrochoid"},
    "Hypotrochoid": {"kind": "curve", "variant": "hypotrochoid"},
    "Catenary": {"kind": "curve", "variant": "catenary"},
    "Tractrix": {"kind": "curve", "variant": "tractrix"},
    "Clothoid": {"kind": "curve", "variant": "clothoid"},
    "Lemniscate": {"kind": "curve", "variant": "lemniscate"},
    "Lemniscate of Bernoulli": {"kind": "curve", "variant": "lemniscate"},
    "Lemniscate of Gerono": {"kind": "curve", "variant": "lemniscate"},
    "Cassini Oval": {"kind": "curve", "variant": "cassini"},
    "Lissajous Curve": {"kind": "curve", "variant": "lissajous"},
    "Rose Curve": {"kind": "curve", "variant": "rose"},
    "Superellipse": {"kind": "curve", "variant": "superellipse"},
    "Witch of Agnesi": {"kind": "curve", "variant": "witch"},
    "Cissoid of Diocles": {"kind": "curve", "variant": "cissoid"},
    "Conchoid of Nicomedes": {"kind": "curve", "variant": "conchoid"},
    "Folium of Descartes": {"kind": "curve", "variant": "folium"},
    "Strophoid": {"kind": "curve", "variant": "strophoid"},
    "Elliptic Curve": {"kind": "curve", "variant": "elliptic"},
    "Polygonal Chain": {"kind": "polyline"},
    "Arc": {"kind": "arc"},
    "Circle": {"kind": "circle"},
    "Spiral": {"kind": "spiral", "variant": "archimedean"},
    "Archimedean Spiral": {"kind": "spiral", "variant": "archimedean"},
    "Logarithmic Spiral": {"kind": "spiral", "variant": "logarithmic"},
    "Spiral of Theodorus": {"kind": "spiral", "variant": "theodorus"},
    "Helix": {"kind": "helix", "variant": "helix"},
    "Conical Spiral": {"kind": "helix", "variant": "conical"},
    "Spline": {"kind": "spline", "variant": "bezier"},
    "Bézier Curve": {"kind": "spline", "variant": "bezier"},
    "B-Spline": {"kind": "spline", "variant": "b-spline"},
    "NURBS": {"kind": "spline", "variant": "nurbs"},
    # Planar non-polygonal
    "Disk": {"kind": "disk", "variant": "disk"},
    "Semicircle": {"kind": "disk", "variant": "semicircle"},
    "Crescent": {"kind": "disk", "variant": "crescent"},
    "Reuleaux Triangle": {"kind": "disk", "variant": "reuleaux"},
    "Stadium": {"kind": "disk", "variant": "stadium"},
    "Ellipse": {"kind": "ellipse"},
    "Annulus": {"kind": "annulus"},
    "Circular Sector": {"kind": "sector"},
    "Circular Segment": {"kind": "segment-region"},
    "Lens": {"kind": "lens"},
    "Cardioid": {"kind": "cardioid"},
    "Parabolic Region": {"kind": "parabolic-region"},
    # Spherical / hyperbolic
    "Spherical Triangle": {"kind": "surface", "variant": "spherical-triangle"},
    "Spherical Lune": {"kind": "surface", "variant": "spherical-lune"},
    "Spherical Cap": {"kind": "surface", "variant": "spherical-cap"},
    "Spherical Polygon": {"kind": "surface", "variant": "spherical-polygon"},
    "Hyperbolic Triangle": {"kind": "surface", "variant": "hyperbolic-triangle"},
    "Ideal Triangle": {"kind": "surface", "variant": "ideal-triangle"},
    # Solids
    "Polyhedron": {"kind": "polyhedron", "variant": "generic"},
    "Prism": {"kind": "polyhedron", "variant": "prism"},
    "Rectangular Prism": {"kind": "polyhedron", "variant": "prism"},
    "Triangular Prism": {"kind": "polyhedron", "variant": "prism"},
    "Pentagonal Prism": {"kind": "polyhedron", "variant": "prism"},
    "Hexagonal Prism": {"kind": "polyhedron", "variant": "prism"},
    "Oblique Prism": {"kind": "polyhedron", "variant": "prism"},
    "Parallelepiped": {"kind": "polyhedron", "variant": "prism"},
    "Rhombohedron": {"kind": "polyhedron", "variant": "prism"},
    "Pyramid": {"kind": "polyhedron", "variant": "pyramid"},
    "Square Pyramid": {"kind": "polyhedron", "variant": "pyramid"},
    "Triangular Pyramid": {"kind": "polyhedron", "variant": "pyramid"},
    "Pentagonal Pyramid": {"kind": "polyhedron", "variant": "pyramid"},
    "Oblique Pyramid": {"kind": "polyhedron", "variant": "pyramid"},
    "Frustum": {"kind": "polyhedron", "variant": "frustum"},
    "Antiprism": {"kind": "polyhedron", "variant": "antiprism"},
    "Platonic Solid": {"kind": "polyhedron", "variant": "generic"},
    "Tetrahedron": {"kind": "polyhedron", "variant": "tetrahedron"},
    "Disphenoid": {"kind": "polyhedron", "variant": "tetrahedron"},
    "Trirectangular Tetrahedron": {"kind": "polyhedron", "variant": "tetrahedron"},
    "Orthoscheme": {"kind": "polyhedron", "variant": "tetrahedron"},
    "Cube": {"kind": "polyhedron", "variant": "cube"},
    "Octahedron": {"kind": "polyhedron", "variant": "octahedron"},
    "Dodecahedron": {"kind": "polyhedron", "variant": "dodecahedron"},
    "Icosahedron": {"kind": "polyhedron", "variant": "icosahedron"},
    "Archimedean Solid": {"kind": "polyhedron", "variant": "generic"},
    "Johnson Solid": {"kind": "polyhedron", "variant": "generic"},
    "Deltahedron": {"kind": "polyhedron", "variant": "generic"},
    "Bipyramid": {"kind": "polyhedron", "variant": "bipyramid"},
    "Trapezohedron": {"kind": "polyhedron", "variant": "generic"},
    "Prismatoid": {"kind": "polyhedron", "variant": "frustum"},
    "Cupola": {"kind": "polyhedron", "variant": "generic"},
    "Rotunda": {"kind": "polyhedron", "variant": "generic"},
    "Wedge": {"kind": "polyhedron", "variant": "prism"},
    "Sphenoid": {"kind": "polyhedron", "variant": "tetrahedron"},
    "Zonohedron": {"kind": "polyhedron", "variant": "generic"},
    "Toroidal Polyhedron": {"kind": "polyhedron", "variant": "torus"},
    "Kepler–Poinsot Solid": {"kind": "polyhedron", "variant": "star"},
    "Small Stellated Dodecahedron": {"kind": "polyhedron", "variant": "star"},
    "Great Dodecahedron": {"kind": "polyhedron", "variant": "star"},
    "Great Stellated Dodecahedron": {"kind": "polyhedron", "variant": "star"},
    "Great Icosahedron": {"kind": "polyhedron", "variant": "star"},
    "Catalan Solid": {"kind": "polyhedron", "variant": "generic"},
    "Quadric Surface": {"kind": "quadric", "variant": "generic"},
    "Sphere": {"kind": "quadric", "variant": "sphere"},
    "Hemisphere": {"kind": "quadric", "variant": "hemisphere"},
    "Ellipsoid": {"kind": "quadric", "variant": "ellipsoid"},
    "Paraboloid": {"kind": "quadric", "variant": "paraboloid"},
    "Hyperboloid": {"kind": "quadric", "variant": "hyperboloid"},
    "Cylinder": {"kind": "quadric", "variant": "cylinder"},
    "Right Circular Cylinder": {"kind": "quadric", "variant": "cylinder"},
    "Oblique Cylinder": {"kind": "quadric", "variant": "cylinder"},
    "Elliptic Cylinder": {"kind": "quadric", "variant": "cylinder"},
    "Cone": {"kind": "quadric", "variant": "cone"},
    "Right Circular Cone": {"kind": "quadric", "variant": "cone"},
    "Oblique Cone": {"kind": "quadric", "variant": "cone"},
    "Double Cone": {"kind": "quadric", "variant": "double-cone"},
    "Hyperbolic Paraboloid": {"kind": "quadric", "variant": "saddle"},
    "Monkey Saddle": {"kind": "quadric", "variant": "saddle"},
    "Torus": {"kind": "torus", "variant": "torus"},
    "Spindle Torus": {"kind": "torus", "variant": "spindle"},
    "Horn Torus": {"kind": "torus", "variant": "horn"},
    "Solid Torus": {"kind": "torus", "variant": "solid"},
    "Möbius Strip": {"kind": "surface", "variant": "mobius"},
    "Klein Bottle": {"kind": "surface", "variant": "klein"},
    "Surface of Revolution": {"kind": "surface", "variant": "revolution"},
    "Fractal Solid": {"kind": "fractal", "variant": "fractal-solid"},
    "Menger Sponge": {"kind": "fractal", "variant": "menger"},
    "Sierpiński Tetrahedron": {"kind": "fractal", "variant": "sierpinski-tetrahedron"},
    "Ruled Surface": {"kind": "surface", "variant": "ruled"},
    "Developable Surface": {"kind": "surface", "variant": "ruled"},
    "Minimal Surface": {"kind": "surface", "variant": "minimal"},
    "Catenoid": {"kind": "surface", "variant": "catenoid"},
    "Helicoid": {"kind": "surface", "variant": "helicoid"},
    "Enneper Surface": {"kind": "surface", "variant": "minimal"},
    "Scherk Surface": {"kind": "surface", "variant": "minimal"},
    "Gyroid": {"kind": "surface", "variant": "minimal"},
    "Pseudosphere": {"kind": "surface", "variant": "pseudosphere"},
    "Boy's Surface": {"kind": "surface", "variant": "boys"},
    "Roman Surface": {"kind": "surface", "variant": "roman"},
    "Cross-Cap": {"kind": "surface", "variant": "cross-cap"},
    "Real Projective Plane": {"kind": "surface", "variant": "projective"},
    "Dini's Surface": {"kind": "surface", "variant": "dini"},
    # Higher-dimensional
    "Polytope": {"kind": "polytope", "variant": "generic"},
    "Simplex": {"kind": "polytope", "variant": "simplex"},
    "Hypercube": {"kind": "polytope", "variant": "hypercube"},
    "Tesseract": {"kind": "polytope", "variant": "hypercube"},
    "Cross-Polytope": {"kind": "polytope", "variant": "cross-polytope"},
    "Regular Polytope": {"kind": "polytope", "variant": "generic"},
    "24-Cell": {"kind": "polytope", "variant": "cell"},
    "120-Cell": {"kind": "polytope", "variant": "cell"},
    "600-Cell": {"kind": "polytope", "variant": "cell"},
    "Demihypercube": {"kind": "polytope", "variant": "hypercube"},
    "Hypersimplex": {"kind": "polytope", "variant": "simplex"},
    "Duoprism": {"kind": "polytope", "variant": "prism"},
    "Duocylinder": {"kind": "polytope", "variant": "cylinder"},
    "Hypercone": {"kind": "polytope", "variant": "cone"},
    "Zonotope": {"kind": "polytope", "variant": "generic"},
    "Permutohedron": {"kind": "polytope", "variant": "generic"},
    "Associahedron": {"kind": "polytope", "variant": "generic"},
    "Ball": {"kind": "ball"},
    "Hypersphere": {"kind": "hypersphere"},
    "3-Sphere": {"kind": "hypersphere"},
    "N-Torus": {"kind": "n-torus"},
    # Arrangements
    "Compound Shape": {"kind": "arrangement", "variant": "compound"},
    "Cross": {"kind": "arrangement", "variant": "cross"},
    "Yin-Yang": {"kind": "arrangement", "variant": "yin-yang"},
    "Stellated Octahedron": {"kind": "arrangement", "variant": "stellated-octahedron"},
    "Compound of Cube and Octahedron": {"kind": "arrangement", "variant": "cube-octahedron"},
    "Tessellation": {"kind": "arrangement", "variant": "tessellation"},
    "Regular Tessellation": {"kind": "arrangement", "variant": "tessellation"},
    "Archimedean Tessellation": {"kind": "arrangement", "variant": "tessellation"},
    "Voronoi Diagram": {"kind": "arrangement", "variant": "voronoi"},
    "Delaunay Triangulation": {"kind": "arrangement", "variant": "delaunay"},
    "Aperiodic Tessellation": {"kind": "arrangement", "variant": "penrose"},
    "Penrose Tiling": {"kind": "arrangement", "variant": "penrose"},
    "Packing": {"kind": "arrangement", "variant": "packing"},
    "Circle Packing": {"kind": "arrangement", "variant": "circle-packing"},
    "Sphere Packing": {"kind": "arrangement", "variant": "sphere-packing"},
    "Hexagonal Close Packing": {"kind": "arrangement", "variant": "sphere-packing"},
}


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def strip_md(text: str) -> str:
    """Plain display text: keep link labels and math, drop markdown syntax."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("`", "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def link_targets(text: str) -> list[str]:
    """Corpus-note paths named by explicit markdown links in a description."""
    found = []
    for target in re.findall(r"\]\(([^)]+)\)", text):
        path = None
        m = re.search(r"[?&]p=notes/([^&#]+)", target)
        if m:
            path = m.group(1)
        elif target.startswith("/corpus/notes/"):
            path = target[len("/corpus/notes/"):]
        elif target.startswith("notes/"):
            path = target[len("notes/"):]
        if path:
            path = path.split("#", 1)[0].split("?", 1)[0]
            if path.endswith(".md") or path.endswith(".html"):
                found.append(path)
    return found


def table_rows(text: str):
    """Yield (path_cell, description) for the decomposition table rows."""
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or not line.endswith("|"):
            continue
        if "Epistemic Element" not in line or "Geometric Shape" not in line:
            continue
        inner = line[1:-1]
        if " | " not in inner:
            continue
        path, desc = inner.split(" | ", 1)
        yield path, desc.strip()


def path_names(path_cell: str) -> list[str]:
    """Shape labels below the `Geometric Shape` root in one table path."""
    tokens = []
    for match in re.finditer(r"`([^`]*)`|([^`]+)", path_cell):
        code, plain = match.group(1), match.group(2)
        if code is not None:
            inner = code.strip()
            if re.fullmatch(r"\(\s*(?:→|->)\s*.+?\)", inner):
                continue
            tokens.append(("type", inner))
        else:
            text = re.sub(r"\(\s*(?:→|->)\s*.+?\)", " ", plain)
            for part in re.split(r"\s{2,}", text):
                part = part.strip()
                if part:
                    tokens.append(("text", part))

    start = next((i for i, (kind, value) in enumerate(tokens)
                  if kind == "text" and value == ROOT_LABEL), None)
    if start is None:
        return []

    names = []
    is_property = False
    for kind, value in tokens[start + 1:]:
        if kind == "type":
            if value == "Property":
                is_property = True
            continue
        names.append(value)
    if is_property:
        names.insert(0, "Shape Properties")
    return names


class Node:
    def __init__(self, label: str, names: list[str], family: str):
        self.label = label
        self.names = names
        self.family = family
        self.description = ""
        self.note = None
        self.children: list[Node] = []

    def child(self, label: str) -> "Node":
        for node in self.children:
            if node.label == label:
                return node
        # Top-level branches own their family; deeper nodes inherit it.
        family = label if self.label == ROOT_LABEL else self.family
        node = Node(label, self.names + [label], family)
        self.children.append(node)
        return node


def family_id(name: str) -> str:
    return FAMILIES.get(name, {}).get("id", slug(name))


def family_dimension(name: str) -> str:
    return FAMILIES.get(name, {}).get("dimension", "mixed")


def figure_for(label: str, family: str, kind: str) -> dict:
    if kind == "root":
        return {"kind": "family", "variant": "root"}
    if kind == "family":
        return {"kind": "family", "variant": family_id(family)}
    if family == "Shape Properties":
        return {"kind": "property", "variant": slug(label)}
    if label in EXACT_FIGURES:
        return dict(EXACT_FIGURES[label])

    if label in TRIANGLES:
        variant = {
            "Triangle": "generic", "Equilateral Triangle": "equilateral",
            "Isosceles Triangle": "isosceles", "Scalene Triangle": "scalene",
            "Right Triangle": "right", "Acute Triangle": "acute",
            "Obtuse Triangle": "obtuse", "Isosceles Right Triangle": "isosceles-right",
            "Golden Triangle": "golden", "30-60-90 Triangle": "30-60-90",
            "Heronian Triangle": "3-4-5", "Equable Triangle": "equable",
            "Golden Gnomon": "golden-gnomon",
        }.get(label, "generic")
        return {"kind": "triangle", "variant": variant}

    if label in QUADRILATERALS:
        return {"kind": "quadrilateral", "variant": slug(label)}

    if label in POLYGON_SIDES:
        return {"kind": "polygon", "sides": POLYGON_SIDES[label]}

    if label in STAR_POLYGONS:
        sides, step = STAR_POLYGONS[label]
        return {"kind": "polygon", "sides": sides, "step": step, "variant": "star"}

    if label == "Star Polygon":
        return {"kind": "polygon", "sides": 5, "step": 2, "variant": "star"}
    if label == "Degenerate Polygon":
        return {"kind": "polygon", "sides": 4, "variant": "degenerate"}
    if label == "Monogon":
        return {"kind": "polygon", "sides": 1, "variant": "degenerate"}
    if label == "Digon":
        return {"kind": "polygon", "sides": 2, "variant": "degenerate"}
    if label == "Apeirogon":
        return {"kind": "polygon", "sides": 18, "variant": "apeirogon"}
    if label in ("Equilateral Polygon", "Equiangular Polygon",
                 "Cyclic Polygon", "Tangential Polygon"):
        return {"kind": "polygon", "sides": 6, "variant": slug(label)}

    if label == "Fractal Curve":
        return {"kind": "fractal", "variant": "koch-curve"}
    if label == "Fractal Region":
        return {"kind": "fractal", "variant": "sierpinski-triangle"}
    if label in ("Koch Curve", "Dragon Curve", "Hilbert Curve", "Lévy C Curve",
                 "Minkowski Sausage", "Moore Curve", "Sierpiński Curve",
                 "Gosper Curve", "Peano Curve"):
        variant = {
            "Lévy C Curve": "levy-c-curve",
            "Sierpiński Curve": "sierpinski-curve",
        }.get(label, slug(label))
        return {"kind": "fractal", "variant": variant}
    if label in ("Sierpinski Triangle", "Sierpinski Carpet", "Koch Snowflake",
                 "Mandelbrot Set", "Julia Set", "Apollonian Gasket", "Cantor Dust",
                 "Vicsek Fractal"):
        return {"kind": "fractal", "variant": slug(label)}

    fallback = {
        "Elemental Shapes": {"kind": "family", "variant": "elemental-shapes"},
        "One-Dimensional Shapes": {"kind": "curve", "variant": "generic"},
        "Planar Shapes": {"kind": "polygon", "sides": 5},
        "Spherical Shapes": {"kind": "surface", "variant": "spherical-triangle"},
        "Hyperbolic Shapes": {"kind": "surface", "variant": "hyperbolic-triangle"},
        "Solid Shapes": {"kind": "polyhedron", "variant": "cube"},
        "Higher-Dimensional Shapes": {"kind": "polytope", "variant": "hypercube"},
        "Shape Arrangements": {"kind": "arrangement", "variant": "tessellation"},
        "Shape Properties": {"kind": "property", "variant": "dimension"},
    }
    return dict(fallback.get(family, {"kind": "generic", "variant": family_id(family)}))


def note_index() -> tuple[dict, dict]:
    """Unambiguous title and stem maps for the geometry corpus."""
    titles: dict[str, set[str]] = {}
    stems: dict[str, set[str]] = {}
    for path in sorted((NOTES / "epistemica" / "mathematical" / "geometry").rglob("*.md")):
        rel = path.relative_to(NOTES).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"^#\s+(.+?)\s*$", text, re.M)
        title = strip_md(match.group(1)) if match else path.stem.replace("-", " ")
        titles.setdefault(slug(title), set()).add(rel)
        stems.setdefault(slug(path.stem), set()).add(rel)
    return titles, stems


def resolve_note(label: str, explicit: list[str], titles: dict, stems: dict) -> str | None:
    for path in explicit:
        if (NOTES / path).is_file():
            return path
    for table in (titles, stems):
        found = table.get(slug(label), set())
        if len(found) == 1:
            return next(iter(found))
    return None


def serialise(node: Node, kind: str, titles: dict, stems: dict, depth: int, stats: dict) -> dict:
    family = node.family
    explicit = link_targets(node.description)
    note = node.note or resolve_note(node.label, explicit, titles, stems)
    if note and not (NOTES / note).is_file():
        note = None
    figure = figure_for(node.label, family, kind)
    out = {
        "id": "-".join(slug(x) for x in ([ROOT_LABEL] + node.names[1:])),
        "label": node.label,
        "kind": kind,
        "family": family_id(family) if kind != "root" else "geometric-shape",
        "dimension": family_dimension(family) if kind != "root" else "mixed",
        "path": " → ".join([ROOT_LABEL] + node.names[1:]),
        "description": strip_md(node.description),
        "figure": figure,
        "children": [],
    }
    if note:
        out["note"] = note
    stats["nodes"] += 1
    stats["maxDepth"] = max(stats["maxDepth"], depth)
    stats["figures"] += 1
    for child in node.children:
        child_kind = "family" if depth == 1 else (
            "property" if child.family == "Shape Properties" else "shape")
        out["children"].append(serialise(child, child_kind, titles, stems, depth + 1, stats))
    return out


def build(progress: Progress | None = None) -> bool:
    if not SOURCE.is_file():
        print(f"shape-atlas: missing source {SOURCE}", file=sys.stderr)
        return False
    text = SOURCE.read_text(encoding="utf-8", errors="replace")
    root = Node(ROOT_LABEL, [ROOT_LABEL], "Geometric Shape")
    root.description = "The form a figure carries — the orbit of a point set under a declared transformation group."
    row_count = 0
    for path_cell, desc in table_rows(text):
        row_count += 1
        names = path_names(path_cell)
        if not names:
            if desc:
                root.description = strip_md(desc)
            continue
        family = names[0]
        parent = root
        for label in names:
            parent = parent.child(label)
        if desc and not parent.description:
            parent.description = desc

    if not root.children:
        print("shape-atlas: no decomposition rows found", file=sys.stderr)
        return False

    # The property rows create this branch implicitly; give it its family text.
    for child in root.children:
        if child.label == "Shape Properties" and not child.description:
            child.description = FAMILIES["Shape Properties"]["essence"]

    titles, stems = note_index()
    root.note = "epistemica/mathematical/geometry/geometric-shape.md"
    stats = {"rows": row_count, "nodes": 0, "families": 0,
             "maxDepth": 0, "figures": 0}
    tree = serialise(root, "root", titles, stems, 1, stats)
    stats["families"] = len(tree["children"])

    def walk(node: dict):
        yield node
        for child in node.get("children", []):
            yield from walk(child)

    family_counts = Counter(node["family"] for node in walk(tree))
    today = date.today().isoformat()
    store = {
        "title": "Geometric Shape Atlas",
        "abbr": "GSA",
        "version": today,
        "generated": today,
        "subtitle": "The figures of geometry, from the point and the ray to the solid and the polytope.",
        "intro": (
            "Every geometric shape in the corpus decomposition, rendered as a figure and "
            "read as a path. The atlas follows the table in the Geometric Shape note: "
            "elemental forms first, then curves, planar and curved regions, solids, "
            "higher-dimensional polytopes, and arrangements."
        ),
        "source": "generated from epistemica/mathematical/geometry/geometric-shape.md",
        "note": "epistemica/mathematical/geometry/geometric-shape.md",
        "families": [
            {
                "id": FAMILIES[name]["id"],
                "name": name,
                "color": FAMILIES[name]["color"],
                "essence": FAMILIES[name]["essence"],
                "dimension": FAMILIES[name]["dimension"],
                "count": family_counts.get(FAMILIES[name]["id"], 0),
            }
            for name in FAMILY_ORDER
            if name in {c.family for c in root.children}
        ],
        "dimensions": DIMENSIONS,
        "stats": stats,
        "roots": [tree],
    }
    atomic_write_text(OUT, json.dumps(store, indent=2, ensure_ascii=False) + "\n")
    print(
        f"shape-atlas: {stats['rows']} table rows -> {stats['nodes']} nodes, "
        f"{stats['families']} families, depth {stats['maxDepth']}, "
        f"{stats['figures']} figures -> {OUT.relative_to(REPO)}"
    )
    if progress is not None:
        progress.set_total(stats["nodes"])
        progress.start("writing Geometric Shape Atlas")
        progress.step(stats["nodes"], f"{stats['nodes']} nodes")
        progress.finish(f"{stats['nodes']} nodes")
    return True


def main() -> int:
    return run_builder("shape-atlas", build)


if __name__ == "__main__":
    sys.exit(main())
