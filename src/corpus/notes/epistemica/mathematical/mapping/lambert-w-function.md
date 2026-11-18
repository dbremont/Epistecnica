---
tags: [note, mathematics, function, special-function, lambert-w]
qa:
 - Is the Lambert W a function or a representation?
 - Why does inverting x·e^x need two branches where inverting e^x needs one?
 - What does W extract that the logarithm does not?
---

# Lambert W Function

> The **Lambert W function** is the inverse of the map $x \mapsto x e^x$: $W(z)$ is the number $w$ such that $w e^{w} = z$. It is the function that turns an implicit transcendental condition — a variable both multiplying and inside an exponential — into an explicit one.

> Because $x e^x$ is not injective on the reals, the inverse is multivalued: the **principal branch** $W_0$ covers $x \ge -1$ and the **lower branch** $W_{-1}$ covers $x \le -1$, meeting at the minimum $W(-1/e) = -1$. On the complex plane the function has infinitely many branches; the two real ones are the ones that matter in applications.

## The representation

> The definition is an operator statement: $W$ is the **inverse of the product map** $x \mapsto x e^x$. It belongs to the same representational family as the logarithm — $\ln$ inverts $e^x$, $W$ inverts $x e^x$ — and the difference between them is the whole point. The exponential can be inverted by taking a logarithm because the unknown appears once, as an exponent. The product puts the unknown in two places at once, and the inverse must therefore solve an equation of its own kind rather than isolate an exponent.

> Read that way, $W$ is not merely a new special function but a **representational move**: when a problem arrives as "$x$ times $e^x$ equals something", the problem is implicit in $x$; applying $W$ extracts the value. That is the sense in which the function "extracts information from the input" — the input carries the answer in a form the notation does not expose, and $W$ is the operator that exposes it.

## Definition and branches

| Item | Expression |
| --- | --- |
| **Defining relation** | $W(z)\,e^{W(z)} = z$ |
| **Principal branch** | $W_0(x)$ for $x \ge -1/e$ |
| **Lower branch** | $W_{-1}(x)$ for $-1/e \le x < 0$ |
| **Branch point** | $W_0(-1/e) = W_{-1}(-1/e) = -1$ |
| **At the origin** | $W_0(0) = 0$ |
| **Omega constant** | $W_0(1) = \Omega \approx 0.567143$ |
| **Derivative** | $W'(z) = \dfrac{W(z)}{z\,(1 + W(z))}$ for $z \ne -1/e$ |
| **Series** | $W_0(x) = \displaystyle\sum_{n\ge 1} \frac{(-n)^{n-1}}{n!} x^n$, $|x| \le 1/e$ |
| **Large argument** | $W_0(x) \sim \ln x - \ln\ln x + \dfrac{\ln\ln x}{\ln x} + \cdots$ |

> The series is the **tree function**'s: $T(x) = -W_0(-x)$ counts rooted trees, and the Cayley formula falls out of it. That is not a coincidence — $T = x e^{T}$ is the same fixed-point equation that defines $W$, which is why the function keeps appearing wherever recursive structures are counted.

## What it solves

| Equation | Solution |
| --- | --- |
| $w e^{w} = z$ | $w = W(z)$ |
| $x^x = y$ | $x = \dfrac{\ln y}{W(\ln y)}$ |
| $a^x = b x$ | $x = -\dfrac{W\!\left(-\ln a / b\right)}{\ln a}$ |
| $x + \ln x = c$ | $x = W(e^{c})$ |
| $x e^{x} = a$ with $a<0$ | the two real solutions use $W_0$ and $W_{-1}$ |
| Infinite power tower $x^{x^{x^\cdots}} = y$ | $x = y^{1/y}$, when the tower converges |

> The last row is the function's most vivid use: the tower converges to a fixed point of $y \mapsto x^y$, and the inverse question — which base produces a given height — is a Lambert W evaluation.

## Where it appears

| Field | The equation | Why $W$ |
| --- | --- | --- |
| **Delay differential equations** | $y'(t) = a\,y(t-1)$ | The characteristic equation is $\lambda = a e^{-\lambda}$, i.e. a Lambert W equation |
| **Combinatorics** | $T = x e^{T}$ | Rooted-tree enumeration, the tree function |
| **Epidemiology** | $1 - x = e^{-R_0 x}$ | The final-size equation of an SIR epidemic; the root is a Lambert W value |
| **Queueing and reliability** | implicit service or failure equations | Any model where the unknown appears in a rate and in an exponent |
| **Physics** | Wien-type and threshold equations | Transcendental equations with the unknown in a product |
| **Iterated exponentiation** | $x^x$, towers, tetration inverses | The inverse of the product is the inverse of the tower's step |

## Properties worth keeping

> The function is real-analytic on each branch away from the branch point, satisfies the recurrence-type identity $W(z e^z) = z$ on the appropriate branch, and has a continued-fraction and Newton iteration for evaluation. The numerical evaluation is the practical face of the operator: a few Newton steps from a logarithmic initial guess converge quickly, which is why the function is available in numerical libraries even where it is not in the elementary calculus.

## References

- Lambert, J. H. (1758). *Observationes variae in mathesin puram*. — the first appearance of the equation $x = x^a + \cdots$ that leads to the function
- Euler, L. (1783). De serie Lambertina plurimisque eius insignibus proprietatibus. *Acta Academiae Scientiarum Petropolitanae*. — the series and the name
- Corless, R. M., Gonnet, G. H., Hare, D. E. G., Jeffrey, D. J., & Knuth, D. E. (1996). On the Lambert W function. *Advances in Computational Mathematics*, 5, 329–359. — the modern definition, branches and applications
- [Lambert W function](https://en.wikipedia.org/wiki/Lambert_W_function)
- [Logarithm](/view.html?p=notes/epistemica/mathematical/number/logarithm.md) — the inverse of $e^x$, the sibling move
- [Gamma Function](/view.html?p=notes/epistemica/mathematical/mapping/gamma-function.md) · [Bessel Function](/view.html?p=notes/epistemica/mathematical/mapping/bessel-function.md) — the special functions this one sits beside
- [Operator](/view.html?p=notes/epistemica/mathematical/mapping/operator.md) — the operator reading of the inverse
- [Representation](/view.html?p=notes/epistemica/mathematical/method/representation.md) — the representation table this function belongs to
- [Gamma Function](/view.html?p=notes/epistemica/mathematical/mapping/gamma-function.md) — the other interpolating special function
