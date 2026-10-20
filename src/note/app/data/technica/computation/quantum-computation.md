# Quantum Computation

> In this note, we analyze the ontic and epistemic structure of quantum computation from a general perspective, examining how quantum-mechanical processes are  harnessed to  to create computational substrate.
> 

> Qubits (quantum states) – Quantum gates (unitary operators: the fundamental primitives for specifying quantum computations).
> 

Quantum Computation:

- Abstract Quantum Models of Computation: **Quantum models of computation** explore various algorithms and protocols that take advantage of quantum properties such as superposition and entanglement to perform specific tasks more efficiently than classical algorithms. Examples of such tasks include factoring large numbers, searching unsorted databases, and simulating quantum systems.
- Concrete  Quantum Computers Models
- **Machine:** What is the space of quantum computing machines? What characterizes a quantum computing machine?
- Program
    - What is the data model?
    - What is the notion of computation (State Change)?
- Evaluation
- What is the expersabilty  of such computing models? Is  a  quantugm computer faster than a classical computer?
- Abstarction Hierchy to Specify Computations

Physical system

↓

Quantum state (Hilbert space vector)

↓

Unitary operators (gates)

↓

Circuits (compositions of gates)

↓

Subroutines / patterns

↓

Algorithms

↓

Computational models

Guiding Questions:

- What is the ontic status of quantum computation? Is it an `*ars practica*`, an epistemic field, both,  or something else? Is it a set of techniques, a class of problems, a domain of phenomena, or a constituent of reality itself?

## Models

> Computations somehow must be encoded in this models.
> 
1. **Quantum Turing Machine (QTM)**: This is a theoretical model of computation that extends the classical Turing machine to operate with quantum states. It was introduced by physicist David Deutsch in 1985.
2. **Quantum Circuit Model**: In this model, quantum computation is represented as a sequence of quantum gates acting on a set of qubits. These gates manipulate the quantum state of the qubits to perform computations.
3. **Adiabatic Quantum Computation (AQC)**: This model utilizes the adiabatic theorem from quantum mechanics to perform computations. It starts with a simple Hamiltonian whose ground state is easy to prepare and gradually transforms into a Hamiltonian representing the problem of interest.
4. **Quantum Annealing**: This variation of adiabatic quantum computation focuses on solving optimization problems. Quantum annealers use quantum effects to explore the solution space and find the optimal solution to a given problem.
5. **Measurement-Based Quantum Computation (MBQC)**: In this model, quantum computation is performed by preparing an entangled state (usually a cluster state) and then measuring individual qubits according to a specific pattern. The computation emerges from the correlations between the measurement outcomes.
6. **Topological Quantum Computation**: This model utilizes non-Abelian anyons, which emerge as qubits in certain topological phases of matter. The computation is performed by braiding these anyons, which induces transformations in the quantum state.
7. **Holonomic Quantum Computation**: This model relies on geometric phases (such as Berry phases) to perform quantum computation. The quantum state is manipulated by adiabatically evolving it along a closed path in parameter space, accumulating geometric phases that encode the computation.

## Quantum Computation Models - Building Blocks

Sure, here's a list of fundamental ingredients of quantum computations:

