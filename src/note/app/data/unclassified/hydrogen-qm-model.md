---
tags: [miscellanea, model]
---

# Hydrogen QM Model

> Modeling the **Hydrogen atom** using quantum mechanics is a classic and fundamental problem.
>

> The hydrogen atom model **captures the quantum behavior of the electron bound to a proton**, explaining the discrete energy levels and spatial probability patterns that define atomic structure.
>

## Modelling Goal

| Aspect | What is Modeled |
| --- | --- |
| **Electron’s quantum state** | The probability distribution of where the electron can be found around the nucleus (wavefunction) |
| **Energy levels** | The discrete allowed energy values the electron can have (quantization of energy) |
| **Angular momentum** | The quantized orbital angular momentum of the electron and its orientation in space |
| **Spatial distribution** | The shapes and sizes of atomic orbitals (regions where the electron is likely to be found) |
| **Spectral lines** | The emitted or absorbed photon energies when the electron transitions between energy levels |
| **Fundamental interactions** | The electromagnetic Coulomb attraction between electron and proton modeled via potential energy |

## Data

> The quantum state of the hydrogen atom was modeled **purely from physical laws and constants**, not by fitting data. The resulting predictions (energy levels, orbitals, angular momentum) were then **confirmed by spectroscopic experiments**.
>

## Electron’s Quantum State in Hydrogen Model

> A **quantum state** that describes the **probability amplitude** of finding the electron at different points in space, influenced by the proton’s Coulomb potential.
>

> To **model only the electron’s quantum state** in the hydrogen atom using quantum mechanics, we focus on the **wavefunction** $\psi(\vec{r})$, which contains **all information** about the **electron’s behavior**.
>

### **Physical Setup**

- **System**: Electron of mass mm attracted by a fixed proton at the origin
- **Potential**: $V(r) = -\dfrac{e^2}{4\pi\epsilon_0 r}$
- **Objective**: Solve for $\psi(\vec{r})$ in 3D space

### **Mathematical Formulation**

Use the **time-independent Schrödinger equation**:  $\hat{H} \psi(\vec{r}) = E \psi(\vec{r})$

with:  $\hat{H} = -\dfrac{\hbar^2}{2m} \nabla^2 - \dfrac{e^2}{4\pi\epsilon_0 r}$

### **Solution Strategy**

Due to spherical symmetry, switch to **spherical coordinates** and separate variables: $\psi(\vec{r}) = R_{n\ell}(r) \cdot Y_\ell^m(\theta, \phi)$

- $R_{n\ell}(r)$: Radial part
- $Y_\ell^m(\theta, \phi)$: Spherical harmonics (angular part)

## Experimental Validation

> …
>

## References

- [Hydrogen](note.html?n=nature/chemical-element/chemical-element-database/hydrogen.md)
- [Quantum Framework](https://app.notion.com/p/Quantum-Framework-1e6c0f5171ec80bfb5b7cb858905c0e9?pvs=21)

## Provenance

- Notion export: `Modelo/Miscellanea/Miscellanea/Hydrogen QM Model 22dc0f5171ec8008bd10e4330baa8f47.md`
