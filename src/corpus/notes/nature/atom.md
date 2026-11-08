---
tags: [note, nature, natural-system, physics, system]
---

# Atom

> A **quantum-mechanical many-body system** composed of a nucleus and a discrete set of bound electrons, described by the solutions to the non-relativistic (or relativistic, in high-precision contexts) Schrödinger (or Dirac) equation, subject to electromagnetic interactions governed by quantum electrodynamics (QED), and characterized by quantized energy levels, angular momentum states, and a probabilistic electron density distribution.
>

QA:

- Why do we mean by the energies?
- **What gives rise to the *stability* of atoms?**
    - Why don’t electrons spiral into the nucleus?
    - What role does quantization play in ensuring stability?
- **What determines the discrete energy levels of atoms?** How do they emerge from boundary conditions, symmetries, and potentials?
- **What is the origin of fine and hyperfine structures?** How does spin, relativistic correction, and nuclear structure affect atomic spectra?
- **How do atoms interact with electromagnetic fields?** What governs emission, absorption, stimulated emission? What is the quantum theory of light–atom interaction?
- **How do atoms couple to each other to form molecules and matter?** What governs bonding, hybridization, Van der Waals interactions?
- ….

## Index

### Structure

### **Nucleus**

- Consists of *Z* protons and *N* neutrons.
- Mass ≈ total baryon mass, charge = +Ze.
- Acts as the central Coulomb potential for electrons.
- Quantum object: exhibits spin, magnetic moment, and sometimes quadrupole moment.
- Subject to strong and weak nuclear forces (internal structure not relevant to electronic structure in most atomic models).

### **Electrons**

- *Z* electrons (for neutral atoms) treated as indistinguishable fermions.
- Obey Pauli exclusion principle and Fermi-Dirac statistics.
- Their spatial and spin distribution described by antisymmetric many-electron wavefunctions.

## Modelling

> Technical models for an atom span several levels of physical abstraction, depending on the precision needed and the physical regime (e.g., low-energy quantum mechanics vs. high-energy relativistic QED). Below is a structured hierarchy of **technical atomic models**, from basic to advanced:
>

### **Rutherford Model (1911)**

- Atom = dense, positively charged nucleus + classical electrons in orbits.
- No energy quantization ⇒ predicts radiation collapse (inconsistent with observations).

### **Bohr Model (1913)**

- Quantized orbits with angular momentum $L = n\hbar$.
- Energies: $E_n = -\frac{13.6\,\text{eV}}{n^2}$.
- Only works well for hydrogen; no electron-electron interaction.

### **Hydrogenic Atom Model**

- Single-electron Schrödinger equation with Coulomb potential:

    $\left[-\frac{\hbar^2}{2m} \nabla^2 - \frac{Ze^2}{4\pi\epsilon_0 r}\right]\psi(\vec{r}) = E\psi(\vec{r})$

- Exact analytic solution for hydrogen (Z=1).

### **Hartree Model**

- **Mean-field** approximation.
- Each electron moves in an average potential created by the nucleus + other electrons.
- Wavefunction: product of one-electron orbitals:  $\Psi(\vec{r}_1, ..., \vec{r}_N) \approx \prod_{i=1}^N \psi_i(\vec{r}_i)$
- Ignores exchange symmetry.

### **Hartree–Fock (HF) Method**

- Introduces **antisymmetry** using Slater determinants:

    $\Psi(\vec{r}_1, ..., \vec{r}_N) = \frac{1}{\sqrt{N!}} \begin{vmatrix}
    \psi_1(\vec{r}_1) & \cdots & \psi_1(\vec{r}_N) \\
    \vdots & \ddots & \vdots \\
    \psi_N(\vec{r}_1) & \cdots & \psi_N(\vec{r}_N)
    \end{vmatrix}$

- Includes exchange interaction (Fock term).
- Neglects dynamic electron correlation.

### **Configuration Interaction (CI)**

- Expand total wavefunction as linear combinations of Slater determinants from excited states.
- Very accurate but scales poorly: $\mathcal{O}(N!)$.

### **Møller–Plesset Perturbation Theory (MPn)**

