# Find All Four Sum Numbers

# Given an array of integers and another number. Find all the unique quadruple from the given array that sums up to the given number.
#
# Example 1:
#
# Input:
# N = 5, K = 3
# A[] = {0,0,2,1,1}
# Output: 0 0 1 2 $
# Explanation: Sum of 0, 0, 1, 2 is equal
# to K.

# Example 2:
#
# Input:
# N = 7, K = 23
# A[] = {10,2,3,4,5,7,8}
# Output: 2 3 8 10 $2 4 7 10 $3 5 7 8 $
# Explanation: Sum of 2, 3, 8, 10 = 23,
# sum of 2, 4, 7, 10 = 23 and sum of 3,
# 5, 7, 8 = 23.

def fourSum(nums,k):
    x = 0
    y = 1
    z = 2
    n = 3
    l = []
    while True:
        if x < len(nums):
            if y < len(nums):
                if z < len(nums):
                    if n < len(nums):
                        if nums[x]+nums[y]+nums[z]+nums[n] == k:
                            value = ' '.join(list(map(str,sorted([nums[x],nums[y],nums[z],nums[n]]))))
                            if value not in l:
                                l.append(value)

                        n = n + 1
                    else:
                        z += 1
                        n = z + 1
                else:
                    y = y + 1
                    z = y
            else:
                x = x + 1
                y = x
        else:
            break
    print('$'.join(l))

for value in [[[0,0,2,1,1],3],[[10,2,3,4,5,7,8],23]]:
    print(f'Input is {value}')
    fourSum(*value)