


#1---------------------------------------

class BankAccount:

    def __init__(self, account_number, initial_balance=0):
        self._account_number = account_number
        self._balance = initial_balance
        self._transaction_count = 0

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    def deposit(self, amount):
        if amount <= 0 :
            print("negative value")
            return
        self._balance += amount
        self._transaction_count += 1

    def withdraw(self, amount):
        if amount < 0 or amount > self._balance:
            print("error")
            return
        self._balance -= amount
        self._transaction_count += 1

    def get_transaction_count(self):
        return self._transaction_count


















