- Perturbative correction to HF (e.g., MP2 includes 2nd-order corrections).
- Balances accuracy and cost.

### **Coupled-Cluster (CC) Methods**

- Wavefunction: exponential ansatz:  $|\Psi\rangle = e^{\hat{T}}|\Phi_0\rangle$ where  $\hat{T} = \hat{T}_1 + \hat{T}_2 + \cdots$ creates excitations.
- Gold standard in quantum chemistry (e.g., CCSD(T)).

### **Density Functional Theory (DFT)**

- Reformulates the quantum problem in terms of **electron density** $\rho(\vec{r})$, not wavefunction.
- Core principle: *Hohenberg–Kohn theorems*.
- Energy functional: $E[\rho] = T_s[\rho] + E_{\text{ext}}[\rho] + E_H[\rho] + E_{\text{xc}}[\rho]$
- Accuracy depends on choice of exchange-correlation functional $E_{\text{xc}}[\rho]$.
- Efficient for large atoms and molecules.

### **Dirac Equation for the Hydrogen Atom**

- Relativistic wave equation for electrons:

    $\left[ c\boldsymbol{\alpha} \cdot \vec{p} + \beta mc^2 - \frac{Ze^2}{r} \right]\psi = E\psi$

- Predicts fine structure and spin naturally.

### **Relativistic Quantum Chemistry**

- Dirac–Hartree–Fock, Douglas–Kroll–Hess, or ZORA methods.
- Necessary for heavy atoms (Z > 30), where relativistic effects shift core-level energies.

### **Bound-State QED**

- Treats atom as a system of quantized fields: Dirac field (electrons), Maxwell field (photons).
- Corrections include:
    - **Lamb shift**
    - **Anomalous magnetic moments**
    - **Vacuum polarization**
- Required for high-precision atomic spectra (e.g., hydrogen 1s–2s transition).

### **NRQED (Non-Relativistic QED)**

- Effective field theory that expands QED in powers of v/cv/c.
- Used in precision atomic physics.

## Model Limits

> We **do not have a complete atomic model in the absolute sense**, but we do have a **modular, layered, and highly accurate toolkit of atomic models**—each rigorously derived and extremely predictive within its applicable domain.
>

| **Model Type** | **Captures** | **Limits** |
| --- | --- | --- |
| **Non-relativistic QM (Schrödinger)** | Hydrogenic atoms, light atoms, low-Z | Breaks down for heavy atoms or high precision needs |
| **Hartree–Fock + Post-HF** | Electron correlation and exchange | Computationally expensive, limited to small systems |
| **Density Functional Theory (DFT)** | Ground-state properties for large systems | Approximate functionals; lacks precision in some excited-state phenomena |
| **Dirac Equation (Relativistic)** | Fine structure, spin–orbit coupling | No electron correlation, limited to few-electron systems |
| **Quantum Electrodynamics (QED)** | Radiative corrections, Lamb shift, g-2 | Very accurate for few-electron atoms, but not scalable |
| **Effective Field Theories (NRQED)** | High-precision hydrogen-like systems | Not used for complex atoms or dynamics |
| **Lattice QED / QCD** | Simulation of fundamental particle interactions | Too computationally intense for ordinary atomic structure |

Reasons:

- **Many-body problem**
    - Solving the full Schrödinger or Dirac equation for >3 electrons exactly is intractable.
    - Electron correlation scales exponentially with particle number.
- **Relativistic and QED corrections**
    - Necessary for precision spectroscopy and heavy atoms.
    - Require perturbative methods or numerical QED (not full solutions).
- **Nuclear effects**
    - Most atomic models assume a pointlike, static nucleus.
    - Finite size, shape, spin, polarizability, and nuclear excitation states can influence electron behavior.
- **Environmental interactions**
    - External fields (E, B), thermal radiation, pressure, and collisions add complexity not always captured.
- **Computational limits**
    - Even the most advanced methods (e.g., full CI or CCSDTQ) scale poorly and are only feasible for light atoms.

### **Lattice QED/QCD**

- Numerical methods to simulate bound atomic states (e.g., in exotic atoms or heavy nuclei).
- Rarely used for ordinary atoms.

## Atomic Orbital

