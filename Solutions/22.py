# Factorials of large numbers 

# Given an integer, the task is to find factorial of the number.
 
# Input:
# The first line of input contains an integer T denoting the number of test cases.  
# The first line of each test case is N,the number whose factorial is to be found
 
# Output:
# Print the factorial of the number in separate line.

# Example:
# Input
# 3
# 5
# 10
# 2
 
# Output
# 120
# 3628800
# 2

from functools import reduce

def fact(number):
    result  = 1
    for y in range(1,number+1):
        result = result * y
    return result

def factorial(nums):
    for x in nums:
        #Solution 1
        print(f'factorial is {reduce(lambda x,y:x*y,range(1,x+1))}')

        #Solution 2
        print(list(map(fact,nums)))


if __name__ == '__main__':
    list_of_values = [[3,5,10,2]]
    for li in list_of_values:
        print(f'Input is {li}')
        factorial(li)