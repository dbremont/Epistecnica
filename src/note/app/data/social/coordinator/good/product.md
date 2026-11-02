---
tags: [product, good, economic, social-element]
---

# Product

> A **Product** is the exchangeable outcome of production offered into a market: a good or service carrying value from a firm's portfolio to a buyer. Source: Produceologia `docs/Catalog/Product.md` and `docs/Catalog/Good/` (read-only import; the originals are untouched).

## Formulation

### What social element type does this social instance belong to?

**Product belongs to the `Product` social element type (Coordinators category)** — the exchangeable outcome of `Economic Activity` offered into a `Market`; a good or a service. Its layer is **Multi**: it holds an Ontic side (the physical good, its materiality and lifecycle stage) and a Synontic side (the recognized offer: price, contract, brand) at once. Its facet is economic.

Readable secondarily through its Synontic offer reading (product-as-`Price / Asset`: the priced, contracted, claimable offer) and through its Noetic ranks (`Product Type`, `Product Family`, `Product Category`, `Product Class`, `Product Taxonomy`) per the multi-root forest rule; those readings are prose here, not separate trees. A product is **not** a coordinator — prices, money, and contracts coordinate; the product is what is coordinated.

### What is this social instance?

> A product fixes *what is exchanged*: the portfolio position, the deliverable offer, and the terms under which it changes hands. The Catalog distinguishes the generic product from concrete goods (Lemon, Cheese, Wine, …), each with its own production base and market.

### What is the recursive instance decomposition of this social instance?

> Boundary: one generic Product, decomposed at shallow depth — root plus the exemplar goods family only.
>
> Stopping rule: a row is terminal when it names the product or one exemplar good.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| Price / Asset `(→ Part)` Product | Priced, contracted outcome of production offered into a market. |
| Price / Asset `(→ Part)` Product `(→ Part)` Price / Asset | Grouping: exemplar goods realizing the product family. |
| Price / Asset `(→ Part)` Product `(→ Part)` Price / Asset `(→ Part)` Lemon | Citrus fruit good traded fresh and processed. |
| Price / Asset `(→ Part)` Product `(→ Part)` Price / Asset `(→ Part)` Cheese | Dairy good traded fresh and aged. |
| Price / Asset `(→ Part)` Product `(→ Part)` Price / Asset `(→ Part)` Wine | Fermented beverage good traded bottled and bulk. |

## References

- Produceologia `docs/Catalog/Product.md` and `docs/Catalog/Good/Agriculture/`
- Produceologia `docs/Firm/Toolkit/Product/` (MVP, lifecycle, strategy)
- [Philosophia Socialium et Operis](note.html?n=meta/philosophia-socialium-et-operis.md)
- [Economic Activity](note.html?n=social/action/activity/economic/economic-activity.md)
- [Market](note.html?n=social/coordinator/market/market.md)
- [Harmonized System — World Customs Organization](https://www.wcoomd.org/en/topics/nomenclature/overview.aspx)
