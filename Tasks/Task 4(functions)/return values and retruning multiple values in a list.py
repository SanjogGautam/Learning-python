# passing in arguments to a function
def sanjog(name):#parameter
    print("My name is " + name)
sanjog("Sanjog") #argument
#returing multiple values from a function
#returning a single value from a function
def add(a,b):
    return a + b
result = add(10,5)
print("The sum is:", result)
#it is possible to return multiple values from a function by separating them with commas. The returned values are packed into a tuple, which can be unpacked into individual variables or accessed using indexing.
def add_subtract(a,b):
    add = a + b
    subtract = a - b
    return add,subtract
result = add_subtract(10,5)
#accessing using indexing
print("Addition:", result[0])
print("Subtraction:", result[1])
#unpacking into individual variables
add, subtract = add_subtract(10,5)
print("Addition:", add)
print("Subtraction:", subtract)
#python can return any type of data, including lists, dictionaries, and even other functions. This allows for great flexibility in how functions can be used and what they can return.

