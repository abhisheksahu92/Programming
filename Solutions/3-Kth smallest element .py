#Kth smallest element 

# Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element 
# in the given array. It is given that all array elements are distinct.

import random

def kthsmallest(array,kth):
    for x in range(kth):
        min = x
        for y in range(x+1,len(array)):
            if array[min] > array[y]:
                min = y
        array[x],array[min] = array[min],array[x]
    return array[kth-1]

if __name__ == '__main__':
    list_of_values = random.sample(range(10,100),10)
    kthvalue = random.randint(1,len(list_of_values))
    print(f'Input: {list_of_values}')
    print(f'value is {kthvalue}')
    value = kthsmallest(list_of_values,kthvalue)
    print(f'Kth Smallest value is {value}')
    