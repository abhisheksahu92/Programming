# Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
                            
# Merge Without Extra Space 

# Given two sorted arrays arr1[] of size N and arr2[] of size M. Each array is sorted in non-decreasing order. Merge the two arrays into one sorted array in non-decreasing order without using any extra space.


# Example 1:

# Input:
# N = 4, M = 5
# arr1[] = {1, 3, 5, 7}
# arr2[] = {0, 2, 6, 8, 9}
# Output: 0 1 2 3 5 6 7 8 9
# Explanation: Since you can't use any 
# extra space, modify the given arrays
# to form 
# arr1[] = {0, 1, 2, 3}
# arr2[] = {5, 6, 7, 8, 9}

import random

def mergeinterval(nums):
    index = 0
    while index < len(nums) - 1 :
        if nums[index][1] >= nums[index+1][0]:
            variable = [nums[index][0],nums[index+1][1]]
            nums.pop(index)
            nums.pop(index)
            nums.insert(index,variable)
        else:
            index = index + 1
    return nums
        

if __name__ == '__main__':
    list_of_values = [[[1,3],[2,6],[8,10],[12,18]],[[1,4],[4,5]]]
    for li in list_of_values:
        print(f'Input is {li}')
        print(f'Merge interval value is {mergeinterval(li)}')


