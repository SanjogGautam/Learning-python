from abc import ABC, abstractmethod

# This is the Abstract Class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        # We leave this empty because every shape calculates it differently
        pass

    def description(self):
        # we can still have normal methods in an abstract class
        print("I am a geometric shape.")

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    # We MUST implement area() or Python will throw an error
    def area(self):
        return self.side * self.side

# s = Shape() # This would throw an ERROR: Cannot instantiate abstract class
sq = Square(5)
print(f"Square Area: {sq.area()}")
sq.description()