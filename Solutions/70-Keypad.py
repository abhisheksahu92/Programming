# Convert a sentence into its equivalent mobile numeric keypad sequence

# Input : GEEKSFORGEEKS
# Output : 4333355777733366677743333557777
# For obtaining a number, we need to press a
# number corresponding to that character for
# number of times equal to position of the
# character. For example, for character C,
# we press number 2 three times and accordingly.
#
# Input : HELLO WORLD
# Output : 4433555555666096667775553

import string
def keypadSequence(str1):
    d = {}
    alphabet = list(string.ascii_uppercase)
    start = 0
    end = 3
    for x in range(2,10):
        if x not in [7,9]:
            for a,b in enumerate(alphabet[start:end]):
                d[b] = str(x) * (a+1)
            start += 3
            end += 3
        else:
            for a, b in enumerate(alphabet[start:end+1]):
                d[b] = str(x) * (a+1)
            start += 4
            end += 4
    for x in str1:
        if x in d:
            print(d[x],end='')
        else:
            print(0,end='')
    print('\n')


for value in ['GEEKSFORGEEKS','HELLO WORLD']:
    print(f'Input is {value}')
    keypadSequence(value)