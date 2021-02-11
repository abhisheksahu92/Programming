# A Program to check if strings are rotations of each other or not

# Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?
# (eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)

def areRotations(str1,str2):
    str1 = str1 + str1
    if str2 in str1:
        return True
    return False

values = [['ABCD','CDAB'],['ABCD','ACBD']]
for value in values:
    print(f'Input is {value}')
    print(areRotations(*value))