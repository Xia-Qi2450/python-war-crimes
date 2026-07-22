"""Why this shouldn't work: this metaclass renames every method on
every class that uses it, reversing the method name at
class-creation time. Calling the "wrong" name still works, because
that's now the ONLY name the method has."""

class ReverseMeta(type):
    def __new__(mcs, name, bases, namespace):
        new_namespace = {}
        for key, value in namespace.items():
            if callable(value) and not key.startswith("__"):
                new_namespace[key[::-1]] = value
            else:
                new_namespace[key] = value
        return super().__new__(mcs, name, bases, new_namespace)

class Backwards(metaclass=ReverseMeta):
    def hello(self):
        return "hi"

b = Backwards()
print(b.olleh())  # the method is now named "olleh" -- "hello" no longer exists
