#Maximum and minimum of an array using minimum number of comparisons
import random

def maximum(array):
    max = 0
    for y in range(1,len(array)):
        if array[max] < array[y]:
            max = y
    return array[max]

def minimum(array):
    min = 0
    for y in range(1,len(array)):
        if array[min] > array[y]:
            min = y
    return array[min]

if __name__ == '__main__':
    list_of_values = random.sample(range(10,100),10)
    print(f'Input: {list_of_values}')
    maximum_value =  maximum(list_of_values)
    print(f'Maximum Value is {maximum_value}')

    minimum_value =  minimum(list_of_values)
    print(f'Minimum Value is {minimum_value}')
