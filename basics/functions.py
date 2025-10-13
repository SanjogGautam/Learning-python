#inbuilt functions in python
x=-7.5
print(abs(x)) #absolute value
print(pow(2,3)) #2^3
print(max(2,3,4,5,6)) #maximum value
print(min(2,3,4,5,6)) #minimum value
import math
x=16
print(math.sqrt(x)) #square root
print(math.pi) #value of pi
print(math.ceil(3.4)) #rounds to next integer
print(math.floor(3.4)) #rounds to previous integer
#user defined functions
def greet(name):
    print("hello " + name)
greet("sanjog")