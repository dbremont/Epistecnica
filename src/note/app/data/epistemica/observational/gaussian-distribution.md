---
tags: [continous]
---

# Gaussian Distribution


> Models continuous data with a symmetric, bell-shaped curve.
> 

## Characterization

> Notation:
> 
> 
> X ~ 𝒩(μ, σ²)
> 

> Parameters:
> 
> 
> • μ ∈ ℝ (location / mean)
> 
> • σ > 0 (scale / standard deviation)
> 

> Support:
> 
> 
> x ∈ (-∞, ∞)
> 

### PDF

> f(x | μ, σ) = (1 / √(2πσ²)) · exp( - (x – μ)² / (2σ²) )
> 

### CDF

> Φ((x – μ)/σ) = ½ [ 1 + erf( (x – μ)/(σ√2) ) ]
> 

### Moments

> • Mean E[X] = μ
> 
> 
> • Variance Var[X] = σ²
> 
> • Skewness 0
> 
> • Excess kurtosis 0
> 
> • Moment-generating function M_X(t) = exp( μt + ½σ²t² )
> 

## Fisher Information

> I(μ, σ) =
> 
> 
> [ 1/σ²   0 ]
> 
> [ 0   2/σ² ]
> 
> (diagonal matrix; parameters μ and σ² are orthogonal)
> 

## Underlying Principles Influencing the Distribution

> • Central Limit Theorem: the sum (or average) of many i.i.d. random variables tends toward 𝒩(μ, σ²).
> 
> 
> • Maximum entropy among all distributions with fixed mean and variance on ℝ.
> 
> • Symmetry, infinite divisibility, and closure under affine transformations.
> 

## Standard Gaussian Distribution

> Z ~ 𝒩(0, 1)
> 
> 
> • PDF φ(z) = (1/√(2π)) e^{-z²/2}
> 
> • CDF Φ(z) = ½ [1 + erf(z/√2)]
> 
> • Quantile function Φ⁻¹(p) (probit function)
> 
> • 68–95–99.7 rule: P(|Z| ≤ 1, 2, 3) ≈ 68 %, 95 %, 99.7 %
> 

## Applications

> • Statistical inference: hypothesis tests, confidence intervals, linear regression.
> 
> 
> • Measurement errors, noise modeling in engineering.
> 
> • Finance: log-returns often assumed ~𝒩(μ, σ²).
> 
> • Quality control: control charts.
> 
> • Machine learning: Gaussian processes, Bayesian classifiers.
> 

## Relations

> • Affine transform: if X ~ 𝒩(μ, σ²), then aX + b ~ 𝒩(aμ + b, a²σ²).
> 
> 
> • Sum of independent normals: X₁ + … + X_k ~ 𝒩(Σμ_i, Σσ_i²).
> 
> • χ² distribution: Z² ~ χ²(1).
> 
> • Student-t: ratio of 𝒩 to √(χ²/ν).
> 
> • Lognormal: if ln Y ~ 𝒩(μ, σ²), then Y is log-normal.
> 
> • Conjugate priors: Normal–Inverse-Gamma for Bayesian updates.
> 

## References

- https://en.wikipedia.org/wiki/Normal_distribution
- https://news.ycombinator.com/item?id=41912160
