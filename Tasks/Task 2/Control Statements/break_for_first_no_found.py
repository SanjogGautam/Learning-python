#break stop at first even number found in the list
lst=[1,3,5,7,8,10]
for i in lst:
    if i%2 == 0:
        print(f"First even no found= {i}")
        break
