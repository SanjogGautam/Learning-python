#public access modifyres we can declare public using (_prefix)
class sanjog:
    def __init__(self,name,age):
        self.name=name
        self._age=age
    @staticmethod
    def _sum_of(a,b):
        return a+b
class child(sanjog):
    def __init__(self,name,age):
        super().__init__(name,age)
    def access_public_method(self):
        return _self.sum_of(10,20)

c1=child("Sanjog",20)
print(c1._age)
