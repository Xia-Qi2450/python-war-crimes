"""Why this shouldn't work: Python has no goto and no labeled break,
so this defines a private exception class for the sole purpose of
jumping out of two nested for-loops at once -- something a plain
break cannot do on its own."""

class _JumpOut(Exception):
    pass

def find_pair(matrix, target):
    try:
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == target:
                    raise _JumpOut((i, j))
    except _JumpOut as jump:
        return jump.args[0]
    return None

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(find_pair(grid, 6))
print(find_pair(grid, 42))
