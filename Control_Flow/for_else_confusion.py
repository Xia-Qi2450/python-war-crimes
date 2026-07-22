"""Why this shouldn't work: for-else runs the else clause when the
loop completes WITHOUT hitting break -- the opposite of what most
people guess on first read. This file nests TWO for-else pairs to
find the first prime in a list, using break/continue/else together
with no explicit boolean flag anywhere."""

def first_prime(numbers):
    for n in numbers:
        if n < 2:
            continue
        for p in range(2, int(n ** 0.5) + 1):
            if n % p == 0:
                break
        else:
            # inner loop completed with no divisor found -- n is prime
            return f"first prime found: {n}"
    else:
        return "no primes found"

print(first_prime([4, 6, 8, 9, 10, 11, 12]))
print(first_prime([4, 6, 8, 9, 10]))
