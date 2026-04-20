# a decorator is a function that takes another function as input and extends its behavior without modifying the original function. It allows us to add functionality to an existing function in a clean and reusable way. 
def decorator(func):
    def wrapper():
        print("SANJOG",end=" ")
        func()
    return wrapper
@decorator#this is a syntactic sugar for sanjog = decorator(sanjog)
def say_hello():
    print("Hello, World!")
say_hello()
#if we don't have the exact no of arguments in the wrapper function, we can use *args and **kwargs to pass any number of positional and keyword arguments to the original function.\
def decorator(func):
    def wrapper(*args, **kwargs):
        print("SANJOG",end=" ")
        return func(*args, **kwargs)
    return wrapper
@decorator
def say_hello(name):
    print("Hello, " + name + "!")
say_hello("Sanjog")