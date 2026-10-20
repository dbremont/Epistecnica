---
tags: [debug]
---

# Debug


> Debugging is the process of identifying and resolving defects or errors in software code.
> 

 The main ideas in debugging and the papers that contributed to them are:

- Systematic Debugging: This approach involves using a systematic method to identify the root cause of an error in the code. Andreas Zeller’s paper “Why Programs Fail: A Guide to Systematic Debugging” introduced this approach and emphasized the importance of automated tools for debugging.
- Stepwise Refinement: This is a method of breaking down a complex problem into simpler sub-problems that can be solved incrementally. Niklaus Wirth’s paper “Program Development by Stepwise Refinement” introduced this concept and its application to debugging.
- Debugging Psychology: Debugging is a mental process, and it is influenced by various psychological factors. Robert K. Blum’s paper “The Psychology of Debugging” explores the psychological aspects of debugging, such as problem-solving strategies and cognitive biases.
- Fault Localization: This approach involves identifying the location of an error in the code. Spiros M. Mancoridis’ paper “The Tarantula Approach to Fault Localization” introduced the Tarantula technique for localizing faults in software code by analyzing test coverage and the correlation between passing and failing test cases.
- Crowdsourced Debugging: This approach involves harnessing the power of crowdsourcing to assist in debugging. Yuxiong He’s paper “CrowdDebugging: Harnessing the Power of Crowdsourced Testing” explores the use of crowdsourcing to identify and fix software bugs.
- Differential Testing: This technique involves comparing the behavior of two versions of a program to identify differences that could indicate the presence of a bug. Hao Chen’s paper “Difftest: Differential Testing for Sequential Programs” introduced this technique for detecting bugs in software code.

## References

- [The Debugging Book Tools and Techniques for Automated Software Debugging](https://www.debuggingbook.org/)
- Gilmore, D. J. (1991). Models of debugging. 78(1–3), 151–172.
- Araki, K., Furukawa, Z., & Cheng, J. (1991). A general framework for debugging. 8(3), 14–20.
- Huang, J., & Zhang, C. (2011). An efficient static trace simplification technique for debugging concurrent programs. 163–179.
- McDowell, C. E., & Helmbold, D. P. (1989). Debugging concurrent programs. 21(4), 593–622.
- Qi, D., Roychoudhury, A., Liang, Z., & Vaswani, K. (2012). Darwin: An approach to debugging evolving programs. 21(3), 1–29.
- Law, R. (1997). An overview of debugging tools. 22(2), 43–47
- Kocher, W. (1969). A survey of current debugging concepts.
- Gazzola, L., Micucci, D., & Mariani, L. (2018). Automatic software repair: A survey. 1219.
- Designing the whyline: a debugging interface for asking questions about program behavior https://dl.acm.org/doi/abs/10.1145/985692.985712
- Models of debugging https://www.sciencedirect.com/science/article/abs/pii/000169189190009O
- Debugging concurrent programs https://dl.acm.org/doi/abs/10.1145/76894.76897
- GDB https://www.sourceware.org/gdb/current/onlinedocs/gdb.pdf
- [How debbuggers works](http://www.alexonlinux.com/how-debugger-works)
- [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/)
- [TED: The Tiny Exfiltrating Debugger](https://www.codereversing.com/archives/561)

[GDB (GNU Project Debugger)](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/gdb-gnu-project-debugger.md)

[ELF (Executable and Linkable Format)](note.html?n=technica/computation/language-system/conceptual-model-language-system/elf-executable-and-linkable-format.md)