#4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
from abc import ABC, abstractmethod
PI=3.14
class shape(ABC):

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return PI*(self.radius**2)
    def perimeter(self):
        return 2*PI*self.radius
class triangle(shape):
    def __init__(self,a,b,c,base,height):
        self.a=a
        self.b=b
        self.c=c
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
    def perimeter(self):
        return self.a+self.b+self.c
class square(shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length**2
    def perimeter(self):
        return 4*self.length
c1=circle(20)
t1=triangle(10,5,15,10,5)
s1=square(10)
print(f"Area of square= {s1.area()}\n Area of Circle= {c1.area()}\n Area of Triangle= {c1.area()}")
print(f"Preimeter of Square= {s1.perimeter()}\n Perimeter of Circle= {c1.perimeter()}\n Perimeter of Triangle= {t1.perimeter()}")

