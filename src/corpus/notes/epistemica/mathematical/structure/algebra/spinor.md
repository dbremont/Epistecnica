---
tags: [note, mathematics, algebra, geometry]
qa:
 - Is a spinor a representation of a group or a module over an algebra — and does the choice change the object, or only the proof?
 - Does the double cover explain the 720°, or does it restate it in topological language?
 - Why does the spinor dimension grow as $2^{\lfloor n/2 \rfloor}$ while the vector space grows as $n$ — what is the extra structure buying?
 - Is spin a property of the particle or of the spacetime the particle lives in — Wigner's classification against the Dirac field?
 - Is the flagpole-and-flag picture a derivation of spinor behaviour, or a mnemonic that runs out of dimensions?
---

# Spinor

> A **spinor** is what the rotation group acts on when the action is allowed to be double-valued: the object that comes back to itself only after a full turn twice over. It is not a vector and not a tensor — it is the square root of geometry, the space from which vectors are built by symmetrization, and the reason an electron's state cannot be drawn as an arrow.

## 1. Definition

Two definitions, equivalent, answering different questions.

**Group-theoretic.** The orthogonal group $SO(n)$ has a connected double cover

\[
\rho:\ \mathrm{Spin}(n) \longrightarrow SO(n),
\qquad \ker \rho = \{\pm 1\},
\]

and a **spinor** is a vector in a representation of $\mathrm{Spin}(n)$ that does not come from a representation of $SO(n)$. Concretely: rotating the underlying space by $2\pi$ acts on a spinor as $-1$, and only $4\pi$ returns it to itself.

**Algebraic.** Given a vector space with an inner product, form the **Clifford algebra** $\mathrm{Cl}(V)$, the quotient of the tensor algebra by the relation

\[
v \otimes v = g(v,v)\cdot 1 ,
\]

so that $v w + w v = 2\,g(v,w)$. Then $V$ embeds in $\mathrm{Cl}(V)$, products of pairs of unit vectors generate $\mathrm{Spin}(n) \subset \mathrm{Cl}^0(V)$, and a **spinor** is a vector in an irreducible $\mathrm{Cl}(V)$-module — equivalently, a minimal left ideal. The two definitions meet because the Clifford action restricts to a representation of the spin group.

Three consequences follow immediately and are worth stating before anything else:

- **The dimension is $2^{\lfloor n/2 \rfloor}$ over $\mathbb{C}$** — exponential in the dimension, unlike the vector space's $n$. The spin representation is the smallest one the group has that is genuinely new, and it is large.
- **The object is not unique.** An irreducible spinor module depends on the group (the signature), on the field ($\mathbb{R}$, $\mathbb{C}$ or $\mathbb{H}$), and — in even dimensions — on chirality. "The spinors" is shorthand for a family, and the shorthand is where most confusion starts.
- **Nothing about it is a defect of notation.** The sign is not a bookkeeping convention that a cleaner formalism would remove; it is forced by the topology of the group, as §2 shows.

## 2. Why the double cover, and why twice around

$\pi_1(SO(n)) = \mathbb{Z}/2$ for every $n \ge 3$: the rotation group has exactly one non-trivial loop, the $2\pi$ rotation. Its universal cover is $\mathrm{Spin}(n)$, and the covering map has degree two. Two standard facts then give the spinor:

- **Projective representations lift.** A representation of a group that is only defined up to a phase — a *projective* representation — is a genuine representation of the universal cover (Wigner). Since quantum states are rays rather than vectors, phases are unobservable, so a projective representation of $SO(n)$ is a legitimate physical object; it is a true representation of $\mathrm{Spin}(n)$. Spinors exist because nature is allowed to represent rotations projectively.
- **The fundamental group is the sign.** The loop that goes once around in $SO(n)$ is non-trivial, so it lifts to a path in $\mathrm{Spin}(n)$ from $+1$ to $-1$; going twice is null-homotopic and returns to $+1$. The $720^\circ$ is the statement $\pi_1 = \mathbb{Z}/2$, written as a rotation.

The **belt (or plate) trick** — a hand-held object attached by strings that cannot be untwisted after one turn and can after two — is a demonstration of the same fact, not a proof of it.

The low case is the honest exception and the clearest illustration. For $n = 2$, $\mathrm{Spin}(2) = U(1)$ and $\rho$ is $z \mapsto z^2$; a spinor is a complex number acted on by $e^{i\theta/2}$, so a rotation by $\theta$ halves the angle. There the universal cover is $\mathbb{R}$, and $\mathrm{Spin}(2)$ is a double cover but not the universal one — $\pi_1(SO(2)) = \mathbb{Z}$, not $\mathbb{Z}/2$. The half-angle is the whole story in the plane; it is only a *sign* from three dimensions up, where the covering has degree two.

