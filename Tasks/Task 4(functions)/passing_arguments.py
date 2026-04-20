#keyword arguments
def greet(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old.")
greet(name="Sanjog", age=25) #keyword arguments
#positional arguments
def greet(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old.")
greet("Sanjog", 25) #positional arguments
#*args and **kwargs
def greet(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
greet("Sanjog", "Python", language="English", country="Nepal")
#application of positinal only arguments ,/ and keyword only arguments,*
def greet(name, /, age, *, language):
    print("Hello " + name + ", you are " + str(age) + " years old and you speak " + language + ".")
greet("Sanjog", age=25, language="English")
#*args allows you to pass a variable number of positional arguments to a function, while **kwargs allows you to pass a variable number of keyword arguments. This can be useful when you want to create functions that can handle a wide range of input without having to specify every possible argument in advance.
def sanjog(*args):
    print("Positional arguments:", args)
sanjog("Hello", "World", 123)