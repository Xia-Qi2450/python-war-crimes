"""Why this shouldn't work: the default argument is created exactly
once, at function DEFINITION time, and silently shared by every
call forever after. This isn't a bug in this file. It's a bug in
how default arguments work, being used on purpose."""

def append_to_history(item, history=[]):
    history.append(item)
    return history

print(append_to_history("first call"))
print(append_to_history("second call"))
print(append_to_history("third call"))
# there is only ever one `history` list. there will only ever be one.


def memoize_wrong(n, _cache={}):
    if n in _cache:
        print(f"cache hit for {n}")
        return _cache[n]
    result = n * n
    _cache[n] = result
    return result

memoize_wrong(4)
memoize_wrong(4)  # cache hit, using a module-load-time dict as permanent global state
print("the 'default' argument, exposed and mutated:", memoize_wrong.__defaults__)
