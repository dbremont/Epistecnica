---
tags: [note, mathematics, equation, dynamical-system]
---

# Differential Equation

> A **differential equation** is a mathematical relation that specifies how a function $y: D \subseteq \mathbb{R}^n \to \mathbb{R}^m$ and its derivatives (of various orders) relate to each other, typically encoding constraints on the local behavior of the function through the action of differential operators.

## Formulation

### What is this epistemic instance?

> The **differential-equation instance** is the written relation that binds an unknown function and its derivatives on a declared domain. It is not the solution, not the problem that adds boundary or initial conditions, and not the method that produces a solution.

#### Standard Form

A **differential equation** is an equation of the form:

$$F\left(x, y(x), \frac{dy}{dx}, \frac{d^2y}{dx^2}, \dots, \frac{d^n y}{dx^n} \right) = 0$$

where:

- $F$ is a given (often smooth or analytic) function,
- $y(x)$ is the unknown function (scalar or vector-valued),
- $x \in D \subseteq \mathbb{R}^n$,
- and the derivatives may be ordinary (ODEs) or partial (PDEs), depending on whether $y$ depends on one or multiple independent variables.

#### Operator Reading

> This perspective is critical in defining generalized solutions in weak or distributional senses, particularly in infinite-dimensional function spaces (e.g., Sobolev spaces).

In functional analysis, a differential equation can be represented abstractly as:

$$\mathcal{D}(y) = f$$

where:

- $\mathcal{D}$ is a differential operator (e.g., linear like the Laplacian $\Delta$, or nonlinear),
- $y$ is the unknown function,
- and $f$ is a known function or distribution.

### What epistemic element type does this epistemic instance belong to?

> Primary type: **`Epistemic Representation`** — the **differential-equation scheme**: the notational construct through which a relation among a function and its derivatives is written, transformed, and interpreted.

> `readable as` an **`Epistemic Construction`** (→ Kind `Model`) when the equation models a target system, and as a **`Description`** when it states a relation about that system. `readable as` an **`Epistemic Act`** is refused: the act is the `Computation` that solves or evaluates the equation. `readable as` an **`Epistemic Method`** is refused: the solution techniques are methods, not the equation. `readable as` a **`Transformation Rule`** is refused: the derivative and integral operators are the rules; the equation is the constraint they help state.

> The change the equation describes is read in the **Ontic Order** when it is applied to a segment of reality; the relation that states it is epistemic.

### Is the type of this `epistemic element instance` unambiguous?

> Yes, in three directions the decomposition keeps apart.

> **Aspect.** “Differential equation” names the written relation, the solution set, and the problem (equation plus conditions). This note types the written relation; the solution is a function (or a `Trajectory`), and a BVP or IVP is a problem specification, not a second equation.

> **Kind.** Ordinary, partial, stochastic, delay, integro-differential, fractional, and differential-algebraic equations are instances of the one construct, not separate constructs. Order, linearity, homogeneity, autonomy, and exactness are classification axes over those instances; they are not further kinds.

> **Reading.** The same equation can be read as a `Model` of a target system or as a `Description` of a relation. Representation is primary because the note is about the formal relation, not about any one target that realizes it.

> The ambiguity is resolved by declaring `Epistemic Representation` primary, typing the notation and its substrate, and growing the families as `Instance`s. Filing the solution as the equation would erase the difference between the relation and what satisfies it; filing the solution method as the equation would erase the difference between the constraint and the routine that discharges it.

### What is the recursive instance decomposition of this epistemic instance?

> **Boundary.** This table decomposes one epistemic instance — the differential-equation scheme as a representational construct — into the notation that carries it, the rules and readings constituting that notation, and the main equation families. Solution methods, boundary and initial conditions, and the dynamical systems an equation models are named and linked, never grown here: they are `Epistemic Method`s, problem specifications, and ontic targets respectively.

