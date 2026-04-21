'''5. WAP to find the Nth term of fibonacci series using recursive function.'''
from functools import lru_cache
@lru_cache(maxsize=None)
def fibo(n):
    a=0
    b=1
    print(f"{a},{b}",end="")
    for i in range(2,n):
        c=a+b
        print(f",{c}",end="" )
        a=b
        b=c
number=int(input("Enter number of fibonacci sequence= "))
fibo(number)
#here i wanted to do without recursion putting my own logic
