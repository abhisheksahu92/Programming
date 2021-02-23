def remove_rep(str1):
    d = {}
    for x in str1:
        if x != ' ':
            if x not in d:
                print(x,end='')
                d[x] = ''
            else:
                pass
        else:
            print(x,end='')
            d = {}


for value in ['Thiiissss boooookkk isss sooooo ggggoooodddd']:
    print(f'Value is {value}')
    remove_rep(value)