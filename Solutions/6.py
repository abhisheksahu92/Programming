# Union of two arrays
# Input:
# 5 3
# 1 2 3 4 5
# 1 2 3

# Output: 
# 5

# Explanation: 
# 1, 2, 3, 4 and 5 are the
# elements which comes in the union set
# of both arrays. So count is 5.

import random

def union(array,array1):
    for x in array1:
        if x not in array:
            array.append(x)
    return array
    
if __name__ == '__main__':
    array1 = random.sample(range(1,10),k=5)
    array2 = random.sample(range(1,10),k=5)
    print(f'Input: {array1} and {array2}')
    print(f'Count of Union is {len(union(array1,array2))}')