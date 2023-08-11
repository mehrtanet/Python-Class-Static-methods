# Methods : instsnce|Regular , class, static

import datetime

# Instance methode ----------------------------------------------

# class Person():
#     def __init__(self, fname, lname):
#         self.name = fname
#         self.family = lname
#
#     def show(self):
#         print(f'My name is {self.name} {self.family} .')
#
# person = Person('David', 'Daribi')
# person.show()



# Class methode ----------------------------------------------

class Person():
    def __init__(self, fname, lname, age):
        self.name = fname
        self.family = lname
        self.age = age

    def show(self):
        print(f'My name is {self.name} {self.family} and {self.age} yaers old. .')

    @classmethod
    def from_birth(cls, fname, lname, age):
        return cls( fname, lname, datetime.datetime.now().year - age )

    @staticmethod
    def is_adult(age):
        if age > 18:
            print(' is Adult ...')
        else:
            print(' ist Adult ...')

person = Person.from_birth('David', 'Daribi', 1984)
person.show()

Person.is_adult(39)
