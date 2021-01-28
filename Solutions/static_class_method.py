from datetime import date

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def personByYear(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def isAdult(age):
        if age>18:
            return 'Adult'
        else:
            return 'Not Adult'

p1 = Person('Abhi',27)
p2 = Person.personByYear('Abhi',1993)
print(p1.name,p1.age)
print(p2.name,p2.age)
print(f'check if person with 31 age is {p1.isAdult(31)}')