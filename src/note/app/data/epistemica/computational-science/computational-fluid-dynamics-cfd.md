---
tags: [framework]
---

# Computational Fluid Dynamics (CFD)

   :  Navier–Stokes Equations (Navier%E2%80%93Stokes%20Equations%2022cc0f5171ec8096933dfc80a6337ea0.md), Continuum Mechanic Framework (Continuum%20Mechanic%20Framework%201a1c0f5171ec801c9d1bedf4aa03f703.md), Lattice Boltzmann Method (Lattice%20Boltzmann%20Method%2022dc0f5171ec8082a117f5a016be4f70.md)

> CFD simulations simulate the flow of fluids and gases using numerical methods. They are used to investigate the behavior of fluids and gases in chemical reactions.
> 

> Note: **Fluid Dynamic** is Part of **Continuum Mechanics**.
> 

## Unifying Framework

| **Aspect** | **Description** |
| --- | --- |
| **Fundamental Framework** | **Navier-Stokes Equations** — partial differential equations governing conservation of mass, momentum, and energy in fluids. |
| **Core Variables** | Velocity field **u(x,t)**, pressure **p(x,t)**, density **ρ(x,t)**, temperature **T(x,t)**. |
| **Governing Principles** | **Conservation of Mass** (Continuity equation) |
|  | **Conservation of Momentum** (Newton’s Second Law applied to fluid parcels) |
|  | - **Conservation of Energy** (First Law of Thermodynamics in fluid context) |
| **Dimensionless Numbers** | Characterize flow regimes and similarity: |
|  | - Reynolds number (Re) — ratio of inertial to viscous forces |
|  | - Mach number (Ma) — ratio of flow velocity to speed of sound |
|  | - Prandtl, Grashof, Froude numbers — characterize thermal, buoyancy, surface effects |
| **Unified Description** | The Navier-Stokes equations plus appropriate boundary/initial conditions and constitutive relations describe all fluid phenomena (laminar, turbulent, compressible, incompressible, multiphase) within a single mathematical framework. |
| **Scale and Approximation** | Different approximations (e.g., Euler equations, Stokes flow, boundary layer equations) emerge by simplifying the unified model based on scale and dominant effects. |
| **Numerical Simulation** | Computational Fluid Dynamics (CFD) numerically solves the unified equations to simulate complex real-world flows. |

## Target System and Phenomena

| Aspect | Description |
| --- | --- |
| System Type | Fluids and gases in chemical reactions |
| Phenomena | Flow behavior, turbulence, mixing, reaction dynamics |
| Application Areas | Chemical reactors, combustion, pollutant dispersion |
| Typical Scales | Microscale to industrial scale |
| Objectives | Predict flow patterns, optimize process parameters |

Phenomena

| **Category** | **Subcategory** | **Phenomena** | **Typical Regime** |
| --- | --- | --- | --- |
| **Laminar Flow** | — | Smooth, orderly flow; layers slide past each other | Low Reynolds number (Re < 2000) |
| **Turbulent Flow** | — | Chaotic, irregular fluctuations; eddies and vortices | High Reynolds number (Re > 4000) |
|  | Isotropic Turbulence | Uniform turbulence with no preferred direction | Fully developed turbulence |
|  | Anisotropic Turbulence | Direction-dependent turbulence | Wall-bounded or sheared flows |
| **Boundary Layer Phenomena** | Laminar Boundary Layer | Smooth velocity gradient near solid surfaces | Low Re, smooth surfaces |
|  | Turbulent Boundary Layer | Thickened layer with turbulence near surfaces | High Re, rough or complex surfaces |
|  | Separation | Flow detachment from surface causing wake formation | Adverse pressure gradients |
| **Compressible Flow** | Shock Waves | Sudden changes in pressure, temperature, density | Supersonic/hypersonic flows |
|  | Expansion Fans | Smooth expansion regions with decreasing pressure | Supersonic flow regions |
| **Multiphase Flow** | Bubbly Flow | Gas bubbles dispersed in liquid | Gas-liquid reactors, boiling |
|  | Slug Flow | Alternating regions of gas and liquid | Pipes, oil production |
|  | Droplet and Spray | Liquid dispersed as droplets in gas | Combustion, atomization |
| **Heat and Mass Transfer** | Convection | Transport of heat/mass by fluid movement | Natural and forced convection |
|  | Diffusion | Molecular transport of heat or species | Low flow velocity regimes |
|  | Phase Change | Evaporation, condensation within flow | Boiling, condensation |
| **Flow Instabilities** | Kelvin-Helmholtz Instability | Instability at interface of shear layers | Atmospheric flows, jets |
|  | Rayleigh-Taylor Instability | Instability when heavy fluid rests atop lighter fluid | Gravity-driven flows |
|  | Taylor-Couette Flow | Instabilities between rotating concentric cylinders | Rotating machinery |

## Toolbox

| Tool Category | Tools / Methods | Purpose / Use Case |
| --- | --- | --- |
| Numerical Methods | Finite Volume Method (FVM), Finite Element Method (FEM), Finite Difference Method (FDM) | Discretize governing equations (Navier-Stokes, convection-diffusion) |
| Turbulence Models | k-ε, Large Eddy Simulation (LES), Reynolds-Averaged Navier-Stokes (RANS) | Model turbulent flow effects |
| Meshing Tools | Structured grids, unstructured meshes, adaptive mesh refinement | Spatial discretization of geometry |
| Solver Types | Steady-state, transient solvers | Time-dependent or steady flow simulation |
| Postprocessing | Visualization (streamlines, velocity fields), data extraction | Analyze flow fields and reaction outcomes |

# References

- https://en.wikipedia.org/wiki/Computational_fluid_dynamics
- [**Fluid**](https://app.notion.com/p/Fluid-10cc0f5171ec809b98d9f7a1b292dba4?pvs=21)
