# Longest Common Subsequence

# Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.
#
# Example 1:
#
# Input:
# A = 6, B = 6
# str1 = ABCDGH
# str2 = AEDFHR
# Output: 3
# Explanation: LCS for input Sequences
# “ABCDGH” and “AEDFHR” is “ADH” of
# length 3.

# Input:
# A = 3, B = 2
# str1 = ABC
# str2 = AC
# Output: 2
# Explanation: LCS of "ABC" and "AC" is
# "AC" of length 2.

def lcs(str1,str2):
    x = 0
    y = 0
    count = 0
    while True:
        if x < len(str1):
            if y < len(str2):
                if str1[x] == str2[y]:
                    count += 1
                    x = x + 1
                y = y  + 1
            else:
                x = x + 1
                y = 0
        else:
            break
    return count

for value in [['ABCDGH','AEDFHR'],['ABC','AC']]:
    print(f'Input is {value}')
    print(lcs(*value))
