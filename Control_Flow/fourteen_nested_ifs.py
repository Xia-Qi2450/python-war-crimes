"""Why this shouldn't work: there are exactly three meaningful
conditions in this function -- is it a positive int, is it even,
is it over 100 -- wrapped in fourteen levels of nested if
statements, most of which check things that are always true."""

def classify(n):
    if n is not None:
        if isinstance(n, int):
            if n != 0:
                if n > -10**9:
                    if n < 10**9:
                        if n == n:                    # always true
                            if abs(n) >= 0:            # always true
                                if n > 0:
                                    if n % 1 == 0:      # always true for an int
                                        if n % 2 == 0:
                                            if n // 2 == n / 2:  # always true here
                                                if n > 100:
                                                    if n < 10**8:
                                                        if str(n) == str(n):  # always true
                                                            return "positive, even, large"
    return "not that"

print(classify(144))
print(classify(-4))
print(classify(3))
