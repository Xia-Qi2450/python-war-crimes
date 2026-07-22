"""Why this shouldn't work: len is reassigned at module scope to
something that lies about the length of every list in the file,
and every later call to len() believes the lie -- for lists only."""

len = lambda x: 9999 if isinstance(x, list) else __builtins__.len(x)

print(len([1, 2, 3]))  # 9999
print(len("abc"))       # 3 -- strings weren't part of the lie
