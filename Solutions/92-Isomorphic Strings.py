# Isomorphic Strings

# Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.
# Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible for every character of str1 to every character of str2 while preserving the order.
# Note: All occurrences of every character in ‘str1’ should map to the same character in ‘str2’
#
# Example 1:
#
# Input:
# str1 = aab
# str2 = xxy
# Output: 1
# Explanation: There are two different
# charactersin aab and xxy, i.e a and b
# with frequency 2and 1 respectively.

# Example 2:
#
# Input:
# str1 = aab
# str2 = xyz
# Output:
# Explanation: There are two different
# charactersin aab but there are three
# different charactersin xyz. So there
# won't be one to one mapping between
# str1 and str2.
from collections import OrderedDict
def areIsomorphic(str1,str2):
    d1 = OrderedDict()
    d2 = OrderedDict()
    for x in str1:
        d1[x] = d1.get(x,0) + 1
    for x in str2:
        d2[x] = d2.get(x,0) + 1

    return list(d1.values()) == list(d2.values())

for value in [['aab','xxy'],['aab','xyz']]:
    print(f'Input is {value}')
    print(areIsomorphic(*value))