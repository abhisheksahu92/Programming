# Triplet Sum in Array 

# Given an array arr of size N and an integer K. Find if there's a triplet in the array which sums up to the given integer K.


# Example 1:

# Input:
# N = 6, K = 13
# arr[] = [1 4 45 6 10 8]
# Output:
# true
# Explanation:
# The triplet {1, 4, 8} in 
# the array sums up to 13.

def tripleSum(nums):
    sum_ = nums[1]
    nums = list(map(int,nums[0].split()))

    x = 0
    y = x + 1
    while True:
        if x < len(nums):
            if y < len(nums):
                third = sum_ - (nums[x]+nums[y])
                if third in nums[y+1:]:
                    print(nums[x],nums[y],third)
                y = y + 1
            else:
                x = x + 1
                y = x + 1
        else:
            break
    print(nums)

if __name__ == '__main__':
    values = [['1 4 45 6 10 8',13]]
    for value in values:
        print(f'Input is {value}')
        tripleSum(value)