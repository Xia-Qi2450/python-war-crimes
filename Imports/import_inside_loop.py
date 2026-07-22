"""Why this shouldn't work: importing inside a loop, 100,000 times.
Python caches modules in sys.modules after the first real import,
so this is "only" 100,000 dict lookups pretending to be 100,000
imports -- still a crime, just a cheaper one than it looks."""

import time

start = time.perf_counter()
for i in range(100_000):
    import math  # cached after the first call, written as if it isn't
    result = math.sqrt(i + 1)
elapsed = time.perf_counter() - start

print(f"100,000 redundant imports took {elapsed:.4f}s")
print("last result:", result)
