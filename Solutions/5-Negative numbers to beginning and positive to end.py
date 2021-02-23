# Move all negative numbers to beginning and positive to end with constant extra space

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

import random

def sortnegpos(array):
    new_array = []
    for x in array:
        if x < 0:
            new_array.insert(0,x)
        else:
            new_array.append(x)
    return new_array


if __name__ == '__main__':
    list_of_values = random.sample(range(-100,100),10)
    print(f'Input: {list_of_values}')
    print(f'Sorted array is {sortnegpos(list_of_values)}')
