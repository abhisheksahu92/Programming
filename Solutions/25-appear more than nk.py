# Given an array of size n and a number k, find all elements that appear more than n/k times

# Given an array of size n, find all elements in array that appear more than n/k times. For example, if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. Note that size of array is 8 (or n = 8), so we need to find all elements that appear more than 2 (or 8/4) times. There are two elements that appear more than two times, 2 and 3. 

# Consider k = 4, n = 9 
# Given array: 3 1 2 2 2 1 4 3 3 

import math

def fact(number):
    pass

def countMoreThanNK(nums):
    nums_ = list(map(int,nums[0].split()))
    count = len(nums_) //  nums[1]
    d = {}

    for x in nums_:
        d[x] = d.get(x,0) + 1
        if d[x] > count:
            print(x)
        
if __name__ == '__main__':
    list_of_values = [['3 1 2 2 2 1 4 3 3',4]]
    for li in list_of_values:
        print(f'Input is {li[0]} and k is {li[1]}')
        countMoreThanNK(li)
