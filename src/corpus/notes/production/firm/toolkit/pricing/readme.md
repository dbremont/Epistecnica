---
tags: [note, firm]
---

# Pricing

> Pricing is the formal process and analytical framework through which the monetary value of a good, service, or access right is determined. It integrates economic modeling, cost structures, market dynamics, behavioral responses, and strategic objectives to assign exchange values that optimize one or more performance criteria—such as profit, market share, or welfare.

> It also refers to the set of techniques and mechanisms employed by an agent (e.g., a firm or platform) to determine the cost imposed on users for accessing or consuming the products and services it offers.

Guiding Questions:

* How should we **think about pricing** — as a decision, a signal, or a system?
* What is the **relationship between price, cost, and value**?
* How can we model **optimal pricing** under different competitive or behavioral assumptions?
* How does **pricing strategy evolve** with scale, market learning, or technological change?
* How can pricing be used to **shape behavior** (e.g., incentives, segmentation, demand management)?
* Which is the relation between the pricing model and the business strategy?
* Which is the relation between pricing strategy and sales strategy?
* Is the Razor-and-Blades Model primarily a pricing strategy, or is it better understood as a sales or business strategy?

## **Formulation**

> The **pricing problem** can be formalized as finding the function $P(q, c, v, d, s, t)$ that maximizes the objective (profit, welfare, adoption, etc.) given constraints and signals: $\max_{P} ; \Pi = (P - C) \cdot D(P, S, T)$

where:

* $P$ = price
* $C$ = cost (variable or total)
* $D(P, S, T)$ = demand as a function of price, market structure $S$, and time $T$

The **pricing problem** thus integrates:

* **Cost structure** (production, transaction, opportunity costs)
* **Demand elasticity** and behavioral response
* **Strategic interaction** with competitors
* **Value perception** and willingness to pay
* **Temporal and dynamic factors** (learning, network effects, inflation, etc.)

## Method

> Which are the pricing methods (model, mechanism technique, etc )?

> A pricing model is a formal structure or rule that determines how prices are set for goods or services, given a set of variables such as cost, demand, competition, and strategic objectives.

| **Category** | **Name** | **Type** | **Description** | **Economic Logic** | **When to Use** |
| --- | --- | --- | --- | --- | --- |
| **Cost-Based** | *Cost-Plus Pricing* | Model | Price = cost + markup; simple, stable, ignores demand. | **Cost recovery** – guarantees margin regardless of demand. | Stable cost environments or regulated industries. |
| **Value-Based** | *Perceived Value Pricing* | Model | Sets price according to perceived customer value, not cost. | **Value capture** – align price with willingness to pay. | Differentiated or brand-driven products. |
| **Competition-Based** | *Market Benchmarking* | Technique | Prices aligned with competitors or market averages. | **Market alignment** – avoid price wars, maintain parity. | Commodity or competitive markets. |
| **Adaptive** | *Dynamic Pricing* | Mechanism | Continuously adjusts prices based on time, demand, or inventory. | **Demand management** – optimize utilization and revenue. | Airlines, hotels, mobility, e-commerce. |
| **Discriminatory** | *Price Discrimination* | Strategy | Charges different prices across segments or conditions. | **Surplus extraction** – maximize revenue from heterogeneity. | Segmented markets with resale control. |
| **Behavioral** | *Psychological Pricing* | Technique | Uses cognitive biases (e.g., $9.99, anchoring) to shape perception. | **Perception shaping** – influence demand via framing. | Consumer and retail markets. |
| **Mechanism-Based** | *Auction / Subscription / Freemium* | Mechanism | Price emerges from structured participation or tiers. | **Market revelation** – self-selection or competitive bidding. | SaaS, platforms, digital ecosystems. |
| **Promotional** | *Loss Leader Strategy* | Strategy | Sells below cost to attract customers and trigger other sales. | **Traffic generation** – acquire customers for cross-selling. | Retail, supermarkets, marketplaces. |
| **Complementary** | *Razor-and-Blades (Gancho Comercial)* | Strategy | Base product cheap; profit from dependent complements. | **Lock-in and recurring revenue** – monetize through ecosystem. | Durable + consumable product systems. |
| **Optimization-Based** | *Profit-Maximizing / Welfare-Maximizing* | Model | Solves for prices that maximize objectives under constraints. | **Efficiency** – formal optimization of profit or welfare. | Data-rich or algorithmic pricing contexts. |
| **Elasticity Estimation** | Statistical Model | Estimates how demand responds to price changes. | **Demand sensitivity** – quantify marginal revenue impact. | Foundational step for analytical pricing. |  |
| **Conjoint Analysis** | Statistical Technique | Infers value of attributes and price tolerance from preferences. | **Value decomposition** – derive perceived utility components. | Product design, packaging, new product pricing. |  |
| **Regression-Based Models** | Predictive Model | Predicts sales or revenue given price inputs. | **Empirical optimization** – learn demand-price relation. | Historical data contexts; retail, e-commerce. |  |
| **Game-Theoretic Pricing** | Analytical Model | Models competitive price interactions to find equilibria. | **Strategic interaction** – anticipate rival pricing responses. | Oligopolistic or competitive sectors. |  |
| **Dynamic Programming Pricing** | Algorithmic Model | Optimizes pricing over time with inventory or uncertainty. | **Intertemporal optimization** – manage trade-offs across periods. | Airlines, perishables, digital markets. |  |
| **Probabilistic Pricing** | Statistical Algorithm | Updates price beliefs as data accumulates. | **Adaptive learning** – pricing under uncertainty. | Small data or experimental settings. |  |
| **Reinforcement Learning Pricing** | Learning Mechanism | Learns optimal pricing via reward feedback (trial & error). | **Exploration–exploitation balance** – continuous adaptation. | Online platforms, ads, and automated marketplaces. |  |
| **A/B & Multivariate Testing** | Experimental Technique | Tests price variants empirically to observe response. | **Empirical validation** – measure real-world behavior. | Web platforms, continuous optimization. |  |
| **Agent-Based Simulation** | Simulation Model | Simulates interactions among agents to test emergent outcomes. | **Complex system exploration** – study dynamic price behavior. | Research, policy design, strategic foresight. |  |

