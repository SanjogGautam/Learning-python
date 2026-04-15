#there are various types of constructors in python but here we will discuss only default constructor
class sanjog: #defining class
    def __init__(self): #default constructor
        self.name="Sanjog"
        self.age=20
sanjog1=sanjog() #creating object
print(f"Name: {sanjog1.name}, Age: {sanjog1.age}")
#__new__() is a static method that is responsible for creating a new instance of a class. It is called before __init__() and is used to allocate memory for the new object. __new__() takes the class as its first argument and returns a new instance of that class. __init__() is an instance method that initializes the attributes of the newly created object. It takes the newly created object as its first argument (usually named self) and can take additional arguments to initialize the object's attributes.
class gautam:
    def __new__(cls):
        print("Creating instance of Gautam")
        instance = super(gautam, cls).__new__(cls)
        return instance
    def __init__(self):
        print("Initializing instance of Gautam")
        self.name = "Gautam"
        self.age = 25
g1 = gautam()
print(f"Name: {g1.name}, Age: {g1.age}")
# by default __new__() is called when we create an object and it returns an instance of the class which is then passed to __init__() for initialization.
# if we create a class without defining __init__() method, python will provide a default constructor which does nothing and allows us to create an object of the class without any initialization.
class default_constructor:
    pass
d1 = default_constructor()
print(d1)
#if we use __init__ but not __new__, python will automatically call the default __new__ method which creates an instance of the class and then calls our defined __init__ method to initialize it.
