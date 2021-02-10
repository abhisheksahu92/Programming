# Longest Repeating Subsequence

# Given a string str, find length of the longest repeating subseequence such that the two subsequence don’t have same string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.
 

# Exampel 1:

# Input: str = "axxxy"
# Output: 2
# Explanation: The longest repeating subsequenece
# is "xx".

def LongestRepeatingSubsequence(str1):
    longest_count = 0
    count = 0
    for x in range(len(str1)-1):
        if str1[x] == str1[x+1]:
            count = count + 1
        else:
            if count > longest_count:
                longest_count = count
            count = 0
            
    if count > longest_count:
        longest_count = count
    print(longest_count)

for value in ['axxxy','aab','axxxyxxxxxx']:
    print(f'Input is {value}')
    LongestRepeatingSubsequence(value)