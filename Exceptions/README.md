# Exceptions

Crimes against error handling, honesty about failure, and the idea that `except:` should ever appear without a type after it.

- `except_pass.py` — every risky line wrapped in `except: pass`, function never raises, never truly succeeds either
- `catching_systemexit.py` — a "safe" wrapper that also politely swallows `sys.exit()`
