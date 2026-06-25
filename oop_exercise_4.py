
#1------------------------------------
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount < 0 :
            print("error")
            return
        else:
            self.__balance += amount
            print(self.__balance, "is the new balance")

    def withdraw(self, amount):
        if amount < 0 :
            print("error, you cannot draft a negative sum")
            return
        elif amount > self.__balance:
            print("there is no enough money in your account")
            return
        else:
            self.__balance -= amount
            print(self.__balance, "is the new balance")

    def get_balance(self):
        print(f"the current balance is {self.__balance}")

























