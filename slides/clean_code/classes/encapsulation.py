
# BAD EXAMPLE
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # publicly accessible balance

account = BankAccount(100)
account.balance += 50  # allows direct modification


# GOOD EXAMPLE
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # private balance

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

account = BankAccount(100)
account.deposit(50)