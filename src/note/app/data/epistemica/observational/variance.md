---
tags: [operator]
---

# Variance

 : Covariance (Covariance%201cfc0f5171ec80aead47fc52bbd5c430.md), Linear Discriminant Analysis (LDA) (Linear%20Discriminant%20Analysis%20(LDA)%20a12a15756fc246dfbaef71058ebab3a4.md), Random Object (Random%20Object%2024ec0f5171ec800b8c30edbce9c37968.md), Standard Deviation (Standard%20Deviation%20f38be66cd46745d0bca4e847bbfb62dd.md)

> In this note, we examine the **variance** statistic, which quantifies the **dispersion of a random variable around its mean by computing** the expected value of the squared deviation from the mean. This measure reflects how much the values of the variable tend to fluctuate, with higher variance indicating greater spread and lower variance implying tighter concentration around the mean.
> 

> Note: There are many formulations of the concept of variance, like **Sample Variance**.
> 

## Meta

> Evaluation Framework.
> 

> **The understanding of a concept is proportional** to the time invested in deep reflection, deliberate practice, and repeated engagement with its nuances. If a Concept has been learned soft of by osmosis - then is not well understood.
> 

### **✅** Evaluation

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

> See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21) & [](https://app.notion.com/p/250c0f5171ec8010a8d3caa5d0a1266e?pvs=21)
> 

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | … |
| **Completeness** | … |
| **Coherence & Structure** | … |
| **Epistemic Self-Assessment** | Need More Practice In - () and Analytical Examples. |
| **Should I Reorganize This -in My Content Forest?** |  |
| **What’s my study Strategy? Should I Change It?** |  |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | What is the deepest essence? |
| **Evidentia (Evidence) 📊** | What proofs, data, or logical arguments support it? How can its claims or performance be verified? |
| **Telos (Intent) 🎯** | What is it for? Toward what end is it directed? What tools does it offer, if any? What outcomes does it aim to achieve? |
| **Gnosis (Understanding) 🧠** | How to grow a **mental represented** (compress, fluid,  hierarchical (depth, abstraction), meta-awareness, flexibility, minimal sensitivity, well-connected) that capture this topic both its declarative aspects and procedural aspects?  How can we develop an **explicit representation & organization** of this topic that supports the growth of a strong **mental representation**? What **previous structure**  must be in place in order to make the growth of the new representation feasible? |
| **Epignosis (Application) 🛠️** | How is this knowledge applied in practice? What advanced skills or insights emerge from mastery? What real-world problems does it solve? |
| **Relatio (Connections) 🔗** | How does this topic relate to other subjects or fields? What are the interdisciplinary connections? |
| **Idoneitas (Suitability) 📐** | How effectively does it achieve its purpose? What metrics prove its value? |
| **Limites (Limits) ⛔** | What are its boundaries? What constraints define its operation? |
| **Contextus (Context) 🌍** | What is the historical, cultural, or situational context in which this study occurs? |
| **Dynamis (Evolution) 🌱** | How might it transform? What emerging influences could redefine it? |
| **Critica (Critique) 🔍** | What are the common criticisms or challenges associated with this topic? How have these been addressed or debated? |
| **Verbum Usus (Language Use) 🗣️** | How is the word/concept used in language and discourse? What are the typical semantic, pragmatic, and stylistic patterns surrounding its use? How do people’s usage contexts, connotations, and variations influence understanding? What shifts or trends in language use reflect its evolving meaning or social significance? |

### 🧠 Mental Representation

> How should we think about Variance?
> 

> See more in [How do different **mental representations** of the same RepTarget impact performance?](https://app.notion.com/p/How-do-different-mental-representations-of-the-same-RepTarget-impact-performance-24ac0f5171ec80dbaea5cc0e93f7647e?pvs=21).
> 

## Formulation

> Here’s the formal **mathematical formulation** of variance:
> 

For a **random variable** $X$: $\operatorname{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2]$

Where:

- $\mathbb{E}[X]$ is the expected value (mean) of $X$,
- The expression measures the expected squared deviation from the mean.

For a **sample** of values $x_1, x_2, \dots, x_n$, the **sample variance** is: $\operatorname{Var}(X) = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2$

Where:

- $\bar{x}$ is the sample mean,
- The denominator $n - 1$ ensures the estimate is unbiased.

## Property

> What are some fundamental truths about the variance functional?
> 

- **Non-Negativity: $\mathrm{Var}(X) \geq 0 \quad \text{(and it is 0 iff \(X\) is constant almost surely).}$**
- **Effect of Shifts (Translation Invariance) -** Adding a constant does not change the variance:  $\mathrm{Var}(X + c) = \mathrm{Var}(X)$
- **Effect of Scaling:**  Scaling multiplies variance by the square of the scale: - $\mathrm{Var}(aX) = a^2 \, \mathrm{Var}(X)$
- **Variance of Sum of Independent Variables:**  If $X$ and $Y$ are independent: $\mathrm{Var}(X+Y) = \mathrm{Var}(X) + \mathrm{Var}(Y)$
- **Variance of Sum:**  $\mathrm{Var}(X+Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) + 2\,\mathrm{Cov}(X,Y)$
- **Variance of Expected Value:**   Variance measures spread around the mean, so for a constant $c$:  $\mathrm{Var}(c) = 0$
- **Law of Total Variance (Variance Decomposition):**  For any random variable $Y$:  $\mathrm{Var}(X) = \mathbb{E}\!\big[\mathrm{Var}(X \mid Y)\big] + \mathrm{Var}\!\big(\mathbb{E}[X \mid Y]\big)$
- **Convexity (Popoviciu’s Inequality):  For a bounded random variable $X \in [a,b]$:    $\mathrm{Var}(X) \leq \frac{(b-a)^2}{4}$**
- **Variance of a Constant:** $\mathrm{Var}(c) = 0$

## ❓ QA

- How can we calculate the variance of an estimator?
- Suppose we have a set of observations $X_1, X_2, \dots, X_n$ from a random variable $X$ that follows a normal distribution. Why isn’t the variance of the sample mean the same as the variance of $X$?

## References

- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [Plato’s Dialectic Method](https://app.notion.com/p/Plato-s-Dialectic-Method-268c0f5171ec805cbb91d16158ae579e?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- [](https://app.notion.com/p/24ac0f5171ec8020aec7f11bae9eb632?pvs=21)
- [Prototype](https://www.notion.so/Prototype-1cec0f5171ec801e86e6c894702cfe23?pvs=21)
- [A Guide to Study](https://www.notion.so/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- https://en.wikipedia.org/wiki/Variance
- https://github.com/dbremont/algorithms/blob/main/om/prob/variance.ipynb
- [A Usage Guide to Human Languages & Communication](https://www.notion.so/A-Usage-Guide-to-Human-Languages-Communication-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- https://stats.stackexchange.com/questions/18058/how-would-you-explain-covariance-to-someone-who-understands-only-the-mean
- https://en.wikipedia.org/wiki/Pooled_variance
