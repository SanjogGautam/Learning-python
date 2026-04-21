def fact(n):
    return n if n<2 else n*fact(n-1)
print(fact(5))