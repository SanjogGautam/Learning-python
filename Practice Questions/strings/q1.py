'''WAP to input a sentence and count its number of characters.'''
string1=input("Enter your setence= ")
print("The no of characters= {}".format(len(string1)))
count=0
for i in string1:
    if i == " ":
        continue
    else:
        count+=1
print("The no of characters without white spaces= {}".format(count))
