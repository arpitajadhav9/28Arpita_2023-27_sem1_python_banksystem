#creating account

# bank_package/bank.py

class Bank:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def create_account(self):
        print(f"Account created for {self.account_holder}")

    def withdraw(self):
        amount = float(input("Enter the withdrawal amount: "))
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")

    def deposit(self):
        amount = float(input("Enter the deposit amount: "))
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance for {self.account_holder}: {self.balance}")

