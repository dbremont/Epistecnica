---
tags: [metric]
---

# Metric


> ..
> 

QA:

- Does high **throughput** imply **low latency**?

## Taxonomy

| **Category** | **Definition** | **Examples** |
| --- | --- | --- |
| **Throughput** | Measures the amount of work a system can complete in a **given time.** | Transactions per second (TPS), Instructions per second (IPS), Requests per second (RPS). |
| **Latency** | Measures the time taken to complete a single operation or task. | Response time, Round-trip time (RTT), Execution time. |
| **Utilization** | Measures how effectively system resources are being used. | CPU utilization, Memory utilization, Disk I/O utilization, Network utilization. |
| **Scalability** | Measures how well the system can handle increased load or resources. | Horizontal scalability, Vertical scalability, Performance under increasing workload. |
| **Reliability** | Measures the system's ability to perform consistently without failure. | Mean Time Between Failures (MTBF), Mean Time To Repair (MTTR), Availability. |
| **Efficiency** | Measures how well the system uses resources to achieve its goals. | Energy efficiency (performance per watt), Resource efficiency, Cost efficiency. |
| **Fairness** | Measures how evenly resources or performance is distributed among users/tasks. | Fairness index (e.g., Jain’s fairness index), Resource allocation fairness. |
| **Overhead** | Measures the additional resources or time required by the system. | Communication overhead, Context-switching overhead, Protocol overhead. |
| **Quality of Service (QoS)** | Measures the system's ability to meet specific performance requirements. | Packet loss rate, Jitter, Throughput guarantees. |
| **Benchmark-Specific Metrics** | Metrics tailored to specific benchmarks or workloads. | SPEC CPU benchmarks, LINPACK, TPC benchmarks (e.g., TPC-C). |
| **Energy and Power Metrics** | Measures the energy consumption and power efficiency of the system. | Power usage (watts), Energy per task (joules per operation), Performance per watt. |
| **Cost Metrics** | Measures the cost-effectiveness of the system. | Total Cost of Ownership (TCO), Cost per transaction, Cost per performance unit (e.g., $/GB/s). |
| **User-Centric Metrics** | Measures the system's performance from the user's perspective. | User response time, Task completion time, User satisfaction (e.g., via surveys). |
| **Fault Tolerance and Recovery** | Measures the system's ability to handle and recover from failures. | Recovery time, Data loss rate, Redundancy effectiveness. |

## Metrics

Here's a more detailed table that includes specific monitoring metrics for various components of a system, the thresholds that, when exceeded, will trigger alerts, the level of severity of those alerts, and the method by which the data is collected:

| Component | Metric | Threshold | Alert Level |
| --- | --- | --- | --- |
| CPU | Usage | > 85% | Critical |
| CPU | Clock Speed (GHz) |  |  |
| CPU | Core Count |  |  |
| CPU | Thread Count |  |  |
| CPU | Cache Size (MB) |  |  |
| CPU | Power Consumption (W) |  |  |
| CPU | Temperature (°C) |  |  |
| CPU | Utilization (%) |  |  |
| CPU | Instructions per Second (IPS) |  |  |
| CPU | Floating Point Operations per Second (FLOPS) |  |  |
| CPU | Instructions per Clock (IPC) |  |  |
| CPU | Cycles per Instruction (CPI) |  |  |
| **Data Center** | Power Usage Effectiveness (PUE) |  |  |
| **Data Center** | Data Throughput (Gbps) |  |  |
| **Data Center** | Network Latency (ms) |  |  |
| **Data Center** | Storage Utilization (%) |  |  |
| **Data Center** | Cooling Efficiency (%) |  |  |
| **Data Center** | Uptime (%) |  |  |
| **Data Center** | Energy Consumption (kWh) |  |  |
| **Data Center** | Carbon Footprint (CO2 Emission) |  |  |
| Memory | Utilization | > 75% | High |
| GPU | Clock Speed (MHz) |  |  |
| GPU | Core Count |  |  |
| GPU | Shader Units |  |  |
| GPU | Tensor Cores (if applicable) |  |  |
| GPU | Streaming Multiprocessors (SMs) |  |  |
| GPU | Power Consumption (W) |  |  |
| GPU | Utilization (%) |  |  |
| GPU | Floating Point Operations per Second (FLOPS) |  |  |
| GPU | Tensor Operations per Second (TOPS) |  |  |
| GPU | Ray Tracing Cores (if applicable) |  |  |
| **Graphics Card** |  |  |  |
| **Graphics Card** | Frame Rate (FPS) |  |  |
| **Graphics Card** | Video Output Ports (HDMI, DisplayPort, etc.) |  |  |
| **Graphics Card** | Memory Type (GDDR6, HBM2, etc.) |  |  |
| **Graphics Card** | TDP (Thermal Design Power, W) |  |  |
| **Graphics Card** | PCIe Interface (x16, x8) |  |  |
| **Graphics Card** | DirectX/OpenGL Version Support |  |  |
| **Graphics Card** | Video RAM (VRAM, GB) |  |  |
| **Graphics Card** | GPU Boost Clock (MHz) |  |  |
| Disk | Read/Write IOPS | > 10,000 IOPS | Warning |
| Disk | Usage | > 90% | Critical |
| Network Interface | Throughput | < 100 Mbps | Warning |
| Network Interface | Packet Loss | > 1% | High |
| Database | Query Latency | > 1 sec | High |
| Database | Connection Timeouts | > 10 per hour | Critical |
| Application | Response Time | > 2 sec | High |
| Application | Error Rate | > 0.1% | Critical |
| Server Temperature | Temperature | > 80°C (176°F) | Critical |
| Power Supply | Power Fluctuations | Any fluctuation | Critical |
| Software System | **Throughput** |  |  |
| Software System | Number of simultaneous users or tasks the system can handle. |  |  |
| Software System | Page Load Time |  |  |
| Software System | User Sessions |  |  |
| … | … |  |  |