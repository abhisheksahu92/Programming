# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(li):
    s = ''
    for x in range(len(min(li,key=len))):
        if li[0][x] != li[1][x] or li[0][x] != li[2][x]:
            return s
        else:
            s += li[0][x]
    return s

for value in [["flower","flow","flight"],["dog","racecar","car"]]:
    print(f'Input is {value}')
    print(longestCommonPrefix(value))