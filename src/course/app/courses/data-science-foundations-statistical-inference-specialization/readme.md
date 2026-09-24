---
tags: [mathematics]
---

# Data Science Foundations: Statistical Inference Specialization


> Note: The concepts provide by this course must be inmediatly; integrated in my  Notes - Bremontix Ars.
> 

> Note: This course  does not count I have violated the Coursera Aggreement by using in several problems LLM Tools,  so take it again.
> 

## Summary

**Three courses:**

- Probability Theory: Foundation for Data Science
- Statistical Inference for Estimation in Data Science
- Statistical Inference and Hypothesis Testing in Data Science Applications

## Descriptive Statistics and the Axioms of Probability

- [ ]  Reading: https://bookdown.org/probability/beta/r.html & https://bookdown.org/probability/beta/counting.html, [Introducing the formula sheet for this course](https://www.coursera.org/api/rest/v1/asset/download/pdf/6ZjCDVtCQPGRBkGouxZfww?pageStart=&pageEnd=)
- [ ]  Lecture:
    - [ ]  [Intro to Probability Slides](https://d3c33hcgiwev3.cloudfront.net/OrSDb-bQRd20g2_m0KXdCA_91969fbe8d8d4a899c809b03c0329af1_module1_V1_slides.pdf?Expires=1754870400&Signature=SIkpp76ScE902f4IsE7-G~mHc7c733pEODF6rxS25XizmzbYGlM9fEKt1tkVEiQ2gXewnnAuD-Xc53KTHP0HVUXGErigcaGUTj8~ojMdDnIXXxfKAQDj9lKAuWFlFiVEAxuz9KPHu~lEu6ZD5m71oepErP66WvGjcNT-15xOgEc_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)
    - [ ]  [Axioms of Probability Slides pdf](https://d3c33hcgiwev3.cloudfront.net/ziXEvcQeSDGlxL3EHkgxDw_ffd2801b85034465bd80d06e58b74df1_module1_V2_slides.pdf?Expires=1754870400&Signature=VdNmHrRDdjDdTiHzFW6aJ8HrHTGdYd~eexWesbTLye-ZIsBdBFUs0RCFQ2-cr4Hi3gHxh-Vl6jZQJ7LAgsZwo7b~MTLpFMjp1y67NVwHHJpeeBRAZE28hiqt0kJtnGDv64SnaEb~lFKH~2QLitwPb-NZoRiIKs9rO7qDm9is2S8_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)
    - [ ]  [Counting: Permutations and Combinations Slides pdf](https://d3c33hcgiwev3.cloudfront.net/26_c7M7jT7Wv3OzO4z-1VA_9cb6e75880754fbd92d6be1c8decfaf1_module1_V3_slides.pdf?Expires=1754870400&Signature=jyBGg1M6WoylNO8fV5NUWJ9W~bH3mknqtHS0wxXKs8bQK9V5RDObkkrMpSVwrAIqGMnnndnmWakXshj3Y05btR9qAxzTSqXBDmqwQxDr1DSZToq~H7g6HzTeZfM-ABoZXmN58X0-w9-2fYWZ~USIZEqAcamIVOE9JDazPkBj~rU_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)
- [ ]  Notebooks:
    - [Introduction to Jupyter Notebooks and R](https://www.coursera.org/learn/probability-theory-foundation-for-data-science/ungradedLab/AubrC/introduction-to-jupyter-notebooks-and-r/lab?path=%2Fnotebooks%2FIntroduction%2520to%2520Jupyter%2520Notebooks%2520and%2520R.ipynb)
    - [descriptive_and_axioms](https://www.coursera.org/learn/probability-theory-foundation-for-data-science/ungradedLab/yU2e6/guided-exploratory-ungraded-lab/lab?path=%2Fnotebooks%2Fdescriptive_and_axioms.ipynb)

## Conditional Probability

- [ ]  Read: https://bookdown.org/probability/beta/
- [ ]  Lab: [https://www.coursera.org/learn/probability-theory-foundation-for-data-science/ungradedLab/pDTsk/guided-exploratory-ungraded-lab](https://www.coursera.org/learn/probability-theory-foundation-for-data-science/ungradedLab/pDTsk/guided-exploratory-ungraded-lab)

## Discrete Random Variables

- Read: [https://bookdown.org/probability/beta/](https://bookdown.org/probability/beta/)
- Lab: [https://www.coursera.org/learn/probability-theory-foundation-for-data-science/ungradedLab/vVG1N/guided-exploratory-ungraded-lab](https://www.coursera.org/learn/probability-theory-foundation-for-data-science/ungradedLab/vVG1N/guided-exploratory-ungraded-lab)

## Continuous Random Variable

- In this module, we explore the extension of the toolset to the continuous case and examine new distributions, such as the Poisson and Gaussian distributions.

## Joint Distribution and Covariance

> Read: https://bookdown.org/probability/beta/
> 

![image.png](courses/data-science-foundations-statistical-inference-specialization/image.png)

![image.png](courses/data-science-foundations-statistical-inference-specialization/image-1.png)

Let $X$ be a random variable such that $E(X) = 3$, $sd(X) = 4$, and let $Y$ be a
r.v. such that $E(Y ) = 1$, $sd(Y ) = 2$. $X$ and $Y$ are not linearly independent, and
$corr(X, Y ) = 0.5$. 

What is $E(X + 3Y + 1)$?

1. 25
2. 0.3412
3. 0.5
4. 0.25
5. 5.4
6. 0.4345
7. No

## The Central Limit Theorem

![image.png](courses/data-science-foundations-statistical-inference-specialization/image-2.png)

1. 0.471
2. 2
3. 5
4. 0.814

## Point Estimation

> In this module, we introduce discrete random variables, the Probability Mass Function (PMF), and the Bernoulli distribution,  Indicator Function, …
> 

> Distributions: Bernoulli Distribution, The Geometric Distribution, The Binomial Distribution,  The Poisson Distribution.
> 

Recognizing Probability Distributions - Is a Skill That I Should Practice.

| **Distribution** | **Description** |
| --- | --- |
| **Bernoulli** | Models a single trial with only two possible outcomes: success (1) or failure (0), with probability of success $p$. |
| **Geometric** | Models the number of independent Bernoulli trials needed until the first success occurs, with probability of success $p$. |
| **Binomial** | Models the number of successes in $n$ independent Bernoulli trials, each with probability of success $p$. |
| **Poisson** | Models the number of events occurring in a fixed time or space interval when events happen independently at an average rate $\lambda$. |
| **Gauss** |  |
| Exponential |  |
| Continuous Uniform |  |
| Gamma Distribution |  |
| Chi-squared Distribution |  |

> **Transformation of Distribution**:  Let’s say that we have a random variable X that follows certain distribution D, and we apply operator to that random variable - including ones that deal with other random variable; how to derive the new distribution form $X_d$ where d means derived?
> 

> **Estimator:** A rule or function that provides an estimate of a population parameter based on sample data.
> 

> **Method of Moments:** A technique for estimating population parameters by equating sample moments (like mean, variance) to the corresponding theoretical moments of the distribution.
> 

## Maximum Likelihood Estimation

> 
- MLE, Invariant Property, …

## Large Sample Properties of Maximum Likelihood Estimators

> See more here [‣](https://app.notion.com/p/270c0f5171ec80c6b159ffe9613ef6e5?pvs=21).
> 

> Fisher Information: How much information the data gives about the unknown parameter. It is based on how sensitive the likelihood is to changes in the parameter.
> 

> Cramér-Rao Lower Bound: The smallest possible variance that any unbiased estimator of a parameter can have. It is a benchmark for efficiency.
> 

> The Weak Law of Large Numbers: As the sample size gets bigger, the sample mean gets closer (in probability) to the true population mean.
> 

> The Central Limit Theorem:  For large samples, the sample mean is approximately normally distributed, no matter the original distribution (if it has finite mean and variance).
> 

**Large Sample Properties of Estimators:**

- **Consistent Estimator:** As the sample size grows, the estimator gets closer to the true parameter value.
- **Asymptotically Unbiased:** Any bias in the estimator disappears as the sample size grows.
- **Asymptotically Efficient:** For large samples, the estimator has the smallest possible variance among all consistent estimators.

## Confidence Intervals Involving the Normal Distribution

> 

## References

- https://www.coursera.org/specializations/statistical-inference-for-data-science-applications
