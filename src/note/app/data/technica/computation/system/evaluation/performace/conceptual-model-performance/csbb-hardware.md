---
tags: [system]
---

# CSBB: Hardware

- [How to Find Time Scale Resolution of Your Hardware in Linux?](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/how-to-find-time-scale-resolution-of-your-hardware-in-linux.md), [CSBB: Linux](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/csbb-linux.md)

QA:

- How to **Characterize** the Hardware?
- …

### How to Infer Hardware Capabilities from Workload Performance

You can analyze your hardware's capabilities by carefully observing how it handles different types of workloads. Here's a systematic approach:

---

## **CPU Capabilities**

### **Key Metrics to Monitor**

- **Single-Thread Performance**
    
    ```bash
    taskset -c 0 stress-ng --cpu 1 --cpu-method matrixprod --metrics-brief --timeout 60
    
    ```
    
    - Check sustained clock speed (`watch -n 0.5 "cat /proc/cpuinfo | grep 'MHz'"`)
    - Compare against base/boost specs
- **Multi-Core Scaling**
    
    ```bash
    stress-ng --cpu $(nproc) --cpu-method fft --metrics-brief --timeout 60
    
    ```
    
    - Monitor frequency drops due to thermal/power limits
    - Check scaling efficiency:
        
        ```bash
        perf stat -e cycles,instructions -a -- sleep 5
        
        ```
        

### **What to Look For**

- Sustained all-core boost frequency
- Thermal throttling patterns (`sensors`)
- IPC (Instructions Per Cycle) differences between workloads

---

## **Memory Subsystem**

### **Benchmark Tools**

```bash
# RAM bandwidth
sudo apt install mbw
mbw -n 5 256

# Cache hierarchy performance
sudo apt install lmbench
cachebench

```

### **Key Observations**

- Cache latencies (L1/L2/L3)
- Memory bandwidth saturation points
- NUMA effects (if multi-socket):
    
    ```bash
    numactl --hardware
    numactl --preferred=1 stress-ng --vm 2 --vm-bytes 10G
    
    ```
    

---

## **Storage I/O Capabilities**

### **Workload Tests**

```bash
# Raw sequential throughput
fio --name=seqread --rw=read --direct=1 --ioengine=libaio --bs=1M --numjobs=4 --size=1G --runtime=60

# Random IOPS capability
fio --name=randrw --rw=randrw --direct=1 --ioengine=libaio --bs=4k --numjobs=16 --iodepth=32 --size=1G --runtime=60

```

### **Analysis Points**

- Compare against device specs (NVMe/SATA)
- Queue depth scaling behavior
- Cache effects (repeat tests with O_DIRECT)

---

## **Network Performance**

- **Throughput & Latency:** `iperf3 -s` (server) & `iperf3 -c <IP>` (client)
- **Packet Loss & Jitter:** `ping -c 10 <destination>`, `netstat -s`
- **TCP/UDP Behavior:** `ss -tuan`, `tcpdump -i eth0`

## **GPU/Accelerator Performance**

```bash
# OpenCL capability
sudo apt install clinfo
clinfo | grep "Max compute units"

# CUDA (if NVIDIA)
nvidia-smi --query-gpu=clocks.max.gr,memory.total --format=csv

```

### **Workload Testing**

```bash
# Example with OpenCL
sudo apt install beignet-dev
clpeak

```

## **Power & Thermal Analysis**

- **Power Consumption:** `powertop`, `turbostat` (Intel), `rapl` (Running Average Power Limit)
- **Temperature Monitoring:** `sensors` (from `lm_sensors`), `watch -n 1 cat /sys/class/thermal/thermal_zone*/temp`

## **System-Wide Characterization**

### **Simulate Real Workloads**

```bash
# Mixed CPU/memory/IO load
stress-ng --cpu 4 --io 2 --vm 1 --vm-bytes 4G --timeout 120s

```

### **Monitoring Tools**

```bash
# Comprehensive view
sudo apt install intel-gpu-tools # For Intel graphics
htop
iotop -o
nmon
glances

```

---

## **Interpreting Results**

1. **Frequency vs. Utilization Curves**
    - Plot clock speed against load percentage
    - Identify power/thermal limits
2. **Bottleneck Analysis**
    - `perf stat` for CPU-bound workloads
    - `iostat -x 1` for storage limits
    - `dstat -cdngy` for system-wide view
3. **Compare Against Specifications**
    
    ```bash
    lshw -short
    dmidecode -t processor
    
    ```
    
4. **Thermal Constraints**
    
    ```bash
    watch -n 1 "cat /sys/class/thermal/thermal_zone*/temp"
    
    ```
    

---

## **Advanced Techniques**

- **CPU Microarchitecture Analysis**
    
    ```bash
    perf list | grep cache
    perf stat -e cache-misses,cache-references -a sleep 5
    
    ```
    
- **Memory Controller Utilization**
    
    ```bash
    perf stat -e uncore_imc_0/cas_count_read/,uncore_imc_0/cas_count_write/ -a -- sleep 5
    
    ```
    
- **PCIe Lane Verification**
    
    ```bash
    lspci -vv | grep -i width
    
    ```
    

By correlating workload performance with these measurements, you can build a detailed profile of your hardware's true capabilities beyond manufacturer specs. For precise comparisons, always:

- Control for thermal conditions
- Disable frequency scaling during tests (`cpupower frequency-set --governor performance`)
- Repeat measurements to account for variability