def fun1():
    x="sanjog"
    def fun2():
        nonlocal x#nonlocal keyword is used to indicate that a variable is not local to the function, but it is also not global. It allows you to modify a variable defined in the nearest enclosing scope that is not global.
        x="Gautam"
    fun2()
    return x
print(fun1())