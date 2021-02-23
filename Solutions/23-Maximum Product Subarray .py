# Maximum Product Subarray 

# Given an array Arr that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.

# Example 1:

# Input:
# N = 5
# Arr[] = {6, -3, -10, 0, 2}
# Output: 180
# Explanation: Subarray with maximum product
# is  6, -3, -10 which gives product as 180.

import math

def fact(number):
    pass

def maxProduct(nums):
    x,y = 0,1
    max_product = 0
    while True:
        if x < len(nums):
            product = abs(math.prod(nums[x:y]))
            if product > max_product:
                max_product =product
            y = y + 1
            if y < len(nums):
                continue
            else:
                x = x + 1
                y = x + 1
        else:
            break
    print(max_product)


if __name__ == '__main__':
    list_of_values = [[6, -3, -10, 0, 2],[2, 3, 4, 5, -1, 0]]
    for li in list_of_values:
        print(f'Input is {li}')
        maxProduct(li)
