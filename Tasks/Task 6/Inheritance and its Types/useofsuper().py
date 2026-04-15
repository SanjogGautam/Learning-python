#super() in oop is a built-in function that allows you to call methods from a parent class in a child class. It is commonly used in inheritance to access and extend the functionality of the parent class.
class sanjog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return f"Name: {self.name}, Age: {self.age}"
class child(sanjog):
    def __init__(self,name,age):
        super().__init__(name,age) #super() is used to call the constructor of the parent class sanjog and initialize the name and age attributes in the child class
    def display_child(self):
        parent_display = super().display() #super() is used to call the display method of the parent class sanjog and get its return value
        return f"{parent_display}, This is the child class." #we can also add more functionality to the child class by using the return value of the parent class method
c1=child("Child",10)
print(c1.display_child())
