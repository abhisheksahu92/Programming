# Longest Prefix Suffix
# Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.
#
# Example 1:
#
# Input: s = "abab"
# Output: 2
# Explanation: "ab" is the longest proper
# prefix and suffix.
#
# Example 2:
#
# Input: s = "aaaa"
# Output: 3
# Explanation: "aaa" is the longest proper
# prefix and suffix.

def longestPrefixSuffix(str1):
    count = 0
    for x in range(1,len(str1)):
        if str1[0:x] == str1[-x:]:
            if count < x:
                count = x
    return count

for value in ['abab','aaaa']:
    print(f'Input is {value}')
    print(longestPrefixSuffix(value))