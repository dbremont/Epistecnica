---
tags: [miscellanea, model]
---

# Price Dynamics Analysis

> **Price** is an **emergent macro-level** variable resulting from the micro-level interactions of heterogeneous agents engaged in exchange within a market structure, subject to institutional constraints, information asymmetries, and dynamic feedback mechanisms. It reflects the marginal rate of substitution or marginal utility under equilibrium assumptions, or a non-equilibrium signal in adaptive or decentralized systems.
>

> **Price** is a scalar or vector-valued signal that encodes the relative marginal valuation of a good, service, or asset, emerging from the interaction of supply and demand dynamics within a defined institutional and informational structure. Formally, in general equilibrium theory, price vectors constitute elements of a Walrasian **equilibrium set** where excess demand functions vanish. In algorithmic or auction-based markets, prices are computed as clearing solutions to optimization problems (e.g., tâtonnement, convex programming, or dual formulations of utility maximization).
>

> In **complex adaptive systems,** price functions as a distributed coordination mechanism, arising endogenously from agent-based interactions under conditions of bounded rationality, local information, strategic heterogeneity, and dynamic learning. It serves not only as a clearing metric but also as a feedback variable influencing future agent behavior, enabling decentralized adaptation in **non-equilibrium environments**.
>

QA:

- Can this model capture **temporal dynamics**? And can it account for the fact that the underlying dynamics themselves may change over time?

## Index

## System Profile

> What is the underlying **ecosystem** **driving price** changes?
>

> Do we need to have a **model of the ecosystem**?
>

> The price system can be viewed as part of a larger **economic ecosystem**, where the interactions between various agents—consumers, producers, investors, and intermediaries—give rise to the dynamics of price formation. These agents interact within a given **market structure** that is shaped by:
>
> - **Institutional frameworks** (e.g., regulations, market design)
> - **Technological constraints** (e.g., infrastructure, algorithmic trading)
> - **Information flows** (e.g., news, market sentiment)
>
> These factors collectively influence the supply-demand equilibrium, but the process by which prices emerge is fundamentally **nonlinear**, **adaptive**, and **emergent** from agent interactions.
>

## Modelling

> **Note:** In order to **model price dynamics** accurately, a deep understanding of the underlying ecosystem—including the market structure and influencing factors—is essential.
>

### Economic Equilibrium

> In many models, especially **general equilibrium theory**, prices tend to settle at levels where **markets clear**—i.e., supply equals demand.
>

> These equilibria act as **attractors** in the phase space of economic dynamics. In the long term, barring shocks, prices may oscillate around these points.
>

> Equilibrium prices serve as **reference points** for assessing efficiency, welfare optimization, and stability in macroeconomic and microeconomic models.
>

> Economic Equilibrium refers to a theoretical state of an economic system in which all agents' plans are mutually consistent, markets clear (i.e., supply equals demand for all goods and services), and no agent has an incentive to unilaterally change their behavior. It constitutes a macro-level fixed point arising from micro-level optimizations under a specified set of constraints.
>
>
> In its classical form—e.g., **Walrasian general equilibrium**—the concept assumes an **idealized economic ecosystem** characterized by:
>
> - **Stationary dynamics** (unchanging preferences, technologies, and endowments),
> - **Perfect information and rationality**,
> - **Complete markets**, and
> - **No frictions** (e.g., transaction costs, market power, adjustment lags).

> Under these assumptions, prices act as coordinating signals, adjusting until a vector of prices is found that satisfies market-clearing conditions across all goods and agents. In dynamic variants (e.g., **Arrow–Debreu** models), equilibrium may extend across time and contingent states, incorporating intertemporal choices and uncertainty.
>

> More broadly, economic equilibrium serves as a modeling abstraction: a baseline against which deviations (e.g., shocks, disequilibria, path dependencies, or institutional frictions) can be studied in **non-equilibrium** or **evolutionary economic** theories.
>

Limits:

- In reality, economies are **non-stationary**: preferences, technologies, institutions, and endowments change.
- Real systems exhibit **hysteresis**, **lock-in effects**, and **non-ergodic dynamics**—features not captured by static equilibrium models.
- In complex adaptive systems (e.g., financial markets, platform economies), **prices are outcomes of evolving agent behavior**, not fixed points.
- Long-run prices may reflect **non-equilibrium steady states** or **meta-stable regimes** rather than classical equilibria.

