'''A common example of Hybrid inheritance is the Diamond Problem, which combines Hierarchical and Multiple inheritance:

1.Class A is the grandparent.

2.Class B and Class C both inherit from A (Hierarchical).

3.Class D inherits from both B and C (Multiple).

'''
class Vehicle: # Base Parent
    def info(self):
        print("This is a vehicle.")

class Car(Vehicle): # Hierarchical (from Vehicle)
    def drive(self):
        print("Driving on the road.")

class Airplane(Vehicle): # Hierarchical (from Vehicle)
    def fly(self):
        print("Flying in the sky.")

# Hybrid: Multiple Inheritance (from Car and Airplane)
class FlyingCar(Car, Airplane):
    def special_feature(self):
        print("I can both drive and fly!")

# Testing the Hybrid
fc = FlyingCar()
fc.info()    # From Vehicle
fc.drive()   # From Car
fc.fly()     # From Airplane