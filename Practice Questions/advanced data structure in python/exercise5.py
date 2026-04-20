'''5. Create a list with 3 colors. Then ask the user to give a color as input.
If the color is in the list, display a message saying so. Otherwise,
append the color given by the user to the end of the list and print the
updated lis'''
colors = ["red", "blue" , "green"]
colorinput=input("Enter the user color: ")
if colorinput in colors:
    print("The color is in the list")
else:
    print("the color is not in the list")
    colors.append(colorinput)
    print("Update list", colors)
