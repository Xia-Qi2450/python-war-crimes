"""Why this shouldn't work: four classes form a diamond inheritance
graph, and each one defines greet() differently. C3 linearization
resolves the diamond via super() -- and lands on a single
deterministic order that not one of these four classes knows about."""

class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return "B->" + super().greet()

class C(A):
    def greet(self):
        return "C->" + super().greet()

class D(B, C):
    def greet(self):
        return "D->" + super().greet()

print(D().greet())   # D->B->C->A
print(D.__mro__)     # the order nobody consciously chose
