#6. Write a python program to add two Distance objects that contain the instance variables km and m.
class add:
    def __init__(self,km,m):
        self.km=km
        self.m=m
    def __add__(self,other):
        return add(self.km+other.km,self.m+other.m)
ob1=add(10,200)
ob2=add(12,300)
ob3=ob1+ob2
print(f"{ob3.km}.{ob3.m//100}km ")