# What is the difference -
array1 = list(range(10))
array2 = array1
array3 = array1[:]

#decorator
# def print_argu(func):
#     def wraps(*args):
#         print(*args)
#         func(*args)
#     return wraps
#
# @print_argu
# def get_Argument(a,b,c):
#     print(a+b+c)
#
# get_Argument(1,2,3)

# 0,1,1,2,3,5
# 2 febo(1) + febo(0)
# 3 febo(2) + febo(1)
# 4 febo(3) + febo(2)
# enb

# def febo_recur(index,d = {}):
#     if index in d:
#         return d[index]
#     if index in [0,1]:
#         return index
#     value  = febo_recur(index-1,d) + febo_recur(index-2,d)
#     d[index] = value
#     return value



# print(febo_recur(50))

# Given a table employee_salary with columns employee and salary give me a query to find the second
# highest salary of an employee.
#
# select salary from employee_salary order by salary desc limit 1 offset 1

class A:
  def __init__(self, a, b):
    self.__a = a
    self.__b = b




