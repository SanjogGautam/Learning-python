'''WAP to input a sentence and count the number of vowels.'''
sent1=input("Enter your string= ")
count=0
for i in sent1:
    if i in "AEIOUaeiou":
        count+=1
print(f"The numbers of vowels in the sentence = {sent1} = {count}")
