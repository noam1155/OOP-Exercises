


#1---------------------------

class Person:
    def __init__(self,name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"hello, my name is {self.name},i am {self.age} years old, i'm from {self.city} ")

    def happy_bitrhday(self):
        self.age += 1
        print(f"now im {self.age} !")


yossi = Person("yossi", 40, "tel aviv")
david = Person("david", 30, "jerusalem")
moshe = Person("moshe", 20, "bnei brak")

Person.introduce(yossi)
Person.introduce(david)
Person.introduce(moshe)

Person.happy_bitrhday(david)

#2------------------------------------

class Mosad:
    def __init__(self, name, type, students_count, city):
        self.name = name
        self.type = type
        self.students_count = students_count
        self.city = city

    def print_details(self):
        print("--- פרטי מוסד ---")
        print(f"שם המוסד: {self.name}")
        print(f"סוג המוסד: {self.type}")
        print(f"עיר: {self.city}")
        print(f"מספר תלמידים: {self.students_count}")
        print("-----------------")

    def add_students(self, amount):
        self.students_count += amount
        print(f"נוספו {amount} תלמידים ל{self.name}. סך הכל עכשיו: {self.students_count}")

    def remove_students(self, amount):
        if self.students_count - amount < 0:
            print(f"שגיאה: הפעולה בוטלה. אי אפשר להוריד תלמידים, הכמות תרד מתחת ל-0 ב{self.name}!")
        else:
            self.students_count -= amount
            print(f"הוסרו {amount} תלמידים מ{self.name}. סך הכל עכשיו: {self.students_count}")


uni = Mosad("האוניברסיטה הפתוחה", "אוניברסיטה", 50000, "רעננה")
school = Mosad("תיכון עירוני א'", "תיכון", 1200, "תל אביב")

Mosad.print_details(uni)
Mosad.print_details(school)

uni.add_students(50)
school.remove_students(20)

Mosad.print_details(uni)
Mosad.print_details(school)

















