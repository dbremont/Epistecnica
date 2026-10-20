---
tags: [interpreter, language-system, ruby, tool]
---

# CRuby


> 

## Interpreter

```bash
file /usr/bin/ruby3.0
/usr/bin/ruby3.0: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6f6be25d0fb4d749762b5edb55219c2c82a4e68b, for GNU/Linux 3.2.0, stripped
```

## List of Share Libraries

```bash
ldd /usr/bin/ruby3.0
	linux-vdso.so.1 (0x00007ffccddb8000)
	libruby-3.0.so.3.0 => /lib/x86_64-linux-gnu/libruby-3.0.so.3.0 (0x00007f4cdc800000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f4cdc400000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f4cdcbcc000)
	libgmp.so.10 => /lib/x86_64-linux-gnu/libgmp.so.10 (0x00007f4cdc77e000)
	libcrypt.so.1 => /lib/x86_64-linux-gnu/libcrypt.so.1 (0x00007f4cdcb92000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f4cdc697000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f4cdcc01000)
```

## Debugger

- `Ruby's rdbg debugger`
- https://stackoverflow.com/questions/3955688/how-to-debug-ruby-scripts

## References

- https://github.com/ruby/ruby
- https://github.com/mruby/mruby
- https://github.com/codicoscepticos/ruby-implementations
- Chevalier-Boisvert, Maxime, et al. "Evaluating YJIT’s Performance in a Production Context: A Pragmatic Approach." Proceedings of the 20th ACM SIGPLAN International Conference on Managed Programming Languages and Runtimes. 2023.
-