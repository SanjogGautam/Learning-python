#multi-level inheritance is the type of inheritance in which the parent inherits from grandfather and child inherits from father
class grandfather:
    def method1(slef):
        print("This is grandfather")
class father(grandfather):
    def method2(self):
        print("This is father")
class child(father):
    def method3(self):
        print("This is child")
c1=child()
c1.method1()
c1.method2()
c1.method3()