# POCL

```bash
# ICD:  Means  Installable Client Driver.

## Open CL
export  LLVM_VERSION=14
apt install -y python3-dev libpython3-dev build-essential ocl-icd-libopencl1 cmake git pkg-config libclang-${LLVM_VERSION}-dev clang-${LLVM_VERSION} llvm-${LLVM_VERSION} make ninja-build ocl-icd-libopencl1 ocl-icd-dev ocl-icd-opencl-dev libhwloc-dev zlib1g zlib1g-dev clinfo dialog apt-utils libxml2-dev libclang-cpp${LLVM_VERSION}-dev libclang-cpp${LLVM_VERSION} llvm-${LLVM_VERSION}-dev

## Intel
sudo apt-get install intel-opencl-icd
sudo apt-get install intel-gpu-tools

## AMD
sudo apt install rocm-opencl-runtime
ls /etc/OpenCL/vendors

## Poclcc
sudo apt install libpocl-dev
clinfo
```

## Pocl Architecture

"POCL" stands for "Portable Computing Language," an open-source implementation of the OpenCL standard. OpenCL (Open Computing Language) is a framework for writing programs that execute across heterogeneous platforms, including CPUs, GPUs, DSPs, and more. POCL aims to enhance the portability of OpenCL programs by enabling them to run on more types of hardware and by improving performance on some kinds of CPUs. Here's a brief overview of the architecture of POCL:

1. **Device Support Layer**: POCL implements a device abstraction layer that allows it to interface with various types of hardware. This includes everything from general-purpose CPUs and custom accelerators to GPUs and processors. POCL leverages existing hardware capabilities through device drivers and extensions.
2. **Kernel Compiler**: At the core of POCL is a kernel compiler that translates OpenCL C kernels into the executable machine code for the target device. POCL uses LLVM (Low-Level Virtual Machine) as its primary infrastructure for compiling and optimizing the code. This approach allows POCL to support a wide range of processor architectures effectively.
3. **Runtime Layer**: The runtime layer of POCL handles the execution management of OpenCL kernels. It includes scheduling, memory management, and data transfer between host and devices. The runtime is responsible for setting up the execution environment, managing resources, and ensuring that computations are performed efficiently.
4. **Memory Management**: Efficient memory management is crucial for performance in heterogeneous computing. POCL includes buffer and memory object management mechanisms, which handle the allocation, deallocation, and migration of memory between different computing devices and the host.
5. **Concurrency and Task Management**: POCL implements sophisticated task and concurrency management features to exploit the full potential of hardware resources. This includes support for parallel task execution across multiple cores or devices and synchronization primitives to manage dependencies and resource sharing.
6. **Portability and Extensions**: One of POCL's goals is to be as portable as possible. To achieve this, it adheres to the OpenCL standard and includes support for various extensions that enhance its functionality and performance on non-traditional devices.
7. **Backend Generators**: POCL's modular architecture allows it to target different backends. Depending on the target device's architecture, each backend may have different optimizations and capabilities.

## Pocl Example

