class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

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



account = SavingsAccount(101, "Vivek", 5000, 4.5)
account.display()