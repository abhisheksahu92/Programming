# Edit Distance

# Given two strings s and t. Find the minimum number of operations that need to be performed on str1 to convert it to str2. The possible operations are:
#
#     Insert
#     Remove
#     Replace

# Example 1:
#
# Input:
# s = "geek", t = "gesrfk"
# Output: 1
# Explanation: One operation is required
# inserting 's' between two 'e's of str1.

# Input :
# s = "gfg", t = "gfg"
# Output:
# 0
# Explanation: Both strings are same.

def editDistance(str1,str2):
    total = 0
    if len(str1) < len(str2):
        # Insert or Resplace
        insert = len(str2) - len(str1)
        total += insert
        s = set(str1)
        for x in s:
            if str1.count(x) == str2.count(x):
                pass
            else:
                total += 1
        return total
    elif len(str1) > len(str2):
        #Remove or Replace
        s = set(str1)
        for x in s:
            if str1.count(x) == str2.count(x):
                pass
            else:
                total += 1
        return total
    else:
        # Same or repalce
        if str2 == str1:
            return 0
        for x in range(len(str1)):
            if str2[x] == str1[x]:
                pass
            else:
                total +=1
        return total
    print(str1,str2)

for value in [['geek','gesek'],['gesfk','geek'],['gfg','gfg'],['gfg','fgg']]:
    print(f'Input is {value}')
    print(editDistance(*value))