```bash
// # matrix_mul.c
// # ...

#include <stdio.h>
#include <stdlib.h>
#include <CL/cl.h>

// Error checking omitted for brevity
int main() {
    // Define matrix size N x N
    int N = 3;
    float A[] = {1, 2, 3, 4, 5, 6, 7, 8, 9}; // Example matrix A
    float B[] = {9, 8, 7, 6, 5, 4, 3, 2, 1}; // Example matrix B
    float C[9]; // Result matrix C

    // Set up OpenCL environment
    cl_platform_id platform;
    cl_device_id device;
    cl_context context;
    cl_command_queue queue;
    cl_program program;
    cl_kernel kernel;

    clGetPlatformIDs(1, &platform, NULL);
    clGetDeviceIDs(platform, CL_DEVICE_TYPE_DEFAULT, 1, &device, NULL);
    context = clCreateContext(NULL, 1, &device, NULL, NULL, NULL);
    queue = clCreateCommandQueue(context, device, 0, NULL);

    // Read kernel file
    FILE* fp = fopen("matrix_mul.cl", "r");
    fseek(fp, 0, SEEK_END);
    size_t kernel_size = ftell(fp);
    rewind(fp);
    char* kernel_src = (char*)malloc(kernel_size + 1);
    fread(kernel_src, 1, kernel_size, fp);
    kernel_src[kernel_size] = '\0';
    fclose(fp);

    // Create and build program
    program = clCreateProgramWithSource(context, 1, (const char**)&kernel_src, NULL, NULL);
    clBuildProgram(program, 1, &device, NULL, NULL, NULL);

    // Create kernel
    kernel = clCreateKernel(program, "matrix_multiply", NULL);

    // Allocate memory for matrices on the device
    cl_mem bufA = clCreateBuffer(context, CL_MEM_READ_ONLY, sizeof(float) * N * N, NULL, NULL);
    cl_mem bufB = clCreateBuffer(context, CL_MEM_READ_ONLY, sizeof(float) * N * N, NULL, NULL);
    cl_mem bufC = clCreateBuffer(context, CL_MEM_WRITE_ONLY, sizeof(float) * N * N, NULL, NULL);

    // Copy matrices to the device
    clEnqueueWriteBuffer(queue, bufA, CL_TRUE, 0, sizeof(float) * N * N, A, 0, NULL, NULL);
    clEnqueueWriteBuffer(queue, bufB, CL_TRUE, 0, sizeof(float) * N * N, B, 0, NULL, NULL);

    // Set the kernel arguments
    clSetKernelArg(kernel, 0, sizeof(cl_mem), &bufA);
    clSetKernelArg(kernel, 1, sizeof(cl_mem), &bufB);
    clSetKernelArg(kernel, 2, sizeof(cl_mem), &bufC);
    clSetKernelArg(kernel, 3, sizeof(int), &N);

    // Execute the kernel
    size_t global_size[2] = {N, N};
    clEnqueueNDRangeKernel(queue, kernel, 2, NULL, global_size, NULL, 0, NULL, NULL);
    
    // Read the matrix back to host memory
    clEnqueueReadBuffer(queue, bufC, CL_TRUE, 0, sizeof(float) * N * N, C, 0, NULL, NULL);

    // Output the result
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            printf("%f ", C[i * N + j]);
        }
        printf("\n");
    }

    // Cleanup
    clReleaseMemObject(bufA);
    clReleaseMemObject(bufB);
    clReleaseMemObject(bufC);
    clReleaseKernel(kernel);
    clReleaseProgram(program);
    clReleaseCommandQueue(queue);
    clReleaseContext(context);
    clReleaseDevice(device);
    free(kernel_src);

    return 0;
}

```

```bash
// # matrix_mul.cl
__kernel void matrix_multiply(const __global float* A, const __global float* B, __global float* C, const int N) {
    int row = get_global_id(0);
    int col = get_global_id(1);
    float sum = 0.0;
    for (int k = 0; k < N; ++k) {
        sum += A[row * N + k] * B[k * N + col];
    }
    C[row * N + col] = sum;
}

```

```bash
gcc -g -o matrix_mul matrix_mul.c -lOpenCL
poclcc matrix_mul.cl 
```

## References

- [http://portablecl.org/downloads.html](http://portablecl.org/downloads.html)
- [Portable Computing Language](http://portablecl.org/)
- [http://portablecl.org/docs/html/pocl_binary.html](http://portablecl.org/docs/html/pocl_binary.html)
- [How do application programs tell the operating system whether to use GPU or CPU to generate graphics?](https://superuser.com/questions/1827872/how-do-application-programs-tell-the-operating-system-whether-to-use-gpu-or-cpu)
- https://en.wikipedia.org/wiki/Standard_Portable_Intermediate_Representation
- https://github.com/pocl/pocl
- …