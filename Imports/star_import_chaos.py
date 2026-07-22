"""Why this shouldn't work: this file has no idea it just redefined
len, print, and sorted, because it did `from module import *` and
trusted the module's __all__ without reading it first."""

from _wildcard_source import *

print("hello")             # not the builtin print anymore
print(len([1, 2, 3]))       # "not a number, a lie"
print(sorted([3, 1, 2]))    # [2, 1, 3] -- this "sorted" just reverses input order
