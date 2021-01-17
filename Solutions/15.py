# Next Permutation

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]

# Example 4:
# Input: nums = [1]
# Output: [1]

import random

def nextpermutation(nums):
    minimum = int(''.join(list(map(str,nums)))) + 1
    nums.sort(reverse=True)
    maximum = int(''.join(list(map(str,nums)))) + 1

    if minimum == maximum:
        return nums[::-1]

    for x in range(minimum,maximum):
        temp_list = []
        temp_value = x 
        while temp_value > 0:
            temp_list.append(temp_value%10)
            temp_value = temp_value // 10
        
        temp_list.sort(reverse=True)
        if temp_list == nums:
            return [int(y) for y in str(x)]
            
if __name__ == '__main__':
    list_of_values = [[1,2,3],[3,2,1],[1,1,5],[1]]
    for li in list_of_values:
        print(f'Input is {li}')
        print(f'Next Permutation is {nextpermutation(li)}')   