1. **Qubits (Quantum Bits)**: Qubits are the basic units of quantum information analogous to classical bits. However, qubits can exist in superposition states, unlike classical bits, allowing them to represent multiple classical bits simultaneously.
2. **Superposition**: Qubits can exist in a superposition of states, meaning they can combine 0 and 1 states simultaneously. This property enables quantum parallelism and forms the basis for many quantum algorithms.
3. **Entanglement**: Entanglement is a phenomenon where the quantum states of multiple qubits become correlated so that the state of one qubit cannot be described independently of the state of the others. Entanglement is a crucial resource in quantum computing that enables specific quantum algorithms and communication protocols.
4. **Quantum Gates**: Quantum gates are the basic building blocks of quantum circuits, analogous to classical logic gates. They manipulate qubits' quantum states, enabling superposition, entanglement, and measurement operations.
5. **Quantum Measurement**: Quantum measurement is extracting classical information from a quantum system. When a qubit is measured, it collapses to one of its basis states (0 or 1) with specific probabilities determined by its quantum state.
6. **Quantum Algorithms**: Quantum algorithms are algorithms designed to run on quantum computers, leveraging the principles of **superposition** and **entanglement** to solve problems more efficiently than classical algorithms.
7. **Quantum Error Correction**: Quantum error correction is a set of techniques to protect quantum information from errors caused by decoherence and other noise in quantum systems. It is essential for building reliable and scalable quantum computers.
8. **Quantum Gates Sets**: Similar to classical computing, quantum computing has a set of basic operations (quantum gates) that can be combined to perform arbitrary quantum computations. Examples include the Pauli-X gate, Hadamard gate, CNOT gate, and many others.

## Algorithms

1. **Grover's Algorithm**: Grover's algorithm provides a quadratic speedup over classical algorithms for unstructured search problems. It can be used to find a marked item in an unsorted database of size N with O(√N) queries, compared to O(N) queries in classical algorithms.
2. **Shor's Algorithm**: Shor's algorithm is a quantum algorithm for integer factorization, which efficiently factors large composite integers into their prime factors. It demonstrates exponential speedup over the best-known classical algorithms, posing a potential threat to classical cryptographic systems like RSA.
3. **Quantum Phase Estimation (QPE)**: QPE is a fundamental quantum algorithm used to estimate the eigenvalues of unitary operators. It has applications in various quantum algorithms, including Shor's algorithm and quantum simulation.
4. **Quantum Fourier Transform (QFT)**: The QFT is a quantum analog of the classical discrete Fourier transform. It efficiently computes the discrete Fourier transform of quantum states and serves as a key subroutine in many quantum algorithms, including Shor's algorithm.
5. **Quantum Walks**: Quantum walks are quantum analogs of classical random walks, in which a quantum particle evolves on a graph according to quantum mechanical principles. They have applications in algorithms for searching, graph theory, and optimization.
6. **HHL Algorithm (Harrow-Hassidim-Lloyd)**: The HHL algorithm is a quantum algorithm for solving systems of linear equations, which shows exponential speedup over classical algorithms for certain types of problems. It has applications in machine learning, optimization, and quantum simulation.
7. **Variational Quantum Eigensolver (VQE)**: VQE is a hybrid quantum-classical algorithm used to find the ground state energy of a quantum system described by a Hamiltonian. It combines quantum circuits with classical optimization routines to approximate the ground state energy.
8. **Quantum Approximate Optimization Algorithm (QAOA)**: QAOA is another hybrid quantum-classical algorithm for solving combinatorial optimization problems. It constructs a variational ansatz and utilizes quantum circuits to approximate the solution to the optimization problem.
9. **Quantum Amplitude Estimation (QAE)**: QAE is a quantum algorithm estimates the probability of measuring a specific state in a quantum superposition. It has applications in machine learning, optimization, and finance.

## List of Algorithms

> 

