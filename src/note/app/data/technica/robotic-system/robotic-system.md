# Robotic System

> How to characterie the robotics problem?    Robotic Ssytem: Actuacotr, Goal, Internal Cojmputation
> 

→ Software + Electro Mechanics

> **Note:** Robotics is not just the next big thing — understanding it is no longer optional but essential.
> 

> **Note:** This is actually a derivative system; but it’s too important not to be in the front sea.
> 

> **Electricity Based Systems are winning the race against thermodynamics based one.**
> 

> **Robotics engineering** involves designing, building, and programming robots to perform tasks autonomously or with human interaction, often integrating elements of mechanical, electrical, and computer engineering.
> 

> **Automation engineering** involves the design, development, and implementation of systems and processes to automatically control and monitor various industrial and technological tasks, optimizing efficiency and reducing human intervention.
> 

QA:

- What is the simplest project to start in robotics? It’s start a project with quadcopter or something related to drones?’

## Formulation

## **1. Robot System Definition**

Let a robot be represented as a tuple:

[

\mathcal{R} = (S, A, C)

]

Where:

- (S) = **State space** — all possible states of the robot and possibly parts of the environment it can observe
- (A) = **Action space (Actuators)** — all actions the robot can perform
- (C: S \to A) = **Control / Computation function** — maps states (or observations) to actions

---

## **2. Environment**

Let the environment be:

[

\mathcal{E} = (X, T)

]

Where:

- (X) = Environment state space
- (T: X \times A \to X) = **Transition function** describing how actions change the environment

---

## **3. Sensor Model**

The robot perceives the environment through sensors:

[

O: X \to S

]

- (O) = Observation function mapping environment states to perceived states
- Can include noise: (s_t = O(x_t) + \epsilon)

---

## **4. Goal Specification**

The goal is defined as a **cost or reward function**:

[

G: S \times A \to \mathbb{R}

]

- Can be generalized as a **utility function** to maximize (or a cost function to minimize)
- Encodes task success, constraints, and preferences

---

## **5. Robot Problem Statement**

Given:

- Robot (\mathcal{R} = (S, A, C))
- Environment (\mathcal{E} = (X, T))
- Observation function (O)
- Goal function (G)

Find a control function (C^*) such that the robot selects actions (a_t = C^*(s_t)) over time (t = 0 \dots T) to **maximize cumulative reward** (or achieve goal) while respecting system and environment constraints:

[

C^* = \arg\max_{C} \sum_{t=0}^{T} G(s_t, a_t)

]

Subject to:

[

\begin{cases}

s_t = O(x_t) \

x_{t+1} = T(x_t, a_t) \

a_t \in A, \ s_t \in S, \ x_t \in X

\end{cases}

]

---

This formalization covers:

- **Actuators** → (A)
- **Internal Computation** → (C)
- **Goal** → (G)
- **Environment** → ((X, T))
- **Sensors** → (O)

## Skill Map

| **Domain** | **Skill** | **Description** |
| --- | --- | --- |
| **Programming** | Embedded systems | Programming microcontrollers and interfacing with hardware. |
|  | Algorithm design | Designing efficient computational procedures for robotic tasks. |
|  | Real-time programming | Writing time-critical code with strict execution deadlines. |
| **Control Systems** | PID control | Tuning and implementing proportional-integral-derivative feedback controllers. |
|  | Adaptive control | Dynamically adjusting control parameters in real-time based on system changes. |
|  | State estimation | Inferring unobservable internal states from sensor data. |
|  | System identification | Modeling systems by observing their inputs and outputs. |
| **Kinematics & Dynamics** | Forward kinematics | Computing end-effector position from joint parameters. |
|  | Inverse kinematics | Determining joint parameters to reach a target position. |
|  | Rigid body dynamics | Modeling motion and force of mechanical systems. |
| **Perception** | Computer vision | Extracting information from images or video. |
|  | LIDAR/IMU integration | Combining data from LIDAR and inertial sensors. |
|  | Sensor fusion | Merging multiple sensor inputs for better accuracy and robustness. |
| **AI & ML** | Path planning | Computing collision-free and optimal movement trajectories. |
|  | Reinforcement learning | Learning behavior via trial and error in an environment. |
|  | Object recognition | Identifying and classifying objects in sensor data. |
| **Hardware Integration** | Wiring and soldering | Building electrical connections for robotic systems. |
|  | PCB design | Designing custom printed circuit boards for specific robotic applications. |
|  | Motor control | Controlling speed, position, and torque of motors. |
|  | Encoders and actuators | Measuring motion and converting control signals into physical movement. |
| **Mechatronics** | CAD design | Designing mechanical components in 3D. |
|  | Mechanism design | Creating mechanical linkages and movement systems. |
|  | Mechatronic integration | Merging electronics, control, and mechanical parts into a unified system. |
| **Embedded Systems** | RTOS fundamentals | Understanding real-time operating system principles. |
|  | Low-level interfacing | Communicating directly with hardware peripherals. |
|  | Bootloaders and memory mapping | Managing startup routines and memory layout in embedded platforms. |
| **Networking & Comms** | TCP/IP, UART, SPI, I2C | Using standard protocols for data transfer between components. |
|  | Robot-to-robot communication | Exchanging data directly between multiple robotic agents. |
|  | Robot-to-server communication | Connecting robots to remote systems or servers for control and telemetry. |
| **Simulation & Testing** | Physics-based simulation | Emulating robotic behavior in virtual environments. |
|  | Hardware-in-the-loop (HIL) | Integrating real hardware with simulated systems for testing. |
| **Safety & Reliability** | Fault-tolerance | Designing systems that continue operating after partial failures. |
|  | Redundancy | Including backups to improve system reliability. |
|  | Risk analysis | Evaluating potential hazards and failure modes. |
| **Systems Engineering** | Requirements specification | Defining functional and technical needs for a robotic system. |
|  | Systems integration | Combining subsystems into a cohesive operational whole. |
|  | Verification and validation | Ensuring the system meets specifications and performs as intended. |

