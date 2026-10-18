---
tags: [operator, probability]
---

# Expected Value

 : Kelly Criterion (Kelly%20Criterion%2017fc0f5171ec80fd99edfc2c271b3862.md), Martingale (Martingale%207b5a50c6c4c042b99e85cc9a1c5d643c.md), Random Object (Random%20Object%2024ec0f5171ec800b8c30edbce9c37968.md), Fisher Information (Fisher%20Information%204cefa509a9c94f7b912cfbdc477adbec.md)

> The expected value of a random variable $X$ is the long-run average or mean value that $X$ takes, weighted by its probabilities.
> 

> Note: To develop intuition, take a set of numbers, assign a probability to each number (ensuring that the probabilities sum to 1), and then compute the expected value.
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

> How should we think about Expected Value?
> 

> See more in [How do different **mental representations** of the same RepTarget impact performance?](https://app.notion.com/p/How-do-different-mental-representations-of-the-same-RepTarget-impact-performance-24ac0f5171ec80dbaea5cc0e93f7647e?pvs=21).
> 

## Formulation

Let $(\Omega, \mathcal{F}, P)$ be a probability space, where:

- $\Omega$ is the sample space,
- $\mathcal{F}$ is a σ-algebra (set of possible events),
- $P$ is a probability measure.

Given a **random variable** $X: \Omega \to \mathbb{R},$ the **expected value** $\mathbb{E}[X]$ is defined as:

- **Discrete Case:** If  $X$ takes values in a countable set $\{x_1, x_2, \dots\}$, then:  $\mathbb{E}[X] = \sum_{i} x_i \cdot P(X = x_i)$, provided the sum converges absolutely (i.e., $\sum_{i} |x_i| P(X = x_i) < \infty$).
- **Continuous Case:** If   $X$ has a probability density function (PDF)  $f_X(x)$, then:  $\mathbb{E}[X] = \int_{-\infty}^{\infty} x f_X(x) \, dx$,  provided the integral converges absolutely (i.e.,$\int_{-\infty}^{\infty} |x| f_X(x) \, dx < \infty$).
- **General Measure-Theoretic Definition:** For any random variable $X$, the expected value is the **Lebesgue integral**:  $\mathbb{E}[X] = \int_{\Omega} X(\omega) \, dP(\omega)$, which unifies both discrete and continuous cases (and more general distributions).

## **Properties**

> **Note:** These properties can be very subtle. $X$ and $Y$ must be functions defined on the same sample space $\Omega$; that is, $X: \Omega \to \mathbb{R}$ and $Y: \Omega \to \mathbb{R}$. Each random variable is evaluated at an outcome $\omega \in \Omega$ as $X(\omega)$ or $Y(\omega)$. Because they share the same underlying $\Omega$, they also share the same probability distribution over the outcomes.
> 
1. **Bounds**: For a real-valued random variable $X$ with finite minimum and maximum, $\min(X) \le \mathbb{E}[X] \le \max(X)$ i.e., the expectation lies between the smallest and largest possible values of $X$,  this is trivial for the unbounded cased.
2. **Non-Negativity: …**
3. **Linearity**: $\mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y], \quad \text{for constants } a, b$.
4. **Monotonicity**: If $X \leq Y$ almost surely, then $\mathbb{E}[X] \leq \mathbb{E}[Y]$.
5. **Expectation of a Constant**:  $\mathbb{E}[c] = c$.
6. **Jensen’s Inequality**: If  $\phi$ is convex, then:   $\phi(\mathbb{E}[X]) \leq \mathbb{E}[\phi(X)]$.
7. **Law of the Unconscious Statistician (LOTUS)**: For a measurable function  $g$,  $\mathbb{E}[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) \, dx \quad \text{(continuous case)}$.
8. Independence Property: If 
9. Fatou’s Lemma (Inequality version)
10. **Translation Invariance**
11. Monotone Convergence

## **Interpretation**

