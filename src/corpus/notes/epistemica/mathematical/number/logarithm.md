---
tags: [note, mathematics, function]
---

# Logarithm

 : Exponentiation (Exponentiation%20223c0f5171ec80b3849af0330ac62930.md)

> A **logarithm** is the power to which a base number must be raised to produce a given value, effectively reversing the process of exponentiation.
> 

> The **primary motivation** behind the invention of logarithms, developed by John Napier in the early 17th century, was to simplify complex calculations, particularly multiplication and division of large numbers, by transforming them into addition and subtraction, thereby making computations faster and less error-prone—especially useful in astronomy, navigation, and engineering at the time.
> 

> **Logarithms** transform multiplicative relationships into additive ones, providing a powerful tool for simplifying calculations, analyzing exponential growth, and modeling nonlinear phenomena in a linear framework.
> 

## Uses

### **Linearizing Nonlinear Relationships**

> **Simplification of multiplicative relationships**: Many economic models involve multiplicative relationships, such as production functions (e.g., Cobb-Douglas) or compound growth models. Taking logarithms of both sides transforms these into additive relationships, which are easier to analyze and interpret.
> 

### **Interpretation of Elasticities**

> **Elasticity**: When you take logarithms of variables, the coefficients of the variables in the log-transformed equation directly correspond to elasticities, which are the percentage change in one variable for a 1% change in another.
> 

### **Dealing with Growth Rates**

> **Growth rate approximation**: In economics, taking the log of a time series (e.g., GDP, population, or other economic variables) allows you to approximate the growth rate as a constant percentage change over time.
> 

### **Dealing with Large Numbers**

**Handling large or skewed data**: Logarithms help compress large numbers and reduce the impact of extreme values, making it easier to work with skewed data or data with high variance. This is especially useful in economic data where some variables (such as GDP or population) can span several orders of magnitude.

### **Solving Exponential Growth Models**

> **Exponential growth**: Many economic models, such as those involving compound interest, population growth, or technological progress, are based on exponential growth processes. Taking the logarithm of an exponential function transforms it into a linear form, which is easier to handle analytically or computationally.
> 

### **Error Terms and Homoscedasticity**

> **Stabilizing variance**: In econometrics, taking the logarithms of variables can help stabilize the variance of error terms, making them more homoscedastic (constant variance). This can be particularly helpful in regression analysis, where unequal variances across observations (heteroscedasticity) may lead to biased or inefficient estimates.
> 

### **Simplifying Optimization Problems**

> **Convexity and optimization**: Many optimization problems in economics involve nonlinear functions, and logarithms can simplify the process of finding the optimal solution. Logarithmic transformations often convert concave or convex functions into simpler forms that are easier to maximize or minimize.
> 

### **Statistical Modeling and Estimation**

> **Linear regression with log-transformed data**: In econometrics, log transformations are often used in regression analysis, especially when the dependent or independent variables are expected to have a multiplicative effect or non-constant variance. This helps to make the relationship between variables more linear and to simplify the estimation of model parameters.
> 

### **Normalization and Scaling**

> **Making variables more comparable**: Logarithmic transformation can help to normalize data, bringing variables with different magnitudes to a comparable scale. This is particularly useful when comparing the relative importance of different variables in a model.
> 

### **Convenience in Differentiation**

> **Differentiation and marginal analysis**: Logarithms make it easier to differentiate complex expressions, especially in models involving growth, production, and utility. The derivative of a logarithmic function is simpler (i.e., ) compared to directly differentiating the original function.
> 

## The Family of Inverses

> A logarithm is one instance of a general move: **invert a monotone operation to recover what was applied**. The exponential composes a base with an exponent, and $\ln$ recovers the exponent. The product $x e^x$ composes a variable with its own exponential, and the [Lambert W function](/view.html?p=notes/epistemica/mathematical/mapping/lambert-w-function.md) recovers the variable. The two functions are the same representational act applied to different products — and the difference in difficulty is the difference between isolating an exponent and solving an implicit equation.

| Operation | Inverse | What it recovers | Domain of the inverse |
| --- | --- | --- | --- |
| $e^x$ | $\ln x$ | The exponent, given the power | $x > 0$ |
| $a^x$ | $\log_a x$ | The exponent, given base and power | $x > 0$ |
| $x e^x$ | $W(x)$ | The variable, given the product | $x \ge -1/e$, two real branches |
| $x^x$ | $\dfrac{\ln y}{W(\ln y)}$ | The base, given the power tower's value | where the tower converges |

> Read this way, the logarithm is not only a computational convenience but the **first** member of a family of inverse operators, and the special functions the corpus files beside it — gamma, beta, Bessel, Lambert W — are the members that answer questions the elementary inverses cannot. The representational lesson is constant: the function is the inverse of a construction, and the construction determines how hard the inversion is.

## References

- [Jost Bürgi](/view.html?p=notes/social/collective/actor/private/persona/jost-burgi.md) — the tables of progressions built independently of Napier around 1600 and published only in 1620; the invention above is Napier's publication, not Napier's alone
- https://en.wikipedia.org/wiki/Logarithm
- https://en.wikipedia.org/wiki/History_of_logarithms
- https://betterexplained.com/articles/using-logs-in-the-real-world/
- …
