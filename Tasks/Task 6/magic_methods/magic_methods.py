#This are the python operation that calls automatically in response to a certain operation
#often called magic methods or dunder methodsw
class sanjog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Name= {self.name}, age= {self.age}"#it gives string representaion of object
    def __len__(self):
        return self.age#it gives the lenght of the object
    def __call__(self):
        print("sanjog is a coder")
    def __del__(self):#destructor
        print("object is destroyed")
s1=sanjog("sanjog",20)
print(s1)
s1()
print(len(s1))
del s1