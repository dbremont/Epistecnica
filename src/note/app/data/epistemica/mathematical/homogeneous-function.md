---
tags: [function]
---

# Homogeneous Function

 : Projective Geometry (Projective%20Geometry%20206c0f5171ec8016b1e0d9772b9e9a07.md)

> A **homogeneous function** is a function that scales predictably when all of its arguments are scaled by a common factor.
> 

> **Note**:  The concept of **homogeneity** appears across **many branches of mathematics**, each time capturing the idea of **scale-invariance** or **uniform structure**.
> 

## Formulation

> A function $f(x_1, x_2, \dots, x_n)$ is said to be **homogeneous of degree $k$** if, for all $\lambda \in \mathbb{R} \setminus \{0\}$: $f(\lambda x_1, \lambda x_2, \dots, \lambda x_n) = \lambda^k f(x_1, x_2, \dots, x_n)$;  Here, $k \in \mathbb{R}$ is called the **degree of homogeneity**.
> 

## 🔷  Case Study

### ✅ Homogeneous of Degree 1:

- $f(x, y) = 3x + 2y$
- $f(\lambda x, \lambda y) = 3\lambda x + 2\lambda y = \lambda(3x + 2y) = \lambda f(x, y)$

### ✅ Homogeneous of Degree 2:

- $f(x, y) = x^2 + xy + y^2$
- $f(\lambda x, \lambda y) = \lambda^2 (x^2 + xy + y^2) = \lambda^2 f(x, y)$

### ❌ Not homogeneous:

- $f(x, y) = x^2 + y + 1$
- $f(\lambda x, \lambda y) \ne \lambda^k f(x, y) \text{ for any } k$

## 🔹 Uses of Homogeneous Functions

- **Economics**: Describing production functions (e.g., constant returns to scale)
- **Thermodynamics**: Euler’s theorem on homogeneous functions
- **Algebraic geometry**: Defining projective varieties
- **Homogeneous polynomials**: Polynomials where all terms have the same total degree (e.g., $x^2 + xy + y^2$)

## 🔸Euler’s Theorem (for differentiable homogeneous functions)

> If ff is differentiable and homogeneous in degree $k$, then:  $\frac{\partial f}{\partial x_1} + x_2 \frac{\partial f}{\partial x_2} + \cdots + x_n \frac{\partial f}{\partial x_n} = k f(x_1, \dots, x_n)$.
> 

## References

- https://en.wikipedia.org/wiki/Homogeneous_function
