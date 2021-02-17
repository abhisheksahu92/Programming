# Roman Number to Integer
# Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000

# Input:
# s = V
# Output: 5

# Input:
# s = III
# Output: 3

def romanToDecimal(str1):
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    for x in range(len(str1)):
        try:
            left = str1[x]
            right = str1[x+1]
            if d[left] < d[right]:
                total -= d[left]
            else:
                total += d[left]
        except:
            total += d[left]
    return total

for value in ['V','III','IV','XXIV','LC','XL']:
    print(f'Input is {value}')
    print(romanToDecimal(value))