## 3. Three constructions

**Exterior algebra (Chevalley).** Choose a maximal isotropic subspace $W \subset V_{\mathbb{C}}$. Then $\mathrm{Cl}(V)$ acts on $\Lambda^\bullet W$: vectors in $W$ act as creation, vectors in the dual part as annihilation, and the Clifford relations are exactly the canonical anticommutation relations. The spin module is $\Lambda^\bullet W$, of dimension $2^{\dim W} = 2^{\lfloor n/2 \rfloor}$. This is the construction that makes the physics visible: **spinors are the Fock space of a fermionic oscillator**, and the reason they describe fermions is that the algebra acting on them is the algebra of anticommutation.

**Minimal left ideal.** In even dimensions the Clifford algebra splits $\mathrm{Cl}(V) \cong \mathrm{End}(\Delta)$ for the spin module $\Delta$; a spinor is a vector in a minimal left ideal, and the whole algebra is recovered as the algebra of operators on spinors. This is the algebraic form of "the spinor is the smallest thing the algebra can act on".

**Spinor bundle.** On a manifold, a spin structure is a principal $\mathrm{Spin}(n)$-bundle double-covering the frame bundle; the associated vector bundle is the spinor bundle, sections are spinor fields, and the Clifford action is fibrewise. Not every manifold admits one — the obstruction is the second Stiefel–Whitney class $w_2$, so orientability is not enough. This is the construction the Dirac operator and the index theorem live in.

## 4. Low dimensions, worked

| Dimension | Group | Spinors are | Notable reading |
| --- | --- | --- | --- |
| $n = 2$ | $\mathrm{Spin}(2) = U(1)$ | complex numbers, acted on by $e^{i\theta/2}$ | the half-angle made literal |
| $n = 3$ | $\mathrm{Spin}(3) = SU(2)$ = unit quaternions | two-component complex vectors | spin-$\tfrac12$; the Bloch sphere; a vector is a traceless Hermitian $2\times2$ matrix, i.e. a **symmetrized pair of spinors** |
| $n = 4$ | $\mathrm{Spin}(4) = SU(2)\times SU(2)$ | pairs of two-component spinors | chirality: the two factors are the left and right Weyl pieces |
| $3+1$ | $\mathrm{Spin}(3,1) = SL(2,\mathbb{C})$ | two-component **Weyl** spinors; the **Dirac** bispinor is a pair | the electron; see the trichotomy below |
| $n = 6$ | $\mathrm{Spin}(6) = SU(4)$ | four-component complex | the Euclidean face of six-dimensional geometry |

The relativistic trichotomy is the part worth naming precisely, because the three words are used interchangeably and are not:

- **Weyl spinors** are the two irreducible halves $(\tfrac12,0)$ and $(0,\tfrac12)$ of the Lorentz group; each is two-component; a massless fermion of definite chirality is one of them.
- **Dirac spinors** are the direct sum of the two halves — four components — and are what a massive electron is described by, because a mass term couples the halves.
- **Majorana spinors** are the real (self-conjugate) ones: a condition that halves the degrees of freedom. In four dimensions a spinor can be Weyl or Majorana but not both, which is why the "Majorana neutrino" question is a question about which condition nature imposes.

## 5. Real, complex, quaternionic

Over $\mathbb{C}$ the classification is simple: $\mathbb{C}\mathrm{l}(n+1) \cong \mathbb{C}\mathrm{l}(n) \otimes \mathbb{C}(2)$, so the complex story repeats with period two. Over $\mathbb{R}$ it is the famous period eight: the real Clifford algebras $\mathrm{Cl}(p,q)$ run through a cycle of eight, and the real spinor modules are real, complex or quaternionic according to the position in the cycle — the **Atiyah–Bott–Shapiro** classification, which is also the statement that the Clifford algebras generate the periodicity of real $K$-theory.

The practical content: "a spinor" is meaningless without the field and the signature. The same word names an $\mathbb{R}^2$, a $\mathbb{C}^2$ and an $\mathbb{H}$-line in different dimensions, and statements transferred between them without checking the cycle are simply wrong.

## 6. Why they matter

**Vectors are symmetrized spinors.** In three dimensions the map from a spinor to its expectation value $\langle \psi | \sigma | \psi \rangle$ lands in the vector space, and the symmetric square of the spin-$\tfrac12$ representation is the vector representation. In four dimensions the same statement holds in the form "a four-vector is a $2\times2$ Hermitian matrix", the correspondence that makes the Lorentz group act on spinors first and on vectors by composition. This is what "square root of geometry" means.

**Fermions.** The Clifford algebra is the algebra of canonical anticommutation relations, and the spin module is its Fock space (§3). The spin–statistics theorem turns the half-integer spin into the antisymmetric exchange sign, so the reason matter is fermionic and the reason spinors exist are the same fact seen twice.

