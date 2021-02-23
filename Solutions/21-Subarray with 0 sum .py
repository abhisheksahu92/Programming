# Subarray with 0 sum 

# Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

# Example 1:

# Input:
# 5
# 4 2 -3 1 6

# Output: 
# Yes

# Explanation: 
# 2, -3, 1 is the subarray 
# with sum 0.

def subArrayWithZeroSum(nums):
    nums = list(map(int,nums.split()))

    #Solution 1
    for x in range(len(nums)):
        for y in range(x,len(nums)):
            if sum(nums[x:y]) == 0 and x < y:
                print(f'Sub Array is {nums[x:y]}')

    #Solution 2
    x = 0
    y = 1

    while True:
        if x < len(nums):
            if sum(nums[x:y]) == 0:
                print(f'Sub Array is {nums[x:y]}')
                if y < len(nums):
                    y = y + 1
                else:
                    x = x + 1
                    y = x + 1  
            else:
                if y < len(nums):
                    y = y + 1
                else:
                    x = x + 1
                    y = x + 1
        else:
            break

if __name__ == '__main__':
    list_of_values = ['4 2 -3 1 6','4 2 0 1 6']
    for li in list_of_values:
        print(f'Input is {li}')
        subArrayWithZeroSum(li)
