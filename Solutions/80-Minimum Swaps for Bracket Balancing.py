# Minimum Swaps for Bracket Balancing
# You are given a string of 2N characters consisting of N ‘[‘ brackets and N ‘]’ brackets. A string is considered balanced if it can be represented in the for S2[S1] where S1 and S2 are balanced strings. We can make an unbalanced string balanced by swapping adjacent characters. Calculate the minimum number of swaps necessary to make a string balanced.

# Input  : []][][
# Output : 2
# First swap: Position 3 and 4
# [][]][
# Second swap: Position 5 and 6
# [][][]
#
# Input  : [[][]]
# Output : 0
# String is already balanced.

def minSwap(pattern):
    pattern = list(pattern)
    return pattern

for value in ['[]][][','[[][]]']:
    print(f'Input is {value}')
    print(minSwap(value))