## Price Presentation Psychology

> What is the effect of price presentation on consumer perception and behavior?

> **Price Presentation Psychology** is the study and application of cognitive and perceptual principles that shape how people interpret, evaluate, and emotionally respond to prices. It examines how the format, context, framing, and visual design of price information influence perceived value, fairness, and willingness to pay.

| **Aspect**                       | **Description**                                                                | **Case**                                                            |
| -------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| **Framing**                      | The way a price or discount is expressed changes how it is perceived.          | "$99" feels cheaper than "$100" (left-digit effect).                            |
| **Anchoring**                    | Initial reference prices influence later evaluations.                          | Showing a $300 option makes a $200 option feel more affordable.                 |
| **Contextual Comparison**        | Prices are judged relative to other available options.                         | Tiered pricing (Basic, Pro, Premium) steers users toward the “middle” option.   |
| **Charm Pricing**                | Using prices ending in .99 or .95 suggests a bargain or precision.             | $19.99 appears significantly cheaper than $20.00.                               |
| **Font and Visual Design**       | The typography, color, and layout affect cognitive fluency and emotional tone. | Smaller fonts and clean designs feel more “premium.”                            |
| **Temporal Framing**             | Dividing costs over time increases affordability perception.                   | "$1/day" seems cheaper than "$365/year."                                        |
| **Social and Emotional Framing** | Price tied to identity, belonging, or moral justification.                     | “Support local farmers” framing increases purchase intent despite higher price. |


## Case Study

| **Case**                              | **Context**                                | **Applied Method(s)**                         | **Outcome**                                  | **Key Insight**                                                 |
| ------------------------------------- | ------------------------------------------ | --------------------------------------------- | -------------------------------------------- | --------------------------------------------------------------- |
| **Gillette – Razor-and-Blades Model** | Consumer goods; durable + consumable combo | *Loss Leader Pricing* + *Cross-Subsidization* | High adoption, recurring consumable revenue  | Initial loss enables ecosystem lock-in and customer dependency. |
| **Amazon Prime**                      | E-commerce, subscription ecosystem         | *Freemium → Subscription → Value-Based*       | Increased retention and cross-category spend | Bundled value shifts perception from cost to convenience.       |
| **Apple iPhone**                      | Premium consumer electronics               | *Value-Based* + *Psychological Pricing*       | Sustained high margins, strong brand loyalty | Price communicates quality and exclusivity.                     |
| **Tesla**                             | Direct-to-consumer automotive              | *Dynamic* + *Optimization-Based*              | High adaptability and margin control         | Real-time pricing aligns production, demand, and branding.      |
| **Netflix**                           | Streaming service                          | *Subscription* + *Tiered Pricing*             | Predictable revenue, customer segmentation   | Tiered access maximizes willingness to pay across segments.     |

## References

* [Pricing](https://en.wikipedia.org/wiki/Pricing)
* [Price](https://www.bremontix.xyz/lab/ar/Locus-Social-Realitatis/Facet/Economy/Intersection/Price/)
* [Fair Pricing](https://news.ycombinator.com/item?id=42944371)
* [Razor and blades model](https://en.wikipedia.org/wiki/Razor_and_blades_model)
* [Pricing niche products (kevinlynagh.com)](https://news.ycombinator.com/item?id=36358754)
* [Do not talk about pricing (medium.com/fluxx-studio-notes)](https://news.ycombinator.com/item?id=11563378)
* [Don't just roll the dice – Software pricing guide (2012)](https://news.ycombinator.com/item?id=22027912)
* [The Psychology of Pricing: A Gigantic List of Strategies](https://news.ycombinator.com/item?id=9501892)
* [A Guide to Pricing Plans (capitalandgrowth.org)](https://news.ycombinator.com/item?id=22895842)
* [Ten Years' Worth of Learning About Pricing (tomtunguz.com)](https://news.ycombinator.com/item?id=16180570)
* [Pricing psychology - 33% more beats 33% off (time.com)](https://news.ycombinator.com/item?id=4207134)
* [Pricing Money: A beginner's guide to money, bonds, futures and swaps](https://news.ycombinator.com/item?id=36358754)