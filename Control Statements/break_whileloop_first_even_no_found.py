#break at first even no found in list using while loop
lst=[1,23,14,8,12]
i=0
while i<len(lst):
    if lst[i]%2==0:
        print(f"First even no found= {lst[i]}")
        break
    i+=1
