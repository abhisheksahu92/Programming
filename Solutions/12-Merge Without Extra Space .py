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

def mergewithoutspace(nums):
    array1 = nums[0]
    array2 = nums[1]
    for x in range(len(array1)):
        for y in range(len(array2)):
            if array1[x] > array2[y]:
                array1[x],array2[y] = array2[y],array1[x]
    array2.sort()
    return array1 + array2
                

if __name__ == '__main__':
    list_of_values = [[[1, 3, 5, 7],[0, 2, 6, 8, 9]],[[10, 12],[5, 18, 20]]]
    for li in list_of_values:
        print(f'Input is {li}')
        print(f'duplicate value is {mergewithoutspace(li)}')

