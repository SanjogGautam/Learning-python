#inheritance ko one of the example
class Polygon:
    def __init__(self,numofedge):
        self.numofedge = numofedge
        
    def edge(self):
        return self.numofedge

class Rectangle(Polygon):
    def __init__(self, length,  width):
        super().__init__(4)
        self.length= length
        self.width= width
    def area(self):
        return self.length * self.width
rect=Rectangle(10,20)
print(f"Number of edges= {rect.edge()}")
print(f"Area of the rectangle= {rect.area()}")
