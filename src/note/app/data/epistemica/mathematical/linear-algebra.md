---
tags: [linear-algebra]
---

# Linear  Algebra

 : Linear Space (Linear%20Space%20b935942a1a064729b3f2be42d174923a.md), Matrix (Matrix%20171c0f5171ec80c58898c4e26151fbb8.md), Normed Vector Space (Normed%20Vector%20Space%20171c0f5171ec80049680d68f0ec033b4.md), Norm (Norm%20170c0f5171ec8070b6c5f594eeab1e7b.md)

> Linear algebra is **not a algebra**,  is the study of linear systems and the structures and techniques—like vectors, matrices, and linear transformations—used to analyze and solve them.
> 

- **Problem Space:** The set of all possible linear systems or configurations we want to study or solve.
- **Representation:** The way we encode elements of the problem space, e.g., using vectors, matrices, or linear transformations.
- **Computation:** The techniques and algorithms we apply to manipulate these representations and find solutions.

## Representation

- [ ]  Matrix
- [ ]  System of Equation
- [ ]  Vector Space
    - [ ]  Linear Span
    - [ ]  …
- [ ]  Operator
- [ ]  **Basis:** A set of linearly independent vectors whose linear combinations generate the entire vector space; provides coordinates for representation.
- [ ]  Coordinate System: Assignment of numerical values to vectors relative to a chosen basis; allows concrete computation and comparison.
- [ ]  Tensor
- [ ]  Network Representation: Some linear systems can be represented as graphs, where adjacency or incidence matrices capture connections and flows.
- [ ]  Functional Representation: In infinite-dimensional vector spaces (like function spaces), functions themselves are vectors, and operators act on them linearly.
- [ ]  **Decompositions:** Representations of matrices as products of simpler matrices (e.g., LU, QR, SVD) that reveal structure, simplify computation, and expose fundamental properties.
- [ ]  **Augmented Matrices:** Matrices that combine the coefficients and constants of linear systems to simplify solving via elimination methods.
- [ ]  **Dual Space Representation:** Represents linear functionals acting on a vector space, providing another perspective on linear relationships.
- [ ]  Bilinear Form
- [ ]  Quadratic Forms
- [ ]  Trace
- [ ]  Characteristic Polynomial
- [ ]  Minimal Polynomial
- [ ]  **Linear Map**

## Property

- **Eigenvectors and Eigenvalues:** Special representation highlighting directions invariant under a linear operator; crucial for diagonalization, stability analysis, and decompositions.
- Determinant
- …

### Technique

> A **linear method** is a mathematical approach that operates on linear relationships or functions, where the output changes proportionally to changes in the input, following a straight line pattern.
> 

| **Method** | **Description** |
| --- | --- |
| **Gaussian Elimination** | A method for solving linear systems by systematically eliminating variables from equations until a unique solution is found. |
| **Matrix Inversion** | Solving a linear system by finding the inverse of the coefficient matrix and multiplying it with the constant vector. |
| **Matrix Factorization (LU Decomposition)** | Decomposing the coefficient matrix into lower and upper triangular matrices to simplify solving linear systems. |
| **Iterative Methods (e.g., Jacobi, Gauss-Seidel)** | Methods that iteratively refine an initial guess until a solution to the linear system is reached. |
| **Least Squares Approximation** | A technique used when the linear system is overdetermined, finding the solution that minimizes the sum of squared differences between observed and predicted values. |
| **Eigenvalue Decomposition** | Decomposing the coefficient matrix into eigenvectors and eigenvalues to analyze the behavior of the linear system. |
| **QR Decomposition** | Decomposing the coefficient matrix into an orthogonal and upper triangular matrix to simplify solving linear systems. |
| **Cholesky Decomposition** | Decomposing the coefficient matrix into the product of a lower triangular matrix and its conjugate transpose to efficiently solve symmetric positive definite linear systems. |

### Decomposition

> 

### Canonical System

