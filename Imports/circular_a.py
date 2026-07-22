"""Why this shouldn't work: a imports b, and b imports a. This only
survives because the actual `import circular_b` call is deferred
until it's inside a function body -- called after both module
top-levels have already finished executing."""

def whoami():
    return "a"

def greet_from_a():
    import circular_b
    return "a says hi to " + circular_b.whoami()
