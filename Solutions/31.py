# Smallest subarray with sum greater than x 

# Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value.

# Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).

# Example 1:

# Input:
# A[] = {1, 4, 45, 6, 0, 19}
# x  =  51
# Output: 3
# Explanation:
# Minimum length subarray is 
# {4, 45, 6}

def smallestSubarray(nums,element):
    d = {}
    print(nums,element)
    x,y = 0,0
    while True:
        if x < len(nums):
            if y < len(nums):
                sum1 = sum(nums[x:y+1])
                if sum1 > element:
                    if sum1 not in d:
                        d[sum1] = nums[x:y+1]
                    else:
                        if len(d[sum1]) > len(nums[x:y+1]):
                            d[sum1] = nums[x:y+1]
                y = y + 1
            else:
                x = x + 1
                y = x
        else:
            break
    print(d[sorted(d)[0]])

if __name__ == '__main__':
    li = [[[1, 4, 45, 6, 0, 19],51],[[1, 10, 5, 2, 7],9]]
    for input in li:
        print(f'Input is {input[0]} and element is {input[1]}')
        smallestSubarray(*input)