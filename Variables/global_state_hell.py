"""Why this shouldn't work: three functions mutate the same global
variable from different scopes, in an order nobody designed, and
the final value still comes out deterministic -- by accident of
call order, not by anyone's intention."""

counter = 0
log = []

def increment():
    global counter
    counter += 1
    log.append(("inc", counter))

def double():
    global counter
    counter *= 2
    log.append(("double", counter))

def reset_if_even():
    global counter
    if counter % 2 == 0:
        counter = 0
        log.append(("reset", counter))

for fn in [increment, increment, double, increment, reset_if_even, increment]:
    fn()

print(log)
print("final counter:", counter)
