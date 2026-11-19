---
tags: [document, paper, algorithms, online-algorithms, competitive-analysis]
---

# The k-server conjecture is true (2026). *arXiv*:2609.15979. https://arxiv.org/abs/2609.15979

## Notes

> The **k-server problem** is the canonical problem of *online* algorithmics. A set of **k servers** sits on the points of a metric space; requests arrive one at a time at points of the space; to serve a request, some server must be moved there; the cost is the total distance travelled; and the algorithm must decide *before seeing the next request*. The quality measure is not the running time but the **competitive ratio** — the worst-case ratio of the online algorithm's cost to the cost of an offline algorithm that saw the whole sequence.

> The **k-server conjecture** (Manasse, McGeoch and Sleator, 1990) states that a *deterministic* online algorithm can achieve ratio **k** on **every** metric space. It has been open for three decades, and the best general bound has been worse than k — the work function algorithm is known to achieve at most $2k-1$ on any metric, and the conjecture says the truth is k.

**What the 2026 paper claims:**

| Element | Content |
| --- | --- |
| **Result** | The conjecture is true — the **work function algorithm** satisfies the ratio-k bound |
| **Method** | An **algebraic representation of the work function as a matrix**, encoding all feasible paths to a configuration; in that representation the min and addition of optimal costs become matrix operations |
| **Significance** | A thirty-year-old lower-bound-matching result, and a structural statement about the work function itself, not just a bound |

> Why it matters beyond the problem: **competitive analysis** is the theory of algorithms that must act without the future, and k-server is its cleanest case. A proof that the natural algorithm is optimal on every metric says the online/offline gap is exactly k — a statement about what determinism costs, independent of the space.

> The honest caveat: the result is a 2026 arXiv preprint, and a claim of this weight needs the usual scrutiny — but the statement is precise and the method (a matrix representation of the work function) is checkable, which is what makes it a corpus entry rather than a news item.

## References

- [The k-server conjecture is true — arXiv](https://arxiv.org/abs/2609.15979)
- [Algorithm](/view.html?p=notes/technica/computation/algorithm.md) — the catalogue this problem belongs to
- Manasse, M., McGeoch, L., & Sleator, D. (1990). Competitive algorithms for server problems. *Journal of Algorithms*, 11(2), 208–230.
