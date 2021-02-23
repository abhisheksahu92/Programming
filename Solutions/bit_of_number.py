def bits(nums):
    l = []
    b = ''
    while nums > 0:
        if nums % 2 == 0:
            b += '0'
        else:
            b += '1'
        nums = nums // 2
    print(f'Output is :{b[::-1]}')

for value in [5, 2, 3, 9, 4, 6, 7, 15, 32]:
    print(f'Input is {value}',end=' ')
    bits(value)