# Print Anagrams Together
# Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.
#
#
# Example 1:
#
# Input:
# N = 5
# words[] = {act,god,cat,dog,tac}
# Output:
# god dog
# act cat tac
# Explanation:
# There are 2 groups of
# anagrams "god", "dog" make group 1.
# "act", "cat", "tac" make group 2.
#
# Example 2:
#
# Input:
# N = 3
# words[] = {no,on,is}
# Output:
# no on
# is
# Explanation:
# There are 2 groups of
# anagrams "no", "on" make group 1.
# "is" makes group 2.

def Anagrams(strlis):
    d = {}
    for x in strlis:
        y = ''.join(sorted(x))
        if y not in d:
            d[y] = [x]
        else:
            d[y].append(x)
    for v in d.values():
        print(' '.join(v))

for value in [['act','god','cat','dog','tac'],['no','on','is']]:
    print(f'Input is {value}')
    Anagrams(value)