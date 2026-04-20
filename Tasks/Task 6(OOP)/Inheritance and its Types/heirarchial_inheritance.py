#heirarchial inheritance is the inheritance in which the strucure is in the tree like manner meaning it is structred in higher authorial style
# The Parent Class (Base)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        print("This vehicle uses some form of energy.")

# Child Class 1
class ElectricCar(Car):
    def fuel_type(self):
        print(f"The {self.brand} {self.model} runs on Electricity ")

# Child Class 2
class PetrolCar(Car):
    def fuel_type(self):
        print(f"The {self.brand} {self.model} runs on Petrol ")

# Creating objects
tesla = ElectricCar("Tesla", "Model S")
mustang = PetrolCar("Ford", "Mustang")

tesla.fuel_type()   # Output: Runs on Electricity
mustang.fuel_type() # Output: Runs on Petrol