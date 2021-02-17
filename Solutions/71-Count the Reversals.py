# Given a string S consisting only of opening and closing curly brackets '{' and '}' find out the minimum number of reversals required to make a balanced expression.
#
# Input
# The first line of input contains an integer T, denoting the number of test cases. Then T test cases
# follow. The first line of each test case contains a string S consisting only of { and }.
#
# Output
# Print out minimum reversals required to make S balanced. If it cannot be balanced, then print -1.

#Constraints
# 1 <= T <= 100
# 0 <= |S| <= 50
#
# Examples
# Input
# 4
# }{{}}{{{
# {{}}}}
# {{}{{{}{{}}{{
# {{{{}}}}
#
# Output
# 3
# 1
# -1
# 0
from math import ceil


def countReversal(pattern):
    count = 0
    reverse = 0
    total = 0
    if len(pattern) % 2 != 0:
        return -1

    for x in pattern:
        if x == '{':
            count +=1
        else:
            if count > 0:
                count -= 1
            else:
                if reverse > 0:
                    total += 1
                    reverse -= 1
                else:
                    reverse += 1

    print(reverse+ total + ceil(count/2))




for value in ['}{{}}{{{','{{}}}}','{{}{{{}{{}}{{','{{{{}}}}']:
    print(f'Input is {value}')
    print(countReversal(value))