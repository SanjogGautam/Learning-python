def fibo(n:int)->int:
    return n if n<2 else fibo(n-1)+fibo(n-2)
num = int(input("Enter number= "))
for i in range(num):
    print(fibo(i),end=" ," if i<num-1 else "")