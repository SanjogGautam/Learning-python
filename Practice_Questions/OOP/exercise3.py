'''3. Create a class called Rectangle with a constructor that takes in the
width and height. The class should have methods get_area() and
get_perimeter() that return the area and perimeter of the rectangle
respectively. Create an instance of the class and call the methods to
display the values.'''
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def get_area(self):
        return self.height*self.width
    def get_perimeter(self):
        return 2*(self.width+self.height)

rect=Rectangle(20,30)
print(f"Area of the the Rectangle{rect.get_area()}")
print(f"Perimeter of the the Rectangle{rect.get_perimeter()}")
