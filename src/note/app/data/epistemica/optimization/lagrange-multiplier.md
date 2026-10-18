# Lagrange Multiplier

 : Hamiltonian Optimization (Hamiltonian%20Optimization%201d8c0f5171ec80a591dec4e7f774099a.md)

> The **Lagrange multiplier** is a scalar parameter introduced in the method of **constrained optimization** to transform a constrained extremization problem into an unconstrained one by augmenting the objective function with a linear combination of the constraints.
> 

## Formal Definition

Let $f : \mathbb{R}^n \to \mathbb{R}$ be a differentiable **objective function**, and let  $g : \mathbb{R}^n \to \mathbb{R}^m$ be a differentiable **constraint function**, where the constraint is given by g(x)=0g(x) = 0. The Lagrangian  $\mathcal{L} : \mathbb{R}^n \times \mathbb{R}^m \to \mathbb{R}$ is defined as: $\mathcal{L}(x, \lambda) = f(x) - \lambda^\top g(x)$

Here, $\lambda \in \mathbb{R}^m$ is the vector of **Lagrange multipliers**.

The **first-order necessary conditions** (KKT conditions for equality constraints) for a local extremum under constraint are given by:

$\nabla_x \mathcal{L}(x, \lambda) = \nabla f(x) - J_g(x)^\top \lambda = 0 \\
g(x) = 0$

where  $g(x) \in \mathbb{R}^{m \times n}$ is the **Jacobian matrix** of the constraint function $g$.

## Interpretation

- The Lagrange multipliers $\lambda_i$ represent the **rate of change of the objective function’s optimal value with respect to a marginal relaxation of the corresponding constraint**.
- Geometrically, at a local extremum under constraints, the gradient of the objective function lies in the **span of the gradients of the constraints**, i.e., the constraint surface is tangent to a level set of the objective function.

## References

- https://en.wikipedia.org/wiki/Lagrange_multiplier
- https://tutorial.math.lamar.edu/classes/calciii/lagrangemultipliers.aspx
- https://en.wikipedia.org/wiki/Hamiltonian_(control_theory)
