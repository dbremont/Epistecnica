---
tags: [analytical]
---

# Differential Equation


> A **differential equation** is a mathematical relation that specifies how a function y:   $D \subseteq \mathbb{R}^n \to \mathbb{R}^m$  and its derivatives (of various orders) relate to each other, typically encoding constraints on the local behavior of the function through the action of differential operators.
> 

## Formulation

### Standard

A **differential equation** is an equation of the form:

$F\left(x, y(x), \frac{dy}{dx}, \frac{d^2y}{dx^2}, \dots, \frac{d^n y}{dx^n} \right) = 0$

where:

- $F$ is a given (often smooth or analytic) function,
- $y(x)$ is the unknown function (scalar or vector-valued),
- $x \in D \subseteq \mathbb{R}^n$,
- and the derivatives may be ordinary (ODEs) or partial (PDEs), depending on whether $y$  depends on one or multiple independent variables.

### Operator-Theoretic View

> This perspective is critical in defining generalized solutions in weak or distributional senses, particularly in infinite-dimensional function spaces (e.g., Sobolev spaces).
> 

In functional analysis, a differential equation can be represented abstractly as:

$\mathcal{D}(y) = f$

where:

- $\mathcal{D}$ is a differential operator (e.g., linear like the Laplacian $\Delta$, or nonlinear),
- $y$ is the unknown function,
- and $f$ is a known function or distribution.

## Branch

> Study Branches of DE.
> 

| **Branch** | **Description** |
| --- | --- |
| **Ordinary Differential Equations (ODEs)** | Equations involving functions of a **single independent variable** and their derivatives. Example: $\frac{dy}{dx} = x^2 + y$. |
| **Partial Differential Equations (PDEs)** | Equations involving functions of **multiple independent variables** and their partial derivatives. Example: $u_t = u_{xx}$. |
| **Linear Differential Equations** | DEs in which the unknown function and its derivatives appear **linearly** (no powers or products of the function). Example: $y'' + 3y' + 2y = 0$. |
| **Nonlinear Differential Equations** | DEs where the unknown function or its derivatives appear **nonlinearly** (powers, products, or nonlinear functions). Example: $y'' + y^2 = 0$. |
| **Homogeneous Differential Equations** | DEs where all terms involve the unknown function or its derivatives; no independent term appears. Example: $y'' - 3y' + 2y = 0$. |
| **Nonhomogeneous Differential Equations** | DEs containing a **nonzero term independent** of the unknown function. Example: y′′−3y′+2y=exy'' - 3y' + 2y = e^x. |
| **Exact Differential Equations** | Equations that can be expressed as the **total differential** of a function: $M(x,y)dx + N(x,y)dy = 0$ is exact if $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$. |
| **Non-exact Differential Equations** | Equations that **cannot initially** be expressed as a total differential; may require an integrating factor. |
| **Autonomous Differential Equations** | DEs where the independent variable **does not appear explicitly**. Example: $\frac{dy}{dx} = y^2 - 1$. |
| **Non-autonomous Differential Equations** | DEs where the independent variable **appears explicitly**. Example: $\frac{dy}{dx} = xy + 1$. |
| **Stochastic Differential Equations (SDEs)** | DEs that include **random processes** or noise terms, often used in modeling uncertainty or randomness. Example: $dX_t = \mu X_t dt + \sigma X_t dW_t$. |
| **Delay Differential Equations (DDEs)** | DEs in which the derivative at a certain time depends on **past values** of the function. Example: $y'(t) = y(t-1)$. |

## **Taxonomy**

> Note (🚨): The column 'Canonical Form' is used more as a convenient label; the term 'canonical' may not perfectly align with its typical semantic meaning in this context.
> 

> The **tractability** of a **`differential equation`** refers to the ease with which it can be solved or analyzed, often depending on the existence of closed-form solutions, numerical methods, or the simplicity of its structure and boundary conditions.
> 

