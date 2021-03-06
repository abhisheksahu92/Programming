# Find Missing And Repeating

# Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.
#
# Example 1:
#
# Input:
# N = 2
# Arr[] = {2, 2}
# Output: 2 1
# Explanation: Repeating number is 2 and
# smallest positive missing number is 1.

# Example 2:
#
# Input:
# N = 3
# Arr[] = {1, 3, 3}
# Output: 3 2
# Explanation: Repeating number is 3 and
# smallest positive missing number is 2.

def findTwoElement(li,N):
    d = {}
    repeating = []
    missing = []
    for x in range(1,N+1):
        if x not in li:
            missing.append(str(x))
        else:
            if li.count(x) > 1:
                repeating.append(str(x))
    print(' '.join(repeating+missing))
    print(li,N)

for value in [[[2,2],2],[[1,3,3],3]]:
    print(f'Input is {value}')
    findTwoElement(*value)
