'''6. WAP to multiply two numbers by using recursive function.'''
from functools import lru_cache
@lru_cache(maxsize=None)
def multiply(a,b):
    if b == 0:
        return 0
    
    # Handling negative 'b' by flipping the signs which will give the value for positive flip and then add - sign at the end
    if b < 0:
        return -multiply(a, -b)
    
    # Standard Recursive Step (for positive b)
    return a + multiply(a, b - 1)
n1=int(input("Enter the firt number= "))
n2=int(input("Enter the second number= "))
print(f"{n1} x {n2} = {multiply(n1,n2)}")