> **Stopping rule.** A row is terminal when it names a concrete notation element, axiom, formation rule, transformation rule, convention, interpretation, or equation family. No family is decomposed into its solution theory; the methods are catalogued in `## Technique Space`.

> **Identity.** Instance Tree Path holds instances only — never epistemic element types; every path in this table is unique, and no type segment terminates a branch. Order, linearity, homogeneity, autonomy, and exactness are classification axes over the families, not further families, so they remain in `## Branch` and `## Taxonomy` rather than becoming sibling paths.

> **Typing.** The root type is `Epistemic Representation`, declared once: the equation is a representational construct, not the act of solving it, not the method that orders the solving, and not the derivative rule that rewrites expressions. The operator form $\mathcal{D}(y)=f$ is an `Interpretation` of the same notation, not a second root.

> **Reading.** The tree is read as **representation**: it records how a differential equation is written, constituted, and interpreted, not how a segment of reality is parsed. The families are instances of one construct; the cross-cutting properties are axes, not kinds.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation | The written relation binding an unknown function and its derivatives on a domain — the representational construct this note decomposes. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` | Grouping: the sign system in which the relation is written. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Instance) Differential Equation Notation | The differential-equation notation: functions, derivative terms, independent variables, the equality sign, and the domain. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Representation Element` | Grouping: combinable constituents of the notation. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Unknown Function | The function $y$ whose derivatives appear and whose values the relation constrains. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Independent Variable | The variable or variables $x$ on which $y$ depends; one variable for an ODE, several for a PDE. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Derivative Term | A derivative $y', y'', \ldots, \partial u/\partial x, \ldots$ — the term that makes the relation differential rather than algebraic. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Equality Sign | The sign `=` asserting that the two sides name the same function relation. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Domain | The set $D$ on which $y$ is defined and on which the relation is asserted. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Coefficient | A term multiplying the function or a derivative, possibly depending on the independent variables. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Source Term | The term independent of the unknown function; zero for a homogeneous equation. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Order | The highest derivative order $n$ appearing in the relation. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` | Grouping: the rules, structures, and readings constituting the notation. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: the relations and assumptions the notation is founded on. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Equality Relation | The equality that binds the two sides; not identity of symbols, but equality of the function relation on the domain. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Differentiability Assumption | The class of differentiability assumed for $y$ — classical, weak, or distributional — which fixes what counts as a solution. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Existence and Uniqueness Condition | The conditions under which a solution exists and is unique: Picard–Lindelöf for ODEs, Cauchy–Kovalevskaya for analytic PDEs, and their weak counterparts. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Formation` | Grouping: rules of well-formed differential equations. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Well-Formed Differential Equation Rule | The function, its derivatives, and the independent variables must be defined on a common domain, with derivative orders matching the differentiability assumed. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Standard Form Rule | The rewrite of the relation into a standard form — isolating the highest derivative or writing $F=0$ — without changing its solution set. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` | Grouping: rewrite licences that preserve or transform the relation. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Differentiation Rule | The rule that replaces a function by its derivative; the operator that makes the equation differential. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Integration Rule | The inverse-side rule that recovers a function from its derivative, used in solving and in integral formulations. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Equivalence Transformation Rule | A rule that rewrites the equation into an equivalent one — algebraic rearrangement, change of variables, or normalization — preserving the solution set. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` | Grouping: stabilized notational choices. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Derivative Notation Convention | The choice among Leibniz, prime, dot, and subscript notation for derivatives. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Equality Orientation Convention | The choice of which side carries the unknown function and which carries the source term. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Order Convention | The convention fixing the order counted and the standard form used for a family. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` | Grouping: meaning assignments carried by the notation. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Solution Reading | Reading a solution as a function that satisfies the relation on the domain. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Operator Reading | Reading the relation as $\mathcal{D}(y)=f$: a differential operator applied to the unknown function equals a source. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Weak Solution Reading | Reading a solution in a weak or distributional sense, where derivatives are taken against test functions. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Ordinary Differential Equation | Equations in one independent variable; the derivative terms are ordinary. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Ordinary Differential Equation (→ Instance) First-Order ODE | An ODE whose highest derivative is first order. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Ordinary Differential Equation (→ Instance) Second-Order ODE | An ODE whose highest derivative is second order. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Ordinary Differential Equation (→ Instance) Higher-Order ODE | An ODE whose highest derivative is of order three or more. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Ordinary Differential Equation (→ Instance) System of ODEs | Several ODEs coupled through their unknown functions. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Partial Differential Equation | Equations in two or more independent variables; the derivative terms are partial. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Partial Differential Equation (→ Instance) First-Order PDE | A PDE whose highest partial derivatives are first order. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Partial Differential Equation (→ Instance) Second-Order PDE | A PDE whose highest partial derivatives are second order. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Partial Differential Equation (→ Instance) Elliptic PDE | A second-order PDE of elliptic type: steady-state or equilibrium problems, e.g. Laplace and Poisson. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Partial Differential Equation (→ Instance) Parabolic PDE | A second-order PDE of parabolic type: diffusion and heat flow. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Partial Differential Equation (→ Instance) Hyperbolic PDE | A second-order PDE of hyperbolic type: wave propagation and transport. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Partial Differential Equation (→ Instance) Mixed-Type PDE | A PDE whose type changes with the domain or the solution, e.g. the Tricomi equation. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Stochastic Differential Equation | An equation whose differential term is driven by a stochastic process; the solution is a random function. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Delay Differential Equation | An equation whose derivative at a time depends on past values of the function. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Integro-Differential Equation | An equation combining a derivative with an integral of the unknown function. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Fractional Differential Equation | An equation whose derivative is of non-integer order. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Differential Equation (→ Instance) Differential-Algebraic Equation | A coupled system of differential and algebraic equations; the algebraic constraints restrict the state. |

