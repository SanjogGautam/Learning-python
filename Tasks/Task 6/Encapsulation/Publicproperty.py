#access modifiyer public: it can be accessed anywhere inside and outside of the class as well as by the child class
class sanjog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def sum_of(a,b):
        return a+b
class child(sanjog):
    def __init__(self,name,age):
        super().__init__(name,age)
    def access_public_method(self):
        return self.sum_of(10,20)
c1=child("Child",10)
c1.name="Child Name"#we can access public variable and method in child class
c1.age=15#we can also modify public variables in child class
print(c1.access_public_method())#we can access public method in child class
