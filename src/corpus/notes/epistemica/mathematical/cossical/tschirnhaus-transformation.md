---
tags: [note, mathematics, algebraic, technique]
qa:
 - Is the claim "it removes all intermediate terms" false in general, or only its unrestricted form — and which premise exactly fails at degree five?
 - The substitution carries \(n\) coefficients but only \(n-1\) are effective: what does the remaining degree of freedom fix, and can it ever be spent on a coefficient?
 - Does the field-theoretic reading — a change of primitive element — exhaust the historical substitution, or is the substitution one realizable case of it?
---

# Tschirnhaus Transformation

> A change of variable chosen so that the obstruction disappears: the equation is not solved, it is re-posed in the form the existing methods presuppose.

> A **Tschirnhaus transformation** replaces the unknown of a polynomial equation by a polynomial — or rational — function of a new indeterminate, with coefficients chosen so that some or all of the intermediate terms of the transformed equation vanish.

It was published by [Ehrenfried Walther von Tschirnhaus](/view.html?p=notes/social/actor/private/persona/ehrenfried-walther-von-tschirnhaus.md) in the *Acta Eruditorum* of May 1683, pages 204–207, as *Methodus auferendi omnes terminos intermedios ex data aequatione* — a method for removing all intermediate terms from a given equation.

## 1. The problem it attacks

The sixteenth-century solution formulas do not answer the general equation. Cardano's formula answers the *depressed* cubic \(y^3+py+q=0\); Ferrari's answers a quartic already stripped of its cubic term. Both presuppose a normalization step, performed first, that the formula does not contain.

For the general monic equation of degree \(n\),

\[
f(x)=x^{n}+a_{1}x^{n-1}+a_{2}x^{n-2}+\cdots+a_{n-1}x+a_{n}=0,
\]

the coefficients are the elementary symmetric functions of the roots \(r_{1},\dots,r_{n}\):

\[
a_{1}=-(r_{1}+\cdots+r_{n}),\qquad
a_{2}=\sum_{i<j}r_{i}r_{j},\qquad \dots,\qquad
a_{n}=(-1)^{n}r_{1}r_{2}\cdots r_{n}.
\]

Each nonzero coefficient is therefore a constraint the roots must satisfy. Removing one is discharging one constraint. Tschirnhaus's question was how many constraints a single change of variable can discharge at once — and whether all of them can be discharged, leaving a binomial.

## 2. One coefficient, one parameter: the shift

Begin with the linear substitution \(x=y+\alpha\). Expanding,

\[
f(y+\alpha)=(y+\alpha)^{n}+a_{1}(y+\alpha)^{n-1}+\cdots+a_{n},
\]

the coefficient of \(y^{n-1}\) collects exactly two contributions, \(n\alpha\) from the leading power and \(a_{1}\) from the next:

\[
n\alpha+a_{1}=0
\qquad\Longrightarrow\qquad
\alpha=-\frac{a_{1}}{n}.
\]

The term of degree \(n-1\) is gone. The resulting equation is the **depressed** form, and the case \(n=2\) is completing the square. This step costs one linear equation in one unknown, and it is available at every degree — which is why it is invisible as a *method* and indispensable as a *step*.

Tschirnhaus worked it on the general cubic \(f(x)=x^{3}-px^{2}+qx-r\). With \(\alpha=p/3\),

\[
f\!\left(y+\frac{p}{3}\right)
=
y^{3}+\left(q-\frac{p^{2}}{3}\right)y
+\left(\frac{pq}{3}-\frac{2p^{3}}{27}-r\right),
\]

the form into which Cardano's formula substitutes \(y=u+v\). The transformation has done its whole work before any root is found.

| Step | Equation | Intermediate terms |
|---|---|---|
| General cubic | \(x^{3}-px^{2}+qx-r=0\) | quadratic and linear |
| After \(x=y+p/3\) | \(y^{3}+Py+Q=0\) | linear only |
| Cardano | \(y=u+v\), \(uv=-P/3\) | — |

## 3. Several coefficients, several parameters: the general substitution

To remove more than one term, allow a richer reparametrization:

\[
y=k_{1}x^{n-1}+k_{2}x^{n-2}+\cdots+k_{n-1}x+k_{n},
\]

