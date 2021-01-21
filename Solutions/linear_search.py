
def linearSearch(nums,number):
    print(f'Element found at {[index + 1 for index in range(len(nums)) if number == nums[index]]}')
    print(nums,number)
    
        
if __name__ == '__main__':
    list_of_values = [[[1,3,5,6,7,8,9,10,7,13,14,17,7,19],7]]
    
    for li in list_of_values:
        print(f'Input is {li[0]} and number is {li[1]}')
        linearSearch(*li)