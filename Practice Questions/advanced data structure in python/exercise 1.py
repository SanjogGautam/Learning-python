'''1. List exercise: Create a list of 5 numbers and then print the sum and
average of the numbers.'''
list =[1,2,3,4,5]
sum=0
for i in list:
    sum= sum+i
avg= sum/len(list)
print(f"The sum of the list = {sum}")
print(f"The avg of the list = {avg}")
