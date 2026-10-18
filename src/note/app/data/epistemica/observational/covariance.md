---
tags: [statistic]
---

# Covariance

 : Variance (Variance%201cfc0f5171ec80f5a7f1c535bbde6e1c.md), Linear Discriminant Analysis (LDA) (Linear%20Discriminant%20Analysis%20(LDA)%20a12a15756fc246dfbaef71058ebab3a4.md), Pearson Correlation Coefficient (Pearson%20Correlation%20Coefficient%2020dc0f5171ec8057a1e1d8368df4fffe.md)

> In this note, we examine the **`covariance`**, a fundamental statistic that **captures the directional linear dependence** between **two random variables** by computing the expected product of their mean-centered deviations. A positive covariance indicates that the variables tend to increase together, while a negative value suggests that one tends to increase as the other decreases.
> 

> **Note:** The definition refers to **random variables**, but you can intuitively think of it in terms of datasets.
> 

> Notes intent.
> 

> **Short definition** of the topic.
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
| **Epistemic Self-Assessment** | … |
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

> How should we think about Covariance?
> 

> See more in [How do different **mental representations** of the same RepTarget impact performance?](https://app.notion.com/p/How-do-different-mental-representations-of-the-same-RepTarget-impact-performance-24ac0f5171ec80dbaea5cc0e93f7647e?pvs=21).
> 

## Formulation

> See some visualizations here https://github.com/dbremont/algorithms/blob/main/om/cov.ipynb for intuition.
> 

The mathematical formulation of **covariance** between two random variables $X$ and $Y$ is: $\operatorname{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])]$ $=$ $\mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$.

Where:

- $\mathbb{E}[X]$ and $\mathbb{E}[Y]$ are the expected values (means) of X and $Y$,
- The expression inside the expectation quantifies how $X$ and $Y$ deviate from their means *jointly*.

For a **sample** of paired observations $(x_1, y_1), \dots, (x_n, y_n)$, the **sample covariance** is:

$\operatorname{Cov}(X, Y) = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$

Where:

- $\bar{x}$ and $\bar{y}$ are the sample means of $X$and $Y$,
- The denominator $n - 1$ is used for an unbiased estimate.

## Property

> What fundamental truths does the covariance functional obey?
> 

> Note: Each of this bust be proof.
> 
- **Symmetry:  $\mathrm{Cov}(X,Y) = \mathrm{Cov}(Y,X)$.**
- Variance as a Special Case: $\mathrm{Cov}(X,X) = \mathrm{Var}(X)$$.$
- Bilinearity:  Covariance is linear in each argument:
    - $\mathrm{Cov}(aX + b, Y) = a \,\mathrm{Cov}(X,Y).$
    - $\mathrm{Cov}(aX + b, cY + d) = ac \,\mathrm{Cov}(X,Y).$
- Covariance of a Sum: $\mathrm{Cov}(X+Y, Z) = \mathrm{Cov}(X,Z) + \mathrm{Cov}(Y,Z)$.
- Effect of Independence: If $X$ and $Y$ are **independent**: $\mathrm{Cov}(X,Y) = 0.$; btw the converse is not truth.
- Bounds (Cauchy–Schwarz Inequality):  $|\mathrm{Cov}(X,Y)| \leq \sqrt{\mathrm{Var}(X)\mathrm{Var}(Y)}$.
- Invariance to Shifts:  $\mathrm{Cov}(X + c, Y + d) = \mathrm{Cov}(X,Y)$.
- Scaling Property:  $\mathrm{Cov}(aX, bY) = ab \,\mathrm{Cov}(X,Y)$.

## Case Study

> 

## ❓ QA

> 

## References

- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- 
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [Plato’s Dialectic Method](https://app.notion.com/p/Plato-s-Dialectic-Method-268c0f5171ec805cbb91d16158ae579e?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- [](https://app.notion.com/p/24ac0f5171ec8020aec7f11bae9eb632?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- https://en.wikipedia.org/wiki/Covariance
- [General Topic Note Template](https://app.notion.com/p/General-Topic-Note-Template-1cec0f5171ec801e86e6c894702cfe23?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- https://www.visiondummy.com/2014/04/draw-error-ellipse-representing-covariance-matrix/
- https://github.com/dbremont/algorithms/blob/main/om/cov.ipynb
