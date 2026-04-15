#__del__ is automatically called when an object is destroyed. It is used to clean up any resources that the object may have acquired during its lifetime. The __del__ method is defined in a class and is called when an object of that class is garbage collected. It is important to note that the __del__ method may not always be called, especially if there are circular references or if the program is exiting. Therefore, it is generally recommended to use other methods for resource cleanup, such as context managers or explicit cleanup methods.
class sanjog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __del__(self):
        print(f"{self.name} is being destroyed")
s1=sanjog("Sanjog",20)
print(s1.name)
print(s1.age)
del s1 #this will call the __del__ method and print the message
print(s1.name)# this will show an error since s1 is destroyed and we can't access its attributes anymore