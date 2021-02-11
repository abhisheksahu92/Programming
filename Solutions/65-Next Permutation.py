# Next Permutation

# Implement the next permutation, which rearranges the list of numbers into Lexicographically next greater permutation of list of numbers. If such arrangement is not possible, it must be rearranged to the lowest possible order i.e. sorted in an ascending order. You are given an list of numbers arr[ ] of size N.

# Input: N = 6
# arr = {1, 2, 3, 6, 5, 4}
# Output: {1, 2, 4, 3, 5, 6}
# Explaination: The next permutation of the
# given array is {1, 2, 4, 3, 5, 6}.
#
# Input: N = 3
# arr = {3, 2, 1}
# Output: {1, 2, 3}
# Explaination: As arr[] is the last permutation.
# So, the next permutation is the lowest one.

from functools import reduce
def nextPermutation(nums):
    # Solution 1
    # l = []
    # for x in list(permutations((nums))):
    #     l.append(int(''.join(list(map(str,x)))))
    # l.sort()
    # for x in l:
    #     if x > int(''.join(list(map(str,nums)))):
    #         return list(str(x))

    # Solution 2
    if sorted(nums,reverse=True) == nums:
        return sorted(nums)
    number = int(''.join(list(map(str,nums))))
    largest_number = int(''.join(list(map(str, sorted(nums,reverse=True)))))
    for x in range(number+1,largest_number+1):
        n = list(map(int,list(str(x))))
        if sorted(n) == sorted(nums):
            return n


for value in [[1,2,3],[1, 2, 3, 6, 5, 4],[3,2,1]]:
    print(f'Input is {value}')
    print(nextPermutation(value))