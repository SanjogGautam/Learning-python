class Calculator:
    # One method to handle 2 or 3 numbers
    def add(self, a, b, c = 0):
        return a + b + c

obj = Calculator()
print(obj.add(5, 5))      # Works with 2 numbers
print(obj.add(5, 5, 10))  # Works with 3 numbers
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3))       # Output: 6
print(multiply(2, 3, 4, 5)) # Output: 120