| **Category** | **Name** | **Canonical Form** | **Description** |
| --- | --- | --- | --- |
| **Ordinary Differential Equations (ODEs)** | **First-Order ODEs** | $\frac{dy}{dx} = f(x, y)$ | Equations involving only the first derivative of the unknown function. |
|  | **Second-Order ODEs** | $\frac{d^2y}{dx^2} + p(x)\frac{dy}{dx} + q(x)y = g(x)$ | Equations involving the second derivative of the unknown function. |
|  | **Higher-Order ODEs** | $\frac{d^ny}{dx^n} + a_{n-1}\frac{d^{n-1}y}{dx^{n-1}} + \dots + a_0 y = 0$ | Equations involving derivatives of order $n \geq 3$. |
|  | **Linear ODEs** | $\frac{dy}{dx} + p(x)y = q(x)$ | Equations where the unknown function and its derivatives appear linearly. |
|  | **Nonlinear ODEs** | $\frac{dy}{dx} = y^2 + x$ | Equations where the unknown function or its derivatives appear nonlinearly. |
|  | **Autonomous ODEs** | $\frac{dy}{dx} = f(y)$ | Equations where the independent variable does not explicitly appear. |
|  | **Non-Autonomous ODEs** | $\frac{dy}{dx} = f(x, y)$ | Equations where the independent variable explicitly appears. |
|  | **Exact ODEs** | $M(x, y)dx + N(x, y)dy = 0$ | Equations that can be expressed as the total differential of a function. |
|  | **Separable ODEs** | $\frac{dy}{dx} = g(x)h(y)$ | Equations where the variables can be separated on either side of the equation. |
|  | **Homogeneous ODEs** | $\frac{dy}{dx} = f\left(\frac{y}{x}\right)$ | Equations where the function $f$ depends only on the ratio $\frac{y}{x}$. |
|  | **Systems of ODEs** | $\frac{dx}{dt} = f(x, y), \frac{dy}{dt} = g(x, y)$ | Multiple ODEs coupled together. |
| **Partial Differential Equations (PDEs)** | **First-Order PDEs** | $a(x, y)\frac{\partial u}{\partial x} + b(x, y)\frac{\partial u}{\partial y} = c(x, y)$ | Equations involving only the first partial derivatives of the unknown function. |
|  | **Second-Order PDEs** | Heat equation, wave equation, Laplace equation | Equations involving second partial derivatives of the unknown function. |
|  | **Higher-Order PDEs** | Biharmonic equation | Equations involving partial derivatives of order $n \geq 3$. |
|  | **Linear PDEs** | $a(x, y)\frac{\partial^2 u}{\partial x^2} + b(x, y)\frac{\partial^2 u}{\partial x \partial y} + c(x, y)\frac{\partial^2 u}{\partial y^2} = 0$ | Equations where the unknown function and its derivatives appear linearly. |
|  | **Nonlinear PDEs** | Burgers' equation, Navier-Stokes equations | Equations where the unknown function or its derivatives appear nonlinearly. |
|  | **Elliptic PDEs** | Laplace equation, Poisson equation | Equations describing steady-state phenomena (e.g., potential fields). |
|  | **Parabolic PDEs** | Heat equation, diffusion equation | Equations describing diffusion or heat flow. |
|  | **Hyperbolic PDEs** | Wave equation, transport equation | Equations describing wave propagation or transport phenomena. |
|  | **Mixed-Type PDEs** | Tricomi equation | Equations that change type depending on the domain. |
| Stochastic Differential Equations (SDEs) |  | $dx = f(x)dt + g(x)dW_t$ | Equations involving random processes, typically in finance or physics. |
| Partial Stochastic Differential Equations (SDEs) |  |  |  |
| Delay Differential Equations (DDEs) |  | $\frac{dy(t)}{dt} = f(y(t), y(t-\tau))$ | Equations where the rate of change of the function depends on past values. |
| Integro-Differential Equations |  | $\frac{dy(t)}{dt} = \int_0^t K(t, s)y(s)ds$ | Equations that involve both integration and differentiation. |
| Fractional Differential Equations |  | Equations involving derivatives of non-integer order.	$D^\alpha y(t) = f(t)$, where $\alpha$ is a fractional derivative. | Differential Equations involving derivatives of noninteger order. |

