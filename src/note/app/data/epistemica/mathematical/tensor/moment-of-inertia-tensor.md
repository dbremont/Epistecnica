---
tags: [analytical, type, physical, mathematics]
---

# Moment of Inertia Tensor

> The **moment of inertia tensor** $I_{ij}$ relates a rigid body's angular velocity to its angular momentum: $L_i = I_{ij}\omega_j$. It is the rotational analogue of mass, and the clearest example of a tensor that is not a matrix of coordinates.

## Formulation

> **What it is.** For a body with mass density $\rho$, $I_{ij} = \int \rho\,(r^2\delta_{ij} - r_i r_j)\,dV$. The subtraction is what makes it a tensor rather than a scalar: rotation about different axes meets different resistance, and the off-diagonal terms couple the axes.
>
> **Type.** A `Concept` — a symmetric positive-definite second-rank tensor attached to a rigid body.
>
> **Boundary.** It depends on the point about which moments are taken; the parallel-axis theorem transports it. It is constant in the body frame and time-dependent in the space frame — the source of the gyroscopic terms in Euler's equations.

## Key results

- **Principal axes.** Diagonalizing $I$ gives the axes about which rotation is torque-free; the three eigenvalues are the principal moments.
- **Diagonal dominance.** For any body, $I_{ii} \le I_{jj} + I_{kk}$ for distinct axes — a triangle inequality on the principal moments.
- **Kinetic energy.** $T = \tfrac12 \omega_i I_{ij}\omega_j$; angular momentum is $L = I\omega$, not parallel to $\omega$ in general.
- **Euler's equations.** $I\dot\omega + \omega\times(I\omega) = \tau$ — the rigid-body dynamics, and the reason a free body can tumble.
- **Tensor, not matrix.** The components change under rotation as a tensor should; the object is the linear map from angular velocity to angular momentum, and that map is what the tensor is.

## References

- https://en.wikipedia.org/wiki/Moment_of_inertia
- [Tensor](tensor.md) · [Eigenvalue](../structure/linear/eigenvalue.md) · [Rigid Body Mechanics](note.html?n=epistemica/singular/rigid-body-mechanics.md) · [Stress Tensor](stress-tensor.md)
