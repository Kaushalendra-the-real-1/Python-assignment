# class Person:
#     def __init__(self):
#         print("Hello Reader ... ")
# class Male(Person):
#     def get_gender(self):
#         print("I am from Male Class")
# class Female(Person):
#     def get_gender(self):
#         print("I am from Female Class")

# Obj = Female()
# Obj.get_gender()

# ----------------------------------------------------------------------------------------------------------------------
# Bonus Section

from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_gender(self):
        return 0
class Male(Person):
    def get_gender(self):
        print("I am from Male Class")
class Female(Person):
    def get_gender(self):
        print("I am from Female Class")
unknown = Person() #expecteed to throw an error.
