#a generator function is a funciton that returns an iterator that produces a sequence of values when iterated over.
#it uses the yield statement to produce a value and suspend its execution until the next value is requested.
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(5)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
print(next(counter))  # Output: 4
print(next(counter))  # Output: 5
#we can also use a for loop to iterate over the generator
for number in count_up_to(5):
    print(number)
#we can also use the generator expression to create a generator
squares = (x**2 for x in range(1, 6))
print(next(squares))  # Output: 1
for square in squares:
    print(square)
# it is more memory efficient than a list comprehension because it generates values on the fly instead of storing them all in memory at once.
# it is used when we want to iterate over a large sequence of values without storing them all in memory at once. wihtout it we would have to create a list of all the values and then iterate over it, which can be memory intensive. with a generator we can generate each value on the fly and iterate over it without storing it all in memory at once.
#send() method is used to send a value to the generator and resume its execution. 
def sanjog():
    name = yield "What is your name?"
    age = yield f"Hi {name}, how old are you?"
    print(f"{name} is {age} years old.")

g = sanjog()
print(next(g))           # Printing: prints "What is your name?"
g.send("Sanjog") # Injects name, prints "how old are you?"
print(g.send(20))  # Injects age, prints "Sanjog is 20 years old."