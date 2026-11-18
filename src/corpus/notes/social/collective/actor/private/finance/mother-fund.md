---
tags: [note, mother-fund, fund-of-funds, capital, actor]
---

# Mother Fund

> A Mother Fund is a wholesale investment fund that pools capital from investors and allocates it to a portfolio of guidance (child) funds, which further channel the capital, under different investment strategies (e.g., equity or debt), into Operating Funds (e.g., venture capital funds, private equity funds, infrastructure funds, real estate funds, growth funds, debt funds, hedge funds, and other specialized investment vehicles).

- Fondo Guia Mayor.
- Fondo Guid Sectorial Menor <Sector>

Note:

- This strategy must be combined with a matching-fund mechanism to align investment incentives, ensure the appropriate targeting of investment destinations, and leverage the knowledge and informational capabilities of the surrounding investment ecosystem when identifying priority sectors, firms, and specific investment opportunities.  Also money, the matchign rule can be 50:50, etc.
- The operating funds must not be state align.
- The operating funds must be periodicaly audited.
- The operating funds must have ceratin proven history.
- Remember I have a war wiwh the idea of SME; in the sense that economic activaties, dictate relationship of firm size (capital, etc) -> theoritical price of cost archivable.
- We should promote competitive, firms, and we shoudl not be pre-emptubly be selecting the size, we shoudl select the sector, and let the operating funds select the size, i mean we can have policy of concentration, etc.

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

### Which are some case study?

| Country | Case | Description |
|---|---|---|
| Israel | **Yozma Fund (1993)** | Government-backed fund-of-funds that invested in ten privately managed venture capital funds, attracting foreign investors, domestic financial institutions, and private capital. Private partners had the option to buy out the government's participation. One of the strongest examples of catalytic public investment and independent fund management. |
| Canada | **Venture Capital Catalyst Initiative (VCCI)** | Federal investment program allocating capital to privately managed venture capital funds, including specialized streams for life sciences and clean technology. Combines public commitments with private fundraising. |
| China | **Government Guidance Funds (GGFs)** | A large system of central and subnational government-backed funds that establish or invest in sectoral and regional subfunds. Targets strategic industries, including semiconductors, biotechnology, advanced manufacturing, and clean energy. Particularly relevant to the proposed multi-tier architecture, although government direction can extend into operating investment decisions. |
| India | **National Investment and Infrastructure Fund (NIIF)** | Government-sponsored investment platform that mobilizes domestic and international institutional capital into infrastructure and other strategic sectors through specialized investment vehicles and co-investment arrangements. |
| Sweden | **Regional Co-investment Funds** | Public-private regional venture capital funds matching public resources with private investment to finance early-stage companies and strengthen regional investment ecosystems. |
| Australia | **Innovation Investment Fund (IIF)** | Government-supported venture capital program providing capital to privately managed funds, with preferential financial arrangements designed to attract private investors and stimulate investment in innovative firms. |
| Netherlands | **Dutch Good Growth Fund (DGGF)** | Fund-of-funds that invests in local and regional investment funds, which subsequently finance SMEs. Uses blended finance and accepts higher investment risks to mobilize private capital in underserved markets. |
| Indonesia | **Indonesia Investment Authority (INA)** | Sovereign investment institution that mobilizes domestic and international institutional capital through co-investments, investment platforms, and partnerships in infrastructure, healthcare, digital infrastructure, and other sectors. |
| Germany | **High-Tech Gründerfonds (HTGF)** | Public-private venture capital fund investing in technology-based startups, combining government and corporate participation. Useful for examining institutional cooperation between public capital and private industrial investors. |
| United Kingdom | **British Business Bank – Enterprise Capital Funds** | Government-backed investment structure supporting independently managed venture capital funds through public-private financing arrangements, particularly for companies facing financing gaps. |

## References

- [Government Guidance Fund](/view.html?p=notes/social/collective/actor/public/catalog/finance/government-guidance-fund.md) (the guided child-fund family this fund channels into)
- [Philosophia Socialium et Operis](/view.html?p=notes/philosophia-socialium-et-operis.md)
- [Market](/view.html?p=notes/social/coordinator/market/market.md) (arena allocated capital enters)
- Graph nodes of the same names: `mother-fund`, `government-guidance-fund` (Social Space, dataset `social`)
