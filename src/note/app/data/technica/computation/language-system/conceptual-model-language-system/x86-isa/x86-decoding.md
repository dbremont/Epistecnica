# x86 Decoding

> 

No, you cannot always decode an x86 instruction deterministically without additional context due to its variable-length encoding, overlapping opcodes, and state-dependent prefixes (e.g., `REX`, `VEX`, `EVEX`, segment overrides, operand-size overrides), meaning a given byte sequence may be interpreted differently depending on:

1. **Current mode** (real/protected/long mode, 16/32/64-bit operand/address size).
2. **Prefix state** (e.g., `0x66`, `0x67`, `LOCK`, `REP`, `REX` modifying opcode semantics).
3. **Undocumented/illegal opcodes** (some sequences behave unpredictably or trap).
4. **Speculative execution effects** (some bytes may be consumed incorrectly before #UD).

Thus, x86 decoding is ***context-sensitive***—some byte streams (e.g., `0xF0 0xC3` as `LOCK RET` or overlapping multi-byte opcodes) may be ambiguous without knowing the CPU state at decode time.