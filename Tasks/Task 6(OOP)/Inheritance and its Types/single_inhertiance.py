#single inheritance is a type of inheritance where a child class inherits from a single parent class. In this example, we have a parent class called 
class sanjog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return f"Name: {self.name}, Age: {self.age}"
class child(sanjog):
    def __init__(self,name,age):
        super().__init__(name,age)#super() is used to call the constructor of the parent class sanjog and initialize the name and age attributes in the child class
    def display_child(self):
        parent_display = super().display()
        return f"{parent_display}, This is the child class."
c1=child("Child",10)
print(c1.display_child())