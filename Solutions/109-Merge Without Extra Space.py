# Merge Without Extra Space
# Given two sorted arrays arr1[] of size N and arr2[] of size M. Each array is sorted in non-decreasing order. Merge the two arrays into one sorted array in non-decreasing order without using any extra space.
#
#
# Example 1:
#
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
#
# Example 2:
#
# Input:
# N = 2, M = 3
# arr1[] = {10, 12}
# arr2[] = {5, 18, 20}
# Output: 5 10 12 18 20
# Explanation: Since you can't use any
# extra space, modify the given arrays
# to form
# arr1[] = {5, 10}
# arr2[] = {12, 18, 20}

def merge(arr1,arr2):
    arr1.extend(arr2)
    for x in range(len(arr1)):
        small = x
        for y in range(x+1,len(arr1)):
            if arr1[y] < arr1[small]:
                small = y
        arr1[x],arr1[small] = arr1[small],arr1[x]
    return arr1

for value in [[[1, 3, 5, 7],[0, 2, 6, 8, 9]],[[10, 12],[5, 18, 20]]]:
    print(f'Input is {value}')
    print(merge(*value))
