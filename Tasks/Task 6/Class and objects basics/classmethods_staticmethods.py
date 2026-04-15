#@classmethod is used to define a class function which is accessible to all
class sanjog:
    lastname="gautam"#class vairable which is accessible to all
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod# this method doesn't need self or cls it is independent but also part of the given class
    def add(a,b):
        return a+b

    @classmethod
    def change_surname(cls,newsurname):#it uses cls as the first parameter
        cls.lastname=newsurname
    #__str__()method is a special method that controls what is returned when the object is printed
    def __str__(self):
        return f"{self.name} , {self.age}"
s1=sanjog("sanjog",20)
print(s1)#since __str__ returns what it has given
print(sanjog.lastname)
sanjog.change_surname("Neupane")#changing the class variable
print(s1)
print(sanjog.lastname)
print(sanjog.add(20,30))

        
