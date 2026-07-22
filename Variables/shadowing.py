"""Why this shouldn't work: every name below shadows a built-in,
and yet the script runs top to bottom without a single NameError."""

list = [3, 1, 2]
list = sorted(list)  # builtins.sorted still works -- the NAME "list" does not, anymore
print(list)

dict = {"a": 1}
dict["b"] = 2
print(dict)

type = "cursed"
print(type, len(type))  # len hasn't been shadowed. yet.

str = 42
print(str + 8)  # str is now an int. arithmetic works. str(str) would not.

id = "not a memory address, just a variable now"
print(id)
