'''4. Create a class called BankAccount with a constructor that takes in the
owner's name, balance and type of account. The class should have
methods get_balance(), deposit(amount) and withdraw(amount) that
return the balance, deposit an amount, and withdraw an amount
respectively. Create an instance of the class and call the methods to
display the values.'''
class BankAccount:
    def __init__(self, owner_name, balance, typeofacc):
        self.owner_name = owner_name
        self.balance = balance
        self.typeofacc = typeofacc

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        # BRUTAL LOGIC: You must UPDATE the balance, not just return it
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds! Hack blocked."
        else: 
            self.balance -= amount
            return self.balance

# Create account with a starting balance
acc1 = BankAccount("Sanjog", 1000, "Savings")



print(f"Initial Balance: {acc1.get_balance()}")
print(f"New Balance after Deposit: {acc1.deposit(300)}")
print(f"New Balance after Withdrawal: {acc1.withdraw(200)}")
