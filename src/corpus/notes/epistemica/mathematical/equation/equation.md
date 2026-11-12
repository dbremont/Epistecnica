---
tags: [note, mathematics, equation, notation]
---

# Equation

> An **equation** is a statement that asserts the equality of two expressions.

> La palabra **"ecuación"** proviene del latín **"aequatio"**, que a su vez deriva del verbo **"aequare"**, que significa **"igualar"** o **"hacer igual"**. Este verbo está relacionado con la raíz **"aequus"**, que significa **"igual"** o **"equilibrado"**.

### What is the technical (mathematical) Essence of an Equation?

> A mathematical constraint that defines the admissible combinations of values of a set of variables or mathematical elements through an equality relationship.

### What is the operational (epistemological) Essence of an Equation?

> We begin with a piece of reality and partition and structure it in terms of mathematical elements. We then seek to describe selected aspects of that reality by formulating equality relationships among those elements, thereby imposing constraints on their possible values and configurations. These constraints capture selected relationships within the phenomenon and allow us to derive the possible states consistent with our mathematical representation.

> The deeper idea is that equations allow us to encode what we know about a phenomenon as explicit mathematical constraints, while leaving unknown or uncharacterized aspects unconstrained. This enables us to represent partial knowledge without requiring a complete description of reality.

> As new knowledge becomes available, we can incorporate it by introducing additional mathematical elements and constraints, refining or extending our existing equations. This progressively reduces the space of admissible possibilities, enabling us to derive further implications and move from a partial representation toward an increasingly comprehensive description of reality.

## Which are the types of equations?

