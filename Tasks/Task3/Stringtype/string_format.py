#.format() nethod is used to format the string in a specific way. It allows us to insert values into a string at specific placeholders. The placeholders are defined using curly braces {} and can be replaced with values passed as arguments to the format() method.
price=49.99
quantity=5
total=price*quantity
message="The total price for {} items is ${:.2f}".format(quantity,total)
print(message)
#we can also index the placeholders to specify the order of the arguments
message="The total price for {1} items is ${0:.2f}".format(total,quantity)
print(message)
#we can also use named placeholders
message="The total price for {qty} items is ${pr:.2f}".format(pr=total,qty=quantity)
print(message)