- **Frequentist**: If an experiment is repeated infinitely,  $\mathbb{E}[X]$ is the long-run average of the outcomes.
- **Bayesian**: Represents a "central tendency" of the distribution of $X$.
- **Decision Theory**: The best predictor minimizing mean squared error (i.e., $\mathbb{E}[(X - c)^2]$ is minimized when $c = \mathbb{E}[X]$.
- Center of Mass:  Analogous to the **center of mass**, where $\mathbb{E}[X]$ represents the “balance point” of the probability distribution.

## **Conditional Expectation**

The **conditional expected value** $\mathbb{E}[X \mid \mathcal{G}]$, where  $\mathcal{G} \subseteq \mathcal{F}$ is a sub-σ-algebra, is a random variable that generalizes expectation to partial information. It satisfies: $\int_G \mathbb{E}[X \mid \mathcal{G}] \, dP = \int_G X \, dP \quad \forall G \in \mathcal{G}$.

## Low of Total Expectation

> 

## Moment

> A **moment** of a random variable is a quantitative measure that captures the shape, location, or spread of its probability distribution. Moments are expressed as **expected values of powers of the variable**, relative either to the origin or to the mean.
> 

| **Moment (Order)** | **Definition** | **What it Measures?** |
| --- | --- | --- |
| 1st (Mean) | $\mu_1' = \mathbb{E}[X]$ | Location / central tendency of the distribution |
| 2nd (Variance) | $\mu_2 = \mathbb{E}[(X - \mathbb{E}[X])^2]$ | Spread / dispersion around the mean |
| 3rd (Skewness) | $\mu_3 = \mathbb{E}[(X - \mathbb{E}[X])^3]$ | Asymmetry of the distribution (left/right skew) |
| 4th (Kurtosis) | $\mu_4 = \mathbb{E}[(X - \mathbb{E}[X])^4]$ | “Peakedness” or heaviness of tails |
| Higher-order moments | $\mu_k = \mathbb{E}[(X - \mathbb{E}[X])^k], k>4$ | Capture increasingly subtle shape features of the distribution |
| Raw moments | $\mu_k' = \mathbb{E}[X^k]$ | Describe distribution relative to origin; useful for reconstruction of the distribution in some contexts |

## Case Study

> 

### **Discrete Example (Fair Die)**

Let  $X$ be the outcome of a fair 6-sided die:   $\mathbb{E}[X] = \sum_{k=1}^6 k \cdot P(X = k) = \frac{1 + 2 + \cdots + 6}{6} = 3.5$.

### **Continuous Example (Exponential Distribution)**

If $X \sim \text{Exp}(\lambda)$ with PDF $f_X(x) = \lambda e^{-\lambda x}$:  $\mathbb{E}[X] = \int_0^\infty x \lambda e^{-\lambda x} \, dx = \frac{1}{\lambda}.$

## ❓ QA

### Why does the monotonicity property hold?

> My question arises when we have arguments like $m \le X \le M \implies \mathbb{E}[m] \le \mathbb{E}[X] \le \mathbb{E}[M]$.
> 

> Note:  Monotonicty requires equivalences; meanig they  come from the same experiment; but provided different view of it.
> 

> Monotonicity does not required the same probability distribution.
> 

### Why $E[C]$, where $C$ is a constant is $C$?

> My question arises when we have arguments like $m \le X \le M \implies \mathbb{E}[m] \le \mathbb{E}[X] \le \mathbb{E}[M]$.
> 

> Thinking It Trhought in a better way
> 

### Why a Moment if called a Moment?

> The term **“moment”** in probability and statistics comes from **mechanics**, specifically from the concept of a **moment of force** (torque) in physics.
> 

> A moment in statistics is called a **moment** because it’s a measure of the “weighted magnitude” of a distribution relative to a reference point, analogous to the concept of a moment in mechanics.
> 

### How do you compute the expected value of an estimator?

> 

### What is the relation of the Expected Value and the Sample Mean?

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
- https://en.wikipedia.org/wiki/Expected_value
- https://en.wikipedia.org/wiki/Law_of_total_expectation
