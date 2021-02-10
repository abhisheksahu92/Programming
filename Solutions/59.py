# Split the binary string into substrings with equal number of 0s and 1s
# Given a binary string str of length N, the task is to find the maximum count of substrings str can be divided into such that all the substrings are balanced i.e. they have equal number of 0s and 1s. If it is not possible to split str satisfying the conditions then print -1.
#
# Example:
#
#     Input: str = “0100110101”
#     Output: 4
#     The required substrings are “01”, “0011”, “01” and “01”.
#
#     Input: str = “0111100010”
#     Output: 3

def maxSubStr(nums):
    count0 = 0
    count1 = 0
    cnt = 0
    for x in nums:
        if x == '0':
            count0 = count0 + 1
        else:
            count1 = count1 + 1
        if count0 == count1:
            cnt += 1
    print(cnt)

for value in ['0100110101','0111100010']:
    print(f'Input is {value}')
    maxSubStr(value)