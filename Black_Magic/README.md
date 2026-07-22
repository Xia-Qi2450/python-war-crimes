# Black Magic

Crimes against the CPython implementation. These lean on internals that are not part of the language spec -- expect some of them to behave differently, or not at all, on other Python versions or other interpreters (PyPy, etc).

- `swap_bytecode.py` — a decorator that swaps one function's compiled bytecode into another, live
- `exec_eval_chaos.py` — a program built entirely out of strings, evaluating more strings
- `self_modifying_code.py` — a script that rewrites its own source file on disk while running
- `deface_small_int.py` — uses `ctypes` to overwrite a cached small integer in memory (CPython-version-dependent; on 3.12.3 this segfaults the interpreter on exit, which is the point, not a bug)
