# Longest consecutive subsequence

# Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
 

# Example 1:

# Input:
# N = 7
# a[] = {2,6,1,9,4,5,3}
# Output:
# 6
# Explanation:
# The consecutive numbers here
# are 1, 2, 3, 4, 5, 6. These 6 
# numbers form the longest consecutive
# subsquence.

import math

def fact(number):
    pass

def consecutiveSequence(nums):

    # Solution 1
    nums.sort()
    min = nums[0]
    for x in range(1,len(nums)):
        if nums[x]-1 == min:
            min = nums[x]
        else:
            print(nums[0:min])
            break

if __name__ == '__main__':
    list_of_values = [[2,6,1,9,4,5,3],[1,9,3,10,4,20,2]]
    for li in list_of_values:
        print(f'Input is {li}')
        consecutiveSequence(li)