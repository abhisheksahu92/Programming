# Sort an array of 0s, 1s and 2s 

# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

#Maximum and minimum of an array using minimum number of -comparisons
import random

def sort012(array):
    l = []
    for x in [0,1,2]:
        for y in array:
            if x == y:
                l.append(x)
    return l

if __name__ == '__main__':
    list_of_values = random.choices([0,1,2],k=10)
    print(f'Input: {list_of_values}')
    print(f'Sorted Array is {sort012(list_of_values)}')
    
