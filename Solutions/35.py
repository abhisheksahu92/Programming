# Find the median
# Given an array arr[] of N integers, calculate the median
 

# Example 1:

# Input: N = 5
# arr[] = 90 100 78 89 67
# Output: 89
# Explanation: After sorting the array 
# middle element is the median 

# Example 2:

# Input: N = 4
# arr[] = 56 67 30 79â€‹
# Output: 61
# Explanation: In case of even number of 
# elemebts average of two middle elements 
# is the median

def find_median(nums):
    nums = sorted(list(map(int,nums.split())))
    length = len(nums)
    if length % 2 == 0:
        print((nums[length // 2] + nums[(length // 2) - 1]) // 2)
    else:
        print(nums[len(nums) // 2])
    print(nums)

if __name__ == '__main__':
    values = ['90 100 78 89 67','56 67 30 79']
    for value in values:
        find_median(value)

