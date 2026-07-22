"""Why this shouldn't work: this is curry() implemented as six
nested closures for a function that takes six arguments nobody
asked to be curried, followed by a recursive factorial implemented
as a single anonymous lambda expression with no name to recurse on."""

def add6(a):
    def _b(b):
        def _c(c):
            def _d(d):
                def _e(e):
                    def _f(f):
                        return a + b + c + d + e + f
                    return _f
                return _e
            return _d
        return _c
    return _b

print(add6(1)(2)(3)(4)(5)(6))  # 21


def y_combinator(f):
    return (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))

factorial = y_combinator(lambda self: lambda n: 1 if n == 0 else n * self(n - 1))
print(factorial(5))  # 120, computed via a recursive lambda that never names itself
