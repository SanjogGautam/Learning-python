'''5. WAP to print the following patterns:
   a.         b.             c. 
     1           *           1
     12         ***          10
     113       *****         101
     1114     *******        1010
     11115   *********       10101'''
print(""" 1.          2.        3.           4.To exit
 1           *           1
 12         ***          10
 113       *****         101
 1114     *******        1010
 11115   *********       10101""")
while True:
    n=int(input("Enter choice (1-4): "))
    match n:
        case 1:
            for i in range(1,6):
                for j in range(1,i+1):
                    if i==j and i!=1:
                        print(i,end="")
                    else:
                        print("1",end="")#end=""perevents the formation of new line
                        continue
                print()
        case 2:
            rows = 5
            for i in range(1, rows + 1):
                # Step 1: Print leading spaces
                print(" " * (rows - i), end="")
                # Step 2: Print stars (Odd numbers: 1, 3, 5, 7, 9)
                print("*" * (2 * i - 1))#for this i have taken help of gemini
        case 3:
            for i in range(1,6):
                for j in range(1,i+1):
                    if j % 2== 0:
                        print("0",end="")
                    else:
                        print("1",end="")
                print()
        case 4:
            print("Exitting")
            break
        case _:
            print("You entered the wrong value")
    
