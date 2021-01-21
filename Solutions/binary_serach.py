
def binarysearch(nums,number):   
    mini = 0
    maxi = len(nums)
    found = False

    while mini < maxi:
        mid = (maxi + mini) // 2
        if nums[mid] == number:
            print(f'Element found at {mid+1}')
            found = True
            break
        else:
            if nums[mid] < number:
                mini = mid
            else:
                maxi = mid
    if not found:
        print('Element not found')
        
if __name__ == '__main__':
    list_of_values = [[[1,3,5,6,7,8,9,10,13,14,17,19],7]]
    
    for li in list_of_values:
        print(f'Input is {li[0]} and number is {li[1]}')
        binarysearch(*li)