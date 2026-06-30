class BankAccount:
    def __init__(self, account_no: str, name: str, initial_balance: float = 0.0):
        self.account_no = account_no
        self.name = name
        self.balance = initial_balance
    def deposit(self, amount: float) -> float:
        if amount > 0:
            self.balance += amount
            print(self.balance)
            return self.balance
        print("Deposit amount must be positive.")
        return self.balance
    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(self.balance)
        return self.balance
    def check_balance(self) -> float:
        print(self.balance)
        return self.balance
