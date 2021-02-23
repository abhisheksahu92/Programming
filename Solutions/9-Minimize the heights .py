# Minimize the heights 

# Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. 
# Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.

# Example 1:

# Input:
# K = 2, N = 4
# Arr[] = {1, 5, 8, 10}
# Output: 5
# Explanation: The array can be modified as 
# {3, 3, 6, 8}. The difference between 
# the largest and the smallest is 8-3 = 5.

import random

def TowerHeight(array,k):
    smallest = []
    largest = []
    for x in array:
        if x - k > 0:
            smallest.append(x-k)
        largest.append(x+k)
    if min(smallest) < min(largest):
        small = min(smallest)
    else:
        small = min(largest)
    
    if max(smallest) < max(largest):
        large = max(smallest)
    else:
        large = max(largest)
    
    return large-small

if __name__ == '__main__':
    list_of_values = [3, 9, 12, 16, 20]
    K = 3
    print(f'Input: {list_of_values}')
    print(f'Minimum possible hieght is {TowerHeight(list_of_values,K)}')

    
