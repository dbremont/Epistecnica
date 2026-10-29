---
tags: [estimator, technique]
---

# Fisher Information

 : Cramér–Rao Lower Bound (CRLB) (Cram%C3%A9r%E2%80%93Rao%20Lower%20Bound%20(CRLB)%20270c0f5171ec8038973bc8ee4b89bfec.md), Expected Value (Expected%20Value%20a126776d511e4492b643fb5075e68ef2.md), Theory of Statistics (Theory%20of%20Statistics%20272c0f5171ec80ce988eebaba3a61964.md), Relative Efficiency (Relative%20Efficiency%20272c0f5171ec80f39b6dc6ed72cd8f62.md), Information Geometry (Information%20Geometry%209e8f47513e9c4b8ba9e9450c52dced78.md), Information (Information%2017ac0f5171ec813d813ff6055c98fe7d.md)

It measures **how much information an observable random variable carries about an unknown parameter**. Intuitively:

- If a dataset provides **a lot of information about a parameter**, you can estimate that parameter more precisely.
- If a dataset provides **little information**, your estimates will be noisier.

## Formulation

> Let $X$ be a random variable with probability density (or mass) function $f(x;\theta)$, where $\theta$ is an unknown parameter.
> 

The **Fisher Information** $I(\theta)$ is defined as:

$I(\theta) = \mathbb{E} \Bigg[ \Bigg( \frac{\partial}{\partial \theta} \ln f(X;\theta) \Bigg)^2 \Bigg]$

Where:

- $\ln f(X;\theta)$ is the **log-likelihood function** of a single observation.
- The derivative $\frac{\partial}{\partial \theta} \ln f(X;\theta)$ is called the **score function**.
- The expectation $\mathbb{E}[\cdot]$ is taken **over the distribution of $X$** at the true parameter value.

Equivalent form (sometimes easier to compute) - Both forms are equal under regularity conditions.:
$I(\theta) = - \mathbb{E} \Bigg[ \frac{\partial^2}{\partial \theta^2} \ln f(X;\theta) \Bigg]$

## Property

1. **Additivity:** For independent observations $X_1, \dots, X_n$: $I_n(\theta) = n \, I(\theta)$
2. **Connection to variance of estimators:**
The **Cramér–Rao Lower Bound (CRLB)** states that the variance of any unbiased estimator $\hat{\theta}$ satisfies:  $\text{Var}(\hat{\theta}) \ge \frac{1}{I_n(\theta)}$

## Case

### **Normal Distribution with Unknown Mean $\mu$, Known Variance $\sigma^2$**

The pdf is:  $f(x;\mu) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\Big(-\frac{(x-\mu)^2}{2\sigma^2}\Big)$

**Step 1: Compute log-likelihood for a single observation**
$\ell(\mu) = \ln f(x;\mu) = -\frac{1}{2}\ln(2\pi\sigma^2) - \frac{(x-\mu)^2}{2\sigma^2}$

**Step 2: Compute derivative w\.r.t $\mu$ (score function)**
$\frac{\partial \ell}{\partial \mu} = \frac{(x-\mu)}{\sigma^2}$

**Step 3: Compute Fisher Information**
$I(\mu) = \mathbb{E}\Big[\Big(\frac{\partial \ell}{\partial \mu}\Big)^2\Big]
= \mathbb{E}\Big[\frac{(X-\mu)^2}{\sigma^4}\Big]
= \frac{1}{\sigma^4} \mathbb{E}[(X-\mu)^2]
= \frac{1}{\sigma^4} \cdot \sigma^2
= \frac{1}{\sigma^2}$

### **Normal Distribution with Known Mean $\mu$, Unknown Variance $\sigma^2$**

Let $\theta = \sigma^2$. The pdf:  $f(x;\sigma^2) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\Big(-\frac{(x-\mu)^2}{2\sigma^2}\Big)$

**Step 1: Log-likelihood**
$\ell(\sigma^2) = -\frac{1}{2}\ln(2\pi\sigma^2) - \frac{(x-\mu)^2}{2\sigma^2}$

**Step 2: Derivative w\.r.t $\sigma^2$**
$\frac{\partial \ell}{\partial \sigma^2} = -\frac{1}{2\sigma^2} + \frac{(x-\mu)^2}{2\sigma^4} = \frac{(x-\mu)^2 - \sigma^2}{2\sigma^4}$

**Step 3: Fisher Information**
$I(\sigma^2) = \mathbb{E}\Big[\Big(\frac{\partial \ell}{\partial \sigma^2}\Big)^2\Big]
= \mathbb{E}\Big[\frac{((X-\mu)^2 - \sigma^2)^2}{4\sigma^8}\Big]$

We know $\text{Var}((X-\mu)^2) = 2(\sigma^2 )^2$, so:  $I(\sigma^2) = \frac{2\sigma^4}{4\sigma^8} = \frac{1}{2\sigma^4}$

## QA

> Which the assumption of the method?
> 

> 

## References

- https://en.wikipedia.org/wiki/Fisher_information
