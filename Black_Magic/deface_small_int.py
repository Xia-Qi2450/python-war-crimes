"""Why this shouldn't work, and why it might not work at all:
CPython caches small integers (-5 to 256) as singleton objects. This
uses ctypes to reach directly into that object's memory and
overwrite the numeric value it stores. If it works, every reference
to the literal `5` anywhere in the running process is affected
afterward -- not just a variable, the LITERAL.

This depends on PyLongObject's internal memory layout, which has
changed across CPython versions (notably around 3.11-3.12, when
small ints became immortal objects with a different internal
layout). Treat a crash, a silent no-op, or a genuinely defaced
integer as three equally valid, equally cursed outcomes.

Tested on CPython 3.12.3: it corrupts the integer object badly
enough that the process segfaults on exit (nonzero/negative exit
code, no traceback -- the interpreter just dies). That is not a bug
in this file. That IS the demonstration. Run in a throwaway
process, never in anything you care about, and don't be alarmed
when your terminal reports a crash instead of clean output."""

import ctypes
import sys

print("Python version:", sys.version)
print("2 + 2 =", 2 + 2)

five = 5
offset = five.__sizeof__() - 8
try:
    ctypes.memmove(id(five) + offset, (ctypes.c_long * 1)(42), 8)
    print("2 + 3 =", 2 + 3, "(if this isn't 5, it worked)")
except Exception as e:
    print(f"the interpreter's internals resisted: {type(e).__name__}: {e}")
