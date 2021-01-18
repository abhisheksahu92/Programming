# Count pairs with given sum 

# Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


# Example 1:

# Input:
# N = 4, K = 6
# arr[] = {1, 5, 7, 1}
# Output: 2
# Explanation: 
# arr[0] + arr[1] = 1 + 5 = 6 
# and arr[1] + arr[3] = 5 + 1 = 6.


def getPairsCount(numswithk):
    nums = numswithk[0]
    k = numswithk[1]
    count = 0
    for x in range(len(nums)):
        for y in range(x+1,len(nums)):
            if nums[x] + nums[y] == k:
                count = count + 1
    return count
    #return nums
                 
if __name__ == '__main__':
    list_of_values = [[[1, 5, 7, 1],6],[[1, 1, 1, 1],2]]
    for li in list_of_values:
        print(f'Input is {li[0]} and sum is {li[1]}')
        print(f'Count is {getPairsCount(li)}')