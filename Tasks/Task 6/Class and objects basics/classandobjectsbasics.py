class sanjog: #defining class
    def __init__(self,name,age): #constructor
        self.name=name
        self.age=age
    def display(self): #method
        print(f"Name: {self.name}, Age: {self.age}")
sanjog1=sanjog("Sanjog", 25) #creating object
sanjog1.display() #calling method
#adding instance variable after creating object
sanjog1.email="sanjog@example.com" #adding instance variable
print(f"Name: {sanjog1.name}, Age: {sanjog1.age}, Email: {sanjog1.email}")
#adding instance method after creating object
def greet(self):
    print(f"Hello, my name is {self.name} and I am {self.age} years old.")
sanjog1.greet = greet.__get__(sanjog1) #adding instance method
#__get__ is used to bind the method to the instance sanjog1
sanjog1.greet() #calling instance method
#instance variable and method are added to the object sanjog1, but not to the class sanjog or any other object created from the class.
