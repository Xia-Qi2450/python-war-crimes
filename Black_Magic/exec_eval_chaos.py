"""Why this shouldn't work: the entire "logic" of this program is a
string, assembled from other strings, evaluated at runtime,
including a loop body that itself calls eval() on more strings it
builds on the fly."""

program_parts = ["for i in range(5): ", "print(eval(f'i ** {i}'))"]
full_program = "".join(program_parts)
exec(full_program)

expr = "".join(["3", "+", "4", "*", "2"])
print(eval(expr))  # 11, built one character-group at a time for no reason
