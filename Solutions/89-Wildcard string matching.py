# Wildcard string matching
# Given two strings where first string may contain wild card characters and second string is a normal string. Write a function that returns true if the two strings match. The following are allowed wild card characters in first string.
#
# * --> Matches with 0 or more instances of any character
#       or set of characters.
# ? --> Matches with any one character.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two strings, a string with wildcard and one without.
#
# Output:
# Print "Yes" (without quotes) if the two strings match else print "No" (without quotes).

# Example:
# Input:
# 2
# ge*ks
# geeks
# ge?ks*
# geeksforgeeks
#
# Output:
# Yes
# Yes
import re

def wildcardmatch(str1,str2):
    #Solution 1

    # if re.match(str1.replace('?','.'),str2):
    #     return 'Yes'

    #Solution 2
    s = ''
    x = 0
    y = 0
    while True:
        if x < len(str1):
            if y < len(str2):
                print(str1[x],str2[y])
                if str1[x] == str2[y]:
                    s = s + str2[y]
                    x = x + 1
                    y = x
                else:
                    if str1[x] == '?':
                        s += str2[y]
                        x += 1
                        y = x - 1
                    else:
                        if x == len(str1) - 1:
                            s += str2[y:]
                            break
                        else:
                            if str1[x+1] != str2[y]:
                                s += str2[y]
                                x += 1
                                y = x - 1
                    y = y + 1
            else:
                x = x + 1
                y = x
        else:
            break
    return 'Yes' if s == str2 else 'No'


for value in [['ge*ks','geeeeeeks'],['ge?ks*','geeksforgeeks']]:
    print(f'Input is {value}')
    print(wildcardmatch(*value))