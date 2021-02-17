# Given a binary string, that is it contains only 0s and 1s. We need to make this string a sequence of alternate characters by flipping some of the bits, our goal is to minimize the number of bits to be flipped.
# Examples:
#
# Input : str = “001”
# Output : 1
# Minimum number of flips required = 1
# We can flip 1st bit from 0 to 1
#
# Input : str = “0001010111”
# Output : 2
# Minimum number of flips required = 2
# We can flip 2nd bit from 0 to 1 and 9th
# bit from 1 to 0 to make alternate
# string “0101010101”.

def minFlip(str1):
    start = '0'
    flip_x = 0
    for x in range(len(str1)):
        if str1[x] != start:
            flip_x += 1
            start = '1' if start == '0' else '0'
        else:
            start = '1' if start == '0' else '0'

    expected = '1'
    flip_y = 0
    for y in range(len(str1)):
        if str1[x] != expected:
            flip_y += 1
            expected = '1' if expected == '0' else '0'
        else:
            expected = '1' if expected == '0' else '0'
    return flip_x if flip_x < flip_y else flip_y

for value in ['001','0001010111','01010']:
    print(f'Input is {value}')
    print(minFlip(value))