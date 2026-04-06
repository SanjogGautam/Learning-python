'''2. Write a program that counts the number of vowels (a, e, i, o, u) of a
string given as input from the user. Loop the string and check if the
current character is a vowel.'''
word=input("Enter the word: ").lower()
count = 0
vowels='aeiou'
for i in word:
    if i in vowels:
        count= count + 1
        print(f"The current character {i} is a vowel")
    else:
        continue
print(f"Total no of vowels = {count}")
    
