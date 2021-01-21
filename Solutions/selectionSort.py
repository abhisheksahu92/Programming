def selectionSort(nums):
    # Solution 1
    # for x in range(len(nums)):
    #     minimum = x
    #     for y in range(x+1,len(nums)):
    #         if nums[minimum] > nums[y]:
    #             minimum = y
    #     nums[x],nums[minimum] = nums[minimum],nums[x] 

    # Solution 2
    x = 0
    y = x + 1
    minimum = x
    while True:
        if x < len(nums):
            if y < len(nums):
                if nums[minimum] > nums[y]:
                    minimum = y
                y = y + 1
            else:
                nums[x],nums[minimum] = nums[minimum],nums[x] 
                x = x + 1
                y = x + 1
                minimum = x
        else:
            break

    print(nums)
          
if __name__ == '__main__':
    list_of_values = [[1,3,5,6,7,8,9,10,7,13,14,17,7,19]]
    
    for li in list_of_values:
        print(f'Input is {li}')
        selectionSort(li)