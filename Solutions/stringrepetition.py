import re
def stringRepetition(nums):
    alpha = re.findall(r'[a-z]+',nums)
    digits = re.findall(r'[0-9]+',nums)
    for x in range(len(digits)):
        print(alpha[x] * int(digits[x]),end='')
    print(''.join(alpha[len(digits):]))

if __name__ == '__main__':
    values = ['ha12','a1b4cae10b']
    for value in values:
        print(f'Input is {value}')
        stringRepetition(value)

    

