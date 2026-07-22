"""A module engineered to poison anything that star-imports it."""

__all__ = ["len", "print", "sorted"]  # yes, really -- these are exported deliberately

def len(x):
    return "not a number, a lie"

def print(x):
    import builtins
    builtins.print(f"[INTERCEPTED] {x}")

def sorted(x):
    return list(reversed(x))
