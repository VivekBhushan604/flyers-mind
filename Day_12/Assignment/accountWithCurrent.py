class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def display(self):
        print("\nAccount Details")
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ₹{self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def display(self):
        super().display()
        print(f"Interest Rate: {self.interest_rate}%")

class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance):
        super().__init__(account_number, holder_name, balance)

    def withdraw(self, amount):
        if amount <= self.balance + 1000:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Overdraft limit exceeded.")

savings = SavingsAccount(101, "Vivek", 5000, 4.5)
current = CurrentAccount(201, "Rahul", 5000)

print("Savings Account")
savings.display()

print("\nCurrent Account")
current.display()
current.withdraw(5500)
print("\nAfter Withdrawal")
current.display()