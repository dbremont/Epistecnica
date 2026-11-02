---
tags: [mother-fund, fund-of-funds, capital, actor]
---

# Mother Fund

> A Mother Fund is a wholesale investment fund that pools capital from investors and allocates it to a portfolio of guidance (child) funds, which further channel the capital, under different investment strategies (e.g., equity or debt), into Operating Funds (e.g., venture capital funds, private equity funds, infrastructure funds, real estate funds, growth funds, debt funds, hedge funds, and other specialized investment vehicles).

- Fondo Guia Mayor.
- Fondo Guid Sectorial Menor <Sector>

Mother Fund
→ Guidance Fund A (FoF) → VC / PE / infrastructure / credit funds
→ Guidance Fund B (FoF) → VC / growth / technology funds
→ Guidance Fund C (FoF) → regional / sectoral funds
→ Operating Funds → companies / projects / assets


```
                    NATIONAL MOTHER FUND
                  strategic / reporting layer
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
   Guidance FoF       Guidance FoF       Guidance FoF
   Biotechnology      Manufacturing      Infrastructure
          │                 │                 │
          ▼                 ▼                 ▼
   Operating Funds    Operating Funds    Operating Funds
          │                 │                 │
          ▼                 ▼                 ▼
       Investments       Investments       Investments

```

## Formulation

### What social element type does this social instance belong to?

**Mother Fund belongs to the `Capital / Labor` social element type — a multi-layer economic operator pooling resources and directing productive capacity.**

It is a capital pool with an allocation compass: investors commit capital that the mother fund divides across guidance funds and managers toward mandated ends. Its layer is read twice — **Ontic** as the committed pool and legal entity, **Synontic** as the recognized allocation claim and mandate signal markets act upon — which is why it types as a Multi operator rather than a plain fund. Its facet is economic. A mother fund is not a `Firm` (it allocates rather than operates) and not a `Policy` (it is the capitalized instrument, not the rule itself).

### What is this social instance?

> A mother fund fixes *where wholesale capital goes*: investors commit money, the mother fund channels it into guidance funds, and the guidance funds steer it into enterprises and sectors that struggle to secure market funding. The type spans a spectrum from pure fund-of-funds allocation across independent sub-funds to mandate-driven channeling into state-guided vehicles, and any classification of a given mother fund must state where on that spectrum it sits.

### What is the recursive instance decomposition of this social instance?

> Boundary: one generic Mother Fund — mechanism plus the guidance-fund family only.
>
> Stopping rule: a row is terminal when it names a mechanism component or a guidance-fund exemplar.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| Capital / Labor `(→ Part)` Mother Fund | Wholesale fund channeling pooled capital into guidance funds. |
| Capital / Labor `(→ Part)` Mother Fund `(→ Part)` Price / Asset | Grouping: capital components of the fund. |
| Capital / Labor `(→ Part)` Mother Fund `(→ Part)` Price / Asset `(→ Part)` Committed Investor Capital | Investor commitment anchoring the fund and signaling mandate scale. |
| Capital / Labor `(→ Part)` Mother Fund `(→ Part)` Price / Asset `(→ Part)` Guidance Fund Stakes | Allocated positions in guidance (child) funds executing onward investment. |
| Capital / Labor `(→ Part)` Mother Fund `(→ Component)` Institution | Grouping: rules stabilizing the fund's operation. |
| Capital / Labor `(→ Part)` Mother Fund `(→ Component)` Institution `(→ Component)` Allocation Mandate | Policy rule bounding which guidance funds and ends the fund may back. |
| Capital / Labor `(→ Part)` Mother Fund `(→ Part)` Social Relation / Network | Grouping: ties binding the fund to its executors. |
| Capital / Labor `(→ Part)` Mother Fund `(→ Part)` Social Relation / Network `(→ Part)` Guidance Fund Tie | Ties to guidance funds channeling capital into priority targets. |

## QA

### Which are the models of `State Capital Allocation`?

| Model                           | Strategic coordination | Capital allocation | Investment execution |
| ------------------------------- | ---------------------- | ------------------ | -------------------- |
| **Direct state allocation**     | State                  | State              | State                |
| **Sovereign fund**              | Central fund           | Central fund       | Fund                 |
| **Development bank**            | Central bank           | Bank               | Bank/funds           |
| **National FoF**                | Central fund           | Professional funds | Funds                |
| **Mother Fund + thematic FoFs** | **Mother Fund**        | **FoFs / funds**   | **Operating funds**  |
| **Guidance-fund system**        | State + multiple funds | Guidance funds     | Operating funds      |
| **Distributed state funds**     | Multiple agencies      | Multiple agencies  | Funds                |
| **Institutional-capital model** | State/regulator        | Institutions       | Markets              |
| **Tax/incentive model**         | State                  | Private markets    | Private investors    |

## References

- [Government Guidance Fund](note.html?n=social/collective/actor/public/catalog/finance/government-guidance-fund.md) (the guided child-fund family this fund channels into)
- [Philosophia Socialium et Operis](note.html?n=meta/philosophia-socialium-et-operis.md)
- [Market](note.html?n=social/coordinator/market/market.md) (arena allocated capital enters)
- Graph nodes of the same names: `mother-fund`, `government-guidance-fund` (Social Space, dataset `social`)
