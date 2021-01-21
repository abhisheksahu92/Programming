import copy

def bubbleSort(nums):
    nums2 = copy.deepcopy(nums)
    
    # Solution 1
    for x in range(len(nums)-1,0,-1):
        for y in range(x):
            if nums[x] < nums[y]:
                nums[x],nums[y] = nums[y],nums[x]

    # Solution 2
    x = 0
    y = x + 1
    while True:
        if x < len(nums2):
            if y < len(nums2):
                if nums2[x] < nums2[y]:
                    nums2[x],nums2[y] = nums2[y],nums2[x]
                y = y + 1
            else:
                x = x + 1
                y = x + 1
        else:
            break
    print(nums)
    print(nums2)
          
if __name__ == '__main__':
    list_of_values = [[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]]
    
    for li in list_of_values:
        print(f'Input is {li}')
        bubbleSort(li)