## Technique Space

> Which techniques do we used to solved **Differential Equations**?
> 

| **Category** | **Method** | **Description** |
| --- | --- | --- |
| **Analytical** | **Separation of Variables** | Solving equations by separating variables on opposite sides, typically used for PDEs and some ODEs. |
|  | **Integrating Factors** | Used for solving first-order linear ODEs by multiplying both sides by an integrating factor to make the equation exact. |
|  | **Exact Equations** | Solving differential equations that are exact or can be made exact by finding an integrating factor. |
|  | **Method of Characteristics** | Applied to first-order PDEs by converting them into a system of ODEs along characteristic curves. |
|  | **Method of Integrating Factors** | Used for non-exact ODEs, turning them into exact ones to solve the differential equation. |
|  | **Variation of Parameters** | A technique for solving non-homogeneous linear ODEs by finding a particular solution that is added to the homogeneous solution. |
|  | **Homogeneous Solutions** | Solutions to the equation where the right-hand side is zero. |
|  | **Particular Solutions** | Specific solutions derived from initial or boundary conditions for linear and non-linear systems. |
| **Numerical** | **Euler’s Method** | A simple method for solving ODEs by approximating the solution at discrete steps using a linear approximation. |
|  | **Runge-Kutta Methods** | Higher-order methods that provide a more accurate approximation of ODE solutions compared to Euler’s method. |
|  | **Finite Difference Method** | Approximates PDE solutions by discretizing time and space and solving at grid points. |
|  | **Finite Element Method (FEM)** | A numerical method that divides a large system into smaller parts (elements) to approximate solutions to PDEs, often used in engineering. |
|  | **Boundary Element Method (BEM)** | Used to solve PDEs by reducing the problem to a boundary integral equation, typically for problems with boundary conditions. |
|  | **Spectral Methods** | Uses global polynomials to approximate the solution, useful for problems with smooth solutions. |
|  | **Multigrid Methods** | Solving PDEs on multiple grids to improve the efficiency of numerical solutions, often used in simulations of fluid dynamics. |
| **Perturbation** | **Regular Perturbation** | Applied when a small parameter is involved; the solution is expressed as an asymptotic series in terms of that parameter. |
|  | **Singular Perturbation** | Perturbation method used when solutions exhibit boundary layers or rapid changes in behavior due to small parameters. |
|  | **Matched Asymptotic Expansions** | A technique for dealing with boundary layers in singular perturbation problems, matching solutions in different regions. |
|  | **WKB Approximation** | A semiclassical method for solving linear differential equations in quantum mechanics and other physical problems, using an asymptotic expansion. |
| **Transform** | **Laplace Transform** | Converts ODEs/PDEs into algebraic equations by transforming them from the time domain to the complex frequency domain. |
|  | **Fourier Transform** | Converts time-domain functions into frequency-domain representations, used extensively for periodic or wave-related problems. |
|  | **Z-Transform** | Used for discrete-time systems to convert difference equations into algebraic equations. |
|  | **Mellin Transform** | Converts a function into a form amenable to asymptotic analysis and solution of problems in integral equations and PDEs. |
| **Series** | **Power Series** | Expresses solutions to ODEs as an infinite sum of powers of the independent variable, useful for variable coefficient equations. |
|  | **Frobenius Method** | A generalization of the power series method for solving second-order linear ODEs near singular points. |
|  | **Pade Approximation** | A method for approximating functions as rational functions (ratios of polynomials), improving convergence over truncated series. |
|  | **Asymptotic Expansions** | A method for approximating the behavior of solutions in the limit of large or small parameters. |
| **Green's Function** | **Green’s Function for Laplace Equation** | Used to solve boundary value problems, especially for the Laplace or Poisson equation, by representing the solution as an integral over the domain. |
|  | **Green’s Function for Heat Equation** | Represents the solution to the heat equation as an integral involving the Green’s function, often used in diffusion problems. |
|  | **Green’s Function for Wave Equation** | Used in wave propagation problems to express the solution as an integral involving the Green’s function. |
| **Boundary and Initial Value Problems** | **Separation of Variables** | Solving boundary value problems by separating spatial and temporal variables in PDEs. |
|  | **Dirichlet Conditions** | Boundary conditions specifying the value of the solution on the boundary of the domain. |
|  | **Neumann Conditions** | Boundary conditions specifying the derivative (slope) of the solution on the boundary. |
|  | **Cauchy Conditions** | Initial conditions for solving initial value problems, typically providing values of the solution and its derivative at t=0t = 0. |
| **Nonlinear Method** | **Newton's Method** | Used for solving nonlinear algebraic equations, often applied in solving nonlinear differential equations through iterative solutions. |
|  | **Bifurcation Theory** | Studies changes in the qualitative behavior of solutions as parameters in nonlinear differential equations are varied. |
|  | **Perturbation Expansion** | Expanding solutions to nonlinear problems in terms of small perturbations to an easily solvable problem. |
| **Algebraic** | **Lie Group Analysis** | Uses symmetries of the differential equation to reduce its order or transform it into a simpler equation. |
|  | **Noether’s Theorem** | Applied in physics to find conserved quantities in differential equations, often in the context of field theories. |
| **Stochastic Methods** | **Fokker-Planck Equation** | Describes the evolution of probability distributions of a system’s state, commonly used in statistical mechanics and diffusion problems. |
|  | **Ito Calculus** | A method used in stochastic differential equations (SDEs), especially in finance and physics, to model random processes. |
|  | **Stochastic Differential Equations (SDEs)** | Describes systems influenced by random noise, solved using numerical methods such as Monte Carlo simulations. |
| **Functional Methods** | **Variational Methods** | Methods for finding approximate solutions by minimizing or maximizing a functional, often used in physical systems modeled by PDEs. |
|  | **Euler-Lagrange Equation** | Derives the equations of motion for a system in physics, often resulting in second-order differential equations. |
|  | **Action Principle** | Used to derive equations of motion by requiring that the action is stationary, typically resulting in ODEs or PDEs. |
| **Linear vs. Nonlinear Solutions** | **Linear Superposition** | Applied to linear ODEs and PDEs where solutions can be superimposed to form the general solution. |
|  | **Nonlinear Superposition** | In nonlinear systems, superposition is generally not valid; however, methods like the method of characteristics or perturbation theory may be used. |
| **Homogeneous vs. Inhomogeneous** | **Homogeneous Solutions** | Solutions to differential equations where the right-hand side (source term) is zero. |
|  | **Inhomogeneous Solutions** | Solutions to equations with non-zero source terms, often requiring methods like Green's functions or particular solution techniques. |
| **Approximation Methods** | **Finite Difference Method** | A numerical technique to approximate derivatives by discretizing the independent variable, used for solving ODEs and PDEs. |
|  | **Finite Volume Method** | A numerical technique for solving PDEs, focusing on the conservation of fluxes across small control volumes within the domain. |
|  | … |  |
|  |  |  |

### Computational Method

- [ ]  [Euler Method](../computational-science/euler-method.md)

## **Boundary Value Problems (BVPs)**

> **Boundary Value Problems (BVPs)** are differential equations where the solution is determined by specifying values of the unknown function at two or more distinct points, typically at the boundaries of the domain.
> 

## **Initial Value Problems (IVPs)**

> **Initial Value Problems (IVPs)** are differential equations where the solution is determined by specifying the value of the unknown function at a single point, typically at the initial condition of the domain.
> 

## References

- https://en.wikipedia.org/wiki/Differential_equation
- [ ]  [A Case Study of a Dissipative System: **Damped Pendulum**](https://app.notion.com/p/A-Case-Study-of-a-Dissipative-System-Damped-Pendulum-1ebc0f5171ec80c09a6af45b6f968c2b?pvs=21)
- [ ]  https://github.com/dbremont/algorithms/blob/main/cm/ode.ipynb
- [ ]  https://github.com/dbremont/algorithms/blob/main/cm/integral.ipynb
- [ ]  https://github.com/dbremont/algorithms/blob/main/cm/differential.ipynb
