# Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.

import random

def firstduplicate(nums):
    d = {}
    for x in nums:
        if x in d.keys():
            return x
        d[x] = d.get(x,0) + 1


if __name__ == '__main__':
    list_of_values = [[1,3,4,2,2],[3,1,3,4,2],[1,1],[1,1,2]]
    for li in list_of_values:
        print(f'Input is {li}')
        print(f'duplicate value is {firstduplicate(li)}')
    