#Operator Overloading is a feature in Python that allows you to change the way an operator (like +, -, *, or >) works when it is used with your own custom objects.
#example multiplying two points
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __mul__(self,other):#self gives left obejct(x) and other gives right object(y)
        return point(self.x*other.x,self.y*other.y)#return a new point object here 
    def __str__(self):#it returns the userfriendly string version of the object
        return f"{self.x} , {self.y}"

p1=point(2,2)
p2=point(4,4)
p3=p1*p2
print(f"p1 * p2 = {p3}")
print(p3.x , p3.y)