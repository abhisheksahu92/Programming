# Count triplets with sum smaller than X

# Given an array arr[] of distinct integers of size N and a sum value X, the task is to find count of triplets with the sum smaller than the given sum value X.
#
#
#
# Example 1:
#
# Input: N = 6, X = 2
# arr[] = {-2, 0, 1, 3}
# Output:  2
# Explanation: Below are triplets with
# sum less than 2 (-2, 0, 1) and (-2, 0, 3).
#
#
# Example 2:
#
# Input: N = 5, X = 12
# arr[] = {5, 1, 3, 4, 7}
# Output: 4
# Explanation: Below are triplets with
# sum less than 12 (1, 3, 4), (1, 3, 5),
# (1, 3, 7) and (1, 4, 5).

def countTriplets(nums,k):
    x = 0
    y = 1
    z = 2
    while True:
        if x < len(nums):
            if y < len(nums):
                if z < len(nums):
                    if nums[x]+nums[y]+nums[z] < k:
                        print(sorted([nums[x],nums[y],nums[z]]))
                    z = z + 1
                else:
                    y = y + 1
                    z = y + 1
            else:
                x = x + 1
                y = x
        else:
            break
    return nums,k

for value in [[[-2, 0, 1, 3],2],[[5, 1, 3, 4, 7],12]]:
    print(f'Input is {value}')
    print(countTriplets(*value))