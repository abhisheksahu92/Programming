def anagram(str1,str2):
    # Solution 1
    # d = {}
    # for x in str1:
    #     d[x] = d.get(x,0) + 1
    # for x in str2:
    #     d[x] = d.get(x,0) - 1
    # return all(list(map(lambda x : x == 0,d.values())))
    # SOlution 2
    if len(str1) != len(str2):
        return False
    a,b =0,0
    for x in range(len(str1)):
        a += ord(str1[x])
        b += ord(str2[x])
    if a == b:
        return True


for value in [['doog','good']]:
    print(f'Input is {value}')
    print(anagram(*value))