---
tags: [decision-making, probability]
---

# Kelly Criterion

 : Expected Value (Expected%20Value%20a126776d511e4492b643fb5075e68ef2.md), Betting (Betting%20183c0f5171ec80288181fb6b78a4c610.md)

> If you have $100 and a bet with a 60% chance of winning that pays 1:1, how much should you bet according to the Kelly Criterion? You should bet $20, which is 20% of your $100 bankroll.
> 

> The **Kelly Strategy** (or **Kelly Criterion**) is a **mathematical formula** used to determine the optimal size of a series of bets or investments in order to maximize the expected logarithmic growth of wealth over time, balancing the trade-off between risk and reward. It is based on the principle of betting a fraction of your capital that is proportional to the expected edge of the bet, calculated as the difference between the probability of winning and the odds, relative to the total possible outcomes. The strategy seeks to avoid both under-betting (which sacrifices potential gains) and over-betting (which risks significant loss), providing a long-term optimal growth strategy.
> 

> **Kelly Strategy**: A **decision-making under uncertainty** method; it requires an underlying model of the probabilities (this is  the challenging part, as probability distributions in real-life  scenarios are often dynamic and difficult to estimate accurately).
> 

> **Edge**: The Kelly Criterion is most useful when you have a positive expected value (i.e., $bp - q > 0$. This means you have an "edge" in the bet or investment.
> 

> **Risk Taking**: The Kelly Criterion helps avoid over-betting, which can lead to ruin, while still allowing for aggressive growth when you have an edge.
> 

> **Bankroll** means `Fondo / Capital`  ; wager means `Apuesta`.
> 

QA:

- Determine the optimal fraction of your bankroll to bet on the Dominican Lottery  (betting option 1-100) , payout structure (60:1) using the Kelly Criterion, given the low probability of winning (1%).
- …

The **Kelly Criterion formula** is:  $f^* = \frac{bp - q}{b}$

Where:

- $f^*$: The fraction of the current bankroll to wager.  How much money should i Bet / Invest?
- $b$: The net odds received on the **wager** (i.e., the amount you win per unit wagered). What is the Pay out structure?
- $p$: The probability of winning.
- $q$: The probability of losing $q = 1 - p$.

## Kelly Methods

> 

| **Method** | **Description** | **Formula** | **Use Case** |
| --- | --- | --- | --- |
| **Classic Kelly Criterion** | Determines the optimal fraction of bankroll to bet for binary outcomes. | $f^* = \frac{bp - q}{b}$ | Binary bets (e.g., win/lose, heads/tails). |
| **Fractional Kelly** | Bets a fraction of the Kelly-recommended amount to reduce volatility. | $f_{\text{frac}} = k \cdot f^*$ (e.g., $k = 0.5$ for half-Kelly). | Conservative betting or investing to reduce risk. |
| **Kelly for Multiple Outcomes** | Extends the Kelly Criterion to scenarios with more than two possible outcomes. | $f^* = \frac{\sum_{i} p_i \cdot b_i - 1}{\sum_{i} p_i \cdot b_i}$ | Horse racing, sports betting, or investments with multiple outcomes. |
| **Kelly for Continuous Returns** | Optimizes position sizing for investments with continuous return distributions. | $f^* = \frac{\mu - r}{\sigma^2}$ (Sharpe ratio-like formula). | Stock market investing or portfolio management. |
| **Kelly for Leveraged Bets** | Adjusts for leverage or margin in betting or investing. | $f^* = \frac{bp - q}{b \cdot L}$ (where $L$ is leverage factor). | Trading with leverage (e.g., forex, futures). |
| **Kelly for Correlated Bets** | Accounts for correlations between multiple bets or investments. | Requires solving a system of equations or using optimization techniques. | Portfolio optimization with correlated assets. |
| **Kelly for Partial Information** | Adjusts for uncertainty in probabilities or payoffs. | Bayesian or probabilistic approaches to estimate $p$ and $b$. | Scenarios with incomplete or uncertain information. |

## References

- https://en.wikipedia.org/wiki/Kelly_criterion
- https://news.ycombinator.com/item?id=42466676
- https://www.youtube.com/watch?v=-9JM9suCIHs
- https://www.youtube.com/watch?v=91IOwS0gf3g
- Kelly, John L. "A new interpretation of information rate." *the bell system technical journal* 35.4 (1956): 917-926.
- …
