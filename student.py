from enum import Enum, auto


class Gender(Enum):
    MAN = auto()
    WOMAN = auto()

    def get_title(self):
        if self == self.WOMAN:
            return "Женщина"
        else:
            return "Мужчина"


class Student:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def print(self):
        print(
            f"Name: {self.name} {self.surname};\tAge: {self.age};\t Gender: {self.gender.get_title()};\n----------------------------------\n")

    def is_military_acceptable(self):
        return self.age > 17 and self.gender == Gender.MAN

# umar = Student("Umar", "Mansurov", 18, Gender.MAN)
# # umar.print()
# samad = Student("Samad", "Qodirov", 17, Gender.MAN)
# madina = Student("Madina", "Shamsiyeva", 18, Gender.WOMAN)
# gr1 = [umar, samad, madina]
#
# for s in gr1:
#     if s.is_military_acceptable():
#         s.print()
