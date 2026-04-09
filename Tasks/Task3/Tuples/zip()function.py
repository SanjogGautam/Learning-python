#zip funciton returns the zip object of the given tuple or iterable
#zip funciton iterates the given tuples
#like((tuple1[0],tuple2[0]),....)the length is determined by the legth of the smallest tuple
t1=(1,2,3,4)
t2=(5,6)
x=zip(t1,t2)
print(x)#this gives the zip object
print(tuple(x))#it gives the tuple mannered format