> In linear algebra, systems like the Vandermonde matrix—a specific class of matrices—serve as base structures, possessing well-defined properties and canonical techniques that allow us to solve certain problems efficiently; this pattern of studying special structures with associated methods recurs throughout linear algebra, in a way similar to how standard forms and techniques appear in integral calculus.
> 

| Canonical System | Structure | Main Uses |
| --- | --- | --- |
| **Vandermonde Matrix** | Rows are geometric progressions of variables | Polynomial interpolation, determinant formulas, solving systems |
| **Diagonal Matrix** | Nonzero entries only on the main diagonal | Simplifies matrix powers, eigenvalue problems, linear transformations |
| **Identity Matrix** | Diagonal entries = 1, all others = 0 | Neutral element for multiplication, basis reference |
| **Triangular Matrix (Upper / Lower)** | Entries below or above the diagonal are zero | Solving systems via forward/backward substitution |
| **Symmetric Matrix** | Equal to its transpose | Quadratic forms, eigenvalue decomposition, optimization |
| **Orthogonal / Unitary Matrix** | Columns (or rows) form an orthonormal basis | Preserves lengths and angles; rotations; diagonalization |
| **Permutation Matrix** | One 1 per row/column, rest 0 | Reordering elements, pivoting in elimination |
| **Toeplitz Matrix** | Constant along each diagonal | Signal processing, convolution, fast algorithms |
| **Circulant Matrix** | Each row is a cyclic shift of the previous row | FFT applications, convolution problems |
| **Nilpotent Matrix** | Some power of the matrix equals zero | Jordan canonical forms, linear operator analysis |
| **Jordan Block / Jordan Matrix** | Upper triangular with eigenvalues on diagonal and ones on superdiagonal | Jordan decomposition, linear operator structure |
| **Diagonalizable Matrix** | Can be written as PDP$^{-1}$ with DD diagonal | Simplifies powers, differential equations, dynamical systems |
| **Augmented Matrix** | Combines coefficients and constants of a linear system | Solving linear systems via elimination |
| **Sparse Matrix** | Mostly zeros or follow a pattern | Efficient storage and computation in large-scale systems |
| **Block Matrix** | Divided into sub-matrices or “blocks” | Simplifies computations and analysis in large or coupled systems |

## Algebraic Structure

> Which are algebraic structures are study in linear algebra?
> 

| **Category** | **Structure** | **Description** | **Case** |
| --- | --- | --- | --- |
| **Scalar Base** | Field | Set of scalars with addition, multiplication, inverses (except zero), distributive law | ℝ, ℂ, ℚ |
| **Core Space** | Vector Space | Set of vectors over a field with vector addition and scalar multiplication satisfying 8 axioms | ℝ³, ℂⁿ |
| **Substructure** | Subspace | Subset of vector space that is itself a vector space | Span of a set of vectors |
| **Geometric Decoration** | Inner Product Space | Vector space with an inner product defining angles and lengths | ℝ² with dot product; Hilbert spaces in QM |
| **Geometric Decoration** | Normed / Banach Space | Vector space with a norm, possibly complete | ℓ² space of square-summable sequences |
| **Associative Algebra** | Matrix Algebra | Vector space with associative bilinear multiplication (matrix multiplication) | Mₙ(ℝ) — n×n matrices |
| **Associative Algebra** | Tensor Algebra | Algebra of tensors of all orders over a vector space | Multilinear maps in physics / engineering |
| **Associative Algebra** | Symmetric Algebra | Algebra of symmetric tensors | Polynomials over vector space |
| **Associative Algebra** | Exterior / Grassmann Algebra | Algebra of antisymmetric tensors | Differential forms in geometry |
| **Associative Algebra** | C*-Algebra / Operator Algebra | Algebra of bounded operators on a Hilbert space, closed under adjoint and norm | Quantum observables, functional analysis |
| **Non-Associative Algebra** | Jordan Algebra | Commutative algebra with Jordan identity: x²∘(x∘y) = x∘(x²∘y) | Symmetric matrices under x∘y = ½(xy+yx), quantum mechanics observables |
| **Non-Associative Algebra** | Lie Algebra | Algebra with anti-commutative bracket [x,y], Jacobi identity | so(3) — rotations in 3D space, symmetry groups |
| **Division Algebra** | Quaternions, Octonions | Algebra where nonzero elements have inverses; may be non-commutative | ℍ (quaternions), ℝ⁸ (octonions) |
| **Geometric / Clifford** | Clifford Algebra | Associative algebra generated by a vector space with a quadratic form | Spinors, Dirac matrices, geometric algebra |