## Robot Parts

| **Functional Layer** | **Subsystem** | **Component** | **Notes** |
| --- | --- | --- | --- |
| **Control & Computation** | Central Processing | CPU, MCU, SoC, FPGA | Main control unit |
|  | Memory & Storage | RAM, Flash, EEPROM, SSD | Runtime + program data |
|  | Communication Buses | I²C, SPI, CAN, UART, USB, Ethernet | Internal/external signaling |
|  | OS & Middleware | RTOS, ROS, DDS, Custom Frameworks | Software backbone |
|  | AI & Decision Logic | ML Engines, Behavior Trees, FSMs | Autonomy and decision-making |
| **Actuation** | Locomotion | Wheels, Tracks, Legs, Rotors | Movement systems |
|  | Manipulation | Robotic Arms, Grippers, End Effectors | Interacting with environment |
|  | Actuators | Servo Motors, Stepper Motors, Pneumatic Actuators | Mechanical action |
|  | Power Transmission | Gears, Belts, Shafts, Linkages | Motion transfer |
|  | Compliance Devices | Springs, Dampers, Torque Sensors | Mechanical adaptability |
| **Perception (Sensors)** | Vision | RGB Cameras, Depth Cameras, Stereo, IR | Visual perception |
|  | Proximity | LIDAR, Ultrasonic, Infrared Sensors | Obstacle detection |
|  | Positioning | IMU, GPS, Wheel Encoders | Localization |
|  | Tactile | Force Sensors, Touch Sensors, Tactile Arrays | Physical interaction sensing |
|  | Audio | Microphones, Acoustic Sensors | Sound perception |
|  | Environment Sensing | Gas, Temperature, Humidity, Light Sensors | Contextual awareness |
| **Energy & Power** | Power Source | Batteries, Fuel Cells, External Power Supply | Energy input |
|  | Power Regulation | Voltage Regulators, BMS, Fuses | Voltage/current control |
|  | Power Distribution | PCBs, Connectors, Switches, Rails | Deliver power to subsystems |
| **Mechanical Structure** | Frame & Chassis | Base Structure, Mounts, Housings | Structural support |
|  | Kinematic Chain | Links, Revolute/Prismatic Joints | Mobility structure |
|  | Enclosure | Covers, Weatherproof Casings | Environmental protection |
|  | Mobility Platform | Wheels, Tracks, Landing Gear | Base locomotion |
| **Interface & Communication** | Human Interface | Screens, Buttons, Speakers, LEDs | Human–robot interaction |
|  | Wireless Comm | Wi-Fi, Bluetooth, ZigBee, 5G, LoRa | Telemetry and remote control |
|  | Cloud Interface | MQTT, ROSBridge, REST APIs | Backend integration |
|  | Safety Interface | Emergency Stop, Kill Switch, Safety Relays | Protection mechanisms |
| **Software & Logic** | Navigation | SLAM, Path Planning, Obstacle Avoidance Algorithms | Spatial awareness |
|  | Control Algorithms | PID, MPC, RL, Feedforward Controllers | Motion control |
|  | Task Planning | Task Trees, Automated Planning Graphs | High-level logic |
|  | Perception Software | Object Detection, Feature Extraction, Filtering | Process sensor data |
|  | Simulation | Gazebo, Webots, PyBullet, V-REP | Testing/virtual environments |
|  | Diagnostics | Self-Test Routines, Logs, Alerts, Error Codes | System health and feedback |

