"""Why this shouldn't work: this reaches into the builtins module
itself and replaces print for the ENTIRE process, not just this
file. Every print() call after this point, anywhere in this
program, is affected -- until it's put back."""

import builtins

_real_print = builtins.print

def loud_print(*args, **kwargs):
    _real_print(*[str(a).upper() for a in args], **kwargs)

builtins.print = loud_print

print("this is getting shouted at you")  # LOUD, even though we called plain print()

builtins.print = _real_print
print("back to whispering")
