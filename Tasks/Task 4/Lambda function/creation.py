#it is a single line funciton
#it s syntax looks like lambda ag1,ag2,...: experession
x=lambda x,y:x*y
print(x(1,2))
#note: for me : lambda function is better used when we use them as anonymous function inside of other functions
def fact(n):
    return lambda x: x*n
times3=fact(3)
print(times3(12))
