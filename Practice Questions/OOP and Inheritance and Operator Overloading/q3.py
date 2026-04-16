class Calculator:
    def __init__(self, *args):
        self.args = args

    def add(self):
        return sum(self.args)

    def diff(self):
        # Start with the first number, then subtract the rest
        res = self.args[0]
        for i in self.args[1:]:
            res -= i
        return res

    def mul(self):
        res = 1
        for i in self.args:
            res *= i
        return res

    def div(self):
        res = self.args[0]
        for i in self.args[1:]:
            if i == 0:
                return "Error: Cannot divide by zero"
            res /= i
        return res

    def mod(self):
        # Modulo usually happens between two numbers
        if len(self.args) < 2:
            return "Error: Modulo requires at least two numbers"
        res = self.args[0]
        for i in self.args[1:]:
            res %= i
        return res

# Usage
my_calc = Calculator(100, 10, 2)
print(f"Addition: {my_calc.add()}")    # 112
print(f"Subtraction: {my_calc.diff()}") # 100 - 10 - 2 = 88
print(f"Division: {my_calc.div()}")       # 100 / 10 / 2 = 5.0
print(f"Modulo: {my_calc.mod()}")         # 100 % 10 % 2 = 0