> An atomic orbital is a mathematical function that describes the region around an atom's nucleus where there is a high probability of finding an electron.
>

## 🧬 **Taxonomy of Atomic Phenomena**

> Processes and Structure.
>

| 🧭 **Category** | 🧩 **Subcategory** | ✨ **Phenomena** | ⚛️ **Typical Regime** |
| --- | --- | --- | --- |
| **Electronic Structure** | — | Energy levels, quantum states, term symbols, orbitals | Quantum mechanics |
|  | Fine structure | Spin–orbit coupling, relativistic corrections | Atomic spectroscopy (fine splitting) |
|  | Hyperfine structure | Nuclear spin–electron interaction, magnetic dipole/quadrupole splitting | Atomic clocks, NMR |
|  | Electron correlation | Collective effects beyond independent-particle models | Many-body quantum systems |
| **Electromagnetic Interactions** | Light–atom interaction | Absorption, stimulated emission, spontaneous emission, Rabi oscillations | Quantum optics |
|  | Spectroscopic shifts | Stark effect, Zeeman effect, Lamb shift | Field-dependent atomic behavior |
|  | Optical phenomena | Electromagnetically induced transparency (EIT), optical pumping, laser cooling | Laser–atom systems |
|  | Coherence phenomena | Coherent population trapping, quantum beats | Precision metrology |
| **Ionization & Recombination** | — | Photoionization, collisional ionization, autoionization | Plasma physics, astrophysics |
|  | Recombination processes | Radiative, three-body, and dielectronic recombination | Low-temperature plasmas |
| **Collision & Scattering** | Elastic scattering | No energy exchange (momentum only) | Electron/atom collisions |
|  | Inelastic scattering | Excitation, ionization | EELS, atomic/molecular beams |
|  | Resonant scattering | Fano resonances, Breit–Wigner profiles | Atomic and nuclear scattering |
| **Radiation Emission** | Bound–bound transitions | Discrete line spectra | Optical, UV, and X-ray spectroscopy |
|  | Bound–free & free–free | Bremsstrahlung, continuum radiation, X-ray emission | Astrophysics, fusion plasmas |
|  | Auger processes | Non-radiative decay via electron ejection | Surface science, core-hole dynamics |
| **Exotic Atomic Systems** | Muonic atoms | Atoms with muons replacing electrons | High-Z precision QED |
|  | Antimatter atoms | Positronium, antihydrogen | Fundamental CPT/QED tests |
|  | Rydberg atoms | Highly excited states with large radius and high sensitivity | Quantum info, precision spectroscopy |
| **Quantum Measurement Effects** | — | Decoherence, entanglement, measurement backaction | Quantum foundations, quantum control |
|  | Quantum Zeno effect | Inhibited evolution via frequent measurement | Quantum computing, control theory |
| **Thermal & Statistical Effects** | Thermodynamic properties | Polarizability, heat capacity, partition functions | Statistical mechanics |
|  | Doppler broadening | Spectral line broadening due to thermal motion | High-resolution spectroscopy |
|  | Pressure broadening | Collisional broadening in dense environments | Spectroscopy in gases and plasmas |
| **Nuclear Coupling Effects** | Isotope shift | Spectral shifts due to nuclear mass and volume | Precision atomic spectroscopy |
|  | Electron-induced nuclear excitation | Coupling to nuclear states via electronic transitions | Hyperfine studies, Mössbauer effect |

## References

- https://en.wikipedia.org/wiki/Atom
- https://en.wikipedia.org/wiki/Atomic_orbital
- https://en.wikipedia.org/wiki/Orbital_hybridisation

## Related

- [Molecule](/view.html?p=notes/nature/molecule.md)
- [Protonuclide](/view.html?p=notes/nature/matter/protonuclide.md)
- [Interaction](/view.html?p=notes/nature/theory/interaction.md)
- [Fundamental Interaction](/view.html?p=notes/nature/fundamental-interaction.md)
- [Spin](/view.html?p=notes/nature/spin.md)

## Provenance

- Notion export: `Modelo/Nature/Conceptual Model Natural System/Atom 10cc0f5171ec8083b1baf8f9d2d99620.md`
