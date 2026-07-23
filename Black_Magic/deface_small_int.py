"""Why this shouldn't work, and why it might not work at all:
CPython caches small integers (-5 to 256) as singleton objects. This
uses ctypes to reach directly into that object's memory and
overwrite the numeric value it stores. If it works, every reference
to the literal `5` anywhere in the running process is affected
afterward -- not just a variable, the LITERAL.

This depends on PyLongObject's internal memory layout, which has
changed across CPython versions (notably around 3.11-3.12, when
small ints became immortal objects with a different internal
layout) and varies further across builds and platforms even within
the same version. Treat a crash, a silent no-op, or a genuinely
defaced integer as three equally valid, equally cursed outcomes --
this is not hypothetical hedging, it's observed behavior: on one
CPython 3.12.3 build this segfaults on exit; on GitHub Actions'
hosted 3.12 and 3.13 runners it exits cleanly with no visible
effect, because the offset math lands somewhere that isn't the
digit value. Both are the crime. Neither is a bug in this file.
CI logs this one's exit code but never fails the build over it --
see scripts/verify_crimes.py. Run in a throwaway process, never in
anything you care about."""

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
