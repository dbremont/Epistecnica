---
tags: [discrete]
---

# Bernoulli Distribution

   : Binomial Distribution (Binomial%20Distribution%2093d6cef12f104d769af0627f2a04c139.md), Negative Binomial Distribution (Negative%20Binomial%20Distribution%20d9d392b312aa4766bdccde4c07ccfd70.md), Geometric Distribution (Geometric%20Distribution%205b08dc3f91464f80a3f9aacd5ad797cd.md)

> Models a single trial with two possible outcomes (success or failure).
> 

> The **Bernoulli distribution** is a **discrete probability distribution** for a random variable that has exactly **two possible outcomes**, often coded as `1` (success) and `0` (failure). It models a single **trial** of a **binary experiment**.
> 

> What kinds of **underlying systems**, experiments, or processes does this distribution represent?
> 

## Relation

| **Distribution** | **Relation to Bernoulli** | **Description** | **Typical Use Cases** |
| --- | --- | --- | --- |
| **Binomial** | Sum of independent Bernoulli trials | Models the number of successes in $n$ independent Bernoulli trials with same pp | Coin flips, number of successful vaccines in a population, number of passing students in a class |
| **Negative Binomial** | Generalization of geometric | Counts the number of trials until a fixed number $r$ of successes occurs | Number of patients treated until 5 respond, number of sales calls until 3 sales |
| **Geometric** | Waiting time until first success in Bernoulli trials | Counts the number of trials needed to get the first success | First defective item in production, first successful free-throw |
| **Hypergeometric** | Bernoulli trials without replacement | Number of successes in a sample drawn without replacement from a finite population | Lottery, quality control when sampling without replacement |
| **Poisson** | Limit of Binomial when $n$ large, $p$ small | Models number of successes in large number of rare Bernoulli-like trials | Rare events: emails per minute, defects per batch |
| **Multinomial** | Generalization to more than two outcomes | Counts occurrences of multiple categories in $n$ independent trials | Dice rolls, voting outcomes, product category sales |
| **Beta-Bernoulli (Bayesian)** | Bernoulli parameter pp is random (Beta distributed) | Captures uncertainty about success probability | Bayesian modeling of conversion rates, vaccine effectiveness |

## Case Study

| **Case Study** | **Notes** | **Success $(X=1)$** | **Failure $(X=0)$** |
| --- | --- | --- | --- |
| Coin Toss | Classic Bernoulli trial | Heads | Tails |
| Single Vaccine Response | Trial only counts if patient is eligible | Immune response | No response |
| Light Bulb Test | Only valid if bulb is installed properly | Bulb works | Bulb fails |
| Email Spam Detection | Only applicable if email is valid | Email correctly marked as spam | Not marked / wrongly marked |
| Single Free-Throw in Basketball | Must be performed under official game conditions | Basket made | Basket missed |
| Customer Purchase Decision | Trial counts only if customers saw the product | Customer buys | Customer does not buy |
| Product Defect Check | Only tests valid products from production line | Defective | Not defective |
| Kidney Transplant Compatibility | Bernoulli trial represents whether a transplant succeeds given compatibility | Transplant successful | Transplant fails |

## References

- https://en.wikipedia.org/wiki/Bernoulli_distribution
