import re
count = 0
with open('file.txt','r') as f:
    for line in f.readlines():
        count += len(re.findall(f'[A-Z]',line))

# - Inheritance
# - polymorphism
# - abstraction
# - Encapsulation

# private = _ - used in class and child class
# protected = __

# list = [1,2,3,4] - changeble - mutable
# tuple = (1,2,3,4) - unchangeable - immutable

# list_of_cars = ((1,'Ford'),(2,'Acura'),(3,'Farrari'))
# Charfield(choices = list_of_cars)

# def __del__(self):
#     pass
# import pytest,Phone
# @pytest.fixture(autouse=True)
#     d = Phone.objects.create(*args)
#
# def test_get_name():

# Person.object.filter(user_id=user_id).exists()
# Person.object.get(user_id=user_id).exists()

# Person.objects.filter(brand)