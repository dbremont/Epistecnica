---
tags: [miscellanea, model]
---

# A Case Study of a Dissipative System: Damped Pendulum

> In an ideal, undamped pendulum, once you set it in motion, it would swing back and forth forever with a constant amplitude. However, in the real world, various forces like air resistance and friction at the pivot point act to dissipate the mechanical energy of the system. This means the amplitude of the oscillations gradually decreases over time until the pendulum eventually comes to rest. This loss of energy to the surroundings (usually as heat) is the hallmark of a dissipative system.
>

## Index

## **Mathematical Model**

### 🧮 Differential Equation

$\frac{d^2\theta}{dt^2} + \gamma \frac{d\theta}{dt} + \frac{g}{L} \sin(\theta) = 0$

### ⚙️ Model Parameters

| Parameter | Description | Units |
| --- | --- | --- |
| $\theta$ | Angular displacement from vertical | radians |
| $\frac{d\theta}{dt} = \omega$ | Angular velocity | radians/second |
| $\frac{d^2\theta}{dt^2}$ | Angular acceleration | radians/second² |
| $\gamma$ | Damping coefficient (viscous damping) | 1/second |
| $g$ | Acceleration due to gravity | meters/second² |
| $L$ | Length of the pendulum | meters |

### 📌 Interpretation of Each Term

- **$\frac{d^2\theta}{dt^2}$**: Inertia — how quickly the pendulum's angle is changing.
- **$\gamma \frac{d\theta}{dt}$**: Damping — energy lost due to friction or air resistance; proportional to angular velocity.
- **$\frac{g}{L} \sin(\theta)$**: Restoring torque from gravity — tries to pull the pendulum back to vertical (nonlinear because of sin⁡(θ)\sin(\theta)).

### 🧪 Effect of Parameters

- Increasing **$\gamma$** → more damping → faster decay of motion.
- Increasing **$L$** → slower oscillations (longer period).
- Increasing **$g$** → faster oscillations (shorter period).

## ✅ Python Code

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
g = 9.81      # gravitational acceleration (m/s^2)
L = 1.0       # length of pendulum (m)
gamma = 0.5   # damping coefficient

# Differential equation system
def damped_pendulum(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -gamma * omega - (g / L) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Initial conditions
theta0 = np.pi / 3  # 60 degrees
omega0 = 0.0        # initial angular velocity
y0 = [theta0, omega0]

# Time span
t_span = (0, 10)
t_eval = np.linspace(*t_span, 1000)

# Solve ODE
sol = solve_ivp(damped_pendulum, t_span, y0, t_eval=t_eval)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(sol.t, sol.y[0], label=r'$\theta(t)$ (angle)')
plt.plot(sol.t, sol.y[1], label=r'$\omega(t)$ (angular velocity)', linestyle='--')
plt.title('Damped Nonlinear Pendulum')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.show()
```

## Provenance

- Notion export: `Modelo/Miscellanea/Miscellanea/A Case Study of a Dissipative System Damped Pendul 1ebc0f5171ec80c09a6af45b6f968c2b.md`
