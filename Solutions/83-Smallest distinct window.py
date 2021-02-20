# Smallest distinct window

# Given a string 's'. The task is to find the smallest window length that contains all the characters of the given string at least one time.
# For eg. A = “aabcbcdbca”, then the result would be 4 as of the smallest window will be “dbca”.
#
#
#
# Example 1:
#
# Input : "AABBBCBBAC"
# Output : 3
# Explanation : Sub-string -> "BAC"
#
# Example 2:
#
# Input : "aaab"
# Output : 2
# Explanation : Sub-string -> "ab"

def findSubString(str1):
    s = ''.join(set(str1))
    length = len(s)
    for x in range(len(str1)-length + 1):
        value = str1[x:x+length]
        if sorted(value) == sorted(s):
            return value

for value in ['AABBBCBBAC','aaab']:
    print(f'Input is {value}')
    print(findSubString(value))