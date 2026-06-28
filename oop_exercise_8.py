


#1---------------------------------------

# class BankAccount:
#
#     def __init__(self, account_number, initial_balance=0):
#         self._account_number = account_number
#         self._balance = initial_balance
#         self._transaction_count = 0
#
#     @property
#     def balance(self):
#         return self._balance
#
#     @property
#     def account_number(self):
#         return self._account_number
#
#     def deposit(self, amount):
#         if amount <= 0 :
#             print("negative value")
#             return
#         self._balance += amount
#         self._transaction_count += 1
#
#     def withdraw(self, amount):
#         if amount < 0 or amount > self._balance:
#             print("error")
#             return
#         self._balance -= amount
#         self._transaction_count += 1
#
#     def get_transaction_count(self):
#         return self._transaction_count

#2-------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) != str:
            print("name must be str")
            return
        if not name.strip():
            print("empty name")
            return
        self._name = name.title()


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            print("age must be whole number")
            return
        if age < 0 or 150 < age:
            print("age not allowd")
            return
        self._age = age


    @property
    def category(self):
        if self._age < 13:
            return "child"
        elif 13 <= self._age <= 19 :
            return "teenager"
        elif 19 < self._age <= 64 :
            return "Adult"
        else:
            return "old"


























































