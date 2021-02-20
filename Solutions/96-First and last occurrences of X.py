# First and last occurrences of X
# Given a sorted array with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.
#
# Note: If the number x is not found in the array just print '-1'.
#
# Input:
# The first line consists of an integer T i.e number of test cases. The first line of each test case contains two integers n and x. The second line contains n spaced integers.
#
# Output:
# Print index of the first and last occurrences of the number x with a space in between.

# Example:
# Input:
# 2
# 9 5
# 1 3 5 5 5 5 67 123 125
# 9 7
# 1 3 5 5 5 5 7 123 125
#
# Output:
# 2 5
# 6 6
def firstlastindex(li,nums):
    li = list(map(int,li.split()))
    l2 = [x for x in range(len(li)) if li[x] == nums]
    print(l2[0],l2[-1])

for value in [['1 3 5 5 5 5 67 123 125',5],['1 3 5 5 5 5 7 123 125',7]]:
    print(f'Input is {value}')
    firstlastindex(*value)