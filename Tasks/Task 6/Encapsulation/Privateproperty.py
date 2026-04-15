#encapsulation: it is about the protecting the data inside of a class
#it means keeping data and methods together in a class while controlling the data that can be accessed
#to show private propery we use __ prefix
#private class can't be accessed outside of class as well as by the childern classes
class sanjog:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self):
        self.__age=age
    @staticmethod
    def __sum_of(a,b):#it is also a private method/function
        return a+b
    def info(self):
        print(f"name: {self.name}, age={self.__age}")
s1=sanjog("Sanjog",20)
s1.info()
#shows an error since we can't access private outside of the class print(s1.__age)
#but we can access it using name mangling
print(s1._sanjog__age)
#we can't access private method outside of the class and also by the child class 
class child(sanjog):
    def __init__(self,name,age):
        super().__init__(name,age)
    def access_private_method(self):
        return self.__sum_of(10,20)
c1=child("Child",10)
print(c1.access_private_method())#shows an error since we can't access private method in child class