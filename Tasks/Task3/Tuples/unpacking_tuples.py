#when we create a tuple we normally assign values to it.This is called "packing" in tuple
fruits=("A","B",1,2,3)
#but in puthon we are also allowed to extract values back to the variables. This is called unpacking
(d,*e,f)=fruits#* is used if there is not enough variable to assign values to it
print(d)
print(e)
print(f)
#this creates a separtate list while creation of it
