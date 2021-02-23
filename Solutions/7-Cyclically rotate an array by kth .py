# Cyclically rotate an array by kth 

# Input:
# N = 5
# A[] = {1, 2, 3, 4, 5}
# Output:
# 5 1 2 3 4

import random

def cyclicrotata(array,kth):
    return array[kth:len(array)] + array[0:kth]
    
if __name__ == '__main__':
    list_of_values = random.sample(range(10,100),10)
    print(f'Input: {list_of_values}')
    value = random.randint(1,len(list_of_values))
    print(f'Cyclic rotate by {value} is {cyclicrotata(list_of_values,value)}')

