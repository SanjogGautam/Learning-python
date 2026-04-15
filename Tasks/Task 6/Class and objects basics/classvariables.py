#class variaibles are shared by all instances of a class. They are defined within the class construction but outside of any instance methods. They can be accessed using the class name or through any instance of the class.
class sanjog:
    species = "Human" #class variable
    def __init__(self,name,age):
        self.name=name
        self.age=age
sanjog1=sanjog("Sanjog", 25)
print(f"Name: {sanjog1.name}, Age: {sanjog1.age}, Species: {sanjog1.species}")#accessing class variable through instance
print(f"Species: {sanjog.species}")#accessing class variable through class name
#adding class variable 
sanjog.national="Nepal" #adding class variable
print(f"Nationality: {sanjog.national}")
#changing class variable
sanjog.species="Homo sapiens" #changing class variable
print(f"Species: {sanjog.species}")
#adding class methods
# 1. Define a regular function with 'cls' as the first argument
def get_species_func(cls):
    return cls.species

# 2. Wrap it in classmethod() and attach it to the class
sanjog.get_species = classmethod(get_species_func)

# 3. Now it works!
print(f"Species: {sanjog.get_species()}")