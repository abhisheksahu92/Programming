# Trapping Rain Water

# Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
 

# Example 1:

# Input:
# N = 6
# arr[] = {3,0,0,2,0,4}
# Output:
# 10

# Input:
# N = 4
# arr[] = {7,4,0,9}
# Output:
# 10
# Explanation:
# Water trapped by above 
# block of height 4 is 3 units and above 
# block of height 0 is 7 units. So, the 
# total unit of water trapped is 10 units.

# Input:
# N = 3
# arr[] = {6,9,9}
# Output:
# 0
# Explanation:
# No water will be trapped.

def trappingWater(nums):
    total_water = 0
    x = 0
    y = 1
    while True:
        if x < len(nums):
            if y < len(nums):
                print(nums[x],nums[y]) 
                print(total_water)
                if nums[x] < nums[y]:
                    if y != len(nums) - 1:
                        print(nums[y+1:])
                        if nums[x] < max(nums[y+1:]):
                            x = y
                        else:
                            x = nums.index(max(nums[y+1:]))
                else:
                    total_water = total_water + (nums[x] - nums[y])
                y = y + 1
            else:
                break
        else:
            break
    print(total_water)

if __name__ == '__main__':
    value = [[3,0,0,2,0,4],[6,9,9],[7,4,0,9],[3,0,0,5,0,4,3,0,6]]
    for input in value:
        print(f'Input is {input}')
        trappingWater(input)