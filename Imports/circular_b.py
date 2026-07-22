"""The other half of the circle. See circular_a.py."""

def whoami():
    return "b"

def greet_from_b():
    import circular_a
    return "b says hi to " + circular_a.whoami()
