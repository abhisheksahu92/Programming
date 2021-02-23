# Zero Sum Subarrays

# You are given an array A[] of size N. Find the total count of sub-arrays having their sum equal to 0.
#
#
# Example 1:
#
# Input:
# N = 6
# A[] = {0,0,5,5,0,0}
# Output: 6
# Explanation: The 6 subarrays are
# [0], [0], [0], [0], [0,0], and [0,0].
#
#
# Example 2:
#
# Input:
# N = 10
# A[] = {6,-1,-3,4,-2,2,4,6,-12,-7}
# Output: 4
# Explanation: The 4 subarrays are [-1 -3 4]
# [-2 2], [2 4 6 -12], and [-1 -3 4 -2 2]

from itertools import combinations
def findSubarray(arr):
    x = 0
    y = 0
    count = 0
    while True:
        if x < len(arr):
            if y < len(arr):
                if sum(arr[x:y+1]) == 0:
                    count += 1
                y += 1
            else:
                x = x + 1
                y = x
        else:
            break
    return count

for value in [[0,0,5,5,0,0],[6,-1,-3,4,-2,2,4,6,-12,-7]]:
    print(f'Input is {value}')
    print(findSubarray(value))