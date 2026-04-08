'''else with while loop the condition runs only if the loop is executed fully and
only doesn't execute when there is occurence of break statement'''
#searching of the elements in the list
lst=[1,2,3,65,12]
i=0
target=int(input("Enter the element you are searching"))
while i<len(lst)+1:
    if target==lst[i]:
        print("Target found:")
        break
else:
    print("Target not found")
