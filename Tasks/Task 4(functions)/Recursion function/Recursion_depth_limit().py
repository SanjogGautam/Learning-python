#python has limit on how depth recursion can go
#default is 1000 times
import sys
print(sys.getrecursionlimit())
#we can also set the recursion depth limit
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
