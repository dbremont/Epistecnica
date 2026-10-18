# Solomonoff Induction


> **Solomonoff induction** is a **formal, theoretical framework for universal prediction** based on algorithmic probability.
> 

### **Core Idea**

- Suppose you want to predict the next symbol in a sequence (e.g., coin flips, sensor readings, text).
- Consider **all possible computable models** (programs) that could generate the observed data.
- Weight each model by its simplicity (shorter programs get exponentially higher weight — via **Kolmogorov complexity**).
- The prediction is a weighted average over all these models.
- It’s the **theoretically optimal** way to do inductive inference — but uncomputable in practice.

## References

- [Solomonoff's theory of inductive inference](https://en.wikipedia.org/wiki/Solomonoff%27s_theory_of_inductive_inference)
- [Solomonoff Induction](https://www.lesswrong.com/tag/solomonoff-induction)
- Hutter, Marcus. "Universal algorithmic intelligence: A mathematical top→ down approach." Artificial general intelligence. Berlin, Heidelberg: Springer Berlin Heidelberg, 2007. 227-290.
- [The Problem of Induction](https://app.notion.com/p/The-Problem-of-Induction-1fdc0f5171ec8031a27ef5c52d2c549e?pvs=21)
