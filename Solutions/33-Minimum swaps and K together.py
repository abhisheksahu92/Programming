# Minimum swaps and K together 
# Given an array of n positive integers and a number k. Find the minimum number of swaps required to bring all the numbers less than or equal to k together.
# Input : arr[ ] = {2, 1, 5, 6, 3} and K = 3
# Output : 1
# Explanation:
# To bring elements 2, 1, 3 together, swap element '5' with '3'
# such that final array will be- arr[] = {2, 1, 3, 6, 5}

def minswap(nums,element):
    for x in range(len(nums)):
        if nums[x] > element:
            l = nums[x:]
            small = len(list(filter(lambda x: x <= element,l)))
            large = len(list(filter(lambda x: x > element,l)))
            print(min([small,large]))
            break

if __name__ == '__main__':
    li = [[[2, 7, 9, 5, 8, 7, 4],6],[[2, 1, 5, 6, 3],3]]
    for input in li:
        print(f'Input is {input[0]} and element is {input[1]}')
        minswap(*input)