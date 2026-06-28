


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

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         if type(name) != str:
#             print("name must be str")
#             return
#         if not name.strip():
#             print("empty name")
#             return
#         self._name = name.title()
#
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         if not isinstance(age, int):
#             print("age must be whole number")
#             return
#         if age < 0 or 150 < age:
#             print("age not allowd")
#             return
#         self._age = age
#
#
#     @property
#     def category(self):
#         if self._age < 13:
#             return "child"
#         elif 13 <= self._age <= 19 :
#             return "teenager"
#         elif 19 < self._age <= 64 :
#             return "Adult"
#         else:
#             return "old"


#3----------------------------------

#
# class User:
#     user_count = 0
#     users_list = []
#
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password_hash = User._hash_password(password)
#         User.user_count += 1
#         User.users_list.append(self)
#
#     def __str__(self):
#         return f"username = {self.username}, email = {self.email}"
#     @staticmethod
#     def _hash_password(password:str) :
#             return str(hash(password))
#
#     @staticmethod
#     def is_valid_email(email:str) -> bool :
#         if "@" not in email:
#             return False
#         parts = email.split("@")
#         return "." in parts[1]
#
#     @staticmethod
#     def is_strong_password(password:str) -> bool :
#         if len(password) < 8 :
#             return False
#         has_upper = any(char.isupper() for char in password)
#         has_lower = any(char.islower() for char in password)
#         has_digit = any(char.isdigit() for char in password)
#         return has_upper and has_lower and has_digit
#
#     @staticmethod
#     def create_user_safely(username, email, password):
#         if not User.is_valid_email(email) or not User.is_strong_password(password):
#             print("wrong email")
#             return None
#         new_user = User(username, email, password)
#         return new_user
#
#     @classmethod
#     def get_user_count(cls):
#         return cls.user_count
#
#     @classmethod
#     def find_user_by_username(cls, username):
#         for user in cls.users_list:
#             if user.username == username:
#                 return user
#         return None


#4--------------------------------------

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f"Rectangle({self._width}, {self._height})"
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         if value <= 0 :
#             print("error")
#             return
#         self._width = value
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         if value <= 0 :
#             print("error")
#             return
#         self._height = value
#
#     @property
#     def area(self):
#         return self._width * self._height
#
#     @property
#     def perimeter(self):
#         return (self._width + self._height ) * 2
#
#     @property
#     def is_square(self):
#         return self._height == self._width
#
#     @staticmethod
#     def create_square(side):
#         square = Rectangle(side, side)
#         return square
#
#     @staticmethod
#     def compare_areas(rect1, rect2):
#         area1 = rect1.area
#         area2 = rect2.area
#
#         if area1 > area2:
#             return f"{rect1} is bigger "
#         elif area2 > area1:
#             return f"{rect2} is bigger "
#         else:
#             return "both rects are equale"
































