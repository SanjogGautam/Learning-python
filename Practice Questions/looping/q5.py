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
            pass
        case 3:
            pass
        case 4:
            print("Exitting")
            break
        case _:
            print("You entered the wrong value")
    
