# Inversion of array 

# Given an array of integers. Find the Inversion Count in the array. 
# Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 
# Example 1:
# Input: N = 5, arr[] = {2, 4, 1, 3, 5}
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5 
# has three inversions (2, 1), (4, 1), (4, 3).

def inversearray(nums):
    count = 0
    for x in range(len(nums)):
        for y in range(x+1,len(nums)):
            if nums[x] > nums[y] and x < y:
                count = count + 1
                nums[x],nums[y] = nums[y],nums[x]
    return count 
    

if __name__ == '__main__':
    list_of_values = [[2, 4, 1, 3, 5],[2, 3, 4, 5, 6],[10,10,10]]
    for li in list_of_values:
        print(f'Input is {li}')
        print(f'Inverse Array count is {inversearray(li)}')
