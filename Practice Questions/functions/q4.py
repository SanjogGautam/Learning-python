'''WAP to find factorial of a number using recursive function.'''
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return n*factorial(n-1)
number=int(input("Enter you number= "))
print(factorial(number))
