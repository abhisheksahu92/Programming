# Remove Consecutive Characters
# Given a string S delete the characters which are appearing more than once consecutively.
#
# Example 1:
#
# Input:
# S = aabb
# Output:  ab
# Explanation: 'a' at 2nd position is
# appearing 2nd time consecutively.
# Similiar explanation for b at
# 4th position.
#
# Example 2:
#
# Input:
# S = aabaa
# Output:  aba
# Explanation: 'a' at 2nd position is
# appearing 2nd time consecutively.
# 'a' at fifth position is appearing
# 2nd time consecutively.

def removeConsecutiveCharacter(str1):
    s = [0]
    for x in str1:
        if s[-1] != x:
            s.append(x)
    return ''.join(s[1:])

for value in ['aabb','aabaa']:
    print(f'Input is {value}')
    print(removeConsecutiveCharacter(value))