or the rational form \(x=\dfrac{b_{0}+b_{1}y+\cdots+b_{n-1}y^{n-1}}{c_{0}+c_{1}y+\cdots+c_{n-1}y^{n-1}}\) that Tschirnhaus himself moved to. Under the polynomial form, \(y\) takes the values \(\phi(r_{1}),\dots,\phi(r_{n})\) on the roots, so the transformed equation is

\[
f'(t)=\prod_{i=1}^{n}\left(t-\phi(r_{i})\right)=0,
\]

whose coefficients are symmetric functions of the transformed values. Annihilating the first \(k\) coefficients imposes \(k\) conditions on the coefficients \(k_{1},\dots,k_{n}\) of the substitution. With \(k=n-1\) conditions the target is a binomial \(y^{n}+c=0\).

The counting needs one correction, and it is the reason the substitution has \(n\) coefficients but \(n-1\) effective ones: multiplying every \(k_{i}\) by the same constant rescales \(y\), which rescales the roots of \(f'\) without changing which coefficients vanish. The scale is a free parameter of the *representation*, not of the *conditions*, so it can never be spent on a coefficient. Removing all \(n-1\) intermediate terms therefore uses all \(n-1\) effective parameters, leaving none.

Tschirnhaus's own second step was \(x^{2}=bx+y+a\) — a quadratic substitution used to kill two coefficients at once. That is the moment the operation stops being a shift and becomes a genuine change of variable: \(x\) and \(y\) no longer generate the same *polynomial expression*, only the same *field* (see § 5).

## 4. Where the method stops

The conditions are not linear in the parameters once \(k\ge 2\), and solving them is an elimination problem: the coefficients of the substitution are themselves the roots of an auxiliary equation. The transformation is free only in the linear case; beyond it, it trades the original equation for an auxiliary one, and the trade is worth making only while the auxiliary stays solvable.

- **Quartic.** Two coefficients (the cubic and the quadratic) can be removed; the auxiliary stays within reach.
- **Quintic, partially.** The general binomial reduction is impossible — that would be a solution by radicals, which Abel (1824) and Ruffini forbade. Bring (1786) reduced the general quintic to the trinomial \(y^{5}+py+q=0\); Jerrard (1834) extended the three-coefficient reduction to every degree \(>3\). Producing that reduction for a general quintic already requires solving an auxiliary quartic ([Adamchik & Jeffrey 2003](https://doi.org/10.1145/990353.990371)) — solvable, and that is the whole reason the Bring–Jerrard form exists.
- **Quintic, in general.** The binomial target fails, and not because the algebra was done badly: no reparametrization of a generic quintic by a function of one indeterminate can place it inside a radical tower that the extension does not already admit.

Tschirnhaus's paper claimed the general result — a method giving the roots of an equation of any degree. The claim is false, and its refutation is not a detail of the construction: it is the same obstruction that [Abel and Galois](https://en.wikipedia.org/wiki/Abel%E2%80%93Ruffini_theorem) identified, reached from the other side.

## 5. The modern reading: a change of primitive element

Let \(K\) be a field, \(P\) an irreducible polynomial over \(K\), \(\alpha\) a root, and \(L=K(\alpha)\cong K[t]/(P)\). Any other primitive element of \(L\) has the form \(\beta=F(\alpha)\) for some polynomial \(F\) over \(K\), with \(\alpha=G(\beta)\) for a polynomial \(G\). The minimal polynomial \(Q\) of \(\beta\) over \(K\) is then a Tschirnhaus transformation of \(P\) — and, conversely, every Tschirnhaus transformation arises this way. So the classical operation of substituting and expanding is one way of computing an operation on fields.

Two consequences follow directly.

- The set of Tschirnhaus transformations of \(P\) is the set of ways of changing \(P\) while leaving \(L\) fixed. When \(L/K\) is Galois, the Galois group *is* the set of Tschirnhaus transformations of \(P\) to itself.
- The normal forms of classical algebra are choices of primitive element. Bring–Jerrard is the statement that a quintic's splitting field has a generator whose minimal polynomial has three fewer terms.

The same reading powers computation: testing which Tschirnhaus images of \(\alpha\) satisfy an equation of low degree is how resolvents — and, through them, Galois groups — are actually determined.

## 6. Relation to the resolvent

The two auxiliary constructions of classical algebra are often confused. They transform different objects and produce different things.

| Construction | What is re-parameterized | What is produced | Where it stops |
|---|---|---|---|
| Tschirnhaus transformation | the unknown, \(x\mapsto\varphi(y)\) | a new equation for the *same* extension, with chosen coefficients zero | when the auxiliary equation for the parameters becomes unsolvable |
| [Lagrange's resolvent](/view.html?p=notes/epistemica/mathematical/cossical/lagrange-resolvent.md) | the roots, as a weighted combination | an auxiliary equation for the combination, of *lower* degree | when the resolvent itself cannot be solved |

Tschirnhaus re-poses the equation; Lagrange reduces the problem. Both are attempts to arrive at a form within reach, and both stall at the quintic — Tschirnhaus because the transformation cannot be computed, Lagrange because the resolvent cannot be solved. That these are two faces of one obstruction is Galois's result, not either author's.

## 7. What the transformation is

| Attribute | Description |
|---|---|
| Technique | Tschirnhaus transformation |
| Technique family | Polynomial transformation — change of variable |
| Mathematical domain | Polynomial algebra; field theory |
| Input | a monic equation of degree \(n\), and a chosen set of intermediate coefficients to annihilate |
| Operation | substitution \(x=\varphi(y)\) with \(\varphi\) polynomial or rational of degree \(\le n-1\) |
| Secondary operation | elimination of the coefficients of \(\varphi\) from the vanishing conditions |
| Output | a transformed equation with the chosen coefficients zero, together with the map back to the original roots |
| Mathematical mechanism | re-parametrization of the same field extension — a new primitive element |
| Objective | reach a form that the existing solution methods presuppose |
| Historical origin | E. W. von Tschirnhaus, *Acta Eruditorum*, May 1683 |

## 8. The three things to keep apart

Three components are routinely collapsed into one name, and the collapse is what produces the false general claim.

1. **The substitution** — \(x=\varphi(y)\), a change of variable on the equation.
2. **The coefficient conditions** — the equations that make selected terms vanish.
3. **The auxiliary system** — the problem of solving those equations for the coefficients of \(\varphi\).

The substitution is always available. The conditions are always writable. Only the auxiliary system can fail, and whether it is solvable is a fact about the extension, not about the technique. A statement of the form "the Tschirnhaus transformation removes all intermediate terms" asserts that the third step always succeeds — true for the shift, true for the quartic and for the Bring–Jerrard form, false for the binomial target at degree five and beyond.

## References

- [Tschirnhaus transformation — Wikipedia](https://en.wikipedia.org/wiki/Tschirnhaus_transformation)
- [Tschirnhaus, E. W. von (1683). Methodus auferendi omnes terminos intermedios ex data aequatione. *Acta Eruditorum*, 204–207 — English translation by R. F. Green, *ACM SIGSAM Bulletin* 37(1), 2003](https://doi.org/10.1145/844076.844078)
- [Garver, R. (1927). The Tschirnhaus Transformation. *Annals of Mathematics* 29, 319–333](https://www.jstor.org/stable/1968002)
- [Adamchik, V. S. & Jeffrey, D. J. (2003). Polynomial transformations of Tschirnhaus, Bring and Jerrard. *ACM SIGSAM Bulletin* 37(3), 90–94](https://doi.org/10.1145/990353.990371) — [author's copy](https://www.uwo.ca/apmaths/faculty/jeffrey/pdfs/Adamchik.pdf)
- [Bring–Jerrard normal form — Wikipedia](https://en.wikipedia.org/wiki/Bring_radical)
- [Weisstein, E. W. — Tschirnhausen Transformation, MathWorld](https://mathworld.wolfram.com/TschirnhausenTransformation.html)
- [Tschirnhaus, Ehrenfried Walther von — the persona](/view.html?p=notes/social/actor/private/persona/ehrenfried-walther-von-tschirnhaus.md)
- [Tschirnhaus, E. W. von (1695). *Medicina mentis* — the digitised copy](https://archive.org/details/medicinamentissi00tsch)
- [Polynomial — the transformation family, and its § Tschirnhaus Transformation](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md)
- [Classical Algebra — the Ars Cossica technique path tree](/view.html?p=notes/epistemica/mathematical/cossical/classical-algebra.md)
- [Lagrange's Resolvent — the other auxiliary construction](/view.html?p=notes/epistemica/mathematical/cossical/lagrange-resolvent.md)
- [Group Theory](/view.html?p=notes/epistemica/mathematical/structure/algebra/group-theory.md)
- [Philosophia Artium Epistemicarum et Operis](/view.html?p=notes/philosophia-artium-epistemicarum-et-operis.md)
