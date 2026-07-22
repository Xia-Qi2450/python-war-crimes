"""Why this shouldn't work: Unicode combining diacritical marks
(category Mn) are legal ID_Continue characters under PEP 3131,
meaning you can stack an arbitrary number of accents onto a single
letter and still have a valid Python identifier. This file defines
a variable name with five invisible-at-a-glance combining acute
accents crammed onto it, and a second, "clean" variable that looks
identical in most fonts. They are two different names."""

clean = "the boring one"

cursed_name = "clean" + "\u0301" * 5  # "clean" + 5 stacked combining acute accents
src = f'{cursed_name} = "the one wearing five invisible hats"\nprint({cursed_name})'
exec(src)

print(clean)
print(f"'clean' is {len('clean')} characters long")
print(f"the cursed name is {len(cursed_name)} characters long, "
      f"despite rendering as roughly the same width")
