# a fucntion has metadata that provides information about the function, such as its name, docstring, and other attributes. When we create a new function by assigning an existing function to a new variable, the metadata of the original function is preserved in the new variable. This means that the new variable will have the same name, docstring, and other attributes as the original function.
def original_function():
    """This is the original function."""
    print("Hello, World!")
new_function = original_function
print(new_function.__name__) # Output: original_function
print(new_function.__doc__) # Output: This is the original function.
#but if we use decorator function to create a new function, the metadata of the original function is not preserved in the new function. 
def decorator(func):
    def wrapper():
        print("SANJOG",end=" ")
        func()
    return wrapper
@decorator
def say_hello():
    """This is the say_hello function."""
    print("Hello, World!")
print(say_hello.__name__) # Output: wrapper
print(say_hello.__doc__) # Output: None
#but we can use functools.wraps to preserve the metadata of the original function 
import functools
def decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("SANJOG",end=" ")
        func()
    return wrapper
@decorator
def say_hello():
    """This is the say_hello function."""
    print("Hello, World!")
print(say_hello.__name__) # Output: say_hello
print(say_hello.__doc__) # Output: This is the say_hello function.