# Palindrome String 
# Given a string S, check if it is palindrome or not.

# Example 1:

# Input: S = "abba"
# Output: 1
# Explanation: S is a palindrome

# Example 2:

# Input: S = "abc" 
# Output: 0
# Explanation: S is not a palindrome

def isPlaindrome(nums):
    if nums == nums[::-1]:
        return '1'
    return '0'

values = ['abba','abc']
print('\n'.join(list(map(isPlaindrome,values))))