| Type | Form | Constraint Value Type | Description | Operational Role |
|---|---|---|---|---|
| **Algebraic** | \(f(x_1,\ldots,x_n)=g(x_1,\ldots,x_n)\) | Scalar | Establishes equality between algebraic expressions. | Constrains possible values of mathematical quantities. |
| **Polynomial** | \(a_nx^n+\cdots+a_1x+a_0=0\) | Scalar | Establishes a polynomial relationship between variables and coefficients. | Represents polynomial dependencies. |
| **Rational** | \(\frac{P(x)}{Q(x)}=0\) | Scalar | Establishes relationships involving ratios of polynomial expressions. | Represents quotient-based dependencies. |
| **Exponential** | \(a^x=f(x)\) | Scalar | Relates quantities through exponential functions. | Represents exponential growth and decay. |
| **Logarithmic** | \(\log_a(x)=f(y)\) | Scalar | Establishes relationships involving logarithmic functions. | Represents logarithmic dependencies. |
| **Trigonometric** | \(\sin(x)=f(y)\) | Scalar | Establishes relationships involving trigonometric functions. | Represents angular and periodic relationships. |
| **Hyperbolic** | \(\sinh(x)=f(y)\) | Scalar | Establishes relationships involving hyperbolic functions. | Represents hyperbolic dependencies. |
| **Differential** | \(F(x,y,y',\ldots,y^{(n)})=0\) | Scalar / Function | Relates unknown functions to their derivatives. | Constrains continuous change and evolution. |
| **Integral** | \(\int_a^b f(x)\,dx=c\) | Scalar | Establishes relationships involving integrals. | Represents accumulation and aggregate quantities. |
| **Integro-differential** | \(F(x,y,y',\int y\,dx)=0\) | Scalar / Function | Combines differential and integral relationships. | Represents local changes and accumulated effects. |
| **Difference** | \(x_{t+1}-x_t=f(x_t)\) | Scalar / Sequence | Relates quantities across discrete steps. | Represents discrete evolution and transitions. |
| **Functional** | \(F[f]=g\) | Function | Establishes relationships involving unknown functions. | Constrains entire functions or mappings. |
| **Matrix** | \(A\mathbf{x}=\mathbf{b}\) | Vector / Matrix | Establishes relationships through matrix operations. | Represents interconnected linear systems. |
| **Tensor** | \(\mathcal{F}(\mathbf{T})=\mathbf{S}\) | Tensor | Establishes relationships involving tensors. | Represents multidimensional transformations and dependencies. |
| **Stochastic** | \(X_t=f(X_{t-1})+\varepsilon_t\) | Random Variable / Stochastic Process | Incorporates randomness into mathematical relationships. | Represents systems involving uncertainty and random variation. |
| **Probabilistic** | \(P(X=x)=p\) | Probability / Distribution | Establishes relationships involving probabilities and distributions. | Represents probabilistic outcomes. |
| **Statistical** | \(Y=\beta_0+\beta_1X+\varepsilon\) | Random Variable / Sample | Represents relationships between variables through statistical models. | Estimates associations and explains observed variation. |
| **Optimization** | \(\nabla f(x)=0\) | Scalar / Vector | Expresses mathematical conditions associated with optimization. | Identifies candidate optimal solutions. |
| **Implicit** | \(F(x,y)=0\) | Scalar | Defines relationships without explicitly isolating a dependent variable. | Represents implicitly defined mathematical relationships. |
| **Parametric** | \(x=f(t),\ y=g(t)\) | Scalar / Vector | Defines variables as functions of one or more parameters. | Represents parameterized relationships and trajectories. |
| **Recursive** | \(x_n=f(x_{n-1},x_{n-2},\ldots)\) | Scalar / Sequence | Defines quantities in terms of previously established quantities. | Represents recursive dependencies and sequences. |
| **Conservation** | \(\frac{dQ}{dt}=0\) | Scalar / Vector / Tensor | Expresses the conservation of a quantity within a system. | Constrains the evolution of conserved quantities. |
| **Balance** | \(\text{Inflow}-\text{Outflow}=\text{Accumulation}\) | Scalar / Vector | Relates incoming, outgoing, and accumulated quantities. | Represents mass, energy, financial, and material balances. |
| **State-space** | \(\dot{\mathbf{x}}=A\mathbf{x}+B\mathbf{u}\) | Vector / Matrix | Relates system states, inputs, and their evolution. | Represents the dynamics of a system. |
| **Eigenvalue** | \(A\mathbf{v}=\lambda\mathbf{v}\) | Scalar / Vector | Relates a linear transformation to its invariant directions and scaling factors. | Identifies characteristic modes and properties of transformations. |
| **Equilibrium** | \(f(x^*)=0\) | Scalar / Vector | Establishes conditions under which a system has no net change. | Identifies stationary or equilibrium states. |
| **Partial Differential** | \(F(x,y,u,u_x,u_y,\ldots)=0\) | Function / Field | Relates an unknown function to its partial derivatives. | Constrains spatial and temporal variations of fields. |
| **Delay Differential** | \(x'(t)=f(x(t),x(t-\tau))\) | Function / History | Relates the current rate of change to present and past states. | Represents systems with delayed responses and memory. |
| **Fractional Differential** | \(D^\alpha y(t)=f(t,y)\) | Function | Relates an unknown function to its fractional-order derivatives. | Represents nonlocal dynamics and memory-dependent processes. |
| **Operator** | \(L(u)=f\) | Map of Function Spaces | Constrains mappings through transformations between mathematical spaces. |  |
| **Operator Eigenvalue** | \(L(u)=\lambda u\) | Scalar / Function | Relates an operator to its eigenfunctions and eigenvalues. | Identifies characteristic modes of operators. |
| **Nonlinear** | \(F(x_1,\ldots,x_n)=0\) | Scalar / Vector / Function | Establishes nonlinear relationships among unknown quantities. | Represents nonlinear dependencies and interactions. |
| **Polynomial System** | \(P_i(x_1,\ldots,x_n)=0\) | Scalar / Vector | Establishes multiple polynomial constraints over shared variables. | Determines simultaneous solutions to polynomial relationships. |
| **Diophantine** | \(P(x_1,\ldots,x_n)=0,\quad x_i\in\mathbb Z\) | Integer | Establishes polynomial constraints with integer-valued unknowns. | Identifies integer solutions to algebraic relationships. |
| **Boolean** | \(A\land B=C\) | Boolean | Establishes relationships among logical variables and operations. | Constrains logical states and conditions. |
| **Set-Valued** | \(F(x)\ni y\) | Set | Relates quantities through mappings that may produce multiple admissible values. | Represents multivalued relationships and admissible solution sets. |
| **Complementarity** | \(x\geq0,\ y\geq0,\ xy=0\) | Scalar / Vector | Establishes complementary conditions between variables. | Represents mutually exclusive active constraints. |
| **Boundary-Value** | \(y''=f(x,y),\quad y(a)=\alpha,\ y(b)=\beta\) | Function / Boundary Values | Combines a differential equation with conditions imposed at domain boundaries. | Determines solutions satisfying prescribed boundary conditions. |
| **Initial-Value** | \(y'=f(t,y),\quad y(t_0)=y_0\) | Function / Initial Values | Combines a differential equation with prescribed initial conditions. | Determines system evolution from an initial state. |
| **Integral Equation** | \(y(x)=f(x)+\lambda\int_a^b K(x,t)y(t)\,dt\) | Function | Defines an unknown function through an integral relationship. | Constrains functions through accumulated or nonlocal dependencies. |
| **Stochastic Differential** | \(dX_t=\mu(X_t,t)dt+\sigma(X_t,t)dW_t\) | Stochastic Process | Relates stochastic processes to deterministic and random differential components. | Models continuous evolution under randomness. |
| **Permutation** | \(\pi(\pi(i))=i\) | Permutation | Establishes constraints on permutations or their compositions. | Represents permutation properties, compositions, and structural arrangements. |

## Which are the set of properties (attributes) that can be attributed to equations?

> **Equation** properties describe the **characteristics** used to analyze, classify, and distinguish equations independently of their particular mathematical form.

| Property | Description | Scope |
|---|---|---|
| **Degree** | Highest exponent of the unknown variable in a polynomial equation. | Algebraic structure |
| **Linearity** | Indicates whether the equation expresses linear relationships between its unknowns or functions. | Mathematical structure |
| **Homogeneity** | Indicates whether an equation is homogeneous or contains independent terms. | Mathematical structure |
| **Order** | Highest order of derivative appearing in a differential equation. | Differential structure |
| **Dimensionality** | Number of independent variables or dimensions involved. | Mathematical structure |
| **Number of Unknowns** | Number of unknown quantities or functions involved. | Mathematical composition |
| **Number of Terms** | Number of distinct terms appearing in the equation. | Mathematical composition |
| **Explicitness** | Indicates whether an unknown is isolated and expressed directly in terms of other quantities. | Mathematical representation |
| **Completeness** | Indicates whether the equation includes all necessary terms and conditions for the intended mathematical formulation. | Mathematical formulation |
| **Determinacy** | Indicates whether the constraints establish a unique solution, multiple solutions, or leave the solution underdetermined. | Solution structure |
| **Consistency** | Indicates whether the equation or system admits at least one solution. | Solution structure |
| **Solvability** | Indicates whether solutions can be obtained analytically, numerically, or through other methods. | Solution properties |
| **Existence** | Concerns whether at least one solution exists within the specified domain. | Solution properties |
| **Uniqueness** | Indicates whether the equation admits exactly one solution under the specified conditions. | Solution properties |
| **Domain** | Set of admissible values for the variables and expressions involved. | Mathematical definition |
| **Solution Set** | Set of all values or configurations satisfying the equation. | Solution properties |
| **Symmetry** | Indicates whether the equation remains invariant under specified transformations. | Structural properties |
| **Periodicity** | Indicates whether the equation exhibits repeating behavior over specified intervals or transformations. | Behavioral properties |
| **Reversibility** | Indicates whether the mathematical relationship can be inverted to recover its inputs from its outputs. | Relational properties |
| **Stability** | Indicates whether solutions or system behavior remain bounded or respond continuously to perturbations, according to the relevant stability notion. | Behavioral properties |
| **Sensitivity** | Measures how solutions or outputs respond to changes in parameters, coefficients, or initial conditions. | Behavioral properties |
| **Approximation Error** | Measures the deviation between an approximate solution and the exact solution or reference value. | Numerical properties |

## What Is the History of the Equals Sign (=)?

> The "=" symbol was introduced in **1557** by **Robert Recorde**, who wrote:

> “...to avoid the tedious repetition of the words 'is equal to', I will set, as I often do in work use, a pair of parallels or twin lines of one length, thus: ‘=’, because no two things can be more equal.” (Recorde, 1557)

The sign’s adoption was gradual; for its history and standardization, see Cajori (1928–1929), Mazur (2014), and Roberts and Smith (2012).

## What Is the Meaning and Essence of the Equals Sign (=)?

| Dimension | Aspect | Description |
|---|---|---|
| Symbolic | Symbol | \(=\) |
| Semantic | Meaning | Expresses equality between two mathematical expressions. |
| Relational | Relationship | Asserts that both sides represent the same mathematical value. |
| Structural | Operands | Relates a left-hand expression (LHS) to a right-hand expression (RHS). |
| Logical | Assertion | Establishes a proposition that can be evaluated as true or false. |
| Relational | Symmetry | Equality holds regardless of the order of its operands. |
| Representational | Equivalence | Allows different mathematical expressions to represent the same value. |
| Operational | Substitutability | Allows equal expressions to replace one another while preserving equality. |
| Constraint | Restriction | Restricts admissible values or configurations to those satisfying the equality. |
| Solving | Solution | Identifies values that make an equality true. |
| Inferential | Deduction | Enables mathematical transformations and derivations based on equality. |
| Modeling | Representation | Expresses equivalences and conditions identified within a mathematical representation of reality. |
| Epistemological | Knowledge expression | Makes asserted equivalences and known conditions explicit within mathematical reasoning. |


## Reference

- [Equality Sign](https://en.wikipedia.org/wiki/Equals_sign)
- Alaee, D. Z., Sayre, E. C., Kornick, K., & Franklin, S. V. (2022). How physics textbooks embed meaning in the equals sign. *American Journal of Physics, 90*(4), 273–278. https://doi.org/10.1119/10.0009096
- Cajori, F. (1928–1929). *A history of mathematical notations* (Vols. 1–2). Open Court.
- Frege, G. (1948). Sense and reference (M. Black, Trans.). *The Philosophical Review, 57*(3), 209–230. https://doi.org/10.2307/2181485 (Original work published 1892)
- Jones, I., & Pratt, D. (2006). Connecting the equals sign. *International Journal of Computers for Mathematical Learning, 11*(3), 301–325. https://doi.org/10.1007/s10758-006-9107-6
- Kieran, C. (1981). Concepts associated with the equality symbol. *Educational Studies in Mathematics, 12*(3), 317–326. https://doi.org/10.1007/BF00311062
- Mazur, J. (2014). *Enlightening symbols: A short history of mathematical notation and its hidden powers*. Princeton University Press.
- McNeil, N. M., Grandau, L., Knuth, E. J., Alibali, M. W., Stephens, A. C., Hattikudur, S., & Krill, D. E. (2006). Middle-school students’ understanding of the equal sign: The books they read can’t help. *Cognition and Instruction, 24*(3), 367–385. https://doi.org/10.1207/s1532690xci2403_3
- Mirin, A. (2019). The relational meaning of the equals sign: A philosophical perspective. In *Proceedings of the 22nd Annual Conference on Research in Undergraduate Mathematics Education*. http://sigmaa.maa.org/rume/crume2019/Papers/151.pdf
- Opsal, H., & Topphol, A. K. (2023). The problematic equal sign. *Nordic Studies in Mathematics Education, 28*(1–2), 99–112. https://doi.org/10.7146/nomad.v28i1-2.149263
- Recorde, R. (1557). *The whetstone of witte*. John Kyngstone. https://archive.org/details/TheWhetstoneOfWitte
- Roberts, G., & Smith, F. (Eds.). (2012). *Robert Recorde: The life and times of a Tudor mathematician*. University of Wales Press.
- Vincent, J., Bardini, C., Pierce, R., & Pearn, C. (2015). Misuse of the equals sign: An entrenched practice from early primary years to tertiary mathematics. *Australian Senior Mathematics Journal, 29*(2), 31–39.
- Wittgenstein, L. (1961). *Tractatus logico-philosophicus* (D. F. Pears & B. F. McGuinness, Trans.). Routledge & Kegan Paul. (Original work published 1921)
