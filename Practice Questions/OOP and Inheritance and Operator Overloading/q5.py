#5. Write a python program to add two Point objects.
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return point(self.x+other.x,self.y+other.y)
p1=point(2,2)
p2=point(3,3)
p3=p1+p2
print(p3.x,p3.y)