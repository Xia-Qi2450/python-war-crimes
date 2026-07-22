"""Why this shouldn't work: `a` and `а` look identical in most
fonts. One is Latin U+0061. The other is Cyrillic U+0430. Python
treats them as two completely different variable names, and this
file uses both, side by side."""

a = 1        # Latin 'a', U+0061
а = 2        # Cyrillic 'а', U+0430 -- looks identical to the line above

print(a, а)                          # 1 2 -- two different variables
print(hex(ord("a")), hex(ord("а")))  # 0x61 vs 0x430 -- proof they were never the same character
