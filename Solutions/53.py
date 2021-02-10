# Print all the duplicates in the input string
# Write an efficient program to print all the duplicates and their counts in the input string 
# Algorithm: Let input string be “geeksforgeeks” 
# 1: Construct character count array from the input string.
# count[‘e’] = 4 
# count[‘g’] = 2 
# count[‘k’] = 2 

def countDuplicate(nums):
    d = {}
    for c in nums:
        d[c] = d.get(c,0) + 1
    print(d)
 
values = ['geeksforgeeks','teststring']
for value in values:
    print(f'Input is {value}')
    countDuplicate(value)