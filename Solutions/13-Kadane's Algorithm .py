# Kadane's Algorithm 
# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

# Input:
# N = 5
# arr[] = {1,2,3,-2,5}
# Output: 9
# Explanation: Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which 
# is a contiguous subarray.

import random

def sumsubarray(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > 0: 
            nums[i] += nums[i - 1]
    return max(nums)

if __name__ == '__main__':
    list_of_values = [1,2,8,-2,1]
    print(f'Input: {list_of_values}')
    print(f'Largest subarray sum is {sumsubarray(list_of_values)}')