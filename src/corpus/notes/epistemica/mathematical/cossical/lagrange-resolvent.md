---
tags: [note, mathematics, algebraic, technique]
qa:
 - Why exactly does the cube root of unity collapse a six-element permutation orbit into two values — and is the count-three structure of the collapse special to the cubic, or general?
 - What precisely breaks at degree five — the resolvent construction, or the solvability of the resolvent it produces?
 - Is the triple the technique really reduces to — resolvent expression, permutation analysis, resolvent polynomial — clean, or do the middle two fuse in the operation?
---

# Lagrange's Resolvent: How He Used It and Why

> The important thing about Lagrange's work is that **he was not simply trying to find another formula for solving polynomial equations. He was trying to understand the mathematical mechanism that made existing solution formulas possible.**

His central question was:

> Why can certain polynomial equations be solved through radicals, and what mathematical properties make those solutions possible?

To investigate this, he studied how expressions constructed from polynomial roots behave when the roots are permuted.

This approach appeared in his 1770–1771 work, *Réflexions sur la résolution algébrique des équations*.

## 1. The problem Lagrange wanted to understand

Consider a polynomial equation:

\[
f(x)=x^3+px+q=0
\]

Suppose its three roots are:

\[
a,\quad b,\quad c
\]

By definition:

\[
f(x)=(x-a)(x-b)(x-c)
\]

The problem is to determine these roots using the coefficients \(p\) and \(q\).

Before Lagrange, mathematicians had developed formulas for solving quadratic, cubic and quartic equations.

But there was a deeper question: **Why do these solution procedures work, and can the same principles be extended to higher-degree equations?**

Lagrange approached this by examining the roots themselves.

## 2. Lagrange's actual technique: constructing combinations of roots

Let's use a cubic equation because it illustrates the technique particularly well.

Consider the depressed cubic:

\[
x^3+px+q=0
\]

Let its three roots be:

\[
a,\quad b,\quad c
\]

By Vieta's relations:

\[
a+b+c=0
\]

\[
ab+bc+ca=p
\]

\[
abc=-q
\]

Lagrange introduced combinations of these roots using the cube roots of unity.

Define:

\[
\omega=e^{2\pi i/3}
\]

where:

\[
\omega^3=1,\qquad 1+\omega+\omega^2=0
\]

Now construct two expressions:

\[
\boxed{u=a+\omega b+\omega^2c}
\]

\[
\boxed{v=a+\omega^2b+\omega c}
\]

These are examples of **Lagrange resolvents**.

Notice what happened: instead of working directly with the original roots, we constructed two new algebraic quantities from them.

Why these particular combinations?

Because the coefficients \(1,\omega,\omega^2\) interact in a particularly useful way with permutations of the three roots.

## 3. The key operation: permuting the roots

There are six possible permutations of three roots:

\[
(a,b,c)
\]

\[
(a,c,b)
\]

\[
(b,a,c)
\]

\[
(b,c,a)
\]

\[
(c,a,b)
\]

\[
(c,b,a)
\]

Now examine what happens to the resolvent:

\[
u=a+\omega b+\omega^2c
\]

Under these six permutations, its possible values are:

\[
u,\quad \omega u,\quad \omega^2u,
\quad v,\quad \omega v,\quad \omega^2v
\]

Therefore, the resolvent has six possible values under permutations.

But here is the important observation:

\[
(\omega u)^3=u^3
\]

\[
(\omega^2u)^3=u^3
\]

And similarly:

\[
(\omega v)^3=v^3
\]

Consequently, the six possible values collapse into just two distinct values after cubing:

\[
\boxed{u^3,\quad v^3}
\]

**This reduction in the number of distinct values is the central mathematical insight.**

## 4. Constructing the resolvent equation

We now have two quantities:

\[
U=u^3,\qquad V=v^3
\]

We want to construct an equation whose roots are precisely \(U\) and \(V\).

For this, we calculate their sum and product.

Using the relations between the original roots:

\[
uv=-3p
\]

Therefore:

\[
UV=u^3v^3=(uv)^3=-27p^3
\]

Similarly:

\[
u^3+v^3=-27q
\]

We can now construct a quadratic equation using the sum and product of its roots:

\[
t^2-(U+V)t+UV=0
\]

Substituting:

\[
\boxed{t^2+27qt-27p^3=0}
\]

This is the **resolvent equation** for the particular cubic construction.

Notice the transformation in mathematical complexity:

| Mathematical object | Degree | Description |
|---|---:|---|
| Original polynomial | 3 | Contains the unknown roots \(a,b,c\). |
| Resolvent expressions | — | Combinations of the original roots. |
| Permutation orbit of \(u\) | 6 | Six possible values under root permutations. |
| Cubed resolvent values | 2 | Only two distinct values remain. |
| Resolvent polynomial | 2 | Quadratic equation determining those two values. |

We have transformed the original root problem into an auxiliary quadratic problem.

## 5. Recovering the original roots

Once we solve:

\[
t^2+27qt-27p^3=0
\]

we obtain:

\[
U=u^3,\qquad V=v^3
\]

We can extract cube roots to obtain \(u\) and \(v\).

The original roots can then be recovered through:

\[
\boxed{a=\frac{u+v}{3}}
\]

\[
\boxed{b=\frac{\omega^2u+\omega v}{3}}
\]

