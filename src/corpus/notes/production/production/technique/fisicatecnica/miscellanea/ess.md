---
tags: [note, production]
---

# Stationary Energy Storage Systems (ESS)

tags: Energy System
: 39

> A **stationary ESS** is engineered for **large-scale, long-duration, and high-power applications** with sophisticated management and safety systems.
> 

> A **power bank** is basically a **tiny, portable ESS** designed for convenience and small loads.
> 

## Index

## Structure

| Component | Function |
| --- | --- |
| **Battery bank** | Stores energy (usually Li-ion, LiFePO₄, or lead-acid). |
| **Battery Management System (BMS)** | Monitors voltage, current, temperature, and ensures safe operation. |
| **Inverter/Charger** | Converts DC↔AC and controls power flow between grid, solar, and batteries. |
| **Transfer switch or gateway** | Automatically switches between grid and battery supply. |

## Metric

| **Metric** | **Description** | **Case** |
| --- | --- | --- |
| **Energy Capacity** | Total amount of energy the system can store | kWh for batteries, MWh for grid ESS |
| **Power Rating / Output** | Maximum instantaneous power the system can deliver | kW → MW |
| **Charge/Discharge Rate** | Speed at which the system can charge or discharge | C-rate for batteries (1C = full charge/discharge in 1 hour) |
| **Round-Trip Efficiency** | Fraction of energy recovered vs energy stored | 85–95% for Li-ion, 70–80% for CAES |
| **Cycle Life** | Number of full charge/discharge cycles before capacity drops below threshold | 2000–10000 cycles for Li-ion, 3000–5000 for flow batteries |
| **Depth of Discharge (DoD)** | Percentage of total capacity that can be used safely | 80–90% for Li-ion, 50% for lead-acid |
| **Self-Discharge Rate** | Energy lost per unit time while idle | 1–5% per month for Li-ion, higher for lead-acid |
| **Specific Energy** | Energy stored per unit mass | Wh/kg, important for weight-sensitive applications |
| **Energy Density** | Energy stored per unit volume | Wh/L, relevant for footprint and space |
| **Response Time** | Time to reach full power output | Milliseconds for flywheels, seconds for batteries |
| **Operating Temperature Range** | Temperature limits for safe operation | -20°C → 60°C for Li-ion, higher for NaS |
| **Scalability / Modularity** | Ease of increasing capacity or power by adding modules | Flow batteries and Li-ion systems are highly modular |
| **Cost Metrics** | $/kWh stored, $/kW delivered | $150–400/kWh for Li-ion ESS, $1000+/kWh for pumped hydro |
| **Safety & Reliability** | Risk of failure, thermal runaway, degradation | Fire suppression systems, BMS monitoring, redundancy |
| **Lifetime / Durability** | Years of service under typical operating conditions | 10–20 years for stationary Li-ion ESS |
| **Environmental Impact** | Lifecycle CO₂, recyclability, hazardous material content | Li-ion recycling, lead-acid disposal |

## Storage Economics

> How much does it cost to store a KWh?
> 

## Vendor

| Vendor | Energy Capacity | Power Rating (Output) | Charge Mode | Price |
| --- | --- | --- | --- | --- |
| **OUPES Exodus 1200** | 992 Wh | 1200 W AC (Surge 3600 W), 140 W USB-C | AC, Solar, Car | $549.00 |
| **Jackery Explorer 1000** | 1002 Wh | 1000 W AC (Surge 2000 W), 100 W USB-C | AC, Solar, Car | $999.00 |
| **Bluetti EB70** | 716 Wh | 700 W AC (Surge 1400 W), 100 W USB-C | AC, Solar, Car | $649.00 |
| **Goal Zero Yeti 1000X** | 983 Wh | 1500 W AC (Surge 3000 W), 60 W USB-C | AC, Solar, Car | $1,199.95 |
| **EcoFlow River Pro** | 720 Wh | 800 W AC (Surge 1600 W), 100 W USB-C | AC, Solar, Car | $799.00 |
| **Bluetti AC200P** | 2048 Wh | 2000 W AC (Surge 4800 W), 100 W USB-C | AC, Solar, Car | $1,199.00 |
| **EcoFlow Delta 1300** | 1260 Wh | 1800 W AC (Surge 3300 W), 100 W USB-C | AC, Solar, Car | $1,399.00 |
| **Goal Zero Yeti 3000X** | 3032 Wh | 2000 W AC (Surge 3500 W), 60 W USB-C | AC, Solar, Car | $3,099.95 |

## Electrical Device

> Which are the requirements space for energy power to Electrical Devices?
> 

| Requirement | Description | Note | Case |
| --- | --- | --- | --- |
| **Voltage** | Electrical potential difference required for operation | Usually in volts (V) | 5V for USB devices, 230V for home appliances |
| **Current** | Amount of electric charge per unit time the device draws | Measured in amperes (A) | 0.5A for smartphone chargers, 10A for heaters |
| **Power Rating** | Maximum power consumption | Watts (W) = Voltage × Current | 10W LED bulb, 1500W microwave |
| **Energy Consumption** | Total energy used over time | Kilowatt-hours (kWh) | 0.1 kWh/day for a small appliance |
| **Frequency** | Required AC frequency for device | Hertz (Hz) | 50 Hz in Europe, 60 Hz in the US |
| **Power Factor** | Efficiency of device in using AC power | Cos φ, dimensionless | Important for large motors, not critical for small electronics |
| **Surge Tolerance** | Maximum transient voltage/current device can handle | Protects against spikes | Computers often rated for ±10% voltage variations |
| **Operating Time / Duty Cycle** | Continuous vs intermittent operation | Determines cooling and durability | Industrial motor: continuous; fan: intermittent |
| **Standby Power** | Energy drawn when device is on but idle | Usually small but accumulates | TVs, routers |

## Electrical Device Comparison

| **Requirement** | **Fan** | **Laptop** | **Monitor** |
| --- | --- | --- | --- |
| **Voltage** | 110–230 V AC | 19 V DC (via adapter) | 110–230 V AC (or 12 V DC for some) |
| **Current** | 0.5–2 A | 2–6 A | 0.5–3 A |
| **Power Rating** | 30–100 W | 30–90 W | 20–100 W |
| **Energy Consumption** | ~0.03–0.1 kWh/day | ~0.1–0.5 kWh/day | ~0.05–0.2 kWh/day |
| **Frequency** | 50/60 Hz | N/A (DC device) | 50/60 Hz |
| **Power Factor** | ~0.8–0.9 | ~0.95 | ~0.9 |
| **Surge Tolerance** | ±10% | ±10% | ±10% |
| **Operating Time / Duty Cycle** | Continuous | Intermittent (laptop usage) | Intermittent/Continuous |
| **Standby Power** | <1 W | 1–5 W | 0.5–3 W |

## Stationary Energy Storage Systems (ESS) Evaluation

> How to evaluate the ESS against demand?  Does it met the requirements?
> 

## Security

> Which are the risk? How to mitigate the risks?
> 

## References

- https://www.amazon.com/power-bank/s?k=power%20bank
- https://es.wikipedia.org/wiki/Power_Bank
- https://www.amazon.com/Portable-Station-LiFePO4-Generator-Emergency/dp/B0DN9QHGG8?sp_csd=d2lkZ2V0TmFtZT1zcF9idGY
- https://www.youtube.com/watch?v=IVwR5qJg0zg
- https://oupes.com/
- https://www.pricesmart.com/en-do/product/forza-power-technologies-portable-power-station-titan-series-700-w-2-ac-470200/470200