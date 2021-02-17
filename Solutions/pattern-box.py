def boxpattern(row,column):
    # SOlution 1
    # for x in range(row):
    #     for y in range(column):
    #         if x in [0,row-1] or y in [0,column-1]:
    #             print('*',end = '')
    #         else:
    #             print(' ',end='')
    #     print()

    # Solution 2
    x,y = 0,0
    while True:
        if x < row:
            if y < column:
                if x in [0, row - 1] or y in [0, column - 1]:
                    print('*', end='')
                else:
                    print(' ', end='')
                y = y + 1
            else:
                x = x + 1
                y = 0
                print()
        else:
            break

for value in [[5,5]]:
    print(f'Input is {value}')
    boxpattern(*value)