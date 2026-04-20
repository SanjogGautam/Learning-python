#multiple inheritance is a feature of object-oriented programming where a class can inherit from more than one parent class. This allows the child class to have access to the properties and methods of multiple parent classes, enabling code reuse and creating more complex relationships between classes.
class parent1:
    def method1(self):
        return "This is method 1 from parent 1"
class parent2:
    def method2(self):
        return "This is method 2 from parent 2"
class child(parent1, parent2):
    def method3(self):
        return "This is method 3 from child class"
c1=child()
print(c1.method1())#we can access method1 from parent1 class
print(c1.method2())#we can also access method2 from parent2 class
print(c1.method3())#we can also access method3 from child class