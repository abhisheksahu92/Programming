# Longest Palindrome in a String 

# Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index ).
# NOTE: Required Time Complexity O(n2).
# Input:
# The first line of input consists number of the testcases. The following T lines consist of a string each.
# Output:
# In each separate line print the longest palindrome of the string given in the respective test case.

# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ Str Length ≤ 104

# Example:
# Input:
# 1
# aaaabbaa

# Output:
# aabbaa

# Explanation:
# Testcase 1: The longest palindrome string present in the given string is "aabbaa". 


def longest_palindrome(str1):
    s = ''
    for x in range(len(str1)):
        new_string = str1[x:]
        if new_string == new_string[::-1]:
            if len(s) < len(new_string):
                s = new_string
    print(s)

longest_palindrome('aaaabbaa')