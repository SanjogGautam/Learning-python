'''WAP to input two words and print the longest word.'''
w1=input("Enter your first word= ")
w2=input("Enter your second word= ")
if len(w1)>len(w2):
    print(f"The longest word = {w1}")
else:
    print(f"The longest word = {w2}")
    
