"""Why this shouldn't work: the filtering, the transformation, and
the loop condition are all expressed as side effects of walrus
assignments, with no ordinary '=' anywhere in sight."""

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [
    y
    for x in data
    if (y := x ** 2) > 10
    if (y % 3 == 0) or (y % 2 == 0)
]
print(result)

# a walrus inside an f-string inside a list comprehension inside a lambda
cursed = lambda seq: [f"{(n := i * 2)}:{n ** 2}" for i in seq]
print(cursed(range(5)))

# a while-loop whose condition both consumes AND checks the data
remaining = list(data)
while (chunk := remaining[:3]):
    remaining = remaining[3:]
    print("chunk:", chunk)