\[
\boxed{c=\frac{\omega u+\omega^2v}{3}}
\]

The appropriate choices of cube roots must be coordinated so that:

\[
uv=-3p
\]

This is closely related to Cardano's solution of the cubic equation.

The important point is that the resolvent did not simply produce an alternative representation: it exposed an intermediate mathematical structure through which the original roots could be recovered.

## 6. Why did Lagrange develop this technique?

There were three major motivations.

### A. Understand why existing solution methods worked

Mathematicians had discovered methods for solving cubic and quartic equations, but these methods did not generalize successfully to equations of degree five and above.

Lagrange wanted to identify the common mathematical principles underlying the existing methods.

He examined the algebraic expressions used by earlier mathematicians and discovered that their methods could be understood through auxiliary equations whose roots were particular combinations of the original roots.

### B. Investigate the relationship between roots and permutations

Lagrange recognized that permutations were not merely different arrangements of roots.

They determined how algebraic expressions constructed from those roots changed.

By studying these changes, he could determine how many distinct values an expression could assume and construct equations satisfied by those values.

This was a major conceptual development: **the algebraic structure of an equation could be investigated through the permutation behavior of its roots.**

### C. Understand the limitations of solving higher-degree equations

Lagrange extended his reasoning beyond cubic equations.

For a polynomial of degree \(n\), he considered expressions of the general form:

\[
R=x_1+\alpha x_2+\alpha^2x_3+\cdots+
\alpha^{n-1}x_n
\]

where \(\alpha\) is an appropriate root of unity.

He investigated the different values these expressions could assume under permutations of the original roots.

However, for higher-degree equations, the resulting resolvent equations could become too complicated to solve by radicals.

His investigation therefore helped explain why the known methods worked for cubic and quartic equations but did not straightforwardly extend to the general quintic.

## 7. What mathematical technique did Lagrange actually use?

We can now classify his procedure more precisely.

| Attribute | Description |
|---|---|
| Technique | Lagrange resolvent construction |
| Technique family | Auxiliary algebraic construction |
| Mathematical domain | Polynomial algebra |
| Input | Polynomial roots |
| Operation | Weighted combination of roots |
| Secondary operation | Permutation analysis |
| Transformation | Construction of an auxiliary polynomial |
| Mathematical mechanism | Reduction in the number of distinct values under permutations |
| Output | Resolvent expressions and resolvent equation |
| Objective | Investigate the algebraic structure and solvability of polynomial equations |
| Historical origin | Joseph-Louis Lagrange, 1770–1771 |

## 8. The deeper historical significance

Lagrange's work became an important precursor to the development of group theory and Galois theory.

The progression was approximately:

- Polynomial equations
- ↓ Roots
- ↓ Root combinations
- ↓ Permutations
- ↓ Resolvent equations
- ↓ Algebraic solvability

Lagrange did not formulate modern group theory, but he established a crucial connection between permutations of roots and the algebraic solution of equations. Galois subsequently developed this connection into a much more powerful theory.

**The recommendation this exposition carries:** when documenting this technique, distinguish three things — the *resolvent expression* (the constructed combination of roots), the *permutation analysis* (the operation used to investigate it), and the *resolvent polynomial* (the resulting auxiliary equation). They are three distinct mathematical components of Lagrange's method.

## References

- [Lagrange, J.-L. (1770–1771). Réflexions sur la résolution algébrique des équations. In Œuvres de Lagrange, Vol. 3 (pp. 205–421). Gauthier-Villars, 1868 — original text at Wikisource](https://fr.wikisource.org/wiki/M%C3%A9moires_extraits_des_recueils_de_l%E2%80%99Acad%C3%A9mie_royale_de_Berlin/R%C3%A9flexions_sur_la_r%C3%A9solution_alg%C3%A9brique_des_%C3%A9quations)
- [History of Science and Mathematics SE — Where did Lagrange write his technique of resolvents for solving polynomials?](https://hsm.stackexchange.com/questions/15489/where-did-lagrange-write-his-technique-of-resolvents-for-solving-polynomials)
- [Mathematics SE — Clarifications regarding Lagrange resolvent](https://math.stackexchange.com/questions/1629629/clarifications-regarding-lagrange-resolvent)
- [Mathematics SE — Finding cube roots of unity: a proper explanation](https://math.stackexchange.com/questions/3835121/finding-cube-roots-of-a-unity-proper-explanation-is-needed)
- [Clark, A. — Elements of Abstract Algebra (secondary exposition; scanned copy)](https://poincare.matf.bg.ac.rs/~zarkom/Book_Math_Clark_Elements_of_abstract_algebra%202.pdf)
- [Lagrange, Joseph-Louis — the persona](/view.html?p=notes/social/collective/actor/private/persona/joseph-louis-lagrange.md)
- [Classical Algebra — the Ars Cossica technique path tree](/view.html?p=notes/epistemica/mathematical/cossical/classical-algebra.md)
- [Polynomial](/view.html?p=notes/epistemica/mathematical/cossical/polynomial.md)
- [Group Theory](/view.html?p=notes/epistemica/mathematical/structure/algebra/group-theory.md)
- [Philosophia Artium Epistemicarum et Operis](/view.html?p=notes/philosophia-artium-epistemicarum-et-operis.md)