| **Category** | **Algorithm** | **Purpose** | **Speedup / Type** |
| --- | --- | --- | --- |
| **Foundational** | Deutsch–Jozsa | Detect if a function is constant or balanced | Exponential (theoretical) |
|  | Bernstein–Vazirani | Find hidden binary string in a linear function | Exponential |
|  | Simon’s Algorithm | Find hidden period in a function | Exponential |
| **Number Theory / Cryptanalysis** | Shor’s Algorithm | Factor integers, compute discrete logarithms | Exponential |
|  | Quantum Phase Estimation (QPE) | Estimate eigenvalues of unitary operators | Core subroutine |
| **Search / Optimization** | Grover’s Algorithm | Search unstructured database | Quadratic |
|  | Amplitude Amplification | Boost probability of success for probabilistic algorithms | Quadratic |
|  | Quantum Walks | Solve graph and search problems | Problem-dependent |
|  | QAOA (Quantum Approximate Optimization Algorithm) | Approximate solutions to combinatorial optimization | Heuristic |
| **Simulation & Physics** | Trotter–Suzuki Decomposition | Simulate time evolution in quantum systems | Polynomial |
|  | VQE (Variational Quantum Eigensolver) | Estimate molecular ground states | Heuristic (NISQ-suitable) |
|  | QITE (Quantum Imaginary Time Evolution) | Ground state approximation | Heuristic |
| **Quantum Machine Learning** | QSVM (Quantum SVM) | Classification using quantum kernels | Heuristic |
|  | QPCA (Quantum PCA) | Principal component analysis | Requires density matrix input |
|  | Quantum k-Means | Clustering | Experimental |
|  | VQC (Variational Quantum Classifier) | Hybrid quantum-classical classification | Heuristic |
| **Linear Algebra & Data** | HHL Algorithm (Harrow-Hassidim-Lloyd) | Solve linear systems (Ax = b) | Exponential (under conditions) |
|  | QSVT (Quantum Singular Value Transformation) | Matrix functions, solving systems | General-purpose transformation |
| **Emerging / Hybrid** | Quantum Metropolis | Sample from thermal distributions | Quantum MCMC |
|  | Hamiltonian Learning | Learn quantum system models | Scientific modeling |

## Challenges

> Quantum computing holds transformative potential—but scaling it into something useful is **extremely difficult**.
> 

| **Category** | **Challenge** | **Details** |
| --- | --- | --- |
| **Physics** | Decoherence & Noise | Qubits lose coherence quickly due to interaction with environment. |
|  | High Error Rates | Gate and measurement operations are imprecise. |
| **Engineering** | Quantum Error Correction Overhead | Requires thousands of physical qubits for one logical qubit; needs constant error tracking. |
|  | Cryogenic Requirements | Most systems operate near absolute zero; cooling infrastructure is complex and expensive. |
|  | Control Signal Bandwidth | High-precision, low-latency control and readout per qubit becomes unmanageable at scale. |
|  | Qubit Fabrication & Yield | Difficult to manufacture large arrays of stable and identical qubits. |
| **System Architecture** | Limited Quantum Interconnects | Low-bandwidth, high-latency connections limit modular and distributed systems. |
|  | Lack of Modularity | Monolithic systems are hard to scale physically and logically. |
| **Algorithms & Software** | Limited Algorithms with Speedup | Only a few quantum algorithms (e.g. Shor's, Grover's) provide clear advantages. |
|  | Low-Level Programming Models | Quantum programming is still hardware-specific and lacks abstraction. |
|  | Poor Performance Prediction | It's hard to estimate how well a quantum algorithm will run on real hardware. |
| **Strategic / Economic** | High Cost & Energy Demand | Infrastructure, research, and operation costs are prohibitive. |
|  | Talent Shortage | Few engineers are trained in quantum physics *and* scalable systems engineering. |
|  | Unclear Use Cases | Lack of industry-wide killer applications limits demand and funding. |

## References

