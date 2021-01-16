# Minimum number of jumps 

# Given an array of integers where each element represents the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

# Example 1:

# Input:
# N=11 
# arr=1 3 5 8 9 2 6 7 6 8 9 
# Output: 3 
# Explanation: 
# First jump from 1st element to 2nd 
# element with value 3. Now, from here 
# we jump to 5th element with value 9, 
# and from here we will jump to last. 

import random

def minjump(array):
    length = len(array) - 1
    jumps = 0
    start = 0
    while start < length:
        start = start + array[start]
        jumps += 1
    return jumps


if __name__ == '__main__':
    list_of_values = list(map(int,'1 3 5 8 9 2 6 7 6 8 9'.split()))
    print(f'Input: {list_of_values}')
    print(f'Number of Jumps is {minjump(list_of_values)}')