**The Dirac equation.** The relativistic wave equation for the electron is a first-order equation on a spinor field, and its solutions carry spin-$\tfrac12$ automatically — spin is not added to the theory, it is what the representation provides. The prediction of antimatter comes from the same structure.

**Wigner's classification.** The unitary irreducible representations of the Poincaré group are labelled by mass and spin; the spin label is the spinor representation appearing as the little group's representation. Here the disagreement with the Dirac reading is instructive — the note's fourth question — because Wigner classifies *states* of a particle while the Dirac field is an *operator-valued* object on spacetime, and the two are related by quantization rather than being the same construction.

**Spin geometry.** On a curved manifold the Dirac operator couples the spinor bundle to the Levi-Civita connection; its index is topological (Atiyah–Singer), and Witten's proof of the positive mass theorem is the most quoted case of a geometric statement proved by a spinor identity.

**Twistors and qubits.** The twistor correspondence rests on $SU(2,2) = \mathrm{Spin}(4,2)$, the conformal group of Minkowski space, acting on spinors as the primary object and on spacetime points as secondary ones. And a spin qubit is a spinor: a two-component state whose $2\pi$ sign is unobservable but whose interference effects are not.

## 7. What a spinor is not

- **Not a tensor.** Every tensor representation of $SO(n)$ is single-valued, so no tensor can be a spinor. This is not a technicality but the definition: the spin representation exists precisely because it does not descend to $SO(n)$.
- **Not a spatial vector.** The association of a spinor with a direction is through the expectation value, and that map loses the phase and the sign.
- **Not "the electron's little arrow".** The arrow picture is the expectation value; the spinor is what the arrow is computed from, and two spinors differing by a sign give the same arrow.
- **Not captured by flagpole and flag.** The flagpole is the direction, the flag the phase; the picture illustrates the double cover in three dimensions and does not generalise into a construction of spinors in higher ones.
- **Not one object.** Group, field and signature each select one. A statement about "spinors" that does not say which is a statement about none.

## References

- [Spinor — Wikipedia](https://en.wikipedia.org/wiki/Spinor)
- Cartan, É. (1913/1966). *The Theory of Spinors*. MIT Press. — the original construction
- Chevalley, C. (1954). *The Algebraic Theory of Spinors*. Columbia University Press. — the exterior-algebra construction
- Lawson, H. B. & Michelsohn, M.-L. (1989). *Spin Geometry*. Princeton University Press. — spin structures, Dirac operator, index theory
- Deligne, P. (1999). Notes on spinors. In *Quantum Fields and Strings: A Course for Mathematicians*, vol. 1. AMS. — the real/complex/quaternionic classification
- Atiyah, M. F., Bott, R. & Shapiro, A. (1964). Clifford modules. *Topology* 3 (suppl. 1), 3–38. — periodicity mod eight
- Penrose, R. & Rindler, W. (1984). *Spinors and Space-Time*, vol. 1. Cambridge University Press. — the two-component calculus, flagpole and flag
- Misner, C. W., Thorne, K. S. & Wheeler, J. A. (1973). *Gravitation*, §41. Freeman. — spinors as the square root of geometry
- Wigner, E. (1939). On unitary representations of the inhomogeneous Lorentz group. *Annals of Mathematics* 40, 149–204. — mass and spin as the classification labels
- [Clifford Algebra](/view.html?p=notes/epistemica/mathematical/structure/algebra/clifford-algebra.md) — the algebra the spin module is a module over
- [Rotation](/view.html?p=notes/epistemica/mathematical/geometry/rotation.md) — the group being covered
- [Quaternion](/view.html?p=notes/epistemica/mathematical/complex/quaternion.md) — $\mathrm{Spin}(3)$ in coordinates
- [Representation Theory](/view.html?p=notes/epistemica/mathematical/structure/algebra/representation-theory.md) — why projective representations lift
- [Orthogonal Group](/view.html?p=notes/epistemica/mathematical/structure/algebra/orthogonal-group.md) — $\pi_1$ and the covering
- [Minkowski Space](/view.html?p=notes/epistemica/mathematical/space/minkowski-space.md) — the signature that produces Weyl, Dirac and Majorana
- [Tensor](/view.html?p=notes/epistemica/mathematical/tensor/tensor.md) — the class of objects a spinor is not in
- [Spin](/view.html?p=notes/nature/spin.md) and [Spin Angular Momentum](/view.html?p=notes/nature/spin-angular-momentum.md) — the physical reading of the same object
- [Dirac Equation](/view.html?p=notes/nature/dirac-equation-relativistic.md) and [Dirac Field](/view.html?p=notes/nature/dirac-field.md) — where the spinor becomes a field
