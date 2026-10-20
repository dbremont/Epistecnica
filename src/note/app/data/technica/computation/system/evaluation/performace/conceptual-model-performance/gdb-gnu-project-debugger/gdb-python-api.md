# GDB Python API

> 

```python
import gdb

class ListGlobals(gdb.Command):
    """List all global variables in the current context."""

    def __init__(self):
        super(ListGlobals, self).__init__("list_globals", gdb.COMMAND_DATA, gdb.COMPLETE_NONE)

    def invoke(self, arg, from_tty):
        # Get the global block of the current program space
        block = gdb.current_progspace().block_for_pc(gdb.selected_frame().pc())
        while block.global_block() is False:
            block = block.superblock

        # Iterate over all symbols in the global block
        for sym in block:
            if sym.is_variable:
                print(f"Global variable: {sym.name} -> Type: {sym.type}")

ListGlobals()

```

## References

- [The GDB Python API](https://developers.redhat.com/blog/2017/11/10/gdb-python-api)
- [23.2.2 Python API](https://www-zeuthen.desy.de/unix/unixguide/infohtml/gdb/Python-API.html)
- [CppCon 2018: Jeff Trull “Liberating the Debugging Experience with the GDB Python API”](https://www.youtube.com/watch?v=ck_jCH_G7pA)
-