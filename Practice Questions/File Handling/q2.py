'''2. Write the following menu driven program:
   1. Write
   2. Read
   3. Append
    Enter your choice:'''
import os
while True:
    print("1.Write\n2.Read\n3.Append\n4.Exit")
    choice=int(input("Enter your choice= "))
    match choice:
        case 1:
            data=input("Enter your Text you want to insert= ")
            with open('b.txt','w') as f:
                f.write(data)
        case 2:
            if os.path.exists('b.txt'):
                with open('b.txt','r') as f:
                     print(f.read())
            else:
                print("File doesn't exist write first")
        case 3:
            data=input("Enter your Text you want to insert= ")
            with open('b.txt','a') as f:
                f.write("\n"+data)
        case 4:
            print("Exitting the program")
            break
        case _: 
            print("You Entered teh wrong choice")

