def sequence(numbers):
    l = []
    result = 0
    for x in numbers:
        small = 0
        large = 0
        for y in l:
            if y < x:
                small += 1
            elif y > x:
                large += 1
            else:
                pass
        l.append(x)
        l.sort()
        vari = small if large >= small else large
        result += vari * 2 + 1
        print(l, x,result)
    return result
l = [15,9,8,4,9,28,21,24,18,29,25,9,3,19,5,3]
print(sequence(l))