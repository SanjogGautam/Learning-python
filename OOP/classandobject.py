class Person:
    # Class Attribute (Shared by all humans)
    species = "Homo sapiens" 

    # Constructor (MUST have double underscores)
    def __init__(self, name):
        self.name = name

    def hello(self):
        # Accessing the instance variable using self.name
        print(f"Hello, my name is {self.name}")

# Creating instances
p1 = Person("Sanjog")
p2 = Person("Swagat")

print(p1.name, p2.name)
print(Person.species)

# Calling the method
p1.hello()
