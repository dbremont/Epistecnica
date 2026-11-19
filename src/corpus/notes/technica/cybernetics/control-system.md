---
tags: [note, control, cybernetics, automation, technique]
---

# Control System

> A **control system** is an arrangement that drives a plant's output toward a reference by measuring the error and acting on it. The version every other engineering discipline inherits is the **feedback loop**: reference → controller → actuator → plant → sensor → error → controller. Everything else — PID, stability theory, SCADA — is elaboration of that circuit.

## The loop

| Element | Function | What fails without it |
| --- | --- | --- |
| **Reference** (setpoint) | The value the output should take | No error signal exists, so no control |
| **Sensor / measurement** | Reads the actual output | The controller is open-loop: it acts without knowing the result |
| **Controller** | Computes the action from the error | The loop has a signal but no decision |
| **Actuator** | Applies the action to the plant | The decision has no effect |
| **Plant** (process) | The system being controlled | — |
| **Disturbance** | What the loop must reject | The design has no reason to be feedback at all |

## The taxonomy

| Type | Principle | Typical instance |
| --- | --- | --- |
| **Open-loop** | Acts on a schedule, never measures the output | Timers, stepper positioning, batch recipes |
| **Closed-loop (feedback)** | Corrects in proportion to the measured error | Thermostats, motor drives, process loops |
| **Feedforward** | Acts on a measured disturbance before it reaches the output | Boiler feedwater, dead-time compensation |
| **Cascade** | A fast inner loop serves a slow outer loop | Flow loop inside a temperature loop |
| **Sequential / discrete** | Steps through states and interlocks, not a continuous variable | PLC machine sequencing, safety interlocks |
| **Model-based (MPC)** | Optimises the inputs over a prediction horizon | Refineries, power plants, large HVAC |
| **Supervisory** | Sets the targets and monitors the loops beneath | SCADA, DCS |

> The timescales are the real taxonomy: a motor current loop closes in microseconds, a temperature loop in seconds, a supervisory layer in minutes. Choosing the wrong layer for a problem is the classic design error — a fast loop cannot fix a slow disturbance, and a supervisory system cannot replace a stabilising controller.

## PID, the working core

| Term | Acts on | What it contributes | What too much of it costs |
| --- | --- | --- | --- |
| **Proportional** (P) | The present error | Speed of response | Offset remains; large gain causes oscillation |
| **Integral** (I) | The accumulated error | Eliminates the steady-state offset | Windup and slow oscillation |
| **Derivative** (D) | The rate of change of error | Damping, anticipation | Amplifies measurement noise |

> The tuning trade is the whole discipline in miniature: **speed against stability**. A loop tuned for fast response overshoots and rings; a loop tuned for robustness is slow to reject disturbances. The margins (gain and phase) are the formal statement of how much of either is left.

## SCADA

> **SCADA** — supervisory control and data acquisition — is the layer above the loops: it does not stabilise anything, it **supervises**. Field devices (PLCs, RTUs, smart instruments) run the local control; telemetry carries their state to a control centre; an HMI presents it; alarms, trends and a historian record it; operators issue setpoints and commands down the same path.

| Layer (Purdue / ISA-95) | What lives there | Timescale |
| --- | --- | --- |
| **0 — Process** | Sensors and actuators | Microseconds to seconds |
| **1 — Basic control** | PLCs, loop controllers, safety systems | Milliseconds to seconds |
| **2 — Supervisory** | SCADA, HMI, alarms, historian | Seconds to minutes |
| **3 — Operations management** | Production scheduling, maintenance | Hours to days |
| **4 — Business planning** | ERP, enterprise systems | Days to months |
| **5 — Enterprise / external** | Corporate and external networks | — |

> Two consequences follow from the layer model. **Control must not depend on the network**: a PLC keeps a plant safe when the SCADA link is down, and a design where the loop needs the control centre is a design with a single point of failure. **And SCADA is operational technology wired to physical processes** — the "air gap" is a myth in any plant that also wants remote access and business integration, which is why its security is a physical-safety problem, not a data-confidentiality one.

## References

- [Control system — Wikipedia](https://en.wikipedia.org/wiki/Control_system)
- [SCADA — Wikipedia](https://en.wikipedia.org/wiki/SCADA)
- [Automation Regime](/view.html?p=notes/technica/production/industry/automation-regime.md) — the regime the control system instantiates
- [System](/view.html?p=notes/technica/cybernetics/system/system.md) — the cybernetic reading of the plant
- [Robotic System](/view.html?p=notes/technica/robotics/robotic-system.md) — the control loop with a body
- [Observation Technology and Method Catalog](/corpus/notes/epistemica/observation/organon.html) — the sensor side of the loop
