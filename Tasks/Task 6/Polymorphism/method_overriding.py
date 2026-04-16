#Child Class provides its own specific implementation of a method that is already provided by its Parent Class.
class parent:
    def fly(self):
        print("Sanjog can't fly")
class child(parent):
    def fly(self):
        print("Birds can fly")
c=child()
c.fly()#it overrideds the parent method
parent.fly(c)