'''5. Create a class called Vehicle with a constructor that takes in the
make, model and year. The class should have methods get_make(),
get_model() and get_year() that return the respective values. Create
two classes, Car and Truck, that inherit from Vehicle. The Car class
should have an additional method get_type() that returns "Car" and
the Truck class should have an additional method get_type() that
returns "Truck". Create instances of both classes and call the methods
to display the values.
'''
class vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_make(self):
        return self.make
class car(vehicle):
    def get_typeof(self):
        return "car"
class truck(vehicle):
    def get_typeof(self):
        return "truck"
t1=truck("BYD","9rr",2005)
print(f"The type of vehicle is: {t1.get_typeof()}")
