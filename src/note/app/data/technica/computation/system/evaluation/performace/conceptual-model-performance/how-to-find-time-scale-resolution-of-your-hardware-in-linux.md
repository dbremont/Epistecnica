---
tags: [how-to]
---

# How to Find Time Scale Resolution of Your Hardware in Linux?

- [CSBB: Hardware](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/csbb-hardware.md)

You can determine your system's timing resolution using several Linux tools and techniques. Here are the most effective methods:

## Interpreting Results

> Note: `Core 0: 1929.600 MHz`  →  `Cycle time = 1 / frequency = 1 / 4,341,814,000 Hz ≈ 0.2303 nanoseconds (230.3 picoseconds)`.
> 

> 
1. **CPU Cycle Time**: Modern CPUs typically have 0.2-0.5 ns resolution (2-5 GHz)
2. **System Timer Resolution**: Usually 1 ns (TSC) to 1000 ns (1 μs for older HPET)
3. **Kernel Tick Rate**: Typically 250 Hz (4 ms) to 1000 Hz (1 ms)
4. **Sleep Granularity**: `nanosleep()` can reach ~50-100 ns on modern systems

## 1. Check CPU Clock Speed and Cycle Time

```bash
# Check CPU frequency (shows current and max speed)
cat /proc/cpuinfo | grep "MHz"

# More detailed CPU info including base frequency
lscpu

# Calculate cycle time (1/frequency)
# Example for 2.4 GHz CPU: 1/2,400,000,000 = 0.416 nanoseconds
echo "scale=10; 1/($(lscpu | grep "CPU max MHz" | awk '{print $4}')*1000000)" | bc

```

## 2. Check System Timer Resolution

```bash
# Check available clocksources (usually tsc or hpet)
cat /sys/devices/system/clocksource/clocksource0/current_clocksource

# Check timer resolution (in nanoseconds)
sudo apt install pmtools
pmtimer -r

# Alternative method
cat /proc/timer_list | grep resolution | head -n 1

```

## 3. Measure Actual Timing Granularity

```c
#include <stdio.h>
#include <time.h>

int main() {
    struct timespec res;
    clock_getres(CLOCK_MONOTONIC, &res);
    printf("System clock resolution: %ld ns\\n", res.tv_nsec);
    return 0;
}

```

Compile and run with:

```bash
gcc timer_res.c -o timer_res && ./timer_res

```

## 4. Check Kernel Tick Rate

```bash
# Check HZ value (kernel timer frequency)
grep CONFIG_HZ= /boot/config-$(uname -r)

# Or check actual tick rate
grep "jiffies" /proc/timer_list | head -n 1

```

## 5. Advanced Hardware Timing (Requires Root)

```bash
# Check TSC (Time Stamp Counter) frequency
sudo dmidecode -t processor | grep -i "speed"

# Check HPET (High Precision Event Timer) capabilities
sudo cat /sys/kernel/debug/hpet/*

# Check RDTSC resolution (cycle-accurate timing)
sudo modprobe msr
sudo rdmsr 0x10

```

```bash
sudo apt install rt-tests
cyclictest --nanosleep -t1 -p80 -n -i 1000 -l 10000

```

## References

- [‣](https://app.notion.com/p/fe6e9732f0ce4104b49c95bc3e106a70?pvs=21)
- [Time](note.html?n=technica/computation/miscelanea/time.md)
- https://gist.github.com/sandeep-mg/06183efdc89b4cc6ae244b9967f7c9cc
- https://man.archlinux.org/man/cyclictest.8.en
- https://www.passmark.com/
- https://github.com/resurrecting-open-source-projects/stress?tab=readme-ov-file