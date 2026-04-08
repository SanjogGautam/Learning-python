'''3. Create the following menu driven program:
   1.Area of Circle
   2.Vowel/Consonant
   3.Odd/Even'''
PI=3.14
def area (r):
    return PI*(r**2)
def vowel_consonant(a):
    vowel='aeiouAEIOU'
    if a in vowel:
        print(f"{a} is a vowel")
    else:
        print(f"{a} is a consonant")
def odd_even(n):
    if n%2==0:
        print(f"{n} is a even number")
    else:
        print(f"{n} is a odd number")
while True:
    print("\n\nSelect the one you want to do: ")
    print("""1.Area of Circle
2.Vowel/Consonant
3.Odd/Even
4.Exit""")
    n=int(input("Enter your choice(1-4)= "))
    match n:
        case 1:
            radius=float(input("Enter the radius of circle= "))
            print(f"Area of the circle= {area(radius)}")
        case 2:
            char=input("Enter your character= ")
            vowel_consonant(char)
        case 3:
            num=int(input("Enter the number= "))
            odd_even(num)
        case 4:
            print("Exiting the program")
            break
        case _:
            print("Enter a valid choice")
            
    

        

    