### Demand Modelling

> Demand modeling focuses on understanding how various factors influence the demand side of price formation. A well-constructed demand model can help to estimate how changes in external factors (e.g., income, preferences, prices of substitutes) influence the quantity demanded of a good or service.
>

### Preference Modelling

> **Preference Modeling** refers to the theoretical and computational frameworks used to represent and predict the decision-making processes of individuals or agents, based on their preferences, tastes, and utility functions. It aims to capture how different factors (e.g., price, quality, availability, brand, etc.) influence consumer choice and demand behavior.
>

### **Market Structure Modeling**

> **Market Structure Modeling** refers to the representation and analysis of the organization, characteristics, and competitive dynamics within a market. The market structure dictates how firms interact, set prices, and behave within the system. Understanding market structure is crucial for predicting price formation, firm behavior, and overall market efficiency.
>

### Other Factors

- Supply Side Factors
- Information Asymmetries
- Competition and Strategic Behavior
- Behavioral and Psychological Factors
- Market Liquidity and Transaction Costs
- Market Dynamics and Feedback Loops
- External Shocks and Exogenous Factors

## Modelling Tools

| **Category** | **Tool** | **Use** |
| --- | --- | --- |
| Preference Modeling | **Utility Theory** | Models consumer choice based on utility maximization. |
|  | **Discrete Choice Models** | Predicts choices between discrete alternatives. |
|  | **Conjoint Analysis** | Estimation of consumer preferences for product features. |
| Demand-Supply Modeling | **Demand-Supply Equilibrium Models** | Determines price based on the interaction of demand and supply. |
| Competition Modeling | **Game Theory** | Analyzes strategic interactions between market participants. |
| Behavioral Modeling | **Agent-Based Modeling (ABM)** | Simulates individual agents with decision rules interacting within a market. |
| Optimization Modeling | **Linear Programming (LP)** | Solves for optimal allocation of resources under constraints. |
| Macroeconomic Modeling | **Dynamic Stochastic General Equilibrium (DSGE)** | Models economic systems with stochastic shocks and feedback loops. |
| Econometric Modeling | **Vector Autoregression (VAR)** | Models time-series data to understand relationships between multiple time-varying variables. |
| Policy and Regulation Modeling | **Monetary and Fiscal Models** | Models the effects of monetary and fiscal policies on the economy and prices. |
| Stochastic Simulation | **Monte Carlo Simulation** | Uses random sampling to simulate the behavior of complex systems and estimate price distributions. |
| Simulation Modeling | **Agent-Based Market Simulation (ABMS)** | Simulates the behavior of agents in market settings to understand price dynamics. |
| Supply Chain & Market Modeling | **Price-Volume Optimization Models** | Focuses on finding optimal price and volume combinations to maximize profit. |
| Time Series Analysis | **Time Series Forecasting (ARIMA, GARCH)** | Predicts future prices based on past price data. |
| Network Economics | **Network Effects Modeling** | Models how the value of goods/services increases as the number of users grows. |
| System Dynamics | **Complex System Models** | Models large-scale systems with feedback loops and interactions between various components. |
| Psychological & Behavioral | **Behavioral Economics Models** | Incorporates cognitive biases and psychological factors into economic decision-making models. |
| Supply Chain Modeling | **Supply Chain Management Models** | Optimizes pricing and production decisions along the supply chain. |

## Data Sets

- https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction
- https://www.kaggle.com/datasets/manjeetsingh/retaildataset
- IRI Marketing Data Set [Link](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YQQSLM)
- https://www.worldbank.org/en/research/commodity-markets
- Real State Prices - https://www.zillow.com/research/
- https://fred.stlouisfed.org/
- https://www.crsp.org/
- Dominick’s  Dataset https://www.chicagobooth.edu/research/kilts/research-data/dominicks

## References

- https://keepa.com/#

## Provenance

- Notion export: `Modelo/Miscellanea/Miscellanea/Price Dynamics Analysis 1dfc0f5171ec80508e24da8408aff551.md`
