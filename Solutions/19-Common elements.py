# Common elements 

# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?

# Example 1:

# Input:
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
# Explanation: 20 and 80 are the only
# common elements in A, B and C.


def commonelement(nums):
    A = nums[0]
    B = nums[1]
    C = nums[2]
    count = {}
    for a in A:
        count[a] = count.get(a,0) + 1
    for b in B:
        count[b] = count.get(b,0) + 1
    for c in C:
        count[c] = count.get(c,0) + 1
    
    for x,y in count.items():
        if y == 3:
            print(x,end=' ')
                 
if __name__ == '__main__':
    list_of_values = [[[1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]]]
    for li in list_of_values:
        print(f'Input is {li[0]} and sum is {li[1]}')
        commonelement(li)