- https://en.wikipedia.org/wiki/Quantum_computing
- [https://archive.org/details/QuantumComputationAndQuantumInformation10thAnniversaryEdition](https://archive.org/details/QuantumComputationAndQuantumInformation10thAnniversaryEdition)
- [https://arxiv.org/abs/0708.0261](https://arxiv.org/abs/0708.0261)
- Quantum Computing Since Democritus  - [https://www.scottaaronson.com/democritus/](https://www.scottaaronson.com/democritus/)
- https://github.com/Qiskit/qiskit
    - [ ]  https://quantum.cloud.ibm.com/docs/en/guides/hello-world
    - [ ]  …
- https://ocw.mit.edu/courses/8-370x-quantum-information-science-i-spring-2018/
- [On The Power of Quantum Computation - Daniel R. Simon](https://courses.cs.washington.edu/courses/cse599/01wi/papers/simon_qc.pdf)
- [Models of quantum computation and quantum programming languages - Jaroslaw Adam MISZCZAK](https://arxiv.org/pdf/1012.6035.pdf)
- [What are the models of quantum computation?](https://quantumcomputing.stackexchange.com/questions/74/what-are-the-models-of-quantum-computation)
- [Introduction to Quantum Computing and Quantum Hardware](https://www.youtube.com/playlist?list=PLOFEBzvs-VvrXTMy5Y2IqmSaUjfnhvBHR)
- [Qubit](https://en.wikipedia.org/wiki/Qubit)
- [Quantum entanglement](https://en.wikipedia.org/wiki/Quantum_entanglement)
- Theory of Quantum Computing - David Shimkus
- [Quantum algorithm](https://en.wikipedia.org/wiki/Quantum_algorithm)
- [I'm Scott Aaronson, quantum computing/computational complexity researcher. AMA](https://news.ycombinator.com/item?id=17425377)
- [Epistemic Tool Template](https://app.notion.com/p/Epistemic-Tool-Template-2e5c0f5171ec800fa9caf91bb16bcab9?pvs=21)
- [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md)
- Quantum Computation and Quantum Information - Michael Nielsen, Isaac Chuang
- **Shor’s Algorithm -**
- Grover’s Algorithm
- Feynman, R. P. (1982). Simulating physics with computers. International Journal of Theoretical Physics, 21(6-7), 467–488. [https://doi.org/10.1007/BF02650179](https://doi.org/10.1007/BF02650179)
- Deutsch, D. (1985). Quantum theory, the Church-Turing principle and the universal quantum computer. Proceedings of the Royal Society of London. A. Mathematical and Physical Sciences, 400(1818), 97–117. [https://doi.org/10.1098/rspa.1985.0070](https://doi.org/10.1098/rspa.1985.0070)
- Shor, P. W. (1994). Algorithms for quantum computation: Discrete logarithms and factoring. Proceedings of the 35th Annual Symposium on Foundations of Computer Science, 124–134. [https://doi.org/10.1137/S0097539795293172](https://doi.org/10.1137/S0097539795293172)
- Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. Proceedings of the Twenty-Eighth Annual ACM Symposium on Theory of Computing, 212–219. [https://doi.org/10.1145/237814.237866](https://doi.org/10.1145/237814.237866)
- Bernstein, E., & Vazirani, U. (1997). Quantum complexity theory. SIAM Journal on Computing, 26(5), 1411–1473. [https://doi.org/10.1137/S0097539796300921](https://doi.org/10.1137/S0097539796300921)
- Nielsen, M. A., & Chuang, I. L. (2010). Quantum computation and quantum information (10th anniversary ed.). Cambridge University Press. [https://doi.org/10.1017/CBO9780511976667](https://doi.org/10.1017/CBO9780511976667)
Cited by: 67,105
- Kitaev, A. Y. (2003). Fault-tolerant quantum computation by anyons. Annals of Physics, 303(1), 2–30. [https://doi.org/10.1016/S0003-4916(02)00018-0](https://doi.org/10.1016/S0003-4916(02)00018-0)
- Arute, F., Arya, K., Babbush, R., Bacon, D., Bardin, J. C., Barends, R., ... & Martinis, J. M. (2019). Quantum supremacy using a programmable superconducting processor. Nature, 574(7779), 505–510. [https://doi.org/10.1038/s41586-019-1666-5](https://doi.org/10.1038/s41586-019-1666-5)
- Fowler, A. G., Mariantoni, M., Martinis, J. M., & Cleland, A. N. (2012). Surface codes: Towards practical large-scale quantum computation. Physical Review A, 86(3), 032324. [https://doi.org/10.1103/PhysRevA.86.032324](https://doi.org/10.1103/PhysRevA.86.032324)
- Preskill, J. (2018). Quantum computing in the NISQ era and beyond. Quantum, 2, 79. [https://doi.org/10.22331/q-2018-08-06-79](https://doi.org/10.22331/q-2018-08-06-79)