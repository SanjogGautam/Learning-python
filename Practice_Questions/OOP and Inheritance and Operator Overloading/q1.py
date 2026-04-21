#1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
PI=3.14
class circle():
    def __init__(self,radius:float)->float:
        self.radius=radius
    def area(self)->float:
        return PI*(self.radius**2)
    def perimeter(self)->float:
        return 2*PI*self.radius
c1=circle(20)
print(f"Area of the circle= {c1.area()}")
print(f"Perimeter of the circle= {c1.perimeter()}")
