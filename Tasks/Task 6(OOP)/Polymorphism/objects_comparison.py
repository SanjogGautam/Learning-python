class sanjog:
    def __init__(self,x):
        self.x=x
    def __gt__(self,other):#gt for > greater then

        if self.x>other.x:
            return self.x
        else:
            return other.x
s1=sanjog(5)
s2=sanjog(6)
s3=s1>s2
print(s3)

