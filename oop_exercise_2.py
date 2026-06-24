
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


class Student(Person):
    def __init__(self, name, age, city, student_id, grade):
        super().__init__(name, age, city)

        self.student_id = student_id
        self.grade = grade

    def study(self):
        print(f"{self.name} study in grade {self.grade}")

    def introduce(self):
        print(f"hello, my name is {self.name}, i am {self.age} years old, i'm from {self.city}, studying in grade {self.grade}")

    def advance_grade(self, new_grade):
        self.grade = new_grade
        print(f"Congratulations! {self.name} advanced to grade {self.grade}")

class Teacher(Person):
    def __init__(self, name, age, city, subject, years_experience):
        super().__init__(name, age, city)
        self.subject = subject
        self.years_experience = years_experience

    def teach(self):
        print(f"{self.name} teach {self.subject} already {self.years_experience} years ")

    def introduce(self):
        print(f"hello, my name is {self.name}, i am {self.age} years old, i'm from {self.city}, and i'm teaching {self.subject}")

    def gain_experience(self, amount):
        self.years_experience += amount


class Principal(Person):
    def __init__(self, name, age, city, years_experience):
        super().__init__(name, age, city)
        self.years_of_principal = years_experience

    def manage(self):
        print(f"{self.name} managing this school for {self.years_of_principal} years")

    def introduce(self):
        print(f"hello, my name is {self.name}, i am {self.age} years old, i'm from {self.city}, principal of this mosad")

    def add_management_experience(self, amount):
        self.years_of_principal += amount



student1 = Student("noam", 23, "kiryat shmona", 123123, "a")
teacher1 = Teacher("moshe", 40, "bnei brak", "math", 10)
principal1 = Principal("haim", 60, "tel aviv", 20)

print()
print("*" * 50 )
print()

student1.introduce()
teacher1.introduce()
principal1.introduce()

print()
print("*" * 50 )
print()

student1.study()
teacher1.teach()
principal1.manage()

print()
print("*" * 50 )
print()

student1.advance_grade("b")
teacher1.gain_experience(1)
principal1.add_management_experience(1)

print()
print("*" * 50 )
print()

student1.study()
teacher1.teach()
principal1.manage()