### What is a critical conceptual evaluation of this `epistemic element instance`?

> The evaluation follows the `## Evaluation` criteria and the minimum set of the [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

> **Verdicts.** The concept is strongly identifiable and internally consistent once its domain and differentiability assumptions are fixed. It is definitionally clear at the core but underdetermined at the boundaries, because “differential equation” covers ordinary, partial, stochastic, delay, integro-differential, fractional, and differential-algebraic forms whose solution theories differ. Its representational adequacy is high for continuous, local change and weaker for discrete, nonlocal, and random dynamics unless those are explicitly typed. Its purpose adequacy is high for modelling change, but the concept should not be asked to carry the solution method or the problem specification. It is not redundant with “equation” or “dynamical system”: it adds the derivative relation that makes change stateable.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Identification** | Strong | The concept is distinguished from equation, dynamical system, solution, and solution method; the derivative relation is the differentia. |
| **Definitional Clarity** | Strong at the core, moderate at the boundary | The standard form $F(x,y,y',\ldots,y^{(n)})=0$ is precise once the domain, order, and differentiability class are declared; “differential equation” alone does not declare them. |
| **Conceptual Determinacy** | Moderate | The families are determinate, but the umbrella admits ODE, PDE, SDE, DDE, integro-differential, fractional, and differential-algebraic forms without a single boundary rule; the note supplies the family list, not a decision procedure. |
| **Internal Consistency** | Strong | The standard, operator, and weak-solution readings are compatible once the function space is fixed; mixing classical and weak differentiability without declaring it is the failure mode. |
| **Ontological Adequacy** | Strong | The concept correctly characterizes its target as a representational construct and relation, not as an act, a method, or an ontic process. |
| **Representational Adequacy** | High for continuous and local dynamics; moderate for discrete, nonlocal, and random dynamics | The notation captures derivatives and domains; SDEs, DDEs, and fractional equations require additional structure — noise, history, noninteger order — that the base notation does not carry. |
| **Discriminative Power** | Strong | It separates ODE from PDE by the number of independent variables, linear from nonlinear by the form of $F$, and the families by the structure of the derivative term. |
| **Purpose Adequacy** | Strong for modelling change; weak if used as a solution method | The concept is fit for stating constraints on a function; it is not fit for carrying the algorithm that solves them or the conditions that select a unique solution. |

## Branch

> The families are the instance branch of the decomposition; the remaining rows are cross-cutting classification axes over those families.

| **Branch** | **Description** |
| --- | --- |
| **Ordinary Differential Equations (ODEs)** | Equations involving functions of a **single independent variable** and their derivatives. Example: $\frac{dy}{dx} = x^2 + y$. |
| **Partial Differential Equations (PDEs)** | Equations involving functions of **multiple independent variables** and their partial derivatives. Example: $u_t = u_{xx}$. |
| **Linear Differential Equations** | DEs in which the unknown function and its derivatives appear **linearly** (no powers or products of the function). Example: $y'' + 3y' + 2y = 0$. |
| **Nonlinear Differential Equations** | DEs where the unknown function or its derivatives appear **nonlinearly** (powers, products, or nonlinear functions). Example: $y'' + y^2 = 0$. |
| **Homogeneous Differential Equations** | DEs where all terms involve the unknown function or its derivatives; no independent term appears. Example: $y'' - 3y' + 2y = 0$. |
| **Nonhomogeneous Differential Equations** | DEs containing a **nonzero term independent** of the unknown function. Example: $y'' - 3y' + 2y = e^x$. |
| **Exact Differential Equations** | Equations that can be expressed as the **total differential** of a function: $M(x,y)dx + N(x,y)dy = 0$ is exact if $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$. |
| **Non-exact Differential Equations** | Equations that **cannot initially** be expressed as a total differential; may require an integrating factor. |
| **Autonomous Differential Equations** | DEs where the independent variable **does not appear explicitly**. Example: $\frac{dy}{dx} = y^2 - 1$. |
| **Non-autonomous Differential Equations** | DEs where the independent variable **appears explicitly**. Example: $\frac{dy}{dx} = xy + 1$. |
| **Stochastic Differential Equations (SDEs)** | DEs that include **random processes** or noise terms, often used in modeling uncertainty or randomness. Example: $dX_t = \mu X_t dt + \sigma X_t dW_t$. |
| **Delay Differential Equations (DDEs)** | DEs in which the derivative at a certain time depends on **past values** of the function. Example: $y'(t) = y(t-1)$. |
| **Differential-Algebraic Equations (DAEs)** | Coupled systems of differential and algebraic equations; the algebraic constraints restrict the admissible states. |

## Taxonomy

> Note (🚨): The column 'Canonical Form' is used more as a convenient label; the term 'canonical' may not perfectly align with its typical semantic meaning in this context.

> The **tractability** of a **`differential equation`** refers to the ease with which it can be solved or analyzed, often depending on the existence of closed-form solutions, numerical methods, or the simplicity of its structure and boundary conditions.

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
| Delay Differential Equations (DDEs) |  | $\frac{dy(t)}{dt} = f(y(t), y(t-\tau))$ | Equations where the rate of change of the function depends on past values. |
| Integro-Differential Equations |  | $\frac{dy(t)}{dt} = \int_0^t K(t, s)y(s)ds$ | Equations that involve both integration and differentiation. |
| Fractional Differential Equations |  | $D^\alpha y(t) = f(t)$ | Equations involving derivatives of non-integer order. |
| Differential-Algebraic Equations (DAEs) |  | $F(x,y,y') = 0,\; G(x,y) = 0$ | Coupled differential and algebraic constraints; the algebraic equations restrict the state. |

## Technique Space

> Which techniques do we use to solve **differential equations**?

| **Category** | **Method** | **Description** |
| --- | --- | --- |
| **Analytical** | **Separation of Variables** | Solving equations by separating variables on opposite sides, typically used for PDEs and some ODEs. |
|  | **Integrating Factors** | Used for solving first-order linear ODEs, and for non-exact ODEs, by multiplying both sides by an integrating factor to make the equation exact. |
|  | **Exact Equations** | Solving differential equations that are exact or can be made exact by finding an integrating factor. |
|  | **Method of Characteristics** | Applied to first-order PDEs by converting them into a system of ODEs along characteristic curves. |
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
|  | **Padé Approximation** | A method for approximating functions as rational functions (ratios of polynomials), improving convergence over truncated series. |
|  | **Asymptotic Expansions** | A method for approximating the behavior of solutions in the limit of large or small parameters. |
| **Green's Function** | **Green’s Function for Laplace Equation** | Used to solve boundary value problems, especially for the Laplace or Poisson equation, by representing the solution as an integral over the domain. |
|  | **Green’s Function for Heat Equation** | Represents the solution to the heat equation as an integral involving the Green’s function, often used in diffusion problems. |
|  | **Green’s Function for Wave Equation** | Used in wave propagation problems to express the solution as an integral involving the Green’s function. |
| **Boundary and Initial Conditions** | **Dirichlet Conditions** | Boundary conditions specifying the value of the solution on the boundary of the domain. |
|  | **Neumann Conditions** | Boundary conditions specifying the derivative (slope) of the solution on the boundary. |
|  | **Cauchy Conditions** | Initial conditions for solving initial value problems, typically providing values of the solution and its derivative at $t=0$. |
| **Nonlinear Method** | **Newton's Method** | Used for solving nonlinear algebraic equations, often applied in solving nonlinear differential equations through iterative solutions. |
|  | **Bifurcation Theory** | Studies changes in the qualitative behavior of solutions as parameters in nonlinear differential equations are varied. |
|  | **Perturbation Expansion** | Expanding solutions to nonlinear problems in terms of small perturbations to an easily solvable problem. |
| **Algebraic** | **Lie Group Analysis** | Uses symmetries of the differential equation to reduce its order or transform it into a simpler equation. |
|  | **Noether’s Theorem** | Applied in physics to find conserved quantities in differential equations, often in the context of field theories. |
| **Stochastic Methods** | **Fokker-Planck Equation** | Describes the evolution of probability distributions of a system’s state, commonly used in statistical mechanics and diffusion problems. |
|  | **Itō Calculus** | A method used in stochastic differential equations (SDEs), especially in finance and physics, to model random processes. |
|  | **Stochastic Differential Equations (SDEs)** | Describes systems influenced by random noise, solved using numerical methods such as Monte Carlo simulations. |
| **Functional Methods** | **Variational Methods** | Methods for finding approximate solutions by minimizing or maximizing a functional, often used in physical systems modeled by PDEs. |
|  | **Euler-Lagrange Equation** | Derives the equations of motion for a system in physics, often resulting in second-order differential equations. |
|  | **Action Principle** | Used to derive equations of motion by requiring that the action is stationary, typically resulting in ODEs or PDEs. |
| **Linear vs. Nonlinear Solutions** | **Linear Superposition** | Applied to linear ODEs and PDEs where solutions can be superimposed to form the general solution. |
|  | **Nonlinear Superposition** | In nonlinear systems, superposition is generally not valid; however, methods like the method of characteristics or perturbation theory may be used. |
| **Homogeneous vs. Inhomogeneous** | **Homogeneous Solutions** | Solutions to differential equations where the right-hand side (source term) is zero. |
|  | **Inhomogeneous Solutions** | Solutions to equations with non-zero source terms, often requiring methods like Green's functions or particular solution techniques. |
| **Approximation Methods** | **Finite Volume Method** | A numerical technique for solving PDEs, focusing on the conservation of fluxes across small control volumes within the domain. |

### Computational Method

- [ ] [Euler Method](/view.html?p=notes/epistemica/singular/euler-method.md)

## Boundary Value Problems (BVPs)

> A **boundary value problem (BVP)** consists of a differential equation together with conditions imposed at two or more distinct points of the domain, typically at its boundaries.

## Initial Value Problems (IVPs)

> An **initial value problem (IVP)** consists of a differential equation together with conditions imposed at a single point of the domain, typically the initial condition.

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) — the epistemic schema, the permitted link forms, and the Arithmetic case study.
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md) — the `## Evaluation` criteria used in the conceptual evaluation.
- [Differential Equation — Wikipedia](https://en.wikipedia.org/wiki/Differential_equation)
- [A Case Study of a Dissipative System: Damped Pendulum](https://app.notion.com/p/A-Case-Study-of-a-Dissipative-System-Damped-Pendulum-1ebc0f5171ec80c09a6af45b6f968c2b?pvs=21)
- [Ordinary Differential Equations — Notebook](https://github.com/dbremont/algorithms/blob/main/cm/ode.ipynb)
- [Integral Calculus — Notebook](https://github.com/dbremont/algorithms/blob/main/cm/integral.ipynb)
- [Differential Calculus — Notebook](https://github.com/dbremont/algorithms/blob/main/cm/differential.ipynb)
- Arnold, V. I. (1973). *Ordinary differential equations*. MIT Press.
- Boyer, C. B., & Merzbach, U. C. (1991). *A history of mathematics* (2nd ed.). John Wiley & Sons.
- Coddington, E. A., & Levinson, N. (1955). *Theory of ordinary differential equations*. McGraw-Hill.
- Evans, L. C. (2010). *Partial differential equations* (2nd ed.). American Mathematical Society.
- Euler, L. (1755). *Institutiones calculi differentialis cum eius usu in analysi finitorum ac doctrina serierum*. Academiae Imperialis Scientiarum Petropolitanae.
- Euler, L. (1768–1770). *Institutiones calculi integralis* (Vols. 1–3). Academiae Imperialis Scientiarum Petropolitanae.
- Fourier, J. (1822). *Théorie analytique de la chaleur*. Firmin Didot.
- Hairer, E., Nørsett, S. P., & Wanner, G. (1993). *Solving ordinary differential equations I: Nonstiff problems* (2nd ed.). Springer.
- Hairer, E., & Wanner, G. (1996). *Analysis by its history*. Springer.
- Hartman, P. (1964). *Ordinary differential equations*. John Wiley & Sons.
- Ince, E. L. (1926). *Ordinary differential equations*. Longmans, Green and Co.
- Jahnke, H. N. (Ed.). (2003). *A history of analysis*. American Mathematical Society and London Mathematical Society.
- Kline, M. (1972). *Mathematical thought from ancient to modern times*. Oxford University Press.
- Logan, J. D. (2015). *Applied mathematics* (4th ed.). John Wiley & Sons.
- Lyapunov, A. M. (1992). *The general problem of the stability of motion*. Taylor & Francis. (Original work published 1892).
- Newton, I. (1687). *Philosophiæ naturalis principia mathematica*. Josephi Streater.
- Øksendal, B. (2003). *Stochastic differential equations: An introduction with applications* (6th ed.). Springer.
- Podlubny, I. (1999). *Fractional differential equations*. Academic Press.
- Poincaré, H. (1892–1899). *Les méthodes nouvelles de la mécanique céleste* (Vols. 1–3). Gauthier-Villars.
- Schwartz, L. (1950–1951). *Théorie des distributions* (Vols. 1–2). Hermann.
- Simmons, G. F. (1972). *Differential equations with applications and historical notes*. McGraw-Hill.
- Sobolev, S. L. (1963). *Applications of functional analysis in mathematical physics*. American Mathematical Society.
- Strogatz, S. H. (2015). *Nonlinear dynamics and chaos: With applications to physics, biology, chemistry, and engineering* (2nd ed.). Westview Press.
- Teschl, G. (2012). *Ordinary differential equations and dynamical systems*. American Mathematical Society.
- Archibald, T., Fraser, C., & Grattan-Guinness, I. (2005). The history of differential equations, 1670–1950. *Oberwolfach Reports, 2*(4). https://ems.press/journals/owr/articles/765
