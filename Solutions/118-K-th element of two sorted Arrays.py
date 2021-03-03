# K-th element of two sorted Arrays

# Given two sorted arrays arr1 and arr2 of size M and N respectively and an element K. The task is to find the element that would be at the k’th position of the final sorted array.
#
#
# Example 1:
#
# Input:
# arr1[] = {2, 3, 6, 7, 9}
# arr2[] = {1, 4, 8, 10}
# k = 5
# Output:
# 6
# Explanation:
# The final sorted array would be -
# 1, 2, 3, 4, 6, 7, 8, 9, 10
# The 5th element of this array is 6.

# Example 2:
#
# Input:
# arr1[] = {100, 112, 256, 349, 770}
# arr2[] = {72, 86, 113, 119, 265, 445, 892}
# k = 7
# Output:
# 256
# Explanation:
# Final sorted array is - 72, 86, 100, 112,
# 113, 119, 256, 265, 349, 445, 770, 892
# 7th element of this array is 256.

def kthElement(arr1,arr2,k):
    i,j = 0,0
    li = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            li.append(arr1[i])
            i += 1
        else:
            li.append(arr2[j])
            j += 1
    return li[k-1]

for value in [[[2, 3, 6, 7, 9],[1, 4, 8, 10],5],[[100, 112, 256, 349, 770],[72, 86, 113, 119, 265, 445, 892],7]]:
    print(f'Input is {value}')
    print(kthElement(*value))