### Use

| **Field** | **Application** | **Description** |
| --- | --- | --- |
| **Computer Graphics** | Transformations (scaling, rotating, translating) | Linear algebra is used to manipulate graphical objects via transformation matrices. |
| **Machine Learning** | Data Representation, Dimensionality Reduction (PCA), and Optimization | Vectors and matrices represent data points, while eigenvectors/eigenvalues help in reducing dimensions. |
| **Physics** | Quantum Mechanics, Mechanics of Rigid Bodies | State vectors describe quantum states, and linear transformations represent physical phenomena. |
| **Economics** | Input-Output Models, Game Theory | Linear algebra models relationships between industries (input-output) and payoff matrices in strategic interactions. |
| **Engineering** | Electrical Circuit Analysis, Structural Analysis, Control Systems | Solving systems of linear equations helps analyze circuits, structures, and dynamic systems. |
| **Data Science** | Data Representation, Linear Regression | Datasets are represented in matrix form, and linear regression uses least-squares methods for prediction models. |
| **Computer Vision** | Image Processing, Feature Detection | Matrices represent images, and transformations such as convolution are used for edge detection and filtering. |
| **Cryptography** | Encryption Algorithms | Linear algebra underpins cryptographic methods like coding theory and secure communication protocols. |
| **Robotics** | Kinematics, Path Planning | Vectors and matrices are used to represent positions, movements, and configurations in robot motion. |
| **Genomics** | Gene Expression Analysis, Genetic Data Clustering | Matrix factorization helps analyze high-dimensional genetic data and cluster gene expression profiles. |
| **Signal Processing** | Filtering, Fourier Transforms | Signals are represented as vectors and matrices, and transformations like DFT/FFT are essential for processing. |
| **Econometrics** | Linear Regression, Time Series Analysis | Matrices model economic data relationships and trends, and linear algebra solves regression systems. |
| **Artificial Intelligence** | Neural Networks | Linear algebra operations like matrix multiplication are central to the function of neural networks. |
| **Chemistry** | Molecular Orbital Theory, Spectroscopy | Linear algebra models atomic orbitals and their interactions in molecular systems. |
| **Network Theory** | Graph Theory, Social Network Analysis | Adjacency and incidence matrices represent networks, and eigenvalues help identify key nodes and patterns. |
| **Operations Research** | Linear Programming, Optimization | Linear algebra is used to solve optimization problems in resource allocation and scheduling. |
| **Statistics** | Covariance Matrices, Multivariate Analysis | Linear algebra underlies techniques like Principal Component Analysis (PCA) and handling multivariate distributions. |
| **Economy & Finance** | Portfolio Optimization, Risk Management | Linear algebra helps model asset returns, risks, and optimize financial portfolios. |
| **Geology** | Seismic Data Analysis | Matrices are used to represent and process seismic waves and data for analysis and predictions. |
| **Robotics and Automation** | Inverse Kinematics, Trajectory Planning | Linear algebra helps solve systems to determine the movement of robotic arms or mobile robots. |
| **Computer-Aided Design (CAD)** | 3D Modeling and Rendering | Linear algebra allows for the creation, transformation, and rendering of complex 3D models. |
| … | … | … |

## References

- https://en.wikipedia.org/wiki/System_of_linear_equations
- https://en.wikipedia.org/wiki/Vandermonde_matrix
