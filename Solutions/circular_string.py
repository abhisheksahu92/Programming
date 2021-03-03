def Circular_str(N, S1, M, S2):
    print(S2 + S2)
    entry = False
    start = 0
    l = []
    for x in S2:
        if x in S1:
            pass
        else:
            l.append(x)

    print(l)
    l.extend(list(S1))
    l.sort(reverse=True)
    print(print(''.join(l)))

Circular_str(3,'abc',5,'acdef')