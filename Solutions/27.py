# Array Subset of another array 

# Example:
# Input:
# 3
# 6 4
# 11 1 13 21 3 7
# 11 3 7 1
# 6 3
# 1 2 3 4 5 6
# 1 2 4
# 5 3
# 10 5 2 23 19
# 19 5 3

# Output:
# Yes
# Yes
# No

# Explanation:
# Testcase 1: (11, 3, 7, 1) is a subset of first array.



def IsSubArray(nums):
    array1 = list(map(int,nums[0].split()))
    array2 = list(map(int,nums[1].split()))
    print(all(list(map(lambda x: True if x in array1 else False,array2))))

if __name__ == '__main__':
    list_of_values = [['11 1 13 21 3 7','11 3 7 1'],['1 2 3 4 5 6','1 2 3'],['10 5 2 23 19','19 5 3']]
    for li in list_of_values:
        print(f'Input is {li}')
        IsSubArray(li)
