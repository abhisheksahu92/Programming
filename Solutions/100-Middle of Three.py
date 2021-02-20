# Middle of Three
# Given three distinct numbers A, B and C. Find the number with value in middle (Try to do it with minimum comparisons).
# Example 1:
#
# Input:
# A = 978, B = 518, C = 300
# Output:
# 518
# Explanation:
# Since 518>300 and 518<978, so
# 518 is the middle element.
# Example 2:
#
# Input:
# A = 162, B = 934, C = 200
# Output:
# 200
# Exaplanation:
# Since 200>162 && 200<934,
# So, 200 is the middle element.

def middle(a,b,c):
    if a > b and a < c:
        return a
    elif b > a and b < c:
        return b
    else:
        return c

for value in [[978,518,300],[162,934,200]]:
    print(f'Input is {value}')
    print(middle(*value))
