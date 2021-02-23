# Rearrange array in alternating positive & negative items with O(1) extra space

# Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa maintaining the order of appearance. 
# Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.

# Examples : 

# Input:  arr[] = {1, 2, 3, -4, -1, 4}
# Output: arr[] = {-4, 1, -1, 2, 3, 4}

# Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0} 

def ordernegativepositive(nums):
    list_ = []
    list_2 = []
    for x in nums:
        if x < 0:
            list_.insert(0,x)
        else:
            list_.append(x)
    print(list_)
    start = 0
    end = None
    while True:
        if list_[start] > 0:
            end = start - 1
            break
        start = start + 1

    while True:
        if end >= 0:
            list_2.append(list_[end])
            list_2.append(list_[start])
            start =  start + 1
            end = end - 1
        else:
            list_2.extend(list_[start:])
            break
    print(list_2) 

if __name__ == '__main__':
    list_of_values = [[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8],[1, 2, 3, -4, -1, 4]]
    for li in list_of_values:
        print(f'Input is {li}')
        ordernegativepositive(li)

