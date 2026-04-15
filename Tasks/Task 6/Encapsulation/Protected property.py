class Sanjog:
    def __init__(self, name, age):
        self.name = name     # Public
        self._age = age      # Protected (signaled by _)

    @staticmethod
    def _sum_of(a, b):       # Protected Static Method
        return a + b

class Child(Sanjog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def access_protected_method(self, x, y):
        # Correct syntax: self._methodname
        return self._sum_of(x, y)

c1 = Child("Sanjog", 20)

# Accessing protected variable (allowed by Python, but discouraged)
print(f"Protected Age: {c1._age}") 

# Accessing the method through the child
print(c1.access_protected_method(20, 30))
