"""Why this shouldn't work: this decorator swaps a function's
__code__ object with a completely different function's compiled
bytecode, live, at import time. Calling add() afterward literally
runs multiply()'s bytecode -- the function object never changed,
only what's inside it did."""

def swap_bytecode(source_fn):
    def decorator(target_fn):
        target_fn.__code__ = source_fn.__code__
        return target_fn
    return decorator

def multiply(a, b):
    return a * b

@swap_bytecode(multiply)
def add(a, b):
    return a + b

print(add(3, 4))  # 12, not 7 -- `add` now runs `multiply`'s bytecode