## Study Plan

- [ ]  https://github.com/henki-robotics/robotics_essentials_ros2
- [ ]  https://news.ycombinator.com/item?id=44158353
- [ ]  https://news.ycombinator.com/item?id=8495786
- [ ]  https://news.ycombinator.com/item?id=25608932
- [ ]  https://news.ycombinator.com/item?id=30099347

## Kits

- https://dorna.ai/
- https://www.ufactory.cc/#/en/swiftPro
- https://open-arm.org/
- https://mujoco.org/
- https://github.com/janesmae/awesome-drones
- https://diydrones.com/
- https://nuttx.apache.org/
- https://docs.px4.io/main/en/
- https://dronecode.org/
- https://genesis-embodied-ai.github.io/
- https://opensourceleg.org/
- https://docs.qgroundcontrol.com/master/en/
- **ROS (Robot Operating System)** – middleware for control, kinematics, vision
- **MoveIt!** – motion planning
- **Gazebo / Webots** – simulation
- **OpenCV** – vision + object tracking

## Sensors

> 

## Open Problems

> https://news.ycombinator.com/item?id=24207424
> 

## Conceptual Model

Automatum: Conceptual Model

## References

- [Robotics](https://en.wikipedia.org/wiki/Robotics)
- [Industrial robot](https://en.wikipedia.org/wiki/Industrial_robot)
- [Solid Works](https://www.solidworks.com/)
- https://www.tsungxu.com/p/quadcopter-vision?triedRedirect=true
- The End of Starsky Robotics ([medium.com/starsky-robotics-blog](http://medium.com/starsky-robotics-blog))
[https://news.ycombinator.com/item?id=22629023](https://news.ycombinator.com/item?id=22629023)
- Getting Started in Robotics ([allshire.org](http://allshire.org/))
[https://news.ycombinator.com/item?id=25608932](https://news.ycombinator.com/item?id=25608932)
- My adventures in CNC robotics ([coredump.cx](http://coredump.cx/))
[https://news.ycombinator.com/item?id=8495786](https://news.ycombinator.com/item?id=8495786)
- Open Problems in Robotics ([scottlocklin.wordpress.com](http://scottlocklin.wordpress.com/))
[https://news.ycombinator.com/item?id=24207424](https://news.ycombinator.com/item?id=24207424)
- Getting into robotics as a software engineer ([bou.ke](http://bou.ke/))
[https://news.ycombinator.com/item?id=39325110](https://news.ycombinator.com/item?id=39325110)
- Deep Learning in Robotics: A Review of Recent Research ([arxiv.org](http://arxiv.org/))
[https://news.ycombinator.com/item?id=14846399](https://news.ycombinator.com/item?id=14846399)
- Low Cost Robot Arm ([github.com/alexanderkoch-koch](http://github.com/alexanderkoch-koch))
[https://news.ycombinator.com/item?id=39902205](https://news.ycombinator.com/item?id=39902205)
- PAROL6 robotic arm + LEAP motion controller
[https://x.com/SourceRobotics/status/1819037417640206837](https://x.com/SourceRobotics/status/1819037417640206837)
- PAROL6 Robotic arm KIT
[https://source-robotics.com/products/parol6-robotic-arm-kit](https://source-robotics.com/products/parol6-robotic-arm-kit)
- [‣](https://app.notion.com/p/10e598edb79081d69eabee728e9678b9?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081028d64f10d4e56045e?pvs=21)
- [‣](https://app.notion.com/p/10e598edb790818ab587ca90d3c79cff?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081cf9756f09c8a06a076?pvs=21)
- [‣](https://app.notion.com/p/10e598edb7908158a1dbfe3021c11216?pvs=21)
- [‣](https://app.notion.com/p/140c0f5171ec804eba5bd5581c8fe8cf?pvs=21)
- https://news.ycombinator.com/item?id=28906333
- https://news.ycombinator.com/item?id=22629023
- https://news.ycombinator.com/item?id=41600177
- https://en.wikipedia.org/wiki/Servomotor
