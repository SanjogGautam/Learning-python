'''1.Create a function that takes radius of circle as input
from user and return the area.'''
PI= 3.14
def area(r):
    return PI*(r**2)
radius=float(input("Enter the radius= "))
print(f"The area of the circle= {area(radius)}")
