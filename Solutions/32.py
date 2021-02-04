# Three way partitioning 

# Given an array of size N and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.
# The individual elements of three sets can appear in any order. You are required to return the modified array.


# Example 1:

# Input: 
# N = 5
# A[] = {1, 2, 3, 3, 4}
# [a, b] = [1, 2]
# Output: 1
# Explanation: One possible arrangement is:
# {1, 2, 3, 3, 4}. If you return a valid
# arrangement, output will be 1.

def threeWayPartition(nums,element):
    d = {'small':[],'middle':[],'large':[]}
    l = []
    a,b = element
    for x in nums:
        if x <= a:
            d['small'].append(x)
        elif x >= b:
            d['large'].append(x)
        elif x > a and x < b:
            d['middle'].append(x)
    for x in d.values():
        l.extend(x)
    print(l)


if __name__ == '__main__':
    li = [[[1, 2, 3, 3, 4],[1, 2]],[[1, 2, 3],[1,3]]]
    for input in li:
        print(f'Input is {input[0]} and element is {input[1]}')
        threeWayPartition(*input)
