# Minimum Swaps to Sort

# Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.
#
#
# Example 1:
#
# Input:
# nums = {2, 8, 5, 4}
# Output:
# 1
# Explaination:
# swap 8 with 4.
#
# Example 2:
#
# Input:
# nums = {10, 19, 6, 3, 5}
# Output:
# 2
# Explaination:
# swap 10 with 3 and swap 19 with 5.

def minSwaps(arr):
    count = 0
    for x in range(len(arr)):
        small = x
        for y in range(x+1,len(arr)):
            if arr[y] < arr[small]:
                small = y
        if x != small:
            count += 1
            arr[x],arr[small] = arr[small],arr[x]
    return count

for value in [[2, 8, 5, 4],[10, 19, 6, 3, 5]]:
    print(f'Input is {value}')
    print(minSwaps(value))