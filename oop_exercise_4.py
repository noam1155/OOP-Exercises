
import hashlib



#1------------------------------------
# class BankAccount:
#     def __init__(self, account_number, account_holder, balance):
#         self.account_number = account_number
#         self._account_holder = account_holder
#         self.__balance = balance
#
#     def deposit(self, amount):
#         if amount < 0 :
#             print("error")
#             return
#         else:
#             self.__balance += amount
#             print(self.__balance, "is the new balance")
#
#     def withdraw(self, amount):
#         if amount < 0 :
#             print("error, you cannot draft a negative sum")
#             return
#         elif amount > self.__balance:
#             print("there is no enough money in your account")
#             return
#         else:
#             self.__balance -= amount
#             print(self.__balance, "is the new balance")
#
#     def get_balance(self):
#         print(f"the current balance is {self.__balance}")




#2------------------------------------------

# class Vehicle:
#     def __init__(self, model, color):
#         self.model = model
#         self._color = color
#         self.__speed = 0
#
#     def accelerate(self, speed_increase):
#         self.__speed += speed_increase
#
#     def brake(self, speed_decrease):
#         if self.__speed - speed_decrease >= 0 :
#             self.__speed -= speed_decrease
#
#     def get_speed(self):
#         return self.__speed
#
#     def get_color(self):
#         print(f"the vehicle color is {self._color}")
#
#
# class Car(Vehicle):
#     def __init__(self, model, color, max_speed):
#         super().__init__(model, color)
#         self.__max_speed = max_speed
#
#     def accelerate(self, speed_increase):
#         if self.get_speed() + speed_increase > self.__max_speed:
#             return
#         else:
#             super().accelerate(speed_increase)
#
#     def get_max_speed(self):
#         print(self.__max_speed)
#
# tesla = Car("tesla", "black", 150 )
# tesla.get_speed()
# tesla.accelerate(10)
# tesla.get_speed()


#3----------------------------------------------

class DigitalSafe:
    def __init__(self, safe_id, code):
        self._safe_id = safe_id
        self.__code_hash = hash(code)
        self.__is_locked = False
        self.__attempt_count = 0

    def __str__(self):
        if self.__is_locked:
            status ="locked"
        else:
            status = "open"
        return  f" safe no. : {self._safe_id} | status: {status} | failed attempt: {self.__attempt_count}"

    def try_unlock(self, code):
        if not self.__is_locked:
            print("the safe is already open")
            return

        if self.__attempt_count >= 3:
            print("too many attempts")
            return

        if hash(code) == self.__code_hash:
            self.__is_locked = False
            self.reset_attempts()
            print("safe unlocked")
        else:
            self.__attempt_count += 1
            print("wrong password, try again")


    def lock(self):
        self.__is_locked = True


    def is_locked(self):
        if self.__is_locked:
            print("the safe is locked")
        else:
            print("the safe is not locked")


    def get_attampts_left(self):
        return 3 - self.__attempt_count


    def reset_attempts(self):
        if not self.__is_locked:
            self.__attempt_count = 0



safe1 = DigitalSafe("a123", 0000)

print(safe1)


#4---------------------------------------














