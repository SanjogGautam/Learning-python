'''3. Create a function that takes a word and
check whether it is palindrome or not.'''
def palindrome(word):
    if word== word[::-1]:
        print(f"The word: {word} is a palindrome")
    else:
        print(f"The word: {word} is not palindrome")

w=input("Enter your word= ")
palindrome(w)
