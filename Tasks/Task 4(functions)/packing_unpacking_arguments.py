#* and ** are used for packing and unpacking arguments in Python functions.
#unpacking arguments using tuples
t1=(1,2,3)#packing the arguments into a tuple
def sanjog(a,b,c):
    return a + b + c
result = sanjog(*t1) #unpacking the tuple
print("The sum is:", result)
#unpacking arguments using dictionaries
d1={'a':1,'b':2,'c':3} #packing the arguments into a dictionary
def sanjog(a,b,c):
    return a + b + c, a*b*c
(result1,result2) = sanjog(**d1) #unpacking the dictionary
print("The sum is:", result1)
print("The product is:", result2)