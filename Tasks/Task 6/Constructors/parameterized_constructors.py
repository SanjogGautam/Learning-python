#parameterized constructor is a constructor that takes parameters and assigns them to the instance variables. It is used to initialize the instance variables with the values passed as arguments while creating an object of the class.
class sanjog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=sanjog("Sanjog",20)
print(s1.name)
print(s1.age)
#default parameterized constructor
class gautam:
    def __init__(self,name="Gautam",age=25):
        self.name=name
        self.age=age
g1=gautam()
print(g1.name)
print(g1.age)